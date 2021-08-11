import re

def pekofy(words):
    """
    Pekofies sentences, including ones that are already pekofied. Pekofication occurs on any [.!?]. On empty input, outputs PE↗KO↘ PE↗KO↘ PE↗KO↘.

    Inputs:
        words (str) - string containing the message to be pekofied.

    Output:
        (str) - pekofied string.

    """
    
    punc = ['.','!','?','',' ']
    orig_sentences = str(words)
    if orig_sentences != "":
        temp_list = re.split("([.?!])", orig_sentences)
        pekofied_list = []
        for i in temp_list:
            if i in punc:
                pekofied_list.append(i)
            else:
                a=-1
                while i[a]==' ':
                    a=a-1
                a=-(a+1)
                pekofied_list.append(i.rstrip(" ")+" peko"+" "*a)
        peko = ''.join(pekofied_list)
        return peko
    else:
        return "PE↗KO↘ PE↗KO↘ PE↗KO↘"



