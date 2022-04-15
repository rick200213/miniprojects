"""
string concatenation
to concatenate a couple of strings
there a few ways to do this
print("string 1" +"string 2")
a="string 2"
print("string 1"+ a)
print("string 1 {}".format(a))
print("string 1 {}".format("string 2"))
print(f"string 1 {a}")
print("sting 1" + " string 2")
"""
input1=int(input("Age:"))
value2=1
value3=input1 + value2
input2=input("profession:")
input3=input("Article:")
madlib=f"I am {input1} years old.Next year I will be {value3} years old.\
I  am {input3} {input2}."
print(madlib)

