def solution(s1, s2):
    from collections import Counter
    ans=""
    s1c=Counter(s1)
    s2c=Counter(s2)
    print(s1c,s2c)
    s1p=0
    s2p=0
    while s1p<len(s1) and s2p<len(s2):
        s1n=s1c[s1[s1p]]
        s2n=s2c[s2[s2p]]
        if s1n<s2n:
            ans+=(s1[s1p])
            s1p+=1
        elif s1n>s2n:
            ans+=(s2[s2p])
            s2p+=1
        else:
            if s1[s1p]<s2[s2p]:
                ans+=(s1[s1p])
                s1p+=1
            elif s1[s1p]>s2[s2p]:
                ans+=(s2[s2p])
                s2p+=1
            else:
                ans+=(s1[s1p])
                s1p+=1
    if s1p<s2p:
        ans+=(s1[s1p:])
    elif s1p>s2p:
        ans+=(s2[s2p:])
    else:
        print("what the deuce")
    return ans
        
            
            
            
            
    
        

