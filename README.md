# DjangoでWebアプリ作成（SQLite3）



## 仮想環境作成(venv)

1. 仮想環境  `venv` 作成のためのコマンド  
注意：Macの場合は python3としてください。

```
python -m venv dj_todo
```

2. `cd`コマンドで出来上がったフォルダ（ここではdj_todo）に移動

```
cd dj_todo
```

1. 以下の仮想環境を実行するコマンドを実行（MacとWindowsでコマンドは違うので注意）

#### Macの場合

Macで`venv` の仮想環境を実行するコマンド

```
source bin/activate
```

#### Windowsの場合

Windowsで`venv` の仮想環境を実行するコマンド

```
Scripts\activate
```

#### Windowsで仮想環境を実行時に出るエラー対策

`Scripts\activate`で**「PSSecurityException」**が発生する場合がる

この場合次のコマンド

```
Set-ExecutionPolicy RemoteSigned -Scope Process
```

実行ポリシーを聞かれたら、「Y」を入力してEnter

再び仮想環境に入る

```
Scripts\activate
```

### pip upgrade

```
python -m pip install --upgrade pip
```


仮想環境に入るとMacの場合でも、python3ではなくpythonコマンドが使えるようになります。

また、pipもpip3ではなくpipが使えるようになります。

バージョンなどを確認して正しくこれらのコマンドが使えるか確認してください。

```
python -V
```

```
pip -V
```




## Djangoのインストール

Djangoインストールコマンド  

```
pip install django
```

Djangoのバージョン確認コマンド  

```
python -m django --version
```



## TODOプロジェクト作成

1.  `venv` 仮想フォルダの中にプロジェクト用の新しいフォルダ「TODOPROJECT」を作成

2. コマンドの `cd` でカレントディレクトリを `TODOPROJECT` フォルダに移動します。

   ```
   cd TODOPROJECT
   ```

3. Djangoのプロジェクトを作成するコマンド

```
django-admin startproject todoproject .
```



### アプリケーションの作成

1. アプリケーション作成コマンド  

```
python manage.py startapp todo
```



## Gitの作成

「TODOPROJECT」フォルダ内をGit管理します。

TODOPROJECTフォルダ内に新規で` .gitignore` ファイルを作成して以下記述

GitHubにpushする場合、static/はpushしないように.gitignoreファイルに記述します。

ただし、HEROKUにpushする場合はこの記述を削除します。

```
*.pyc
__pycache__/
db.sqlite3
static/
```

以下コマンドを実行

```
git init
```

```
git add .
```

```
git commit
```

## Djangoの設定

### settings.pyの変更

#### import文の追加

1. 先頭にimport osを追加

```
import os
```

#### シークレットキーの設定

1. シークレットキーの情報をコピーして保存

   ```
   SECRET_KEY = 'ei!mmcb3n(me^ww$&9xz3$r^xf+75_8^2x6_&38)^dti6338-t$=s'
   ```

2. シークレットキーの情報を環境変数に隠蔽

```
SECRET_KEY = os.environ.get('SECRET_KEY_TODO')
```

3. MAC の場合、元々SECRET_KEYに記述されていた値をコピーして自分のPCの環境変数に貼り付け
   ZSHの場合：.zshrcをエディタで開いて下記貼り付け

   bashの場合：.bash_profileをエディタで開いて下記貼り付け

```
export SECRET_KEY_TODO='w0ni-ss@e13^v!dddwb59bug+g4h18-3h^*!sisden#bb@66+@ase'
```

​		**一度deactivateして必ずターミナルを再起動してくだい。**
​		Macで`venv` の仮想環境を実行するコマンド

```
source bin/activate
```

4. Windowsの場合、システムの「環境変数を編集」からユーザー環境変数で新規を選ぶ
   変数名：SECRET_KEY_TODO
   変数値：'w0ni-ss@e13^v!dddwb59bug+g4h18-3h^*!sisden#bb@66+@ase'

   その後、コマンド `deactivate` で仮想環境を出てから**PowerShellを再起動**
   再び仮想環境に入って、cdで現在の階層まで戻る

   Windowsのactivateコマンド

   ```
   Set-ExecutionPolicy RemoteSigned -Scope Process
   ```

   実行ポリシーを聞かれたら、「Y」を入力してEnter

   ```
   Scripts\activate
   ```

   ### 

#### アプリの指定

1. インストールしたアプリの指定

settings.py　INSTALLED_APPS 部分

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
]
```

#### テンプレートの指定

1. TODOPROJECTフォルダ直下にtemplatesフォルダを作成
2. settings.py　TEMPLATES部分の'DIRS'の値を変更

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### データベースの設定

DATABASESの設定は、今回はSQLite3を使用するので変更の必要はない

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### 言語とタイムゾーン

言語とタイムゾーンを変更

```
LANGUAGE_CODE = 'ja'
 
TIME_ZONE = 'Asia/Tokyo'
```

#### staticフォルダ作成

1. cssや画像などを保存するために、static という名前のフォルダをTODOPROJECTフォルダ内に作成

2. settings.pyの最後の`STATIC_URL = '/static/'` の次に下記記述

settings.py

```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```



### 現在のフォルダの状態

```
.
├── manage.py
├── static
├── templates
├── todo
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── todoproject
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   └── settings.cpython-38.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## staticフォルダの準備

staticフォルダにcssやjavascript、画像などの準備をします。

今回はstatic.zipを展開してその内容を全てstaticフォルダに置きます。

static.zip

https://www.startlab-classroom.com/5/static.zip

### ルーティング　urls.pyの編集

#### プロジェクトのurls.pyを編集

1. todoproject/urls.pyの編集
   1. `path('', include('todo.urls')),` を追加
   2. from import文にincludeの追加

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
```

#### アプリのurls.pyを編集

1. todoフォルダに `urls.py` を新規作成（アプリのurls.pyは自動で作成されないので注意）
2. todo/urls.pyに以下コードを追加

```
from django.urls import path
from .views import todo

urlpatterns = [
    path('test/', todo)
]
```

### views.pyの編集

関数ベースビューを `views.py` に作成（Hello!と表示するためのもの）

1. `from django.http import HttpResponse`を追加
2. todo関数の定義　以下コード

```
from django.shortcuts import render
from django.http import HttpResponse

def todo(request):
	return HttpResponse('Hello!')
