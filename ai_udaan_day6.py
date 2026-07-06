# print("hello manish")
# print("hello anish")
# print("bye nish")
# print("bye nish")
# print("bye ish")
# print("hello sh")

# def greet(name,age):
#     print("hello " + name)


# greet("manish",22) #hello manish
# greet("anish",23) #hello anish
# greet("nish",24) #hello nish


#return 
# def add(num1,num2):
#     return num1+num2

# sum = add(1,4)
# print(sum)

# def student():
#     return "Manish",23,"Itahari"

# name,age,location = student() #tuples ma return garxa
# print(name)


# def say_hello(name="manish"):
#     print("hello " + name)

# say_hello()
# say_hello("anish")


def multiple(num1,num2):
    print(num1,num2)
    print(num1+num2)

multiple(1,"1")


def square_num(num):
    return num*num

result = square_num(2)
result(2)

result2 = lambda num:num*num
result2(2)



def bahira_ko_function():
    def vitra_ko_function():
        print("Vitra bata print vako ho")
    vitra_ko_function()
bahira_ko_function()

# repetition vairaxa or duplication of code 
# unmanageable

# function vaneko a block of code raixa, jasko sayatw bata hamile code repetition lai kaam garna 
# sakxam, manageable banauna sakxam, sharing easy parna sakxam 