import re

def pekofy(words):
    """
    Pekofies sentences, including ones that are already pekofied. Pekofication occurs on any [.!?]. On empty input, outputs PE↗KO↘ PE↗KO↘ PE↗KO↘.

    Inputs:
        words (str) - string containing the message to be pekofied.

    Output:
        (str) - pekofied string.

    """
    
    punc = ['.','!','?','']
    orig_sentences = str(words)
    if orig_sentences != "":
        temp_list = re.split("([.?!])", orig_sentences)
        pekofied_list = [i+' peko' if i not in punc else i for i in temp_list]
        peko = ''.join(pekofied_list)
        return peko
    else:
        return "PE↗KO↘ PE↗KO↘ PE↗KO↘"


