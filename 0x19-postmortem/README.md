# Incident report for the web stack debugging #3 project

## The Typo Nightmare :grimacing:


###  Timeline (all West African Time)
5.20 PM: The Configuration push was done.
5.22 PM: The Datadog monitoring service alerted me of a 500 error responses being returned to clients via pagerduty.
5:29 PM: The Debugging process begun.
6:12 PM: The issue was found.
6:13 PM: The Configuration files were edited and pushed
6:13 PM: Upon testing 100% of traffic was back online.

### Root Cause

At 5:20 PM WAT, a configuration change was done by one of the site maintenance crew and was  inadvertently released to our production environment without first been properly tested. The change occurred on the editing of one of the many configuration files presented on the server. The error resulted from a typo error of a resource name resulting in invalid system calls made the apache2 background parent process try to find a resource that isn’t present in the server’s file system. All incoming traffic was then met with this issue and greeted with the 500 error.

### Resolution and recovery

At 5:29 PM WAT, with the fact provided by Datadog that the site was returning 500 error responses I used the strace debugging tool and attached it to the apache2 parent process to view the system calls it made that resulted in the error and voila I found a call to a file name with a .phpp file extension instead of the .php file extension native to php scripts and this system resulted in a 500 resource not found error. All these without doubt indicated that a typo error had been made in the configuration environment, and a simple configuration debug wouldn’t fish it out. So after carefully look around in the config files hierarchy I was able to pinpoint the file in which a typo was made and fixed it promptly.

### Corrective and preventative measures

This issue was as a result of the absence of a proper software deployment protocol and procedure within the team, as any changes in the production environment first be properly tested before pushed. So a meeting was held with the involved parties and they were properly educated on the right steps to follow before deploying code the production branch.

Note that in response to this error, I wrote a Puppet manifest `0-strace_is_your_friend.pp` to automate fixing of any such identitical errors should they occur in the future. The manifest replaces any phpp extensions in the file `/var/www/html/wp-settings.php` with `php`.

But of course, it will never occur again, because we're programmers, and we never make errors! :innocent:
