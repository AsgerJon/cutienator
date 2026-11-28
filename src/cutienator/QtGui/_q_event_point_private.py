"""
QEventPointPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qeventpoint_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QEventPointPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QEventPoint

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from . import QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventPointPrivate(QSharedData):
  """
  The cute side of Qt's QEventPointPrivate: a plain Python object standing in
  front of one C++ QEventPointPrivate.

  It is built on the cute 'QSharedData', as Qt's QEventPointPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QEventPointPrivate around as a copy, so every C++
  QEventPointPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QEventPointPrivate that has a ritual and that Python
  can call so far, 1 name in all: '__eq__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QEventPointPrivate::~QEventPointPrivate()': the destructor: Python
    removes its C++ QEventPointPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QEventPointPrivate is created at the first use, not by
    'QEventPointPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QEventPointPrivate back gives a copy the ritual made
    for Python, in a new cute QEventPointPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventPointPrivate'

  #  Qt's '~QEventPointPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QEventPointPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QEventPointPrivateD1Ev'

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

  @overload(THIS)
  def __eq__(self, other: QEventPointPrivate) -> bool:
    """
    Calls Qt's 'bool QEventPointPrivate::operator==(const QEventPointPrivate
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventpointprivate.html#operator==

    Parameters
    ----------

    other : QEventPointPrivate
      Passed on as a value: Qt reads the C++ QEventPointPrivate, which stays
      Python's own.
    """
    #  bool QEventPointPrivate::operator==(const QEventPointPrivate &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QEventPointPrivateeqERKS_', self._valueOf(other),
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

  @overload(int, QPointingDevice)
  @overload(int, NoneType)
  def __init__(self, id: int, device: Optional[QPointingDevice]) -> None:
    """
    Notes what was given, for Qt's
    'QEventPointPrivate::QEventPointPrivate(int id, const QPointingDevice
    *device)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpointprivate.html#QEventPointPrivate

    Parameters
    ----------

    id : int
      Passed on as it is.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QEventPointPrivate::QEventPointPrivate(int id, const QPointingDevice
    #      *device)
    self._noteCreation(QEventPointPrivate, lambda: Rituals.call(
        'ritual_ZN18QEventPointPrivateC1EiPK15QPointingDevice',
        id, self._addressOf(device),
    ))

  @overload(int, QEventPoint.State, QPointF, QPointF)
  def __init__(
      self,
      pointId: int,
      state: QEventPoint.State,
      scenePosition: QPointF,
      globalPosition: QPointF,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QEventPointPrivate::QEventPointPrivate(int pointId, QEventPoint::State
    state, const QPointF &scenePosition, const QPointF &globalPosition)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventpointprivate.html#QEventPointPrivate

    Parameters
    ----------

    pointId : int
      Passed on as it is.

    state : QEventPoint.State
      Passed on as its number.

    scenePosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QEventPointPrivate::QEventPointPrivate(int pointId, QEventPoint::State
    #      state, const QPointF &scenePosition, const QPointF
    #      &globalPosition)
    self._noteCreation(QEventPointPrivate, lambda: Rituals.call(
        'ritual_ZN18QEventPointPrivateC1EiN11QEventPoint5StateERK7QPointFS4'
        '_',
        pointId, state.value, self._valueOf(scenePosition, 'QPointF'),
        self._valueOf(globalPosition, 'QPointF'),
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
