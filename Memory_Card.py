# Імпорт потрібних класів із бібліотеки PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
QHBoxLayout, QVBoxLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel, QButtonGroup)
from random import shuffle,  randint


from random import shuffle
# Створюємо головний застосунок (обов’язково для PyQt5)
app = QApplication([])




#Класс
class Question():
     def __init__(self, ques, right_answer, wrong1, wrong2, wrong3):
          self.ques = ques
          self.right_answer = right_answer
          self.wrong1 = wrong1
          self.wrong2 = wrong2
          self.wrong3 = wrong3









# Створюємо головне вікно програми
window = QWidget()
window.resize(800, 500)
window.setWindowTitle("Memory card")

# Створюємо основні елементи інтерфейсу
question = QLabel("Переклади англійською слово автомобіль")
btn_ok = QPushButton("Answer")

# === ГРУПА З ВАРІАНТАМИ ВІДПОВІДЕЙ ===
RadioGroupBox = QGroupBox("Варіанти відповідей")

# Створюємо радіокнопки (можна обрати лише одну)

rbtn1 = QRadioButton("Bus")
rbtn2 = QRadioButton("Car")
rbtn3 = QRadioButton("Tax")
rbtn4 = QRadioButton("Shu")


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

# --- Внутрішній макет для кнопок ---
ans_hline = QHBoxLayout()
ans_vline1 = QVBoxLayout()
ans_vline2 = QVBoxLayout()

# Додаємо кнопки в колонки
ans_vline1.addWidget(rbtn1)
ans_vline1.addWidget(rbtn2)
ans_vline2.addWidget(rbtn3)
ans_vline2.addWidget(rbtn4)

# Додаємо обидві колонки у горизонтальний ряд
ans_hline.addLayout(ans_vline1)
ans_hline.addLayout(ans_vline2)

# Встановлюємо розмітку для групи з відповідями
RadioGroupBox.setLayout(ans_hline)

# === ГРУПА З РЕЗУЛЬТАТОМ ТЕСТУ ===
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?')
lb_Correct = QLabel('the answer will be here!')

# Створюємо вертикальну розмітку для результатів
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)

# === ОСНОВНЕ РОЗТАШУВАННЯ ВІКНА ===
v_line = QVBoxLayout()

# Горизонтальні блоки для окремих частин
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()

# --- Заповнюємо блоки ---
h1_line.addWidget(question, alignment=Qt.AlignHCenter)
h2_line.addWidget(RadioGroupBox)
h2_line.addWidget(AnsGroupBox)

AnsGroupBox.hide()

# Центруємо кнопку внизу
h3_line.addStretch(1)
h3_line.addWidget(btn_ok, stretch=2)
h3_line.addStretch(1)

# --- Збираємо всі частини разом ---
v_line.addLayout(h1_line, stretch=2)
v_line.addLayout(h2_line, stretch=8)
v_line.addStretch(1)
v_line.addLayout(h3_line, stretch=1)
v_line.addStretch(1)
v_line.addSpacing(5)


#def




def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Наступне питання")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()

    btn_ok.setText("Answer")

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)


    

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

window.cur_question = -1

question_list = []

question_list.append(Question("Як буде печиво на англійськи?", "cookie", "car", "strawberry", "shark", ))
question_list.append(Question("Що п'ють корови?", "вода", "молоко", "мед", "олія", ))
question_list.append(Question("Що таке вода в химії?", "H2O", "O2", "H", "RO", ))
question_list.append(Question("Як буде ворона на англійськи?", "crow", "sparrow", "fish", "wolf", ))





def next_question():
     window.total += 1
     cur_question =  randint(0, len(question_list) - 1)
     q = question_list[cur_question]
     print(window.total, window.score)

     ask(q)


def click_OK():
     if btn_ok.text() == "Answer":
          check_answer()
     else:
          next_question()


def ask(q: Question):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)    
        answers[2].setText(q.wrong2)    
        answers[3].setText(q.wrong3)

        question.setText(q.ques)
        lb_Correct.setText(q.right_answer)
        show_question()

def show_correct(res):
     lb_Result.setText(res)
     show_result()
     
def check_answer():
     if answers[0].isChecked():
          show_correct("Правильно")
          window.score += 1
          print("Вьсого питань:", window.total, "Балів:", window.score)
          print(window.score / window.total * 100, "%")
     else:
          if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
               show_correct("Неправильно")
               print("Вьсого питань:", window.total, "Балів:", window.score)
               print("Рейтінг:", window.score / window.total * 100, "%")
        




           

btn_ok.clicked.connect(click_OK)

window.score = 0
window.total = 0

next_question()



window.setLayout(v_line)

# Показуємо вікно
window.show()


app.exec()