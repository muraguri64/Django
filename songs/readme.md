<h3>Create project</h3>
<p>django-admin startproject mysite</p>

<h3> Create the different apps </h3>
<ul>
<li>python.manage.py startapp auth</li>
<li>python.manage.py startapp albums</li>
<li>python.manage.py startapp songs</li>
</ul>

<h3> Migrate admin, auth, contenttypes, sessions </h3>
<p>python manage.py migrate --database=authdb</p>


<h3> Migrate the fields added to albumsdb </h3>
<ul>
<li>python manage.py makemigrations albums </li>
<li>python manage.py sqlmigrate albums 0001 --database=albumsdb</li>
<li>python manage.py migrate --database=albumsdb</li>
</ul>


<h3> Migrate the fields added to songsdb </h3>
<ul>
<li>python manage.py makemigrations songs</li>
<li>python manage.py sqlmigrate songs 0001 --database=songsdb</li>
<li>python manage.py migrate --database=songsdb</li>
</ul>

<h3> Add data to albums using python shell </h3>
<ul>
<li>python manage.py shell</li>
<li>from albums.models import Album</li>
<li>a= Album(artist="Taylor Swift", album_title="Red", genre="Country", album_logo="https://taylor.com")</li>
<li>b= Album(artist="Myth", album_title="High School", genre="Punk", album_logo="https://myth.com")</li>
<li>a.save(using='albumsdb')</li>
<li>b.save(using='albumsdb')</li>
</ul>

<h3> Add data to songs using python shell </h3>
<ul>
<li>python manage.py shell</li>
<li>from songs.models import Song</li>
<li>c= Song(album=1, song_title="The Lucky One", file_type="mp3")</li>
<li>d = Song(album=1, song_title="State of Grace", file_type="mp3")</li>
<li>e = Song(album=2, song_title="Walking Away", file_type="mp3")</li>
<li>c.save(using='songsdb')</li>
<li>d.save(using='songsdb')</li>
<li>e.save(using='songsdb')</li>
</ul>

<h3> Query songs belonging to album 1 and it will return 2 data objects </h3>
<p>Song.objects.using('songsdb').filter(album=1)</p>


<h3> Query songs belonging to album 2 and it will return 1 data objects </h3>
<p>Song.objects.using('songsdb').filter(album=2)</p>

<h3>NOTE</h3> 

<p>According to Django docs Django does not currently support foreign key relationships spanning multiple databases.
This is because of referential integrity. In order to maintain a relationship between two objects, 
Django needs to know that the primary key of the related object is valid. 
If the primary key is stored on a separate database, it’s not possible to easily evaluate the validity of a primary key.</p>

