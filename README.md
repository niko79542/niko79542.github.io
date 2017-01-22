# to push content to github pages...

#!/bin/sh

pelican content -s publishconf.py
#to preview changes
#pelican content 

#push to dev
git add -A
git commit -m "push blog post"
git push origin dev

#import to master branch, push
ghp-import output -b master
git push origin master
