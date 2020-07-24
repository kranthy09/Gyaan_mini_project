from django.db import models


class Domain(models.Model):

    domain_name = models.CharField(max_length=200)
    domain_description = models.CharField(max_length=500)


class DomainExperts(models.Model):

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    domain_expert_id = models.IntegerField()


class DomainRequests(models.Model):

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    requested_by = models.IntegerField()
    is_approved = models.BooleanField(default=False)


class DomainPost(models.Model):

    user_id = models.IntegerField()
    post_id = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)


class DomainTag(models.Model):

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    tag_id = models.IntegerField()
