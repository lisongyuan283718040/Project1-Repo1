class TestClassA:

    def funA1(self):
        print("ClassA funA1")

    def funA2(self):
        print("ClassA funA2")

    def funA3(self):
        print("ClassA funA3")
        
    def funEnd(self):
        print("The jenkins job dir is: /var/lib/jenkins/workspace/job1")

if __name__ == '__main__':
    TestClassA.funA1(self="funA1")
    TestClassA.funA2(self="funA2")
    TestClassA.funA3(self="funA3")
    TestClassA.funEnd(self="End")