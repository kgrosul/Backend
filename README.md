# Backend

Бэк для дипломной работы "Разработка приложения для мониторинга психоэмоционального состояния человека"

###### Запуск сервера на локальной машине:

```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
cd backend
python3 manage.py runserver

```

###### Доступные сейчас запросы:
```url
/api/doctors: получить всех докторов
/api/users: получить всех пациентов
/api/users?doctor_id=1: получить всех пациентов доктора с таким id
/api/test: получить все тесты
/api/test?with_questions=True: получить все тесты с вопросами
/api/test?with_questions?test_id=1: получить тест с таким id и вопросами к нему
```
