
def plot_bar(X, Y, labels=['x', 'y'], xticks=None, legend=None):
    """Plot histograms

    :param X: x values
    :type X: list (of doubles)
    :param Y: y values
    :type Y: list (of doubles)
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
