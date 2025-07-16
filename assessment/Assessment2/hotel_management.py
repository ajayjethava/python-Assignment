import tkinter as tk
from tkinter import messagebox
from db_connection import DatabaseConnection
from datetime import datetime

class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Customer(Person):
    def __init__(self, name, address, phone, checkin, checkout, balance):
        super().__init__(name, address, phone)
        self.checkin = checkin
        self.checkout = checkout
        self.__balance = balance

    def get_balance(self):
        return self.__balance

class HotelApp:
    def __init__(self, master):
        self.master = master
        master.title("Hotel Management System")
        master.geometry("600x500")
        master.configure(bg="#f0f0f0")

        self.db = DatabaseConnection()

        tk.Label(master, text="Hotel Management System", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

        tk.Button(master, text="Check-In Guest", command=self.check_in, bg="#4CAF50", fg="white", font=("Arial", 12), width=20).pack(pady=10)
        tk.Button(master, text="Show All Guests", command=self.show_guests, bg="#2196F3", fg="white", font=("Arial", 12), width=20).pack(pady=10)
        tk.Button(master, text="Check-Out Guest", command=self.check_out, bg="#FFC107", fg="black", font=("Arial", 12), width=20).pack(pady=10)
        tk.Button(master, text="Delete Guest", command=self.delete_guest, bg="#f44336", fg="white", font=("Arial", 12), width=20).pack(pady=10)
        tk.Button(master, text="Exit", command=self.exit_app, bg="#9E9E9E", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    def check_in(self):
        top = tk.Toplevel(self.master)
        top.title("Check-In Guest")
        top.geometry("400x400")
        top.configure(bg="#e0f7fa")

        labels = ["Name", "Address", "Phone", "Check-In Date (YYYY-MM-DD)", "Check-Out Date (YYYY-MM-DD)", "Balance"]
        entries = []

        for label_text in labels:
            tk.Label(top, text=label_text, bg="#e0f7fa").pack()
            entry = tk.Entry(top)
            entry.pack()
            entries.append(entry)

        def save_guest():
            try:
                values = [e.get().strip() for e in entries]
                if not all(values):
                    messagebox.showerror("Error", "All fields are required!")
                    return
                customer = Customer(*values[:3], values[3], values[4], float(values[5]))
                query = "INSERT INTO customers (name, address, phone, checkin_date, checkout_date, balance) VALUES (%s, %s, %s, %s, %s, %s)"
                self.db.execute(query, (customer.name, customer.address, customer.phone, customer.checkin, customer.checkout, customer.get_balance()))
                messagebox.showinfo("Success", "Guest Checked-In Successfully!")
                top.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")

        tk.Button(top, text="Save", command=save_guest, bg="#4CAF50", fg="white").pack(pady=10)

    def show_guests(self):
        top = tk.Toplevel(self.master)
        top.title("All Guests")
        top.geometry("500x400")
        top.configure(bg="#fff3e0")

        result = self.db.execute("SELECT * FROM customers")
        for row in result:
            tk.Label(top, text=str(row), bg="#fff3e0").pack()

    def check_out(self):
        top = tk.Toplevel(self.master)
        top.title("Check-Out Guest")
        top.geometry("300x200")
        top.configure(bg="#ede7f6")

        tk.Label(top, text="Enter Guest ID", bg="#ede7f6").pack()
        id_entry = tk.Entry(top)
        id_entry.pack()

        def process_checkout():
            try:
                guest_id = id_entry.get().strip()
                if not guest_id.isdigit():
                    messagebox.showerror("Error", "Invalid ID")
                    return
                query = "DELETE FROM customers WHERE id = %s"
                self.db.execute(query, (guest_id,))
                messagebox.showinfo("Success", f"Guest ID {guest_id} Checked-Out")
                top.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Checkout Failed: {e}")

        tk.Button(top, text="Check-Out", command=process_checkout, bg="#FFC107").pack(pady=10)

    def delete_guest(self):
        top = tk.Toplevel(self.master)
        top.title("Delete Guest")
        top.geometry("300x200")
        top.configure(bg="#ffebee")

        tk.Label(top, text="Guest ID", bg="#ffebee").pack()
        id_entry = tk.Entry(top)
        id_entry.pack()

        def confirm_delete():
            guest_id = id_entry.get().strip()
            if not guest_id.isdigit():
                messagebox.showerror("Error", "Invalid Guest ID")
                return
            if messagebox.askyesno("Confirm", f"Delete Guest ID {guest_id}?"):
                self.db.execute("DELETE FROM customers WHERE id = %s", (guest_id,))
                messagebox.showinfo("Deleted", f"Guest ID {guest_id} Deleted")
                top.destroy()

        tk.Button(top, text="Delete", command=confirm_delete, bg="#f44336", fg="white").pack(pady=10)

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.db.close()
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()
