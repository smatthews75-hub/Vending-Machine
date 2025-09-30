

# Vending Machine Mini Project
### A python CLI application for university issued mini project
### C.L.I stands for Command Line Interface, this CLI application will be using the terminal as the sole method to receive and display information.
---
## Priority Feature
1. greedy cashier algorithm
2. menu based Command Line Interface
3. money conversion IDR <=> SGD
4. cash dispence limit of 100 unit for each paper or coin
---
THIS is an unofficial group sketch to give a picture of what to make ! 



## Program Flow
1. Program enters MENU : (Probably a dedicated function to display the items)
```
--!-< Beverage n Snacks  Vending Machine >-!--
1. Mild Latte    Rp. 18K | 7. Krispr   Rp.  8K
2. Power Brew    Rp. 22K | 8. Chitota  Rp.  9K
3. Strong Kick   Rp. 30K | 9. Zheetos  Rp. 12K
4. Thirst Aid    Rp. 10K |10. Potebee  Rp. 10K
5. Fizz Wizz     Rp. 15K |11. Corn     Rp. 10K
6. Cringe Drink  Rp. 12K |12. Brocoli  Rp. 15K
-----< type the number of your choice ! >-----
```
#### That will be the item list menu, we'll think of better names later  
But to make a vending machine.. we need a fridge ! Something to store our items. In code, we gotta store its `name` and its `price`, where do we store it ? We need to learn how to use PYTHON DICTIONARIES !!! 
#### TODO : RESEARCH PYTHON DICTIONARIES to store variables that have multiple values inside them, each has a `name` and a `price`
lesser TODO : - Think of better item names - improve aesthetic ascii art.



---
---
---
2. Ask for USER INPUT ! receive: only number `int` of their Choice !  
> The user's choice is a number that corresponds to an item we have in vending machine's fridge

> Implement error handling to make sure no errors when user inputs something that is NOT of type `int` I'll teach you guys how to use `try` and `except` to cleverly handle potential errors.
#### TODO : RESEARCH `try` AND `except ValueError` BLOCKS for graceful error handling (try except blocks are called python's exception handling actually)

### Input handling behavior pseudocode
```
#1 GET user input
#2 CHECK if user input can be !safely converted to int using int()!
#if input is NOT an integer --> DO NOT PROCEED, ask again until input is valid
#if input IS a valid integer -> PROCEED to return the valid integer as choice
```
when we receive a valid choice, we need to match it with the corresponding item in the fridge... hmmm think abt how we'll use DICTIONARIES hmmmm
#### TODO : HOW TO MAKE an `int` Choice correspond to the item in the fridge that user chose? 
#### TODO : RESEARCH PYTHON `match case` BLOCKS to make life easier :)



---
---
---
3. DISPLAY the item's price, and ASK FOR THE USER'S MONEY to pay for it !
> but wait ! we are specified to have to accept two currency types !
#### Indonesian Rupiah -- IDR
```
Rp. 100,000     Rp. 2,000
Rp. 50,000      Rp. 1,000
Rp. 20,000      Rp. 500
Rp. 10,000      Rp. 200
Rp. 5,000       Rp. 100
```
#### Singaporean Dollars -- SGD
```
$ 100 dollars   $ 1 dollar = 100 cents
$ 50 dollars    $ 50 cents = 0.5 dollar
$ 10 dollars    $ 20 cents = 0.2 dollar
$ 5 dollars     $ 10 cents = 0.1 dollar
$ 2 dollars     $ 5 cents = 0.05 dollar
```
> we need to show the item's price, and make a variable to store the money that the user gave. We'll call it `user_money`