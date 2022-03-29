import csv

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode

# Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head
         
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None

    def LListprint(self):
        printval = self.head
        print(printval.data.data)
        printval = printval.next
        while (printval):
            print(printval.data.data)
            printval = printval.next

    def Listprint(self):
        printval = self.head
        print(printval.data)
        printval = printval.next
        while (printval):
            print(printval.data)
            printval = printval.next

    def Traversal(self):
        arr = []
        printval = self.head
        while (printval):
            arr.append(printval.data)
            printval = printval.next
        return arr

class Helper:
    myDic = {}
    finalList = []
    def __init__(self):
        self.myDic = {}
        self.finalList = []

    def rankedWords(self, included, notIncluded):

        with open('wordRank.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in reader:
                    self.myDic[row[0].replace(',', '')] = row[1].replace(',', '')
        
        #When no input is provided
        if len(included) == 0 and len(notIncluded) == 0:
            for i in range(1,51):
                defaultList.AtEnd(Node(self.myDic[str(i)]))
            defaultList.LListprint()
        
        #Add elements with included letters
        if len(included) != 0:
            for key in range(1,len(self.myDic)):
                flag = 0
                for letter in included:
                    if letter not in self.myDic[str(key)]:
                        flag = 1
                if flag == 0:
                    finalList.AtEnd(self.myDic[str(key)])
        else:
            for key in self.myDic:
                finalList.AtEnd(self.myDic[str(key)])

        #Remove elements that have not included letters
        if len(notIncluded) != 0:
            myArr = finalList.Traversal()
            for word in myArr:
                flag = 0
                for letter in notIncluded:
                    if letter in word:
                        flag = 1
                if flag == 1:
                    finalList.RemoveNode(word)
        if len(included) != 0 or len(notIncluded) != 0:
            finalList.Listprint()


#Calls to check function

defaultList = SLinkedList()
finalList = SLinkedList()
myRun = Helper()
myRun.rankedWords(['o', 'n', 'e', 's'],['b', 'z'])

