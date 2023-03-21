python3 -m venv ${가상환경이름} //가상환경 생성
source ${가상환경이름}/bin/activate //가상환경 실행
deactivate //가상환경 종료
pip install django //django 설치
django-admin startproject myproject //myproject생성으로 프로젝트 실행

python manage.py runserver // url들어가면 페이지 하나 생성되어 있음
python manage.py startapp myapp //
myproject/settings.py의 INSTALLED_APPS에 'myapp'적어주기

mkdir templates하고 html파일 만들어주기

views.py에서 연결
