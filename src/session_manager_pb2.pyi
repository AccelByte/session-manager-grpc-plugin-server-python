from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DSStatusChanged: Action
None: Action
SessionCreated: Action
SessionDeleted: Action
SessionInviteCancelled: Action
SessionInviteTimeout: Action
SessionLeaderPromoted: Action
SessionMembersChanged: Action
SessionStorageUpdated: Action
SessionSync: Action
SessionUpdated: Action
SessionUserConnected: Action
SessionUserDisconnected: Action
SessionUserDropped: Action
SessionUserInvited: Action
SessionUserJoined: Action
SessionUserKicked: Action
SessionUserLeave: Action
SessionUserRejected: Action

class BaseSession(_message.Message):
    __slots__ = ["attributes", "configuration", "configuration_name", "created_at", "created_by", "expired_at", "id", "is_active", "is_full", "leader_id", "members", "namespace", "storages", "updated_at", "version"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_FIELD_NUMBER: _ClassVar[int]
    LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    STORAGES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    attributes: _struct_pb2.Struct
    configuration: Configuration
    configuration_name: str
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    expired_at: _timestamp_pb2.Timestamp
    id: str
    is_active: bool
    is_full: bool
    leader_id: str
    members: _containers.RepeatedCompositeFieldContainer[User]
    namespace: str
    storages: _struct_pb2.Struct
    updated_at: _timestamp_pb2.Timestamp
    version: int
    def __init__(self, is_active: bool = ..., is_full: bool = ..., version: _Optional[int] = ..., id: _Optional[str] = ..., namespace: _Optional[str] = ..., created_by: _Optional[str] = ..., configuration_name: _Optional[str] = ..., leader_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expired_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., storages: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., configuration: _Optional[_Union[Configuration, _Mapping]] = ..., members: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class Configuration(_message.Message):
    __slots__ = ["attributes", "auto_join", "disable_resend_invite", "inactive_timeout", "invite_timeout", "joinability", "leader_election_grace_period", "max_players", "min_players", "persistent", "text_chat", "type"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    AUTO_JOIN_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RESEND_INVITE_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    INVITE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    JOINABILITY_FIELD_NUMBER: _ClassVar[int]
    LEADER_ELECTION_GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MAX_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    MIN_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    TEXT_CHAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attributes: _struct_pb2.Struct
    auto_join: bool
    disable_resend_invite: bool
    inactive_timeout: int
    invite_timeout: int
    joinability: str
    leader_election_grace_period: int
    max_players: int
    min_players: int
    persistent: bool
    text_chat: bool
    type: str
    def __init__(self, attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., auto_join: bool = ..., inactive_timeout: _Optional[int] = ..., invite_timeout: _Optional[int] = ..., joinability: _Optional[str] = ..., leader_election_grace_period: _Optional[int] = ..., max_players: _Optional[int] = ..., min_players: _Optional[int] = ..., persistent: bool = ..., text_chat: bool = ..., disable_resend_invite: bool = ..., type: _Optional[str] = ...) -> None: ...

class DSInformation(_message.Message):
    __slots__ = ["requested_at", "status", "status_v2"]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_V2_FIELD_NUMBER: _ClassVar[int]
    requested_at: _timestamp_pb2.Timestamp
    status: str
    status_v2: str
    def __init__(self, requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[str] = ..., status_v2: _Optional[str] = ...) -> None: ...

class GameSession(_message.Message):
    __slots__ = ["backfill_ticket_id", "code", "ds_information", "match_pool", "processing_time", "retry", "secret", "server_name", "session", "step", "teams", "ticket_ids"]
    BACKFILL_TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DS_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    MATCH_POOL_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    TICKET_IDS_FIELD_NUMBER: _ClassVar[int]
    backfill_ticket_id: str
    code: str
    ds_information: DSInformation
    match_pool: str
    processing_time: int
    retry: int
    secret: str
    server_name: str
    session: BaseSession
    step: str
    teams: _containers.RepeatedCompositeFieldContainer[Team]
    ticket_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, retry: _Optional[int] = ..., processing_time: _Optional[int] = ..., match_pool: _Optional[str] = ..., backfill_ticket_id: _Optional[str] = ..., server_name: _Optional[str] = ..., step: _Optional[str] = ..., code: _Optional[str] = ..., ticket_ids: _Optional[_Iterable[str]] = ..., ds_information: _Optional[_Union[DSInformation, _Mapping]] = ..., session: _Optional[_Union[BaseSession, _Mapping]] = ..., teams: _Optional[_Iterable[_Union[Team, _Mapping]]] = ..., secret: _Optional[str] = ...) -> None: ...

class PartyCreatedRequest(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: PartySession
    def __init__(self, session: _Optional[_Union[PartySession, _Mapping]] = ...) -> None: ...

class PartyDeletedRequest(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: PartySession
    def __init__(self, session: _Optional[_Union[PartySession, _Mapping]] = ...) -> None: ...

class PartyMember(_message.Message):
    __slots__ = ["party_id", "user_ids"]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, party_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PartyResponse(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: PartySession
    def __init__(self, session: _Optional[_Union[PartySession, _Mapping]] = ...) -> None: ...

class PartySession(_message.Message):
    __slots__ = ["code", "session"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    code: str
    session: BaseSession
    def __init__(self, session: _Optional[_Union[BaseSession, _Mapping]] = ..., code: _Optional[str] = ...) -> None: ...

class PartyUpdatedRequest(_message.Message):
    __slots__ = ["action", "session_new", "session_old"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SESSION_NEW_FIELD_NUMBER: _ClassVar[int]
    SESSION_OLD_FIELD_NUMBER: _ClassVar[int]
    action: Action
    session_new: PartySession
    session_old: PartySession
    def __init__(self, session_old: _Optional[_Union[PartySession, _Mapping]] = ..., session_new: _Optional[_Union[PartySession, _Mapping]] = ..., action: _Optional[_Union[Action, str]] = ...) -> None: ...

class SessionCreatedRequest(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: GameSession
    def __init__(self, session: _Optional[_Union[GameSession, _Mapping]] = ...) -> None: ...

class SessionDeletedRequest(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: GameSession
    def __init__(self, session: _Optional[_Union[GameSession, _Mapping]] = ...) -> None: ...

class SessionResponse(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: GameSession
    def __init__(self, session: _Optional[_Union[GameSession, _Mapping]] = ...) -> None: ...

class SessionUpdatedRequest(_message.Message):
    __slots__ = ["action", "session_new", "session_old"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SESSION_NEW_FIELD_NUMBER: _ClassVar[int]
    SESSION_OLD_FIELD_NUMBER: _ClassVar[int]
    action: Action
    session_new: GameSession
    session_old: GameSession
    def __init__(self, session_old: _Optional[_Union[GameSession, _Mapping]] = ..., session_new: _Optional[_Union[GameSession, _Mapping]] = ..., action: _Optional[_Union[Action, str]] = ...) -> None: ...

class Team(_message.Message):
    __slots__ = ["party_members", "team_id", "user_ids"]
    PARTY_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    party_members: _containers.RepeatedCompositeFieldContainer[PartyMember]
    team_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., party_members: _Optional[_Iterable[_Union[PartyMember, _Mapping]]] = ..., team_id: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["id", "platform_id", "platform_user_id", "previous_status", "status", "status_v2", "updated_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_V2_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    platform_id: str
    platform_user_id: str
    previous_status: str
    status: str
    status_v2: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., status: _Optional[str] = ..., status_v2: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., platform_id: _Optional[str] = ..., platform_user_id: _Optional[str] = ..., previous_status: _Optional[str] = ...) -> None: ...

class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
