""""""
"""
Pie charts are helpful for displaying data like:

Different ethnicities that make up a school district
Different macronutrients (carbohydrates, fat, protein) that make up a meal
Different responses to an online poll

"""

from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.axis('equal')
plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.legend()
plt.show()

