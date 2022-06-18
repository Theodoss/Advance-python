

def main():
    s = '()()(())()()'
    print(balanced_brackets(s))
    s1 = '(())()())'
    print(balanced_brackets(s1))

def balanced_brackets(s):
    ans = 0
    return balanced_helper(s,ans,0)

def balanced_helper(s, ans, i):
    if len(s) == 0:
        if ans == 0:
            return True
        else :
            return False
    else:
        if s[i] == '(':
            ans +=1
        elif s[i] == ')':
            ans -=1
        s = s[i+1:len(s)]
        return balanced_helper(s, ans, i)



if __name__ == '__main__':
    main()

