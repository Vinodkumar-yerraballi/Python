def find_middle_string(string):
    if len(string)==0:
        return 'no words'
    if len(string)<1:
        return string
    else:
        result=len(string)//2
        if len(string)%2==0:
            print('even length word')
        else:
            print('odd length word')
    
    return string[result]
    
intput='vinod'
print(find_middle_string(intput))