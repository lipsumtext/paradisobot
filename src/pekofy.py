import re

def pekofy(words):
    """
    What pekofy does is pekofy sentences that aren't pekofied

    Peko!

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


