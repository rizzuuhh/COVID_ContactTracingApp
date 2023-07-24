import tkinter as tk
import csv
import os

# Get entry from user
def save_entry():
    status = test_status.get()
    name = name_entry.get()
    address = address_entry.get()
    birthday = birthday_entry.get()
    age = age_entry.get()
    sex = sex_var.get()
    phone_number = phone_entry.get()

    if status == "Positive":
        exposed_date = exposed_date_entry.get()
        close_contacts = close_contacts_entry.get()
    # Save data to the CSV file
        with open("contact_tracing.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([status, name, address, birthday, age, sex, phone_number, exposed_date, close_contacts])
    else:
        symptoms = symptoms_entry.get()


        # Save data to the CSV file
        with open("contact_tracing.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([status, name, address, birthday, age, sex, phone_number, symptoms])
        
    # Show a confirmation message
    confirmation_label.config(text="Data saved successfully!", fg="green")

# Create GUI window
window = tk.Tk()
window.title("COVID Contact Tracing App")
window.geometry("1000x1000")

# Load the app photo
app_photo = tk.PhotoImage(file="c:\\Users\\SAMSUNG\\Downloads\Black Illustration Covid Virus Facebook Post.png")

# Create a label to display the app photo
app_photo_label = tk.Label(window, image=app_photo)
app_photo_label.place(x=0, y=0)  

# Entry fields
# Additional fields for positive cases
# Additional field for contact cases
# Save button 