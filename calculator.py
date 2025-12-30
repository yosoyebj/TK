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
        
        # Update labels directly - IMPROVED FORMATTING
        # Using 0 decimal places for VND as is standard
        result_lbl_1.config(text=f"asian_puppy:\n{percent1:.1f}%   =   {share1:,.0f} VND")
        result_lbl_2.config(text=f"angel_jakes:\n{percent2:.1f}%   =   {share2:,.0f} VND")
        
    except ValueError:
        messagebox.showerror("Lỗi (Error)", "Vui lòng nhập số hợp lệ.\n(Please enter valid numbers.)")

# Main Window setup
root = tk.Tk()
root.title("Token Splitter (VND)")
root.geometry("600x750") # Increased size significantly
root.resizable(True, True) 

# --- DARK THEME STYLING ---
BG_COLOR = "#2D2D2D"
FG_COLOR = "#FFFFFF"
ACCENT_COLOR = "#007ACC"
ENTRY_BG = "#3E3E3E"
ENTRY_FG = "#FFFFFF"
RESULT_COLOR = "#69F0AE" # Bright Mint Green

root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use('clam')

# Configure generic styles
style.configure("TFrame", background=BG_COLOR)
style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR, font=("Arial", 14)) # Larger font
style.configure("TButton", background=ACCENT_COLOR, foreground="white", font=("Arial", 14, "bold"), borderwidth=0)
style.map("TButton", background=[("active", "#005f9e")])

style.configure("TLabelFrame", background=BG_COLOR, foreground=FG_COLOR, font=("Arial", 12, "bold"))
style.configure("TLabelFrame.Label", background=BG_COLOR, foreground=FG_COLOR)

style.configure("TEntry", fieldbackground=ENTRY_BG, foreground=ENTRY_FG, insertcolor="white", borderwidth=1)

# Container
frame = ttk.Frame(root, padding="40") # More padding
frame.pack(fill=tk.BOTH, expand=True)

# Header
header_label = ttk.Label(frame, text="PHÂN CHIA DOANH THU\n(Token Revenue Split)", font=("Arial", 20, "bold"), justify=tk.CENTER)
header_label.pack(pady=(0, 30))

# Inputs
input_frame = ttk.Frame(frame)
input_frame.pack(fill=tk.X, pady=10)

# Input 1
ttk.Label(input_frame, text="Số token của asian_puppy:").pack(anchor=tk.W, pady=(10, 0))
entry_tokens1 = ttk.Entry(input_frame, font=("Arial", 14))
entry_tokens1.pack(fill=tk.X, pady=(0, 15))

# Input 2
ttk.Label(input_frame, text="Số token của angel_jakes:").pack(anchor=tk.W, pady=(10, 0))
entry_tokens2 = ttk.Entry(input_frame, font=("Arial", 14))
entry_tokens2.pack(fill=tk.X, pady=(0, 15))

# Total Money
ttk.Label(input_frame, text="Tổng số tiền nhận được (VND):").pack(anchor=tk.W, pady=(10, 0))
entry_money = ttk.Entry(input_frame, font=("Arial", 14))
entry_money.pack(fill=tk.X, pady=(0, 15))

# Calculate Button
calc_button = ttk.Button(frame, text="TÍNH TOÁN (CALCULATE)", command=calculate_split, cursor="hand2")
calc_button.pack(pady=30, fill=tk.X, ipady=15)

# Results
result_frame = tk.LabelFrame(frame, text="  Kết quả (Results)  ", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 12, "bold"), padx=20, pady=20, borderwidth=1, relief="solid")
result_frame.pack(fill=tk.X, pady=10)

# Large, readable text
# Added wraplength to ensure it fits if window is resized
result_lbl_1 = tk.Label(result_frame, text="asian_puppy: --", font=("Arial", 16, "bold"), bg=BG_COLOR, fg=RESULT_COLOR, anchor="w", justify=tk.LEFT, wraplength=500) 
result_lbl_1.pack(fill=tk.X, pady=10)

tk.Frame(result_frame, height=1, bg="#555555").pack(fill=tk.X, pady=5) # Separator line

result_lbl_2 = tk.Label(result_frame, text="angel_jakes: --", font=("Arial", 16, "bold"), bg=BG_COLOR, fg=RESULT_COLOR, anchor="w", justify=tk.LEFT, wraplength=500)
result_lbl_2.pack(fill=tk.X, pady=10)

# Start App
root.mainloop()
