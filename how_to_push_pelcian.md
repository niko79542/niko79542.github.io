# to preview changes

pelican content
cd output
python -m pelican.server

# to push content to github pages...

pelican content -s publishconf.py
pelican content # otherwise home page image doesn't show for some reason.


#push to dev
git add -A
git commit -m "push blog post"
git push origin dev

ghp-import output -b master
git commit --amend
git push origin master
