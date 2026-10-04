try:
    a = int(input("Enter a number: "))
    print(10 / a)

except:
    print("An error occurred")

else:
    print("No error occurred")

finally:
    print("This will always run")
