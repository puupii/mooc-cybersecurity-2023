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
</ul></div></div></div></div></div></div>
