#!/usr/bin/env Rscript

files <- list.files(path="/Users/ChristinaShehata/Desktop/tree_blanks/", pattern="*.tre", full.names=T, recursive=FALSE)
lst <- vector("list", length(files))
names(lst) <- files

library(ape)

for (tree in files) {
	tree_read <- read.tree(tree)
	tree_read$node.label <- NULL
	write.tree(tree_read,file = paste(tree,".nbs"))}