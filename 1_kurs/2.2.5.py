learners_french = ['a','b','c','d','e','f']
pianists = ['a','b','g','h','e','l']
swimmers = ['l','f','a','b','e']
set_learners_french = set(learners_french)
set_pianists = set(pianists)
set_swimmers = set(swimmers)
s1 = set_swimmers.intersection(set_pianists)
s2 = s1.intersection(set_learners_french)
print(s1.difference(s2))