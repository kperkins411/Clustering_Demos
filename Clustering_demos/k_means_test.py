import unittest
import utilities_KP.utils as ut
import Clustering_demos.k_means  as cd

class Test_K_Means(unittest.TestCase):
    def setUp(self):

        self.pts  = ut.Dataset(size = 4,center=([1, 1, 0]))
        self.pts.dataset=[[0,0,0],[0,2,0],[2,2,0], [2,0,0]]

        pts1 = ut.Dataset(size = 4,center=([5, 5, 5]), group=2)
        pts1.dataset=[[4,0,0],[6,2,0],[4,2,0], [6,0,0]]
        self.pts += pts1

        pts1 = ut.Dataset(size = 4,center=([5, 5, 5]), group=2)
        pts1.dataset=[[2,4,0],[2,6,0],[4,4,0], [4,6,0]]
        self.pts += pts1



        return

    def test_upper(self):
        data = cd.K_means()
        data.run_Algorithm(self.pts, 3)
        ut.plot_3D_dataset(self.pts.dataset,self.pts.results, data.clusters )

        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
