
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

