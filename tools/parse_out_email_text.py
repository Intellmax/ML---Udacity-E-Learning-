#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        #text_string = content[1].translate(str.maketrans("", ""), string.punctuation)
        translator = str.maketrans('', '', string.punctuation)
        text_string = content[1].translate(translator).strip()
        ### project part 2: comment out the line below
        # words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        # print (text_string)

        string_array = text_string.split()
        stem_words = []
        stemmer = SnowballStemmer("english", ignore_stopwords=False)
        for i in string_array:
            stem_words.append(stemmer.stem(i))
        words = " ".join(str(x) for x in stem_words)

    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print (text)



if __name__ == '__main__':
    main()
