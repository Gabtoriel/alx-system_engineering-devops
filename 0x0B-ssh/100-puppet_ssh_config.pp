# Puppet script to configure the ssh configuration file

file_line { 'no_passwd':
  ensure => 'present',
  path   => '/home/viclins_t/.ssh_config',
  line   => 'PasswordAuthentication = no'
}

file_line { 'private_key':
  ensure => 'present',
  path   => '/home/viclins_t/.ssh/ssh_config',
  line   => 'IdentityFile = ~/.ssh/school'
}
