from django.db import models
from django.contrib.auth.models import User as auth_user
import json

class Cv(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(auth_user,on_delete=models.CASCADE)
    introduction = models.CharField(max_length=100,blank=True)
    languages = models.CharField(max_length=100,blank=True)
    skills = models.CharField(max_length=100,blank=True)
    experiences = models.JSONField(blank=True, default=list)  # Use a list to store multiple experiences
    educations = models.JSONField(blank=True, default=list)  # Use a list to store multiple educations

    def add_experience(self, company, job_title, start_date, end_date, description):
        # Add a new experience to the list of experiences
        new_experience = {
            'company': company,
            'job_title': job_title,
            'start_date': start_date,
            'end_date': end_date,
            'description': description,
        }
        self.experiences.append(new_experience)
        self.save()

    def add_education(self, school, degree, start_dateE, end_dateE):
        # Add a new education to the list of educations
        new_education = {
            'school': school,
            'degree': degree,
            'start_date': start_dateE,
            'end_date': end_dateE,
        }
        self.educations.append(new_education)
        self.save()

    @classmethod
    def skills_tojson(self, skills):
        # split skills by , and make it as json
        new_skills = skills.split(",")
        skill = json.dumps(new_skills)
        return skill
    
    @classmethod
    def languages_tojson(self, languages):
        # split languages by , and make it as json
        new_languages = languages.split(",")
        lang = json.dumps(new_languages)
        return lang
    
    def get_experiences(self):
        # Récupère toutes les expériences associées à ce CV
        return self.experiences

    def get_educations(self):
        # Récupère toutes les éducations associées à ce CV
        return self.educations