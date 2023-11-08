
# 18 CSRF

<p>Python package <code class="language-text">safety</code> can be used to find installed vulnerable packages.
The package relies on another package <code class="language-text">safety-db</code> which is simply a curated
JSON file of known vulnerable python modules.</p><p>In this assignment, the goal is to write a simple query system that given
the safety-db json file and a package name returns a list of all vulnerabilities
associated with that package. </p><p>The output should contain a list of tuples</p><div class="gatsby-highlight" data-language="python"><pre class="language-python"><code class="language-python"><span class="token punctuation">[</span><span class="token punctuation">(</span>id1<span class="token punctuation">,</span> version1<span class="token punctuation">,</span> cveid1<span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">(</span>id2<span class="token punctuation">,</span> version2<span class="token punctuation">,</span> cveid2<span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span></code></pre></div><p>During the writing of this exercise the <code class="language-text">safety-db</code> package was quite broken,
so instead of installing <code class="language-text">safety-db</code>, you should download the json file <code class="language-text">insecure_full.json</code> directly
from <a href="https://github.com/pyupio/safety-db/tree/master/data" target="_blank" rel="noopener noreferrer">here</a>.</p>

---

