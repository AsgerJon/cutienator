"""
QOpcUaX509ExtensionKeyUsage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuax509extensionkeyusage.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QOpcUaX509Extension


class QOpcUaX509ExtensionKeyUsage(QOpcUaX509Extension):
  """
  The cute side of Qt's QOpcUaX509ExtensionKeyUsage: a plain Python object
  standing in front of one C++ QOpcUaX509ExtensionKeyUsage.

  It is built on the cute 'QOpcUaX509Extension', as Qt's
  QOpcUaX509ExtensionKeyUsage is built on Qt's QOpcUaX509Extension, and has
  everything that class has.

  C++ hands a QOpcUaX509ExtensionKeyUsage around as a copy, so every C++
  QOpcUaX509ExtensionKeyUsage behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaX509ExtensionKeyUsage that has a ritual and
  that Python can call so far, 3 names in all: '__eq__', 'setKeyUsage',
  'keyUsage'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaX509ExtensionKeyUsage
    &QOpcUaX509ExtensionKeyUsage::operator=(const QOpcUaX509ExtensionKeyUsage
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaX509ExtensionKeyUsage::~QOpcUaX509ExtensionKeyUsage()': the
    destructor: Python removes its C++ QOpcUaX509ExtensionKeyUsage by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaX509ExtensionKeyUsage is created at the first use, not by
    'QOpcUaX509ExtensionKeyUsage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaX509ExtensionKeyUsage back gives a copy the
    ritual made for Python, in a new cute QOpcUaX509ExtensionKeyUsage.
  """

  #  The enums Qt writes inside QOpcUaX509ExtensionKeyUsage, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class KeyUsage(CuteNum, scoped=True):
    """
    The enum 'QOpcUaX509ExtensionKeyUsage::KeyUsage' of Qt, with the 9 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    DigitalSignature = Kee[int](0)
    NonRepudiation = Kee[int](1)
    KeyEncipherment = Kee[int](2)
    DataEncipherment = Kee[int](3)
    KeyAgreement = Kee[int](4)
    CertificateSigning = Kee[int](5)
    CrlSigning = Kee[int](6)
    EnciptherOnly = Kee[int](7)
    DecipherOnly = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaX509ExtensionKeyUsage'

  #  Qt's '~QOpcUaX509ExtensionKeyUsage()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaX509ExtensionKeyUsage behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QOpcUaX509ExtensionKeyUsageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(KeyUsage)
  def keyUsage(self, a0: KeyUsage) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509ExtensionKeyUsage::keyUsage(KeyUsage a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionkeyusage.html#keyUsage

    Parameters
    ----------

    a0 : KeyUsage
      Passed on as its number.
    """
    #  bool QOpcUaX509ExtensionKeyUsage::keyUsage(KeyUsage a0) const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaX509ExtensionKeyUsage8keyUsageENS_8KeyUsageE',
        a0.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(KeyUsage)
  @overload(KeyUsage, bool)
  def setKeyUsage(self, keyUsage: KeyUsage, enable: bool = True) -> None:
    """
    Calls Qt's 'void QOpcUaX509ExtensionKeyUsage::setKeyUsage(KeyUsage
    keyUsage, bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionkeyusage.html#setKeyUsage

    Parameters
    ----------

    keyUsage : KeyUsage
      Passed on as its number.

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QOpcUaX509ExtensionKeyUsage::setKeyUsage(KeyUsage keyUsage, bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN27QOpcUaX509ExtensionKeyUsage11setKeyUsageENS_8KeyUsageEb',
        keyUsage.value, enable,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaX509ExtensionKeyUsage) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509ExtensionKeyUsage::operator==(const
    QOpcUaX509ExtensionKeyUsage &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionkeyusage.html#operator==

    Parameters
    ----------

    rhs : QOpcUaX509ExtensionKeyUsage
      Passed on as a value: Qt reads the C++ QOpcUaX509ExtensionKeyUsage,
      which stays Python's own.
    """
    #  bool QOpcUaX509ExtensionKeyUsage::operator==(const
    #      QOpcUaX509ExtensionKeyUsage &rhs) const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaX509ExtensionKeyUsageeqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaX509ExtensionKeyUsage::QOpcUaX509ExtensionKeyUsage()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionkeyusage.html
    """
    #  QOpcUaX509ExtensionKeyUsage::QOpcUaX509ExtensionKeyUsage()
    self._noteCreation(QOpcUaX509ExtensionKeyUsage, lambda: Rituals.call(
        'ritual_ZN27QOpcUaX509ExtensionKeyUsageC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaX509ExtensionKeyUsage) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaX509ExtensionKeyUsage::QOpcUaX509ExtensionKeyUsage(const
    QOpcUaX509ExtensionKeyUsage &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionkeyusage.html

    Parameters
    ----------

    a0 : QOpcUaX509ExtensionKeyUsage
      Passed on as a value: Qt reads the C++ QOpcUaX509ExtensionKeyUsage,
      which stays Python's own.
    """
    #  QOpcUaX509ExtensionKeyUsage::QOpcUaX509ExtensionKeyUsage(const
    #      QOpcUaX509ExtensionKeyUsage &a0)
    self._noteCreation(QOpcUaX509ExtensionKeyUsage, lambda: Rituals.call(
        'ritual_ZN27QOpcUaX509ExtensionKeyUsageC1ERKS_', self._valueOf(a0),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
