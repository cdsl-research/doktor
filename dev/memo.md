
port forward on windows
```
netsh interface portproxy add v4tov4 listenport=27017 listenaddr=127.0.0.1 connectport=30017 connectaddress=127.0.0.1
```

remove config
```xml
netsh interface portproxy delete v4tov4 listenport=27017 listenaddr=127.0.0.1
```

show
```xml
netsh interface portproxy show all

```