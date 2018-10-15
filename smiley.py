"""
Gary Simmons
March 2018

Kata Prompt Description: Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :] 

Example cases:

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note: In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same

Happy coding!
"""


def smileyIdentifier(emoticon):
    elements=list(emoticon)
    parts=len(elements)
    eyes=elements[0]
    mouth=elements[-1]
    
    part1=eyeValidation(eyes)
    part2=mouthValidation(mouth)
    
    if parts==2:
        if (part1+part2)==parts:
            value=1
        else:
            value=0
    if parts==3:
        nose=elements[1]
        part3=noseValidation(nose)
        if (part1+part2+part3)==parts:
            value=1
        else:
            value=0
    return value
    
def eyeValidation(eyes):
    if (eyes==';' or eyes==':'):
        value=1
    else:
        value=0
    return value
    
def mouthValidation(mouth):
    if (mouth==')' or mouth=='D'):
        value=1
    else:
        value=0
    return value
    
def noseValidation(nose):
    if (nose=='-' or nose=='~'):
        value=1
    else:
        value=0
    return value

def count_smileys(arr):
    smileys=0
    for x in arr:
        emotePositivity=smileyIdentifier(x)
        smileys=smileys+emotePositivity
        
    return smileys#the number of valid smiley faces in array/list
