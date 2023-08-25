# This provisional script uses pip3 to install Flask 2.1.0

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
