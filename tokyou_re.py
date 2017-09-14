import subprocess
import os
import re

def main():

    #get chapters

    page = subprocess.check_output(["curl", "http://ww1.tokyoghoulre.com/chapter/tokyo-ghoulre-chapter-001/"])
    chapters = re.findall(r'value="(.*?)"', page)

    for chapter in chapters:
        name = chapter.split('/')
        name = name[-2]
        page = subprocess.check_output(["curl", chapter])
        srcs = re.findall(r'src="(.*?)"', page)
        srcs = re.findall(r'https?://\S+?\.(?:png)', page)
        os.makedirs("tokyo_re/"+name)
        i = 0
        for src in srcs:
            src_name = src.split('/')
            src_name = src_name[-2]
            subprocess.call(["wget", src, "-O", "tokyo_re/" + name + str(i) + "-" + src_name +".png"])
            i = i + 1

if __name__ == '__main__':
    main()
