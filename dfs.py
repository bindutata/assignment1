class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
def preorder(root):
    if root is None:
        return
    stack=[]
    stack.append(root)
    while stack:
        node=stack.pop()
        print(node.value,end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
def inorder(root):
        if Node is None:
            return
        stack=[]
        current_node=root
        while True:
            if current_node is not None:
                stack.append(current_node)
                current_node=current_node.left
            elif stack:
                current_node=stack.pop()
                print(current_node.value,end=" ")
                current_node=current_node.right
            else:
                break
def postorder(root)  :
        if root is None:
            return
        stack1=[]        
        stack2=[]  
        stack1.append(root)
        while stack1:
            node=stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node=stack2.pop()
            print(node.value,end=" ")
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
root.left.left=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print("preorder traversal:",preorder(root))
print("\ninorder:",inorder(root))
print("\npostorder:",postorder(root))


    



