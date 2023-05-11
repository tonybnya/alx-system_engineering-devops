file { '/var/www/html/wp-content/cache':
    ensure => 'absent',
    recurse => true,
}

service { 'apache2':
    ensure => 'running',
    enable => true,
    require => File['/var/www/html/wp-content/cache'],
}
