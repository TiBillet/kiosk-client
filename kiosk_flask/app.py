from flask import Flask, request, jsonify, make_response, render_template
from flask_cors import CORS
import random
from flask_htmx import HTMX

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:8000", 'http://localhost:8000/'])
htmx = HTMX(app)



@app.route('/scan_nfc/', methods=['GET'])
def reading_nfc():
    rand = random.randint(0, 5)

    if rand == 1:
        print("1 if someone scan the card", 1)
        tag_id = str(random.randint(1,4))
        print("Card number is: ", tag_id)
        return render_template('recived.html', tag_id=tag_id)
    
    print(" ---------  No card scanded  --------- ")
    return render_template('index.html')


# If we want to avoid the decoration we
# can add _post to your method 'recived_data_post'
@app.route('/wait_device_paiment/', methods=['POST'])
def wait_device_paiment():
       
    uuid = request.form.get('uuid')
    total = request.form.get('total')
    pi_data = {
        'uuid': uuid,
        'total': total,
    }

    if random.randint(2,3) != 3:
        print(" User is charging the device ")
        return render_template('asking_device.html',
            pi_data=pi_data)
    
    pi_data['device_confirm_paiment'] = 'confirmation'

    print(f"Total is: {total} and uuid is: {uuid}")
    return render_template('flask_confirmed_paiment.html',
             pi_data=pi_data)


@app.route('/test/', methods=['POST'])
def test_meth():
    bill = request.form.get('bill')
    return render_template('test.html', bill=bill)
    
        

# Declare the host and the route
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2:6997')
