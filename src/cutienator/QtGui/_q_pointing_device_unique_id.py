"""
QPointingDeviceUniqueId binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpointingdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QPointingDeviceUniqueId(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPointingDeviceUniqueId: a plain Python object
  standing in front of one C++ QPointingDeviceUniqueId.

  C++ hands a QPointingDeviceUniqueId around as a copy, so every C++
  QPointingDeviceUniqueId behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPointingDeviceUniqueId that has a ritual and that
  Python can call so far, 5 names in all: 'fromNumericId', 'isValid',
  'numericId', '__eq__', '__ne__'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPointingDeviceUniqueId::~QPointingDeviceUniqueId()': the
    destructor: Python removes its C++ QPointingDeviceUniqueId by it, and has
    no other use for it.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPointingDeviceUniqueId is created at the first use, not by
    'QPointingDeviceUniqueId(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPointingDeviceUniqueId back gives a copy the ritual
    made for Python, in a new cute QPointingDeviceUniqueId.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def fromNumericId(id: int) -> QPointingDeviceUniqueId:
    """
    Calls Qt's 'QPointingDeviceUniqueId
    QPointingDeviceUniqueId::fromNumericId(qint64 id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#fromNumericId

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QPointingDeviceUniqueId
      A new cute QPointingDeviceUniqueId around the copy Qt gave back. Python
      owns it.
    """
    #  QPointingDeviceUniqueId QPointingDeviceUniqueId::fromNumericId(qint64
    #      id)
    address = Rituals.call(
        'ritual_ZN23QPointingDeviceUniqueId13fromNumericIdEx', id,
    )
    return QPointingDeviceUniqueId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPointingDeviceUniqueId'

  #  Qt's '~QPointingDeviceUniqueId()'. Naming it makes this a value class:
  #  Python owns every C++ QPointingDeviceUniqueId behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QPointingDeviceUniqueIdD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPointingDeviceUniqueId::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#isValid
    """
    #  bool QPointingDeviceUniqueId::isValid() const
    return self.uglySide.call(
        'ritual_ZNK23QPointingDeviceUniqueId7isValidEv',
    )

  def numericId(self) -> int:
    """
    Calls Qt's 'qint64 QPointingDeviceUniqueId::numericId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#numericId
    """
    #  qint64 QPointingDeviceUniqueId::numericId() const
    return self.uglySide.call(
        'ritual_ZNK23QPointingDeviceUniqueId9numericIdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPointingDeviceUniqueId) -> bool:
    """
    Calls Qt's 'bool operator==(QPointingDeviceUniqueId lhs,
    QPointingDeviceUniqueId rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#operator==

    Parameters
    ----------

    rhs : QPointingDeviceUniqueId
      Passed on as a value: Qt reads the C++ QPointingDeviceUniqueId, which
      stays Python's own.
    """
    #  bool operator==(QPointingDeviceUniqueId lhs, QPointingDeviceUniqueId
    #      rhs)
    return Rituals.call(
        'ritual_Zeq23QPointingDeviceUniqueIdS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QPointingDeviceUniqueId) -> bool:
    """
    Calls Qt's 'bool operator!=(QPointingDeviceUniqueId lhs,
    QPointingDeviceUniqueId rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html#operator!=

    Parameters
    ----------

    rhs : QPointingDeviceUniqueId
      Passed on as a value: Qt reads the C++ QPointingDeviceUniqueId, which
      stays Python's own.
    """
    #  bool operator!=(QPointingDeviceUniqueId lhs, QPointingDeviceUniqueId
    #      rhs)
    return Rituals.call(
        'ritual_Zne23QPointingDeviceUniqueIdS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    'QPointingDeviceUniqueId::QPointingDeviceUniqueId()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpointingdeviceuniqueid.html
    """
    #  QPointingDeviceUniqueId::QPointingDeviceUniqueId()
    self._noteCreation(QPointingDeviceUniqueId, lambda: Rituals.call(
        'ritual_ZN23QPointingDeviceUniqueIdC1Ev',
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
