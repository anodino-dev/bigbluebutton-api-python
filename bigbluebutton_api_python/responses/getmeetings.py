from typing import Iterable
from .base import BaseResponse
from ..core.meeting import Meeting

class GetMeetingsResponse(BaseResponse):
    def get_meetings(self):
        meetings = []

        try:
            if self.get_message_key() == "noMeetings":
                return []
        except KeyError:
            pass

        meetingsXml = self.get_field("meetings")["meeting"]
        if not isinstance(meetingsXml, Iterable):
            meetingsXml = [meetingsXml]
        for meetingXml in meetingsXml:
            meetings.append(Meeting(meetingXml))
        return meetings