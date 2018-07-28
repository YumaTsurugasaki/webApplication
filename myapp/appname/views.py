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

	# 空いているマスを数える
    for i in range(1,10):
        if appmain.list[i] == 1:
            num += 1

	#結果表示
    if 'result' in request.POST:
        return render(request, 'demo/struckout.html', {"context": "結果", "value": value, "count": appmain.count, "num": num})
	
	#乱数生成
    value = rd.randint(low=0,high=9,size=1)

	#ボールを投げた後に当たったか当たらなかったか
    if 'pitch' in request.POST:
        appmain.count -= 1
        if appmain.list[value] == 0 and appmain.count >= 0:
            appmain.list[value] = 1
        else:
            return render(request, 'demo/struckout.html', {"context": "既に空いています", "value": value, "count": appmain.count, "num": num})
        return render(request, 'demo/struckout.html', {"context": " 番に当たった！！ ", "value": value, "count": appmain.count, "num": num})
	
	#数字のボタンを間違って押したとき
    if 'btn_num' in request.POST:
        value = 10
        return render(request, 'demo/struckout.html', {"context": "そこは押せません", "value": value, "count": appmain.count, "num": num})
  
    #ゲーム終了時のリセット
    if 'reset' in request.POST:
	    appmain.count = 10
	    appmain.list = numpy.array([0,0,0,0,0,0,0,0,0,0])
	    return render(request, 'demo/struckout.html', {"context": "リセット", "value": value, "count": appmain.count, "num": num})

  
    value = 65536
    return render(request, 'demo/struckout.html', {"context": "ゲームスタート", "value": value, "count": appmain.count})

#残りの球数
appmain.count = 10
#的の空いたか空いていないか
appmain.list = numpy.array([0,0,0,0,0,0,0,0,0,0])
