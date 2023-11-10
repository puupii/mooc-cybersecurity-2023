

https://cybersecuritybase.mooc.fi/

---

# 01 PortScanner

<p>In this assignment, you will gain some hands-on experience on working with
ports in Python and familiarize yourself with the tools used for some of the
programming tasks in this course.</p><p>The assignment template that you can retrieve either using Test My Code, or the
Test My Code web site contains the following code in portscanner.py.</p><div class="gatsby-highlight" data-language="python"><pre class="language-python"><code class="language-python"><span class="token comment">#!/usr/bin/env python3</span>
<span class="token keyword">import</span> sys
<span class="token keyword">import</span> socket


<span class="token keyword">def</span> <span class="token function">get_accessible_ports</span><span class="token punctuation">(</span>address<span class="token punctuation">,</span> min_port<span class="token punctuation">,</span> max_port<span class="token punctuation">)</span><span class="token punctuation">:</span>
    found_ports <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>

    # write code here

    return found_ports


<span class="token keyword">def</span> <span class="token function">main</span><span class="token punctuation">(</span>argv<span class="token punctuation">)</span><span class="token punctuation">:</span>
    address <span class="token operator">=</span> sys<span class="token punctuation">.</span>argv<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span>
    min_port <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>sys<span class="token punctuation">.</span>argv<span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
    max_port <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>sys<span class="token punctuation">.</span>argv<span class="token punctuation">[</span><span class="token number">3</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
    ports <span class="token operator">=</span> get_accessible_ports<span class="token punctuation">(</span>address<span class="token punctuation">,</span> min_port<span class="token punctuation">,</span> max_port<span class="token punctuation">)</span>
    <span class="token keyword">for</span> p <span class="token keyword">in</span> ports<span class="token punctuation">:</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span>p<span class="token punctuation">)</span>

<span class="token comment"># This makes sure the main function is not called immediatedly</span>
<span class="token comment"># when TMC imports this module</span>
<span class="token keyword">if</span> __name__ <span class="token operator">==</span> <span class="token string">"__main__"</span><span class="token punctuation">:</span>
    <span class="token keyword">if</span> <span class="token builtin">len</span><span class="token punctuation">(</span>sys<span class="token punctuation">.</span>argv<span class="token punctuation">)</span> <span class="token operator">!=</span> <span class="token number">4</span><span class="token punctuation">:</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'usage: python %s address min_port max_port'</span> <span class="token operator">%</span> sys<span class="token punctuation">.</span>argv<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
    <span class="token keyword">else</span><span class="token punctuation">:</span>
        main<span class="token punctuation">(</span>sys<span class="token punctuation">.</span>argv<span class="token punctuation">)</span></code></pre></div><p>For this assignment, you should write the code needed for the method
<code class="language-text">get_accessible_ports</code> to scan the given range of ports. The method
should scan the ports at a given address, and then return the list of ports
that have a service listening for them.</p><p>Note that the test server will not submit any data; you shouldn't try to
receive any data.</p><p>Once completed, submit your solution to the TMC server for assessment.</p><p>Note that while we implement port scanners and other tools, we will later also
look into existing software that have similar functionality.</p>

---


# 02 Hello Web

<p>In this assignment, you will familiarize yourself with the very basic
functionality of the web framework.</p><p>Change the provided application so that the output is "Hello Web!".</p><p>Once finished, submit the assignment to the TMC server.</p>

---


# 03 Calculator

<p>In this assignment, you will familiarize yourself with handling (1) requests to
several paths and (2) request parameters. Implement the following functionality
in <code class="language-text">src/pages/views.py</code>.</p><ul>
<li>A request to the path <code class="language-text">add/</code> sums the values in the request GET parameters
<code class="language-text">first</code> and <code class="language-text">second</code> together and returns the response to the user. Note that
the parameters are integers and should also be treated as such.</li>
<li>A request to the path <code class="language-text">multiply/</code> multiplies the values in the request GET
parameters <code class="language-text">first</code> and <code class="language-text">second</code> and returns the response to the user. Note
that the parameters are numbers and should also be treated as such.</li>
</ul><p>For example, <code class="language-text">add/?first=10&amp;second=10</code> should result in <code class="language-text">20</code>.</p><p>Once finished, submit the assignment to the TMC server.</p>

---


# 04 Templates

