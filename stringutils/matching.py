def zmatch(text,pattern):
    #construct z table
    if len(text) == 0 or len(pattern) > len(text):
        return -1

    concat_text = pattern + u'\u0000' + text
    ztab = [0]*len(concat_text)
    l,r=0,0
    for i in range(1,len(concat_text)):
        if i > r:
            l,r=i,i
            while r < len(concat_text) and concat_text[r-l] == concat_text[r]:
                r+=1
            ztab[i] = r-l
            r-=1

        else:
            k = i - l
            if ztab[k] < r -l +1:
                ztab[i] = ztab[k]
            else:
                l = i
                while r<len(concat_text) and concat_text[r-l] == concat_text[r]:
                    r+=1

                ztab[i] = r - l
                r-=1

    match = 0
    for z in ztab:
        if z == len(pattern):
            return match - len(pattern) - 1
        else:
            match+=1

    return -1



def hashmatch(text,pattern):
    if len(text) == 0 or len(pattern) > len(text):
        return -1
    window = text[0:len(pattern)]
    s = set()
    s.add(pattern)
    i = len(window)
    while i < len(text):
        if window in s:
            return i - len(window)
        else:
            window = window[1:] + text[i]
            i += 1
    return -1


#test
text,pattern = 'yubcdetyuioprefdaslkjfsalkjf;lsajfksajf;jaslkdf;jalkdsjfsa',';jalx'
print zmatch(text,pattern)
print hashmatch(text,pattern)



