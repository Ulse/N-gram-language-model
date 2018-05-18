# -*- coding: utf-8 -*-
"""
Created on Fri Mar 9 12:24:46 2018

@author: uljana
"""
#the usage of the regex
import re
#to iterate over the values of the lists
import operator
import math
#list or abbrevriations for the tokenizer
abbr_periods=['Mrs.', 'Mr.', 'Ms.', 'Prof.', 'Dr.', 'Gen.', 'Rep.', 'Sen.', 'St.', 'Sr.', 'Jr.','Ph.D', 'inc.', 'ft.','etc.']

# importing the corpus
from nltk.book import *

tokens = [word for word in text1]
#where the set of sentences are loaded
# f = open('English.txt', 'r')

#reading  file opened
# s = f.read()

#splits the read file based on '\n' i.e the new line
#lines = re.split(' |\n', s)
#gets lines as a list of all the sentences

#making the words now
#tokens = [word for word in lines if word!='']
#prepares a list of all the words in the entire sentence sequence

# or
#tokens = lines.split(' ') splitting on spaces

#stores all the tokens
tokens1 =  []

#set of regex
for word in tokens:
	f=0
	if f==0:
		if word in abbr_periods:
			f=1
			tokens1.append(word)
		if f==0:
			l=re.findall('(\.)',word)
			if len(l)>0:
				a=l[0]
				if len(a)>1:
					f=1
					tokens1.append(word)
		if f==0:
			l=re.findall('(\w+)(\.)',word)
			if len(l)>0:
				a=l[0]
				f=1
				for j in a:
					tokens1.append(j)
	if f==0:
		l=re.findall('(\()(\w+)(\))(\")(\))(\.)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\d+)(\*|\+|-|/)(\d+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(=)(\")(\w+)(-)(\w+)(:)(\w+)(;)(\")(\|)(\w+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(=)(\")(\w+)(-)(\w+)(:)(\w+)(;)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(=)(\")(\w+)(-)(\w+)(:)(\w+)(;)(\")',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(-)(\w+)(:)(\w+)(;)(\")(\|)(\w+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\|)(\w+)(=)(\")(\d+)(\")',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\d+)(,)(\d+)',word)
		if len(l)> 0:
			f=1
			tokens1.append(word)
	if f==0:
		l=re.findall('(\()(\")(\w+)(\")(\))',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\()(\")(\w+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\")(\w+)(\")(\))',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\()(\")(\w+)(\")',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\()(\w+)(-)(\w+)(\))',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(,)(\w+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\()(\w+)(\))',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\()(\w+)(\))(\.)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\")(\w+)(,|\.)(\")',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\")(\w+)(\")',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(\.)(\")',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(,)(\")',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(-)(\w+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\d+)(/)(\d+)(/)(\d+)',word)
		if len(l)> 0:
			f=1
			tokens1.apppend(word)
	if f==0:
		l=re.findall('(\d+)(-)(\d+)(-)(\d+)',word)
		if len(l)> 0:
			f=1
			tokens1.apppend(word)
	if f==0:
		l=re.findall('(\w+)(;)(\w+)',word)
		if len(l) > 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(.*)(%)',word)
		if len(l) > 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(\'\w)',word)
		if len(l) > 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(:|;|,|%)(\))',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\()(\w+)(:|;|,|%)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(,|:|\"|\()(\w+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\w+)(!|,|\?|;|\"|\))',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		l=re.findall('(\|)(\||\}|-|\w+)',word)
		if len(l)> 0:
			f=1
			a=l[0]
			for j in a:
				tokens1.append(j)
	if f==0:
		tokens1.append(word)
		
	
#query_token is the entire list of tokens from the corpus


#dict to store the unigram and its occurence in the corpus
unigram = {}
for i in range(0, len(tokens1)):
    x = str(tokens1[i])
    if x in unigram:
        unigram[x] += 1
    else:
        unigram[x] = 1


#dict to store the bigram and its occurence in the corpus
bigram = {}
for i in range(0, len(tokens1)-1):
    x = str(tokens1[i])+" "+str(tokens1[i+1])
    if x in bigram:
        bigram[x] += 1
    else:
        bigram[x] = 1

#dict to store the trigram and its occurence in the corpus
trigram = {}
for i in range(0, len(tokens1)-2):
    x = str(tokens1[i])+" "+str(tokens1[i+1])+" "+str(tokens1[i+2])
    if x in trigram:
        trigram[x] += 1
    else:
        trigram[x] = 1



#calculates the probability of a given sentence (with trigram model)
query = raw_input("Provide a sentence: ")

#just for understanding taking query for space seperated sentence
query_token = query.split(" ")
score = 1
perplexity = 1.0
for i in range(2, len(query_token)):
    tri = str(query_token[i-2])+" "+str(query_token[i-1])+" "+str(query_token[i])
    bi = str(query_token[i-2])+" "+str(query_token[i-1])
    
    try:
        c_tri = trigram[tri]
        c_bi = bigram[bi]
    except:
        c_tri = 1
        try:
            c_bi = bigram[bi] + len(bigram)
        except:
            c_bi = 1 + len(bigram)
   
#probab = float(c_tri)/float(c_bi)
#probab = math.log(probab,10)
#score *= probab
#perplexity *= float(1/probab)"""
    probab = float(c_tri)/float(c_bi) 
    score *= probab 
    perplexity *= float(1/probab)
print score
#perplexity of the entered sentence
print perplexity**(1.0/float(len(trigram)))



#printing some top possible sentences from the model
#sorts the trigram first and store keys.

keys = []
for key in sorted(trigram.iterkeys()):
	keys.append(key)

sentence = str(keys[0])

for i in range(1, len(keys)):
    tri = keys[i].split(" ")
    sent_ends = sentence.split(" ")[-2:]
   
    if(tri[2]=="."):
        sentence = sentence +" "+str(keys[i])
        break
    else:
        if(sent_ends[0]==tri[1] and sent_ends[1]==tri[2]):
             sentence = sentence +" "+str(keys[i])
        else:
            continue
    
print "Predicted Sentence: "
print sentence 