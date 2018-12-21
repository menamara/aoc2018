import unittest
import day7

class Test_Day7(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            "Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin.",]

    def test_graph_order(self):
        self.assertEquals(day7.create_graph(self.test_input)['F'], ['C'])
        self.assertEquals(day7.create_graph(self.test_input)['E'], ['B','D','F'])
        self.assertEquals(day7.order(self.test_input),'CABDFE')

    def test_scheduler(self):
        self.assertEquals(day7.schedule(self.test_input, 2, 0),15)

