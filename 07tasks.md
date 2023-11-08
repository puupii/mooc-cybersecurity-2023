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
</ul></div></div></div></div></div></div>
