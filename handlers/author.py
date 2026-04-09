"""
handlers/author.py
------------------
Handles the Author Information form submission.
"""

import datetime
import state


def safe_date_parse(val) -> datetime.date:
    """Parse a date from various input formats."""
    if val is None or val == "":
        raise ValueError("Date is required (YYYY-MM-DD).")
    if isinstance(val, datetime.date):
        return val
    try:
        return datetime.date.fromisoformat(str(val))
    except Exception:
        from dateutil import parser
        return parser.parse(str(val)).date()


def submit_author(
    title: str,
    keywords: str,
    description: str,
    uploader: str,
    email: str,
    date: str,
    identifier: str,
    contributors: str,
) -> tuple[str, dict]:
    """
    Validate and store author metadata.

    Returns
    -------
    (status_message, author_dict)
    """
    try:
        parsed_date = safe_date_parse(date)
        state.author_data.update(
            {
                "title": title,
                "keywords_comma_sperated": keywords,
                "description": description,
                "uploaded_by": uploader,
                "email": email,
                "date": parsed_date.isoformat(),
                "identifier": identifier,
                "contributors": contributors or "",
            }
        )
        return "✅ Author data submitted successfully!", dict(state.author_data)
    except Exception as exc:
        return f"❌ Error submitting author data: {type(exc).__name__}: {exc}", {}
