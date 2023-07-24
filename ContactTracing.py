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
# Show a confirmation message
# Create GUI window
# Load the app photo
# Create a label to display the app photo
# Entry fields
# Additional fields for positive cases
# Additional field for contact cases
# Save button
