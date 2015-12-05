def left_join(phrases):
	phrases = ",".join(phrases)
	reps = {'right':'left'}
	for item, change in reps.items(): # in python 2 this is reps.iteritems()
		phrases = phrases.replace(item, change)
	print (phrases)


left_join(("left", "right", "left", "stop"))
left_join(("bright aright", "ok"))
left_join(("brightness wright",))
