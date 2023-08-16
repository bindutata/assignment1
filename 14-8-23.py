class Queue:
    def __init__(self,size):
        self.size=size
        self.queue1=[] 
        self.queue2=[]
    def queue1_is_full(self):
        return len(self.queue1)==self.size
    def queue1_is_empty(self):
        return len(self.queue1)==0
    def enqueing1(self,element):
        if self.queue1_is_full():
           print("queue is full.")
        else:
            return self.queue1.append(element)
    def enqueing2(self,elements):
        if len(self.queue2)<self.size:
           self.queue2.append(elements)
        print("the number of elements to be deleted to add elements:",len(self.queue2))
    def dequeing(self):
        if self.queue1_is_empty():
            print( "there are no elements in queue")
        else:
            return self.queue1.pop(0)
    def display(self):
        return self.queue1
q=Queue(5)
(q.enqueing1(1))
(q.enqueing1(2))
(q.enqueing1(3))
(q.enqueing1(4))
(q.enqueing1(5))
(q.enqueing1(6))
print(q.display())
(q.enqueing2(7))
q.enqueing2(8)



'''class Printing():
    def __init__(self):
        self.tasks=[]
    def adding_tasks(self,task):
        self.tasks.append(task)
        print(f" add task:{task}")
    def printing_tasks(self):
        if len(self.tasks)==0:
            print("there are no tasks to be printed")
        else:
            for i in range(len(self.tasks)):
               self.tasks.pop(0)
               print(f"print:{self.tasks}")
p=Printing()
p.adding_tasks("ssc class results")
p.adding_tasks("inter results")
p.adding_tasks("B.tech results")
p.adding_tasks("family photo")
p.adding_tasks("resume")
p.printing_tasks()'''


