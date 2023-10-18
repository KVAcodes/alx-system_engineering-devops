# Changes the Os configuration for the holberton user
# getting too many files open error due to low ulimit
# values set

exec { 'increase_hardfile_limit_for_holberton_user':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 8192/' etc/security/limits.conf",
  path    => '/usr/bin:/usr/sbin:/bin'
}

exec { 'increase_softfile_limit_for_holberton_user':
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 4096/' etc/security/limits.conf",
  path    => '/usr/bin:/usr/sbin:/bin'
}
