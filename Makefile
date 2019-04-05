deploy:
	rsync -aiv --delete . throwingbones@10.0.1.2:/var/www/html/throwingbones --exclude source/ --exclude *.md --exclude Makefile --delete-excluded
