#!/usr/bin/env python3

# Night mode on. Make sure to set USER to your user account

with open('/Users/USER/Library/Application Support/Anki2/prefs21.db', 'r+b') as f:
	content = f.read()
	f.seek(0)
	f.write(content.replace(b'night_mode\x94\x89u.\n', b'night_mode\x94\x88u.\n'))