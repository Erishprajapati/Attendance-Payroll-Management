from datetime import date
from rest_framework import serializers
LEAVE_VALIDATION_RULES = {
    "annual":    {"min_notice_days": 7,  "allow_past_start": False, "max_backdate_days": 0},
    "sick":      {"min_notice_days": 0,  "allow_past_start": True,  "max_backdate_days": 7},
    "casual":    {"min_notice_days": 1,  "allow_past_start": False, "max_backdate_days": 0},
    "maternity": {"min_notice_days": 30, "allow_past_start": True,  "max_backdate_days": 365},
    "paternity": {"min_notice_days": 14, "allow_past_start": False, "max_backdate_days": 0},
    "unpaid":    {"min_notice_days": 30, "allow_past_start": False, "max_backdate_days": 0},
}
