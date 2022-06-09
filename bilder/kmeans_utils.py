from numpy.random import default_rng
from numpy.linalg import norm

import matplotlib.pyplot as plt
import numpy as np

# Zufallszahlengenerator mit "seed=1"
rng = default_rng(1)


def get_labels(datamatrix, centroids=None):
    ''' find the nearest of given centroids for data

    Parameters
    ----------
    datamatrix: (N, n) array
        the data of N data points with n features each
    centroids: list
        of K centroid coordinates of shape (1, n) each
    '''

    listofdiffs = []
    Ndata = datamatrix.shape[0]
    for cj in centroids:
        cjdiff = norm(datamatrix-cj, axis=1)
        listofdiffs.append(cjdiff.reshape((Ndata, 1)))
    arrayofdiffs = np.hstack(listofdiffs)  # better for computing and indexing
    clabels = np.argmin(arrayofdiffs, axis=1)
    vecoferrs = np.min(arrayofdiffs, axis=1)
    clstrerror = norm(vecoferrs)  # the clustering error
    return clabels, clstrerror


def get_centers(datamatrix, K=None, labels=None):
    ''' compute centroids for given clusters

    Parameters
    ----------
    datamatrix: (N, n) numpy array
        the data of N data points with n features each
    labels: list
        of labels that associate data points with clusters
    K: int
        number of clusters
    '''

    newcntrds = []
    for clstr in range(K):
        if (labels == clstr).sum() > 0:
            dataincj = datamatrix[labels == clstr, :]
            newcj = np.mean(dataincj, axis=0)
            newcntrds.append(newcj)
        else:
            # if no points in cluster -- use random datapoint as centroid
            rnddidx = np.random.randint(datamatrix.shape[0])
            newcntrds.append(datamatrix[rnddidx, :])

    return newcntrds


def kmeans(datamatrix, K, maxiter=10, itertol=1e-10, cntrdlist=None):
    ''' compute clusters for data by k-means

    Parameters
    ----------
    datamatrix: (N, n) numpy array
        the data of N data points with n features each
    K: int
        number of clusters
    maxiter: int, optional
        max number of iterations, defaults to 10
    itertol: float, optional
        tolerance to terminate the iteration, defaults to 1e-10
    cntrdlist: list, optional
        of coordinates to be used as initial cluster
    '''

    clabels, olderror = get_labels(datamatrix, centroids=cntrdlist)
    # here we need the iteration that does the kmeans clustering

    return cntrdlist, clabels, newerror


def plot_cluster_data(datamatrix, labels, cntrdlist,
                      xlabel='feature', ylabel='other feature',
                      fignum=10101, figsize=(5, 4), titlestr='Clustering'):
    plt.figure(fignum, figsize=figsize)

    # Set the colors for the plots
    clm = np.linspace(0.2, 0.8, len(cntrdlist))
    plt.rcParams["axes.prop_cycle"] = \
        plt.cycler("color", plt.cm.plasma(clm))
    # done setting colors

    for kkk in range(len(cntrdlist)):
        cdata = datamatrix[labels == kkk, :]
        plt.plot(cdata[:, 0], cdata[:, 1], '.', alpha=.7)
    for kkk in range(len(cntrdlist)):
        plt.plot(cntrdlist[kkk][0], cntrdlist[kkk][1],
                 's', label=f'$c_{kkk+1}$')

    plt.title(titlestr)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='upper left')
    plt.legend()
    plt.tight_layout()
    plt.show(block=False)
    return


if __name__ == '__main__':
    # N = 99
    # K = 4
    N = 9
    K = 2

    x = rng.beta(1, 1, N)
    y = rng.beta(1, 1, N)
    z = (x*x*y)**(1/3)

    cntro = rng.beta(1, 1, 2)
    cntrt = rng.beta(1, 1, 2)

    plt.figure(1, figsize=(5, 3))
    plt.plot(x, z, '.', label='data')
    plt.plot(cntro[0], cntro[1], 's', label='$c_1$')
    plt.plot(cntrt[0], cntrt[1], 's', label='$c_2$')
    plt.legend(loc='upper left')
    plt.title('K-means: initialer Zustand')

    plt.figure(2, figsize=(5, 3))
    plt.plot(x, z, '.', label='data')
    plt.plot(np.NaN, np.NaN, 's', label='$c_1$')
    plt.plot(np.NaN, np.NaN, 's', label='$c_2$')
    plt.legend(loc='upper left')
    plt.title('K-means: ... Zustand')

    cntrdlist = [cntro, cntrt]
    datamatrix = np.hstack([x.reshape((x.size, 1)), z.reshape((z.size, 1))])

    # cntrdlist, labels, cerror = kmeans(datamatrix, K=2, cntrdlist=cntrdlist)
    cntrdlist, labels, cerror = kmeans(datamatrix, K=K)

    plot_cluster_data(datamatrix, labels, cntrdlist,
                      xlabel='feature', ylabel='other feature',
                      fignum=10101, figsize=(5, 4),
                      titlestr='K-means: finaler Zustand')

    plt.show()
