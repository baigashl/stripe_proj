# stripe project


### Запускаем проект локально
- клонируем репозиторий:
- `git clone https://github.com/baigashl/stripe_proj.git`



- заходим в проект:
- `cd stripe_proj`


- запускаем с помощью docker:
- `sudo docker-compose up -d --build`



- создаем суперюзера и делаем миграции:
- `sudo docker-compose exec backend bash`
- `cd backend`
- `python manage.py migrate`
- `python manage.py createsuperuser`



- переходим по ссылке (админ панель):
- http://localhost/admin/

- я сделал запросы динамичными, иными словами можно через админку создать item и в url указать item id:
- переходим по ссылке (checkout session) url:
- http://localhost/item/1



### На удаленном сервере
- ссылка на проект на удаленном сервере aws:
- http://34.202.69.254/item/1/


- домен может не работать на момент вашей проверки так как я поменял доменное имя и изменение может занять 24 часа
- ссылка на удаленный сервер aws по домену:
- http://baigashl.online/item/1/


- Я изучил AWS, так же на сервере я настроил nginx, на это ушло больше времени чем я расчитывал и не успел дополнить функционал в самом проекте.
