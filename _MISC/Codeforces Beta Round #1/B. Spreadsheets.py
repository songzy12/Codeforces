n = int(raw_input())
for i in range(n):
    s = raw_input()
    import re
    rc = re.split('(\D+)', s)
    # print rc
    if len(rc) == 3:
        c, r = rc[1], rc[2]
        c_ = 0
        for i in c:
            c_ = c_*26 + ord(i)-ord('A')+1
        print 'R'+r+'C'+str(c_)
    else:
        r, c = rc[2], int(rc[4])
        c_ = ''
        while c:
            # when c = 26, should print 'Z'
            res = (c-1)%26 
            c_ = chr(res+ord('A')) + c_
            c = (c-1-res)//26
        print c_ + r
