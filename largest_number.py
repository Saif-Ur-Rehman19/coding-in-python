lists = [566,45,8,99,4,5,2,55,97,118,12,0,445,45678987654]
def largest(lists):
    maximum = lists[0]
    for go_through in range(len(lists)-1):
        if lists[go_through+1] > lists[go_through]:
            maximum = lists[go_through+1]
    return str(maximum) + " is the largest number in the list"

# end of largest function

print(largest(lists))

def smallest(lists):
    smal = lists[0]
    for go_untill in range(len(lists)-1):
        if lists[go_untill+1] < lists[go_untill]:
            smal = lists[go_untill+1]
    return str(smal) + " is the smallest number in the list"
#end of smallest function

print(smallest(lists))
