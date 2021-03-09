# pcb-defect-detection-api

## darknet
`git clone https://github.com/AlexeyAB/darknet.git`

`cd Darknet`

`sed -i 's/OPENCV=0/OPENCV=1/' Makefile`

`sed -i 's/LIBSO=0/LIBSO=1/' Makefile`

`sed -i 's/DEBUG=0/DEBUG=1/' Makefile`

`make`


## API
`cd ../`

`git clone https://github.com/anabdck/pcb-defect-detection-api.git`

`cd pcb-defect-detection-api`

`pip3 install virtualenv`

`python3 -m venv flask_venv`

`source flask_venv/bin/activate`

`pip3 install -r requirements.txt`

`cp ../Darknet/libdarknet.so libdarknet.so`

`python3 run.py runserver`

![4](https://github.com/anabdck/pcb-defect-detection-api/tree/main/app/static/4.png)
![1](https://github.com/anabdck/pcb-defect-detection-api/tree/main/app/static/1.png)
![2](https://github.com/anabdck/pcb-defect-detection-api/tree/main/app/static/2.png)
![3](https://github.com/anabdck/pcb-defect-detection-api/tree/main/app/static/3.png)
