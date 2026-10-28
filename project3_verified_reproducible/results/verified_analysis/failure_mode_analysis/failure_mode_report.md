# Failure-Mode Analysis (Official Verifier Evidence)

This analysis reads existing official verifier logs only. It does not make new model calls.

## Preliminary category counts

| Failure mode | Evidence rows |
|---|---:|
| Content missing / requirement not met | 154 |
| File format / structure | 22 |

## Interpretation rule

These categories are rule-based preliminary labels. Representative evidence should be manually checked using `manual_audit_checklist.csv` before making claims in the report.

## Representative evidence

### Content missing / requirement not met
- Task: `court-form-filling`
- Test/error: `../verifier/test_outputs.py::TestPDFValid::test_output_file_valid - Fai...`
- Evidence: ERROR ../verifier/test_outputs.py::TestPDFValid::test_output_file_valid - Fai... ERROR ../verifier/test_outputs.py::TestRequiredContent::test_content_present[plaintiff_name] ERROR ../verifier/test_outputs.py::TestRequiredContent::test_content_present[plaintiff_address] ERROR ../verifier/test_outputs.py::TestRequiredContent::test_content_present[plaintiff_city] ERROR ../verifier/test_outputs.py::TestRequiredContent::test_content_present[plaintiff_zip] ERROR ../verifier/test_outputs.py::TestRequiredContent::test_content_present[plaintiff_phone] ERROR ../verifier/test_outputs.py::TestRequiredContent::test_content_present[plaintiff_email] ERROR .

### File format / structure
- Task: `dialogue-parser`
- Test/error: `../verifier/test_outputs.py::test_visualization_validity[shapes] - Ass...`
- Evidence: FAILED ../verifier/test_outputs.py::test_visualization_validity[shapes] - Ass... FAILED ../verifier/test_outputs.py::test_content_integrity[node_text-StrangerMoreInfo-Back so soon? Afraid?] FAILED ../verifier/test_outputs.py::test_content_integrity[node_text-MerchantShame-I light a candle for each of them] FAILED ../verifier/test_outputs.py::test_content_integrity[node_text-KiraWarning-She's never failed a contract] FAILED ../verifier/test_outputs.py::test_content_integrity[dynamic_script_sample-script.txt-None] FAILED ../verifier/test_outputs.py::test_structural_integrity[Start-TavernEntry] FAILED ../verifier/test_outputs.py::test_structural

