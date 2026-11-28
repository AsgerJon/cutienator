"""
QTiltReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qtiltsensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTiltReading(QSensorReading):
  """
  The cute side of Qt's QTiltReading: a plain Python object standing in front
  of one C++ QTiltReading.

  It is built on the cute 'QSensorReading', as Qt's QTiltReading is built on
  Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTiltReading that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'copyValuesFrom',
  'yRotation', 'setYRotation', 'xRotation', 'setXRotation'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTiltReading::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTiltReading::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QTiltReading::~QTiltReading()': the destructor: Python never
    removes a C++ QTiltReading.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QTiltReading is created at the first use, not by
    'QTiltReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTiltReading.
  - Qt tells when it has removed the C++ QTiltReading. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTiltReading::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTiltReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QTiltReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTiltReading'

  #  A C++ QTiltReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTiltReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTiltReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTiltReading::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QTiltReading10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def yRotation(self) -> float:
    """
    Calls Qt's 'qreal QTiltReading::yRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#yRotation
    """
    #  qreal QTiltReading::yRotation() const
    return self.uglySide.call('ritual_ZNK12QTiltReading9yRotationEv')

  def xRotation(self) -> float:
    """
    Calls Qt's 'qreal QTiltReading::xRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#xRotation
    """
    #  qreal QTiltReading::xRotation() const
    return self.uglySide.call('ritual_ZNK12QTiltReading9xRotationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setYRotation(self, y: float) -> None:
    """
    Calls Qt's 'void QTiltReading::setYRotation(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#setYRotation

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QTiltReading::setYRotation(qreal y)
    self.uglySide.call('ritual_ZN12QTiltReading12setYRotationEd', y)

  @overload(float)
  def setXRotation(self, x: float) -> None:
    """
    Calls Qt's 'void QTiltReading::setXRotation(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#setXRotation

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QTiltReading::setXRotation(qreal x)
    self.uglySide.call('ritual_ZN12QTiltReading12setXRotationEd', x)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTiltReading::QTiltReading(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#QTiltReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTiltReading::QTiltReading(QObject *parent)
    self._noteCreation(QTiltReading, lambda: Rituals.call(
        'ritual_ZN12QTiltReadingC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QSensorReading)
  @overload(NoneType)
  def copyValuesFrom(self, other: Optional[QSensorReading]) -> None:
    """
    Calls Qt's 'void QTiltReading::copyValuesFrom(QSensorReading *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiltreading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTiltReading::copyValuesFrom(QSensorReading *other)
    ritual = 'ritual_ZN12QTiltReading14copyValuesFromEP14QSensorReading'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QTiltReading14copyValuesFromEP14QSensorReading')
    self.uglySide.call(ritual, self._addressOf(other))
