git pull gitee master >> \excluded\git_process\CodeSync.log
read -p "Please Input Your Commit Message:" message
git commit -am message
gitee push gitee master >> \excluded\git_process\CodeSync.log