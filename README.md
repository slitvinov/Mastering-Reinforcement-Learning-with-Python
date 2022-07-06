[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/slitvinov/Mastering-Reinforcement-Learning-with-Python/HEAD)
<h1>Intro</h2>

Code from a book <a
href="https://github.com/PacktPublishing/Mastering-Reinforcement-Learning-with-Python">Mastering
Reinforcement Learning with Python</a> without dependencies on
cufflinks and plotly. To install dependencies

<pre>
python -m pip install -r requirements.txt --force
</pre>

install and run Jupyter Notebook

<pre>
python -m pip install notebook
jupyter notebook
</pre>

<h2>Hacking</h2>

Convert to python
<pre>
for i in */*.ipynb; do jupyter nbconvert --to python "$i" || break; done
</pre>

Clean output
<pre>
for i in */*.ipynb; do  jupyter nbconvert --clear-output --inplace "$i" || break; done
</pre>

List of imported modules
<pre>
awk '/^from.*import/ || /^import/ {sub(/\..*/, "", $2); print $2}' */*.py */*/*.py | sort | uniq
</pre>
