import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

class NLPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NLP Sentiment Analysis App")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")
        
        self.create_login_page()

    def create_login_page(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Login", font=("Helvetica", 24, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="Username", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        self.username = tk.Entry(frame, width=30, font=("Arial", 12), relief=tk.GROOVE, bd=3)
        self.username.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Password", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
        self.password = tk.Entry(frame, width=30, font=("Arial", 12), show="*", relief=tk.GROOVE, bd=3)
        self.password.grid(row=2, column=1, pady=5)

        tk.Button(frame, text="Login", command=self.login, width=15, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=20)
        tk.Button(frame, text="Signup", command=self.create_signup_page, width=15, bg="#2196F3", fg="white", font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=5)

    def create_signup_page(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Signup", font=("Helvetica", 24, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="Username", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        self.new_username = tk.Entry(frame, width=30, font=("Arial", 12), relief=tk.GROOVE, bd=3)
        self.new_username.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Password", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
        self.new_password = tk.Entry(frame, width=30, font=("Arial", 12), show="*", relief=tk.GROOVE, bd=3)
        self.new_password.grid(row=2, column=1, pady=5)

        tk.Button(frame, text="Signup", command=self.signup, width=15, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=20)
        tk.Button(frame, text="Back to Login", command=self.create_login_page, width=15, bg="#2196F3", fg="white", font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=5)

    def create_home_page(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Sentiment Analysis", font=("Helvetica", 24, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="Enter a paragraph:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        self.text_input = tk.Text(frame, height=8, width=40, font=("Arial", 12), relief=tk.GROOVE, bd=3)
        self.text_input.grid(row=2, column=0, columnspan=2, pady=5)

        tk.Button(frame, text="Analyze", command=self.analyze_sentiment, width=15, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def signup(self):
        username = self.new_username.get()
        password = self.new_password.get()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Signup successful!")
            self.create_login_page()

        conn.close()

    def login(self):
        username = self.username.get()
        password = self.password.get()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if cursor.fetchone():
            messagebox.showinfo("Success", "Login successful!")
            self.create_home_page()
        else:
            messagebox.showerror("Error", "Invalid credentials")

        conn.close()

    def analyze_sentiment(self):
        text = self.text_input.get("1.0", tk.END)
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        result = f"Sentiment Analysis:\n\nPositive: {sentiment['pos']}\nNegative: {sentiment['neg']}\nNeutral: {sentiment['neu']}\nOverall: {'Positive' if sentiment['compound'] >= 0 else 'Negative'}"
        messagebox.showinfo("Result", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = NLPApp(root)
    root.mainloop()
