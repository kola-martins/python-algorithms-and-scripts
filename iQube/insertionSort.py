import random  


N = 1000     # number of elements in list
list1 = []   # list of integer elements
for i in range(0, N):
    list1.append(random.randint(0, N-1)) # append random numbers to the list 

# function to print the unsorted numbers in the list
def printList(list2print):
    for i in list2print:
        print i
    print len(list2print)
 
# insertion sort function
def insertion_sort(list2):
    for i in range(1, len(list2)):
        save = list2[i] #store the value in this position
        j = i # store the current index of the outer loop iteration
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1] #swap the values
            j -= 1 #decrement j by 1
        list2[j] = save

#entry point of the program
if __name__ == "__main__" :
    print "this program implements the insertion sort algorithm with a set of 1000 integers:"
    # make a true copy of list1 each time
    list2 = list(list1)
    print "list before sorting"
    printList(list2)
    insertion_sort(list2)
    print "list after sorting"
    printList(list2)
    