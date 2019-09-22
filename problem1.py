import datetime
name=input('What is your name? \n')
age=int(input('How old are you? \n'))
hundred=int((100-age) + datetime.datetime.now().year)
print('hello %s. You will turn 100 years old in %s.'%(name,hundred))
