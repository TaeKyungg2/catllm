from konlpy.tag import Okt
from random import randint
random_num=randint(0,10)
okt=Okt()
def make_cat_style_by_pos(sentence):
    okt_pos=add_space_and_pos(sentence)
    char_location=0
    for pos in okt_pos:
        char_location+=len(pos[0])
        if pos[1]=='Adjective':
            if pos[0][-1]=='다':
                sentence=sentence[:char_location]+'냥'+sentence[char_location:]
                char_location+=1
        elif pos[1]=='Noun':
            if pos[0]=='내' or pos[0]=='나' or pos[0]=='제' or pos[0]=='저':
                sentence=sentence[:char_location-1]+'고양이'+sentence[char_location:]
                char_location+=2
        elif pos[1]=='Josa':
            if randint(0,10)>=5:
                sentence=sentence[:char_location]+', 냥, '+sentence[char_location:]
                char_location+=5
    return sentence
def add_space_and_pos(str):
    str_split=str.split(' ')
    final_str=[]
    for i in str_split:
        final_str=[*final_str,*okt.pos(i)]
        final_str+= [(' ','Space')]
    return final_str
print(make_cat_style_by_pos('저는 곽태경이고 컴퓨터를 좋아합니다.'))