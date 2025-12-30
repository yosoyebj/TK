import tkinter as tk
from tkinter import ttk, messagebox

def calculate_split():
    try:
        # Get inputs
        tokens1_str = entry_tokens1.get()
        tokens2_str = entry_tokens2.get()
        total_money_str = entry_money.get()

        if not tokens1_str or not tokens2_str or not total_money_str:
            messagebox.showerror("Lỗi (Error)", "Vui lòng điền đầy đủ thông tin.\n(Please fill in all fields.)")
            return

        tokens1 = float(tokens1_str)
        tokens2 = float(tokens2_str)
        total_money = float(total_money_str)

        total_tokens = tokens1 + tokens2
        
        if total_tokens == 0:
             messagebox.showerror("Lỗi (Error)", "Tổng số token không thể bằng 0.\n(Total tokens cannot be zero.)")
             return

        # Calculate percentages
        percent1 = (tokens1 / total_tokens) * 100
        percent2 = (tokens2 / total_tokens) * 100

        # Calculate money share
        share1 = (percent1 / 100) * total_money
        share2 = (percent2 / 100) * total_money

        # Update labels with formatted currency
        result_label_1.config(text=f"asian_puppy: {percent1:.2f}%  ➜  ${share1:,.2f}")
        result_label_2.config(text=f"angel_jakes: {percent2:.2f}%  ➜  ${share2:,.2f}")

    except ValueError:
        messagebox.showerror("Lỗi (Error)", "Vui lòng nhập số hợp lệ.\n(Please enter valid numbers.)")

# Main Window setup
root = tk.Tk()
root.title("Công cụ chia tiền Token (Token Splitter)")
root.geometry("480x450")
root.resizable(False, False)

# --- DARK THEME STYLING ---
BG_COLOR = "#2D2D2D"
FG_COLOR = "#FFFFFF"
ACCENT_COLOR = "#007ACC"
ENTRY_BG = "#3E3E3E"
ENTRY_FG = "#FFFFFF"

root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use('clam')

# Configure generic styles
style.configure("TFrame", background=BG_COLOR)
style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR, font=("Segoe UI", 11))
style.configure("TButton", background=ACCENT_COLOR, foreground="white", font=("Segoe UI", 11, "bold"), borderwidth=0)
style.map("TButton", background=[("active", "#005f9e")]) # Darker blue on hover

style.configure("TLabelFrame", background=BG_COLOR, foreground=FG_COLOR, font=("Segoe UI", 10, "bold"))
style.configure("TLabelFrame.Label", background=BG_COLOR, foreground=FG_COLOR)

style.configure("TEntry", fieldbackground=ENTRY_BG, foreground=ENTRY_FG, insertcolor="white", borderwidth=1)

# Container
frame = ttk.Frame(root, padding="30")
frame.pack(fill=tk.BOTH, expand=True)

# Header
header_label = ttk.Label(frame, text="PHÂN CHIA DOANH THU\n(Token Revenue Split)", font=("Segoe UI", 16, "bold"), justify=tk.CENTER)
header_label.pack(pady=(0, 30))

# Inputs
input_frame = ttk.Frame(frame)
input_frame.pack(fill=tk.X, pady=10)

# Input 1
ttk.Label(input_frame, text="Số token của asian_puppy:").pack(anchor=tk.W, pady=(5, 0))
entry_tokens1 = ttk.Entry(input_frame, font=("Segoe UI", 11))
entry_tokens1.pack(fill=tk.X, pady=(0, 10))

# Input 2
ttk.Label(input_frame, text="Số token của angel_jakes:").pack(anchor=tk.W, pady=(5, 0))
entry_tokens2 = ttk.Entry(input_frame, font=("Segoe UI", 11))
entry_tokens2.pack(fill=tk.X, pady=(0, 10))

# Total Money
ttk.Label(input_frame, text="Tổng số tiền nhận được ($):").pack(anchor=tk.W, pady=(5, 0))
entry_money = ttk.Entry(input_frame, font=("Segoe UI", 11))
entry_money.pack(fill=tk.X, pady=(0, 10))

# Calculate Button
calc_button = ttk.Button(frame, text="TÍNH TOÁN CHI TIỀN (CALCULATE)", command=calculate_split, cursor="hand2")
calc_button.pack(pady=20, fill=tk.X, ipady=5)

# Results
result_frame = ttk.LabelFrame(frame, text="  Kết quả (Results)  ", padding="15")
result_frame.pack(fill=tk.X, pady=10)

result_label_1 = ttk.Label(result_frame, text="asian_puppy: --", font=("Segoe UI", 12))
result_label_1.pack(anchor=tk.W, pady=5)

result_label_2 = ttk.Label(result_frame, text="angel_jakes: --", font=("Segoe UI", 12))
result_label_2.pack(anchor=tk.W, pady=5)

# Start App
root.mainloop()
