"""
QMicrophonePermission binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMicrophonePermission(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMicrophonePermission: a plain Python object standing
  in front of one C++ QMicrophonePermission.

  C++ hands a QMicrophonePermission around as a copy, so every C++
  QMicrophonePermission behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QMicrophonePermission yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMicrophonePermission::QMicrophonePermission(QMicrophonePermission
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QMicrophonePermission::~QMicrophonePermission()': the destructor:
    Python removes its C++ QMicrophonePermission by it, and has no other use
    for it.
  - Qt's 'QMicrophonePermission &QMicrophonePermission::operator=(const
    QMicrophonePermission &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QMicrophonePermission
    &QMicrophonePermission::operator=(QMicrophonePermission &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QMicrophonePermission::swap(QMicrophonePermission &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QMicrophonePermission is created at the first use, not by
    'QMicrophonePermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMicrophonePermission back gives a copy the ritual
    made for Python, in a new cute QMicrophonePermission.
  - Each name of Qt's QMicrophonePermission that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMicrophonePermission'

  #  Qt's '~QMicrophonePermission()'. Naming it makes this a value class:
  #  Python owns every C++ QMicrophonePermission behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QMicrophonePermissionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QMicrophonePermission::QMicrophonePermission()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmicrophonepermission.html#QMicrophonePermission
    """
    #  QMicrophonePermission::QMicrophonePermission()
    self._noteCreation(QMicrophonePermission, lambda: Rituals.call(
        'ritual_ZN21QMicrophonePermissionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QMicrophonePermission) -> None:
    """
    Notes what was given, for Qt's
    'QMicrophonePermission::QMicrophonePermission(const QMicrophonePermission
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmicrophonepermission.html#QMicrophonePermission

    Parameters
    ----------

    other : QMicrophonePermission
      Passed on as a value: Qt reads the C++ QMicrophonePermission, which
      stays Python's own.
    """
    #  QMicrophonePermission::QMicrophonePermission(const
    #      QMicrophonePermission &other)
    self._noteCreation(QMicrophonePermission, lambda: Rituals.call(
        'ritual_ZN21QMicrophonePermissionC1ERKS_', self._valueOf(other),
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
    Qt's 'void QMicrophonePermission::swap(QMicrophonePermission &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMicrophonePermission.swap' has no cute function yet. Qt's 'void "
        "QMicrophonePermission::swap(QMicrophonePermission &other)': takes "
        "a type Python has no way to hand over yet.")
