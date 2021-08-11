import os

def copypasta(cp_name):
    """
    Returns a copypasta from a list of copypastas when user inputs a copypasta name. 
    Returns "Copypasta does not exist" when copypasta name is not in list.

    Inputs:
        cp_name (str) - string containing the name of the copypasta
    
    Output:
        cp (str) - returns the copypasta itself
    
    """

    try:
        cp = open(os.path.join(os.path.dirname(__file__), 'copypastas/{}.txt'.format(cp_name.strip())), 'r')

        return cp.read()
    except IOError:
        return "Copypasta does not exist"
