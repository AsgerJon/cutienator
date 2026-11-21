"""
QContactsPermission binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QContactsPermission(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QContactsPermission: a plain Python object standing
  in front of one C++ QContactsPermission.

  C++ hands a QContactsPermission around as a copy, so every C++
  QContactsPermission behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QContactsPermission that has a ritual and that
  Python can call so far, 2 names in all: 'setAccessMode', 'accessMode'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QContactsPermission::~QContactsPermission()': the destructor:
    Python removes its C++ QContactsPermission by it, and has no other use
    for it.

  What has no ritual
  ------------------

  7 of the 12 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QContactsPermission is created at the first use, not by
    'QContactsPermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QContactsPermission back gives a copy the ritual made
    for Python, in a new cute QContactsPermission.
  """

  #  The enums Qt writes inside QContactsPermission, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AccessMode(CuteNum):
    """
    The enum 'QContactsPermission::AccessMode' of Qt, with the 2 names Qt
    gives in it.
    """

    ReadOnly = Kee[int](0)
    ReadWrite = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QContactsPermission'

  #  Qt's '~QContactsPermission()'. Naming it makes this a value class:
  #  Python owns every C++ QContactsPermission behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QContactsPermissionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def accessMode(self) -> AccessMode:
    """
    Calls Qt's 'AccessMode QContactsPermission::accessMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcontactspermission.html#accessMode

    Returns
    -------

    AccessMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AccessMode(number)'
      gives.
    """
    #  AccessMode QContactsPermission::accessMode() const
    return QContactsPermission.AccessMode(self.uglySide.call(
        'ritual_ZNK19QContactsPermission10accessModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AccessMode)
  def setAccessMode(self, mode: AccessMode) -> None:
    """
    Calls Qt's 'void QContactsPermission::setAccessMode(AccessMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcontactspermission.html#setAccessMode

    Parameters
    ----------

    mode : AccessMode
      Passed on as its number.
    """
    #  void QContactsPermission::setAccessMode(AccessMode mode)
    self.uglySide.call(
        'ritual_ZN19QContactsPermission13setAccessModeENS_10AccessModeE',
        mode.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QContactsPermission::QContactsPermission()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcontactspermission.html#QContactsPermission
    """
    #  QContactsPermission::QContactsPermission()
    self._noteCreation(QContactsPermission, lambda: Rituals.call(
        'ritual_ZN19QContactsPermissionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QContactsPermission) -> None:
    """
    Notes what was given, for Qt's
    'QContactsPermission::QContactsPermission(const QContactsPermission
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcontactspermission.html#QContactsPermission

    Parameters
    ----------

    other : QContactsPermission
      Passed on as a value: Qt reads the C++ QContactsPermission, which stays
      Python's own.
    """
    #  QContactsPermission::QContactsPermission(const QContactsPermission
    #      &other)
    self._noteCreation(QContactsPermission, lambda: Rituals.call(
        'ritual_ZN19QContactsPermissionC1ERKS_', self._valueOf(other),
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
