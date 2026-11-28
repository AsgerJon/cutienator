"""
QBluezConst stands for the namespace 'QBluezConst' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QBluezConst:
  """
  The namespace 'QBluezConst' of Qt, which holds no objects. It holds the 4
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AttCommand(CuteNum, scoped=True):
    """
    The enum 'QBluezConst::AttCommand' of Qt, with the 28 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    ATT_OP_ERROR_RESPONSE = Kee[int](1)
    ATT_OP_EXCHANGE_MTU_REQUEST = Kee[int](2)
    ATT_OP_EXCHANGE_MTU_RESPONSE = Kee[int](3)
    ATT_OP_FIND_INFORMATION_REQUEST = Kee[int](4)
    ATT_OP_FIND_INFORMATION_RESPONSE = Kee[int](5)
    ATT_OP_FIND_BY_TYPE_VALUE_REQUEST = Kee[int](6)
    ATT_OP_FIND_BY_TYPE_VALUE_RESPONSE = Kee[int](7)
    ATT_OP_READ_BY_TYPE_REQUEST = Kee[int](8)
    ATT_OP_READ_BY_TYPE_RESPONSE = Kee[int](9)
    ATT_OP_READ_REQUEST = Kee[int](10)
    ATT_OP_READ_RESPONSE = Kee[int](11)
    ATT_OP_READ_BLOB_REQUEST = Kee[int](12)
    ATT_OP_READ_BLOB_RESPONSE = Kee[int](13)
    ATT_OP_READ_MULTIPLE_REQUEST = Kee[int](14)
    ATT_OP_READ_MULTIPLE_RESPONSE = Kee[int](15)
    ATT_OP_READ_BY_GROUP_REQUEST = Kee[int](16)
    ATT_OP_READ_BY_GROUP_RESPONSE = Kee[int](17)
    ATT_OP_WRITE_REQUEST = Kee[int](18)
    ATT_OP_WRITE_RESPONSE = Kee[int](19)
    ATT_OP_PREPARE_WRITE_REQUEST = Kee[int](22)
    ATT_OP_PREPARE_WRITE_RESPONSE = Kee[int](23)
    ATT_OP_EXECUTE_WRITE_REQUEST = Kee[int](24)
    ATT_OP_EXECUTE_WRITE_RESPONSE = Kee[int](25)
    ATT_OP_HANDLE_VAL_NOTIFICATION = Kee[int](27)
    ATT_OP_HANDLE_VAL_INDICATION = Kee[int](29)
    ATT_OP_HANDLE_VAL_CONFIRMATION = Kee[int](30)
    ATT_OP_WRITE_COMMAND = Kee[int](82)
    ATT_OP_SIGNED_WRITE_COMMAND = Kee[int](210)

  class AttError(CuteNum, scoped=True):
    """
    The enum 'QBluezConst::AttError' of Qt, with the 21 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    ATT_ERROR_NO_ERROR = Kee[int](0)
    ATT_ERROR_INVALID_HANDLE = Kee[int](1)
    ATT_ERROR_READ_NOT_PERM = Kee[int](2)
    ATT_ERROR_WRITE_NOT_PERM = Kee[int](3)
    ATT_ERROR_INVALID_PDU = Kee[int](4)
    ATT_ERROR_INSUF_AUTHENTICATION = Kee[int](5)
    ATT_ERROR_REQUEST_NOT_SUPPORTED = Kee[int](6)
    ATT_ERROR_INVALID_OFFSET = Kee[int](7)
    ATT_ERROR_INSUF_AUTHORIZATION = Kee[int](8)
    ATT_ERROR_PREPARE_QUEUE_FULL = Kee[int](9)
    ATT_ERROR_ATTRIBUTE_NOT_FOUND = Kee[int](10)
    ATT_ERROR_ATTRIBUTE_NOT_LONG = Kee[int](11)
    ATT_ERROR_INSUF_ENCR_KEY_SIZE = Kee[int](12)
    ATT_ERROR_INVAL_ATTR_VALUE_LEN = Kee[int](13)
    ATT_ERROR_UNLIKELY = Kee[int](14)
    ATT_ERROR_INSUF_ENCRYPTION = Kee[int](15)
    ATT_ERROR_UNSUPPRTED_GROUP_TYPE = Kee[int](16)
    ATT_ERROR_INSUF_RESOURCES = Kee[int](17)
    ATT_ERROR_APPLICATION_START = Kee[int](128)
    ATT_ERROR_REQUEST_STALLED = Kee[int](129)
    ATT_ERROR_APPLICATION_END = Kee[int](159)

  class OpCodeCommandField(CuteNum):
    """
    The enum 'QBluezConst::OpCodeCommandField' of Qt, with the 8 names Qt
    gives in it.
    """

    OcfLeSetAdvParams = Kee[int](6)
    OcfLeReadTxPowerLevel = Kee[int](7)
    OcfLeSetAdvData = Kee[int](8)
    OcfLeSetScanResponseData = Kee[int](9)
    OcfLeSetAdvEnable = Kee[int](10)
    OcfLeClearWhiteList = Kee[int](16)
    OcfLeAddToWhiteList = Kee[int](17)
    OcfLeConnectionUpdate = Kee[int](19)

  class OpCodeGroupField(CuteNum):
    """
    The enum 'QBluezConst::OpCodeGroupField' of Qt, with the 1 names Qt gives
    in it.
    """

    OgfLinkControl = Kee[int](8)
