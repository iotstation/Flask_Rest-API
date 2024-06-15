from flask import Flask, request, jsonify

app=Flask(__name__)


@app.route('/data', methods=['POST'])
def recieved_data():
	try:
		data = request.get_json()
		if data:
			print("Recieved data", data)
			with open("data.log", "a") as f:
				f. write(str(data) + "\n")
			return jsonify({"message":"Data Recived", "data": data}), 200
		else:
			return jsonify({"error": "NO Data Recived"}), 400
	except Exception as e:
		print( f"Error: /{e}")
		return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)