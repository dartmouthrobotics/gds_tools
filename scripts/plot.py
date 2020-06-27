import os
import math
import re
import cv2
import sys
import roslaunch
import subprocess
import time
import numpy
from matplotlib import pyplot, cm
import entropy_estimators as ee
import yaml

import itertools

# Set font for matplotlib figures
#pyplot.rc('font', **{'size': 30})
pyplot.rc('legend', **{'fontsize': 24})
pyplot.rc('axes', **{'labelsize': 24})
pyplot.rc('xtick', **{'labelsize': 24})
pyplot.rc('ytick', **{'labelsize': 24})

# Scenario
environments = ["test_environment_similarities", "map_turtlebot", "cave", "map_turtlebot_real", "usc-sal200-021120", "fr101", "sdr_site_b"]


# INPUT

num_repetitions = 5
num_robots = [8,24,48]
ENV = [environments[0], environments[2], environments[4], environments[5], environments[6]]
methods = ["informed", "random goal", "furthest", "random_walk"]

"""
num_repetitions = 1
num_robots = [12]
ENV = [environments[1]]
methods = ["informed"]
"""

root_path = "/home/alberto/DATA/experiments/dynamic_obstacles_localization/logs_batch/final/"

logs_path = root_path
yaml_extension = ".yaml"
world_extension = ".world"
marker = itertools.cycle(('^', '+', 'd', 'o', '*'))

consider_angle = True

legend_location = 'upper center'
legend_bbox_to_anchor = (0.5, -0.12)

legend_location0='center right'
legend_bbox_to_anchor0=(1.1, 0.5)

def plot_bar(Y_mean, Y_std, labels=['x', 'y'], xticks=None, legend=None):
    """Plot histograms

    :param Y_mean: y value (mean)
    :type Y_mean: list (of lists of double, according to strategy)
    :param Y_std: y value (std)
    :type Y_std: list (of lists of double)
    :param labels: axes labels
    :type labels: list (of strings)
    :param legend: legend
    :type legend: list (of strings)

    """
    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    width = 0.35 # TODO Parameter
    separator = 0.5 # TODO Parameter

    cmap = cm.jet # TOCHECK

    p = []
    X = []

    # Plot bars for each strategy
    for i, (y_mean, y_std) in enumerate(zip(Y_mean, Y_std)):
        jump = len(Y_mean)*width+separator
        start_point = i*width
        end_point = start_point + (len(y_mean)-1)*jump+width
        x = numpy.arange(start_point, end_point, jump)
        tmp_p = ax.bar(x, y_mean, width, color=cmap(1.*i/len(Y_mean)),
                                            yerr=y_std, error_kw={'linewidth':4})
        p.append(tmp_p)
        X.append(x)

    # Add x and y labels
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])

    ax.grid()

    # Add x labels to groups of bars
    if xticks != None:
        pyplot.xticks(X[int(numpy.floor(len(X)/2))]+width/2., tuple(xticks) )

    # Add legend
    if legend != None:
        legend_1 = ax.legend(tuple(p[0:2]), tuple(legend[0:2]),
          loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, ncol=len(legend[0:2]))

        ax.add_artist(legend_1)

        legend_2 = ax.legend(tuple(p[2:]), tuple(legend[2:]),
          loc=legend_location, bbox_to_anchor=(0.5, -0.25), ncol=len(legend[2:]))
    else:
        legend_1 = None
        legend_2 = None
    return fig, (legend_1, legend_2)


def plot_errorbar(X, Y, Y_std, labels=['x', 'y'], legend=None):
    """Plot errorbar

    :param X: x values associated to each y values in Y_mean
    :type X: list (of lists of double)
    :param Y_mean: y value (mean)
    :type Y_mean: list (of lists of double)
    :param Y_std: y value (std)
    :type Y_std: list (of lists of double)
    :param labels: axes labels
    :type labels: list (of strings)
    :param legend: legend
    :type legend: list (of strings)

    """
    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    #pyplot.ylim(0, 400)
    for i, x in enumerate(X):
        try:
            min_len = min(len(x), len(Y[i]))
            print Y_std[i][:min_len]
            ax.errorbar(x[:min_len], Y[i][:min_len], Y_std[i][:min_len], linewidth=4.0, marker=marker.next(), markersize=8)
        except:
            print "error in plot_errorbar", x[:min_len], Y[i][:min_len], Y_std[i][:min_len]
            return

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])

    ax.grid()

    if legend != None:
        legend_1 = ax.legend(legend,
          loc=legend_location0, bbox_to_anchor=legend_bbox_to_anchor0)
        """
        legend_1 = ax.legend(legend[0:2],
          loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, ncol=len(legend[0:2]))

        ax.add_artist(legend_1)

        legend_2 = ax.legend(legend[2:],
          loc=legend_location, bbox_to_anchor=(0.5, -0.25), ncol=len(legend[2:]))
        """
    else:
        legend_1 = None
        legend_2 = None
    return fig, (legend_1, )

