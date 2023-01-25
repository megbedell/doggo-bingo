import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import textwrap
import numpy as np
import os

import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_items(use_cache=True):
    # get the list of dog names
    # set use_cache to False to re-fetch and overwrite cached
    if use_cache & os.path.exists('breeds.txt'):
        items = np.loadtxt('breeds.txt', dtype='str', delimiter=',')
    url = 'https://www.akc.org/sports/akc-meet-the-breeds/dog-breeds-attending/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    html_table = soup.find('table')
    
    items = []
    for i in html_table.find_all('tr'):
        row_data = i.find_all('td')
        for j in row_data:
            items.append(j.text)
    np.savetxt('breeds.txt', items, fmt='%s')
    return items
    

def make_card(filename):
    # generates a 5x5 bingo card and saves it under filename.
    
    items = np.array(fetch_items())
    
    fig = plt.figure(figsize=(12,12))
    fig.subplots_adjust(wspace=0.0,hspace=0.0) # subplots are flush

    ind = np.random.choice(len(items), size=24, replace=False)
    loc = 0  # location of subplot
    for text in items[ind]:
        loc += 1
        ax = fig.add_subplot(5, 5, loc)
        if (loc==13):  # free space
            img=mpimg.imread('dog.png')
            ax.imshow(img)
            margin = 200 # pts
            ax.set_xlim(-margin, 512+margin)
            ax.set_ylim(512+margin, -margin)
            ax.set_xticks([])
            ax.set_yticks([])
            loc += 1
            ax = fig.add_subplot(5, 5, loc) 
        ax.text(0.5, 0.5, textwrap.fill(text, width=12), horizontalalignment='center', \
                verticalalignment='center', transform=ax.transAxes, fontsize=16)
        ax.set_xticks([])
        ax.set_yticks([])
        
                

    fig.savefig(filename)
    fig.clf()

def make_cards(n, base_name='bingo'):
    # generates n cards.
    for i in range(n):
        filename = base_name+str(i+1)+'.png'
        make_card(filename=filename)
        
    print("{0} bingo cards generated.".format(n))
    
if __name__ == '__main__':
    make_cards(1)
    '''
    make_card(filename='megan.png')
    make_card(filename='lily.png)
    make_card(filename='tim.png)
    make_card(filename='lehman.png)
    make_cards(3, base_name='jd')
    '''