# Puppet script to kill a running process

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
