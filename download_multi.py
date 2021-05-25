import requests
import time
import sys
import threading
row_max = 127
colmun_max = 127

def download_column(col_num):
    for row in range(0, row_max + 1):
        # url = "https://maps.izurvive.com/maps/Esseker-Sat/0.0.2/tiles/7/{}/{}.png".format(col_num, row)
        # response = requests.get(url)
        # if response.status_code != 200:
        #     print(url) 
        # file_name = "{}_{}.png".format(col_num, row)
        # file = open(file_name, "wb")
        # file.write(response.content)
        # file.close()

        file_name = "{}_{}.png".format(col_num, row)
        try: 
            file = open(file_name)
        except IOError:
            print("File not accessible: " + file_name)
            # redownload it
            url = "https://maps.izurvive.com/maps/Esseker-Sat/0.0.2/tiles/7/{}/{}.png".format(col_num, row)
            response = requests.get(url)
            if response.status_code != 200:
                print(url) 
            file_name = "{}_{}.png".format(col_num, row)
            file = open(file_name, "wb")
            file.write(response.content)
            file.close()
            
        finally:
            file.close()


if __name__ == "__main__":
    for col in range(0, colmun_max + 1):
        threading.Thread(target=download_column, args=(col,)).start()