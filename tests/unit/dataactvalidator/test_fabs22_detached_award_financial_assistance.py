from tests.unit.dataactcore.factories.staging import DetachedAwardFinancialAssistanceFactory
from tests.unit.dataactvalidator.utils import number_of_errors, query_columns

_FILE = 'fabs22_detached_award_financial_assistance'


def test_column_headers(database):
    expected_subset = {'row_number', 'correction_delete_indicatr', 'uniqueid_AssistanceTransactionUniqueKey'}
    actual = set(query_columns(_FILE, database))
    assert expected_subset == actual


def test_success(database):
    """ When provided, CorrectionDeleteIndicator must contain one of the following values: C or D. """
    det_award_1 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr='')
    det_award_2 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr=None)
    det_award_3 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr='c')
    det_award_4 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr='D')

    errors = number_of_errors(_FILE, database, models=[det_award_1, det_award_2, det_award_3, det_award_4])
    assert errors == 0


def test_failure(database):
    """ Test failure for when provided, CorrectionDeleteIndicator must contain one of the following values:
        C or D. """
    det_award_1 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr='A')
    det_award_2 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr='Z')
    det_award_3 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr='cd')
    det_award_4 = DetachedAwardFinancialAssistanceFactory(correction_delete_indicatr='L')

    errors = number_of_errors(_FILE, database, models=[det_award_1, det_award_2, det_award_3, det_award_4])
    assert errors == 4
