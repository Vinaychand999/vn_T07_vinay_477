
   # writing a program to reverse alphabets and symbols should be ignored

def reverseString(char):
    index = -1

    # Looping  from  the last index until half of the index
    for i in range(len(char) - 1, int(len(char) / 2), -1):

        # match character is alphabet or not
        if char[i].isalpha():
            temp = char[i]
            while True:
                index += 1
                if char[index].isalpha():
                    char[i] = char[index]
                    char[index] = temp
                    break
    return char

# code
string = "ab@e#cd!ef"
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))




 #  writing  a program to remove zeros from an ip address
def ipString(str1):
    str2 = ""
    for i in str1:
        if i != "0":
            str2 = str2+i
    return str2

print(ipString(input("Enter the IP address: ")))


