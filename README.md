# Clustering_Demos
My implementation of K Means clustering on 3D data
requires utilities_kp module
You choose the number of clusters and k_means will calculate point membership given your data.  Its vulnerable to local minima (shows up 
more often with fewer points).  Also vulnerable to outliers skewing the cluster centers and hence cluster membership. 

And 2 DBSCAN implementations (code comes from others)
Uses cluster density function defined as minimum required number of points/spherical volume as defined by e (radious)).  
This required density is used to calculate clcuter membership and number of clusters.  If a point is more than 2e fromany other point
then its considered an outlier and is not included.  Solves the skewing problem above but introduces issues with correct density
selection.  Too small/large, too small a radius then maybe your clusters are too small, or outliers are not really outliers.

Can use DBSCAN to find outliers to eliminate then k means to find a given number of clusters.  Might still have local minima though.
..

