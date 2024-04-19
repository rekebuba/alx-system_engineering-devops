# Using Puppet, install flask from pip3
# Version must be 2.1.0
exec { 'pip3-install':
    command     => 'pip3 install Flask==2.1.0',
    refreshonly => true,
}
