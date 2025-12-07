from pytubefix import YouTube

from pytubefix.cli import on_progress #this module contains the built in progress bar.

import os
def progress_function(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    deleter = 1./1024/1024
    totalsz = (total_size *deleter)
    totalsz = round(totalsz, 1)
    remain = (bytes_remaining*deleter)
    remain = round(remain, 1)
    dwnd = (bytes_downloaded *deleter)
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion, 2)

    # print(f'Total Size: {totalsz} MB')
    print(
        f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')

def read_data(address):
    #in_data = ["OnWktOJHrjQ"]
    with open(address, "r") as fin:
        in_data = [tuple(row.strip().split('/'))[3] for row in fin.readlines()]
    return in_data

indat = read_data("dl.txt")

print(*indat)

def combine(audio: str, video: str, output: str) -> None:

    if os.path.exists(output) and video != output:
        os.remove(output)

    code = os.system(
        f'.\\ffmpeg.exe -i "{video}" -i "{audio}" -c copy "{output}"')

    if code != 0:
        raise SystemError(code)

    code = os.system(
        f'del /Q "{audio}" "{video}"')

output_path = "D:/WorkX/JR/Lections/"

for video in indat:
    try:
        video_url = "https://www.youtube.com/watch?v="+video
        print(video_url)
        yt = YouTube(video_url,  'WEB',on_progress_callback=progress_function, proxies={"http": "http://127.0.0.1:8881",
             "https": "http://127.0.0.1:8881"},)
        name_of_vi = yt.title
        print("stream: ", name_of_vi)
        fun = lambda x: os.path.isfile(os.path.join(output_path, x))
        files_list = filter(fun, os.listdir(output_path))

        # Create a list of files in directory along with the size
        size_of_file = [
            (f, os.stat(os.path.join(output_path, f)).st_size)
            for f in files_list
        ]
        # Iterate over list of files along with size
        # and print them one by one.
        need_to_dl = True
        for f, s in size_of_file:
            #print("{} : {}MB".format(f, round(s/(1024*1024),3)))
            if f == name_of_vi:
                if s == 0:
                    need_to_dl = False
        if not need_to_dl:
            continue
        quals_ids ={}
        quals = (yt.streams.filter(file_extension='mp4'))
        for qual in quals:
            print("q:", qual)
            td = str(qual).split(':')[1].split('" ')
            mapstr={}
            for var in td:
                lst = var.split("=")
                mapstr[lst[0].strip()] = lst[1].strip()[1:]
            #print(mapstr)
            if 'res' in mapstr.keys():
                if mapstr['res'] not in quals_ids.keys():
                    quals_ids[mapstr['res']] = (mapstr['itag'],mapstr['progressive']== True)

        need_itag = None
        is_prog = True
        if "720p" in quals_ids.keys():
            need_itag = quals_ids["720p"][0]
            is_prog = quals_ids["720p"][1]
        else:
            minres = 0
            for key, val  in quals_ids.items():
                int_val = int(key[0:-1])
                print(int_val)
                if need_itag == None or minres>int_val:
                    minres = int_val
                    need_itag = int(val[0])
                    is_prog = int(val[1])
        print("choosen:",need_itag)
        stream = yt.streams.get_by_itag(need_itag)#get_highest_resolution()
        while True:
            dl_flag = True
            try:
                stream.download(output_path)
            except Exception as e:
                dl_flag=False
            if dl_flag:
                break
        print('video', is_prog)
        if not is_prog:
            print('audio..')
            audio_stream = yt.streams. \
                filter(mime_type='audio/mp4'). \
                order_by('filesize'). \
                desc().first()
            print('\nDownload audio...')
            while True:
                dl_flag = True
                try:
                    audio_stream.download()
                except Exception as e:
                    dl_flag=False
                if dl_flag:
                    break
            print('done')
            combine(audio_stream.default_filename, output_path+stream.default_filename, f'{output_path}{yt.title}.wa.mp4')
            print('combined')
        print('done')
    except Exception as e:
        print("ErrorDownloadVideo  |  " + str(video_url) +' '+e.__repr__())
    finally:
        print("Succsess | "+str(video_url))
        break