print("I can guess the outcome, I'm actually reading your mind.")
first_number=input("choose a number between 1 - 9:")
first_number=int(first_number)
number=first_number
first_number*=2
first_number+=8
first_number+=number
first_number-=2
first_number//=3
first_number-=number
first_number*=4

print(first_number)