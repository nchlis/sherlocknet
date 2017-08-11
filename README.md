## Sherlocknet

[link to related blog post.](https://nchlis.github.io/2017_07_22/page.html)

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


```


===== diversity: 0.1 =====
on the very day that i had come to the station and the colonel and the colonel and the station which had been so far 

as to the station and the colonel and the strange expression of the station and the station which had been seen the 

same as the other was a strong problem which had been a man of the man who had been a very serious conclusion, and i 

was able to see you to the station. i think that i have no doubt that i have not been taken as a strange story of the 

station and the colonel and the station of the station and the station which had been seen the state of the station 

and the colonel and the station which had been so far as to the man of the matter. i was able to see that the man was 

a very small part of the station. i was able to see that the man was a very strange conclusion that i have not been 

taken to the

===== diversity: 0.3 =====
on the very day that i had come to his little time, and i was able to prove that the man was a strong problem which 

would be able

to see him in the morning.”


“what a man was a common conversation which had been taken to his face. “i will not tell you that this should be a 

man of the matter upon the moor?”


“no, i said that the blow was a state of great careless and of my mind and the

whole house was a strange conclusion which was a little man who had been so drawn in the middle of the moor. the lady 

was a pretty strong problem of the facts. i think that i am afraid that i should be very happy to see the station and 

the single character of the house and a look of the house was struck by the station and admiration was still and as 

he could not have been a promise of the matter which i shall be able to see you to the con

===== diversity: 0.5 =====
on the very day that i had come. i should be very glad to have the station of the stream of being

a very strange curious business.  the facts are seriously a man to get up and down. i was at the admirable corner of 

the man who had been done by the police and leave to the strength of the terrible steps and the convict showed me 

that the news are at the man, and that i can see that the

furniture was too much to see him in the law. you said that i could not have to strange and likely that the other 

reason was on the same conclusion. at the same time, i should not give me a singular advantage of the world that they 

had

shown the advantage of his own country. he was an accident and committed to the convict, as it seemed to me that he 

had been made a large

party to see that he was able to see that it was a man of a man of my

===== diversity: 0.7 =====
on the very day that i had come to

any very far to give him in the

same ways of his problem for a strange visitor when the third geemen was still an oath and earnest word. the house 

may have made a carpet. i will

rehurd to the hound to serve these things as to the better?”


“no, no, it is so earnest about the fastent which is too much

able to explain the planking importance to the advertisement which he

had drawn down the door, and the

two continents and murmur showed that the case was so very successful that i should be a man who will certainly do 

it. the carriage would end in the station, and i was standing in his chair and confessed that the great person who

did not find the light upon the middle. it is never bad.”


“none of them are all dreadful.  a month, and that if they were reported to your judgment. the clue w

===== diversity: 1 =====
on the very day that i had come drooping pouch of six air,

it is slightened by an end."



"if dr. mortimer has seen, and

pale cab, since you shauld see a glimpse of that day?"



"no; but there was him and was still weary. it

carefully come from the point.”



“so for it! i think, dr. mortimers i shall need and

make the glimpses."



"what is consequent name? well, you are well sitting in

the meantime. i can easily do so,

for she does not give us on, mr. jonas oney,

and came to a coronet and a square

of hound, for the invalid lib,

leaved ourselves, and the once since everything according to the next bottle and edge took ryaffership about the 

brussion

of his village.  i have night at once did he interrupt you, sir. but, i fancy that what my wretched death shall

not propose, watson?"



"i tell you that you may have made your hei

===== diversity: 2 =====
on the very day that i had comjupinited.  we picked, shaved-peosezt or kenne,

came backpoof, uppersiglizan effrois, just

fapa awgy. yunding

from the lent ermak to-maw?’ tais violet

object about whomeeting it should underivel?"



"is bliosi-raising syfic froe who rrouddn;

est, lorsh-glag from

moilayiam, unty daughter; she kept yax 127 pions upon druw?”



my frodk?"



svitetmus dcmuchest into eye if “you

know anyefus o'clock?” holmes sor,, laughing

wibdled, layfift.' eothur

piere xon toulla.’



“‘ohlahily?"



"i enterectay'--that," he apploved, né know,

perhaps do; why's four’peds, didnegiant!

firun, tobding



442 evidence’s

idmanu, mr., usband."-

in fvalkyil-st; n’k befile the villeter    'us my horsor for a

policymatch_’, glmantit [29 h’:h’t.”



“and i?'w

"it’s bought to jee-undup luffed, ‘you

bring holpeu gum.


    let. he'’

```

## Licence
MIT
