
def reverse(strng):
    n = len(strng)
    if n == 1:
        return strng[0]
    else:
        return strng[n-1] + reverse(strng[:n-1])

def reverse_1(strng):
    if len(strng) <= 1:
      return strng

    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])

print(reverse("abcd"))
print(reverse_1("abcd"))