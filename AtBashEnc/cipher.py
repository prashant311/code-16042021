import time
import threading

global data_list, new_list


def cipher_encryption(data, thr):

    print("start encryption for :", thr)
    crypt = ""
    for i in data:
        print("Thread :", thr, " : ", time.ctime(time.time()))
        char_x = ord(i)

        if ord('a') <= char_x <= ord('z'):
            char_y = ord('a') + ord('z') - char_x
            crypt = crypt + chr(char_y)

        elif ord('A') <= char_x <= ord('Z'):
            char_y = ord('A') + ord('Z') - char_x
            crypt = crypt + chr(char_y)

        else:
            crypt = crypt + i
    new_list[thr-1] = new_list[thr-1] + crypt


def save_file():
    file_name = "Result"
    f = open(file_name + "_Encrypted.txt", "w")
    f.write(new_list[0]+new_list[1]+new_list[2]+new_list[3])
    f.close()


def atbash_test():
    print("\nSelect one Option\n")
    print(
        "1. Go with Default Data\n2. Enter you data for encryption\n3. Enter files name with path")
    try:
        option = input()
        data = ""
        if option is "1":
            data = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together."
        elif option is "2":
            data = input("Enter your Text to encrypt")

        elif option is "3":
            print("Enter Single or Multiple Files Name with their path\nExample: C:/Data/file1.txt\n")
            file = input()
            if file is not "":
                try:
                    text_file = open(file, 'r')
                    data = text_file.read()
                except Exception as e:
                    print("Invalid file path :", e)
            else:
                print("You do not enter file names")

        else:
            print("You Enter invalid option")
            raise Exception

        length, parts = len(data), int(len(data) / 4)
        list_data = [data[i:i + parts] for i in range(0, length, parts)]
        return list_data

    except Exception as e:
        print("Exception :", e)


def timestamp():
    t = time.time()
    return time.ctime(t)


if __name__ == '__main__':
    print("Start at :", timestamp())
    new_list = ["", "", "", ""]
    data_list = atbash_test()
    thread1 = threading.Thread(target=cipher_encryption, args=(data_list[0],1))
    thread2 = threading.Thread(target=cipher_encryption, args=(data_list[1],2))
    thread3 = threading.Thread(target=cipher_encryption, args=(data_list[2],3))
    thread4 = threading.Thread(target=cipher_encryption, args=(data_list[3],4))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    save_file()
    print("Encryption Completed at : ", timestamp())

