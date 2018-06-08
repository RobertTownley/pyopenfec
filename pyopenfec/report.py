from . import utils
from datetime import datetime
from pytz import timezone


class Report(utils.PyOpenFecApiPaginatedClass):

    def __init__(self, **kwargs):
        self.aggregate_amount_personal_contributions_general = None
        self.aggregate_contributions_personal_funds_primary = None
        self.all_loans_received_period = None
        self.all_loans_received_ytd = None
        self.all_other_loans_period = None
        self.all_other_loans_ytd = None
        self.allocated_federal_election_levin_share_period = None
        self.amendment_chain = None
        self.amendment_indicator = None
        self.amendment_indicator_full = None
        self.beginning_image_number = None
        self.calendar_ytd = None
        self.candidate_contribution_period = None
        self.candidate_contribution_ytd = None
        self.cash_on_hand_beginning_calendar_ytd = None
        self.cash_on_hand_beginning_period = None
        self.cash_on_hand_close_ytd = None
        self.cash_on_hand_end_period = None
        self.committee_id = None
        self.committee_name = None
        self.committee_type = None
        self.coordinated_expenditures_by_party_committee_period = None
        self.coordinated_expenditures_by_party_committee_ytd = None
        self.coverage_end_date = None
        self.coverage_start_date = None
        self.csv_url = None
        self.cycle = None
        self.debts_owed_by_committee = None
        self.debts_owed_to_committee = None
        self.document_description = None
        self.end_image_number = None
        self.exempt_legal_accounting_disbursement_period = None
        self.exempt_legal_accounting_disbursement_ytd = None
        self.expenditure_subject_to_limits = None
        self.fec_file_id = None
        self.fec_url = None
        self.fed_candidate_committee_contribution_refunds_ytd = None
        self.fed_candidate_committee_contributions_period = None
        self.fed_candidate_committee_contributions_ytd = None
        self.fed_candidate_contribution_refunds_period = None
        self.federal_funds_period = None
        self.federal_funds_ytd = None
        self.file_number = None
        self.fundraising_disbursements_period = None
        self.fundraising_disbursements_ytd = None
        self.gross_receipt_authorized_committee_general = None
        self.gross_receipt_authorized_committee_primary = None
        self.gross_receipt_minus_personal_contribution_general = None
        self.gross_receipt_minus_personal_contributions_primary = None
        self.html_url = None
        self.independent_contributions_period = None
        self.independent_expenditures_period = None
        self.independent_expenditures_ytd = None
        self.individual_itemized_contributions_period = None
        self.individual_itemized_contributions_ytd = None
        self.individual_unitemized_contributions_period = None
        self.individual_unitemized_contributions_ytd = None
        self.is_amended = None
        self.items_on_hand_liquidated = None
        self.loan_repayments_candidate_loans_period = None
        self.loan_repayments_candidate_loans_ytd = None
        self.loan_repayments_made_period = None
        self.loan_repayments_made_ytd = None
        self.loan_repayments_other_loans_period = None
        self.loan_repayments_other_loans_ytd = None
        self.loan_repayments_received_period = None
        self.loan_repayments_received_ytd = None
        self.loans_made_by_candidate_period = None
        self.loans_made_by_candidate_ytd = None
        self.loans_made_period = None
        self.loans_made_ytd = None
        self.loans_received_from_candidate_period = None
        self.loans_received_from_candidate_ytd = None
        self.means_filed = None
        self.most_recent = None
        self.most_recent_file_number = None
        self.net_contributions_cycle_to_date = None
        self.net_contributions_period = None
        self.net_contributions_ytd = None
        self.net_operating_expenditures_cycle_to_date = None
        self.net_operating_expenditures_period = None
        self.net_operating_expenditures_ytd = None
        self.non_allocated_fed_election_activity_period = None
        self.non_allocated_fed_election_activity_ytd = None
        self.nonfed_share_allocated_disbursements_period = None
        self.offsets_to_fundraising_expenditures_period = None
        self.offsets_to_fundraising_expenditures_ytd = None
        self.offsets_to_legal_accounting_period = None
        self.offsets_to_legal_accounting_ytd = None
        self.offsets_to_operating_expenditures_period = None
        self.offsets_to_operating_expenditures_ytd = None
        self.operating_expenditures_period = None
        self.operating_expenditures_ytd = None
        self.other_disbursements_period = None
        self.other_disbursements_ytd = None
        self.other_fed_operating_expenditures_period = None
        self.other_fed_operating_expenditures_ytd = None
        self.other_fed_receipts_period = None
        self.other_fed_receipts_ytd = None
        self.other_loans_received_period = None
        self.other_loans_received_ytd = None
        self.other_political_committee_contributions_period = None
        self.other_political_committee_contributions_ytd = None
        self.other_receipts_period = None
        self.other_receipts_ytd = None
        self.pdf_url = None
        self.political_party_committee_contributions_period = None
        self.political_party_committee_contributions_ytd = None
        self.previous_file_number = None
        self.receipt_date = None
        self.refunded_individual_contributions_period = None
        self.refunded_individual_contributions_ytd = None
        self.refunded_other_political_committee_contributions_period = None
        self.refunded_other_political_committee_contributions_ytd = None
        self.refunded_political_party_committee_contributions_period = None
        self.refunded_political_party_committee_contributions_ytd = None
        self.refunds_total_contributions_col_total_ytd = None
        self.repayments_loans_made_by_candidate_period = None
        self.repayments_loans_made_candidate_ytd = None
        self.repayments_other_loans_period = None
        self.repayments_other_loans_ytd = None
        self.report_form = None
        self.report_type = None
        self.report_type_full = None
        self.report_year = None
        self.shared_fed_activity_nonfed_ytd = None
        self.shared_fed_activity_period = None
        self.shared_fed_activity_ytd = None
        self.shared_fed_operating_expenditures_period = None
        self.shared_fed_operating_expenditures_ytd = None
        self.shared_nonfed_operating_expenditures_period = None
        self.shared_nonfed_operating_expenditures_ytd = None
        self.subtotal_period = None
        self.subtotal_summary_page_period = None
        self.subtotal_summary_period = None
        self.subtotal_summary_ytd = None
        self.total_contribution_refunds_col_total_period = None
        self.total_contribution_refunds_period = None
        self.total_contribution_refunds_ytd = None
        self.total_contributions_column_total_period = None
        self.total_contributions_period = None
        self.total_contributions_ytd = None
        self.total_disbursements_period = None
        self.total_disbursements_ytd = None
        self.total_fed_disbursements_period = None
        self.total_fed_disbursements_ytd = None
        self.total_fed_election_activity_period = None
        self.total_fed_election_activity_ytd = None
        self.total_fed_operating_expenditures_period = None
        self.total_fed_operating_expenditures_ytd = None
        self.total_fed_receipts_period = None
        self.total_fed_receipts_ytd = None
        self.total_individual_contributions_period = None
        self.total_individual_contributions_ytd = None
        self.total_loan_repayments_made_period = None
        self.total_loan_repayments_made_ytd = None
        self.total_loans_received_period = None
        self.total_loans_received_ytd = None
        self.total_nonfed_transfers_period = None
        self.total_nonfed_transfers_ytd = None
        self.total_offsets_to_operating_expenditures_period = None
        self.total_offsets_to_operating_expenditures_ytd = None
        self.total_operating_expenditures_period = None
        self.total_operating_expenditures_ytd = None
        self.total_period = None
        self.total_receipts_period = None
        self.total_receipts_ytd = None
        self.total_ytd = None
        self.transfers_from_affiliated_committee_period = None
        self.transfers_from_affiliated_committee_ytd = None
        self.transfers_from_affiliated_party_period = None
        self.transfers_from_affiliated_party_ytd = None
        self.transfers_from_nonfed_account_period = None
        self.transfers_from_nonfed_account_ytd = None
        self.transfers_from_nonfed_levin_period = None
        self.transfers_from_nonfed_levin_ytd = None
        self.transfers_from_other_authorized_committee_period = None
        self.transfers_from_other_authorized_committee_ytd = None
        self.transfers_to_affiliated_committee_period = None
        self.transfers_to_affilitated_committees_ytd = None
        self.transfers_to_other_authorized_committee_period = None
        self.transfers_to_other_authorized_committee_ytd = None

        eastern = timezone('US/Eastern')
        date_fields = {
            'coverage_end_date': '%Y-%m-%dT%H:%M:%S+00:00',
            'coverage_start_date': '%Y-%m-%dT%H:%M:%S+00:00',
            'receipt_date': '%Y-%m-%dT%H:%M:%S',
            }

        for k, v in kwargs.items():
            if k in date_fields:
                parsed_date = datetime.strptime(v, date_fields[k])
                tz_aware = eastern.localize(parsed_date)
                setattr(self, k, tz_aware)
                continue
            setattr(self, k, v)

    def __unicode__(self):
        return unicode("{cid} {rtf} ({c} cycle, {csd}-{ced})".format(
            cid=self.committee_id,
            rtf=self.report_type_full,
            c=self.cycle,
            csd=self.coverage_start_date,
            ced=self.coverage_end_date
        ))

    def __str__(self):
        return repr("{cid} {rtf} ({c} cycle, {csd}-{ced})".format(
            cid=self.committee_id,
            rtf=self.report_type_full,
            c=self.cycle,
            csd=self.coverage_start_date,
            ced=self.coverage_end_date
        ))