```

### サーバーの稼働

runserverを稼働させて、admin画面に入りエラーが出ないか確認します。

```
python manage.py runserver
```

URLアドレスは以下を入れる。

http://127.0.0.1:8000/test/

画面に「Hello!」と表示されます。

### サーバーを停止

ctrl + c キーでサーバーを停止

### Gitブランチ作成

ここまでの内容を新しいブランチにします。ブランチ名は「no1_todo」とします。

Gitコマンドは以下

```
git add .
```

```
git commit
```

```
git checkout -b no1_todo
```

```
git checkout master
```

### GitHubにpush

GitHubに新しくリポジトリを作成します。

今回はmainではなくmasterでpushします。

```
git remote add origin https://github.com/[アカウント名]/dj_todo.git
```

```
git push -u origin master
```

```
git push -u origin HEAD
```



.gitignoreファイルにstaticを指定してない場合は、statcが重すぎてpushできないことがあります。

その場合は次のようにします。

```
git config http.postBuffer 10485760
```



## データベースの設定

### models.pyの編集

1. `models.py` の `class` を活用してテーブルを作成します。
   以下コードで、from import文以外のコードを貼り付ける

```
from django.db import models


PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    auther = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY,
    )
    progress = models.PositiveSmallIntegerField()
    duedate = models.DateField()
    complete = models.BooleanField()

    def __str__(self):
        return self.title
```



#### makemigrationsとmigrateコマンドの実行

1. makemigrationsコマンド

```
python manage.py makemigrations
```

2. migrateコマンド

```
python manage.py migrate
```

OKが沢山出たら次へ進む

### admin画面からテストデータの入力

1. superuserを作成は次のコマンド

```
python manage.py createsuperuser
```

2. superuserの名前を聞いてきますので、名前を入力します。（忘れないように！）

3. メールアドレスは不要そのままEnter　

4. パスワードは好みのパスワードを指定します。（忘れないように！）

5. admin.pyを次のように編集

```
from django.contrib import admin
from .models import TodoModel


admin.site.register(TodoModel)
```

これでデータ入力が可能になります。

### サーバーの稼働

runserverを稼働させて、admin画面に入りエラーが出ないか確認します。

```
python manage.py runserver
```

URLアドレスは以下を入れる。

http://127.0.0.1:8000/test/

画面に「Hello!」と表示されます。

### データ登録

次に、adminのアドレスを入れてデータを登録してみます。

http://127.0.0.1:8000/admin/

**http://127.0.0.1:8000ではないので注意！**

#### 認証

superuserで作成したユーザーとパスワードで認証します。

#### データ入力

1. 無事にadmin画面に入れたら、TODOの「追加」からいくつか予定を入力して確認します。

特にエラーが出なければ、データベースとの連携は取れています。

### サーバーを停止

ctrl + c キーでサーバーを停止



### Gitブランチ作成

ここまでの内容を新しいブランチにします。ブランチ名は「no2_todo」とします。

Gitコマンドは以下

```
git add .
```

```
git commit
```

```
git checkout -b no2_todo
```

```
git checkout master
```

### GitHubにpush

masterと作成したブランチをpushします。

```
git push -u origin HEAD
```

## ここまでうまくいかなかった場合

エラーの内容を確認して、ここまでの手順に間違いがなかったか確認します。

解決されない場合、sampleをクローンしたGitデータにcd で移動後に、`git checkout no2_todo` とした上で、TODOPROJECTフォルダ内のファイルを自分のものに上書きするとこの段階まで再現されるはずです。

それでもエラーが出てうまくいかない場合は、最初の仮想環境を作成するところからやり直してください。







## ユーザー登録ページ作成

#### todo/urls.pyの編集

1. from import文に`signupview`を追加
2. urlpatternsに`path('signup/', signupview, name='signup'),`を追加

```
from django.urls import path
from .views import todo, signupview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('test/', todo)
]
```

#### views.pyの編集

1. import文追加
   `from django.db import IntegrityError`を追加
2. def signupview(request):関数の定義追加

```
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError


def todo(request):
    return HttpResponse('Hello!')


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})


```



## テンプレートの編集

### base.htmlテンプレート

1. templates/base.htmlを新規作成
2. 以下コードを追加

```
<!DOCTYPE html>
<html lang="en">

<head>
  {% load static %}
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <!-- Custom fonts for this template-->
  <link href="{% static 'fontawesome-free/css/all.min.css' %}" rel="stylesheet" type="text/css">
  <link
    href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
    rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet">
  <title>TodoList</title>
</head>

<body id="page-top">
  {% block header %}

  {% endblock header %}
  <div class="container">
    {% block content %}

    {% endblock content %}
  </div>
  <!-- Footer -->
  <footer class="sticky-footer bg-white">
    <div class="container my-auto">
      <div class="copyright text-center my-auto">
        <span>Copyright &copy; Python Start Lab.</span>
      </div>
    </div>
  </footer>
  <!-- End of Footer -->
  <!-- Bootstrap core JavaScript-->
  <script src="{% static 'js/jquery.min.js' %}"></script>
  <script src="{% static 'sjs/bootstrap.bundle.min.js' %}"></script>

  <!-- Core plugin JavaScript-->
  <script src="{% static 'js/jquery.easing.min.js' %}"></script>

  <!-- Custom scripts for all pages-->
  <script src="{% static 'js/sb-admin-2.min.js' %}"></script>

</body>

</html>
```

### signup.htmlテンプレート

1. templates/signup.htmlを新規作成
2. 以下コードを追加

```
{% extends 'base.html' %}

{% block content%}

<div class="container">

    <!-- Outer Row -->
    <div class="row justify-content-center">

        <div class="col-xl-10 col-lg-12 col-md-9">

            <div class="card o-hidden border-0 shadow-lg my-5">
                <div class="card-body p-0">
                    <!-- Nested Row within Card Body -->
                    <div class="row">
                        <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                        <div class="col-lg-6">
                            <div class="p-5">
                                <div class="text-center">
                                    <h1 class="h4 text-gray-900 mb-4">Please sign up</h1>
                                </div>
                                <form class="user" method='post'>{% csrf_token %}
                                    {% if error %}
                                    {{ error }}
                                    {% endif %}
                                    <div class="form-group">
                                        <input type="text" class="form-control form-control-user" name="username_data"
                                            id="exampleInputEmail" aria-describedby="emailHelp" placeholder="Username">
                                    </div>
                                    <div class="form-group">
                                        <input type="password" class="form-control form-control-user"
                                            name="password_data" id="exampleInputPassword" placeholder="Password">
                                    </div>

                                    <button class="btn btn-primary btn-user btn-block" type="submit">
                                        Sign up
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

    </div>

