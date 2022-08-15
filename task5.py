
from num2words import num2words #to be able to use it run pip install num2words

for i in range(1, 101):
    if i % 10 == 0:
        print(num2words(i))
    else:
      print(str(i) + "\n")
  