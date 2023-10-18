# Increase the ulimit for the nginx server initially set to 15
# causing the too many files open bug as 15 file descriptors aren't
# enough to handle that many request

exec { 'fix ulimit':
  command => 'bash -c "sed -i s/15/4096/ /etc/default/nginx; service nginx restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