<p>Next, we will look into returning content created using a template. Implement
the following functionality in <code class="language-text">views.py</code>:</p><ul>
<li>A request to the path <code class="language-text">/</code> will return a response based on the template <code class="language-text">pages/index.html</code>.</li>
<li>A request to the path <code class="language-text">/video</code> will return a response based on the template <code class="language-text">pages/video.html</code>.</li>
</ul><p>Once finished, submit the assignment to the TMC server.</p>

---


# 05 Hello List

<p>In this assignment we will look into using lists and using them as data for the
templates.</p><p>The assignment has the server side functionality that handles a request to the
root path and adds a list for the template to process. The template that is
used to create the site is missing some functionality however.</p><p>Your task is to (1) print the values in the list between <code class="language-text">&lt;ul&gt;</code> and <code class="language-text">&lt;/ul&gt;</code> tags, and (2) add a form that can
be used to send content to the server.</p><p>Once finished, submit the assignment to the TMC server.</p>

---


# 06 Notebook

<p>Implement a notebook application in <code class="language-text">views.py</code>
and the template <code class="language-text">index.html</code>. The notebook application
should list the existing notes, allow adding new notes, and erasing notes (see <code class="language-text">urls.py</code> for the mapping but do not change it). If there are more
than 10 notes, the application should only keep the ten most recent ones.</p><p>The test assumes that the text input field containing the note is named <code class="language-text">content</code>.</p><p>To run the server, you will most likely need to initialize the database so that session can be maintained.
This can be done with</p><div class="gatsby-highlight" data-language="shell"><pre class="language-shell"><code class="language-shell">python3 manage.py migrate</code></pre></div><p>NB! Be wary that <code class="language-text">items = request.session.get('items', [])</code> doesn't create a new list in session if one doesn't exist,
it will simply initializes <code class="language-text">items</code> to <code class="language-text">[]</code>. Moreover, for example, <code class="language-text">items = []</code> will not update the list in sessions.
It will only set the <code class="language-text">items</code> to point to <code class="language-text">[]</code>.
Consequently, in certain cases, you have to update the actual list explicitly for example with <code class="language-text">request.session['items'] = items</code>.</p><p>Once finished, submit the assignment to the TMC server.</p>

---


# 07 Tasks

<p>The assignment template has some functionality for adding tasks. Your task is
to alter the loadTasks function so that the existing tasks are loaded when the
page is shown to the user. Do this using Javascript and the server <code class="language-text">tasks</code> service.</p><p>If you wish an additional challenge, add the functionality to remove tasks as well.</p><p>The automated test relies on using selenium with chromedriver and chrome, make
sure that you have installed them properly, see
<a href="/installation-guide">instructions</a>, otherwise you cannot do local
tests.</p><p>Hints:</p><ul>
<li>Do not use absolute URLs, the automated test will start its own server at its own port.</li>
<li>Javascript <a href="https://thecodebarbarian.com/for-vs-for-each-vs-for-in-vs-for-of-in-javascript" target="_blank" rel="noopener noreferrer">for-loop</a> syntax.</li>
<li>The <code class="language-text">tasks</code> service returns you a string that needs to be parsed into a JSON object. The JSON object
will have a field named <code class="language-text">tasks</code> containing the list of tasks.</li>
</ul>

---


# 08 Hello Database

