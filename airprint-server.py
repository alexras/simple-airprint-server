#!/usr/bin/env python3

import argparse
import shlex
import socket
import subprocess


def airprint_server(name: str, domain: str = '.'):
    scan_process = subprocess.Popen(
        ['dns-sd', '-L', name, '_ipp._tcp', domain],
        stdout=subprocess.PIPE
    )

    for line in scan_process.stdout:
        line = line.decode('utf-8').strip()

        if 'txtvers=' in line:
            txt_record = dict(
                chunk.split('=')
                for chunk in shlex.split(line)
            )

            print(f'Found a service named "{name}"; registering its AirPrint version ...')

            txt_record['pdl'] += ',image/urf'
            # These parameters are only a guess at the right URF parameters, based on the CUPS
            # documentation. YMMV.
            txt_record['URF'] = 'CP1,MT1-2-8-9-10-11,OB1,OFU0,PQ3-4-5,RS300-600,SRGB24,W8-16,DEVW8-16,DEVRGB24-48,ADOBERGB24-48,DM3,IS1,V1.3'

            airprint_name = f'{name} AirPrint'

            register_cmd = [
                'dns-sd', '-R', airprint_name, '_ipp._tcp.,_universal', domain, '631'
            ]

            register_cmd.extend(f'{k}={v}' for k, v in txt_record.items())

            subprocess.run(register_cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('name', help='the DNS-SD service to replicate over AirPrint')

    args = parser.parse_args()

    airprint_server(**vars(args))
