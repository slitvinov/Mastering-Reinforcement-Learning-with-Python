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

<pre>
for i in */*.ipynb; do jupyter nbconvert --to python "$i"; done
for i in */*.ipynb; do  jupyter nbconvert --clear-output --inplace "$i"; done
</pre>
