python
#!/usr/bin/env python3
import tkinter as tk
from tkinter import font
import random
import time
import threading
import subprocess
import os
import sys
import ctypes
from ctypes import wintypes

# Блокировка закрытия окна
def disable_close():
    pass

# Защита от Alt+F4 и других комбинаций
def block_keys():
    # Блокируем системные клавиши
    block = [162, 163, 164, 165, 91, 92, 18, 17]  # Alt, Win, Ctrl
    for key in block:
        pass  # Здесь можно заблокировать через win32api

# Красная матрица
def show_matrix():
    matrix_root = tk.Toplevel()
    matrix_root.attributes('-fullscreen', True)
    matrix_root.configure(bg='black')
    matrix_root.attributes('-topmost', True)
    
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    
    columns = []
    for x in range(0, matrix_root.winfo_screenwidth(), 20):
        text = tk.Text(matrix_root, width=1, height=1, bg='black', fg='red', 
                      font=('Courier', 14), highlightthickness=0)
        text.place(x=x, y=0)
        columns.append({'text': text, 'speed': random.randint(5, 20), 'pos': 0})
    
    def update_matrix():
        for col in columns:
            col['pos'] += col['speed']
            if col['pos'] > matrix_root.winfo_screenheight():
                col['pos'] = 0
            col['text'].place(y=col['pos'])
            col['text'].insert('1.0', random.choice(chars))
            col['text'].after(50, lambda: col['text'].delete('1.0', 'end'))
        matrix_root.after(50, update_matrix)
    
    update_matrix()
    return matrix_root

# Открыть калькуляторы
def open_calculators():
    for _ in range(3):
        subprocess.Popen('calc.exe')
        time.sleep(0.5)

# Главное окно вируса
class RedVirus:
    def init(self):
        self.root = tk.Tk()
        self.root.title("CRITICAL SYSTEM FAILURE")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
        # На весь экран и поверх всех окон
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        
        # Запрет на закрытие
        self.root.protocol("WM_DELETE_WINDOW", disable_close)
        
        # Блокировка Alt+F4
        self.root.bind('<Alt-F4>', lambda e: 'break')
        self.root.bind('<Control-q>', lambda e: 'break')
        self.root.bind('<Control-w>', lambda e: 'break')
        
        # Время
        self.remaining = 600  # 10 минут = 600 секунд
        
        self.setup_ui()
        self.update_timer()
        
    def setup_ui(self):
        # Хакерский шрифт
        mono_font = font.Font(family='Courier New', size=12, weight='bold')
        big_font = font.Font(family='Courier New', size=24, weight='bold')
        
        # Замок (ASCII art)
        lock_art = """
        ╔══════════════════════════════════════╗
        ║              🔐  LOCKED              ║
        ╚══════════════════════════════════════╝
        """
        
        lock_label = tk.Label(self.root, text=lock_art, fg='red', bg='black', 
                             font=mono_font, justify='center')
        lock_label.pack(pady=20)
        
        # CRITICAL SYSTEM FAILUREtitle = tk.Label(self.root, text="CRITICAL SYSTEM FAILURE", 
                        fg='red', bg='black', font=big_font)
        title.pack(pady=10)
        
        # Таймер
        self.timer_label = tk.Label(self.root, text="00:59:59", 
                                   fg='red', bg='black', font=('Courier New', 32, 'bold'))
        self.timer_label.pack(pady=20)
        
        # SYSTEM LOG
        log_frame = tk.Frame(self.root, bg='black', relief='ridge', bd=2)
        log_frame.pack(pady=10, padx=50, fill='both', expand=True)
        
        self.log_text = tk.Text(log_frame, bg='#1a1a1a', fg='#00ff00', 
                               font=mono_font, height=10, width=80)
        self.log_text.pack(padx=5, pady=5, fill='both', expand=True)
        
        # Заполняем лог
        self.update_log()
        
        # Поле для кода
        code_frame = tk.Frame(self.root, bg='black')
        code_frame.pack(pady=20)
        
        tk.Label(code_frame, text="[ENTER DECRYPTION CODE]:", 
                fg='red', bg='black', font=mono_font).pack(side='left', padx=5)
        
        self.code_entry = tk.Entry(code_frame, bg='#1a1a1a', fg='#00ff00', 
                                  font=mono_font, width=20, show='*')
        self.code_entry.pack(side='left', padx=5)
        self.code_entry.bind('<Return>', self.check_code)
        
        # Кнопка (но она не работает, только Enter)
        tk.Button(code_frame, text="[DECRYPT]", bg='#1a1a1a', fg='red', 
                 font=mono_font, command=lambda: self.check_code(None)).pack(side='left', padx=5)
        
        # Статус
        self.status_label = tk.Label(self.root, text="[SYSTEM LOCKED - UNAUTHORIZED ACCESS DETECTED]", 
                                    fg='red', bg='black', font=mono_font)
        self.status_label.pack(pady=10)
        
        # Инструкция
        tk.Label(self.root, text="[ENTER CODE 6767 TO DECRYPT]", 
                fg='#00ff00', bg='black', font=mono_font).pack()
        
    def update_log(self):
        logs = [
            "[INFO] CPU Utilization SystemId = 0x00000000 (MAD) Status = 0x00000000 (CPU)",
            "[ERROR] INVALIDATING PTS DESCRIPTOR SEQUENCE ...",
            "[WARN] Memory corruption detected at 0x7FFF0000",
            "[CRITICAL] System integrity compromised",
            "[INFO] Encryption layer active - AES256",
            "[ERROR] Failed to access secure kernel",
            "[INFO] User input required for decryption"
        ]
        
        for i in range(10):
            self.log_text.insert('end', random.choice(logs) + '\n')
        
        # Прокручиваем лог
        self.log_text.see('end')
        
    def update_timer(self):
        if self.remaining > 0:
            minutes = self.remaining // 60
            seconds = self.remaining % 60
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}:59")
            self.remaining -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="00:00:00")
            self.status_label.config(text="[SYSTEM TERMINATED - DATA LOST]")
    
    def check_code(self, event):
        code = self.code_entry.get()
        if code == "6767":
            self.status_label.config(text="[DECRYPTION SUCCESSFUL - SYSTEM RESTORED]", fg='#00ff00')
            self.root.after(2000, self.unlock_system)
        else:
            self.status_label.config(text="[INVALID CODE - ACCESS DENIED]", fg='red')
            self.code_entry.delete(0, 'end')
    
    def unlock_system(self):
        # Убиваем все процессы вируса
        self.root.quit()
        os._exit(0)
    
    def run(self):
        self.root.mainloop()

# Защита от закрытия через диспетчер задач (простейшая)
def protect():
    while True:
        time.sleep(5)
        # Проверяем, запущены ли процессы калькулятора, если нет - запускаем снова
        # Это примитивная защита
        passif name == "main":
    # Показываем матрицу
    matrix = show_matrix()
    
    # Открываем калькуляторы в отдельном потоке
    calc_thread = threading.Thread(target=open_calculators)
    calc_thread.daemon = True
    calc_thread.start()
    
    # Запускаем главное окно через 2 секунды
    time.sleep(2)
    matrix.destroy()  # Убираем матрицу
    
    virus = RedVirus()
    
    # Запускаем защиту в фоне
    protect_thread = threading.Thread(target=protect)
    protect_thread.daemon = True
    protect_thread.start()
    
    virus.run()
