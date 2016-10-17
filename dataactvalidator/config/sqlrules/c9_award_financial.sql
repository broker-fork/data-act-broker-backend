SELECT DISTINCT afa.row_number, afa.fain, afa.uri
FROM award_financial_assistance AS afa
WHERE afa.submission_id = {0}
    AND CAST(afa.federal_action_obligation as numeric) > 0
    AND CAST(afa.original_loan_subsidy_cost as numeric) > 0
    AND (
        afa.row_number NOT IN (
            SELECT afa.row_number
            FROM award_financial_assistance AS afa
                JOIN award_financial AS af
                    ON (afa.submission_id = af.submission_id
                        AND (afa.fain IS NOT DISTINCT FROM af.fain
                            AND afa.uri IS NOT DISTINCT FROM af.uri)
                    )
            WHERE CAST(afa.federal_action_obligation as numeric) > 0
                AND CAST(afa.original_loan_subsidy_cost as numeric) > 0
                AND afa.submission_id = {0}
        ) OR (
            afa.fain IS NOT NULL
            AND afa.uri IS NOT NULL
        )
    );