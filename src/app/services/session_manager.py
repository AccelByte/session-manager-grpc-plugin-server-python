# Copyright (c) 2025 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

from logging import Logger
from typing import Any, Optional

from accelbyte_py_sdk import AccelByteSDK

from google.protobuf.json_format import MessageToJson

from google.protobuf.empty_pb2 import Empty
from google.protobuf.struct_pb2 import Struct

from ..proto.session_manager_pb2 import (
    DESCRIPTOR,
    BaseSession,
    GameSession,
    PartySession,
    PartyCreatedRequest,
    PartyDeletedRequest,
    PartyUpdatedRequest,
    PartyResponse,
    SessionCreatedRequest,
    SessionDeletedRequest,
    SessionUpdatedRequest,
    SessionResponse,
)
from ..proto.session_manager_pb2_grpc import SessionManagerServicer


class AsyncSessionManager(SessionManagerServicer):
    full_name: str = DESCRIPTOR.services_by_name["SessionManager"].full_name

    def __init__(self, sdk: Optional[AccelByteSDK] = None, logger: Optional[Logger] = None, **kwargs) -> None:
        self.sdk = sdk
        self.logger = logger

    async def OnPartyCreated(self, request: PartyCreatedRequest, context: Any) -> PartyResponse:
        self.logger.info("got message from OnPartyCreated")
        self.logger.info(f"party session: {MessageToJson(request.session)}")

        response = PartyResponse()

        if request.HasField("session"):
            response.session.CopyFrom(request.session)

        response.session.session.attributes.update({"PARTY_SAMPLE": "party value from gRPC server"})

        return response

    async def OnPartyDeleted(self, request: PartyDeletedRequest, context: Any) -> Empty:
        self.logger.info("got message from OnPartyDeleted")
        self.logger.info(f"party deleted: {MessageToJson(request.session)}")
        return Empty()

    async def OnPartyUpdated(self, request: PartyUpdatedRequest, context: Any) -> Empty:
        self.logger.info("got message from OnPartyUpdated")
        self.logger.info(f"old party session: {MessageToJson(request.session_old)}")
        self.logger.info(f"new party session: {MessageToJson(request.session_new)}")
        return Empty()

    async def OnSessionCreated(self, request: SessionCreatedRequest, context: Any) -> SessionResponse:
        self.logger.info("got message from OnSessionCreated")
        self.logger.info(f"game session: {MessageToJson(request.session)}")

        response = SessionResponse()

        if request.HasField("session"):
            response.session.CopyFrom(request.session)

        response.session.session.attributes.update({"SAMPLE": "value from gRPC server"})

        return response

    async def OnSessionDeleted(self, request: SessionDeletedRequest, context: Any) -> Empty:
        self.logger.info("got message from OnSessionDeleted")
        self.logger.info(f"session deleted: {MessageToJson(request.session)}")
        return Empty()

    async def OnSessionUpdated(self, request: SessionUpdatedRequest, context: Any) -> Empty:
        self.logger.info("got message from OnSessionUpdated")
        self.logger.info(f"old game session: {MessageToJson(request.session_old)}")
        self.logger.info(f"new game session: {MessageToJson(request.session_new)}")
        return Empty()
