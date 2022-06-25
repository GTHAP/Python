class myclass:
    def func1(self):
            print("Method 1")

    def func2(self, somestring):
            print("Method 2" + " " + somestring)

class childclass(myclass):
    def func1(self):
        myclass.func1(self)
        print("Child class method 1")

    def func2(self, somestring):
        print("Child class" + " " + somestring)

def main():

    c = myclass()
    c.func1()
    c.func2("This is the end")

    c2 = childclass()
    c2.func1()
    c2.func2("This is the end of the second class")

if __name__ == "__main__":
    main()
