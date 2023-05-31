import tkinter as tk
from tkinter import filedialog
import subprocess


class CellSegmentationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cell Segmentation Analysis")

        # Configure initial window size
        self.root.geometry("900x500")

        # self.menu = Menu(root)
        # item = Menu(menu)
        # item.add_command(label='New')
        # menu.add_cascade(label='File', menu=item)
        # root.config(menu=menu)

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create left frame
        self.left_frame = tk.Frame(self.main_frame, width=300)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        # Create right frame
        self.right_frame = tk.Frame(self.main_frame, width=600)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.right_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create text widget
        self.text_widget = tk.Text(self.right_frame, yscrollcommand=self.scrollbar.set)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.text_widget.yview)

        # Create file path selection button
        self.file_button = tk.Button(self.left_frame, text="Select File Location", command=self.select_file)
        self.file_button.pack(pady=10)

        # Create checkbox for histogram
        self.histogram_var = tk.IntVar()
        self.histogram_checkbox = tk.Checkbutton(self.left_frame, text="ACF Functions", variable=self.histogram_var)
        self.histogram_checkbox.pack()

        # Create checkbox for cell surface types
        self.surface_label = tk.Label(self.left_frame, text="Choose cell surface type:")
        self.surface_label.pack(pady=10)

        self.stiff_gel_var = tk.IntVar()
        self.stiff_gel_checkbox = tk.Checkbutton(self.left_frame, text="Stiff Gel", variable=self.stiff_gel_var)
        self.stiff_gel_checkbox.pack()

        self.soft_gel_var = tk.IntVar()
        self.soft_gel_checkbox = tk.Checkbutton(self.left_frame, text="Soft Gel", variable=self.soft_gel_var)
        self.soft_gel_checkbox.pack()

        # create minimum track length label
        self.track_length_label = tk.Label(self.left_frame, text="Enter minimum track length:")
        self.track_length_label.pack(pady=5)

        self.enter_min_length = tk.Entry(self.left_frame)
        self.enter_min_length.pack(pady=5)

        # Create button to run the python script through gui
        self.run_button = tk.Button(self.left_frame, text="Generate Functions", command=self.run_sc)
        self.run_button.pack(pady=20)

        # Create menus
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.about_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="Use", command=self.show_use)
        self.about_menu.add_command(label="Author", command=self.show_author)

    def select_file(self):
        filepath = filedialog.askopenfilename()
        self.text_widget.insert(tk.END, f"Selected file: {filepath}\n")

    def open_file(self):
        self.text_widget.insert(tk.END, "Open file option selected\n")

    def save_file(self):
        self.text_widget.insert(tk.END, "Save file option selected\n")

    def show_use(self):
        self.text_widget.insert(tk.END, "This GUI is created for use in Dr. Tim Elston's Lab at UNC.\n "
                                    "It's purpose is easier access to creation of autocorrelation figures.\n")

    def show_author(self):
        self.text_widget.insert(tk.END, "Author: Noah Shaul\n")

    def run_sc(self):
        min_length = self.enter_min_length.get()
        script = "script_prac.py"
        command = ["python", script, "--min_length", min_length]
        subprocess.call(command)
        self.text_widget.insert(tk.END, f"Script {script} successfully executed\n")
        # self.right_frame(text="Script executed")


# Create the main window
root = tk.Tk()
gui = CellSegmentationGUI(root)
root.mainloop()
