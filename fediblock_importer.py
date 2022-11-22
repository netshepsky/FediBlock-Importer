import configparser
import csv

import requests

# Read settings file
config = configparser.ConfigParser()
config.read('settings.ini')
instance_uri = config['settings']['instance_uri']
access_token = config['settings']['access_token']
headers = {"Authorization": f"Bearer {access_token}"}


def main():
    domains_to_block = []
    # Parse blocklist CSV
    with open('blocklist.csv', 'r') as blocklist_csv:
        csv_reader = csv.reader(blocklist_csv, delimiter=',', quoting=csv.QUOTE_ALL)

        line_count = 0
        for row in csv_reader:
            # Skip header row
            if line_count == 0:
                line_count += 1
                continue
            else:
                domains_to_block.append({
                    'domain': row[0],
                    'block_type': row[1],
                    'reject_media': row[2],
                    'reject_reports': row[3],
                    'private_comment': row[4],
                    'public_comment': row[5],
                    'obfuscate': row[6]
                })

    for domain in domains_to_block:
        # Validate input
        if not len(domain['domain']) > 0:
            print(f"Invalid entry for \"{domain['domain']}\" - domain cannot be blank")
            continue
        elif not domain['block_type'] in ['suspend', 'silence']:
            print(f"Invalid entry for \"{domain['domain']}\" - block_type must be either \"suspend\" or \"silence\"")
            continue
        else:
            reject_media = domain['reject_media'] if domain['reject_media'].lower() == 'true' else 'false'
            reject_reports = domain['reject_reports'] if domain['reject_reports'].lower() == 'true' else 'false'
            obfuscate = domain['obfuscate'] if domain['obfuscate'].lower() == 'true' else 'false'

            r = requests.post(f"https://{instance_uri}/api/v1/admin/domain_blocks", headers=headers, data={
                'domain': domain['domain'],
                'severity': domain['block_type'],
                'reject_media': reject_media,
                'reject_reports': reject_reports,
                'private_comment': domain['private_comment'],
                'public_comment': domain['public_comment'],
                'obfuscate': obfuscate
            })

            print(f"{r.status_code} - {r.content}")


if __name__ == '__main__':
    main()
