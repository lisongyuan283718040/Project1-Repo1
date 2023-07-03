class TestClassB:

    def funB1(self):
        print("ClassB funB1")

    def funB2(self):
        print("ClassB funB2")

    def funB3(self):
        print("ClassB funB3")
        
    def funEnd(self):
        print("The jenkins job dir is: /var/lib/jenkins/workspace/jobn")

if __name__ == '__main__':
    TestClassB.funB1(self="funB1")
    TestClassB.funB2(self="funB2")
    TestClassB.funB3(self="funB3")
    TestClassB.funEnd(self="End")