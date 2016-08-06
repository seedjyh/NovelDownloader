__author__ = 'jiangyh'

from SilukeNovelDownloader import SilukeNovelDownloader
import sys, getopt

def ReadArguments(sysargv):
    novel_book_url = ''
    output_file_path = ''
    opts, args = getopt.getopt(sysargv[1:], "u:w:")
    for op, value in opts:
        if op == '-u':
            novel_book_url = value
        elif op == '-w':
            output_file_path = value
        else:
            print('Unknown argument: ', op)
    return novel_book_url, output_file_path

if __name__ == '__main__':
    url, output_file = ReadArguments(sys.argv)
    if url == '':
        print("No valid URL. Use '-u' to set it.")
        exit()
    downloader = SilukeNovelDownloader()
    book = downloader.DownloadBook(url)
    if output_file == '':
        output_file = book.title() + '.txt'
    book.WriteToFile(output_file)
