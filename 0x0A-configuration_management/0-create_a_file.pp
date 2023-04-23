# manifest to create file in tmp directory
file { '/tmp/School':
  ensure  => file,
  path    => '/tmp/School',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