</div>


{% endblock content %}
```

### サーバー稼働で確認

サーバーが停止していたら再度稼働させます。

```
python manage.py runserver
```
URLアドレスに次のアドレスを入れます。


http://127.0.0.1:8000/signup/

### Gitブランチ作成

ここまでGit branch は　「no3_todo」

```
git add .
```

```
git commit
```

```
git checkout -b no3_todo
```

```
git checkout master
```

### GitHubにpush

masterと作成したブランチをpushします。

```
git push -u origin HEAD
```



## ログインの仕組み作成

#### todo/urls.pyの編集

1. from import文に`loginview`を追加
2. urlpatternsに`path('login/', loginview, name='login'),`を追加

```
from django.urls import path
from .views import todo, signupview, loginview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('test/', todo)
]
```

#### todo/views.pyの編集

1. import文追加
2. def loginview(request):関数の定義追加

```
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login


def todo(request):
    return HttpResponse('Hello!')


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')  #今の段階では機能しない
        else:
            return redirect('login')
    return render(request, 'login.html')

```

### templateの作成

1. templatesフォルダにlogin.htmlを作成
   この段階ではまだCSSは完全に適用されていません。

2. templates/login.html

```
{% extends 'base.html' %}

{% block content%}


<div class="container">
    <form class="form-signin" method='post'>{% csrf_token %}
        <h1 class="h3 mb-3 font-weight-normal">Please login</h1>
        <label for="inputEmail" class="sr-only">Username</label>
        <input type="text" id="inputEmail" class="form-control" placeholder="username" name="username_data" required
            autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input type="password" id="inputPassword" class="form-control" placeholder="Password" name="password_data"
            required>
        <div class="checkbox mb-3">
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">login</button>
        <p class="mt-5 mb-3 text-muted">&copy; 2017-2019</p>
    </form>
</div>
{% endblock content %}
```



### Git ブランチ作成

ここまでGit branch は　add. と　commitした後「no4_todo」

```
git add .
```

```
git commit
```

```
git checkout -b no4_todo
```

pushが終わったらmainにブランチを戻します。

```
git checkout master
```

### GitHubにpush

masterと作成したブランチをpushします。

```
git push -u origin HEAD
```



## CRUDの仕組みを構築

### Home画面の作成

#### todo/urls.pyの編集

1. from import文に`TodoList`を追加、そして todoを削除
2. urlpatternsの`path('test/', todo)`を削除
3. urlpatternsに`path('', TodoList.as_view(), name='list'),`を追加

```
from django.urls import path
from .views import  signupview, loginview, TodoList

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('', TodoList.as_view(), name='list'),
]

```

#### views.pyの編集

1. import文追加
2. def todo(request):関数の定義を削除(仮のHello!を削除)
3. class TodoList(ListView):定義

```
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from .models import TodoModel
from django.http import HttpResponse
 
 
class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel
 
 
def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})
 
 
def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')
```

---------------------------------------------------　　　　ここから説明内容　　　　---------------------------------------------------

### template/index.htmlの概要

#### header部分の作成

1. header部分はBootstrapのJumbotronを使用

2. `{% block header %}`領域にBootstrapのJumbotronの内容を貼り付け、文言を適当な内容に変更します。

#### buttonの設定

3. Bootstrap の Buttonsグループから好みのものを選びコピペします。ボタンはsmallサイズを使いました。

#### 優先度に応じてデザインを変えたい

4. 優先度はpriorityで設定し、high,normal,lowがあります。

5. 優先度の設定次第で背景色を変える仕組みを作ります。

6. 今回変える色のクラス名は `alert-danger` 、 `alert-info` 、 `alert-success`の3種類です。

7. HTMLの方には次のような設定を入れます。

```
<div class="alert alert-{{item.priority}}" role="alert">
```

8. 動的に変更する名前はmodels.pyに次のようなPRIORITYの記述をします。結果、第2引数の指定をすると第1引数の値が`item.priority`に入ることになります。

9. すでに作成している、models.pyの次のコードがPRIORITYに対応しています。

```
PRIORITY = (('danger','high'),('info','normal'),('success','low'))
```

#### タスク完了の処理（完了を表示）

10. 完了の場合はif文で判定して`{% if item.complete == True %}<span class="text-danger font-weight-bold">完了</span>{% endif %}`完了の赤い文字を表示させます。

---------------------------------------------------　　　　ここまで説明　　　---------------------------------------------------





### index.htmlファイル作成

1. index.htmlの新規作成と以下コードを貼り付け
   この段階ではリンクなど設定されていません。

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron text-center">
  <h1 class="display-4">TodoList</h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}

{% block content %}
<!-- Page Wrapper -->
<div id="wrapper">

  <!-- Content Wrapper -->
  <div id="content-wrapper" class="d-flex flex-column">

    <!-- Main Content -->
    <div id="content">


      <!-- Begin Page Content -->
      <div class="container-fluid">
        <p><a class="btn btn-primary btn-sm" href="" role="button">新規作成</a></p>
        <div class="row">
          <!-- Tasks Card Example -->
          {% for item in object_list %}
          <div class="col-md-6 mb-4">
            <div class="card border-left-{{item.priority}} shadow h-100 py-2">
              <div class="card-body">
                <div class="row no-gutters align-items-center">
                  <div class="col mr-2">
                    <div class="text-xs font-weight-bold text-info text-uppercase mb-1">Tasks</div>
                    <div class="row no-gutters align-items-center">
                      <div class="col-auto">
                        <div class="h5 mb-0 mr-3 font-weight-bold text-gray-800">30%</div>
                      </div>
                      <div class="col">
                        <div class="progress progress-sm mr-2">
                          <div class="progress-bar bg-info" role="progressbar" style="width:30%" aria-valuenow="30"
                            aria-valuemin="0" aria-valuemax="100">
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-auto">
                    <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                  </div>
                </div>
                <div class="card-body">
                  {% if item.complete == True %}<span
                    class="text-danger font-weight-bold">完了</span>{% endif %}　{{ item.title }}
                  　<p>期日：{{ item.duedate }}</p>
                </div>
                <p><a class="btn btn-primary btn-sm" href="" role="button">詳細</a>
                  <a class="btn btn-success btn-sm" href="" role="button">編集</a>
                  <a class="btn btn-danger btn-sm" href="" role="button">削除</a></p>
              </div>
            </div>
          </div>

          {% endfor %}
        </div>

      </div>

      <!-- /.container-fluid -->

    </div>
    <!-- End of Main Content -->

  </div>
  <!-- End of Content Wrapper -->

</div>
<!-- End of Page Wrapper -->

<!-- Scroll to Top Button-->
<a class="scroll-to-top rounded" href="#page-top">
  <i class="fas fa-angle-up"></i>
</a>

{% endblock content %}
```

