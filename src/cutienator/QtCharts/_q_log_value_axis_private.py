"""
QLogValueAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qlogvalueaxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLogValueAxisPrivate to be private: it declares the class in a
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
  from . import AbstractDomain, QLogValueAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractDomain = WAIT['AbstractDomain']
  QGraphicsItem = WAIT['QGraphicsItem']
  QLogValueAxis = WAIT['QtCharts:QLogValueAxis']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLogValueAxisPrivate(QAbstractAxisPrivate):
  """
  The cute side of Qt's QLogValueAxisPrivate: a plain Python object standing
  in front of one C++ QLogValueAxisPrivate.

  It is built on the cute 'QAbstractAxisPrivate', as Qt's
  QLogValueAxisPrivate is built on Qt's QAbstractAxisPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QLogValueAxisPrivate that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr',
  'initializeGraphics', 'initializeDomain', 'min', 'max', 'setRange',
  'updateTickCount', 'setMin', 'setMax', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLogValueAxisPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QLogValueAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QLogValueAxisPrivate::~QLogValueAxisPrivate()': the destructor:
    Python never removes a C++ QLogValueAxisPrivate.
  - Qt's 'const QLogValueAxis *QLogValueAxisPrivate::q_func() const': takes
    in Python what 'QLogValueAxis *QLogValueAxisPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QLogValueAxisPrivate is created at the first use, not by
    'QLogValueAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLogValueAxisPrivate.
  - Qt tells when it has removed the C++ QLogValueAxisPrivate. Every call on
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
    Calls Qt's 'QString QLogValueAxisPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#tr

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
    #  QString QLogValueAxisPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QLogValueAxisPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLogValueAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QLogValueAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLogValueAxisPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLogValueAxisPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLogValueAxisPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QLogValueAxisPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QLogValueAxisPrivate::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QLogValueAxisPrivate::setRange(qreal min, qreal max)
    ritual = 'ritual_ZN20QLogValueAxisPrivate8setRangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLogValueAxisPrivate8setRangeEdd'
    self.uglySide.call(ritual, min, max)

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QLogValueAxisPrivate::setRange(const QVariant &min,
    const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QLogValueAxisPrivate::setRange(const QVariant &min, const
    #      QVariant &max)
    ritual = 'ritual_ZN20QLogValueAxisPrivate8setRangeERK8QVariantS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLogValueAxisPrivate8setRangeERK8QVariantS2_'
    self.uglySide.call(ritual, self._valueOf(min), self._valueOf(max))

  @overload(QVariant)
  def setMin(self, min: QVariant) -> None:
    """
    Calls Qt's 'void QLogValueAxisPrivate::setMin(const QVariant &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#setMin

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QLogValueAxisPrivate::setMin(const QVariant &min)
    ritual = 'ritual_ZN20QLogValueAxisPrivate6setMinERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLogValueAxisPrivate6setMinERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(min))

  @overload(QVariant)
  def setMax(self, max: QVariant) -> None:
    """
    Calls Qt's 'void QLogValueAxisPrivate::setMax(const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#setMax

    Parameters
    ----------

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QLogValueAxisPrivate::setMax(const QVariant &max)
    ritual = 'ritual_ZN20QLogValueAxisPrivate6setMaxERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLogValueAxisPrivate6setMaxERK8QVariant'
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

  @overload(QLogValueAxis)
  @overload(NoneType)
  def __init__(self, q: Optional[QLogValueAxis]) -> None:
    """
    Notes what was given, for Qt's
    'QLogValueAxisPrivate::QLogValueAxisPrivate(QLogValueAxis *q)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#QLogValueAxisPrivate

    Parameters
    ----------

    q : Optional[QLogValueAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QLogValueAxisPrivate::QLogValueAxisPrivate(QLogValueAxis *q)
    self._noteCreation(QLogValueAxisPrivate, lambda: Rituals.call(
        'ritual_ZN20QLogValueAxisPrivateC1EP13QLogValueAxis',
        self._addressOf(q),
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
    Calls Qt's 'void QLogValueAxisPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLogValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN20QLogValueAxisPrivate18initializeGraphicsEP13QGraphicsIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QLogValueAxisPrivate18initializeGraphicsEP13QGrap'
          'hicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  @overload(AbstractDomain)
  @overload(NoneType)
  def initializeDomain(self, domain: Optional[AbstractDomain]) -> None:
    """
    Calls Qt's 'void QLogValueAxisPrivate::initializeDomain(AbstractDomain
    *domain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#initializeDomain

    Parameters
    ----------

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLogValueAxisPrivate::initializeDomain(AbstractDomain *domain)
    ritual = (
        'ritual_ZN20QLogValueAxisPrivate16initializeDomainEP14AbstractDomai'
        'n')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QLogValueAxisPrivate16initializeDomainEP14Abstrac'
          'tDomain')
    self.uglySide.call(ritual, self._addressOf(domain))

  def min(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxisPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#min
    """
    #  qreal QLogValueAxisPrivate::min()
    ritual = 'ritual_ZN20QLogValueAxisPrivate3minEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLogValueAxisPrivate3minEv'
    return self.uglySide.call(ritual)

  def max(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxisPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#max
    """
    #  qreal QLogValueAxisPrivate::max()
    ritual = 'ritual_ZN20QLogValueAxisPrivate3maxEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLogValueAxisPrivate3maxEv'
    return self.uglySide.call(ritual)

  def updateTickCount(self) -> None:
    """
    Calls Qt's 'void QLogValueAxisPrivate::updateTickCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#updateTickCount
    """
    #  void QLogValueAxisPrivate::updateTickCount()
    self.uglySide.call('ritual_ZN20QLogValueAxisPrivate15updateTickCountEv')

  def q_func(self) -> Optional[QLogValueAxis]:
    """
    Calls Qt's 'QLogValueAxis *QLogValueAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxisprivate.html#q_func

    Returns
    -------

    Optional[QLogValueAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLogValueAxis *QLogValueAxisPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QLogValueAxisPrivate6q_funcEv')
    from . import QLogValueAxis
    return QLogValueAxis._cuteAt(address)
