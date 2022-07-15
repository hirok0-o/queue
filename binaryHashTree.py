class Node:
    def __init__(self,val=None, priority=0,left=None,right=None,parent=None) -> None:
        self.val=val
        self.left=left
        self.right=right
        self.priority=priority
        self.parent=parent

    def __repr__(self) -> str:
        return f"{self.val},{self.priority}"

class BinaryHashTreeQueue:
    def __init__(self,rootVal=50,rootPrior=0) -> None:
        self.root=Node(rootVal,rootPrior)
    
    def __iter__(self):
        #breadth traversal
        queue=[self.root]
        while len(queue)>0:
            currNode=queue[0]
            yield currNode
            queue=queue[1:]
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)


    def enqueue(self,val,priority):
        #perform depth first search finding first child node that is None
        queue=[self.root]
        while len(queue)>0:
            currNode=queue[0]
            queue=queue[1:]
            if currNode.left:
                queue.append(currNode.left)
            else:
                currNode.left=Node(val,priority,parent=currNode)
                node=currNode.left
                break
            if currNode.right:
                queue.append(currNode.right)
            else:
                currNode.right=Node(val,priority,parent=currNode)
                node=currNode.right
                break
        #after node is inserted to bottom of tree traverse back swapping if its priority is greater than parents
        while node.parent and node.priority>node.parent.priority:
            node.val,node.priority,node.parent.val,node.parent.priority=node.parent.val,node.parent.priority,node.val,node.priority
            node=node.parent
    
    def dequeue(self):
        queue=[self.root]
        #perform breath first search to find most bottom value
        while len(queue)>0:
            currNode=queue[0]
            queue=queue[1:]
            if currNode.left:
                queue.append(currNode.left)
                prevParent=[currNode,'l']
            else:
                bottom=prevParent
                break
            if currNode.right:
                prevParent=[currNode,'r']
                queue.append(currNode.right)
            else:
                bottom=prevParent
                break
        if bottom[1]=='l':
            n=bottom[0].left
            bottom[0].left=None
        else:
            n=bottom[0].right
            bottom[0].right=None
        returnVal=self.root.val
        self.root.val,self.root.priority=n.val,n.priority
        node=self.root
        while node.left:
            if node.left:
                bigger=[node.left,'l']
            if node.right and node.right.priority>node.left.priority:
                bigger=[node.right,'r']
            if bigger[1]=='l':
                node.val,node.priority,node.left.val,node.left.priority=node.left.val,node.left.priority,node.val,node.priority
                node=node.left
            elif bigger[1]=='r':
                node.val,node.priority,node.right.val,node.right.priority=node.right.val,node.right.priority,node.val,node.priority
                node=node.right
        return returnVal


