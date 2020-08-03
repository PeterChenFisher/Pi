dirname=excluded/git_process
echo "the dir name is $dirname"
if [ ! -d $dirname  ];then
  mkdir $dirname
else
  echo dir exist
fi

date >> excluded/git_process/ProjAuto.log
echo "Start Project Automation Script" >> excluded/git_process/ProjAuto.log
git pull>> excluded/git_process/ProjAuto.log
PID=$(ps -e|grep python | awk '{printf $1}')
echo "Main Script PID is: $PID" >> excluded/git_process/ProjAuto.log
sudo kill -9 ${PID} >> excluded/git_process/ProjAuto.log
if [ $? -eq 0 ];then
echo "kill $PID success" >> excluded/git_process/ProjAuto.log
    sudo bash ./main.sh
else
    echo "kill $PID fail" >> excluded/git_process/ProjAuto.log
fi
