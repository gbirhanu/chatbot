from builtins import print

rule2=['oolee','oolii','olii','toota','ota','olee','tootaa','oota','icha','ichi','oomaa','fis','siis','omaa',
       'ooma','ooma','siif','fam','ata']
rule1=['ittii','dha','ttii','tii','irra','rra','ti']
rule3=['eenya','ina','offaa','annoo','umsa','ummaa','insa','am','ni','affaa']
rule4=['aa','uu','ee','e','u','o','s','suu','sa','se','sii','si','Ssi','sse','ssa','nye','nya']
rule51=['du','di','dan']
rule52=['lee']
rule53=['wwan']
rule54=['een','an']
rule55=['f','n']
rule6=['t','te','tu','ti','tee','tuu','nne','nnu','na','ne','nu','naa','dhaa','chaaf','dhaaf','tiif','ach','adh','chuu',
       'at','att','ch','tanu','tanuu','tan','tani']
# stop_word=['akka','akkasumas','akkum','akkuma','ammo','ammoo','ani','booda','booddee','dura','eega','eegana',
#             'eegasii','ennaa','erga','fi','garuu','hanga','henna','hoggaa','hogguu','hoo','illee','immoo','ini','innaa','isaa',
#             'isaan','iseen','itumallee','ituu','ituullee','jechaan','jechuun','kan','kanaaf','kanaafi','kanaafuu','koo','kun',
#             'malee','moo','odoo','ofii','oggaa','oo','osoo','otoo','otumallee','otuu','otuullee','saniif','silaa','simmoo','sun','tahuullee','tanaafi','tanaafuu',"ta'ullee",'tawullee',
#             'waggaa','woo','yammuu','yemmuu','yeroo','yommii','yommuu','yoo','yookaan','yookiiin','yookinimoo','yoom','fi','ennaa']
vowel=['a','e','i','o','u']
double_vowel=['aa','ee','ii','oo','uu']

consunant=['b','c','d','f','g','h',"'",'j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
           'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','z']

def find_R1_R2(word):
    word=word[1:]
    R1=''
    R2=''
    v=0
    ind=0
    c=0
    for i in word:
        if i in consunant and v == 1 and c==0:
            R1=word[ind+1:]
            c=1
        if i in consunant and v >= 2 and c==1:
            R2=word[ind+1:]
            c=2
        if i in vowel:
            v=v+1
        ind=ind+1
    return R1,R2
def measure_vc(words) :
	#accept the word and calculate m in word or sequnce of VC in word C(VC)*V
    words=words[1:]
    v=0
    m=0
    for i in words:
        if (i in consunant) and (v>0):
            m=m+1
            v=0
        if i in vowel:
            v=v+1
    return m


def check_rule_and_remove_suffix(wor):
    # accept the word and remove the suffix depend on the rules 
    if len(wor) <= 3:
        return wor,0
    for m in rule1:
        if wor.endswith(m):
            measure = measure_vc(wor[:-len(m)])
            if measure >= 1:
                ste=wor[:-len(m)]
                if ste[:2] in double_vowel:
                    return wor[:-len(m)],1
    for m in rule2:
        if wor.endswith(m):
            measure = measure_vc(wor[:-len(m)])
            if measure>=1:
                return wor[:-len(m)] , 1

    for m in rule3:
        if wor.endswith(m):
            measure = measure_vc(wor[:-len(m)])
            if measure >= 1:
                ste = wor[:-len(m)]
                if ste[:1] in consunant:
                    return wor[:-len(m)], 1
    for m in rule4:
        if wor.endswith(m):
            measure = measure_vc(wor[:-len(m)])
            if measure >= 1:
                return wor[:-len(m)],1
            if measure == 0:
                return wor[:-len(m)]+"'", 1
    for m in rule51:
        if wor.endswith(m):
            measure = measure_vc(wor[:-len(m)])
            ste = wor[:-len(m)]
            if ste[:1].lower() == 'b' or ste[:1] == 'd' or ste[:1].lower() == 'g':
                if measure >= 1:
                    return wor[:-len(m)], 1
                if measure == 0:
                    return wor[:-len(m)] + "d", 1
    for m in rule52:
        if wor.endswith(m):
            ste = wor[:-len(m)]
            measure = measure_vc(wor[:-len(m)])
            if measure > 0 and (ste[:2] in double_vowel or ((ste[len(ste)-2] in consunant) and (ste[len(ste)-2] in vowel))):
                return ste, 1
    for m in rule53:
        if wor.endswith(m):
            ste = wor[:-len(m)]
            measure = measure_vc(wor[:-len(m)])
            if measure > 0 and (ste[:2] in double_vowel):
                return ste, 1
    for m in rule54:
        if wor.endswith(m):
            ste = wor[:-len(m)]
            measure = measure_vc(wor[:-len(m)])
            if (measure > 0) and ((ste[len(ste)-2] in consunant) and (ste[len(ste)-2] == ste[len(ste)-2])):
                return ste[:-1], 1
            if measure > 0 and ((ste[len(ste)-2] in vowel) and (ste[len(ste)-2] in consunant)):
                return ste, 1
    for m in rule55:
        if wor.endswith(m):
            return wor[:-len(m)], 1
    for m in rule6:
        if wor.endswith(m):
            measure = measure_vc(wor[:-len(m)])
            if measure >= 1:
                return wor[:-len(m)], 1
            if measure == 0:
                return wor[:-len(m)]+"t", 1
    if wor[:1].lower() == 'f' or wor[:1].lower() == 'n':
        return wor[:1], 1
    R1,R2=find_R1_R2(wor)
    r1_index=wor.find(R1)
    # print("R1   "+str(r1_index)+wor[r1_index-1].lower())
    if r1_index>=1:
        if (R1[0] == wor[r1_index-1].lower()) and (R1[0]== wor[0].lower()):
            return R1,1
    return wor, 0


def stemmer(wor):
    print(wor)
    last_letter = ''
    word, rule =check_rule_and_remove_suffix(wor)
    if(len(word)>0):
        last_letter = word[len(word)-1]
    if word.endswith("'"):
        word=word[:-1]
    if (last_letter in vowel) or (last_letter=='n') or (last_letter=='f'): # remove any vowel , n and f at the end of the word 
         word = word[:-1]
         rule =1
    if(rule != 0): # if rule ==0 the is suffix to be removed , if rule ==1 there is uptade , so the word should have to checked again 
        word, rule = check_rule_and_remove_suffix(word)
        if word.endswith("'"):
            word = word[:-1]
        if (last_letter in vowel)or(last_letter == 'n') or (last_letter == 'f'):
                word = word[:-1]
                rule = 1
    return word

# def sentence_spliter(file):
#     return file
# w=input("enter words:")
# print(w+"   "+stemmer(w))
# if(__name__) == "__main__":
#         words = ["Nu", "daawwachuu", "keef","qbu", "galatoomi", "booda", "walitti", "deebina"]
#         words = [stemmer(w) for w in words]
#         print(words)