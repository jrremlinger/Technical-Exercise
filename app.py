from flask import Flask, render_template
import eml_parser
import glob

app = Flask(__name__, static_url_path='/static')
files = glob.glob('./converted/*.eml')
emails = []

# Method for parsing data from a single email
def parse_email(file_path):
	# Store the raw text data from the email
	with open(file_path, 'rb') as f:
		raw_email = f.read()

	# Use the eml_parser library to parse the email into processable json
	parsed = eml_parser.EmlParser().decode_email_bytes(raw_email)

	# Grab required fields from the parsed data and store it as an object in the emails list
	emails.append({
		'to' : parsed.get('header').get('to'),
		'from' : parsed.get('header').get('from'),
		'date' : parsed.get('header').get('date'),
		'subject' : parsed.get('header').get('subject'),
		'message_id' : parsed.get('header').get('header').get('message-id')
	})

	# Close the opened file
	f.close()

# Process all .eml files in the converted folder
for file in files:
	parse_email(file)

@app.route('/')
def index():
	return render_template('index.html', data=emails)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5000)