from debian

run apt update -y && apt upgrade -y
run apt install -y python3
run apt install -y python3-pip
run apt install -y curl
run apt install -y git

run curl https://cli-assets.heroku.com/install.sh | sh

WORKDIR /var/www/html/cinecrawler/cinecrawler
COPY requirements.txt /tmp/requirements.txt
run pip3 install -r /tmp/requirements.txt