def plot_curve(X, Y, labels=['x', 'y'], legend=None):
    """Plot errorbar

    :param X: x values associated to each y values in Y_mean
    :type X: list (of lists of double)
    :param Y: y value (mean)
    :type Y: list (of lists of double)
    :param labels: axes labels
    :type labels: list (of strings)
    :param legend: legend
    :type legend: list (of strings)

    """
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.hold(True)

    #pyplot.ylim(0, 400)

    for i, x in enumerate(X):
        try:
            min_len = min(len(x), len(Y[i]))
            ax.plot(x[:min_len], Y[i][:min_len], linewidth=4.0, marker=marker.next(), markersize=8)
        except:
            return

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])

    ax.grid()

    if legend != None:
        legend_1 = ax.legend(legend,
          loc=legend_location0, bbox_to_anchor=legend_bbox_to_anchor0)
        """
        legend_1 = ax.legend(legend[0:2],
          loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, ncol=len(legend[0:2]))

        ax.add_artist(legend_1)

        legend_2 = ax.legend(legend[2:],
          loc=legend_location, bbox_to_anchor=(0.5, -0.25), ncol=len(legend[2:]))
        """
    else:
        legend_1 = None
        legend_2 = None

    return fig, (legend_1, )


def save_graph(fig, filename, filetype='.png', legend=None):
    """Save figure to file

    :param fig: figure to be saved
    :type fig: matplotlib Figure
    :param filename: filename of output file
    :type filename: str
    """


    """if filetype == '.pdf':
        #TOCHECK is it still useful?
        with PdfPages(filename+filetype) as pdf:
            # Adjust fig size to make room for axes labels
            # TODO Adjust size to fit legend
            pyplot.tight_layout()

            pdf.savefig(fig, bbox_extra_artists=(legend,))

            pyplot.close()
    else:        """
    if legend !=None:
        fig.savefig(filename+filetype, bbox_extra_artists=legend, bbox_inches='tight')
    else:
            fig.savefig(filename+filetype, bbox_inches='tight')


