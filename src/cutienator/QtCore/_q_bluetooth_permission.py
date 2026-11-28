"""
QBluetoothPermission binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QBluetoothPermission(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBluetoothPermission: a plain Python object standing
  in front of one C++ QBluetoothPermission.

  C++ hands a QBluetoothPermission around as a copy, so every C++
  QBluetoothPermission behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBluetoothPermission that has a ritual and that
  Python can call so far, 2 names in all: 'setCommunicationModes',
  'communicationModes'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBluetoothPermission::QBluetoothPermission(QBluetoothPermission
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QBluetoothPermission::~QBluetoothPermission()': the destructor:
    Python removes its C++ QBluetoothPermission by it, and has no other use
    for it.
  - Qt's 'QBluetoothPermission &QBluetoothPermission::operator=(const
    QBluetoothPermission &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QBluetoothPermission
    &QBluetoothPermission::operator=(QBluetoothPermission &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QBluetoothPermission::swap(QBluetoothPermission &other)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QBluetoothPermission is created at the first use, not by
    'QBluetoothPermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBluetoothPermission back gives a copy the ritual
    made for Python, in a new cute QBluetoothPermission.
  - Each name of Qt's QBluetoothPermission that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QBluetoothPermission, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CommunicationMode(CuteFlags, number='unsigned char'):
    """
    The flags enum 'QBluetoothPermission::CommunicationMode' of Qt, with the
    3 names Qt gives in it. Qt names the type of its combinations
    'QBluetoothPermission::CommunicationModes'.
    """

    Access = 0x1
    Advertise = 0x2
    Default = 0x3

  CommunicationModes = CommunicationMode

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothPermission'

  #  Qt's '~QBluetoothPermission()'. Naming it makes this a value class:
  #  Python owns every C++ QBluetoothPermission behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QBluetoothPermissionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def communicationModes(self) -> CommunicationModes:
    """
    Calls Qt's 'CommunicationModes QBluetoothPermission::communicationModes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothpermission.html#communicationModes

    Returns
    -------

    CommunicationModes
      The value standing for the combination Qt gave back.
    """
    #  CommunicationModes QBluetoothPermission::communicationModes() const
    return QBluetoothPermission.CommunicationModes(self.uglySide.call(
        'ritual_ZNK20QBluetoothPermission18communicationModesEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(CommunicationModes)
  def setCommunicationModes(self, modes: CommunicationModes) -> None:
    """
    Calls Qt's 'void
    QBluetoothPermission::setCommunicationModes(CommunicationModes modes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothpermission.html#setCommunicationModes

    Parameters
    ----------

    modes : CommunicationModes
      Passed on as its number.
    """
    #  void QBluetoothPermission::setCommunicationModes(CommunicationModes
    #      modes)
    self.uglySide.call(
        'ritual_ZN20QBluetoothPermission21setCommunicationModesE6QFlagsINS_'
        '17CommunicationModeEE',
        modes.value,
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
    'QBluetoothPermission::QBluetoothPermission()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothpermission.html#QBluetoothPermission
    """
    #  QBluetoothPermission::QBluetoothPermission()
    self._noteCreation(QBluetoothPermission, lambda: Rituals.call(
        'ritual_ZN20QBluetoothPermissionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QBluetoothPermission) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothPermission::QBluetoothPermission(const QBluetoothPermission
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothpermission.html#QBluetoothPermission

    Parameters
    ----------

    other : QBluetoothPermission
      Passed on as a value: Qt reads the C++ QBluetoothPermission, which
      stays Python's own.
    """
    #  QBluetoothPermission::QBluetoothPermission(const QBluetoothPermission
    #      &other)
    self._noteCreation(QBluetoothPermission, lambda: Rituals.call(
        'ritual_ZN20QBluetoothPermissionC1ERKS_', self._valueOf(other),
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
    Qt's 'void QBluetoothPermission::swap(QBluetoothPermission &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBluetoothPermission.swap' has no cute function yet. Qt's 'void "
        "QBluetoothPermission::swap(QBluetoothPermission &other)': takes a "
        "type Python has no way to hand over yet.")
