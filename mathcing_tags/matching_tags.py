"""
Create a function named HTMLElements(str) it will take in the str parameter
being passed, which will be a string of HTML DOM elements and plain text.
The elements that will be used are: <b>, <i>, <em>, <div>, <p>. For example:
if str is "<div><b><p>hello world</p></b></div>" then this string of DOM
elements is nested correctly so your function should return the boolean true.
If a string is not nested correctly, return the first element encountered
where, if changed into a different element, would result in a properly
formatted string. If the string is not formatted properly.

For example:

if str is "<div><i>hello</i>world</b>" then your function should return the
string “div” because if the first <div> element were changed into
a <b>, the string would be properly formatted.

Examples:

    Input: "<div><p>this is totally <i>not</i> a test</p></div>"
    Output: true
    
    Input: "<div><div><b></b></div></p>"
    Output: “div”
    
    Input: "<div><p>If your going through <i>hell</i> <p>keep going</b></p></div>"
    Output: “p”
""" 
def HTMLElements(sent):
    # break str into tags and store in an array tags
    tags_temp = sent.split('<')
    # tags = tags2.split('>')
    # print(tags_temp)
    tags = []
    
    for i in range(len(tags_temp)):
        word = tags_temp[i].split('>')
        if word[0] != '':
            tags.append(word[0])

    
    print(tags)
        
    # <b>, <i>, <em>, <div>, <p>
    # a dict storing key-value pairs with opening and closing tags
    # openclose = {'b': '/b', 'i': '/i', 'em': '/em', 'div': '/div', 'p': '/p'}
    openclose = {'/b': 'b', '/i': 'i', '/em': 'em', '/div': 'div', '/p': 'p'}
    # a dict storing how many opening tags there are
    opencount = {'b': 0, 'i': 0, 'em': 0, 'div': 0, 'p': 0}
    
    for el in tags:
        if el in opencount:
            opencount[el] += 1

    print(opencount)
    # for loop go array tags. If it's an opening tag skip it
    # if it's a closing tag: check that it has a matching opening tag and subtract 1 value from the dict with the correspoinding open tag.
    for el in tags:
        if el not in opencount:
            opencount[openclose[el]] -= 1
            
            
    for el in tags:
        if el in opencount and opencount[el] != 0:
            return el

    return True
# print(HTMLElements("<div><div><b></b></div></p>")) # div
# print(HTMLElements("<div><em>If your going through <i>hell</i> <p>keep going</b></em></div>")) # p
# print(HTMLElements("<em><div>well well well</em></div>")) # em



'''
its variation of vaild () - uses a stack to solve
so we can use as stack here
what might get us is the fact its string, one solid string
what we can do, is since our tags all start with diffrent char
if hit a <, that means we're at the start of a tag which means we can check the char right front of it
 if its a letter we know its an opener, if its / we know its a closer
 
create a stack
a dict to keep track of the pairings
loop over our string
if we hit an opener, via the method I said above
    append that openner to the stack
else
    we'll pop from the stack and try to match it to cur char
    if it doesn't match
        return false
        
when the loop ends, if our stack is empty return true else false
'''

def josiah(inpt_str: str) -> bool:
    stack = list()
    pairs = {'b', 'i', 'e', 'd', 'p'}

    for idx in range(len(inpt_str)):
        char = inpt_str[idx]
        if char == '<':
            if inpt_str[idx+1] in pairs:
                stack.append(inpt_str[idx+1])
            else:
                if stack:
                    top = stack.pop()
                    if inpt_str[idx+2] != top:
                        return {'d': 'div', 'e': 'em'}.get(top, top)
                
    return len(stack) == 0



print(josiah("<div><div><b></b></div></p>")) # div
print(josiah("<div><em>If your going through <i>hell</i> <p>keep going</b></em></div>")) # p
print(josiah("<em><div>well well well</em></div>")) # em



