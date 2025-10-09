# Vending Machine Mini Project
### A python CLI application for university issued mini project
### C.L.I stands for Command Line Interface, this CLI application will be using the terminal as the user interaction medium to receive and display information.

## Presented by Team 3 : 
- Stephen Matthews (252404175)
- Dearryl Jeremiah Mawuntu (252410907)
- Wilson Leonardo (252502509)
- Chiara Clover Gunawan (252404486)
---

# The Purpose of this Mini Project
This project is aimed to explore the process of developing a complete program with the theme of making a vending machine. Procedurely translating the conceptual ideas of how a vending machine works into structured series of instructions to execute with the Python programming langguage. The python version used in production of this project's source code is `Python 3.12.2` with the restriction of using only the material already tought in our lectures.

## Requirements to run this program
1. The minimum stable version of Python to run this program is predicted to be `Python 3.6` and above. This is based on automated analysis of this source code with `vermin 1.6.0` results shown below:
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
- An in depth explanation of the whole structure of this program can be found in the `Source-Code-Breakdown.ipynb` file in this repository.
- This project is made for educational purposes only, and is not intended for commercial use. We don't even think it is useful in any commercial way. This program is not made to be connected to any hardware, and is only a simulation of how a vending machine works.