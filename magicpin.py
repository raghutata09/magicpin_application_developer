import re

# Check min and max length of password
def min_and_max_length (passw):
    if(len(passw)<6):
        return "Failure Password must be at least 6 characters long."
    if(len(passw)>12):
        return "Failure Password must be at max 12 characters long."
    return 1

# Check if password has atleast one character in [a-z],[0-9],[A-Z] and [*$_#=@]
def pass_atleast_one_character(passw):
    if not re.search(r'[a-z]',passw):
        return "Failure Password must contain at least one letter from a-z."
    if not re.search(r'[0-9]',passw):
        return "Failure Password must contain at least one letter from 0-9."
    if not re.search(r'[A-Z]',passw):
        return "Failure Password must contain at least one letter from A-Z."
    if not re.search(r'[*$_#=@]',passw):
        return "Failure Password must contain at least one letter from *$_#=@."
    return 1

# Check if password doesn't contain [%!)(]
def pass_cannot_contain(passw):
    if re.search(r'[%!)(]',passw):
        return "Failure Password cannot contain %!)(."
    return 1



#12sdA@83,aF1#,2w3E*%dg,2We3345,1234567
password_list=str(input())
passwords=password_list.split (",")
for i in passwords:
    passw=i.strip()
    ans=min_and_max_length(passw)
    if(ans==1):
        ans=pass_atleast_one_character(passw)
        if(ans==1):
            ans=pass_cannot_contain(passw)
            if(ans==1):
                print(passw, "Success")
            else:
                print(passw, ans)
        else:
            print(passw, ans)
    else:
        print(passw, ans)   
