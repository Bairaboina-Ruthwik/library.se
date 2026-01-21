# TRACEABILITY MATRIX

Traceability links user stories to implemented code, unit tests, and release tags.  
This ensures that every requirement is implemented, tested, and delivered sprint-wise.

| User Story | Sprint | Feature Implemented | Code Reference | Test Case | Git Tag |
|-----------|--------|--------------------|---------------|-----------|--------|
| Add book to library | Sprint 1 | add_book() | src/library.py | test_add_book_success | v0.1 |
| Prevent duplicate book ID | Sprint 1 | add_book() validation | src/library.py | test_add_duplicate_book | v0.1 |
| Borrow available book | Sprint 2 | borrow_book() | src/library.py | test_borrow_available_book | v0.2 |
| Prevent borrowing borrowed book | Sprint 2 | borrow_book() validation | src/library.py | test_borrow_unavailable_book | v0.2 |
| Return borrowed book | Sprint 2 | return_book() | src/library.py | test_return_book | v0.2 |
| Generate library report | Sprint 3 | generate_report() | src/library.py | test_report_contains_header | v0.3 |
| Report contains book data | Sprint 3 | generate_report() | src/library.py | test_report_contains_book | v0.3 |
