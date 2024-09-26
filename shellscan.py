#!/usr/bin/python3
# Code by satomoru

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time

global starttime

class xiroshigo():

    def __init__(self):
        self.scan()
        
    def scan(self):

        parser = argparse.ArgumentParser(prog="satomoru.py", description="Simple Find Shell in Website")
        parser.add_argument("-m", dest="domain", help="you url")
        parser.add_argument("-d", dest="wordlist", help="you .txt faylingiz")
        args = parser.parse_args()
        if not args.domain:
            sys.exit("\033[36mUsed: shellscan.py -m kun.uz -d text.txt")
        if not args.wordlist:
            sys.exit("\033[36mUsed: python shellscan.py -m kun.uz -d text.txt")
            

        site = args.domain
        print("\033[96m[?] \033[0mStart Crawling...")
        print("\033[96m[!] \033[0mWait a sec!","\n")
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"

        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("\033[91mUpss, Wordlist Not Found!\033[0m")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print("\033[91mWordlist Can\'t Close!\033[0m")
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        found = []
        resp_codes = {403 : "403 forbidden", 401 : "401 unauthorized"}
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("[{0}]".format(time.strftime("%H:%M:%S")),"\033[92mFound:","\033[0m/"+psx)
                    found.append(url)
                    
                except HTTPError as e:
                    if e.code == 404:
                        print("[{0}]".format(time.strftime("%H:%M:%S")),"\033[91mError:","\033[0m/"+psx)
                    else:
                        print("[{0}]".format(time.strftime("%H:%M:%S")),"\033[92minfo :","\033[33m/"+psx,"\033[92mstatus:\033[33m",resp_codes[e.code])
                        
                except URLError as e:
                    sys.exit("\033[31m[!] Upss, No Internet Connection")
                except Exception as er:
                    print("\n\033[93m[?] \033[0mYour Connection Is Bad")
                    print("\033[93m[!] \033[0mExit Program")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print("[?] \033[0mCTRL+C Detected")
                print("[!] \033[0mExit")
                time.sleep(2)
                exit()
        
        if found:
            print("[+] Result Found\033[92m")
            print("\n".join(found))
            print("\033[96m[?] \033[0mTime Elasped: \033[35m%.2f\033[0m Seconds" % float(time.time()-starttime))
        else:
            print("[!] \033[0mCould Not Find Any Shell Backdoor")
            print("[?] \033[0mTime Elasped: \033[33m%.2f\033[0m Seconds" % float(time.time()-starttime))
                
    def banner():

        info = """

╭━━━┳╮╱╱╱╱╭╮╭╮
┃╭━╮┃┃╱╱╱╱┃┃┃┃
┃╰━━┫╰━┳━━┫┃┃┃╭━━┳━━┳━━┳━╮
╰━━╮┃╭╮┃┃━┫┃┃┃┃━━┫╭━┫╭╮┃╭╮╮
┃╰━╯┃┃┃┃┃━┫╰┫╰╋━━┃╰━┫╭╮┃┃┃┃
╰━━━┻╯╰┻━━┻━┻━┻━━┻━━┻╯╰┻╯╰╯
                @satomoru

              """
        return info
    print(banner())
                
if __name__ == '__main__':
    xiroshigo()
