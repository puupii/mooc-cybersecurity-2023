
# 08 Hello Database

<p>You have a database with the following schema at your disposal.</p><div class="gatsby-highlight" data-language="sql"><pre class="language-sql"><code class="language-sql"><span class="token keyword">CREATE</span> <span class="token keyword">TABLE</span> Agent <span class="token punctuation">(</span>
    id <span class="token keyword">varchar</span><span class="token punctuation">(</span><span class="token number">9</span><span class="token punctuation">)</span> <span class="token keyword">PRIMARY</span> <span class="token keyword">KEY</span><span class="token punctuation">,</span>
    name <span class="token keyword">varchar</span><span class="token punctuation">(</span><span class="token number">200</span><span class="token punctuation">)</span>
<span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre></div><p>Write a program that outputs all the agents and their identifier codes from the database. The output format should be as follows:</p><div class="gatsby-highlight" data-language="rest"><pre class="language-rest"><code class="language-rest">agent_id agent_name
agent_id agent_name
...</code></pre></div><p>The output should be ordered by agent id.</p><p>You can create a test database with</p><div class="gatsby-highlight" data-language="shell"><pre class="language-shell"><code class="language-shell">python3 create_test_db.py</code></pre></div><p>in the src directory.</p><p>Once completed, return the assignment to the TMC server.</p>

---

