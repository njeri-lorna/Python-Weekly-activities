try:
    # Open employee file
    f = open("employees.txt", "r")

    # Read and display contents
    contents = f.read()
    print(contents)

    f.close()

except FileNotFoundError:
    print("The employee file was not found.")

finally:
    print("File processing completed.")
