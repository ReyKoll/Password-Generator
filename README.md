# Password Generator

This is a simple password generator based on random. 

Symbols for create password choosing from 4 lists:
+ Lower case list = abcdefghijklmnopqrstuvwxyz
+ Upper case list = ABCDEFGHIJKLMNOPQRSTUVWXYZ
+ List of numbers = 1234567890
+ List of special symbols = !@#$%^&*()?-=_+[]{}

Main loop always using the lower case list, if user want to use other list, lower case list will extends with new list.

```Python
if self.check_upper.isChecked():
    start_list.extend(upper_list)
if self.check_number.isChecked():
    start_list.extend(number_list)
if self.check_special.isChecked():
    start_list.extend(special_list)
elif not self.check_upper.isChecked() and 
    self.check_number.isChecked() and 
    self.check_special.isChecked():
        start_list = password
```

```Python
for _ in range(length):
    password += random.choice(start_list) 
 ```
___

##  QT Designer for UI

User Interface was created in QT Designer and converted from **.ui** to **.py** with external tool in PyCharm. 

There is another way to convert. <br>
***Use next syntax and make sure that the file.ui and pyuic5.bat are in the same location of your project***
``` 
pyuic5 -x file.ui -o file.py
```

## Creating .exe using cx_freeze
For creating an .exe file to build standalone project was used [cx_freeze](https://github.com/marcelotduarte/cx_Freeze) <br>
Settings for build located in **setup.py**.

***Run a setup.py script***
```
 python setup.py build
```

### Clone
``` 
git clone https://github.com/ReyKoll/Password_Generator.git 
```
___
