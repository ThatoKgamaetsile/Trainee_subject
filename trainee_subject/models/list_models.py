from edc_base.model_mixins import BaseUuidModel, ListModelMixin


class Problems(ListModelMixin, BaseUuidModel):



    class Meta(ListModelMixin.Meta):
        app_label = 'trainee_subject'





