03 Movie Quiz
- asking if the user want to play
- if yes: 5 questions with A, B, C, answer/input options
- after everey answer the result(Correct, Incorrect) is displayed

04 Movie Title Randomizer
- from my Excel we are pulling the "title", "year of release" and "how many times I have seen the movie" values
- the infos are in merged cells -> if the first randomly selected cell is empty, it is going to check the next cell until it finds a record*
- *=after line 6736 there is still a title at the moment -> avoiding the search for valid cell on the empty/inactive part of the excel
- Giving back "You have seen this movie (only once / x times)" depends on the "how many times I have seen the movie" cell value

05 Amount Guessing Game - input validation
- asking if the user want to play
- In 3 rounds it will display random amount* of characters and you have to guess the quantity
- * = from a range which is increasing after every round (1nd, 2nd)
- Validating the answers: it has to be a positive integer
- After 3 rounds guessing displaying the user`s points / %

06 Drawing a Xmass Tree with while loop

07 Drawing a cartoon figure with Turtle

08 Automating the display sharing/extend update
   01 
   - From my main display(monitor), after pressing the `WIN + p` keys, 
   - it will select the `Extend` options to use the monitor`s and the laptop`s display too
   02
   - After pressing the `WIN + p` keys, from the `Extend` option (Extend = using the monitor`s and the laptop`s display the same time)
   - it will jump to the `Second screen only` which is my main display/monitor
   03
   - It will randomly select a number from the range -> that many times makes the display sharing (1 or 2 display, if only 1: monitor or paptop, ..)
   - selector jump and eventually selecting the option in the latest loop