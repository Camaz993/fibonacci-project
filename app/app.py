from flask import Flask, request
from fibonacci import fibonacci

# Using flask as rest api host
app = Flask(__name__)

# included default and /fibonacci as 
@app.route('/', methods=['GET'])
@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = request.args.get('n', type=int)
    if n is None:
        return 'Please input paramater "n".', 400
    if n < 0:
        return '"n" must not be a negative interger.', 400
    
    result = fibonacci(n)

    # Return as string to handle large values and be a valid response.
    # I would specific a different format e.g. JSON for a clean API response but assignment specification only wanted the number.
    return str(result)

# Run on port 3000
# Added host='0.0.0.0' so that it can be accessed via docker
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)