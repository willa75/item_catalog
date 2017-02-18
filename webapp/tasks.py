from webapp.extensions import celery
#TODO: make celery work with tasks
@celery.task()
def log(msg):
	return msg