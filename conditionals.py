agreeableness = raw_input("A stranger says hello. Do you *smile*, *scowl*, *ignore*, *flip off*?")
ambition = raw_input("In school, were you an *a*, *b*, *c* & lower  student?")
neuroticism = raw_input("Do you consider yourself someone who *worries* or someone who goes with the *flow*?")
openness = raw_input("Someone suggests a last minute change of plans. Are you *happy* or *frightened*?")

if openness == "happy" and neuroticism == "flow" and agreeableness == "smile":
    if ambition == "a" or ambition == "b":
        print "You are easygoing and get along with people but you get business done."
    elif ambition == "c":
        print "You are a party animal who gets along with people but does not do much else."
else:
    print "You are too complicated to understand. Sorry."
