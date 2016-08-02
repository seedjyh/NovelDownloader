__author__ = 'jiangyh'

from SilukeNovelDownloader import SilukeNovelDownloader

if __name__ == '__main__':
    downloader = SilukeNovelDownloader()
    book = downloader.DownloadBook('http://www.siluke.tw/ny10354/')
    #book = downloader.DownloadBook('http://www.siluke.tw/ny26173/')
    book.WriteToFile(book.title() + '.txt')
