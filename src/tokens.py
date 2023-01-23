#===============#
# IMPORTS       #
#===============#
import re
import time


#===============#
# MAIN          #
#===============#
start_time = time.time()
#: a rather amatuerish approach to tokenizing literally anything
def tokenize(_str): # -> to be remade using dictionaries, better efficiency. CURRENT RUNNING TIME: ~500000ns OR ~0.0005s
    """
    This is a rather amateurish approach to tokenizing something. In this case
    it focuses on styling indicators in `uprint` statements. It is rather shit
    and probably shouldn't be used in an actual project, but since I'm actually
    quite fucking stupid, I had to do it like this, because my brain can't handle
    anything even a little more complex. I'm just one big cognitive deficiency, forgive me.

    Anyway, here is how a token is structured:\n
    `token: [['<tok-attr>', '<tok-attr>', '<tok-attr>', '<TOK-NAME>'], ...]`\n\n
    `<tok-attr>`: The text element that should be changed (anything within the indicators)\n
    `<TOK-NAME>`: The token name indicates whether the text element should be colored, boldend, underlined,...
    """
    #: create an empty list to store the "tokens" in
    tokens = []

    #: find all occurrences of text elements that should be modified
    COL = re.findall(r'\[(.*?)\]', _str)
    BOL = re.findall(r'\*\*(.*?)\*\*', _str)
    UND = re.findall(r'__(.*?)__', _str)
    CUT = re.findall(r'~~(.*?)~~', _str)
    ITA = re.findall(r'\*(.*?)\*', _str)

    #: append token name
    COL.append('COL')
    BOL.append('BOL')
    UND.append('UND')
    CUT.append('CUT')
    ITA.append('ITA')

    #: append everything to the 'tokens' list previously created
    tokens.append(COL)
    tokens.append(BOL)
    tokens.append(UND)
    tokens.append(CUT)
    tokens.append(ITA)

    #: iterate through "tokens" to remove any empty items
    for i in tokens:
        while '' in i:
            i.remove('')

        #: remove empty "tokens"
        if len(i) <= 1:
            tokens.remove(i)

    #: return error-free 'tokens' list
    return tokens

txt = "[red]Hello, **this** is [reset]a so called [green]*test*[reset]! __YOU__ ~~can not~~ can [yellow]style[reset] [purple:bg]outputs like this too!"

print(tokenize(txt))

print("----------- %s seconds -----------" % (time.time() - start_time))