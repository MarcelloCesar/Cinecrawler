from debian

run apt update -y && apt upgrade -y
run apt install -y python3
run apt install -y python3-pip
run apt install -y curl
run apt install -y git

run pip3 install pyTelegramBotAPI
run pip3 install scrapy
run curl https://cli-assets.heroku.com/install.sh | sh