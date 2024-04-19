# Using Puppet, create a file school in /tmp
# that contains the word 'I love Puppet'
file { '/temp/school':
    ensure  => present,
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love puppet',
}
