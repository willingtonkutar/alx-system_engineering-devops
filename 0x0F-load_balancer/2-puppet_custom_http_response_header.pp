# Ensure nginx is installed and running
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

# Configure the default nginx site with the custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure the template directory exists
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates':
  ensure => directory,
}

# Create the template for the nginx default site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @(EOF)
<%
# Get the hostname of the server
hostname = @facts['networking']['hostname']
%>
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
        add_header X-Served-By <%= hostname %>;
    }
}
  EOF
}
