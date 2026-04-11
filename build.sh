pip install -r requirements.txt
mkdir -p $HOME/bin
curl -L https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v4.4.1/ffmpeg-4.4.1-linux-arm-64.zip -o ffmpeg.zip
unzip ffmpeg.zip -d $HOME/bin
rm ffmpeg.zip
export PATH=$HOME/bin:$PATH
