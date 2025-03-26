from django.db import models



    



class Application(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)  # Optional cover letter field
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application from {self.applicant_name} for {self.job_post.title}"
