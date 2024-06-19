punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, welcome ---to python."
no_punct = ""
for i in my_str:
   if i not in punctuations:
       no_punct = no_punct + i
print(no_punct)