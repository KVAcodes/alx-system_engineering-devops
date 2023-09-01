# Installing and configuring an Nginx server using Puppet instead of Bash

package { 'nginx' :
  provider        => 'apt-get';
  install_options => ['-y'];
}
exec { 'ufw allow \'Nginx HTTP\'':
  provider => shell;
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present;
  content => 'Hello World!';
}

exec { 'sed -i \'/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\' /etc/nginx/sites-available/default':
  provider => shell;
}

exec { 'service nginx start':
  provider => shell;
}
