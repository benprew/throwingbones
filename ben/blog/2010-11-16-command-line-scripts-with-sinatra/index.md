---
title: Command line scripts with Sinatra
tags: sinatra
---
There are times when I want to do batch processing or perform other
command line activities that don't fit well into the
web-framework. The trouble is, my db connection info is based on what
"environement" I'm working in. I could re-create the hooks to set that
environment, but I'd rather leverage the existing capabilities in
Sinatra to do so.  That way if they change how it works in the future,
I don't have to work through all that again.

In Sinatra, there's a Delegator module that handles passing requests
for methods like 'production?' or 'set' off to the App. With that in
mind, I can easily just include the Delegator and let it handle
everything from there.

Here a sample of my code:

    require 'rubygems'
    require 'optparse'
    require 'sinatra/base'

    include Sinatra::Delegator
    options = {}
    OptionParser.new do |op|
        op.on('-e env') { |val| set :environment, val.to_sym }
    end.parse!

You can see this on my github page as well: [match_xtns.rb](https://github.com/benprew/mtg/blob/master/bin/match_xtns.rb)
