# A GNU Makefile to build the docs

# Note: This makefile include remake-style target comments.
# These comments before the targets start with #:

.PHONY: mathics.pdf texdoc

all: mathics.pdf

#: Forward the call to latex, Whatever it is you want to do
%:
	$(MAKE) -C latex $@
