class Node(object):
    pass


def create_node(number):
    n = Node()
    n.number = number
    n.next = None
    return n


def create_nodes(start, end):
    n = create_node(start)
    if start != end:
        n.next = create_nodes(start + 1, end)
    return n


def print_node(node):
    print(f'node: {node.number}')
    if node.next != None:
        print_node(node.next)


print_node(create_nodes(1, 5))
