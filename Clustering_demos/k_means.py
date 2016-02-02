# Pick out k random points to use as our initial centroids
import random
import utilities_KP.utils as ut
import utilities_KP.utils_plot as ut_plot
import numpy as np
from scipy.spatial import distance

# initial = random.sample(points, k)
# dst = distance.euclidean(a,b)

class K_means:
    DEFAULT_NUMB_CLUSTERS = 3

    def __init__(self):
        self.at_least_one_point_reassigned = False
        self.iteration =0
        return

    def __initialize_cluster_centers(self, pts, numb_clusters=DEFAULT_NUMB_CLUSTERS):
        # while true algorithm runs
        self.at_least_one_point_reassigned = True

        # choose from the points array numb_clusters samples to start from
        self.clusters = ut.genNonRepeatingRandomSamples(pts.dataset, numb_clusters)
        return

    def __assign_points_to_clusters(self, pts):
        '''
        calc euclidean distance to each cluster center
        assign point to closest one
        pts         List of all the points
        :return:    True one point reassigned to different cluster, recalculate cluster centers
                    False no points reassigned, no need to recalc cluster centers
        '''

        self.at_least_one_point_reassigned = False  # assumme no reassignments

        for i in range(len(pts.dataset)):
            # calculate orig info
            smallest_dst = distance.euclidean(pts.dataset[i], self.clusters[pts.results[i][1]])
            orig_cluster = pts.results[i][1]

            for j in range(len(self.clusters)):
                dst = distance.euclidean(pts.dataset[i], self.clusters[j])
                if dst < smallest_dst:
                    pts.results[i][1] = j
                    smallest_dst = dst
                    if j != orig_cluster:
                        self.at_least_one_point_reassigned = True
        return self.at_least_one_point_reassigned

    def __recalculate_cluster_centers(self,pts):

        for current_cluster in range(len(self.clusters)):
            x=y=z=0
            num_members = 0

            #loop through dataset, find all members assigned to current_cluster
            #and figure out the center of that mass
            for current_dataset in range(len(pts.dataset)):
                if pts.results[current_dataset][1] == current_cluster:
                    x += pts.dataset[current_dataset][0]
                    y += pts.dataset[current_dataset][1]
                    z += pts.dataset[current_dataset][2]
                    num_members+=1

            #recalculate the center
            if num_members>0:
                self.clusters[current_cluster][0] = x/num_members
                self.clusters[current_cluster][1] = y/num_members
                self.clusters[current_cluster][2] = z/num_members
        return

    def run_Algorithm(self, pts, numb_clusters):

        plot = ut_plot.DynamicUpdate()

        self.__initialize_cluster_centers(pts, numb_clusters)

        plot.update(pts.dataset,pts.results,self.clusters)


        while (self.at_least_one_point_reassigned):
            if self.__assign_points_to_clusters(pts):
                self.iteration +=1
                print("running step " + str(self.iteration))
                self.__recalculate_cluster_centers(pts)
                plot.update(pts.dataset,pts.results,self.clusters)
        plot.lock_Plt()

if __name__ == '__main__':
    # generate 3 datasets
    pts  = ut.Dataset(center=([1, 1, 1]))
    pts += ut.Dataset(center=([5, 5, 5]), group=2)
    pts += ut.Dataset(center=([10, 10, 10]), group=3)

    data = K_means()
    data.run_Algorithm(pts, 3)



