#DiceRoll.py
#Name: Jack Schulz
#Date: 2-26-2025
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  totalRolls = 10000
  for r in range(totalRolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    total = dice1 + dice2
    #find the sum total of the two dice
    rolls[total - 2] = rolls[total - 2] + 1
  
  
  #print statictics for dice rolls
  dice = 2
  for count in rolls:
    print(dice, ":",   count, "; That is", str(round(count / totalRolls * 100)) + "%")

    dice = dice + 1


if __name__ == '__main__':
  main()
