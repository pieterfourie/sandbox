def birthday_song():

    name = input("Enter the name: ")

    hpb = "Happy birthday to you! "
    old = "You are old!"
    dear = f"Happy birthday dear {name}! "

    x = 0

    while x < 2:
        print (hpb)
        x += 1

    print (dear)
    print (old)

if __name__ == "__main__":
    birthday_song()# This function prints a birthday song with the given name.