import math  

def main():
    A = int(input("Input A:"))
    B = int(input("Input B:"))
    result = pythag(A, B )
    print(result)


def pythag(A,B):
    c=(A**2)+(B**2)
    result= math.sqrt(c)
    return(c)
main()
