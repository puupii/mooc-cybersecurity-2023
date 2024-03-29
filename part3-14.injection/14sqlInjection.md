
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

