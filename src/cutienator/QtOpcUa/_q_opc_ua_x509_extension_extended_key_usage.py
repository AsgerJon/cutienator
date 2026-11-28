"""
QOpcUaX509ExtensionExtendedKeyUsage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuax509extensionextendedkeyusage.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QOpcUaX509Extension


class QOpcUaX509ExtensionExtendedKeyUsage(QOpcUaX509Extension):
  """
  The cute side of Qt's QOpcUaX509ExtensionExtendedKeyUsage: a plain Python
  object standing in front of one C++ QOpcUaX509ExtensionExtendedKeyUsage.

  It is built on the cute 'QOpcUaX509Extension', as Qt's
  QOpcUaX509ExtensionExtendedKeyUsage is built on Qt's QOpcUaX509Extension,
  and has everything that class has.

  C++ hands a QOpcUaX509ExtensionExtendedKeyUsage around as a copy, so every
  C++ QOpcUaX509ExtensionExtendedKeyUsage behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaX509ExtensionExtendedKeyUsage that has a
  ritual and that Python can call so far, 3 names in all: '__eq__',
  'setKeyUsage', 'keyUsage'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaX509ExtensionExtendedKeyUsage
    &QOpcUaX509ExtensionExtendedKeyUsage::operator=(const
    QOpcUaX509ExtensionExtendedKeyUsage &a0)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QOpcUaX509ExtensionExtendedKeyUsage::
    ~QOpcUaX509ExtensionExtendedKeyUsage()': the destructor: Python removes
    its C++ QOpcUaX509ExtensionExtendedKeyUsage by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaX509ExtensionExtendedKeyUsage is created at the first use,
    not by 'QOpcUaX509ExtensionExtendedKeyUsage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaX509ExtensionExtendedKeyUsage back gives a copy
    the ritual made for Python, in a new cute
    QOpcUaX509ExtensionExtendedKeyUsage.
  """

  #  The enums Qt writes inside QOpcUaX509ExtensionExtendedKeyUsage, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class KeyUsage(CuteNum, scoped=True):
    """
    The enum 'QOpcUaX509ExtensionExtendedKeyUsage::KeyUsage' of Qt, with the
    4 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    TlsWebServerAuthentication = Kee[int](0)
    TlsWebClientAuthentication = Kee[int](1)
    SignExecutableCode = Kee[int](2)
    EmailProtection = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaX509ExtensionExtendedKeyUsage'

  #  Qt's '~QOpcUaX509ExtensionExtendedKeyUsage()'. Naming it makes this a
  #  value class: Python owns every C++ QOpcUaX509ExtensionExtendedKeyUsage
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsageD1Ev'

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
    Calls Qt's 'bool QOpcUaX509ExtensionExtendedKeyUsage::keyUsage(KeyUsage
    a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionextendedkeyusage.html#keyUsage

    Parameters
    ----------

    a0 : KeyUsage
      Passed on as its number.
    """
    #  bool QOpcUaX509ExtensionExtendedKeyUsage::keyUsage(KeyUsage a0) const
    return self.uglySide.call(
        'ritual_ZNK35QOpcUaX509ExtensionExtendedKeyUsage8keyUsageENS_8KeyUs'
        'ageE',
        a0.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(KeyUsage)
  @overload(KeyUsage, bool)
  def setKeyUsage(self, keyUsage: KeyUsage, enable: bool = True) -> None:
    """
    Calls Qt's 'void
    QOpcUaX509ExtensionExtendedKeyUsage::setKeyUsage(KeyUsage keyUsage, bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionextendedkeyusage.html

    Parameters
    ----------

    keyUsage : KeyUsage
      Passed on as its number.

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QOpcUaX509ExtensionExtendedKeyUsage::setKeyUsage(KeyUsage
    #      keyUsage, bool enable)
    self.uglySide.call(
        'ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsage11setKeyUsageENS_8Ke'
        'yUsageEb',
        keyUsage.value, enable,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaX509ExtensionExtendedKeyUsage) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509ExtensionExtendedKeyUsage::operator==(const
    QOpcUaX509ExtensionExtendedKeyUsage &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionextendedkeyusage.html

    Parameters
    ----------

    rhs : QOpcUaX509ExtensionExtendedKeyUsage
      Passed on as a value: Qt reads the C++
      QOpcUaX509ExtensionExtendedKeyUsage, which stays Python's own.
    """
    #  bool QOpcUaX509ExtensionExtendedKeyUsage::operator==(const
    #      QOpcUaX509ExtensionExtendedKeyUsage &rhs) const
    return self.uglySide.call(
        'ritual_ZNK35QOpcUaX509ExtensionExtendedKeyUsageeqERKS_',
        self._valueOf(rhs),
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
    Notes what was given, for Qt's 'QOpcUaX509ExtensionExtendedKeyUsage::
    QOpcUaX509ExtensionExtendedKeyUsage()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionextendedkeyusage.html
    """
    #  QOpcUaX509ExtensionExtendedKeyUsage::
    #      QOpcUaX509ExtensionExtendedKeyUsage()
    self._noteCreation(
        QOpcUaX509ExtensionExtendedKeyUsage, lambda: Rituals.call(
            'ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsageC1Ev',
        ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaX509ExtensionExtendedKeyUsage) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaX509ExtensionExtendedKeyUsage::
    QOpcUaX509ExtensionExtendedKeyUsage(const
    QOpcUaX509ExtensionExtendedKeyUsage &a0)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionextendedkeyusage.html

    Parameters
    ----------

    a0 : QOpcUaX509ExtensionExtendedKeyUsage
      Passed on as a value: Qt reads the C++
      QOpcUaX509ExtensionExtendedKeyUsage, which stays Python's own.
    """
    #  QOpcUaX509ExtensionExtendedKeyUsage::
    #      QOpcUaX509ExtensionExtendedKeyUsage(const
    #      QOpcUaX509ExtensionExtendedKeyUsage &a0)
    self._noteCreation(
        QOpcUaX509ExtensionExtendedKeyUsage, lambda: Rituals.call(
            'ritual_ZN35QOpcUaX509ExtensionExtendedKeyUsageC1ERKS_',
            self._valueOf(a0),
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
