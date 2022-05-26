# 1991


class Node:
    def __init__(self, data, left, right) -> None:
        self.left = left
        self.right = right
        self.data = data

def pre_order(Node):
    print(Node.data, end="")
    if Node.left != None:
        pre_order(tree[Node.left])
    if Node.right !=None:
        pre_order(tree[Node.right])
 
def in_order(Node):
    if Node.left != None:
        in_order(tree[Node.left])
    print(Node.data, end="")
    if Node.right !=None:
        in_order(tree[Node.right])
        
def post_order(Node):
    if Node.left != None:
        post_order(tree[Node.left])
    if Node.right !=None:
        post_order(tree[Node.right])        
    print(Node.data, end="")
N = int(input())
tree = {}

for i in range(N):
    data, left, right = map(str, input().split())
    if i == 0:
        first = data
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = Node(data, left, right)
pre_order(tree[first])
print()
in_order(tree[first])
print()
post_order(tree[first])        