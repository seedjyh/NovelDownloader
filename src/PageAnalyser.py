__author__ = 'jiangyh'

class PageAnalyser:
    def Utf8ToAnsi(self, str):
        unicode_str = str.decode('utf-8')
        ansi_str = ''
        for u in unicode_str:
            try:
                ansi_str = ansi_str + u.encode('gbk')
            except UnicodeEncodeError:
                pass
        return ansi_str
