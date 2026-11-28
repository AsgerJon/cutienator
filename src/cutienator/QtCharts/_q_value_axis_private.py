"""
QValueAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qvalueaxis_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QValueAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractAxisPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtWidgets import QGraphicsItem
  from . import AbstractDomain, QValueAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractDomain = WAIT['AbstractDomain']
  QGraphicsItem = WAIT['QGraphicsItem']
  QValueAxis = WAIT['QtCharts:QValueAxis']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QValueAxisPrivate(QAbstractAxisPrivate):
  """
  The cute side of Qt's QValueAxisPrivate: a plain Python object standing in
  front of one C++ QValueAxisPrivate.

  It is built on the cute 'QAbstractAxisPrivate', as Qt's QValueAxisPrivate
  is built on Qt's QAbstractAxisPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QValueAxisPrivate that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'initializeGraphics',
  'initializeDomain', 'min', 'max', 'setRange', 'tickInterval', 'tickAnchor',
  'setMin', 'setMax', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QValueAxisPrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QValueAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QValueAxisPrivate::~QValueAxisPrivate()': the destructor: Python
    never removes a C++ QValueAxisPrivate.
  - Qt's 'const QValueAxis *QValueAxisPrivate::q_func() const': takes in
    Python what 'QValueAxis *QValueAxisPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QValueAxisPrivate is created at the first use, not by
    'QValueAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QValueAxisPrivate.
  - Qt tells when it has removed the C++ QValueAxisPrivate. Every call on the
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
    Calls Qt's 'QString QValueAxisPrivate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#tr

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
    #  QString QValueAxisPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QValueAxisPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QValueAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QValueAxisPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QValueAxisPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QValueAxisPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QValueAxisPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QValueAxisPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QValueAxisPrivate::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QValueAxisPrivate::setRange(qreal min, qreal max)
    ritual = 'ritual_ZN17QValueAxisPrivate8setRangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QValueAxisPrivate8setRangeEdd'
    self.uglySide.call(ritual, min, max)

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QValueAxisPrivate::setRange(const QVariant &min, const
    QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
    #      &max)
    ritual = 'ritual_ZN17QValueAxisPrivate8setRangeERK8QVariantS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QValueAxisPrivate8setRangeERK8QVariantS2_'
    self.uglySide.call(ritual, self._valueOf(min), self._valueOf(max))

  @overload(QVariant)
  def setMin(self, min: QVariant) -> None:
    """
    Calls Qt's 'void QValueAxisPrivate::setMin(const QVariant &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#setMin

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QValueAxisPrivate::setMin(const QVariant &min)
    ritual = 'ritual_ZN17QValueAxisPrivate6setMinERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QValueAxisPrivate6setMinERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(min))

  @overload(QVariant)
  def setMax(self, max: QVariant) -> None:
    """
    Calls Qt's 'void QValueAxisPrivate::setMax(const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#setMax

    Parameters
    ----------

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QValueAxisPrivate::setMax(const QVariant &max)
    ritual = 'ritual_ZN17QValueAxisPrivate6setMaxERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QValueAxisPrivate6setMaxERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(max))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValueAxis)
  @overload(NoneType)
  def __init__(self, q: Optional[QValueAxis]) -> None:
    """
    Notes what was given, for Qt's
    'QValueAxisPrivate::QValueAxisPrivate(QValueAxis *q)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxisprivate.html#QValueAxisPrivate

    Parameters
    ----------

    q : Optional[QValueAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QValueAxisPrivate::QValueAxisPrivate(QValueAxis *q)
    self._noteCreation(QValueAxisPrivate, lambda: Rituals.call(
        'ritual_ZN17QValueAxisPrivateC1EP10QValueAxis', self._addressOf(q),
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

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QValueAxisPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxisprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN17QValueAxisPrivate18initializeGraphicsEP13QGraphicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QValueAxisPrivate18initializeGraphicsEP13QGraphic'
          'sItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  @overload(AbstractDomain)
  @overload(NoneType)
  def initializeDomain(self, domain: Optional[AbstractDomain]) -> None:
    """
    Calls Qt's 'void QValueAxisPrivate::initializeDomain(AbstractDomain
    *domain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxisprivate.html#initializeDomain

    Parameters
    ----------

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QValueAxisPrivate::initializeDomain(AbstractDomain *domain)
    ritual = (
        'ritual_ZN17QValueAxisPrivate16initializeDomainEP14AbstractDomain')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QValueAxisPrivate16initializeDomainEP14AbstractDo'
          'main')
    self.uglySide.call(ritual, self._addressOf(domain))

  def min(self) -> float:
    """
    Calls Qt's 'qreal QValueAxisPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#min
    """
    #  qreal QValueAxisPrivate::min()
    ritual = 'ritual_ZN17QValueAxisPrivate3minEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QValueAxisPrivate3minEv'
    return self.uglySide.call(ritual)

  def max(self) -> float:
    """
    Calls Qt's 'qreal QValueAxisPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#max
    """
    #  qreal QValueAxisPrivate::max()
    ritual = 'ritual_ZN17QValueAxisPrivate3maxEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QValueAxisPrivate3maxEv'
    return self.uglySide.call(ritual)

  def tickInterval(self) -> float:
    """
    Calls Qt's 'qreal QValueAxisPrivate::tickInterval()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxisprivate.html#tickInterval
    """
    #  qreal QValueAxisPrivate::tickInterval()
    return self.uglySide.call('ritual_ZN17QValueAxisPrivate12tickIntervalEv')

  def tickAnchor(self) -> float:
    """
    Calls Qt's 'qreal QValueAxisPrivate::tickAnchor()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#tickAnchor
    """
    #  qreal QValueAxisPrivate::tickAnchor()
    return self.uglySide.call('ritual_ZN17QValueAxisPrivate10tickAnchorEv')

  def q_func(self) -> Optional[QValueAxis]:
    """
    Calls Qt's 'QValueAxis *QValueAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxisprivate.html#q_func

    Returns
    -------

    Optional[QValueAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValueAxis *QValueAxisPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QValueAxisPrivate6q_funcEv')
    from . import QValueAxis
    return QValueAxis._cuteAt(address)
