# Define the path to the file
$file_path = '/var/www/html/index.html'
$content = 'Hello world'

# Exec resource to create the file if it does not exist or is empty
exec { 'create_file_if_empty_or_nonexistent':
  command => "/bin/bash -c 'if [ ! -s ${file_path} ]; then echo \"${content}\" > ${file_path}; fi'",
  path    => ['/bin', '/usr/bin'],
  creates => $file_path,
}

# File resource to manage file properties
file { $file_path:
  ensure  => 'file',
  mode    => '0644',
  # This will ensure the file properties are correct, but will not overwrite content if the file already exists
  require => Exec['create_file_if_empty_or_nonexistent'],
}
