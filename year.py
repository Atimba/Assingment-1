name = input("Enter your name: ")
num = int(input("Enter year of birth: "))

ans = 2023 - num

if ans >= 18:
        print("Dear Mr./Mrs.", name ,",you can vote.")
else:
        print("Dear Mr./Mrs.", name ,",you are under the required age for voting.")        