### サーバーの再稼働で確認

サーバーが停止していたら再度稼働させます。

この段階では、loginの画面はまだ完成されていません。

```
python manage.py runserver
```

### Git ブランチ作成

ここまでGit branch は　add. と　commitした後「no5_todo」

```
git add .
```

```
git commit
```

```
git checkout -b no5_todo
```

pushが終わったらmainにブランチを戻します。

```
git checkout master
```

### GitHubにpush

masterと作成したブランチをpushします。

```
git push -u origin HEAD
```



### 詳細画面の作成

todoの詳細を見るページ

#### todo/urls.pyの編集

1. from import文に`TodoDetail`を追加、そして todoを削除
2. urlpatternsに` path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),`を追加
   `<int:pk>`がポイント

```
from django.urls import path
from .views import signupview, loginview, TodoList, TodoDetail

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
]
```

#### views.pyの編集

1. from django.views.generic import文に DetailViewを追加
2. class TodoDetail(DetailView):定義

```
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import TodoModel

from django.http import HttpResponse


class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

```



### index.htmlの変更

#### index.htmの編集

1. 詳細リンクのhref属性に値を入れます。`{% url 'detail' item.pk %}`

```
<p>
<a class="btn btn-primary btn-sm" href="{% url 'detail' item.pk %}" role="button">詳細</a>
     <a class="btn btn-success btn-sm" href="" role="button">編集</a>
     <a class="btn btn-danger btn-sm" href="" role="button">削除</a>
</p>
```

#### templates/detail.htmlの新規作成

detail.htmlを新規作成して以下コードを記述

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron text-center">
  <h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}
{% block content %}
<div class="alert alert-primary" role="alert">
  <p><span>タイトル：</span>{{ object.title }}</p>
  <p><span>内容：</span>{{ object.memo }}</p>
  <p><span>期日：</span>{{ object.duedate }}</p>
  <p><span>進捗度：</span>{{ object.progress }}%</p>
</div>
<p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}" role="button">戻る</a></p>
{% endblock content %}
```



## 新規作成画面の作成

#### todo/urls.pyの編集

1. from import文に`TodoCreate`を追加
2. urlpatternsに` path('create/', TodoCreate.as_view(), name='create'),`を追加

```
from django.urls import path
from .views import signupview, loginview, TodoList, TodoDetail, TodoCreate

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
]
```

#### views.pyの編集

1. from django.views.generic import文に CreateViewを追加
2. class TodoCreate(CreateView):定義

```
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import TodoModel
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'auther', 'priority',
              'progress', 'duedate', 'complete')
    success_url = reverse_lazy('list')

```

### create.htmlテンプレート作成

1. create.htmlの編集

```
{% extends 'base.html' %}
{% load static %}
{% block header %}
<div class="jumbotron text-center">
  <h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}
{% block content %}
{% if user.is_authenticated %}
<form action='' method='POST'>{% csrf_token %}
  <p>タイトル：<input type='text' name='title'></p>
  <p>内容：<textarea name='memo' cols="30" rows="10"></textarea></p>
  <p>重要度：
    <select name='priority'>
      <option value="danger">high</option>
      <option value="info">normal</option>
      <option value="success">low</option>
    </select>
  </p>
  <p>期限：<input type='datetime' name='duedate'></p>
  <p>進捗度：<input type='range' name='progress' 　min="0" max="100"></p>
  <p>完了：<input type='checkbox' name='complete' value=False></p>
  <input type="hidden" name="auther" value="{{ user.username }}">
  <!-- {{ form.as_p}} -->
  <input type='submit' value='作成する'>
</form>

<p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}" role="button">戻る</a></p>
{% else %}
ログインしてください。
<a href="{% url 'login' %}" class="btn btn-primary" role="button" aria-pressed="true">ログイン</a>
{% endif %}
{% endblock content  %}
```

### 削除画面の作成とログアウト

1. urls.pyの編集

```
from django.urls import path
from .views import signupview, loginview, TodoList, TodoDetail, TodoCreate, logoutview, TodoDelete

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),

]
```

2. vews.pyの編集

```
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import TodoModel
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy


class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'auther', 'priority',
              'progress', 'duedate', 'complete')
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


def logoutview(request):
    logout(request)
    return redirect('login')
```

3. delete.html作成

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron text-center">
  <h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}

{% block content %}
{% if user.is_authenticated %}
<p>選択したタスクを削除します。</p>
<form action="" method="POST">{% csrf_token %}
  <input type="submit" value="削除します">
</form>
<p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}" role="button">戻る</a></p>
{% else %}
ログインしてください。
<a href="{% url 'login' %}" class="btn btn-primary" role="button" aria-pressed="true">ログイン</a>
{% endif %}
{% endblock content %}
```

### 更新画面の作成(urls.pyとviews.py最終のコード)

1. urls.py編集
2. このコードが最終の urls.py コード

```
from django.urls import path
from .views import signupview, loginview, TodoList, TodoDetail, TodoCreate, logoutview, TodoDelete, TodoUpdate


urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(),name='update')
]

```

1. views.py編集
2. このコードが最終の views.py コード

```
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import TodoModel
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


class TodoList(ListView):
    template_name = 'index.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,
                            password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'auther', 'priority',
              'progress', 'duedate', 'complete')
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'auther', 'priority',
              'progress', 'duedate', 'complete')
    success_url = reverse_lazy('list')


def logoutview(request):
    logout(request)
    return redirect('login')

```

3. update.html新規作成

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron text-center">
	<h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
	<p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}

{% block content %}
{% if user.is_authenticated %}
<form action="" method="POST">{% csrf_token %}
	<p>{{ form.title }}</p>
	<p>{{ form.memo }}</p>
	<p>{{ form.priority }}</p>
	<p>{{ form.duedate }}</p>
	<p>{{ form.progress }}</p>
	<p><input type="hidden" name="auther" value="{{ user.username }}"></p>
	<p>{{ form.complete }}</p>
	<input type="submit" value="更新">
