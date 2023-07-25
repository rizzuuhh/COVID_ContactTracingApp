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

# Test Status Frame
test_status_frame = tk.Frame(window, bg=background_color)
test_status_frame.pack()

# Test Status Frame
test_status_frame = tk.Frame(window, bg=background_color)
test_status_frame.pack() 

test_status_label = tk.Label(test_status_frame, text="Have you tested positive for COVID-19 or been in contact with someone who tested positive?", fg=text_color, bg=background_color)
test_status_label.pack(side=tk.LEFT)

test_status = tk.StringVar(value="Choose One")
test_status_options = ["Choose One", "Positive", "Contact"]
test_status_menu = tk.OptionMenu(test_status_frame, test_status, *test_status_options)
test_status_menu.pack(side=tk.LEFT)

# Entry fields
name_label = tk.Label(window, text="Name:", fg=text_color, bg=background_color)
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

address_label = tk.Label(window, text="Address:", fg=text_color, bg=background_color)
address_label.pack()
address_entry = tk.Entry(window)
address_entry.pack()

birthday_label = tk.Label(window, text="Birthday (MM/DD/YYYY):", fg=text_color, bg=background_color)
birthday_label.pack()
birthday_entry = tk.Entry(window)
birthday_entry.pack()

age_label = tk.Label(window, text="Age:", fg=text_color, bg=background_color)
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

sex_var = tk.StringVar(value="Choose One")
sex_label = tk.Label(window, text="Sex:", fg=text_color, bg=background_color)
sex_label.pack()
sex_options = ["Choose One", "Male", "Female", "Other"]
sex_menu = tk.OptionMenu(window, sex_var, *sex_options)
sex_menu.pack()

phone_label = tk.Label(window, text="Phone Number:", fg=text_color, bg=background_color)
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Additional fields for positive cases
exposed_date_label = tk.Label(window, text="Date of Exposure (MM/DD/YYYY):", fg=text_color, bg=background_color)
exposed_date_entry = tk.Entry(window)


close_contacts_label = tk.Label(window, text="Names and Contact Information of Close Contacts:", fg=text_color, bg=background_color)
close_contacts_entry = tk.Entry(window)
 
# Additional field for contact cases
symptoms_label = tk.Label(window, text="Symptoms:", fg=text_color, bg=background_color)
symptoms_entry = tk.Entry(window)

# Save button 
save_button = tk.Button(window, text="Save", command=save_entry, fg="white", bg=accent_color)
save_button.pack(pady=20)
 
 # Confirmation label
confirmation_label = tk.Label(window, text="", font=("Arial", 12), fg="green", bg=background_color)
confirmation_label.pack()

# Hide additional fields initially
exposed_date_label.pack_forget()
exposed_date_entry.pack_forget()
close_contacts_label.pack_forget()
close_contacts_entry.pack_forget()
symptoms_label.pack_forget()
symptoms_entry.pack_forget()



# Function to show/hide additional fields based on user input
def show_additional_fields(*args):
    if test_status.get() == "Positive":
        exposed_date_label.pack()
        exposed_date_entry.pack()
        close_contacts_label.pack()
        close_contacts_entry.pack()
        symptoms_label.pack_forget()
        symptoms_entry.pack_forget()
    elif test_status.get() == "Contact":
        exposed_date_label.pack_forget()
        exposed_date_entry.pack_forget()
        close_contacts_label.pack_forget()
        close_contacts_entry.pack_forget()
        symptoms_label.pack()
        symptoms_entry.pack()
    else:
        exposed_date_label.pack_forget()
        exposed_date_entry.pack_forget()
        close_contacts_label.pack_forget()
        close_contacts_entry.pack_forget()
        symptoms_label.pack_forget()
        symptoms_entry.pack_forget()

# Bind the show_additional_fields function to the status variable
test_status.trace("w", show_additional_fields)

window.mainloop()




