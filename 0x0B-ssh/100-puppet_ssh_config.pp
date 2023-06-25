# Puppet script to configure the ssh configuration file

file_line { 'no_passwd':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'Host *\n    PasswordAuthentication = no'
}

file_line { 'private_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile = ~/.ssh/school'
}
