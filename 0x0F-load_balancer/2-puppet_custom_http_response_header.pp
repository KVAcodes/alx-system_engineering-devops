# configures a brand new ubuntu machine with the requirements of task 0 using puppet

file { '/0-custom_http_response_header':
  ensure  => present,
  content => "\
#!/usr/bin/env bash
# configures a brand new Ubuntu machine so that it's HTTP response contains a custom header.
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo 'Hello World!' > /var/www/html/index.nginx-debian.html
sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default
echo \"Ceci n'est pas une page\" > /usr/share/nginx/html/custom_404.html
sed -i '/server_name _;/a error_page 404 /custom_404.html;\nlocation = /custom_404.html {\nroot /usr/share/nginx/html;\ninternal;\n}' /etc/nginx/sites-available/default
sudo sed -i \"/listen 80 default_server;/a add_header X-Served-By $(hostname);\" /etc/nginx/sites-enabled/default
service nginx start
",
  mode    => '0755',
}

exec { 'run_the_script':
  command => '/0-custom_http_response_header',
}
