# Puppet script to install the python Flask package

package { 'flask':
  ensure   => 'installed',
  name     => 'flask',
  provider => 'pip3'
}
