#-- ========== NGINX : install and compile
wget ftp://ftp.pcre.org/pub/pcre//pcre-8.43.tar.gz
wget http://zlib.net/zlib-1.2.11.tar.gz
wget http://www.openssl.org/source/openssl-1.1.1d.tar.gz
tar -zxf pcre-8.43.tar.gz
tar -zxf zlib-1.2.11.tar.gz
tar -zxf openssl-1.1.1d.tar.gz
wget https://nginx.org/download/nginx-1.17.6.tar.gz
tar zxf nginx-1.17.6.tar.gz
cd nginx-1.17.6


./configure --with-pcre=../pcre-8.43 --with-openssl=../openssl-1.1.1d --with-zlib=../zlib-1.2.11 --prefix=/opt/nginx --sbin-path=/opt/nginx/sbin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock



./configure
--with-pcre=../pcre-8.43
--with-openssl=../openssl-1.1.1d
--with-zlib=../zlib-1.2.11
--prefix=/opt/nginx
--sbin-path=/opt/nginx/sbin/nginx
--conf-path=/etc/nginx/nginx.conf
--error-log-path=/var/log/nginx/error.log
--pid-path=/var/run/nginx.pid
--lock-path=/var/run/nginx.lock
make
sudo make install
cd /opt/nginx/sbin
sudo ./nginx -v && sudo ./nginx -V

sudo vim /etc/systemd/system/nginx.service

    [Unit]
    Description=A high performance web server and a reverse proxy server
    After=network.target

    [Service]
    Type=forking
    PIDFile=/run/nginx.pid
    ExecStartPre=/opt/nginx/sbin/nginx -t -q -g 'daemon on; master_process on;'
    ExecStart=/opt/nginx/sbin/nginx -g 'daemon on; master_process on;'
    ExecReload=/opt/nginx/sbin/nginx -g 'daemon on; master_process on;' -s reload
    ExecStop=-/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid
    TimeoutStopSec=5
    KillMode=mixed

    [Install]
    WantedBy=multi-user.target

# check
sudo systemctl start nginx.service && sudo systemctl enable nginx.service
sudo systemctl is-enabled nginx.service
sudo systemctl status nginx.service
ps aux | grep nginx
curl -I 127.0.0.1

# creation utilisateur et groupe NGINX
sudo adduser --system --home /nonexistent --shell /bin/false --no-create-home --disabled-login --disabled-password --gecos "nginx user" --group nginx

sudo mkdir -p /var/cache/nginx/client_temp /var/cache/nginx/fastcgi_temp /var/cache/nginx/proxy_temp /var/cache/nginx/scgi_temp /var/cache/nginx/uwsgi_temp
sudo chmod 700 /var/cache/nginx/*
sudo chown nginx:root /var/cache/nginx/*
