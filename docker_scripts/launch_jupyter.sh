docker run\
	-d\
	--rm\
	-v "$(realpath ..)":/home/helmet\
	--name helmet_jupyter_lab\
	--runtime nvidia\
	-p 5008:5008\
	-t helmet\
	jupyter lab\
	--ip 0.0.0.0\
	--port 5008\
	--allow-root\
	--NotebookApp.token=''\
	--NotebookApp.password=''\
