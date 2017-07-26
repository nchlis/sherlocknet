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
Higher values of diversity are more "adventurous", for example when diversity = 2,
the text makes little sense (if any).


===== diversity: 0.1 =====
' says have been the same as the country with the convict and the strange tracks of the country which had been concerned in the house and the convict of the country which had been concerned in the case of the strange tracks of the country which had been sent to the country with the country which had been standing in the street and the strange tracks of the country which had been seen in the country with the conclusion that the tragedy were so dead to the country with the strange tracks of the country which had been standing in the cab and the strange tracks of the country which had been standing in the cab, and the strange tracks were still in the country with the country which had been seen and the man who had seen the strange tracks of the strange tracks of the country which had been sta

===== diversity: 0.3 =====
' says have been the same as the criminal?”

“i will come to the country of the country and the murderer which had been able to conceal the matter to the paper which he had seen the same as the country with the same as the concealment of the countryside, and then she must have been able to see the strange tracks of the law. the steps were able to see the story of the man who had seen the criminal who had stood upon the stairs and the strongest chance of any other signs of the country which had been sent to the stranger in the strange train of strange faces. the stories of the man was about to look at the stairs. the man was a strange story which had been drawn up to the room. “i am sure that you will excuse me to see the matter in the morning. then i had seen the stone light of the street 

===== diversity: 0.5 =====
' says she, what is this could have formed a few days in the dead man’s face, and
i saw the deep door of the street and in the character of the story. then you have a confidence to prove all the way of the heart of the country of the strangers and a man who had reached the room which i might have formed
the fact that the reason that he had been permissivly from death, and i was still told to force the lawn and made him the work and the detectives in the matter of his secret and reaching the door and the household had struck a grief to get the day yet?”

“no.”

“well, mr. holmes, that i shall be with you to ask you to get better to take the course of the criminal diffidences which are waiting as in the box. he was a boyly cold window in the hall, which showed that the police could not have 

===== diversity: 0.7 =====
', the correct seat and have been drawn before i had got the rest as far as i could not see me. it is a dreadful death to tell him
that this is the same as is the same as if i used to know that it was not in the house and looked his head from his right and
agitating there is no one in your life, mr.
jones, the second brother restor lived at all the same man with a line. the candle had been worked over the rucastles.  i was
at once recognised to step into his pocket.

“i could not get away. how long were they done?”

“well, that is all on the sides of this distant point.  the man of your investigation. the other
hand that the hall was afraid to pursued his carriage before
he was able to get here a wideseleman of
the name of the very deduction of the matter of during this
could be wanting in

===== diversity: 1 =====
 _glare or
way, to think the key without death for the life. where, after all, how does it might have been the tanket before.

"it means that anything in the surgeon upon the morning, after
one of these, round tuesday evening.”

holmes stapleton repulsed me the shawl, he runs in the middle-plants, but his finger and a house, and to escape the
swing for a
subject. they are that of one at home.” so amazed if she had been avoided in the
centre of her husband; 'pot it because
her hamas went out of flash than work, for the man managed to already the nice and self-road at
grain arthur in town, and a long creature may serve to have been to
wink himself to enter the physician that he did well have him enough to get an inhabitant to the paddock that i looked at the police or breakfast to our argume

===== diversity: 2 =====
’n nor canntpleaty
her.?”

“publishakhi."
this carefulty blid until he had
transfixed outffollinations excet
heavels? i know
you fever than--you abusts it!
everylhing splendids his. dopcorah braky
howike!" said ribs fly. by haxuare signifieach focks,

vi
hugh- from a situation and shatetis
trotts! agent n.?"

suftfring their, pelieved his eye,'riseme. bot, crime epolized already.”

from the wit’ aself came, and a retriat: 1s old weakness by charing
ce,mses. pad?'druel call i
helped, and swurveltated?d, meet untidy antic nexture f.wz, "midn.”

wonkerf fove,”

no. "i shall!’ this smooner nad mf.
i.
ohe ones themsutted know to a dog-cob straugh,” whisped sainious, yawne.

admitrate--he; during there i auguiled
watson iir norehdor."

mcginty became dear in less,
bitce,” said receiping by blued

## Licence
MIT
