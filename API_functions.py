import sqlite3
import time

import main
import requests
import json


def getPort(ip):  # obtenir port SRT del Kiloview
    try:
        # cridar API
        url = ('http://{}/api/v1/getStreamService.lua?_LANG=en&format=json&Stream=main'.format(ip))
        r = requests.get(url, headers={'Authorization': "Basic YWRtaW46YWRtaW4="}, timeout=1)
        data = r.json()
        # guardar valors
        ServiceStatus = (data['Data']['ServiceStatus'])
        port = ServiceStatus[2]['URL']
        # retornar valors
        return port[-5:]
    except:
        return 0


def getBitrate(ip):  # obtenir bitrate del Kiloview
    try:
        # cridar API
        url = ('http://{}/api/v1/getVideoEncoding.lua?_LANG=en&format=json&Stream=main&Config=1'.format(ip))
        r = requests.get(url, headers={'Authorization': "Basic YWRtaW46YWRtaW4="}, timeout=1)
        data = r.json()
        # guardar valors
        config = (data['Data']['Config'])
        bitrate = config['Bitrate']
        return bitrate / 1000000  # in Mbps
    except:
        return 0


def setBitrate1(ip):  # obtenir bitrate del Kiloview
    try:
        # cridar API
        url = ('http://{}/api/v1/setVideoEncoding.lua?Stream=main&Bitrate=1000000'.format(ip))
        requests.post(url, headers={'Authorization': "Basic YWRtaW46YWRtaW4="})
    except:
        message = 'Error connection'
        main.main_GUI.show_dialog(main.main_GUI(), message)
        print(message)


def setBitrate20(ip):  # obtenir bitrate del Kiloview
    try:
        # cridar API
        url = ('http://{}/api/v1/setVideoEncoding.lua?Stream=main&Bitrate=20000000'.format(ip))
        requests.post(url, headers={'Authorization': "Basic YWRtaW46YWRtaW4="})
    except:
        message = 'Error connection'
        main.main_GUI.show_dialog(main.main_GUI(), message)
        print(message)


def putiVuelta(ip):
    try:
        setBitrate1(ip)
        url = ('http://{}/api/v1/reboot.lua'.format(ip))
        r = requests.get(url, headers={'Authorization': "Basic YWRtaW46YWRtaW4="})
        time.sleep(25)
        setBitrate20(ip)
    except:
        print('Error')


def setPort(url, port):
    if not port:
        message = 'Invalid: empty port'
        print('Invalid: empty')
        main.main_GUI.show_dialog(main.main_GUI(), message)
    else:
        if port.isdigit() == bool(1):
            try:
                # cridar API
                url2 = (
                    'http://{}/api/v1/setStreamService.lua?_LANG=en&format=json&Stream=main&ID=Dynamic_services[0]&SRT_push.port={}'.format(
                        url, port))
                r = requests.get(url2, headers={'Authorization': "Basic YWRtaW46YWRtaW4="}, timeout=0.5)

            except:
                message = 'Error connection'
                main.main_GUI.show_dialog(main.main_GUI(), message)
                print(message)
        else:
            message = 'Invalid format'
            main.main_GUI.show_dialog(main.main_GUI(), message)
            print(message)


def setOutStream(id_out_stream, application, stream):
    url = 'https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/udp/{}?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
        id_out_stream)
    headers = {'Content-Type': 'application/json'}
    data = {"source_streams": [
        {"application": 'application', "stream": 'stream', "pmt_pid": 7166, "video_pid": 256,
         "audio_pid": 257}]}
    data['source_streams'][0]['application'] = application
    data['source_streams'][0]['stream'] = stream
    req = requests.put(url, data=json.dumps(data), headers=headers)
    # print(req.content)


# def setVmix(id_out_stream, ob_id):
#     conf = main.main_GUI.show_dialog_confirmation(main.main_GUI(), 'Segur que voleu aplicar els canvis?')
#     if conf == 16384:
#         for i in range(len(id_out_stream)):
#             setOutStream(id_out_stream[i], ob_id[i][0], ob_id[i][1])

def source_assignation(button):
    # print(button.text())
    bd_mtx_srt_ins = sqlite3.connect('bd_mtx_srt_ins.db')  # creem connexio
    cur = bd_mtx_srt_ins.cursor()  # creem cursor
    # Ejecuta la consulta
    cur.execute("SELECT application, stream, iden FROM MatriuSRT WHERE name='{}'".format(button.text()))
    # Extrae todos los datos
    appli = cur.fetchall()
    bd_mtx_srt_ins.close()
    main.main_GUI.take_app = appli[0][0]
    main.main_GUI.take_stream = appli[0][1]
    main.main_GUI.source_ident = appli[0][2]
    return appli[0][2]


