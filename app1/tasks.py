from project.celery import app

@app.task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done'