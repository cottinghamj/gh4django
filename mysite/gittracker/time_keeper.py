from django.core.mail import send_mail
from django.utils import timezone
from gittracker.models import FileName
import time


def list2string(old_list):
        transforming_string = ''
        for l in old_list :
                transforming_string += l.__str__()
                transforming_string += '\n'
        return transforming_string


while True:
	sent_email = []
	
	current_time = timezone.now()
	for f in FileName.objects.all():
		time_delta = current_time - f.time_inserted
		#print time_delta.seconds
		if time_delta.seconds > (3600 * 6) and f.owner not in sent_email :
			if "Jessica" in f.owner:
				email_receipient = ['Jessica@grouproots.com']
			elif "Jarian" in f.owner:
				email_receipient = ['Jarian@grouproots.com']
			else :
				email_receipient = ['Jessica@grouproots.com','Jarian@grouproots.com']

			list_of_files_out = list2string(FileName.objects.filter(owner=f.owner))
			print	send_mail('You still have a lock on files','Please make sure that you commit and push your files soon. According to our records, you still have a lock on the following files:\n\n %s. As a reminder, no one else can access these files until you release the lock, so only place a lock on the files you are currently working on. As a rule of thumb, you should work on a max of 3 files. \n\nThanks! \nThe Git Tracker'%(list_of_files_out) , 'admin@grouproots.com',email_receipient, fail_silently=False)
			sent_email.append(f.owner) # Idea is that you don't need to multiple reminder emails to a single person during a cycle of the loop. So we check against this list
	

	time.sleep(3600) # Should delay for an hour (3600 secs) before checking if files still out			

