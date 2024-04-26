# creates a file in the /tmp directory
file { '/tmp/school':
ensure  => 'file',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
<<<<<<< HEAD
}
=======
}
>>>>>>> 63ec1623b7f12fdf89ae432f239790bb3ab93fcd