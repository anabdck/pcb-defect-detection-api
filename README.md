# pcb-defect-detection-api

![4](/app/static/4.jpg)

### compilando darknet
`git clone https://github.com/AlexeyAB/darknet.git`

`cd Darknet`

`sed -i 's/OPENCV=0/OPENCV=1/' Makefile`

`sed -i 's/LIBSO=0/LIBSO=1/' Makefile`

`sed -i 's/DEBUG=0/DEBUG=1/' Makefile`

`make`


### API
`cd ../`

`git clone https://github.com/anabdck/pcb-defect-detection-api.git`

`cd pcb-defect-detection-api`

`pip3 install virtualenv`

`python3 -m venv flask_venv`

`source flask_venv/bin/activate`

`pip3 install -r requirements.txt`

`cp ../Darknet/libdarknet.so libdarknet.so`

`python3 run.py runserver`

### Página Inicial 1
![1](/app/static/1.png)


### Página Inicial 2
![2](/app/static/2.png)


### resultados
![3](/app/static/3.png)
