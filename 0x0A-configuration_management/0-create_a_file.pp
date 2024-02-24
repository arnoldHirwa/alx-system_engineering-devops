# A file for creating school file
file { 'school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  path => '/tmp/school',
}
