<h4>
    <h3><p>Hi, it's script that uses local network ( cable or WiFi)</p> 
        To use PC via phone. It's server with terminal.</h3>
    <br>
    <p>Remember 2 patterns: 
        <ol>
            <li>Connect via phone and PC with one general local network </li>
            <br>
            <li>Connect via pc and pc with general local network.</li>
        </ol>
    </p>
    <br>
    <p>Use this [ http:// { IP } : { PORT  } /apple/commands/ ]</p>
    [ http://192.168.100.8:8000/apple/commands/ ]
</h4>

<hr>

<h3>Install python, git, pip or Flash Device</h3>

python: https://www.python.org/downloads/release/python-31011/

git: https://git-scm.com/download/win

pip: <code>python get-pip.py</code> 


<hr>

<h3>Install venv + requirements</h3>

<code>python -m venv venv</code>

<code>venv\Scripts\activate.bat</code>

<code>pip install -r requirements.txt</code>

Check - <code>pip list</code>

<hr>

<h3>Run Server</h3>
1.)
<p>Find IP: <code>ipconfig</code></p>
example: '192.168.100.8'

<br><br>
2.)

<p>Add IP in directory: src/config/setting</p>

example:

<code>
    ALLOWED_HOSTS = [
        '192.168.100.8',
    ]
</code>

<br><br>
3.)

Run command in directory: src/

<code>python manage.py runserver 192.168.100.8:8000</code>

<hr>

<h3>Funny windows commands</h3>

<code>dir = ls</code>
<code>cd = pwd</code>

<code>start chrome https://www.pornhub.com/ </code>

<code>cd media</code>

<code>start cats.mp4</code>
