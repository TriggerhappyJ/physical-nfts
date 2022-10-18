import random
import time
import escpos
from flask import *
from processing_py import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

p = escpos.Usb(0x0000, 0x0000)
p.text("Physical NFT printer is setup and is ready to go!")
p.cut()


seed = 'nft'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render')
def render():
    return json.dumps(seed+'.png')

@app.route('/render', methods=['POST'])
def generateImage():
    global seed
    fName = request.form['fName']
    lName = request.form['lName']
    info1 = request.form['info1']
    info2 = request.form['info2']
    info3 = request.form['info3']
    print(fName, lName, info1, info2, info3)

    seed = fName+lName+info1+info2+info3
    random.seed(seed)

    pApp = App(800,800) # create window: width, height
    pApp.noStroke()
    pApp.background(random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
    for i in range(random.randrange(5, 100)):
        pApp.fill(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        pApp.rect(random.randrange(200, 600), random.randrange(200, 600), random.randrange(20, 400), random.randrange(20, 400))
        pApp.rotate(random.randrange(0, int(TWO_PI)))
    pApp.redraw() # refresh the window
    pApp.saveFrame('../../../../static/renders/'+seed+'.png')
    time.sleep(0.2)
    pApp.exit()
    return 'Gathered Info!'

@app.route('/print', methods=['POST'])
def print():
    fName = request.form['fName']
    lName = request.form['lName']
    p.image("../static/logo.png")
    p.text("Thanks "+fName+" for claiming your NFT!\n")
    p.text("This reciept doesn't have any monetary value")
    p.text("Your NFT has also been deleted.\n")
    p.text("Thanks again for using Physical NFTS!\n")
    p.text("2022 Physical NFTs™")
    p.cut()
    return 'printing reciept'