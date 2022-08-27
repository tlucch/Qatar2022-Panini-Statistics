# Qatar2022-Panini-Statistics
A set of simulation that show how much stickers are needed to complete the Qatar 2022 Panini Album

## No Trading

The "No trading" code generates 1000 simluations in which each person can't trade stickers with other people. The code iterates imitating a person that buys stickers until the ablum is full and counts how many stickers were needed to buy in other to complete the album. After that an histogram is made, in order to see the distribution, and the mean and standard deviations are printed.

### First Results

The fisrt time the simluation was runned, the following chart was generated:


<p align = "center">
  <img src = "Plot%20First%20Run%20No%20Trading.PNG" width = 500>
</p>


This chart shows a normal distribution having its Mean at more or less 4500 stickers. We can confirm this after seeing the Descriptive Statistics results:

* `Mean` : 4474
* `Standard Deviation`: 815

This means that 68.2% of the simluations made needed to buy between 3659 and 5289 stickers in order to finish the album.

## Trading

The "Trading" code is still in development. In this simulation trading is allowed between participants. The objective is to know how many stickers are needed to buy to complete the album when you can trade stickers with other people.
