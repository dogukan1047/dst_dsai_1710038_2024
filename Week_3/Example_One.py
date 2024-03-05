#Agenda
#lists, tuples, Sets, Dictionary
#Funções
#Lambda
#Arrays 
#Classes
#Computação distribuída

list1 = ["abc", 34, True, 40, "male",True, 46]
print(list1[6])
list1.append("25")
print(list1[7])


tuple1 = ("abc", 34, True, 40, "male")
print(f"tuple1:{tuple1}")
# tuple1.append("1") not possible 

list1 = [2,2,"hello"]
tuple2=(2,2,"hello")
set1={2,2,"hello"} # data cannot be repeated

print(set1)
set1.add("ola")
print(set1)

list3=["Dogukan","Polatel"]
list3.append("Artificial intelligence")
print(f"list3 :{list3}")

set2={2,2,3,4,"hello"}
print(f"set2:{set2}")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

today={
    "class":["dst","network","programing"],
    "quantity-of-students":14,
    "students_name":{"Polatel Dogukan"}
}

print(today)
print(today.keys())
today["students_name"]


thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist1)
print(len(thislist1))

list1 = ["abc", 34, True, 40, "male",True, 46]
print(list1[1])
print("[2:5]=",list1[2:5])
print("[:4]=",list1[:4])
print("[2:]=",list1[2:])