# Puppet script to configure the ssh configuration file

file { 'file_line':
  ensure => 'present'
  path   => '$HOME/.ssh/school'
  content => 'Host *\n    PasswordAuthentiction = no\nIdentityFile = ~/.ssh/school'
