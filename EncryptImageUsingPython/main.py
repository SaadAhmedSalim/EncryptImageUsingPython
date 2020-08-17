from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("300x200")
root.config(bg="blue")
root.title("Image Encoder")

def encrypt_image():
    # print("Test")
    file1 = filedialog.askopenfile(initialdir="/home/Documents/EncryptImageUsingPython/", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if file1 is not None:
        # print(file1)
        file_name = file1.name
        # print(file_name)
        key = entry1.get(1.0, END)
        print(file_name, key)
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index,values in enumerate(image):
            image[index] = values^int(key)
        fi1 = open(file_name,'wb')
        fi1.write(image)
        fi1.close()


btn_encrypt = Button(root, text="Encrypt/Decrypt", command=encrypt_image)
btn_encrypt.place(x=60, y=10)

entry1 = Text(root, height=1, width=18)
entry1.place(x=50, y=50)

root.mainloop()
