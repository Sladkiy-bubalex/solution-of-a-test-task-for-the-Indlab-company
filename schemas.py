from pydantic import BaseModel
from typing import List, Optional


# Pydantic модели (при необходимости)
class ChannelInfo(BaseModel):
    channel_link: str


class SummarizeRequest(BaseModel):
    filter_name: str
    summary_type: str  # 'last_10' или 'period'
    period_start: Optional[str] = None
    period_end: Optional[str] = None
