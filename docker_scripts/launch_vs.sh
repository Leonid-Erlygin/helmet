docker run\
 -d\
 --rm\
 -v "$(realpath ..)":/home/helmet\
 --runtime nvidia\
 --name helmet_vs\
 -p 5009:5009\
 -t helmet\
 /root/.local/bin/code-server\
 --bind-addr 0.0.0.0:5009\
 --auth none\

