
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

