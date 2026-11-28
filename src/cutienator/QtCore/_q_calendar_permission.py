"""
QCalendarPermission binding of the Qt C++
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

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QCalendarPermission(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCalendarPermission: a plain Python object standing
  in front of one C++ QCalendarPermission.

  C++ hands a QCalendarPermission around as a copy, so every C++
  QCalendarPermission behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCalendarPermission that has a ritual and that
  Python can call so far, 2 names in all: 'setAccessMode', 'accessMode'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCalendarPermission::QCalendarPermission(QCalendarPermission
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QCalendarPermission::~QCalendarPermission()': the destructor:
    Python removes its C++ QCalendarPermission by it, and has no other use
    for it.
  - Qt's 'QCalendarPermission &QCalendarPermission::operator=(const
    QCalendarPermission &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCalendarPermission
    &QCalendarPermission::operator=(QCalendarPermission &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCalendarPermission::swap(QCalendarPermission &other)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QCalendarPermission is created at the first use, not by
    'QCalendarPermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCalendarPermission back gives a copy the ritual made
    for Python, in a new cute QCalendarPermission.
  - Each name of Qt's QCalendarPermission that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QCalendarPermission, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AccessMode(CuteNum):
    """
    The enum 'QCalendarPermission::AccessMode' of Qt, with the 3 names Qt
    gives in it.
    """

    ReadOnly = Kee[int](0)
    ReadWrite = Kee[int](1)
    WriteOnly = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCalendarPermission'

  #  Qt's '~QCalendarPermission()'. Naming it makes this a value class:
  #  Python owns every C++ QCalendarPermission behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QCalendarPermissionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def accessMode(self) -> AccessMode:
    """
    Calls Qt's 'AccessMode QCalendarPermission::accessMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpermission.html#accessMode

    Returns
    -------

    AccessMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AccessMode(number)'
      gives.
    """
    #  AccessMode QCalendarPermission::accessMode() const
    return QCalendarPermission.AccessMode(self.uglySide.call(
        'ritual_ZNK19QCalendarPermission10accessModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AccessMode)
  def setAccessMode(self, mode: AccessMode) -> None:
    """
    Calls Qt's 'void QCalendarPermission::setAccessMode(AccessMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpermission.html#setAccessMode

    Parameters
    ----------

    mode : AccessMode
      Passed on as its number.
    """
    #  void QCalendarPermission::setAccessMode(AccessMode mode)
    self.uglySide.call(
        'ritual_ZN19QCalendarPermission13setAccessModeENS_10AccessModeE',
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
    'QCalendarPermission::QCalendarPermission()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpermission.html#QCalendarPermission
    """
    #  QCalendarPermission::QCalendarPermission()
    self._noteCreation(QCalendarPermission, lambda: Rituals.call(
        'ritual_ZN19QCalendarPermissionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCalendarPermission) -> None:
    """
    Notes what was given, for Qt's
    'QCalendarPermission::QCalendarPermission(const QCalendarPermission
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpermission.html#QCalendarPermission

    Parameters
    ----------

    other : QCalendarPermission
      Passed on as a value: Qt reads the C++ QCalendarPermission, which stays
      Python's own.
    """
    #  QCalendarPermission::QCalendarPermission(const QCalendarPermission
    #      &other)
    self._noteCreation(QCalendarPermission, lambda: Rituals.call(
        'ritual_ZN19QCalendarPermissionC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCalendarPermission::swap(QCalendarPermission &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCalendarPermission.swap' has no cute function yet. Qt's 'void "
        "QCalendarPermission::swap(QCalendarPermission &other)': takes a "
        "type Python has no way to hand over yet.")
