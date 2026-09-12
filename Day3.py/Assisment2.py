marks = [99,89,96,98,96,98]

# Avg =( marks[0] +marks[1] +marks[2]) / 3
# print(f"marks of these Three number us :{Avg}")


def computer_avg(number):
    if not number:
        return 0
    return sum(number) / len(number)


user_input = int(input("Enter the number"))
nums = 