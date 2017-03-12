"""
Bar chart showing total of learning style scores
"""

def barchart():
        import numpy as np
        import matplotlib.pyplot as plt


        n_groups = 8

        results = [14, 25, 15, 0, 15, 5, 20, 30]

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.5

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = plt.bar(index, results, bar_width,
                         alpha=opacity,
                         color='b',
                         error_kw=error_config,
                         label='Results')

        plt.xlabel('')
        plt.ylabel('Scores')
        plt.title('Learning Styles')
        plt.xticks(index + bar_width/2, ('Visual', 'Audio', 'Reading', 'Kinesthetic', 'Activist', 'Theorist', 'Pragmatist', 'Reflector'))

        plt.tight_layout()
        plt.show()
