# I have  this site : Anuj sharma
from django.http import HttpResponse
from django.shortcuts import render
def index2(request):
    return render(request,'index2.html')

def about(request):
    return  render(request,'about.html')
def analyze(request):
    djtext = request.POST.get('text')
    djresposne =request.POST.get('removepunchuation','off')
    djcap = request.POST.get('fullCap','off')
    djnewlinere = request.POST.get('newlineremover','off')
    djextraspace = request.POST.get('spaceremover','off')
    djcharcount = request.POST.get('charcount','off')

    punch = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    purpose = list()

    if djresposne == 'on':
      analyze = str()
      for char in djtext:
         if char not in punch :
            analyze = analyze+char
      purpose.append('remove punctuation')
      djtext = analyze

    if(djcap=='on'):
        analyze=str()
        for char in djtext:
                analyze  = analyze + char.upper()
        purpose.append('Changed to Capitilize')
        djtext=analyze

    if (djextraspace == 'on'):
        analyze = str()
        djtext.replace(" ",'')
        print(analyze:=" ".join(djtext.split()))
        purpose.append('Removed extra space')
        djtext=analyze

    if (djcharcount == 'on'):
        charcounting = 0
        for i in djtext:
            if i !=' ':
                charcounting+=1
        purpose.append('Total character count')
        djtext = djtext + ' count:' +str(charcounting)



    if (djnewlinere == 'on'):
        analyze = str()
        for char in djtext:
            # print(char)
            if char != '\n' and char!='\r':
              analyze = analyze + char
            else:
                analyze = analyze + ' '

        purpose.append('Remove new line')
        djtext = analyze

    if purpose != []:
        params = {'purpose': purpose, 'analyzed_text': djtext}
        return render(request, 'analyze.html', params)
    else:
        print(purpose)
        return render(request, 'error.html')
