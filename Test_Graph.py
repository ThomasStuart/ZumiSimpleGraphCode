import unittest
from Graph import Graph


class MyTestCase(unittest.TestCase):

    def test_print_coordinates_of_simple_nodes(self):
        graphObject = Graph()
        graphObject.create_simple()
        nodes = graphObject.nodes_dict


        actual_list         = [ (0,0) , (-10,0) , (0,10) , (10,0)]
        corresponding_nodes = [ 's', 'a', 'x', 'b']

        ps  = graphObject.nodes_dict['s'].position
        pa  = graphObject.nodes_dict['a'].position
        px  = graphObject.nodes_dict['x'].position
        pb  = graphObject.nodes_dict['b'].position
        expected_list        =  [ ps,pa,px,pb ]

        self.assertEqual( actual_list, expected_list )

    def test_print_edges_of_node_s(self):
        graphObject = Graph()
        graphObject.create_simple()
        nodes = graphObject.nodes_dict

        edges = graphObject.nodes_dict['s'].edges
        self.assertEqual( 3 , len(edges) )


    def test_print_edges_of_node_x(self):
        graphObject = Graph()
        graphObject.create_simple()
        nodes = graphObject.nodes_dict

        edges = graphObject.nodes_dict['x'].edges
        self.assertEqual(1, len(edges))


    def test_the_num_of_edges_at_s(self):
        graphObject = Graph()
        graphObject.create_complex()
        nodes = graphObject.nodes_dict

        edges = graphObject.nodes_dict['s'].edges
        self.assertEqual( 4 , len(edges) )


    def test_correct_position_of_s(self):
        graphObject = Graph()
        graphObject.create_complex()
        nodes = graphObject.nodes_dict

        position = graphObject.nodes_dict['s'].position
                        # LHS  actual value that you type in
                        # RHS what the program gives us

        self.assertEqual(  (0,0) , position )

if __name__ == '__main__':
    unittest.main()
