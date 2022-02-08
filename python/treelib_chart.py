from treelib import Node, Tree

tree = Tree()

tree.create_node("Harry", "harry")  # No parent means its the root node
tree.create_node("Jane",  "jane"   , parent="harry")
tree.create_node("Bill",  "bill"   , parent="harry")
tree.create_node("Diane", "diane"  , parent="jane")
tree.create_node("Mary",  "mary"   , parent="diane")
tree.create_node("Mark",  "mark"   , parent="jane")

tree.show()


with open('tree.dot', 'w') as example_file_obj:
    example_file_obj.write(tree.to_graphviz())

example_file_obj.close()
