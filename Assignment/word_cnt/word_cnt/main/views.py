from django.shortcuts import render
import re

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    
    text = request.GET['text']
    text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`…》\”\“·\{\}\\\><%]', ' ', text)
    text_list = text.split()
    text_dict = {}
    for word in text_list:
        word = word.lower()
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    words = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)
    return render(request, 'result.html', {'words' : words})