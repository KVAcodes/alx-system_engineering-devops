# 0x05. Processes and signals

### AUTHOR :open_book:
Kadiri Victor.

## TASKS.

### MANDATORY.
#### [0 - what-is-my-pid]()
#####	Write a Bash script that displays its own PID.

#### [1 - list_your_processes]()
#####	Write a Bash script that displays a list of currently running processes.	
* Must show all processes, for all users, including those which might not have a TTY
* Display in a user-oriented format
* Show process hierarchy

#### [2 - show_your_bash_pid]()
#####	Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
You cannot use `pgrep`
The third line of your script must be `# shellcheck disable=SC2009` (for more info about ignoring `shellcheck` error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))

#### [3 - show_your_bash_pid_made_easy]()
#####	Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

* You cannot use `ps`

#### [4 - to_infinity_and_beyond]()
#####	Write a Bash script that displays `To infinity and beyond` indefinitely.	
In between each iteration of the loop, add a `sleep 2`

#### [5 - dont_stop_me_now]()
#####	We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.
##### Write a Bash script that stops `4-to_infinity_and_beyond` process.

#### [6 - stop_me_if_you_can]()
#####	a Bash script that stops `4-to_infinity_and_beyond` process without using `kill` or `killall`.

#### [7 - highlander]()
#####	Write a Bash script that displays:

* `To infinity and beyond` indefinitely
* With a `sleep 2` in between each iteration
* `I am invincible!!!` when receiving a `SIGTERM` signal
Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond one`.

#### [8 - beheaded_process]()
#####	 a Bash script that kills the process `7-highlander`.

### ADVANCED
#### [100 - process_and_pid_file]()
#####	Write a Bash script that:
Creates the file `/var/run/myscript.pid` containing its PID
Displays `To infinity and beyond` indefinitely
Displays `I hate the kill command` when receiving a SIGTERM signal
Displays `Y U no love me?!` when receiving a SIGINT signal
Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

#### []()
#####	

#### []()
#####
