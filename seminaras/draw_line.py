import matplotlib.pyplot as plt


def draw_line(x_values, y_values):
    """Draw a simple line plot from two lists of values."""
    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Simple line plot")
    plt.grid(True)
    plt.show()


fig.savefig("line_plot.png")  # Save the figure as a PNG file

if __name__ == "__main__":
    draw_line([1, 2, 3, 4], [1, 4, 9, 16])
