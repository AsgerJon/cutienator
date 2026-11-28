"""
LogXLogYPolarDomain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/logxlogypolardomain_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means LogXLogYPolarDomain to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import AbstractDomain, PolarDomain

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from . import QAbstractAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LogXLogYPolarDomain(PolarDomain):
  """
  The cute side of Qt's LogXLogYPolarDomain: a plain Python object standing
  in front of one C++ LogXLogYPolarDomain.

  It is built on the cute 'PolarDomain', as Qt's LogXLogYPolarDomain is built
  on Qt's PolarDomain, and has everything that class has.

  What exists
  -----------

  Every function of Qt's LogXLogYPolarDomain that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'type',
  'setRange', 'zoomIn', 'zoomOut', 'move', 'calculateDomainPoint',
  'attachAxis', 'detachAxis', 'handleVerticalAxisBaseChanged',
  'handleHorizontalAxisBaseChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LogXLogYPolarDomain::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int LogXLogYPolarDomain::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'LogXLogYPolarDomain::~LogXLogYPolarDomain()': the destructor:
    Python never removes a C++ LogXLogYPolarDomain.
  - Qt's 'qreal LogXLogYPolarDomain::toAngularCoordinate(qreal value, bool
    &ok) const': takes a number to change where it is.
  - Qt's 'qreal LogXLogYPolarDomain::toRadialCoordinate(qreal value, bool
    &ok) const': takes a number to change where it is.

  What has no ritual
  ------------------

  5 of the 23 functions Qt declares: 2 not a gap; 1 leans on
  'operator==(LogXLogYPolarDomain const&, LogXLogYPolarDomain const&)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken; 1 leans on 'operator!=(LogXLogYPolarDomain const&,
  LogXLogYPolarDomain const&)', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'operator<<(QDebug, LogXLogYPolarDomain const&)', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ LogXLogYPolarDomain is created at the first use, not by
    'LogXLogYPolarDomain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LogXLogYPolarDomain.
  - Qt tells when it has removed the C++ LogXLogYPolarDomain. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString LogXLogYPolarDomain::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/logxlogypolardomain.html#tr

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
    #  QString LogXLogYPolarDomain::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19LogXLogYPolarDomain2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LogXLogYPolarDomain'

  #  A C++ LogXLogYPolarDomain Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LogXLogYPolarDomain'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LogXLogYPolarDomain::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/logxlogypolardomain.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LogXLogYPolarDomain::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19LogXLogYPolarDomain10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPointF)
  def calculateDomainPoint(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF LogXLogYPolarDomain::calculateDomainPoint(const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/logxlogypolardomain.html#calculateDomainPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF LogXLogYPolarDomain::calculateDomainPoint(const QPointF
    #      &point) const
    ritual = (
        'ritual_ZNK19LogXLogYPolarDomain20calculateDomainPointERK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19LogXLogYPolarDomain20calculateDomainPointERK7QPo'
          'intF')
    address = self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, float, float)
  def setRange(
      self,
      minX: float,
      maxX: float,
      minY: float,
      maxY: float,
  ) -> None:
    """
    Calls Qt's 'void LogXLogYPolarDomain::setRange(qreal minX, qreal maxX,
    qreal minY, qreal maxY)'.

    Qt's own words: https://doc.qt.io/qt-6/logxlogypolardomain.html#setRange

    Parameters
    ----------

    minX : float
      Passed on as it is.

    maxX : float
      Passed on as it is.

    minY : float
      Passed on as it is.

    maxY : float
      Passed on as it is.
    """
    #  void LogXLogYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY,
    #      qreal maxY)
    ritual = 'ritual_ZN19LogXLogYPolarDomain8setRangeEdddd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19LogXLogYPolarDomain8setRangeEdddd'
    self.uglySide.call(ritual, minX, maxX, minY, maxY)

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
  def __init__(self, object: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'LogXLogYPolarDomain::LogXLogYPolarDomain(QObject *object)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/logxlogypolardomain.html#LogXLogYPolarDomain

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  LogXLogYPolarDomain::LogXLogYPolarDomain(QObject *object)
    self._noteCreation(LogXLogYPolarDomain, lambda: Rituals.call(
        'ritual_ZN19LogXLogYPolarDomainC1EP7QObject',
        self._addressOf(object, 'QObject'),
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

  def type(self) -> AbstractDomain.DomainType:
    """
    Calls Qt's 'DomainType LogXLogYPolarDomain::type()'.

    Qt's own words: https://doc.qt.io/qt-6/logxlogypolardomain.html#type

    Returns
    -------

    AbstractDomain.DomainType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AbstractDomain.DomainType(number)' gives.
    """
    #  DomainType LogXLogYPolarDomain::type()
    ritual = 'ritual_ZN19LogXLogYPolarDomain4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19LogXLogYPolarDomain4typeEv'
    return AbstractDomain.DomainType(self.uglySide.call(ritual))

  @overload(QRectF)
  def zoomIn(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void LogXLogYPolarDomain::zoomIn(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/logxlogypolardomain.html#zoomIn

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void LogXLogYPolarDomain::zoomIn(const QRectF &rect)
    ritual = 'ritual_ZN19LogXLogYPolarDomain6zoomInERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19LogXLogYPolarDomain6zoomInERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def zoomOut(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void LogXLogYPolarDomain::zoomOut(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/logxlogypolardomain.html#zoomOut

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void LogXLogYPolarDomain::zoomOut(const QRectF &rect)
    ritual = 'ritual_ZN19LogXLogYPolarDomain7zoomOutERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19LogXLogYPolarDomain7zoomOutERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(float, float)
  def move(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void LogXLogYPolarDomain::move(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/logxlogypolardomain.html#move

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void LogXLogYPolarDomain::move(qreal dx, qreal dy)
    ritual = 'ritual_ZN19LogXLogYPolarDomain4moveEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19LogXLogYPolarDomain4moveEdd'
    self.uglySide.call(ritual, dx, dy)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def attachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool LogXLogYPolarDomain::attachAxis(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/logxlogypolardomain.html#attachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool LogXLogYPolarDomain::attachAxis(QAbstractAxis *axis)
    ritual = 'ritual_ZN19LogXLogYPolarDomain10attachAxisEP13QAbstractAxis'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19LogXLogYPolarDomain10attachAxisEP13QAbstractAxis')
    return self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstractAxis)
  @overload(NoneType)
  def detachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool LogXLogYPolarDomain::detachAxis(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/logxlogypolardomain.html#detachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool LogXLogYPolarDomain::detachAxis(QAbstractAxis *axis)
    ritual = 'ritual_ZN19LogXLogYPolarDomain10detachAxisEP13QAbstractAxis'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19LogXLogYPolarDomain10detachAxisEP13QAbstractAxis')
    return self.uglySide.call(ritual, self._addressOf(axis))

  @overload(float)
  def handleVerticalAxisBaseChanged(self, baseY: float) -> None:
    """
    Calls Qt's 'void LogXLogYPolarDomain::handleVerticalAxisBaseChanged(qreal
    baseY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/logxlogypolardomain.html

    Parameters
    ----------

    baseY : float
      Passed on as it is.
    """
    #  void LogXLogYPolarDomain::handleVerticalAxisBaseChanged(qreal baseY)
    self.uglySide.call(
        'ritual_ZN19LogXLogYPolarDomain29handleVerticalAxisBaseChangedEd',
        baseY,
    )

  @overload(float)
  def handleHorizontalAxisBaseChanged(self, baseX: float) -> None:
    """
    Calls Qt's 'void
    LogXLogYPolarDomain::handleHorizontalAxisBaseChanged(qreal baseX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/logxlogypolardomain.html

    Parameters
    ----------

    baseX : float
      Passed on as it is.
    """
    #  void LogXLogYPolarDomain::handleHorizontalAxisBaseChanged(qreal baseX)
    self.uglySide.call(
        'ritual_ZN19LogXLogYPolarDomain31handleHorizontalAxisBaseChangedEd',
        baseX,
    )
