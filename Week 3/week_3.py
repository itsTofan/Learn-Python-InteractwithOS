import re
#Regular Expressions A regular expression, also known as regex or regexp, is essentially a search query for text that's expressed by string pattern.
#A regular expression, also known as regex or regexp, is essentially a search query for text that's expressed by string pattern. 
#When you run a search against a particular piece of text, anything that matches a regular expression pattern you specified, is returned as a result of the search.
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
#print(log[index+1:index+6])
#use regular experession
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

#basic match with grep
#grep is an essential Linux and Unix command. It is used to search text and strings in a given file
#grep in linux. 
#grep thon /usr/share/dict/words

#always use raw string for regular expression in python
result = re.search(r"aza", "plaza")
print (result)
result = re.search(r"aza", "bazaar")
print (result)
result = re.search(r"aza", "test")
print (result)

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

#Wildcards and Character Classes
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy9"))
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) #char not a letter
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")) #char not a letter
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

#Repetition Qualifiers
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

#Escaping Characters
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

#Regex Example
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_ variable1"))

#advance regular expression
#Caputuring groups - portion of the parten that are enclosed in parantheses
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada") #\w will match letters, number, underscrore
print(result)
print(result.group())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))

def rearrenge_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrenge_name("Lovelace, Ada"))
print(rearrenge_name("Ritchie, Dennis"))
print(rearrenge_name("Hopper, Grace M."))

#Repetition Qualifier
#match any string exactly 5 letter
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost"))
print(re.findall(r"\w{5,10}", "I really like strawberry"))
print(re.search(r"s\w{,20}", "I really like strawberry"))

#extractring process ID using regex
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])


def extract_pid(log_line):
    regex = r"\[(\d+)\]" 
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

#split and replace
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
print(re.sub(r"^([\w .-]), ([\w .-]*)$", r"\2\1" ,"Lovelace, Ada"))