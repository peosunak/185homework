#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

days = 365
ppl    = 25
trials = 1000
storedbday = 0 # we wil be adding to this so it needs to be empty

# need a loop for to select person, random bday
for i in range(trials): 		# need range to iterate
	cal = []		# here is our epty list for the 365 day calendar
	for j in range(days):
		cal.append(0)
	for j in range(ppl):
		randate = random.randint(0, days-1)
		cal[randate] += 1
	# does the calendar have any 2's
	count = 0
	for s in cal:
		if s > 1:
			count += 1
	if count > 0:			
		storedbday += 1
print('%.3f' % (storedbday/trials))

# worked on this with krikor

"""
python3 33birthday.py
0.571
"""

