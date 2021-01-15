cd /home/pi/Projects/Pi/
if [! -f "SongResult.txt"] then
    touch "SongResult.txt"
fi

mplayer ../musics/RunningHomeToYou.m4a >> SongResult.txt
