---
title: Testing sessions with Sinatra
tags: sinatra
---
I've got a sinatra-based app that relies on sessions and I need to test them.  After doing a little digging, here was the solution I was able to come up with:
 1. Make sure that you're setting your RACK_ENV to 'test' ( I do this in my Rakefile )
 2. Disable sessions in your app when in test?
 3. when you make a request that requires a session, pass 'rack.session' =&gt; {} in the environment hash

See an example of this in my app:[Picklespears](http://github.com/benprew/picklespears "Picklespears Source")

Here's the breakdown of the code,

In the Rakefile:

    ENV['RACK_ENV']='test'

In the app (picklespears.rb)

    if test?
      set :sessions, false
    else
      set :sessions, true
    end

And finally, in the test itself (test/test_player.rb)

    post '/player/update', { :name => 'new_name' }, 'rack.session' => { :player_id => player.id }
