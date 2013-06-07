def get_user_quota(user):
    from plans.models import PlanQuota
    quota_dic = {}
    for plan_quota in PlanQuota.objects.filter(plan__userplan__user=user).select_related('quota'):
        quota_dic[plan_quota.quota.codename] = plan_quota.value
    return quota_dic