</form>
<p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}" role="button">戻る</a></p>
{% else %}
ログインしてください。
<a href="{% url 'login' %}" class="btn btn-primary" role="button" aria-pressed="true">ログイン</a>
{% endif %}
{% endblock content %}
```

## ここからテンプレートを完成させます。

### indexhtmlの完成

#### リンクの設定

1. index.htmlの編集
2. 編集部分のhref属性の値に`{% url 'update' item.pk %}`の追加
3. 削除部分のhref属性の値に`{% url 'delete' item.pk %}`の追加

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron">
  <h1 class="display-4">TodoList</h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}

{% block content %}
一部省略
{% for item in object_list %}
<div class="alert alert-{{item.priority}}" role="alert">
  <p>{{ item.title }}</p>
  <p><a class="btn btn-primary btn-sm" href="{% url 'detail' item.pk %}" role="button">詳細</a>
  <a class="btn btn-success btn-sm" href="{% url 'update' item.pk %}" role="button">編集</a>
  <a class="btn btn-danger btn-sm" href="{% url 'delete' item.pk %}" role="button">削除</a></p>
</div>
{% endfor %}
{% endblock content %}
```

### 最終デザインの調整

1. index.html 日付の追加
2. ` <p>{{ item.title }} 　期日：{{ item.duedate }}</p>`

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron">
  <h1 class="display-4">TodoList</h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}

{% block content %}
{% for item in object_list %}
<div class="alert alert-{{item.priority}}" role="alert">
  <p>{{ item.title }} 　期日：{{ item.duedate }}</p>
  <p><a class="btn btn-primary btn-sm" href="{% url 'detail' item.pk %}" role="button">詳細</a>
  <a class="btn btn-success btn-sm" href="{% url 'update' item.pk %}" role="button">編集</a>
  <a class="btn btn-danger btn-sm" href="{% url 'delete' item.pk %}" role="button">削除</a></p>
</div>
{% endfor %}
{% endblock content %}
```

### 新規作成ボタン追加

1. index.htmlの編集
2. 新規作成部分のhref属性の値に`{% url 'create' %}`の追加

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron">
  <h1 class="display-4">TodoList</h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}

{% block content %}
{% for item in object_list %}
<div class="alert alert-{{item.priority}}" role="alert">
 <p><a class="btn btn-primary btn-sm" href="{% url 'create' %}" role="button">新規作成</a>
  <p>{{ item.title }} 　期日：{{ item.duedate }}</p>
  <p><a class="btn btn-primary btn-sm" href="{% url 'detail' item.pk %}" role="button">詳細</a>
  <a class="btn btn-success btn-sm" href="{% url 'update' item.pk %}" role="button">編集</a>
  <a class="btn btn-danger btn-sm" href="{% url 'delete' item.pk %}" role="button">削除</a></p>
</div>
{% endfor %}
{% endblock content %}
```

#### ログイン・ログアウトボタン作成

1. index.htmlの`{% block header %}`と`{% endblock header %}`内の内容を以下に変更

```
<div class="jumbotron text-center">
  <ul class="nav nav-pills d-flex flex-row justify-content-end">
    <li class="nav-item">
      <a class="nav-link active" href="{% url 'login' %}">Login</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="{% url 'logout' %}">Logout</a>
    </li>
  </ul>
  <h1 class="display-4">TodoList</h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
```

### プログレスバーデザイン

index.html

```
<div class="col-auto">
     <div class="h5 mb-0 mr-3 font-weight-bold text-gray-800">{{ item.progress }}%</div>
</div>
<div class="col">
 <div class="progress progress-sm mr-2">
   <div class="progress-bar bg-info" role="progressbar" style="width:{{ item.progress }}%"
                            aria-valuenow="{{ item.progress }}" aria-valuemin="0" aria-valuemax="100"></div>
 </div>
</div>
```

## テンプレート完成コード

#### ベースページ

base.htmlテンプレートの完成

```
<!DOCTYPE html>
<html lang="en">

<head>
    {% load static %}
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Custom fonts for this template-->
    <link href="{% static 'fontawesome-free/css/all.min.css' %}" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet">
    <title>TodoList</title>
</head>

<body id="page-top">
    {% block header %} {% endblock header %}
    <div class="container">
        {% block content %} {% endblock content %}
    </div>
    <!-- Footer -->
    <footer class="sticky-footer bg-white">
        <div class="container my-auto">
            <div class="copyright text-center my-auto">
                <span>Copyright &copy; Python Start Lab.</span>
            </div>
        </div>
    </footer>
    <!-- End of Footer -->
    <!-- Bootstrap core JavaScript-->
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'sjs/bootstrap.bundle.min.js' %}"></script>

    <!-- Core plugin JavaScript-->
    <script src="{% static 'js/jquery.easing.min.js' %}"></script>

    <!-- Custom scripts for all pages-->
    <script src="{% static 'js/sb-admin-2.min.js' %}"></script>

</body>

</html>
```

#### Topページ

index.htmlテンプレートの完成

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron text-center">
    <ul class="nav nav-pills d-flex flex-row justify-content-end">
      <li class="nav-item">
        <a class="nav-link active" href="{% url 'login' %}">Login</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'logout' %}">Logout</a>
      </li>
    </ul>
    <h1 class="display-4">TodoList</h1>
    <p class="lead">This is a simple TodoList.</p>
  </div>
{% endblock header %}

