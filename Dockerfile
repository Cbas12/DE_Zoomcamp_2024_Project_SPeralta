FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

# Add Debian Bullseye repository
RUN echo 'deb http://deb.debian.org/debian bullseye main' > /etc/apt/sources.list.d/bullseye.list

RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk

# Remove Debian Bullseye repository
RUN rm /etc/apt/sources.list.d/bullseye.list

# Note: this overwrites the requirements.txt file in your new project on first run. 
# You can delete this line for the second run :) 
COPY requirements.txt ${USER_CODE_PATH}requirements.txt 

RUN pip3 install -r ${USER_CODE_PATH}requirements.txt