def plotting_bars():
    for j, env in enumerate(ENV):
        print env
        avg_final_distance = [[] for c in range(len(methods))]
        std_final_distance = [[] for c in range(len(methods))]
        avg_final_comp_time = [[] for c in range(len(methods))]
        std_final_comp_time = [[] for c in range(len(methods))]
        avg_final_error = [[] for c in range(len(methods))]
        std_final_error = [[] for c in range(len(methods))]
        avg_final_entropy = [[] for c in range(len(methods))]
        std_final_entropy = [[] for c in range(len(methods))]
        avg_final_success = [[] for c in range(len(methods))]
        std_final_success = [[] for c in range(len(methods))]
        avg_final_time = [[] for c in range(len(methods))]
        std_final_time = [[] for c in range(len(methods))]
        avg_final_std = [[] for c in range(len(methods))]
        std_final_std = [[] for c in range(len(methods))]
        #legend = [[] for c in range(len(methods))]
        xtick = []
        legend = methods
        for l, nr in enumerate(num_robots):
            print "nr ", nr
            xtick.append(str(nr))
            for m, method in enumerate(methods):
                tmp_final_distance = []
                tmp_final_comp_time = []
                tmp_final_error = []
                tmp_final_entropy = []
                tmp_final_num_success = []
                tmp_final_time = []
                tmp_final_std = []
                print method
                for i in range(0, num_repetitions):
                    if method == "random goal":
                        method = "random"
                    current_log_path = logs_path + '/'.join([env, str(nr), method, str(i)])

                    print "rep" , i
                    time = numpy.genfromtxt(current_log_path + '/time.txt', unpack=True)
                    distance = numpy.genfromtxt(current_log_path + '/distance.txt', unpack=True)
                    error = numpy.genfromtxt(current_log_path + '/error.txt', unpack=True)
                    try:
                        entropy = numpy.genfromtxt(current_log_path + '/entropy.txt', unpack=True)
                    except IOError:
                        logging_entropy(current_log_path)
                        entropy = numpy.genfromtxt(current_log_path + '/entropy.txt', unpack=True)
                    success = numpy.genfromtxt(current_log_path + '/localized.txt', unpack=True)
                    std = numpy.genfromtxt(current_log_path + '/std.txt', unpack=True)
                    print "SUCC", success
                    if method != "random_walk":
                        comp_time = numpy.genfromtxt(current_log_path + '/computation_time.txt', unpack=True)
                    else:
                        comp_time = 0.0

                    try:
                        tmp_final_distance.append(distance[0][len(distance[0])-1])
                        tmp_final_error.append(error[0][len(error[0])-1])
                        tmp_final_entropy.append(entropy[-1])
                        tmp_final_time.append(time[-1])
                        if method != "random_walk":
                            tmp_final_comp_time.append(comp_time[-1])
                        else:
                            tmp_final_comp_time.append(comp_time)
                        tmp_final_num_success.append(success)
                        tmp_final_std.append(std[0][len(std[0])-1])
                    except:
                        print "no value"
                avg_final_distance[m].append(numpy.mean(tmp_final_distance))
                std_final_distance[m].append(numpy.std(tmp_final_distance))
                avg_final_error[m].append(numpy.mean(tmp_final_error))
                std_final_error[m].append(numpy.std(tmp_final_error))
                avg_final_entropy[m].append(numpy.mean(tmp_final_entropy))
                std_final_entropy[m].append(numpy.std(tmp_final_entropy))
                avg_final_comp_time[m].append(numpy.mean(tmp_final_comp_time))
                std_final_comp_time[m].append(numpy.std(tmp_final_comp_time))
                avg_final_time[m].append(numpy.mean(tmp_final_time))
                std_final_time[m].append(numpy.std(tmp_final_time))

                avg_final_success[m].append(numpy.mean(tmp_final_num_success))
                std_final_success[m].append(numpy.std(tmp_final_num_success))

                avg_final_std[m].append(numpy.mean(tmp_final_std))
                std_final_std[m].append(numpy.std(tmp_final_std))
        if env != 'cave':
            legend = None
        print "plotting distance"
        fig, lgd = plot_bar(avg_final_distance, std_final_distance, ["", "average traveled distance [m]"], xtick, legend)
        save_graph(fig, '_'.join([env, "distance"]))
        fig, lgd = plot_bar(avg_final_error, std_final_error, ["", "average final error [m]"], xtick, legend)
        print "std"
        save_graph(fig, '_'.join([env, "error"]))
        fig, lgd = plot_bar(avg_final_entropy, std_final_entropy, ["", "average entropy"], xtick, legend)
        print "entropy"
        save_graph(fig, '_'.join([env, "entropy"]))
        print "comp_time"
        fig, lgd = plot_bar(avg_final_comp_time, std_final_comp_time, ["", "average computation time [s]"], xtick, legend)
        save_graph(fig, '_'.join([env, "comp_time"]))

        print "time"
        fig, lgd = plot_bar(avg_final_time, std_final_time, ["", "average completion time [s]"], xtick, legend)
        save_graph(fig, '_'.join([env, "time"]))

        print "success"
        fig, lgd = plot_bar(avg_final_success, std_final_success, ["", "average success rate"], xtick, legend)
        save_graph(fig, '_'.join([env, "success"]))

        print "std"
        fig, lgd = plot_bar(avg_final_std, std_final_std, ["", "particles standard deviation"], xtick, legend)
        save_graph(fig, '_'.join([env, "std"]))

