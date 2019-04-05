obj = $(src:.md=.html)

blog: $(obj)
	pandoc -s -c tufte.css foo.md -o foo.html
