import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def draw_plot(df, filename):

    x = df['x']
    y = df['y']

    # fit with np.polyfit
    m, b = np.polyfit(x, y, 1)

    plt.plot(x, y, '.')
    plt.plot(x, m*x + b, '-')
    plt.savefig(filename)   # save the figure to file
    plt.close()


def import_data(filename):

    df = pd.read_csv(filename, sep=';', decimal=',')
    return df


if __name__ == '__main__':

    draw_plot(import_data('../data/theorie/korellation_r+1.csv'), '../img/r+1.png')
    draw_plot(import_data('../data/theorie/korellation_r-1.csv'), '../img/r-1.png')
    draw_plot(import_data('../data/theorie/korellation_r+0.9.csv'), '../img/r+0.9.png')
    # draw_plot(import_data('../data/theorie/korellation_r-0.9.csv'), '../img/r-0.9.png')
    draw_plot(import_data('../data/theorie/korellation_r+0.55.csv'), '../img/r+0.55.png')
    # draw_plot(import_data('../data/theorie/korellation_r-0.55.csv'), '../img/r-0.55.png')
    draw_plot(import_data('../data/theorie/korellation_r+0.2.csv'), '../img/r+0.2.png')
    # draw_plot(import_data('../data/theorie/korellation_r-0.2.csv'), '../img/r-0.2.png')
