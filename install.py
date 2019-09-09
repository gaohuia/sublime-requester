import urllib.request,os,hashlib,tempfile,zipfile,shutil;
version = "1.1.1";
name = "SimpleHttpRequester";
url = "https://github.com/gaohuia/SimpleHttpRequester/archive/v%s.zip" % (version);
pp = sublime.packages_path();
urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) );
by = urllib.request.urlopen(url).read();
io = tempfile.TemporaryFile();
io.write(by);
temp_dir = tempfile.gettempdir();
z = zipfile.ZipFile(io);
z.extractall(temp_dir);
shutil.copytree(temp_dir + "/" + name + "-" + version, pp + "/" + name);
io.close();