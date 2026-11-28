"""
XLogYDomain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/xlogydomain_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means XLogYDomain to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import AbstractDomain

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


class XLogYDomain(AbstractDomain):
  """
  The cute side of Qt's XLogYDomain: a plain Python object standing in front
  of one C++ XLogYDomain.

  It is built on the cute 'AbstractDomain', as Qt's XLogYDomain is built on
  Qt's AbstractDomain, and has everything that class has.

  What exists
  -----------

  Every function of Qt's XLogYDomain that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'type', 'setRange',
  'zoomIn', 'zoomOut', 'move', 'calculateDomainPoint',
  'calculateGeometryPoints', 'attachAxis', 'detachAxis',
  'handleVerticalAxisBaseChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *XLogYDomain::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int XLogYDomain::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'XLogYDomain::~XLogYDomain()': the destructor: Python never removes
    a C++ XLogYDomain.
  - Qt's 'QPointF XLogYDomain::calculateGeometryPoint(const QPointF &point,
    bool &ok) const': takes a number to change where it is.

  What has no ritual
  ------------------

  5 of the 22 functions Qt declares: 2 not a gap; 1 leans on
  'operator==(XLogYDomain const&, XLogYDomain const&)', which Qt's source
  does not mark for use from outside Qt and has no code for that could be
  taken; 1 leans on 'operator!=(XLogYDomain const&, XLogYDomain const&)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken; 1 leans on 'operator<<(QDebug, XLogYDomain const&)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ XLogYDomain is created at the first use, not by
    'XLogYDomain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ XLogYDomain.
  - Qt tells when it has removed the C++ XLogYDomain. Every call on the cute
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
    Calls Qt's 'QString XLogYDomain::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#tr

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
    #  QString XLogYDomain::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11XLogYDomain2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'XLogYDomain'

  #  A C++ XLogYDomain Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_XLogYDomain'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *XLogYDomain::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *XLogYDomain::metaObject() const
    address = self.uglySide.call('ritual_ZNK11XLogYDomain10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPointF)
  def calculateDomainPoint(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF XLogYDomain::calculateDomainPoint(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/xlogydomain.html#calculateDomainPoint

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
    #  QPointF XLogYDomain::calculateDomainPoint(const QPointF &point) const
    ritual = 'ritual_ZNK11XLogYDomain20calculateDomainPointERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11XLogYDomain20calculateDomainPointERK7QPointF'
    address = self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QList[QPointF])
  def calculateGeometryPoints(self, list: QList[QPointF]) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> XLogYDomain::calculateGeometryPoints(const
    QList<QPointF> &list) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/xlogydomain.html#calculateGeometryPoints

    Parameters
    ----------

    list : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> XLogYDomain::calculateGeometryPoints(const
    #      QList<QPointF> &list) const
    address = self.uglySide.call(
        'ritual_ZNK11XLogYDomain23calculateGeometryPointsERK5QListI7QPointF'
        'E',
        self._valueOf(list),
    )
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

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
    Calls Qt's 'void XLogYDomain::setRange(qreal minX, qreal maxX, qreal
    minY, qreal maxY)'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#setRange

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
    #  void XLogYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
    #      maxY)
    ritual = 'ritual_ZN11XLogYDomain8setRangeEdddd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11XLogYDomain8setRangeEdddd'
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
    Notes what was given, for Qt's 'XLogYDomain::XLogYDomain(QObject
    *object)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#XLogYDomain

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  XLogYDomain::XLogYDomain(QObject *object)
    self._noteCreation(XLogYDomain, lambda: Rituals.call(
        'ritual_ZN11XLogYDomainC1EP7QObject',
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
    Calls Qt's 'DomainType XLogYDomain::type()'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#type

    Returns
    -------

    AbstractDomain.DomainType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AbstractDomain.DomainType(number)' gives.
    """
    #  DomainType XLogYDomain::type()
    ritual = 'ritual_ZN11XLogYDomain4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11XLogYDomain4typeEv'
    return AbstractDomain.DomainType(self.uglySide.call(ritual))

  @overload(QRectF)
  def zoomIn(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void XLogYDomain::zoomIn(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#zoomIn

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void XLogYDomain::zoomIn(const QRectF &rect)
    ritual = 'ritual_ZN11XLogYDomain6zoomInERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11XLogYDomain6zoomInERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def zoomOut(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void XLogYDomain::zoomOut(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#zoomOut

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void XLogYDomain::zoomOut(const QRectF &rect)
    ritual = 'ritual_ZN11XLogYDomain7zoomOutERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11XLogYDomain7zoomOutERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(float, float)
  def move(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void XLogYDomain::move(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#move

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void XLogYDomain::move(qreal dx, qreal dy)
    ritual = 'ritual_ZN11XLogYDomain4moveEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11XLogYDomain4moveEdd'
    self.uglySide.call(ritual, dx, dy)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def attachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool XLogYDomain::attachAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#attachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool XLogYDomain::attachAxis(QAbstractAxis *axis)
    ritual = 'ritual_ZN11XLogYDomain10attachAxisEP13QAbstractAxis'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11XLogYDomain10attachAxisEP13QAbstractAxis'
    return self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstractAxis)
  @overload(NoneType)
  def detachAxis(self, axis: Optional[QAbstractAxis]) -> bool:
    """
    Calls Qt's 'bool XLogYDomain::detachAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/xlogydomain.html#detachAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool XLogYDomain::detachAxis(QAbstractAxis *axis)
    ritual = 'ritual_ZN11XLogYDomain10detachAxisEP13QAbstractAxis'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11XLogYDomain10detachAxisEP13QAbstractAxis'
    return self.uglySide.call(ritual, self._addressOf(axis))

  @overload(float)
  def handleVerticalAxisBaseChanged(self, baseY: float) -> None:
    """
    Calls Qt's 'void XLogYDomain::handleVerticalAxisBaseChanged(qreal
    baseY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/xlogydomain.html#handleVerticalAxisBaseChanged

    Parameters
    ----------

    baseY : float
      Passed on as it is.
    """
    #  void XLogYDomain::handleVerticalAxisBaseChanged(qreal baseY)
    self.uglySide.call(
        'ritual_ZN11XLogYDomain29handleVerticalAxisBaseChangedEd', baseY,
    )
