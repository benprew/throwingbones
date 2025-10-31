.PHONY: deploy

deploy:
	rsync -aiv --delete --exclude source/ --exclude *.md --exclude org/ --exclude Makefile --exclude .git --exclude *.sh --exclude blog_src/ --delete-excluded \
	. throwingbones@throwingbones.com:/var/www/html/throwingbones
