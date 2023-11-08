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
look into existing software that have similar functionality.</p></div></div></div></div></div>
