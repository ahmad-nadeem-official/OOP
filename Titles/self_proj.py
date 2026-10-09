class student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def disp(self):
        num_of_questions = 0
        print(f"today we have a student with us {self.name} and his age is {self.age} and currently he is studying {self.course}")
        while True:
           ques = input(f" {self.name}, please ask your question: ")
           if ques == "exit" or ques == "" or ques == "quit"or ques == "stop" or ques == "end":
             print(f"Mr {self.name}, at your age of {self.age}, you have asked {num_of_questions} questions today, thank you for your time") 
             break
           else : 
             print("that a nice question, we will answer it soon")  
             num_of_questions += 1 

student1 = student("Ahmad", 20, "Python")
student2 = student("ali", 20, "java")
student3 = student("ahmad", 20, "C++")