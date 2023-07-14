import matplotlib.pyplot as plt
import networkx as nx


def create_bar_chart(data, title="", xlabel="", ylabel=""):
    """
    Function to create a bar chart
    """
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def create_pie_chart(data, labels, title=""):
    """
    Function to create a pie chart
    """
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()


def create_histogram(data, title="", xlabel="", ylabel=""):
    """
    Function to create a histogram
    """
    plt.hist(data, bins=20)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def create_network_diagram(G):
    """
    Function to create a network diagram
    """
    nx.draw(G, with_labels=True)
    plt.show()