# pylint: disable=C0301 #Line too long (%s/%s)
# pylint: disable=C0303 #Trailing whitespace
# pylint: disable=C0304 #Final newline missing
# pylint: disable=C0305 #Trailing newlines (trailing-newlines)
# pylint: disable=W1203 # Use lazy % formatting in logging functions (logging-fstring-interpolation)

"""
@ ati a.t. ince
@ 19.01.2023
----------------
Not: we going to test the code with fuzzywuzzy and spacy together. 
Going to use fuzzywuzzy for fuzzy matching and spacy for NLP and text similarity.
Need to test Ratio and Computation time for creating a model for each module in therm of accuracy and speed.
"""

## Variables, strings
string = '''i didn't find any playlists in your music library.'''#'which artist would you like to browse?'
stt_ret = '''i didn't find that playlist.'''#'which artist would you like to browse'


# 1. Fuzzy matching
from fuzzywuzzy import fuzz
MatchRatio = fuzz.ratio(string, stt_ret)
print(MatchRatio)


## 2. using Spacy for NLP and text similarity
import spacy
nlp = spacy.load("en_core_web_lg")
doc = nlp(string)


print(doc.similarity(nlp(stt_ret)))
