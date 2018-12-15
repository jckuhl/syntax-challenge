# SyntaxFM Challenge

Syntax hosts Scott Tolinski and Wes Bos talked in their 100th episode about a challenge to find out how long the duration of every episode is.  Wes then mentioned as a challenge, finding a programming solution that can caluclate the total duration of every episode and hasty treat.

This is my attempt.

I might have to do something different later.  The RSS feed only has 99 episodes for me to use.  If I can find a way to expand that to every episode, that would be better.

Currently, with 99 episodes, it is clocking in at 87 hours, 0 minutes and 13 seconds.

I did this in two ways.  First I tried to use different XML parsers to read the RSS feed in JavaScript.  Neither of those worked, I kept getting stonewalled by `[Object object]` objects that wouldn't parse, so I threw my hands up and tried a Python XML parser with better success.

But then I also had a thought about using RegEx (which I hate) and rewrote my javascript code to use RegEx.

Both scripts lead to the same output of 87:00:13 with the given data set.

I might however have to use Beautiful Soup or something to scrape the actual webpage since I can't seem to get more than 99 episodes from the RSS.