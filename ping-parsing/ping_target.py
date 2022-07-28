import json
import pingparsing

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = "192.168.85.3"
transmitter.count = 4
result = transmitter.ping()
parsed_result = ping_parser.parse(result)
print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))