import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

class DynamicUpdate:
    def __init__(self):
        #Set up plot
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.hasPlotted = False
        #Other stuff
        # self.ax.grid()

    def update(self, pts,results,clusters):
        #Update data (with the new _and_ the old points)
        if self.hasPlotted == True:
            self.hand1.remove()
            self.hand2.remove()

        colors = [i for i in range(len(clusters))]
        #c=results[:,1] holds the calculated cluster
        self.hand1 = self.ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], c=results[:,1]*100, marker='o')
        self.hand2 = self.ax.scatter(clusters[:, 0], clusters[:, 1], clusters[:, 2], c=colors, marker='*', s = 444)
        self.hasPlotted = True
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def lock_Plt(self):
        '''
        when finished dynamicly updating, lock it so you can manipulate the data
        :return:
        '''
        plt.ioff()
        plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
def plot_3D_dataset(pts,results):
    assert (len(pts[0]) == 3), "pts not 4 dimensional!"

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], c=results[:,0], marker='o')
    plt.show(block=True)