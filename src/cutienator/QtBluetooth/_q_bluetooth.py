"""
QBluetooth stands for the namespace 'QBluetooth' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class QBluetooth:
  """
  The namespace 'QBluetooth' of Qt, which holds no objects. It holds the 2
  enums Qt writes in it, each under its name, and the 2 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AttAccessConstraint(CuteFlags, scoped=True):
    """
    The flags enum 'QBluetooth::AttAccessConstraint' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QBluetooth::AttAccessConstraints'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    AttAuthorizationRequired = 0x1
    AttAuthenticationRequired = 0x2
    AttEncryptionRequired = 0x4

  AttAccessConstraints = AttAccessConstraint

  class Security(CuteFlags, scoped=True):
    """
    The flags enum 'QBluetooth::Security' of Qt, with the 5 names Qt gives in
    it. Qt names the type of its combinations 'QBluetooth::SecurityFlags'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoSecurity = 0x0
    Authorization = 0x1
    Authentication = 0x2
    Encryption = 0x4
    Secure = 0x8

  SecurityFlags = Security
