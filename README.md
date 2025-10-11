# Vending Machine Mini Project (upgraded version)
### A python CLI application. This is an upgraded version of the vending machine program from branch `main`

This version features the lifted restriction of the 25 characters only for the big_string structure, allowing 'Owners' of the vending machine to add any product of any length - as long as it has the correct order and format of data fields.  

This version still holds true to the original requirements of the vending machine project, and is an improvement on the original codebase. 

We are aware that many of the code implementation in this project can be improved, we have considered many ways to improve efficiency and effectiveness of the source code. However, maintaining compliance with the requirements of only making use of material already covered in lectures, this is as far as the project goes. We are open to suggestions and improvements, we express our utmost gratitude, thank you.

## Presented by Team 3 : 
- Stephen Matthews (252404175)
- Dearryl Jeremiah Mawuntu (252410907)
- Wilson Leonardo (252502509)
- Chiara Clover Gunawan (252404486)
---

# The Purpose of this Mini Project
This project explores the end-to-end development of a complete program themed around a vending machine. In the process, we translate the conceptual mechanics of how vending machines work into structured series of instructions to execute with the Python programming language. The python version used in production of this project's source code is `Python 3.12.2`, though strictly adhering to the scope of material covered in lectures from IBDA1011.

## Requirements to run this program
1. The minimum stable version of Python to run this program is predicted to be `Python 3.6` and above, likely due to the use of f-strings. This is based on automated analysis of this source code with `vermin 1.6.0` results shown below:
```bash
Minimum required versions: 3.6
Incompatible versions:     2
```
Or web based alternative through github codespaces with the `Python 3.12` devcontainer preset on this repository.
# Priority Features
1. Greedy cashier algorithm
> The machine should receive any value of currency as payment and effectively compute how much cash to return with the least bank notes required.
2. Menu based Command Line Interface
> For this project, it will be in the form of a simple terminal/command-line based interaction, no UI/UX development yet. It will rely on the `input()` function in python for prompting user input and `print()` to display text information.
3. Money conversion IDR <=> SGD
> An additional feature to this vending machine is the support for 2 types of currency transactions, either business with IDR Indonesian rupiah or SGD Singaporean dollars. The customer can choose to proceed transaction in IDR or SGD. The vending machine can be set in the source code to adapt the conversion between the two currencies as means of simulating the ever changing exchange rate of currencies in the real world.
4. Cash dispense limit of 100 unit for each paper or coin
> Realistically, the machine would also have a limited amount of banknotes to give change to the customer. So the stock of how much banknotes the machine has is also tracked and can be set in the source code dynamically.
---
## Additional Notes
- This project is made for educational purposes only, and is not intended for commercial use. We don't even think it is useful in any commercial way. This program is not made to be connected to any hardware, and is only a simulation of how a vending machine works.