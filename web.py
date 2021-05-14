# i = 1
# while i < 6:
#     print(i)
#     print("Nigeria")
#     i = i < 1

#     if i ==3:
#         break


# fruits = ["apple", "banana", "mango", "pineapple"]
# for x in fruits:
#     print (x[0:2])
#     # break

# def classroom(a):
#     print("boys")
    
# classroom("girls")

class car:
    b = "car"
    def __init__(self, a):
        print("hello fellows" + a)
    # @Staticmethod
    def brake():
        print("how're you doing today")
    
    def gear(self):
        print("hope ciding is interesting")

benz = car("hello")
print (benz.b)
car.brake()
benz.gear()