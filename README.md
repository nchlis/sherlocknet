## Sherlocknet

A character to character LSTM model for text generation.
The network was trained on the sherlock holmes books by Sir Arthur Conan Doyle.

## Dataset

The following books were used:
- a study in scarlet
- the sign of the four
- the hound of the baskervilles
- the valley of fear
- the adventure of sherlock holmes
- the memoirs of sherlock holmes
- the return of sherlock holmes
- his last bow

all available on Project Gutenberg https://www.gutenberg.org/
the header and footer of each book was removed prior to training and
all books were concatenated in a single .txt file.

## Code & More information
Sherlocknet was based on the keras example code at:
https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py

More information on character to character networks can be found at:
- A. Karpathy's blog: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
- A. Graves, "Generating Sequences With Recurrent Neural Networks": https://arxiv.org/abs/1308.0850

## Example generated text 
800 characters generated with different values of diversity.
Low diversity values yield technically correct but repetitive and boring results.
Higher values of diversity are more "adventurous".

----- diversity: 0.1
----- Generating with seed: "diverting the stream; so i tho"
diverting the stream; so i thought that i have a man of the man who was a man of a man who was a strange and the man who had been the man who was a man of a man who was a man of a single fellow which had been the man who had been the man who was a man of a strange state of some miles of the man who was a man of the statest man who had been so started to the man who had been the man who was a man of the man who had been the man who was a strange state of some sound of the same stranger and the man who had been the man who was a man of a man who was a man of some minutes and the man who had been the man who was a man of some minutes and the man who had been the man who was a man of a single fact that the man who had been a strange and the man who had been the man who was a man of some minutes to the man who had been the 
----- diversity: 0.5
----- Generating with seed: "diverting the stream; so i tho"
diverting the stream; so i thought that he was not to be
taken a man of his own study which i had seen the only means of his strange water and the aid of us, and see if they were able
to do in the world who he has been in the side of the wall in the trail of it. the loss were a strong person to be the honour of the great end of the collection of the interest than the night and the police must admit that the moor was made to do as a series. and the doctor, i should be satisfied that i was a small street and was a few minutes. he would have happened in the disappearance of a long sort of crime, and the violent wind had been the promise of the man who was a single convict and his line which they were able to make a small pencil business. it was a long deal manner which may be seen and came at the table to the tragedy of i
----- diversity: 0.7
----- Generating with seed: "diverting the stream; so i tho"
diverting the stream; so i thought to say that he was unlikely we were annoyed to make us the alternative, and then i regular to
ever stick as i sat slowly out, and the murder, and the same that he
greeted his face without him, and took to extreme the moor and
freed of importance, and yet it was evident, and the house was of eight end that it was lest the orders of his fire when he made him in order to make
for the moor.

“i think that it is a hang at baker street. it was for all that was that i should have
caused by the first and man was over the farther end out of the ordiniance
upon the man, with the night, and to give me not here to make any reason, but not to be found ourselves than any indian. it was dead, and that i was a
pland one of the really the commissions of the room. if you will see how you have none
obse

## Licence
MIT
