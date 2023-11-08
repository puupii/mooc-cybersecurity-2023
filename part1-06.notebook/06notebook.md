
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

