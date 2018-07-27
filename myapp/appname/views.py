from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import numpy.random as rd
#配列を定義するためのもの
import numpy

def appmain(request):
    # Creates a context dictionary (map) to send data to the templated HTML file
    context = {}
	#空いたマス数
    num = 0
    value = 0

    # Retrieve the 'name' parameter, if present, and add it to the context
    if not 'display_number' in request.POST:
    	context['display_number'] = "0"
    	context['opr'] = "+"
    	context['prev_number'] = "0"   	
    else:
    	context['display_number'] = request.POST['display_number']
    	context['opr'] = request.POST['opr']
    	context['prev_number'] = request.POST['prev_number']
    	context['new_number'] = request.POST['new_number']

	# 空いているマスを数える
    for i in range(1,10):
        if appmain.list[i] == 1:
            num += 1

	#結果表示
    if 'result' in request.POST:
        return render(request, 'demo/struckout.html', {"context": "Result", "value": value, "count": appmain.count, "num": num})
	
	#乱数生成
    value = rd.randint(low=0,high=9,size=1)

	#ボールを投げた後に当たったか当たらなかったか
    if 'pitch' in request.POST:
        appmain.count -= 1
        if appmain.list[value] == 0:
            appmain.list[value] = 1
        else:
            return render(request, 'demo/struckout.html', {"context": "Already Open", "value": value, "count": appmain.count, "num": num})
        return render(request, 'demo/struckout.html', {"context": "Struck To ", "value": value, "count": appmain.count, "num": num})
    
	#数字のボタンを間違って押したとき
    if 'btn_num' in request.POST:
        value = 10
        return render(request, 'demo/struckout.html', {"context": "Miss Touch", "value": value, "count": appmain.count, "num": num})
    
    value = 65536
    return render(request, 'demo/struckout.html', {"context": "Game Start", "value": value, "count": appmain.count})

#残りの球数
appmain.count = 8
#的の空いたか空いていないか
appmain.list = numpy.array([0,0,0,0,0,0,0,0,0,0])