{% block content %}
<!-- Page Wrapper -->
<div id="wrapper">

  <!-- Content Wrapper -->
  <div id="content-wrapper" class="d-flex flex-column">

    <!-- Main Content -->
    <div id="content">


      <!-- Begin Page Content -->
      <div class="container-fluid">
        <p><a class="btn btn-primary btn-sm" href="{% url 'create' %}" role="button">新規作成</a></p>
        <div class="row">
          <!-- Tasks Card Example -->
          {% for item in object_list %}
          <div class="col-md-6 mb-4">
            <div class="card border-left-{{item.priority}} shadow h-100 py-2">
              <div class="card-body">
                <div class="row no-gutters align-items-center">
                  <div class="col mr-2">
                    <div class="text-xs font-weight-bold text-info text-uppercase mb-1">Tasks</div>
                    <div class="row no-gutters align-items-center">
                      <div class="col-auto">
                        <div class="h5 mb-0 mr-3 font-weight-bold text-gray-800">{{ item.progress }}%</div>
                      </div>
                      <div class="col">
                        <div class="progress progress-sm mr-2">
                          <div class="progress-bar bg-info" role="progressbar" style="width:{{ item.progress }}%"
                            aria-valuenow="{{ item.progress }}" aria-valuemin="0" aria-valuemax="100">
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-auto">
                    <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                  </div>
                </div>
                <div class="card-body">
                  {% if item.complete == True %}<span
                    class="text-danger font-weight-bold">完了</span>{% endif %}　{{ item.title }}
                  　<p>期日：{{ item.duedate }}</p>
                </div>
                <p>{{ item.title }} 　期日：{{ item.duedate }}</p>
                <p><a class="btn btn-primary btn-sm" href="{% url 'detail' item.pk %}" role="button">詳細</a>
                  <a class="btn btn-success btn-sm" href="{% url 'update' item.pk %}" role="button">編集</a>
                  <a class="btn btn-danger btn-sm" href="{% url 'delete' item.pk %}" role="button">削除</a></p>
              </div>
            </div>
          </div>

          {% endfor %}
        </div>

      </div>

      <!-- /.container-fluid -->

    </div>
    <!-- End of Main Content -->

  </div>
  <!-- End of Content Wrapper -->

</div>
<!-- End of Page Wrapper -->

<!-- Scroll to Top Button-->
<a class="scroll-to-top rounded" href="#page-top">
  <i class="fas fa-angle-up"></i>
</a>

{% endblock content %}
```

#### ログインページ完成

templates/login.html

```
{% extends 'base.html' %}

{% block content%}

<div class="container">

    <!-- Outer Row -->
    <div class="row justify-content-center">

        <div class="col-xl-10 col-lg-12 col-md-9">

            <div class="card o-hidden border-0 shadow-lg my-5">
                <div class="card-body p-0">
                    <!-- Nested Row within Card Body -->
                    <div class="row">
                        <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                        <div class="col-lg-6">
                            <div class="p-5">
                                <div class="text-center">
                                    <h1 class="h4 text-gray-900 mb-4">Please login</h1>
                                </div>
                                <form class="user" method='post'>{% csrf_token %}
                                    {% if error %}
                                    {{ error }}
                                    {% endif %}
                                    <div class="form-group">
                                        <input type="text" class="form-control form-control-user" name="username_data"
                                            id="exampleInputEmail" aria-describedby="emailHelp" placeholder="Username">
                                    </div>
                                    <div class="form-group">
                                        <input type="password" class="form-control form-control-user"
                                            name="password_data" id="exampleInputPassword" placeholder="Password">
                                    </div>

                                    <button class="btn btn-primary btn-user btn-block" type="submit">
                                        Sign up
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

    </div>

</div>

{% endblock content %}
```

#### 新規作成ページ完成

templates/crate.html

```
{% extends 'base.html' %}
{% load static %}

{% block header %}
<div class="jumbotron text-center">
  <h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
  <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}
{% block content %}
{% if user.is_authenticated %}

<div class="container">

  <div class="card o-hidden border-0 shadow-lg my-5">
    <div class="card-body p-0">
      <!-- Nested Row within Card Body -->
      <div class="row">
        <div class="col-lg-5 d-none d-lg-block bg-register-image"></div>
        <div class="col-lg-7">
          <div class="p-5">
            <div class="text-center">
              <h1 class="h4 text-gray-900 mb-4">Create a Todo</h1>
            </div>
            <form class="user" action='' method='POST'>{% csrf_token %}
              <div class="form-group row">
                <div class="col-sm-12 mb-3">
                  <label for="title">タイトル</label>
                  <input type="text" class="form-control form-control-user" id="title" name="title" placeholder="title">
                </div>
                <div class="col-sm-12 mb-3">
                  <label for="memo">内容</label>
                  <textarea name='memo' class="form-control" id="memo" rows="3"></textarea>
                </div>
                <div class=" col-sm-12 mb-3">
                  <label for="priority">重要度</label>
                  <select class="form-control" name="priority" id="priority">
                    <option value="danger">high</option>
                    <option value="warning">normal</option>
                    <option value="success">low</option>
                  </select>
                </div>
                <div class="col-sm-12 mb-3">
                  <label for="duedate">期限</label>
                  <input type="text" class="form-control form-control-user" id="duedate" name="duedate"
                    value="2025-01-11">
                </div>
                <div class="col-sm-12 mb-3">
                  <label for="progress">進捗度</label>
                  <input type="range" class="form-control form-control-user" id="progress" name="progress" min="0"
                    max="100">
                </div>
                <div class="col-sm-12 mb-3 ml-4">
                  <input type="checkbox" class="form-check-input" id="complete" name="complete" value=False>
                  <label for="complete" class="form-check-label">完了</label>
                </div>
                <div> <input type="hidden" name="auther" value="{{ user.username }}"></div>
              </div>
              <input type='submit' value="作成する" class="btn btn-primary btn-user btn-block">
            </form>
            <hr>
            <div class="text-center">
              <p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}" role="button">戻る</a>
              </p>
              {% else %}
              <hr>
              <a href="{% url 'login' %}" class="btn btn-danger btn-user btn-block">
                login
              </a>
              {% endif %}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>
{% endblock content  %}
```

#### 更新ページ完成

templates/update.html

```
{% extends 'base.html' %}
{% block header %}
<div class="jumbotron text-center">
	<h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
	<p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %}

{% block content %}
{% if user.is_authenticated %}

