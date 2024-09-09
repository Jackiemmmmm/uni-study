# Question 1


# class Employee:
#     def __init__(self, id, first_name, last_name, position, phone):
#         self.employee_id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.position = position
#         self.phone = phone


# Question 2


# class Employee:
#     def __init__(self, employee_id, first_name, last_name, position, phone):
#         self.employee_id = employee_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.position = position
#         self.phone = phone

# employeeObj1 = Employee('100001', 'John', 'Lee', 'Accountant', '0001')
# employeeObj2 = Employee('100002', 'Mary', 'Zheng', 'Programmer', '0002')
# employeeObj3 = Employee('100003', 'Cindy', 'Wilson', 'DBA', '0001')


# Question 3 and Question 4


# class Employee:
#     def __init__(self, employee_id, first_name, last_name, position, phone):
#         self.employee_id = employee_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.position = position
#         self.phone = phone

#     def __str__(self):
#         return self.employee_id + " " + self.first_name + " " + self.last_name

#     def __repr__(self):
#         return "Employee('{0}', '{1}', '{2}', '{3}', '{4}')".format(
#             self.employee_id, self.first_name, self.last_name, self.position, self.phone
#         )


# Question 5


class Node:
    def __init__(self, datum, next):
        self.datum = datum
        self.next = next

    def getDatum(self):
        return self.datum


class MyLinkedList:
    def __init__(self):
        self.firstNode = None

    def __str__(self):
        listName = ""
        node = self.firstNode
        while node != None:
            isHaveArrow = ""
            if node.next != None:
                isHaveArrow = "->"
            listName += str(node.datum) + isHaveArrow
            node = node.next
        return "MyLinkedList[{0}]".format(listName)

    def insertFirst(self, datum):
        newNode = Node(datum=datum, next=self.firstNode)
        self.firstNode = newNode

    def getLastNode(self):
        node = self.firstNode
        while (node != None) and (node.next != None):
            node = node.next
        return node

    def getLength(self):
        count = 0
        node = self.firstNode
        while node != None:
            node = node.next
            count = count + 1
        return count

    def getNode(self, index):
        node = self.firstNode
        i = 0
        while (i < index) and (node != None):
            node = node.next
            i = i + 1
        return node

    def removeFirst(self):
        if self.firstNode == None:
            return None
        firstDatum = self.firstNode.datum
        self.firstNode = self.firstNode.next

        return firstDatum


linkedListObj = MyLinkedList()
linkedListObj.insertFirst("dog")
linkedListObj.insertFirst("cat")
linkedListObj.insertFirst("emu")
linkedListObj.insertFirst("frog")
print(linkedListObj.getLength())
print(linkedListObj)
