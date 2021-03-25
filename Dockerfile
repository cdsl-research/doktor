FROM centos:7

#IUSリポジトリを追加
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
#Python3.5をインストール
RUN yum install -y python35u python35u-libs python35u-devel python35u-pip
#Pythonのライブラリrequestsをpip
RUN python3.5 -m pip install requests
#PythonのライブラリFlaskをpip
RUN python3.5 -m pip install flask

COPY web /var/www/html/web/

#コンテナ起動時にFlaskサーバを立ち上げ
CMD ["python3.5", "/var/www/html/web/main.py"]