def plotting_curves():
    for j, env in enumerate(ENV):#
        for l, nr in enumerate(num_robots):
            print env

            for i in range(0, num_repetitions):
                print "rep" , i
                distances = []
                errors = []
                errors_std = []
                comp_times = []
                entropies = []
                times = []
                legend = methods
                stds = []
                for m, method in enumerate(methods):
                    if method == "random goal":
                        method = "random"
                    current_log_path = logs_path + '/'.join([env, str(nr), method, str(i)])
                    logging_entropy(logs_path + '/'.join([env, str(nr), method, str(i)]))

                    time = numpy.genfromtxt(current_log_path + '/time.txt', unpack=True)
                    times.append(time)
                    distance = numpy.genfromtxt(current_log_path + '/distance.txt', unpack=True)
                    distances.append(distance[0])
                    error = numpy.genfromtxt(current_log_path + '/error.txt', unpack=True)
                    errors.append(numpy.sqrt(error[0]))
                    errors_std.append(numpy.sqrt(error[1]))
                    entropy = numpy.genfromtxt(current_log_path + '/entropy.txt', unpack=True)
                    entropies.append(entropy)
                    std = numpy.genfromtxt(current_log_path + '/std.txt', unpack=True)
                    stds.append(std[0])
                    print method
                    if method != "random_walk":
                        comp_time = numpy.genfromtxt(current_log_path + '/computation_time.txt', unpack=True)
                    else:
                        comp_time = numpy.zeros(len(time))
                    comp_times.append(comp_time)
                print "entropy"
                fig, lgd = plot_curve(times, entropies, ["time [s]", "particles entropy"], legend)
                save_graph(fig, '_'.join([env, "entropy_over_time", str(nr), str(i)]))
                if env != 'cave':
                    legend = None
                print "plotting distance"
                fig, lgd = plot_curve(times, distances, ["time [s]", "average traveled distance [m]"], legend)
                save_graph(fig, '_'.join([env, "distance_over_time", str(nr), str(i)]))
                print "std"
                fig, lgd = plot_errorbar(times, errors, errors_std, ["time [s]", "error wrt ground truth [m]"], legend)
                save_graph(fig, '_'.join([env, "error_over_time", str(nr), str(i)]))
                print "comp time"
                fig, lgd = plot_curve(times, comp_times, ["time [s]", "computation time [s]"], legend)
                save_graph(fig, '_'.join([env, "comp_time_over_time", str(nr), str(i)]))

                print "std"
                fig, lgd = plot_curve(times, stds, ["time [s]", "particles standard deviation"], legend)
                save_graph(fig, '_'.join([env, "std_over_time", str(nr), str(i)]))


def logging_entropy(log_path):
    if os.path.isfile(os.path.join(log_path, 'entropy.txt')):
        return
    img = cv2.imread('/home/alberto/catkin_ws/src/pf2d_localizer/worlds/test_environment_similarities/test_environment_similarities.png', 0)
    with open('/home/alberto/DATA/Dropbox/work/catkin_src/pf2d_localizer/worlds/test_environment_similarities/test_environment_similarities.yaml', 'r') as stream:
        yaml_data = yaml.load(stream)

        x_min = -img.shape[1] / 2.0 * float(yaml_data['resolution'])
        y_max = img.shape[0] / 2.0 * float(yaml_data['resolution'])

        onlyfiles = [ f for f in os.listdir(log_path) if os.path.isfile(os.path.join(log_path, f)) and "particles" in f and "txt" in f ]
        onlyfiles = sorted(onlyfiles, key=lambda f: int(os.path.splitext(f)[0].split('_')[1]))
        entropies = []
        for f in onlyfiles:
            #print onlyfiles

            particles = numpy.genfromtxt(os.path.join(log_path, f), unpack=True)


            #img = cv2.imread('/home/alberto/DATA/Dropbox/work/catkin_src/pf2d_localizer/worlds/map_turtlebot/map_turtlebot.pgm', 0)
            """
            total_weight = 0.0
            for w in particles[3]:
                total_weight += w
            for w in particles[3]:
                #print "prev ", w
                w /= total_weight
                #print "aft ", w
            bins = numpy.add.accumulate(particles[3])
            values_indices = numpy.digitize(numpy.random.random_sample(10000), bins)"""
            """for v in values_indices:
                if particles[3][v] == 0:
                    print  particles[3][v]"""
            if consider_angle:
                #particles_pair = [list(p) for p in zip(particles[0]-x_min/float(yaml_data['resolution']), (y_max-particles[1])/float(yaml_data['resolution']), particles[2]/3.14*180+180)] # TODO weight
                particles_pair = [list(p) for p in zip(particles[0], particles[1], particles[2])] # TODO weight
                #particles_pair = [list([particles[0][v]-x_min/float(yaml_data['resolution']), (y_max-particles[1][v])/float(yaml_data['resolution']), particles[2][v]/3.14*180+180]) for v in values_indices if particles[3][v] > 0.000001] # TODO weight
            else:
                #particles_pair = [list(p) for p in zip(particles[0]-x_min/float(yaml_data['resolution']), (y_max-particles[1])/float(yaml_data['resolution']))]
                particles_pair = [list(p) for p in zip(particles[0], particles[1])] # TODO weight
                #particles_pair = [list([particles[0][v-1]-x_min/float(yaml_data['resolution']), (y_max-particles[1][v-1])/float(yaml_data['resolution'])]) for v in values_indices if particles[3][v-1] > 0.0001]

            entropies.append(ee.entropy(particles_pair))

        with open(os.path.join(log_path, 'entropy.txt'), 'w') as f: # TODO parameter
            for e in entropies:
                f.write(str(e) + '\n')


plotting_bars()
plotting_curves()
