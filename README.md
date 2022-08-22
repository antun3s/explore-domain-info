This python tool helps to get domain, DNS server, mail server and web server

After installed you just need to run:

`explore-domain-info domain.com`

![Demo - explore-domain-info ](https://github.com/antun3s/explore-domain-info/blob/master/example.gif?raw=true)

### to install:
Debian/Ubuntu based: `sudo apt install python-pip`

Arch/Manjaro based: `sudo pacman -S python-pip`

```bash
wget https://github.com/antun3s/explore-domain-info/archive/refs/heads/master.zip
unip master.zip
cd explore-domain-info-master/
pip install -r requirements.txt
chmod +x explore-domain-info.py
sudo cp explore-domain-info.py /usr/local/bin/

```

### to run
After to do this, you easily can run on any path:

`explore-domain-info domain.com`