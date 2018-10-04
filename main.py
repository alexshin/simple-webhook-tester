from flask import Flask, request, make_response
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/api/v1/integrations/st/web-hooks/user-authorities', methods=['POST'])
def user_authorities_hook():
    content = json.dumps(json.loads(request.data), indent=4, sort_keys=True)
    with open('./requests.log', 'a') as f:
        f.write('\n\n')
        f.write('-' * 30)
        f.write('\n\n')
        f.write('\n'.join([f'{k}: {v}' for k, v in request.environ.items()]))
        f.write('\n\n')
        f.write(content)
        f.write('\n\n')

    return make_response('OK', 200)



@app.route('/api/v1/integrations/st/web-hooks/user-authorities', methods=['GET'])
def user_authorities_log():
    with open('./requests.log', 'r') as f:
        content = f.read()

    resp = make_response(content, 200)
    resp.headers['Content-Type'] = 'text/plain'
    return resp


