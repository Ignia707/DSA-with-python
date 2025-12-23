# print 5x5 stars
# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print("\n")


# print 1 star to 5 star, in 5 lines resp
# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print("\n")


# print 1  to 5 , in 5 lines resp
# for i in range(5):
#     for j in range(i+1):
#         print(j+1, end="")
#     print("\n")


# print 1 to 5, in 5 lines resp. One number per line
# for i in range(5):
#     for j in range(i+1):
#         print(i+1, end="")
#     print("\n")


# that 5 stars thingy inverted
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print("\n")


# that numbers thingy inverted  
# for i in range(5, 0, -1):
#     for j in range(i):
#         print(j+1, end="")
#     print("\n")


# odd number of stars, 5 lines
# for i in range(5):
#     print((4 - i) * " ", end="")
#     for j in range(0, 2*i + 1, 1):
#         print("*", end="")
#     print("\n")


# odd number of stars, 5 lines => inverted
# for i in range(4, -1, -1):
#     print((4 - i) * " ", end="")
#     for j in range(0, 2*i + 1, 1):
#         print("*", end="")
#     print("\n")


# diamond shaped, 10 line stars
count = 1
for i in range(10):
    for j in range(5):
        if count < 5:
            print((5 - count)" ")