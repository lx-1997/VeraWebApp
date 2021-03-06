from django.utils.translation import ugettext_lazy as _

MESSAGES = {
    'VacancyChange': _('Vacancy status change now pending...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'Not_VacancyChange':
        '<span class="red-text" data-uk-icon="ban"></span>&emsp;To add new pipeline action you have to disable vacancy.',
    'ActionDeleted': _('Action delete now pending...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'NewAction': _(
        'Transaction for add new action now pending...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'Subscribe': _(
        'Transaction for subscribe to vacancy now pending...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'tokenApprove': _('Approving tokens for platform now pending') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'ChangeStatus': _('Changing status now pending...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'NewMember': _('Your new contract now creating...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'NewVacancy': _('Your new vacancy now creating...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'NewCompany': _('New company contract now creating...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
    'MemberSubscribe': _('Vacancy subscribing now pending...') + '&nbsp;<span data-uk-spinner="ratio: 0.5"></span>',
}
