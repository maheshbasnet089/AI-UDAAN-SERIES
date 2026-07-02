

name = "manish"
name2 = "anish"
name3= "nish"
name4= "ish"

names = ["manish","anish","nish","ish","japan",12,True] #list datatypes

country = "japan"
country1 = "usa"
country2 = "nepal"

countries = ["japan","usa","nepal"] #list 
# print(countries[-1])
# countries.append("india") -- adds to last of list 
# countries.pop() -- removes last item of list 
# countries.insert(0,"india") -- adds to 0 index (first)
# countries.remove("nepal") -- removes 
# countries[1] = "china"

# print(len(countries))
# print(countries)



countries_set = {"japan","usa","nepal","nepal","japan"} #sets
print(countries_set)


countries_tuple = ("japan","usa","nepal","japan") #tuple
# print(countries_tuple[0])
# countries_tuple[1] = "china"
# print(countries_tuple.count("japan"))
# print(countries_tuple.index("nepal"))




full_name = "manish basnet"
address = "itahari"
company = "digital pathshala"
college = "itahari namuna college"


person_information = {
    "full_name" : "manish basnet", 
    "address" : "itahari", 
    "company" : "digital pathshala", 
    "college" : "itahari namuna college", 
    "age" : 24, 
    "isNepali" : True
}

# print(person_information["full_name"])
# print(person_information["isNepali"])
# person_information["color"] = "blue"
person_information["age"] = 25
person_information.pop("college")
print(person_information)



# prediction = {
#     "image" : "cat.png", 
#     "class" : "cat", 
#     "confidence" : 98.00
# }
