# Set open file limit UNLIMIT to 4096
exec { 'set_UNLIMIT':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/sbin/', '/usr/bin/']
}
