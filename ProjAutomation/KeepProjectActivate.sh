cd /home/pi/Projects/old_pi/Pi/
if [! -f "SongResult.txt"] then
    touch "SongResult.txt"
fi

mplayer ../musics/RunningHomeToYou.m4a >> SongResult.txt
