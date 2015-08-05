from . import utils
from .filing import Filing


class Committee(utils.PyOpenFecApiClass):

    def __init__(self, **kwargs):
        self.candidate_ids = None
        self.committee_id = None
        self.committee_type = None
        self.committee_type_full = None
        self.designation = None
        self.designation_full = None
        self.expire_date = None
        self.first_file_date = None
        self.last_file_date = None
        self.name = None
        self.organization_type = None
        self.organization_type_full = None
        self.party = None
        self.party_full = None
        self.state = None
        self.treasurer_name = None
        self._history = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{name} {id}".format(name=self.name,
                                            id=self.committee_id))

    def __str__(self):
        return repr("{name} {id}".format(name=self.name,
                                         id=self.committee_id))

    @property
    def history(self):
        if self._history is None:
            self._history = {}
            resource_path = 'committee/{cid}/history'.format(cid=self.committee_id)
            for hp in CommitteeHistoryPeriod.fetch(resource=resource_path):
                self._history[hp.cycle] = hp
        return self._history

    def select_filings(self, **kwargs):
        return [f for f in Filing.fetch(committee_id=self.committee_id, **kwargs)]

    def all_filings(self):
        return [f for f in Filing.fetch(committee_id=self.committee_id)]


class CommitteeHistoryPeriod(utils.PyOpenFecApiClass):

    def __init__(self, **kwargs):
        self.city = None
        self.committee_id = None
        self.committee_type = None
        self.committee_type_full = None
        self.cycle = None
        self.cycles = None
        self.designation = None
        self.designation_full = None
        self.expire_date = None
        self.name = None
        self.organization_type = None
        self.organization_type_full = None
        self.party = None
        self.party_full = None
        self.state = None
        self.state_full = None
        self.street_1 = None
        self.street_2 = None
        self.treasurer_name = None
        self.zip = None

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{name} [{comm_id}] ({period})".format(
            name=self.name,
            comm_id=self.committee_id,
            period=self.two_year_period))

    def __str__(self):
        return repr("{name} [{comm_id}] ({period})".format(
            name=self.name,
            comm_id=self.committee_id,
            period=self.two_year_period))
