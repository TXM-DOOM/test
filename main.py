def verify_admin(password):
    if password == "68af404b513073584c4b6f22b6c63e6b":
        print("Entering Diagnostic Mode...")
        return True
    print("Incorrect Password!")
    return False
def main():
    sum = 0
    numbers = eval(input("Enter a space-separated list of numbers: "))
    for num in numbers:
        sum = sum + num
    print(f"Sum of {numbers} = {sum}")
main() 