<p>You have a database with the following schema at your disposal.</p><div class="gatsby-highlight" data-language="sql"><pre class="language-sql"><code class="language-sql"><span class="token keyword">CREATE</span> <span class="token keyword">TABLE</span> Agent <span class="token punctuation">(</span>
    id <span class="token keyword">varchar</span><span class="token punctuation">(</span><span class="token number">9</span><span class="token punctuation">)</span> <span class="token keyword">PRIMARY</span> <span class="token keyword">KEY</span><span class="token punctuation">,</span>
    name <span class="token keyword">varchar</span><span class="token punctuation">(</span><span class="token number">200</span><span class="token punctuation">)</span>
<span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre></div><p>Write a program that outputs all the agents and their identifier codes from the database. The output format should be as follows:</p><div class="gatsby-highlight" data-language="rest"><pre class="language-rest"><code class="language-rest">agent_id agent_name
agent_id agent_name
...</code></pre></div><p>The output should be ordered by agent id.</p><p>You can create a test database with</p><div class="gatsby-highlight" data-language="shell"><pre class="language-shell"><code class="language-shell">python3 create_test_db.py</code></pre></div><p>in the src directory.</p><p>Once completed, return the assignment to the TMC server.</p>

---


# 09 Hello Insert

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
Feather	Major Tickle</code></pre></div><p>You can create a test database with</p><div class="gatsby-highlight" data-language="shell"><pre class="language-shell"><code class="language-shell">python3 create_test_db.py</code></pre></div><p>in the src directory.</p>

---


# 10 Hello Web With Database

<p>The assignment template contains an application that always returns the message
"Hello Web!" to the user. Change the implementation so that the message content
is selected from the messages in the database. The id of the message is given
as a GET parameter <code class="language-text">id</code>. The database has 3 messages with ids 1, 42, and 99.</p><p>Hint: see how to query with <a href="https://docs.djangoproject.com/en/3.0/topics/db/queries/#the-pk-lookup-shortcut" target="_blank" rel="noopener noreferrer">primary keys</a>.</p><p>Once finished, return your solution to TMC.</p>

---


# 11 Banktransfer

<p>The assignment template has a simple application for managing accounts and
transfers. There is, however, small things to be fixed in the transfer
functionality. Think about the fixes that are needed, perform them, and return
the assignment to the TMC server.</p><p>The automatic test for atomic operation here is quite conservative. Make sure
that during the transfer view, there are no other SQL commands before the
atomic portion. Also, use only one atomic section.</p>

---


# 12 Simple Banking

<p>The assignment template has the entities for managing accounts and clients, but
it is incomplete. Modify the application so that addition and listing
the accounts actually works.</p><p>The web server has 3 users with the following passwords:</p><ul>
<li>admin:admin</li>
<li>bob:squarepants</li>
<li>alice:redqueen</li>
</ul><p>The logged user can be found in <code class="language-text">request.user</code>.</p><p>When the application works as intended, return it to TMC.</p>

---


# 13 Session Hijack

<p>The assignment contains a very simple bank application with 3 normal users</p><ul>
<li>bob:squarepants</li>
<li>alice:redqueen</li>
<li>patrick:asteroid</li>
</ul><p>The application has a predictable session id generation.
Figure out the formula and obtain Alice's balance by guessing Alice's session id (assuming she is logged in).</p><p>Hints:</p><ul>
<li>Note that the server code is now in <code class="language-text">server/</code> directory. Do not modify the server, instead modify the session sniffer in <code class="language-text">src/</code> folder.</li>
<li>The server has a <code class="language-text">/balance/</code> web page that provides the balance in JSON format for the logged in user. Note that this web page is not included in the
<code class="language-text">address</code> parameter when the sniffer is called by the automated test, that is, the <code class="language-text">address</code> will have a form of <code class="language-text">domain:port</code>.</li>
<li>To test your code, log in as Alice in a browser, and only then try to guess the session id with the session sniffer.</li>
<li>You should be able to figure out the session id formula by studying the <a href="https://developers.google.com/web/tools/chrome-devtools/storage/cookies" target="_blank" rel="noopener noreferrer">cookies</a>.</li>
<li>During automated tests, the counter in the session id will be a small random number (between 1 and 11). The sniffer should do multiple guesses to find Alice.</li>
<li>Use Python library <a href="https://www.w3schools.com/python/ref_requests_get.asp" target="_blank" rel="noopener noreferrer">requests</a>.</li>
<li>Note that <code class="language-text">json.loads</code> does not work with byte streams when using Python 3.5. </li>
<li>The session id for Django web servers is stored in a cookie named <code class="language-text">sessionid</code>.</li>
</ul>

---


# 14 SQL Injection

<p>Python SQLite API provides two main methods for executing commands, <code class="language-text">execute</code> and <code class="language-text">executescript</code>.
The latter along with the unsanitized data allows you to escape the current command, and tricks like
<code class="language-text">DROP TABLES</code> become possible. However, with <code class="language-text">execute</code> you can execute only <em>one</em> command. That is, you cannot escape the current command but you can still do
significant damage.</p><p>The exercise contains a database with the schema</p><div class="gatsby-highlight" data-language="sql"><pre class="language-sql"><code class="language-sql"><span class="token keyword">CREATE</span> <span class="token keyword">TABLE</span> Users <span class="token punctuation">(</span>name <span class="token keyword">TEXT</span><span class="token punctuation">,</span> password <span class="token keyword">TEXT</span><span class="token punctuation">,</span> admin <span class="token keyword">BOOL</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">CREATE</span> <span class="token keyword">TABLE</span> Tasks <span class="token punctuation">(</span>name <span class="token keyword">TEXT</span><span class="token punctuation">,</span> body <span class="token keyword">TEXT</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre></div><p>You can create a test database with</p><div class="gatsby-highlight" data-language="shell"><pre class="language-shell"><code class="language-shell">python3 create_test_db.py</code></pre></div><p>in the src directory.</p><p>The exercise performs a single unsafe query</p><div class="gatsby-highlight" data-language="python"><pre class="language-python"><code class="language-python"><span class="token string">"SELECT body FROM Tasks WHERE name='%s' and body LIKE '%%%s%%'"</span> <span class="token operator">%</span> <span class="token punctuation">(</span>username<span class="token punctuation">,</span> query<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span></code></pre></div><p>Complete <code class="language-text">query</code> that finds the admin password stored in Users table. The result should contain only one entry containing the admin password.</p><p>Hints:</p><ul>
<li>If <code class="language-text">injection.py</code> contains an <code class="language-text">Oracle</code> class, then you have outdated exercise. In that case, update the exercise. You may have to do the update manually by downloading the zip file
from the TMC server with a browser.</li>
<li>You can assume that there is only one admin, marked with <code class="language-text">admin = 1</code></li>
<li>See <a href="https://www.w3schools.com/sql/sql_injection.asp" target="_blank" rel="noopener noreferrer">here</a> for various examples of SQL injections</li>
<li>See UNIONs</li>
</ul>

---


# 15 Hiha Upload

<p>The assignment template contains the functionality for uploading and storing
personal files on a web server. The files uploaded by an individual should not
be accessible by anyone else. However, there seems to be a few flaws in how
this has been implemented. Fix the application so that everyone can access only
the files that they have uploaded (unauthorized actions should redirect to <code class="language-text">/</code>).</p><p>The application has the following username and password combinations for testing:</p><ul>
<li>alice:redqueen</li>
<li>bob:squarepants</li>
</ul>

---


# 16 Cross Site Scripting

<p>The exercise contains a simple direct message application, where messages are
not properly sanitized. This allows to send messages containing HTML code, and Javascript code.
Write a message that–when viewed by the victim in the application–will steal the victim cookie.
Write the message in <code class="language-text">src/msg.html</code>.
The test will simulate the heist by sending the message in <code class="language-text">src/msg.html</code>
to the victim and have the victim view the message. </p><p>To steal the cookie, use Javascript to send the cookie to <code class="language-text">mail/</code> on the same server.
Note that in the real world this can be <em>any</em>  server but for
automatic testing we added the <code class="language-text">mail/</code> service to the same server to simulate the heist.</p><p>Use POST request to submit the cookie.
The request body to <code class="language-text">mail/</code> should be a JSON object with a field <code class="language-text">content</code> containing the victim's cookie as a string.</p><p>The application has the following username and password combinations for testing:</p><ul>
<li>alice:redqueen</li>
<li>bob:squarepants</li>
</ul><p>Hints:</p><ul>
<li>Look into Tasks exercise (addTask function) on how to do Javascript POST requests with JSON as request body.</li>
<li>For debugging purposes, the server will print to the console any mail obtained through <code class="language-text">mail/</code> request.</li>
<li>When using POST make sure that you include <code class="language-text">/</code> in <code class="language-text">mail/</code>.</li>
<li>In certain situations you may get <code class="language-text">Message: unknown error: DevToolsActivePort file doesn't exist</code> when running <code class="language-text">tmc test</code>.
This means that your chrome installation is a bit wonky, what often helps is commenting out
the line <code class="language-text">options.add_argument('--user-data-dir=test/chrome_user_data')</code>
in <code class="language-text">test/test_xss.py</code>.</li>
</ul>

---


# 17 Safety

<p>Python package <code class="language-text">safety</code> can be used to find installed vulnerable packages.
The package relies on another package <code class="language-text">safety-db</code> which is simply a curated
JSON file of known vulnerable python modules.</p><p>In this assignment, the goal is to write a simple query system that given
the safety-db json file and a package name returns a list of all vulnerabilities
associated with that package. </p><p>The output should contain a list of tuples</p><div class="gatsby-highlight" data-language="python"><pre class="language-python"><code class="language-python"><span class="token punctuation">[</span><span class="token punctuation">(</span>id1<span class="token punctuation">,</span> version1<span class="token punctuation">,</span> cveid1<span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">(</span>id2<span class="token punctuation">,</span> version2<span class="token punctuation">,</span> cveid2<span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span></code></pre></div><p>During the writing of this exercise the <code class="language-text">safety-db</code> package was quite broken,
so instead of installing <code class="language-text">safety-db</code>, you should download the json file <code class="language-text">insecure_full.json</code> directly
from <a href="https://github.com/pyupio/safety-db/tree/master/data" target="_blank" rel="noopener noreferrer">here</a>.</p>

---


# 18 CSRF

<p>Python package <code class="language-text">safety</code> can be used to find installed vulnerable packages.
The package relies on another package <code class="language-text">safety-db</code> which is simply a curated
JSON file of known vulnerable python modules.</p><p>In this assignment, the goal is to write a simple query system that given
the safety-db json file and a package name returns a list of all vulnerabilities
associated with that package. </p><p>The output should contain a list of tuples</p><div class="gatsby-highlight" data-language="python"><pre class="language-python"><code class="language-python"><span class="token punctuation">[</span><span class="token punctuation">(</span>id1<span class="token punctuation">,</span> version1<span class="token punctuation">,</span> cveid1<span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">(</span>id2<span class="token punctuation">,</span> version2<span class="token punctuation">,</span> cveid2<span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span></code></pre></div><p>During the writing of this exercise the <code class="language-text">safety-db</code> package was quite broken,
so instead of installing <code class="language-text">safety-db</code>, you should download the json file <code class="language-text">insecure_full.json</code> directly
from <a href="https://github.com/pyupio/safety-db/tree/master/data" target="_blank" rel="noopener noreferrer">here</a>.</p>

---


# 19 Password

<p>The assignment template contains a small web application that needs to be hacked.</p><p>Your "friend" forgot his admin password, and you need to "retrieve it".
The account username is admin and since your friend isn't the sharpest tool
in the shed, you suspect that he uses a popular password. The candidate
passwords are listed in <code class="language-text">candidates.txt</code>
and the list is taken from
<a href="https://github.com/danielmiessler/SecLists/tree/master/Passwords" target="_blank" rel="noopener noreferrer">https://github.com/danielmiessler/SecLists/tree/master/Passwords</a>.</p><p>To access the admin panel go to <code class="language-text">http://localhost:8000/admin/login/?next=/admin/</code>
once you have fired up the server.</p><p>Use <code class="language-text">requests.Session()</code> to probe the server (otherwise a certain cookie is not transmitted).
You will also need to deal with csrf token.  Use the provided helper function to extract the token.
The template also provides a function to check whether the login was successful.</p><p>Do not forget to submit <em>all</em> the relevant login form fields.</p><p>For debugging purposes, you can change the admin password with</p><div class="gatsby-highlight" data-language="shell"><pre class="language-shell"><code class="language-shell">python3 manage.py changepassword admin</code></pre></div><p>and get the original password back by deleting the database <code class="language-text">db.sqlite</code>.</p><p>The automated test uses a random admin password. The <code class="language-text">address</code> parameter sent by the automated test
does not have the <code class="language-text">/admin/...</code> part, that is, the <code class="language-text">address</code> will have a form of <code class="language-text">domain:port</code>.
The <code class="language-text">candidates</code> parameter is a list of strings.</p>

---


# 20 Missconfiguration

<p>The assignment template contains a variant of the
banking application used in the previous exercise. </p><p>Go over the code and fix the security issues.</p><p>The users are</p><ul>
<li>bob:squarepants</li>
<li>alice:redqueen</li>
<li>patrick:asteroid</li>
</ul><p>Once you believe that you have solved the issue(s), return your solution to
TMC.</p>

---


# 21 Who Wants to be a Millionaire 
<p>The assignment template contains the core elements of the "Who wants to be a
millionaire?"-game. In this template,
you can observe that the link that is used to input details after finishing the
game can be accessed by anyone — although it should be hidden,
moreover user can go back and change the topic midway.</p><p>Fix these issues Do not change the address scheme though, but do it in the
business logic of the application.</p><p>Once you believe that you have solved the issue(s), return your solution to
TMC.</p>

---


