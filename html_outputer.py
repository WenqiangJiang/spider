# _*_ coding:utf-8 _*_
'''
Created on 2016年8月6日

@author: 姜文强
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html', 'w',encoding='utf-8') #在windows下面，新文件的默认编码是gbk，这样的话，python解释器会用gbk编码去解析我们的网络数据流txt，然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了，出现上述问题。 解决的办法就是，改变目标文件的编码 
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            print(data['title'])
            fout.write('<td>%s</td>' % data['title']) #也可能需要解码
            fout.write('<td>%s</td>' % data['summary']) #fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
    
    
    
    



