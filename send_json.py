import socket
from encryption import encrypt, decrypt
import argparse

# TAKEN FROM https://github.com/softScheck/tplink-smartplug/blob/master/tplink_smartplug.py
presets  = {'info'     : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"system":{"get_sysinfo":{}}}',
            'on'       : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"system":{"set_relay_state":{"state":1}}}',
            'off'      : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"system":{"set_relay_state":{"state":0}}}',
            'ledoff'   : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"system":{"set_led_off":{"off":1}}}',
            'ledon'    : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"system":{"set_led_off":{"off":0}}}',
            'cloudinfo': '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"cnCloud":{"get_info":{}}}',
            'wlanscan' : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"netif":{"get_scaninfo":{"refresh":0}}}',
            'time'     : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"time":{"get_time":{}}}',
            'schedule' : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"schedule":{"get_rules":{}}}',
            'countdown': '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"count_down":{"get_rules":{}}}',
            'antitheft': '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"anti_theft":{"get_rules":{}}}',
            'reboot'   : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"system":{"reboot":{"delay":1}}}',
            'reset'    : '{"context":{"source":"46a4d58b-6279-432c-ae23-e115c2db8354"},"system":{"reset":{"delay":1}}}',
}

def main():
    parser = argparse.ArgumentParser(description='Send commands to TPLink device')
    parser.add_argument('-i', '--ip', help="ip address of TPLink device")
    parser.add_argument('-p', '--port', help="The port number for the TPLink device", type=int, default=9999)

    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("-c", "--command", help="Premade commands that are available: ".join(presets), choices=presets)
    g.add_argument('-j', '--json', help="Json string to send to the device")
    args = parser.parse_args()

    if args.json is None:
        content = presets[args.command]
    else:
        content = args.json

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    content_json = encrypt(content)
    try:
        s.connect((args.ip, args.port))
        s.send(content_json)

        # Receive data from the server and shut down
        received = s.recv(1024)
        received = decrypt(received[4:])
        print(f'Received response: {received}')

    finally:
        s.close()

if __name__ == "__main__":
    main()

