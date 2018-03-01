class Node:
        def __init__(self, data):
                self.leftchild = None
                self.rightchild = None
                self.data = data
                self.size = 1
        def Insert_function(self, data):
                if(self.data == None):
                        self.data = data
                else:
                        if(self.data>data):
                                if(self.leftchild == None):
                                        self.leftchild = Node(data)
                                else:
                                        self.leftchild.Insert_function(data)
                        else:
                                if(self.rightchild == None):
                                        self.rightchild = Node(data)
                                else:
                                        self.rightchild.Insert_function(data)
        def find_parent(self, data, parent):
                if(self.data>data):
                        if(self.leftchild == None):
                                return None
                        return self.leftchild.find_parent(data,self)
                elif(self.data<data):
                        if(self.rightchild == None):
                                return None
                        return self.rightchild.find_parent(data,self)
                else:
                        return parent


        def find_childeren(self, data):
                if(self.data>data):
                        if(self.leftchild == None):
                                return None
                        return self.leftchild.find_childeren(data)
                elif(self.data<data):
                        if(self.rightchild == None):
                                return None
                        return self.rightchild.find_childeren(data)
                else:
                        return self
        def childeren(self):
                check = 0
                if self.leftchild != None:
                        check += 1
                if self.rightchild != None:
                        check += 1
                return check

        
        def delete_function(self, data):
                ch_child = 0
                child = self.find_childeren(data)
                parent = self.find_parent(data, None)
                if(child == None):
                        return
                else:
                        ch_child = child.childeren()
                        if(ch_child==0):
                                if(parent != None):
                                        if(parent.leftchild == child):
                                                parent.leftchild = None
                                        else:
                                                parent.rightchild = None
                                        del child
                                else:
                                        self.data = None #root인경우
                                        self.size = 0
                        elif(ch_child==1):
                                if(child.leftchild != None):
                                        temp = child.leftchild
                                else:
                                        temp = child.rightchild
                                        
                                if(parent!=None):
                                        if(parent.leftchild == child):
                                                parent.leftchild = temp
                                        else:
                                                parent.rightchild = temp
                                        del child
                                else:
                                        self.data = temp.data
                                        self.leftchild = temp.leftchild
                                        self.rightchild = temp.rightchild
                        else:
                                temp = child
                                successor = child.rightchild
                                while(successor.leftchild != None):
                                        temp = successor
                                        successor = successor.leftchild
                                if(temp.leftchild == successor):
                                        child.data = successor.data
                                        temp.leftchild = successor.rightchild
                                else:
                                        child.data = successor.data
                                        temp.rightchild = successor.rightchild
        def preorder(self):
                if(self.size == 0):
                        return
                print(self.data)
                if(self.leftchild != None):
                        self.leftchild.preorder()
                if(self.rightchild != None):
                        self.rightchild.preorder()
        def postorder(self):
                if(self.size == 0):
                        return
                if(self.leftchild != None):
                        self.leftchild.postorder()
                if(self.rightchild != None):
                        self.rightchild.postorder()
                print(self.data)
        def inorder(self):
                if(self.size == 0):
                        return
                if(self.leftchild != None):
                        self.leftchild.inorder()
                print(self.data)
                if(self.rightchild != None):
                        self.rightchild.inorder()