<div class="container">

	<div class="card o-hidden border-0 shadow-lg my-5">
		<div class="card-body p-0">
			<!-- Nested Row within Card Body -->
			<div class="row">
				<div class="col-lg-5 d-none d-lg-block bg-register-image"></div>
				<div class="col-lg-7">
					<div class="p-5">
						<div class="text-center">
							<h1 class="h4 text-gray-900 mb-4">Create a Todo</h1>
						</div>
						<form class="user" action='' method='POST'>{% csrf_token %}
							<div class="form-group row">
								<div class="col-sm-12 mb-3">
									<label>タイトル
										<p>{{ form.title }}</p></label>
								</div>
								<div class="col-sm-12 mb-3">
									<label for="memo">内容
										<p>{{ form.memo }}</p></label>
								</div>
								<div class=" col-sm-12 mb-3">
									<label for="priority">重要度
										<p>{{ form.priority }}</p></label>
								</div>
								<div class="col-sm-12 mb-3">
									<label for="duedate">期限
										<p>{{ form.duedate }}</p></label>
								</div>
								<div class="col-sm-12 mb-3">
									<label for="progress">進捗度
										<p>{{ form.progress }}</p></label>
								</div>
								<div class="col-sm-12 mb-3 ml-4">

									<label for="complete" class="form-check-label">完了 <p>{{ form.complete }}</p>
									</label>
								</div>
								<div> <input type="hidden" name="auther" value="{{ user.username }}"></div>
							</div>
							<input type='submit' value="更新する" class="btn btn-primary btn-user btn-block">
						</form>
						<hr>
						<div class="text-center">
							<p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}"
									role="button">戻る</a>
							</p>
							{% else %}
							<hr>
							<a href="{% url 'login' %}" class="btn btn-danger btn-user btn-block">
								login
							</a>
							{% endif %}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

</div>

{% endblock content %}
```

#### 削除ページ

delete.html

```
{% extends 'base.html' %} {% block header %}
<div class="jumbotron text-center">
    <h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
    <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %} {% block content %} {% if user.is_authenticated %}
<p>選択したタスクを削除します。</p>
<form action="" method="POST">{% csrf_token %}
    <input type="submit" value="削除します">
</form>
<p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}" role="button">戻る</a></p>
{% else %} ログインしてください。
<a href="{% url 'login' %}" class="btn btn-primary" role="button" aria-pressed="true">ログイン</a> {% endif %} {% endblock content %}
```

#### 詳細ページ

detail.html

```
{% extends 'base.html' %} {% block header %}
<div class="jumbotron text-center">
    <h1 class="display-4"><a href="{% url 'list' %}">TodoList</a></h1>
    <p class="lead">This is a simple TodoList.</p>
</div>
{% endblock header %} {% block content %}
<div class="alert alert-primary" role="alert">
    <p><span>タイトル：</span>{{ object.title }}</p>
    <p><span>内容：</span>{{ object.memo }}</p>
    <p><span>期日：</span>{{ object.duedate }}</p>
    <p><span>進捗度：</span>{{ object.progress }}%</p>
</div>
<p class="text-center"><a class="btn btn-outline-primary" href="{% url 'list' %}" role="button">戻る</a></p>
{% endblock content %}
```

#### signupページ

signup.html

```
{% extends 'base.html' %} {% block content%}

<div class="container">

    <!-- Outer Row -->
    <div class="row justify-content-center">

        <div class="col-xl-10 col-lg-12 col-md-9">

            <div class="card o-hidden border-0 shadow-lg my-5">
                <div class="card-body p-0">
                    <!-- Nested Row within Card Body -->
                    <div class="row">
                        <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                        <div class="col-lg-6">
                            <div class="p-5">
                                <div class="text-center">
                                    <h1 class="h4 text-gray-900 mb-4">Please sign up</h1>
                                </div>
                                <form class="user" method='post'>{% csrf_token %} {% if error %} {{ error }} {% endif %}
                                    <div class="form-group">
                                        <input type="text" class="form-control form-control-user" name="username_data" id="exampleInputEmail" aria-describedby="emailHelp" placeholder="Username">
                                    </div>
                                    <div class="form-group">
                                        <input type="password" class="form-control form-control-user" name="password_data" id="exampleInputPassword" placeholder="Password">
                                    </div>

                                    <button class="btn btn-primary btn-user btn-block" type="submit">
                                        Sign up
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

    </div>

</div>


{% endblock content %}
```



### サーバーの再稼働でローカル環境完成の確認

サーバーが停止していたら再度稼働させます。

```
python manage.py runserver
```



### Git ブランチ作成

ここまでGit branch は　add. と　commitした後「no6_todo」

```
git add .
```

```
git commit
```

```
git checkout -b no6_todo
```

```
git checkout master
```

### GitHubにpush

masterと作成したブランチをpushします。

```
git push -u origin HEAD
```



# Herokuへデプロイ（PostgreSQL）

本番のサーバー環境にデプロイする場合、ローカル環境で構築した内容をsettings.py中心に各所の変更が必要になります。そうするとローカル環境での確認ができなくなります。

つまり、ローカル用の記述と本番用の記述が最低必要になります。この切り替えをシステマティックに行いたいものです。もっとも手軽な方法はGitのブランチを切り替える方法です。今回はGitのブランチをローカル用と本番用2つ追加していきます。`master`ブランチにHEROKUデプロイ用の設定を作成します。



現在のブランチを確認するgitコマンド

```
git branch
```

`master` ブランチに戻るgitコマンド

```
git checkout master
```



今後の処理はmasterブランチで行います。

## Herokuにデプロイ

### Herokuのデプロイに必要なパッケージ導入

1. TODOPROJECTフォルダにcdで移動して、次のコマンドを実行

2. dj-database-urlのインストール

```
pip install dj-database-url gunicorn whitenoise
```

3. psycopgのインストール

   **Macではエラーになるので注意**

```
pip install psycopg2
```

4. **MACでpsycopg2のインストールでエラーが出た場合**、
   psycopg2-binaryのインストール

```
pip install psycopg2-binary
```



## `requirements.txt`ファイル作成

1. TODOPROJECTフォルダ直下に、`requirements.txt`ファイルを作成しますが、以下のコマンドで作成することができます。

```
pip freeze > requirements.txt
```

2. 実行後出来た `requirements.txt` の内容の例

```
asgiref==3.2.10
dj-database-url==0.5.0
Django==3.1.1
gunicorn==20.0.4
psycopg2-binary==2.8.6
pytz==2020.1
sqlparse==0.3.1
whitenoise==5.2.0
```

## Procfile

1. テキストエディタで`TODOPROJECT`ディレクトリ下に`Procfile`というファイルを作成

2. 次の行を記述します。`Procfile`に拡張子はありません。

Procfile記述内容

```
web: gunicorn todoproject.wsgi --log-file -
```



## `runtime.txt`ファイル

1. アプリを作成したPCのPythonのバージョンを確認

   ```
   python -V
   ```

2. テキストエディタで``TODOPROJECT``ディレクトリ下に`runtime.txt`というファイルを作成して、Pythonのバージョンを次のテキストを例に書き込む。

```
python-3.9.0
```

## settings.pyの編集

#### ALLOWED_HOSTの変更

1. settings.py ALLOWD_HOSTの編集

```
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
```

2. DEBUG は`DEBUG = False`に変更

3. MIDDLEWARE の2行目に ` 'whitenoise.middleware.WhiteNoiseMiddleware',`を追加

4. INSTALLED_APPS に`'gunicorn'` 追加

5. Postgre SQLに対応するためにすることは次のDATABASEの記述を変更するだけです。

   DATABASEは`DATABASES = {'default': dj_database_url.config()}`に変更

8. 最終行は以下になるように追加

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

9. 最初にimportも追加

```
import dj_database_url
```

HerokuLに対応したsettings.py全てコードは以下


settings.py 

```python
import dj_database_url
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY_TODO')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
    'gunicorn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todoproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {'default': dj_database_url.config()}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

