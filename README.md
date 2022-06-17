## Password Generator

This is a simple password generator based on random. 

Symbols for create password choosing from 4 lists:
+ Lower case list = abcdefghijklmnopqrstuvwxyz
+ Upper case list = ABCDEFGHIJKLMNOPQRSTUVWXYZ
+ List of numbers = 1234567890
+ List of special symbols = !@#$%^&*()?-=_+[]{}

Main loop always using the lower case list, if user want to use other list, lower case list will extends with new list.

```Python
for _ in range(length):
    password += random.choice(start_list) 
 ```

###  QT Designer for UI

User Interface was created in QT Designer and converted from **.ui** to **.py** with external tool in PyCharm. 

### Clone project
``` 
git clone https://github.com/ReyKoll/Password_Generator.git 
```
___
