

def fun():
    print("This is fun in session19")

class CA:
    def __init__(self):
        print("object constructed")

def main():
    print("This is session19")
    print("Session19 __name__ is", __name__)
    fun()
    cref=CA()
if __name__=="__main__":
    main()