```

--------------------------------------------------------               以下説明                      --------------------------------------------------------

settings.pyの次の内容はローカルサーバーにstaticの場所を教えています。

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

次の内容は本番サーバーにstaticの場所を教えます。

`staticfiles`を指定して`python manage.py collectstatic`を実行すると新規にstaticfilesフォルダを作成してその中に静的なファイルを集めます。本番サーバーにはstaticフォルダではなく、staticfilesをデプロイします。

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

--------------------------------------------------------          ここまで説明                   --------------------------------------------------------

## wsgi.pyの編集

wsgi.pyの編集

```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')

application = get_wsgi_application()
```

### collectstaticの実行

全てのアプリケーションにある静的ファイルを自動で一箇所に集めてくれます。

```
python manage.py collectstatic
```

### gitコマンド実行

```
git add .
```

```
git commit
```



## Herokuアカウント

### Heroku CLIをインストール

1. MAC の場合
   Home brewでインストールします。

   HomebrewはMACのパッケージマネージャーです。
   
   これをインストールしておけばPythonも複数のバージョンをインストールできるようになります。

   
   
まずはHome brewをインストールします。
   
   https://brew.sh/index_ja
   
Homebrewのページからインストールのところに表示されているコードをターミナルで実行します。
   
```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   
   Homebrewがインストールされたら以下コマンドでHeroku CLIをインストールします。
   
   ```
   brew install heroku/brew/heroku
   ```
   
   
   
2. Windowsの場合
   次のURLのページからWindows用のインストーラーをダウンロードしてインストールします。
   インストーラーのチェックはそのままチェックが入った状態でNextボタンで進みインストールします。

   https://devcenter.heroku.com/articles/heroku-cli

ここでパワーシェルまたはターミナルを再起動

### Herokuにログイン

1. 次にこのコマンドを実行して、自分のコンピュータでHerokuアカウントを認証します。

```
heroku login
```

2. heroku: Press any key to open up the browser to login or q to exit: 
   と表示されるので何かキーを押すとHerokuのページが立ち上がりますので認証します。



## Webアプリケーション名をつける

1. 名前を考えたら次のコマンドを実行します。

```
heroku create todo-lesson
```

2. HEROKUに名前を任せる場合は次のコマンド

```
heroku create
```

 

## Herokuにデプロイ準備

1. ログインしたHEROKUページから該当アプリを選択
2. ダッシュボードのsettingタブを選択
3. Config Varsを選択
4. キーに　`DISABLE_COLLECTSTATIC`  をセット
5. 値に `1` をセット
6. Addボタンをクリック

## PostgreSQLの準備

1. Herokuのダッシュボードに入ります。
2. グローバルナビの「Overview」を選択します。
3. 「Installed add-ons」が左側にあります。
4. 「Installed add-ons」のConfigure Add-onsを選択します。
5. Add-onsのサーチボックスにPostgresと入力すると「Heroku Postgres」が表示されるので選択します。
6. 出てきたBoxでplan nameがにHobby Dev となってFreeとなっていることを確認します。
7. Submit Order Formをクリック
8. グローバルナビの「Setting」を確認します。
9. Config Varsのところにある「Reveal Config Vars」をクリックします。
10. DATABASE_URLにPostgreSQLの情報が入っていることを確認します。

#### DATABASE_URLの見方

DATABASE_URLに入っている値がデータベースの設定情報になります。

```
postgres://ユーザ名:パスワード@ホスト名:5432/データベース名
```

実例は次のようになります。（*は実際は半角英数記号など）

```
postgres://wclj***********:00e***********************************************************@ec2-*********************.amazonaws.com:5432/d2h*********lsl
```

この情報をsettins,pyで指定したDATABASESのdj_database_url.config()が読み取ってくれる仕組みです。

```
DATABASES = {'default': dj_database_url.config()}
```

### SECRET_KEYの設定

HerokuのダッシュボードのsettingでConfig Varsを選択してSECRET_KEYの設定を行います。

1. KEYに`SECRET_KEY_TODO`と記述
2. VALUEにシークレットキーの値を貼り付けます。値はクオートで囲みます。

## Herokuへデプロイ

デプロイにはGitのpushを使います。

1. `heroku create` コマンドを実行したときに、あなたのリポジトリにHerokuのリモートサーバーが自動的に追加されています。

2. 次のコマンドを実行してpushする先をgitに登録

```
heroku git:remote -a アプリ名
```

3. Herokuにデプロイコマンド
   **Pushする前にaddとcommitやらないとダメ！**

```
git push heroku master
```

現在、自分がチェックアウトして作業しているブランチがmaster以外で、たとえばmainブランチで作業している場合は、次のコマンドをいれる。

```
pushを実行するコマンド
git push heroku main:master
```

以下のエラーが出た場合、ネットの環境の問題があるかもしれません。

授業終了後に再度試してください。

```
fatal: failed to read object 857180863aa54867afc63211abf7fb25b134a600: Interrupted system call
fatal: the remote end hung up unexpectedly
fatal: the remote end hung up unexpectedly
fatal: the remote end hung up unexpectedly
error: failed to push some refs to 'https://git.heroku.com/todo-lesson2.git'
```

一度の転送量を増やす設定にすると解決するかもしれません。

```
git config http.postBuffer 10485760
```

### Heroku上でmigrateが必要

1. データベースの設定が終了したら、migrateします。

```
heroku run python manage.py migrate
```

### superuserの作成

1. superuserは次のコマンドです。

```
heroku run python manage.py createsuperuser
```

名前、パスワードを事前に準備しておきましょう。メールアドレスは何も入力せずに通ります。