def dest_assignation(button):
    # #print(button.text())
    bd_mtx_srt = sqlite3.connect('bd_mtx_srt_outs.db')  # creem connexio
    cur = bd_mtx_srt.cursor()  # creem cursor
    # Ejecuta la consulta
    cur.execute("SELECT iden FROM MatriuSRT WHERE name='{}'".format(button.text()))
    # Extrae todos los datos
    identificador = cur.fetchall()
    bd_mtx_srt.close()
    # status
    main.main_GUI.status_dest = button.text()
    main.main_GUI.take_iden = identificador[0][0]
    return identificador[0][0]


def get_status_dest(identificador):
    url = 'https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/udp/{' \
          '}?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
        identificador)
    r = requests.get(url)
    status = r.json()
    #print(status)
    #app = status['setting']['source_streams'][0]['application']
    stream = status['setting']['source_streams'][0]['stream']
    port = status['setting']['port']
    latency = status['setting']['parameters']['latency']
    paused = status['setting']['paused']
    mode = status['setting']['send_mode']
    return stream, port, latency, paused, mode

def get_status_source(identificador):
    url = 'https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/incoming/{' \
          '}?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
        identificador)
    r = requests.get(url)
    status = r.json()
    #print(status)
    #app = status['setting']['source_streams'][0]['application']
    status_stream = status['stream']['status']
    port = status['stream']['port']
    mode = status['stream']['receive_mode']

    return status_stream, port, mode


def take():
    #print(main.main_GUI.take_app)
    #print(main.main_GUI.take_stream)
    #print(main.main_GUI.take_iden)
    # if application != None and stream != None and identificador != None:
    #     setOutStream(identificador, application, stream)
    # else:
    #     print('error')
    setOutStream(main.main_GUI.take_iden, main.main_GUI.take_app, main.main_GUI.take_stream)

def setPortSource(identification, port):
    if not port:
        message = 'Invalid: empty port'
        print('Invalid: empty')
        main.main_GUI.show_dialog(main.main_GUI(), message)
    else:
        if port.isdigit() == bool(1):
            try:
                # cridar API
                url = 'https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/incoming/{}?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
                    identification)
                data = {"port": 'port'}
                data['setting']['parameters']['latency'] = port
                #print(data['stream'][0]['port'])
                headers = {'Content-Type': 'application/json'}
                req = requests.put(url, data=json.dumps(data), headers=headers)
                #print(req.json())

            except:
                message = 'Error connection'
                main.main_GUI.show_dialog(main.main_GUI(), message)
                print(message)
        else:
            message = 'Invalid format'
            main.main_GUI.show_dialog(main.main_GUI(), message)
            print(message)

    # print(req.content)

def restartSource(identificador):
    try:
        # cridar API
        url = ('https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/incoming/{}/restart?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
                    identificador))
        requests.get(url)
    except:
        message = 'Error connection'
        main.main_GUI.show_dialog(main.main_GUI(), message)
        print(message)


def resumePausedSource(identificador, status):
    if status == 'online':
        try:
            # cridar API
            url = ('https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/incoming/{}/pause?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
                        identificador))
            requests.get(url)
        except:
            message = 'Error connection'
            main.main_GUI.show_dialog(main.main_GUI(), message)
            print(message)
    else:
        try:
            # cridar API
            url = ('https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/incoming/{}/resume?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
                        identificador))
            requests.get(url)
        except:
            message = 'Error connection'
            main.main_GUI.show_dialog(main.main_GUI(), message)
            print(message)

def setPortDest(identification, port):
    if not port:
        message = 'Invalid: empty port'
        print('Invalid: empty')
        main.main_GUI.show_dialog(main.main_GUI(), message)
    else:
        if port.isdigit() == bool(1):
            try:
                # cridar API
                url = 'https://api.wmspanel.com/v1/server/61e14acd03e0437a098a9276/mpegts/udp/{}?client_id=42f23a17-1746-4bc0-9a22-e4a71374d714&api_key=512f124433cb25b495a6c44861ebc1a2'.format(
                    identification)
                data = {"port": 'port'}
                data['port'] = port
                #print(data['stream'][0]['port'])
                headers = {'Content-Type': 'application/json'}
                req = requests.put(url, data=json.dumps(data), headers=headers)
                print(req.json())

            except:
                message = 'Error connection'
                main.main_GUI.show_dialog(main.main_GUI(), message)
                print(message)
        else:
            message = 'Invalid format'
            main.main_GUI.show_dialog(main.main_GUI(), message)
            print(message)

    # print(req.content)


def setLatencyDest():

    return 0
