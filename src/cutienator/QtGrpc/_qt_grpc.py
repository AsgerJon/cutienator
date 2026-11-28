"""
QtGrpc stands for the namespace 'QtGrpc' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtGrpc:
  """
  The namespace 'QtGrpc' of Qt, which holds no objects. It holds the 5 enums
  Qt writes in it, each under its name, and the 2 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class CompressionAlgorithm(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QtGrpc::CompressionAlgorithm' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QtGrpc::CompressionAlgorithms'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    Identity = 0x1
    Deflate = 0x2
    Gzip = 0x4

  CompressionAlgorithms = CompressionAlgorithm

  class InterceptorCapability(CuteFlags, number='unsigned long long', scoped=True):
    """
    The flags enum 'QtGrpc::InterceptorCapability' of Qt, with the 8 names Qt
    gives in it. Qt names the type of its combinations
    'QtGrpc::InterceptorCapabilities'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    Start = 0x1
    InitialMetadata = 0x2
    MessageReceived = 0x4
    WriteMessage = 0x8
    WritesDone = 0x10
    TrailingMetadata = 0x20
    Finished = 0x40
    Cancel = 0x80

  InterceptorCapabilities = InterceptorCapability

  class RpcType(CuteNum, scoped=True):
    """
    The enum 'QtGrpc::RpcType' of Qt, with the 4 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    UnaryCall = Kee[int](0)
    ServerStreaming = Kee[int](1)
    ClientStreaming = Kee[int](2)
    BidiStreaming = Kee[int](3)

  class SerializationFormat(CuteNum, scoped=True):
    """
    The enum 'QtGrpc::SerializationFormat' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Default = Kee[int](0)
    Protobuf = Kee[int](1)
    Json = Kee[int](2)

  class StatusCode(CuteNum, scoped=True):
    """
    The enum 'QtGrpc::StatusCode' of Qt, with the 17 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Ok = Kee[int](0)
    Cancelled = Kee[int](1)
    Unknown = Kee[int](2)
    InvalidArgument = Kee[int](3)
    DeadlineExceeded = Kee[int](4)
    NotFound = Kee[int](5)
    AlreadyExists = Kee[int](6)
    PermissionDenied = Kee[int](7)
    ResourceExhausted = Kee[int](8)
    FailedPrecondition = Kee[int](9)
    Aborted = Kee[int](10)
    OutOfRange = Kee[int](11)
    Unimplemented = Kee[int](12)
    Internal = Kee[int](13)
    Unavailable = Kee[int](14)
    DataLoss = Kee[int](15)
    Unauthenticated = Kee[int](16)
