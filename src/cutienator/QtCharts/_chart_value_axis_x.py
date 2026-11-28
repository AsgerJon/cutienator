"""
ChartValueAxisX binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartvalueaxisx_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ChartValueAxisX to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsItem
from . import HorizontalAxis, QValueAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartValueAxisX(HorizontalAxis):
  """
  The cute side of Qt's ChartValueAxisX: a plain Python object standing in
  front of one C++ ChartValueAxisX.

  It is built on the cute 'HorizontalAxis', as Qt's ChartValueAxisX is built
  on Qt's HorizontalAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartValueAxisX that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'sizeHint',
  'updateGeometry', 'handleTickCountChanged', 'handleMinorTickCountChanged',
  'handleLabelFormatChanged', 'handleTickIntervalChanged',
  'handleTickAnchorChanged', 'handleTickTypeChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartValueAxisX::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int ChartValueAxisX::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'ChartValueAxisX::~ChartValueAxisX()': the destructor: Python never
    removes a C++ ChartValueAxisX.
  - Qt's 'QList<qreal> ChartValueAxisX::calculateLayout() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ChartValueAxisX is created at the first use, not by
    'ChartValueAxisX(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartValueAxisX.
  - Qt tells when it has removed the C++ ChartValueAxisX. Every call on the
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
    Calls Qt's 'QString ChartValueAxisX::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartvalueaxisx.html#tr

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
    #  QString ChartValueAxisX::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15ChartValueAxisX2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartValueAxisX'

  #  A C++ ChartValueAxisX Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ChartValueAxisX'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ChartValueAxisX::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartvalueaxisx.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartValueAxisX::metaObject() const
    address = self.uglySide.call('ritual_ZNK15ChartValueAxisX10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF ChartValueAxisX::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/chartvalueaxisx.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF ChartValueAxisX::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    ritual = 'ritual_ZNK15ChartValueAxisX8sizeHintEN2Qt8SizeHintERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15ChartValueAxisX8sizeHintEN2Qt8SizeHintERK6QSizeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

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

  @overload(QValueAxis)
  @overload(NoneType)
  @overload(QValueAxis, QGraphicsItem)
  @overload(QValueAxis, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      axis: Optional[QValueAxis],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'ChartValueAxisX::ChartValueAxisX(QValueAxis *axis, QGraphicsItem
    *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#ChartValueAxisX

    Parameters
    ----------

    axis : Optional[QValueAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ChartValueAxisX::ChartValueAxisX(QValueAxis *axis, QGraphicsItem
    #      *item)
    self._noteCreation(ChartValueAxisX, lambda: Rituals.call(
        'ritual_ZN15ChartValueAxisXC1EP10QValueAxisP13QGraphicsItem',
        self._addressOf(axis), self._addressOf(item, 'QGraphicsItem'),
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

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void ChartValueAxisX::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#updateGeometry
    """
    #  void ChartValueAxisX::updateGeometry()
    ritual = 'ritual_ZN15ChartValueAxisX14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15ChartValueAxisX14updateGeometryEv'
    self.uglySide.call(ritual)

  @overload(int)
  def handleTickCountChanged(self, tick: int) -> None:
    """
    Calls Qt's 'void ChartValueAxisX::handleTickCountChanged(int tick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#handleTickCountChanged

    Parameters
    ----------

    tick : int
      Passed on as it is.
    """
    #  void ChartValueAxisX::handleTickCountChanged(int tick)
    self.uglySide.call(
        'ritual_ZN15ChartValueAxisX22handleTickCountChangedEi', tick,
    )

  @overload(int)
  def handleMinorTickCountChanged(self, tick: int) -> None:
    """
    Calls Qt's 'void ChartValueAxisX::handleMinorTickCountChanged(int tick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#handleMinorTickCountChanged

    Parameters
    ----------

    tick : int
      Passed on as it is.
    """
    #  void ChartValueAxisX::handleMinorTickCountChanged(int tick)
    self.uglySide.call(
        'ritual_ZN15ChartValueAxisX27handleMinorTickCountChangedEi', tick,
    )

  @overload(str)
  def handleLabelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void ChartValueAxisX::handleLabelFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#handleLabelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ChartValueAxisX::handleLabelFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN15ChartValueAxisX24handleLabelFormatChangedERK7QString',
        format,
    )

  @overload(float)
  def handleTickIntervalChanged(self, interval: float) -> None:
    """
    Calls Qt's 'void ChartValueAxisX::handleTickIntervalChanged(qreal
    interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#handleTickIntervalChanged

    Parameters
    ----------

    interval : float
      Passed on as it is.
    """
    #  void ChartValueAxisX::handleTickIntervalChanged(qreal interval)
    self.uglySide.call(
        'ritual_ZN15ChartValueAxisX25handleTickIntervalChangedEd', interval,
    )

  @overload(float)
  def handleTickAnchorChanged(self, anchor: float) -> None:
    """
    Calls Qt's 'void ChartValueAxisX::handleTickAnchorChanged(qreal anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#handleTickAnchorChanged

    Parameters
    ----------

    anchor : float
      Passed on as it is.
    """
    #  void ChartValueAxisX::handleTickAnchorChanged(qreal anchor)
    self.uglySide.call(
        'ritual_ZN15ChartValueAxisX23handleTickAnchorChangedEd', anchor,
    )

  @overload(QValueAxis.TickType)
  def handleTickTypeChanged(self, type: QValueAxis.TickType) -> None:
    """
    Calls Qt's 'void
    ChartValueAxisX::handleTickTypeChanged(QValueAxis::TickType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartvalueaxisx.html#handleTickTypeChanged

    Parameters
    ----------

    type : QValueAxis.TickType
      Passed on as its number.
    """
    #  void ChartValueAxisX::handleTickTypeChanged(QValueAxis::TickType type)
    self.uglySide.call(
        'ritual_ZN15ChartValueAxisX21handleTickTypeChangedEN10QValueAxis8Ti'
        'ckTypeE',
        type.value,
    )
