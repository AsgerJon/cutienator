"""
Http2 stands for the namespace 'Http2' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class Http2:
  """
  The namespace 'Http2' of Qt, which holds no objects. It holds the 6 enums
  Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class FrameFlag(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'Http2::FrameFlag' of Qt, with the 6 names Qt gives in it.
    Qt names the type of its combinations 'Http2::FrameFlags'. C++ keeps
    these names inside the enum, so the class that holds the enum does not
    have them.
    """

    EMPTY = 0x0
    ACK = 0x1
    END_STREAM = 0x1
    END_HEADERS = 0x4
    PADDED = 0x8
    PRIORITY = 0x20

  FrameFlags = FrameFlag

  class FrameStatus(CuteNum, scoped=True):
    """
    The enum 'Http2::FrameStatus' of Qt, with the 4 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    protocolError = Kee[int](0)
    sizeError = Kee[int](1)
    incompleteFrame = Kee[int](2)
    goodFrame = Kee[int](3)

  class FrameType(CuteNum, scoped=True):
    """
    The enum 'Http2::FrameType' of Qt, with the 11 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    DATA = Kee[int](0)
    HEADERS = Kee[int](1)
    PRIORITY = Kee[int](2)
    RST_STREAM = Kee[int](3)
    SETTINGS = Kee[int](4)
    PUSH_PROMISE = Kee[int](5)
    PING = Kee[int](6)
    GOAWAY = Kee[int](7)
    WINDOW_UPDATE = Kee[int](8)
    CONTINUATION = Kee[int](9)
    LAST_FRAME_TYPE = Kee[int](10)

  class Http2Error(CuteNum):
    """
    The enum 'Http2::Http2Error' of Qt, with the 14 names Qt gives in it.
    """

    HTTP2_NO_ERROR = Kee[int](0)
    PROTOCOL_ERROR = Kee[int](1)
    INTERNAL_ERROR = Kee[int](2)
    FLOW_CONTROL_ERROR = Kee[int](3)
    SETTINGS_TIMEOUT = Kee[int](4)
    STREAM_CLOSED = Kee[int](5)
    FRAME_SIZE_ERROR = Kee[int](6)
    REFUSE_STREAM = Kee[int](7)
    CANCEL = Kee[int](8)
    COMPRESSION_ERROR = Kee[int](9)
    CONNECT_ERROR = Kee[int](10)
    ENHANCE_YOUR_CALM = Kee[int](11)
    INADEQUATE_SECURITY = Kee[int](12)
    HTTP_1_1_REQUIRED = Kee[int](13)

  class Http2PredefinedParameters(CuteNum):
    """
    The enum 'Http2::Http2PredefinedParameters' of Qt, with the 7 names Qt
    gives in it.
    """

    clientPrefaceLength = Kee[int](24)
    connectionStreamID = Kee[int](0)
    frameHeaderSize = Kee[int](9)
    minPayloadLimit = Kee[int](16384)
    maxPayloadSize = Kee[int](16777215)
    defaultSessionWindowSize = Kee[int](65535)
    maxConcurrentStreams = Kee[int](100)

  class Settings(CuteNum, scoped=True):
    """
    The enum 'Http2::Settings' of Qt, with the 6 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    HEADER_TABLE_SIZE_ID = Kee[int](1)
    ENABLE_PUSH_ID = Kee[int](2)
    MAX_CONCURRENT_STREAMS_ID = Kee[int](3)
    INITIAL_WINDOW_SIZE_ID = Kee[int](4)
    MAX_FRAME_SIZE_ID = Kee[int](5)
    MAX_HEADER_LIST_SIZE_ID = Kee[int](6)
