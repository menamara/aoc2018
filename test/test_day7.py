import unittest
import day6

class Test_Day5(unittest.TestCase):
    def setUp(self):
        test_input = [
                    '1, 1',
                    '1, 6',
                    '8, 3',
                    '3, 4',
                    '5, 5',
                    '8, 9', ]
        self.asso_map = day6.Association_Map(test_input)

    def test_ab_xy_transformation(self):
        self.assertEqual(day6.transform_to_ab([1,1]), [2,0])
        self.assertEqual(day6.transform_to_ab([1,6]), [7,-5])
        self.assertEqual(day6.transform_to_ab([8,3]), [11,5])
        self.assertEqual(day6.transform_to_ab([3,4]), [7,-1])
        self.assertEqual(day6.transform_to_ab([8,9]), [17,-1])
        self.assertEqual(day6.transform_to_xy(day6.transform_to_ab([1,1])), [1,1])
        self.assertEqual(day6.transform_to_xy(day6.transform_to_ab([1,6])), [1,6])
        self.assertEqual(day6.transform_to_xy(day6.transform_to_ab([8,3])), [8,3])
        self.assertEqual(day6.transform_to_xy(day6.transform_to_ab([3,4])), [3,4])
        self.assertEqual(day6.transform_to_xy(day6.transform_to_ab([8,9])), [8,9])

    def test_large_area(self):
        self.assertEqual(self.asso_map.area_around_all(32), 16)
    
    def test_asso_map_edges(self):
        self.assertEqual(self.asso_map.xmax, 9)
        self.assertEqual(self.asso_map.ymax, 10)
        self.assertEqual(self.asso_map.xmin, 0)
        self.assertEqual(self.asso_map.ymin, 0)

    def test_asso_map_anchor(self):
        self.assertEqual(len(self.asso_map.anchor), 6)
        self.assertEqual(self.asso_map.anchor[0], [1,1])
        self.assertEqual(self.asso_map.anchor[1], [1,6])
        self.assertEqual(self.asso_map.anchor[2], [8,3])
        self.assertEqual(self.asso_map.anchor[3], [3,4])
        self.assertEqual(self.asso_map.anchor[4], [5,5])
        self.assertEqual(self.asso_map.anchor[5], [8,9])

    def test_asso_map_area(self):
        self.assertEqual(self.asso_map.max_area(), 17)
        
    def test_manhattan_dist(self):
        self.assertEqual(day6.manhattan_dist([0,0],[1,1]),2)
        self.assertEqual(day6.manhattan_dist([0,5],[1,1]),5)
        self.assertEqual(day6.manhattan_dist([0,-5],[1,1]),7)
        self.assertEqual(day6.manhattan_dist([0,-1],[1,0]),2)
