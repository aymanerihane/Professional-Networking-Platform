from django.db import models
from django.contrib.auth.models import User as auth_user
import json

class Cv(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(auth_user,on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    languages = models.CharField(max_length=100,blank=True)
    skills = models.CharField(max_length=100,blank=True)
    experiences = models.JSONField(blank=True, default=list)  # Use a list to store multiple experiences
    educations = models.JSONField(blank=True, default=list)  # Use a list to store multiple educations

    def add_experience(self, company, job_title, start_date, end_date, description):
        print("###################")
        print("add experience")
        print(company)
        # Add a new experience to the list of experiences
        new_experience = {
            'id': len(self.experiences)+1,
            'company': company,
            'job_title': job_title,
            'start_date': start_date,
            'end_date': end_date,
            'description': description,
        }
        self.experiences.append(new_experience)
        self.save()
        print("experience added")

    def add_education(self, school, degree, start_dateE, end_dateE):
        # Add a new education to the list of educations
        new_education = {
            'id': len(self.educations)+1,
            'school': school,
            'degree': degree,
            'start_date': start_dateE,
            'end_date': end_dateE,
        }
        self.educations.append(new_education)
        self.save()

#detete
        
    def delete_experience(self, id):
        # Delete an experience from the list of experiences
        for experience in self.experiences:
            if experience['id'] == id:
                self.experiences.remove(experience)
                self.save()
                break

    def delete_education(self, id):
        # Delete an education from the list of educations
        for education in self.educations:
            if education['id'] == id:
                self.educations.remove(education)
                self.save()
                break

    def delete_skills(self,skil):
        # Load the list of skills from the JSON string
        skills = json.loads(self.skills)

        # Try to remove the specified skill from the list
        if skil in skills:
            skills.remove(skil)

        # Convert the list back to a JSON string and save it
        self.skills = json.dumps(skills)
        self.save()

    def delete_languages(self, lang):
        # Load the list of languages from the JSON string
        languages = json.loads(self.languages)

        # Try to remove the specified language from the list
        if lang in languages:
            languages.remove(lang)

        # Convert the list back to a JSON string and save it
        self.languages = json.dumps(languages)
        self.save()

 #update
    def update_etud(self, id, school, degree, start_dateE, end_dateE):
        # Update an education in the list of educations
        for education in self.educations:
            if education['id'] == id:
                education['school'] = school
                education['degree'] = degree
                education['start_dateE'] = start_dateE
                education['end_dateE'] = end_dateE
                self.save()
                break
    
    def update_exp(self, id, company, job_title, start_date, end_date, description):
        # Update an experience in the list of experiences
        for experience in self.experiences:
            if experience['id'] == id:
                experience['company'] = company
                experience['job_title'] = job_title
                experience['start_date'] = start_date
                experience['end_date'] = end_date
                experience['description'] = description
                self.save()
                break

    @classmethod
    def skills_tojson(self, skills):
        # split skills by , and make it as json
        new_skills = skills.split(",")
        skill = json.dumps(new_skills)
        return skill
    
    def add_skills(self, skills):
        # Add skills to the list of skills
        self.skills = self.skills.split("]")[0]
        print("skills: ",skills)
        skills = self.skills_tojson(skills)
        skills = skills.split("[")[1]
        print("skills: ",skills)
        skills = skills.split("]")[0]
        print("skills: ",skills)
        self.skills += ","+skills+"]"
        self.save()
    
    @classmethod
    def languages_tojson(self, languages):
        # split languages by , and make it as json
        new_languages = languages.split(",")
        lang = json.dumps(new_languages)
        return lang
    
    def add_languages(self, languages):
        # Add languages to the list of languages
        self.languages = self.languages.split("]")[0]
        languages = self.languages_tojson(languages)
        languages = languages.split("[")[1]
        languages = languages.split("]")[0]
        self.languages += ","+languages+"]"
        self.save()
    
    def get_experiences(self):
        # Récupère toutes les expériences associées à ce CV
        return self.experiences

    def get_educations(self):
        # Récupère toutes les éducations associées à ce CV
        return self.educations