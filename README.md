# 6490-project
Project code for CS6490

auto_eavesdrop.sh \
  Run this script to automatically set up ARP spoofing between smartphone and plug and then record network packets between those devices using tshark.\
  Run with "./auto_eavesdrop.sh [smartphoneIP]"

replay.py\
  A script for replaying saved payloads.\
  Run the script with the -i (ip) and -f (file) arguments as follows:
  
  python replay.py -f misc/turn_off_packet -i 192.168.0.83
  - Two sample payloads (turn_on_packet, and turn_off_packet) can be found in the misc folder
  - Optionally add the -p (port) argument to change port numbers

send_json.py
  A script for sending json objects to a device.\
  Run the script with the -i (ip) argument as well as either the -j (json) or -c (command) arguments as follows (both examples turn on the device):
  
  python send_json.py -i 192.168.0.83 -c on
  
  python send_json.py -i 192.168.0.83 -j "{\"context\":{\"source\":\"46a4d58b-6279-432c-ae23-e115c2db8354\"},\"system\":{\"set_relay_state\":{\"state\":1}}}"

  Run with -h flag to see other command options