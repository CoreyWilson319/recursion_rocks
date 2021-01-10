# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss, results = []):
    ss = list(ss)
    if len(ss) == 1:
        results.append(ss[0])
        print("1")
        ', '.join(results)
        return print(str(''.join(results)))
    else:
        results.append(ss[-1])
        del ss[-1]
        ', '.join(ss)
        print(results)
    reverse(ss, results)

            

# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"