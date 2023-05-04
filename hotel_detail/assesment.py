# Question 1. Write a for loop to iterate through the list A = [1, 2, 3, 4, 5, 6]. Square each element of the list in one by one fashion and print them. After the end of the iteration, print - "The sequence has ended".

A = [1, 2, 3, 4, 5, 6]
for i in A:
    print(i**2)
print('The sequence has ended')


# Question 2. If choice of user = 2, print the pattern - > 
# * * * * *
#  * * * *
#   * * *
#    * *
#     *                       
#    _ _
#   _ _ _
#  _ _ _ _
# _ _ _ _ _

# If choice of user = 1, print the pattern - > 

# * * * * *
#  * * * *
#   * * *
#    * *
#     * 

# If choice of the user = any_other_choice_other_than_1_and_2, print the message - >

# 'Invalid Input'

user = int(input('enter number :'))
if user == 1:
    pattern =[]
    for i in range(5):
        for j in range(10)
        if i%2!=0:


# Question 3. Create a tuple t_1 = (1, 4, 9, 16, 25, 36). Square each element of the tuple using tuple comprehension and store the result in a variable known as t_modified. Find element at index position 4 of the tuple t_modified. Now slice the modified tuple in such a way that the sliced  tuple includes only elements from index position 1 to 3 and store this sliced tuple in a variable known as t_sliced. 

t_1 = (1, 4, 9, 16, 25, 36)
t_modified = []
for i in t_1:
    t_modified.append(i**2)
t_modified = tuple(t_modified)

ele_4 = t_modified[4]

t_sliced = t_modified[1:4]



# Question 4. Show by raising a error how tuple are immutable and also define what exactly immutability is in your own words.

t_1 = (1, 4, 9, 16, 25, 36)
# t_1[0] = 9


# Question 5. Create a frozenset named frozen_set_1 containing the elements: 'A', 'B', 'C' and 'D' and combine it using union with a frozenset named frozen_set_2 containing elements 'A', 2, 'C' and 4. The final combined frozenset must be named frozenset_union. Now find the common elements in frozen_set_1 and frozen_set_2 and store the result in a variable named frozenset_common. Lastly, in a new forzenset named forzenset_difference store the elements of frozen_set_1 which are not in frozen_set_2 and in a new frozenset named frozenset_distinct store the elements which are unique to frozen_set_1 and frozen_set_2.

frozen_set_1 = {'A','B','C','D'}
frozen_set_2 = {'A',2,'C',4}
frozenset_union = frozen_set_1.union(frozen_set_2)
frozenset_common = frozen_set_2.intersection(frozen_set_1)

forzenset_difference = frozen_set_1 - frozen_set_2
frozenset_distinct = frozen_set_1 ^ frozen_set_2

# Question 6. Write a python program to remove items in a list containing the character 'a' or 'A'. Use lambda function for it. For this program pass in as argument the list: list_a = ["car", "place", "tree", "under", "grass", "price"] to the lambda function named remove_items_containing_a_or_A.

ans= []
list_a = ["car", "place", "tree", "under", "grass", "price"]
for i in range(len(list_a)):
    flag = lambda list_a[i] :  if ('a' or 'A')in list_a[i] 



print()