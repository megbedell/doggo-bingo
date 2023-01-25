This code generates randomized 5x5 bingo cards for use at the [AKC Meet the Breeds event](https://www.akc.org/sports/akc-meet-the-breeds/) (2023, NYC).

#### Rules of Doggo Bingo:

1. Mark off each dog breed that you pet.
2. The first player to mark off an entire row (horizontal, vertical, or diagonal) is the official winner of Doggo Bingo.
3. Any players who mark off their entire sheet get a special bonus of pride and glory.
4. Just kidding! Everyone is a winner because you got to pet some dogs!!


#### Generating cards:

Quickly generate a card with:

	git clone https://github.com/megbedell/doggo-bingo.git
	cd doggo-bingo
	python generate_cards.py
	
A randomized card will appear under the name `bingo.png`.

If you want to generate a card and save it under a custom filename/format, the python syntax is:

	from generate_cards import make_card
	make_card('bingo.png')
	
If you want to quickly generate a batch of cards, do:

	from generate_cards import make_cards
	make_cards(5, base_name='bingo')
	
The above code will save five cards as `bingo1.png`, `bingo2.png`, etc.

---

<div><a href="https://www.flaticon.com/free-icons/dog" title="dog icons">Dog icon created by deemakdaksina - Flaticon</a></div>