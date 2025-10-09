lst=[1,2,3]
my_str="mlops playlist"
my_int=242

#print(type(my_int))

#lst.clear()
#my_str=my_str.capitalize()
#print(lst)

# a="x"
# b="y"
# print(a+b)

from oops_proj import chatbook
user1=chatbook()
print(user1.id)



# using static method directly from class rathe than obj
# chatbook.set_id(10)

# user2=chatbook()
# print(user2.id)

# user3=chatbook()
# print(user3.id)

# user2=chatbook()
# print(user2.id)

# user3=chatbook()
# print(user3.id)



#getter and setter
# print(user1.get_name())
# user1.set_name("ankit")
# print(user1.get_name())


# print(user1._chatbook__name)

# #function vs method below
# lst=[1,2,3]

# #function
# a1=len(lst)
# print(a1)

# #method
# user1=chatbook()
# user1.sendmsg()