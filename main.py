import time

choice = ''

while choice != "exit":
    print(f"""
                                Menu
    -----------------------------------------------------------------
    1) Shift Cipher
    2) Affine Cipher
    3) Vignere Cipher\n""")

    print('[Type "exit" at any time to quit the program, even if inside a cipher program]')
    choice = input("Which cipher do you wish to use? >")

    if not choice.isdigit() or int(choice) not in [1, 2, 3]:
        if choice == "exit":
            continue
        print("\nEnter a valid option!")
        time.sleep(2)

    elif int(choice) == 1:
        print(f"""
                                  Shift Cipher
       -----------------------------------------------------------------\n""")

    elif int(choice) == 2:
        print(f"""
                                  Affine Cipher
        -----------------------------------------------------------------\n""")

    elif int(choice) == 3:
        print(f"""
                                  Vignere Cipher
        -----------------------------------------------------------------\n""")
