# An algorithm is a piece of code that performs a task - manipulates data somehow

# --> heuristic

# brute force method? Hard coding? Meaning a way to get from pt A to B but maybe not the most efficient

# VC is saving every version of your code so that if you completely break it you can go back,
# different from saving in that saving overwrites the last version, VC maintains a copy at each commit

# Git - local command (on computer), github - remote (company, website)

# git log = show log of commits
# git init = initiate git for directory we are currently in
# git status = status of files in repo, up to date or no or staged
# git add = adds file(s) to stage for commit
# git commit = commits to memory, now saved as a version of code -a for all, -m for message w/commit
# git remote add = stages files to add to github w/correct url
# git remote -v = will tell you if remote repository exists
# git push = pushes to remote repo

# command line is important because it is how you can talk directly with the computer
# important to get into the nitty-gritty of what the compy is doing (memory is helpful)

# the prompt in the command line is where you currently are in the file system
# ex: ~/amandacameron/src specifies where I amandacameron

# ls = show me all the info in the current directory
# pwd = present working directory, where am i?
# cp = copy - must specify file, origin, and new place
# mv = move, must specify file, origin, and new place (can also use this to rename) (ex: mv sally/sally_tax.txt sales_reports/)
# cd = change directory, followed by where you'd like to go (.. = go up one directory)
# mkdir = make new directory, followed by title of directory, will get created in the directory you are in now
# rm = remove - can only remove empty directories unless you use the scary command with a minus and rf
# man = manual
# --help = will give you what you can do with that command
# ctrl-d = gets out of python, ctrl-c = stop stop stop!

# relative vs abs = relative can be in relation to where we are now whereas abs has to start at top of file tree to specify location

# parameters are placeholders in a function parens, arguments are what's eventually passed through when function is called

# return - for computers (captures value) exits function, break - get out of loop, print - for humans(only shows value, does not capture, does not exit function)

# if no return, fuction returns None

# default parameter is somthing you can assign if nothing is assigned when function is called.
# ex: def my_fuc(a, b=2) --> unless you assign another value to b when calling function, 2 will be used by default

# scope = where something is available! what is able to reference something. Function scope is only within scope
# so if the variable dog is only defined in my function it is not available to anything outside of the function. Can't reach into function

# important style considerations for python = spacing btw lines, docstrings are great, balancing
# succinct vs. explanitory, snake_case, functions are verby
# make names clear! variables/lists/whatever - make the name useful

# sorted() = gives us sorted copy of the list
# .sort() = modifies the list, sorts
# .append() = will add one item to list at end
# .extend() = can pass multiple items here to end of list
# list indexing = my_list[0]
# list slicing = my_list[start:stop(exclusive):step]
# loop over list with while or for loop
# for range(len(my_list)) do this thing, will iterate over each list object
# for thing in list, if thing == "other thing" count =+ 1
# for thing in list, print thing

# mutability refers to the place in memory - are we able to assign a new value?
# strings and tuples are immutable, dicts/lists/sets are mutable

# python mem is different than c mem because the variable name is actually not what it's keeping track of, just what it's pointing at
# python variables not classic sense, in c they're a fixed place in mem

# garbage collection - goes and looks for places in mem where nothing is pointing to it! Deletes if found

# id() function is able to give you the exact location in computer memory, while is checks identity

# sets are good for unique values - when you don't need duplicates, also order won't matter

# .add() = adds something to set
# len() = gets length of set
# .remove() = removes specific thing on set
# .pop() = consumes thing one by one, doesn't start at end like lists
# set_of_my_list = set([my_list]) OR set = {my_set}
# for word in set if word == "cat" print yeeehaw, else continue

# tuples = good for collections of data that are unlikely to change, and that order matters!
# ex: my_tuple = (name, month born, year born, day born)
# index a tuple the same way as a list, name = my_tuple[0], 'n' = my_tuple[0][0] (double indexing is sweet)



























