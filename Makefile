.PHONY: deploy

deploy:
	rsync -aiv --delete --exclude source/ --exclude *.md --exclude Makefile --exclude .git --exclude *.sh --delete-excluded \
	. throwingbones@mail.throwingbones.com:/var/www/html/throwingbones
