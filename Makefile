.PHONY: deploy

deploy:
	ssh throwingbones@throwingbones "cd /var/www/html/throwingbones && git pull"
