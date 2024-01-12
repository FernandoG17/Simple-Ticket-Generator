import tkinter as tk
import imaplib
import email
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


imap_server = 'imap.gmail.com'
email_id = "YOUREMAIL@EMAIL.com"
password = "YOURPASSWORD"

def clean():
        nameEntry.delete(0,tk.END)
        contactEntry.delete(0,tk.END)
        emailEntry.delete(0,tk.END)
        requestEntry.delete(0,tk.END)
        descriptionEntry.delete("1.0", tk.END)

def send_email():
    name = nameEntry.get()
    contact_number = contactEntry.get()
    email_address = emailEntry.get()
    request_type = requestEntry.get()
    description = descriptionEntry.get("1.0", tk.END)

    ticketNum = random.randint(800, 1000)

    subject = f"Ticket Request No. {ticketNum}- {request_type} from {name}"
    body = f"Contact Number: {contact_number}\nEmail Address: {email_address}\n\nDescription:\n{description}"

    with smtplib.SMTP('smtp.gmail.com',587) as server: 
        server.starttls()
        server.login(email_id, password)

        to_email_address = 'IT@EMAIL.COM'
        message = MIMEMultipart()
        message['From'] = email_id
        message['To'] = to_email_address
        message['Subject'] = subject
        message.attach(MIMEText(body,'plain'))
        server.sendmail(email_id, to_email_address, message.as_string())
        clean()
        success.config(text=f"Request submitted successfully. Ticket No.{ticketNum}")
        print("Email sent successfully")




# Create a window
window = tk.Tk()
window.title("Ticket Generator")  # Set window title
window.geometry('580x500')

nameLabel = tk.Label(window, text="Name:")
nameLabel.grid(row = 0, column = 0, padx = 30, pady = 30)

nameEntry = tk.Entry(window)
nameEntry.grid(row=0, column=1)

contact = tk.Label(window, text = "Contact Number: ")
contact.grid(row =2, column = 0, padx = 30, pady = 5)

contactEntry = tk.Entry(window)
contactEntry.grid(row = 2, column = 1)

email = tk.Label(window, text = "Email: ")
email.grid(row = 3, column = 0, padx = 5, pady = 20)

emailEntry = tk.Entry(window)
emailEntry.grid(row = 3, column = 1)

typeRequest = tk.Label(window, text = "Type of request: ")
typeRequest.grid(row = 4, column = 0)

requestEntry = tk.Entry(window)
requestEntry.grid(row = 4, column = 1)

descriptionLabel = tk.Label(window, text = "Description: ")
descriptionLabel.grid(row = 5, column=0 , padx = 5, pady = 20)

descriptionEntry = tk.Text(window, width = 40, height = 10)
descriptionEntry.grid(row = 5, column = 1, padx = 5, pady = 20)

success = tk.Label(window)
success.grid(row = 7, column = 1)

button1 = tk.Button(window, text = "Send", command= send_email)
button1.grid(row = 6, column = 1)


# Run the main event loop
window.mainloop()
