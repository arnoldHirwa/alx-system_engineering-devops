#!/usr/bin/pup
# A file to install flask using Puppet

package { 'flask',
    ensure => '2.1.0',
    provider => 'pip3',
}
