# Postmortem: The Case of the Mysterious `.phpp` File

In the early hours of the morning, as the sun rose over Rwanda, ALX's System Engineering & DevOps project 0x19 encountered a hiccup. Our Apache web server, nestled in its Ubuntu 14.04 container, decided to throw a party of 500 Internal Server Errors instead of serving our simple Holberton WordPress site. Here's how we cracked the case:

## The Investigation

Our bug buster, Hirwa (codename: arnoldhirwa), leaped into action around 19:20 PST to tackle the issue head-on.

1. **Process Check**: Started with a `ps aux` to check running processes. Both `apache2` processes (`root` and `www-data`) seemed fine.

2. **Directory Dive**: Checked `/etc/apache2/sites-available` and confirmed the server was looking at `/var/www/html/` for content.

3. **Strace the Apache**: Ran `strace` on the `root` Apache process while curling the server in another terminal. Sadly, `strace` was feeling shy and gave no useful info.

4. **Strace Again**: This time on the `www-data` process. Jackpot! Discovered an `-1 ENOENT (No such file or directory)` error when trying to access `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. **File Hunt**: Scanned files in `/var/www/html/` with Vim pattern matching. Found the culprit in `wp-settings.php` (Line 137, `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).

6. **Typo Terminator**: Removed the sneaky `p` from the file extension.

7. **Test and Triumph**: Curled the server again. A perfect 200!

8. **Automate the Fix**: Wrote a Puppet manifest to ensure this typo never haunts us again.

## Lessons Learned

In the end, it was a simple typo. The WordPress app was stumbling over `class-wp-locale.phpp` when it should have been looking for `class-wp-locale.php` in the `wp-content` directory.

To avoid such hiccups in the future:

* **Test, Test, Test**: Always test the application before deploying.

* **Monitoring Matters**: Set up uptime monitoring (e.g., [UptimeRobot](https://uptimerobot.com/)) to catch issues early.

In response to this incident, I crafted a Puppet manifest ([0-strace_is_your_friend.pp](https://github.com/arnoldHirwa/alx-system_engineering-devops/blob/main/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp)) to automate fixing similar errors. But hey, we're all human (even us programmers), so let's laugh it off and remember: we never make mistakes... right? 😉
