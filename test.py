# a = 3
# print(f"iam{a}")

def sum(n):
    if n<=0:
        return n
    return n+sum(n-1)


print(sum(3))


print("Hi")