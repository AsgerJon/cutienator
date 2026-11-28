"""
QCandlestickSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qcandlestickset.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QPen
  from . import QCandlestickSetPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QPen = WAIT['QPen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCandlestickSet(QObject):
  """
  The cute side of Qt's QCandlestickSet: a plain Python object standing in
  front of one C++ QCandlestickSet.

  It is built on the cute 'QObject', as Qt's QCandlestickSet is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCandlestickSet that has a ritual and that Python
  can call so far, 29 names in all: 'metaObject', 'tr', 'setTimestamp',
  'timestamp', 'setOpen', 'open', 'setHigh', 'high', 'setLow', 'low',
  'setClose', 'close', 'setBrush', 'brush', 'setPen', 'pen', 'clicked',
  'hovered', 'pressed', 'released', 'doubleClicked', 'timestampChanged',
  'openChanged', 'highChanged', 'lowChanged', 'closeChanged', 'brushChanged',
  'penChanged', 'd_func'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCandlestickSet::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCandlestickSet::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCandlestickSet::~QCandlestickSet()': the destructor: Python never
    removes a C++ QCandlestickSet.
  - Qt's 'const QCandlestickSetPrivate *QCandlestickSet::d_func() const':
    takes in Python what 'QCandlestickSetPrivate *QCandlestickSet::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCandlestickSet is created at the first use, not by
    'QCandlestickSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCandlestickSet.
  - Qt tells when it has removed the C++ QCandlestickSet. Every call on the
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
    Calls Qt's 'QString QCandlestickSet::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#tr

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
    #  QString QCandlestickSet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QCandlestickSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCandlestickSet'

  #  A C++ QCandlestickSet Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCandlestickSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCandlestickSet::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCandlestickSet::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QCandlestickSet10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def timestamp(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSet::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#timestamp
    """
    #  qreal QCandlestickSet::timestamp() const
    return self.uglySide.call('ritual_ZNK15QCandlestickSet9timestampEv')

  def open(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSet::open() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#open
    """
    #  qreal QCandlestickSet::open() const
    return self.uglySide.call('ritual_ZNK15QCandlestickSet4openEv')

  def high(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSet::high() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#high
    """
    #  qreal QCandlestickSet::high() const
    return self.uglySide.call('ritual_ZNK15QCandlestickSet4highEv')

  def low(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSet::low() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#low
    """
    #  qreal QCandlestickSet::low() const
    return self.uglySide.call('ritual_ZNK15QCandlestickSet3lowEv')

  def close(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSet::close() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#close
    """
    #  qreal QCandlestickSet::close() const
    return self.uglySide.call('ritual_ZNK15QCandlestickSet5closeEv')

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QCandlestickSet::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QCandlestickSet::brush() const
    address = self.uglySide.call('ritual_ZNK15QCandlestickSet5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QCandlestickSet::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QCandlestickSet::pen() const
    address = self.uglySide.call('ritual_ZNK15QCandlestickSet3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTimestamp(self, timestamp: float) -> None:
    """
    Calls Qt's 'void QCandlestickSet::setTimestamp(qreal timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#setTimestamp

    Parameters
    ----------

    timestamp : float
      Passed on as it is.
    """
    #  void QCandlestickSet::setTimestamp(qreal timestamp)
    self.uglySide.call(
        'ritual_ZN15QCandlestickSet12setTimestampEd', timestamp,
    )

  @overload(float)
  def setOpen(self, open: float) -> None:
    """
    Calls Qt's 'void QCandlestickSet::setOpen(qreal open)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#setOpen

    Parameters
    ----------

    open : float
      Passed on as it is.
    """
    #  void QCandlestickSet::setOpen(qreal open)
    self.uglySide.call('ritual_ZN15QCandlestickSet7setOpenEd', open)

  @overload(float)
  def setHigh(self, high: float) -> None:
    """
    Calls Qt's 'void QCandlestickSet::setHigh(qreal high)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#setHigh

    Parameters
    ----------

    high : float
      Passed on as it is.
    """
    #  void QCandlestickSet::setHigh(qreal high)
    self.uglySide.call('ritual_ZN15QCandlestickSet7setHighEd', high)

  @overload(float)
  def setLow(self, low: float) -> None:
    """
    Calls Qt's 'void QCandlestickSet::setLow(qreal low)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#setLow

    Parameters
    ----------

    low : float
      Passed on as it is.
    """
    #  void QCandlestickSet::setLow(qreal low)
    self.uglySide.call('ritual_ZN15QCandlestickSet6setLowEd', low)

  @overload(float)
  def setClose(self, close: float) -> None:
    """
    Calls Qt's 'void QCandlestickSet::setClose(qreal close)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#setClose

    Parameters
    ----------

    close : float
      Passed on as it is.
    """
    #  void QCandlestickSet::setClose(qreal close)
    self.uglySide.call('ritual_ZN15QCandlestickSet8setCloseEd', close)

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QCandlestickSet::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QCandlestickSet::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN15QCandlestickSet8setBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QCandlestickSet::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QCandlestickSet::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN15QCandlestickSet6setPenERK4QPen', self._valueOf(pen),
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
  @overload(float)
  @overload(float, QObject)
  @overload(float, NoneType)
  def __init__(
      self,
      timestamp: float = 0.0,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCandlestickSet::QCandlestickSet(qreal
    timestamp, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickset.html#QCandlestickSet

    Parameters
    ----------

    timestamp : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCandlestickSet::QCandlestickSet(qreal timestamp, QObject *parent)
    self._noteCreation(QCandlestickSet, lambda: Rituals.call(
        'ritual_ZN15QCandlestickSetC1EdP7QObject',
        timestamp, self._addressOf(parent, 'QObject'),
    ))

  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, QObject)
  @overload(float, float, float, float, float, NoneType)
  def __init__(
      self,
      open: float,
      high: float,
      low: float,
      close: float,
      timestamp: float = 0.0,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCandlestickSet::QCandlestickSet(qreal
    open, qreal high, qreal low, qreal close, qreal timestamp, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickset.html#QCandlestickSet

    Parameters
    ----------

    open : float
      Passed on as it is.

    high : float
      Passed on as it is.

    low : float
      Passed on as it is.

    close : float
      Passed on as it is.

    timestamp : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCandlestickSet::QCandlestickSet(qreal open, qreal high, qreal low,
    #      qreal close, qreal timestamp, QObject *parent)
    self._noteCreation(QCandlestickSet, lambda: Rituals.call(
        'ritual_ZN15QCandlestickSetC1EdddddP7QObject',
        open, high, low, close, timestamp, self._addressOf(parent,
        'QObject'),
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

  def clicked(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::clicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#clicked
    """
    #  void QCandlestickSet::clicked()
    self.uglySide.call('ritual_ZN15QCandlestickSet7clickedEv')

  @overload(bool)
  def hovered(self, status: bool) -> None:
    """
    Calls Qt's 'void QCandlestickSet::hovered(bool status)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.
    """
    #  void QCandlestickSet::hovered(bool status)
    self.uglySide.call('ritual_ZN15QCandlestickSet7hoveredEb', status)

  def pressed(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::pressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#pressed
    """
    #  void QCandlestickSet::pressed()
    self.uglySide.call('ritual_ZN15QCandlestickSet7pressedEv')

  def released(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::released()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#released
    """
    #  void QCandlestickSet::released()
    self.uglySide.call('ritual_ZN15QCandlestickSet8releasedEv')

  def doubleClicked(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::doubleClicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#doubleClicked
    """
    #  void QCandlestickSet::doubleClicked()
    self.uglySide.call('ritual_ZN15QCandlestickSet13doubleClickedEv')

  def timestampChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::timestampChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickset.html#timestampChanged
    """
    #  void QCandlestickSet::timestampChanged()
    self.uglySide.call('ritual_ZN15QCandlestickSet16timestampChangedEv')

  def openChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::openChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#openChanged
    """
    #  void QCandlestickSet::openChanged()
    self.uglySide.call('ritual_ZN15QCandlestickSet11openChangedEv')

  def highChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::highChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#highChanged
    """
    #  void QCandlestickSet::highChanged()
    self.uglySide.call('ritual_ZN15QCandlestickSet11highChangedEv')

  def lowChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::lowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#lowChanged
    """
    #  void QCandlestickSet::lowChanged()
    self.uglySide.call('ritual_ZN15QCandlestickSet10lowChangedEv')

  def closeChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::closeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#closeChanged
    """
    #  void QCandlestickSet::closeChanged()
    self.uglySide.call('ritual_ZN15QCandlestickSet12closeChangedEv')

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::brushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#brushChanged
    """
    #  void QCandlestickSet::brushChanged()
    self.uglySide.call('ritual_ZN15QCandlestickSet12brushChangedEv')

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSet::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#penChanged
    """
    #  void QCandlestickSet::penChanged()
    self.uglySide.call('ritual_ZN15QCandlestickSet10penChangedEv')

  def d_func(self) -> Optional[QCandlestickSetPrivate]:
    """
    Calls Qt's 'QCandlestickSetPrivate *QCandlestickSet::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickset.html#d_func

    Returns
    -------

    Optional[QCandlestickSetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickSetPrivate *QCandlestickSet::d_func()
    address = self.uglySide.call('ritual_ZN15QCandlestickSet6d_funcEv')
    from . import QCandlestickSetPrivate
    return QCandlestickSetPrivate._cuteAt(address)


#  Qt's 'QList<QCandlestickSet *>': the list of QCandlestickSet, which
#  'QList[QCandlestickSet]' gives. It is made here, so that there is one as
#  soon as there can be a QCandlestickSet.
QList.createKind(
    QCandlestickSet, 'address',
    make='ritual_list_make_QCandlestickSet_ptr',
    add='ritual_list_add_QCandlestickSet_ptr',
    size='ritual_list_size_QCandlestickSet_ptr',
    at='ritual_list_at_QCandlestickSet_ptr',
    drop='ritual_list_drop_QCandlestickSet_ptr',
)
