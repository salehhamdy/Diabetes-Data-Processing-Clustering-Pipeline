FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pandas
RUN pip3 install numpy 
RUN pip3 install seaborn
RUN pip3 install matplotlib
RUN pip3 install scikit-learn
RUN pip3 install scipy

RUN mkdir -p /home/doc-bd-a1/

COPY diabetes.csv /home/doc-bd-a1/

COPY load.py /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/
COPY vis.py /home/doc-bd-a1/
COPY model.py /home/doc-bd-a1/

CMD ["/bin/bash"]
