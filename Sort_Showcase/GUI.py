import tkinter as tk
from Graph import generate_and_plot
import time

def run_gui():
    root = tk.Tk()
    root.title("Sort Showcase")
    root.configure(bg="grey")

    amtVar = tk.StringVar()
    sort_var = tk.StringVar(value="Bubble Sort")
    sort_time_label = tk.Label(root, text="Sort Time: N/A", bg="grey", fg="white")
    sort_time_label.grid(row=7, columnspan=2, padx=10, pady=5)

    graph_data = {
        "amount": 0,
        "unsorted_numbers": [],
        "sort_type": ""
    }

    def generate_graph():
        amount = amtVar.get()
        sort_type = sort_var.get()
        try:
            print("Generating unsorted graph...")
            graph_data["amount"] = int(amount)
            graph_data["sort_type"] = sort_type
            graph_data["unsorted_numbers"] = generate_and_plot(amount, sort_type, show_only=True)
        except ValueError as e:
            print(f"Error: {e}")

    def sort_graph():
        if not graph_data["unsorted_numbers"]:
            print("Please generate the graph first!")
            return
        print("Sorting the graph...")
        start_time = time.time()
        generate_and_plot(graph_data["amount"], graph_data["sort_type"], graph_data["unsorted_numbers"])
        end_time = time.time()
        elapsed_time = end_time - start_time
        sort_time_label.config(text=f"Sort Time: {elapsed_time:.2f} seconds")

    tk.Label(root, text="Enter Amount of items to generate (integer):", bg="grey", fg="white").grid(row=0, column=0, padx=10, pady=5)
    item_entry = tk.Entry(root, textvariable=amtVar)
    item_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Select Sort Type:", bg="grey", fg="white").grid(row=2, column=0, padx=10, pady=5)
    sort_options = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
    sort_menu = tk.OptionMenu(root, sort_var, *sort_options)
    sort_menu.grid(row=2, column=1, padx=10, pady=5)

    generate_button = tk.Button(root, text="Generate Graph", command=generate_graph)
    generate_button.grid(row=3, columnspan=2, padx=10, pady=5)

    sort_button = tk.Button(root, text="Sort Graph", command=sort_graph)
    sort_button.grid(row=6, columnspan=2, padx=10, pady=5)

    sort_time_label = tk.Label(root, text="Sort Time: N/A", bg="grey", fg="white")
    sort_time_label.grid(row=7, columnspan=2, padx=10, pady=5)

    root.mainloop()
