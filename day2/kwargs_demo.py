"""
kwargs_demo.py

Kwargs stands for keyword arguments. They can be used to collect different
values into a dictionary. This can be very useful for passing keyword arguments
along to another function.
"""
import matplotlib.pyplot as plt

# We generate some simple dummy data
x = list(range(1, 11))
y = [xi ** 2 for xi in x]
y2 = [xi ** 0.5 for xi in x]


def line_plot(x: list, y: list, **plotargs) -> None:
    """
    This function is a slight variation on the standard plot() function.
    It always uses the same title and requires an x and a y. It can also receive
    keyword arguments, but those are handled by the plotting library.
    :param x:           List of values for x-axis
    :param y:           List of values for y-axis
    :param plotargs:    Any keyword supported by matplotlib.pyplot.plot()
    :return:            -
    """
    # We generate the plot using x and y, but we also pass along any styling
    # keywords we may have received.
    plt.plot(x, y, **plotargs)

    # We can add some logic of our own, like automatically generated titles, storing the
    # plots in the proper location, etc. etc. This is the added functionality of our function.
    plt.title("Kijk een plot met kwargs!")
    plt.show()


# Call the function with our dummy data and some styling information to pass along
line_plot(x, y, color="blue")
line_plot(x, y2, linewidth=3, color="green")
