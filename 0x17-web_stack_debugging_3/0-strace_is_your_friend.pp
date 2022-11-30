# Fixing typing error in word press settings

exec { 'fix-wordpress':
  command => 'sed =i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

