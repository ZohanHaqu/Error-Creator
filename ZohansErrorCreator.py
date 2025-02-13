import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Function to create the VBS script for the error message
def create_vbs(title, icon, message):
    # Map the icon to the correct VBS code (Error, Warning, Information)
    if icon == "Error":
        icon_code = 16  # Critical Error icon
    elif icon == "Warning":
        icon_code = 48  # Warning icon
    elif icon == "Information":
        icon_code = 64  # Information icon
    else:
        icon_code = 64  # Default to Information

    # Create the VBS code for the popup
    vbs_code = f'''Set objMessage = CreateObject("WScript.Shell")
objMessage.Popup "{message}", 10, "{title}", {icon_code}'''

    # Ask the user where to save the VBS file
    file_path = filedialog.asksaveasfilename(defaultextension=".vbs", filetypes=[("VBScript files", "*.vbs")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(vbs_code)
        messagebox.showinfo("Success", "VBS file created successfully!")

# Function to simulate a test error
def test_error(title, icon, message):
    if icon == "Error":
        messagebox.showerror(title, message)
    elif icon == "Warning":
        messagebox.showwarning(title, message)
    elif icon == "Information":
        messagebox.showinfo(title, message)

# Tkinter window setup
root = tk.Tk()
root.title("Zohans Error Creator")

# Set the window icon to the custom icon (if the file exists)
root.iconbitmap(r"C:\Users\zohan\Downloads\Icon\icon.ico")

# Set up the window size and position
root.geometry("400x350")

# Label
label = tk.Label(root, text="Create a Custom Error", font=("Arial", 14))
label.pack(pady=10)

# Title Label and Entry
title_label = tk.Label(root, text="Error Title:")
title_label.pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

# Error message Label and Entry
message_label = tk.Label(root, text="Error Message:")
message_label.pack()
message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

# Error Icon Selection
icon_label = tk.Label(root, text="Error Icon:")
icon_label.pack()

icon_var = tk.StringVar(value="Information")  # Default to Information
icon_error = tk.Radiobutton(root, text="Error", variable=icon_var, value="Error")
icon_warning = tk.Radiobutton(root, text="Warning", variable=icon_var, value="Warning")
icon_information = tk.Radiobutton(root, text="Information", variable=icon_var, value="Information")

icon_error.pack()
icon_warning.pack()
icon_information.pack()

# Buttons for Test Error and Save as VBS
test_button = tk.Button(root, text="Test Error", command=lambda: test_error(title_entry.get(), icon_var.get(), message_entry.get()), width=20)
test_button.pack(pady=10)

save_button = tk.Button(root, text="Save as VBS", command=lambda: create_vbs(title_entry.get(), icon_var.get(), message_entry.get()), width=20)
save_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()

