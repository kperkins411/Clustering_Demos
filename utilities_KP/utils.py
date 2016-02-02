
import numpy as np
import utilities_KP.utils_plot as utplt

class Dataset:

    DEFAULT_SIZE = (1000,)
    DEFAULT_VARIATION = (2,)
    DEFAULT_CENTER = (1, 1, 1)
    DEFAULT_GROUP = (1,)

    def __init__(self, size=DEFAULT_SIZE, variation=DEFAULT_VARIATION,
                 center=None, group=DEFAULT_GROUP):
        '''
        generic dataset creator\n
        size=2              how many points\n
        variation=1         standard deviation from cluster_center\n
        center=([0, 2, 4])  where the gaussian center of the points should be\n
        group=1             used to define which group a point belongs to\n
        self.dataset        random dataset of of 3d points\n
        self.results        dataset of 2d points\n
                            [0] correct cluster\n
                            [1] calculated cluster\n
        keep in mind that your milage may vary on results, you could arrive at a\n
        local minima where you algorithm cconverges correctly but you do not\n
        classify the clusters according to initial assignment\n
        '''
        #avoid mutable array trap
        if center is None:
            center = DEFAULT_CENTER
        self.dataset = self.__gen_normal_dataset(size, variation, center)
        self.results = self.__gen_results_dataset(size,group)

    def __add__(self, other):
        "Add two Positions and return a new one."
        assert (False), "add not implemented, try +="

    def __iadd__(self, other):
        "In-place add += updates the current instance."
        self.dataset = np.vstack((self.dataset, other.dataset))
        self.results = np.vstack((self.results, other.results))
        return self

    def __gen_normal_dataset(self,cluster_size, cluster_variation, cluster_center):
        x = np.random.normal(scale=cluster_variation, size=cluster_size) + cluster_center[0]
        y = np.random.normal(scale=cluster_variation, size=cluster_size) + cluster_center[1]
        z = np.random.normal(scale=cluster_variation, size=cluster_size) + cluster_center[2]
        return (np.transpose(np.vstack((x, y, z ))))

    def __gen_results_dataset(self,cluster_size, group):
        group_expected      = np.ones(cluster_size) * group
        group_calculated    = np.zeros(cluster_size)
        return np.transpose(np.vstack((group_expected,group_calculated )))


def genNonRepeatingRandomSamples(source_array, numSamps):
    assert (len(source_array) >= numSamps), "source_array smaller than numSamps"

    # allocate a buffer to write to
    return_array = np.zeros(shape=(numSamps, len(source_array[0])))

    # want non repeating samples
    # create a 1d array, random shuffle it,
    # first numSamps are what you will use
    randsamples = np.arange(len(source_array))
    np.random.shuffle(randsamples)
    for i in range(numSamps):
        return_array[i] = np.copy(source_array[randsamples[i]])
    return return_array


if __name__ == '__main__':
    pts1 = Dataset(center=([1, 1, 1]))
    pts2 = Dataset(center=([1, 5, 5]), group=2)
    pts3 = Dataset(center=([5, 5, 5]), group=3)
    utplt.plot_3D_dataset((np.vstack((pts1.dataset, pts2.dataset, pts3.dataset))), np.vstack((pts1.results, pts2.results, pts3.results)))
