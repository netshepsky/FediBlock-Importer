#### UPDATE 2024-02-18: This tool is no longer necessary, you can import blocklists directly into Mastodon in newer versions. From your settings page, go to Moderation -> Federation -> Import. Export your existing blocklist first to get a sample of the format your blocklist should be imported in.


This is a tool for bulk blocking federation with Mastodon instances.

## Setup

1. Copy `settings.ini.example` to `settings.ini`
2. Create a new Mastodon application in the settings under Development -> New Application
3. Grant the application `admin:write` permission, and copy the access token to `settings.ini`
4. Enter the URL for your Mastodon instance (excluding the `https://`) in `settings.ini`

## Blocklist formatting

Add rows to `blocklist.csv` for each domain you want to block in the following format:

```
domain,block_type,reject_media,reject_reports,private_comment,public_comment,obfuscate
```

`block_type` should be either `silence` or `suspend`

`reject_media`, `reject_reports`, and `obfuscate` should be **True** or **False** (case-insensitive)

## Usage

1. Install required dependencies (literally just [`requests`](https://pypi.org/project/requests/))
2. `python fediblock_importer.py`
