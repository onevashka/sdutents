import logging
import argparse
import csv


parser = argparse.ArgumentParser(description="lets go")
parser.add_argument("csv_file", type=str, help="Path csv file")
args = parser.parse_args()

FORMAT =    "{levelname:<6} - {asctime}.\nВ модуле '{name}'"\
            "В строке {lineno:03d} функция '{funcName}()'"\
            "В {created} секунд записала сообщение: {msg}"
logging.basicConfig(format=FORMAT, style="{", level=logging.INFO, filename="students.log", encoding="utf-8")


class Student:


    def __init__(self, name, subject_file):

        self.name = name
        self.subject = {}
        self.load_subjects(subject_file)

    def load_subjects(self, subjects_file):
        logging.info(f"Loading subjects from file: {subjects_file}")
        with open(subjects_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for sub in reader:
                for i in sub:
                    self.subject[i] = {"grade" : [], "test_score" : []}
    
    def __setattr__(self, name, value):
        if name == "name":
            if not value.isalpha() and not value.istitle():
                raise ValueError(f"ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subject:
            return self.subject[name]
        else:
            raise ValueError(f"Предмет {name} не найден")

    def __str__(self):
        
        sub = []
        for key, value in self.subject.items():
            if value["grade"] or value["test_score"]:
                sub.append(key)
        subs = ", ".join(sub)
        return f"Студент: {self.name}\nПредметы: {subs}"           
            
    def add_grade(self, subject, grade):
        logging.info()
        if subject in self.subject: 
            if 2 <= grade <= 5:
                self.subject[subject]["grade"].append(grade)
            else:
                raise ValueError(f"Оценка должна быть целым числом от 2 до 5")
        else:
            raise ValueError(f"Предмет {subject} не найден") 

    def add_test_score(self, subject, test_score):
        logging.info()
        if subject in self.subject: 
            if 0 <= test_score <= 100:
                self.subject[subject]["test_score"].append(test_score)
            else:
                raise ValueError(f"Результат теста должен быть целым числом от 0 до 100")
        else:
            raise ValueError(f"Предмет {subject} не найден")

    def get_average_test_score(self, subject):
        logging.info(f"Loading get average score for subject {subject}")
        if subject in self.subject:
            count_test_score = self.subject[subject]["test_score"]
            return sum(count_test_score) / len(count_test_score)
        else:
            raise ValueError(f"Предмет {subject} не найден")
        
    def get_average_grade(self):
        logging.info()
        count_grade = []

        for sub in self.subject:
            count_grade.extend(self.subject[sub]["grade"])
        return sum(count_grade) / len(count_grade)
    

user1 = Student("Gdfgfdd Ggfhfgh", "subject.csv")