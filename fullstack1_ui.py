
from tkinter import *
import requests
import json

# def send_data():
#     name = entry1.get()  # Get text from entry field
#     url = "http://127.0.0.1:8000/submit/"
#     data = {"name": name}  # Create JSON data
#     headers = {"Content-Type": "application/json"}  # Set headers for JSON

#     try:
#         response = requests.post(url, data=json.dumps(data), headers=headers)
#         if response.status_code == 200:
#             print("Success:", response.json())  # Print server response
#         else:
#             print("Failed:", response.status_code, response.text)
#     except requests.exceptions.RequestException as e:
#         print("Error:", e)


def send_data():
    name = entry1.get()
    url = "http://127.0.0.1:8000/submit/"
    data = {"name": name} #create json data
    headers = {"Content-Type": "application/json"} #set header for json

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print ("success:", response.json()) #print server log
        else:
            print("Failed:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

root = Tk()
root.geometry("300x300")
root.title("Full Stack1")

label1 = Label(text="Name")
label1.pack(pady=10)

entry1 = Entry()
entry1.pack(pady=10)

btn1 = Button(text="Submit", command=send_data)
btn1.pack(pady=10)



root.mainloop()

