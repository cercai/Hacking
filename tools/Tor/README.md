
Install tor

```bash
sudo apt install -y tor
```

Uncomment the following lines in the tor configuration file `/etc/tor/torrc`

```bash
ControlPort 9051
CookieAuthentication 1   # Replace 0 by 1
```

Restart the tor service
```bash
service tor restart
```

Notice the IP address changing when the curl command is preceded by `torify`.

```bash
curl https://ifconfig.so
torify curl https://ifconfig.so

curl https://ifconfig.me
torify curl https://ifconfig.me
```

