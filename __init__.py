import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import textwrap
import numpy as np
from items import items

def make_card(filename):
    # generates a 5x5 bingo card and saves it under filename.
    
    fig = plt.figure(figsize=(8,8))
    fig.subplots_adjust(wspace=0.0,hspace=0.0) # subplots are flush

    ind = np.random.choice(len(items), size=24, replace=False)
    loc = 0  # location of subplot
    for text in items[ind]:
        loc += 1
        ax = fig.add_subplot(5, 5, loc)
        ax.tick_params(axis='both', which='both', bottom='off', top='off', \
            left='off', right='off', labelbottom='off', labelleft='off')  # no ticks
        if (loc==13):  # free space
            img=mpimg.imread('ufo.png')
            ax.imshow(img)
            ax.set_xlim(-20, 148)
            ax.set_ylim(148, -20)
            loc += 1
            ax = fig.add_subplot(5, 5, loc) 
            ax.tick_params(axis='both', which='both', bottom='off', top='off', \
                left='off', right='off', labelbottom='off', labelleft='off')  # no ticks   
        ax.text(0.5, 0.5, textwrap.fill(text, width=15), horizontalalignment='center', \
                verticalalignment='center', transform=ax.transAxes, fontsize=12)

    fig.savefig(filename)
    fig.clf()

def make_cards(n, base_name='bingo'):
    # generates n cards.
    for i in range(n):
        filename = base_name+str(i+1)+'.pdf'
        make_card(filename=filename)
        
    print "{0} bingo cards generated.".format(n)