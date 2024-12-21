import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sort import bubble_sort, selection_sort, insertion_sort

SORT_ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

def generate_and_plot(amount, sort_type, numbers=None, show_only=False):
    """
    Generate random numbers (or use existing numbers), and optionally sort them.
    :param amount: The number of random numbers to generate (integer).
    :param sort_type: The sorting algorithm to use.
    :param numbers: (Optional) Existing list of numbers to use.
    :param show_only: If True, only display the unsorted graph.
    :return: The unsorted list of numbers if show_only is True.
    """
    try:
        if numbers is None:
            amount = int(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            numbers = [random.randint(1, 100) for _ in range(amount)]

        if show_only:
            # Display only the unsorted graph
            plt.figure(figsize=(10, 6))
            plt.bar(range(len(numbers)), numbers, color='blue')
            plt.title("Unsorted Graph")
            plt.xlabel("Items")
            plt.ylabel("Value")
            plt.show()
            return numbers

        if sort_type not in SORT_ALGORITHMS:
            raise ValueError(f"Invalid sort type: {sort_type}")

        # Sort and animate the process
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(range(len(numbers)), numbers, color='blue')

        ax.set_title(f"{sort_type} Visualization")
        ax.set_xlabel("Items")
        ax.set_ylabel("Value")

        sort_function = SORT_ALGORITHMS[sort_type]
        steps = sort_function(numbers)

        def update(frame):
            for rect, height in zip(bars, frame):
                rect.set_height(height)
            return bars

        anim = FuncAnimation(fig, update, frames=steps, blit=True, interval=200, repeat=False)
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")
