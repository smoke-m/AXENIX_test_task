# Запуск Redis
redis-server &
REDIS_PID=$!

# Запуск Celery worker
celery -A decent_test worker --loglevel=info &
CELERY_WORKER_PID=$!

# Запуск Celery beat
celery -A decent_test beat --loglevel=info &
CELERY_BEAT_PID=$!

# Функция для завершения всех запущенных процессов
cleanup() {
    kill $REDIS_PID
    kill $CELERY_WORKER_PID
    kill $CELERY_BEAT_PID
}

# Вызов функции cleanup при получении сигнала EXIT
trap cleanup EXIT

# Запуск Django сервера
python manage.py runserver
