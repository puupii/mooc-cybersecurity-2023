<p>The same database schema from the previous assignment is at your disposal here.
Implement the functionality for adding and removing an agent to the database as well as reading them.
When reading the agents should be ordered by their ids.</p><p>The
application should function as follows (input from the user given in red):</p><div class="gatsby-highlight" data-language="rest"><pre class="language-rest"><code class="language-rest">Active agents:

Secret	Clank
Gecko	Gex
Robocod	James Pond
Fox	Sasha Nein

What would you like to do: [a]dd, [r]emove, or [q]uit? a

id? Riddle
name? Voldemort

Active agents:

Secret	Clank
Gecko	Gex
Robocod	James Pond
Fox	Sasha Nein
Riddle	Voldemort

What would you like to do: [a]dd, [r]emove, or [q]uit? q</code></pre></div><p>Now, when the application is started again, agent Voldemort is within the database and the details of a new agent is queried from the user.</p><div class="gatsby-highlight" data-language="rest"><pre class="language-rest"><code class="language-rest">Active agents:

Secret	Clank
Gecko	Gex
Robocod	James Pond
Fox	Sasha Nein
Riddle	Voldemort

What would you like to do: [a]dd, [r]emove, or [q]uit? a

id? Feather
name? Major Tickle

Active agents:

Secret	Clank
Gecko	Gex
Robocod	James Pond
Fox	Sasha Nein
Riddle	Voldemort
Feather	Major Tickle</code></pre></div><p>You can create a test database with</p><div class="gatsby-highlight" data-language="shell"><pre class="language-shell"><code class="language-shell">python3 create_test_db.py</code></pre></div><p>in the src directory.</p></div></div></div></div></div></div>
