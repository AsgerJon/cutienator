"""
QGyroscopeReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qgyroscope.h, Qt 6.12.0. Changes made here are lost.
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


class QGyroscopeReading(QSensorReading):
  """
  The cute side of Qt's QGyroscopeReading: a plain Python object standing in
  front of one C++ QGyroscopeReading.

  It is built on the cute 'QSensorReading', as Qt's QGyroscopeReading is
  built on Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGyroscopeReading that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'copyValuesFrom', 'x',
  'setX', 'y', 'setY', 'z', 'setZ'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGyroscopeReading::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGyroscopeReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGyroscopeReading::~QGyroscopeReading()': the destructor: Python
    never removes a C++ QGyroscopeReading.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGyroscopeReading is created at the first use, not by
    'QGyroscopeReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGyroscopeReading.
  - Qt tells when it has removed the C++ QGyroscopeReading. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QGyroscopeReading::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#tr

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
    #  QString QGyroscopeReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QGyroscopeReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGyroscopeReading'

  #  A C++ QGyroscopeReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGyroscopeReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGyroscopeReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGyroscopeReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGyroscopeReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QGyroscopeReading::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#x
    """
    #  qreal QGyroscopeReading::x() const
    return self.uglySide.call('ritual_ZNK17QGyroscopeReading1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QGyroscopeReading::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#y
    """
    #  qreal QGyroscopeReading::y() const
    return self.uglySide.call('ritual_ZNK17QGyroscopeReading1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QGyroscopeReading::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#z
    """
    #  qreal QGyroscopeReading::z() const
    return self.uglySide.call('ritual_ZNK17QGyroscopeReading1zEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QGyroscopeReading::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QGyroscopeReading::setX(qreal x)
    self.uglySide.call('ritual_ZN17QGyroscopeReading4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QGyroscopeReading::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QGyroscopeReading::setY(qreal y)
    self.uglySide.call('ritual_ZN17QGyroscopeReading4setYEd', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QGyroscopeReading::setZ(qreal z)'.

    Qt's own words: https://doc.qt.io/qt-6/qgyroscopereading.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QGyroscopeReading::setZ(qreal z)
    self.uglySide.call('ritual_ZN17QGyroscopeReading4setZEd', z)

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
    Notes what was given, for Qt's
    'QGyroscopeReading::QGyroscopeReading(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgyroscopereading.html#QGyroscopeReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGyroscopeReading::QGyroscopeReading(QObject *parent)
    self._noteCreation(QGyroscopeReading, lambda: Rituals.call(
        'ritual_ZN17QGyroscopeReadingC1EP7QObject',
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
    Calls Qt's 'void QGyroscopeReading::copyValuesFrom(QSensorReading
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgyroscopereading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGyroscopeReading::copyValuesFrom(QSensorReading *other)
    ritual = 'ritual_ZN17QGyroscopeReading14copyValuesFromEP14QSensorReading'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGyroscopeReading14copyValuesFromEP14QSensorReadi'
          'ng')
    self.uglySide.call(ritual, self._addressOf(other))
