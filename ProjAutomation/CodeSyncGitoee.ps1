git pull >> .\excluded\git_process\CodeSync.log
git commit -am '$args' >> .\excluded\git_process\CodeSync.log
git push gitee master >> .\excluded\git_process\CodeSync.log
git pull
git push