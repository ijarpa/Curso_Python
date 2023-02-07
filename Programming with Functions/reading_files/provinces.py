

def main():
    # Read the contents of a text file named
    # provinces.txt into a list named provinces_list.
    provinces_list = read_list("./provinces.txt")

    # As a debugging aid, print the entire list.
    print(provinces_list)

    # Remove the first element from the list.
    provinces_list.pop(0)
    #print(provinces_list)

    # Remove the last element from the list.
    provinces_list.pop()
    #print(provinces_list)

    # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    #print(provinces_list)

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")


def read_list(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
