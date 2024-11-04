#!/bin/bash
#	$1 : directory name
#	$2 : number of times to repite
#	$3 : remove

if [ -f .env ]; then
	export $(cat .env | xargs)
fi

export OPENAI_API_KEY=$OPENAI_API_KEY



directory_name=$1
library_name=xpdf


if [ -n "$3" ]; then
	docker rm $(docker ps -qa)
	docker rmi $(docker image -q)
	docker system prune -a
	sudo rm -rf /tmp/*
	rm -rf ~/.local/share/Trash/files/*
fi

for ((var=1; var<=$2; var++));
do
	./run_all_experiments.py\
	--model='gpt-4o-mini'\
	-y ./benchmark-sets/all/${library_name}.yaml\
	--work-dir=results/${library_name}/${directory_name}$var

	python3.11 -m report.web -r results/${library_name}/${directory_name}$var -o outputs/${library_name}/${directory_name}$var
#	python3.11 -m http.server 2222 -d outputs/${library_name}/${directory_name}$var
done
