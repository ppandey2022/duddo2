#Learning how a linked list works, and how to add stuff to it

class Node:                             #making a blueprint for a node
    def __init__(self, data):           #constructor taking in data as an argument
        self.data = data                #data of the object = data taken in by the constructor
        self.next = None                #next pointer of the object = none for now

class LinkedList:                       #contains the first node, also known as the "head" node
    def __init__(self):                 #default constructor saying that the head doesn't point to anything for now
        self.head = None

    def trav(self):                     #function to go through, or traverse, through the list
        place = self.head               #placeholder variable to refer to the linked list's head
        while(place):                   #while it is not none, ( two nos make a yes )
            print(place.data)           #print the data of the placeholder
            place = place.next          #let place refer to the next node

    def pushBegin(self, d):             #function to insert an element at the beginning of a linked list
        place = Node(d)                 #placeholder variable that refers to the new node with the data in it
        place.next = self.head          #placeholder's next pointer refers to the first ( head ) element
        self.head = place               #head now refers to the placeholder, since it's the first element

    def pushAfter(self, prev_n, d):     #function to insert an element after a certain node
        if(prev_n == None):             #the node has to exist in the linked list
            print('The node should be in the linked list, lol')
            return

        place = Node(d)                 #placeholder variable that refers to the new node with the data in it
        place.next = prev_n.next        #placeholder's next pointer refers to the previous node's next node
        prev_n.next = place             #previous node's next point now refers to the placeholder

    def pushEnd(self, d):               #function to insert an element at the end of a linked list
        place = Node(d)                 #placeholder variable that refers to the new node with the data in it
        if(self.head == None):          #if the linked list is empty
            self.head = place           #the head pointer now refers to placeholder
            return

        self_p = self.head              #placeholder variable that refers to the head of the linked list
        while(self_p.next):             #while there exists another node after self_p
            self_p = self_p.next        #self_p now refers to the next node ( refers to the last node by the end of the loop)

        self_p.next = place             #now the last element's next pointer refers to place, making place the last element


ll = LinkedList()                       #initializing a linked list

ll.head = Node(1)                       #Making a node, and assigning it to ll's head with data = 1
n2 = Node(2)                            #Making another node, n2 with data = 2
n3 = Node(3)                            #Making a final node, n3 with data = 3

ll.head.next = n2                       #Now, ll's head's next pointer refers to n2
n2.next = n3                            #n2's next pointer refers to n3
                                        #n3's next pointer is already defined as None
ll.trav()
print('\n')

ll.pushBegin(0)

ll.trav()
print('\n')

ll.pushAfter(n2, 2.5)

ll.trav()
print('\n')

ll.pushEnd(4)

ll.trav()
print('\n')
