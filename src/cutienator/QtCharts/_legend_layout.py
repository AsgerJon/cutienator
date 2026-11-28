"""
LegendLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/legendlayout_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means LegendLayout to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsLayout, QGraphicsLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF, QSizeF
  from . import QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLegend = WAIT['QLegend']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LegendLayout(QGraphicsLayout):
  """
  The cute side of Qt's LegendLayout: a plain Python object standing in front
  of one C++ LegendLayout.

  It is built on the cute 'QGraphicsLayout', as Qt's LegendLayout is built on
  Qt's QGraphicsLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's LegendLayout that has a ritual and that Python can
  call so far, 10 names in all: 'setGeometry', 'setOffset', 'offset',
  'invalidate', 'sizeHint', 'count', 'itemAt', 'removeAt',
  'setAttachedGeometry', 'setDettachedGeometry'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'LegendLayout::~LegendLayout()': the destructor: Python never
    removes a C++ LegendLayout.
  - Qt's 'bool LegendLayout::widthLongerThan(const LegendWidthStruct *item1,
    const LegendWidthStruct *item2)': names
    'LegendLayout::LegendWidthStruct', which has no cute class yet.

  What to expect
  --------------

  - The C++ LegendLayout is created at the first use, not by
    'LegendLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LegendLayout.
  - Each name of Qt's LegendLayout that has no cute function yet,
    'widthLongerThan', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LegendLayout'

  #  A C++ LegendLayout Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LegendLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF LegendLayout::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF LegendLayout::offset() const
    address = self.uglySide.call('ritual_ZNK12LegendLayout6offsetEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF LegendLayout::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF()' is then passed on.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF LegendLayout::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    ritual = 'ritual_ZNK12LegendLayout8sizeHintEN2Qt8SizeHintERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12LegendLayout8sizeHintEN2Qt8SizeHintERK6QSizeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int LegendLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#count
    """
    #  int LegendLayout::count() const
    ritual = 'ritual_ZNK12LegendLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12LegendLayout5countEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def itemAt(self, a0: int) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *LegendLayout::itemAt(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#itemAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *LegendLayout::itemAt(int a0) const
    ritual = 'ritual_ZNK12LegendLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12LegendLayout6itemAtEi'
    address = self.uglySide.call(ritual, a0)
    return QGraphicsLayoutItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void LegendLayout::setGeometry(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void LegendLayout::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN12LegendLayout11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12LegendLayout11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(float, float)
  def setOffset(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void LegendLayout::setOffset(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#setOffset

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void LegendLayout::setOffset(qreal x, qreal y)
    self.uglySide.call('ritual_ZN12LegendLayout9setOffsetEdd', x, y)

  @overload(QRectF)
  def setAttachedGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void LegendLayout::setAttachedGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendlayout.html#setAttachedGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void LegendLayout::setAttachedGeometry(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12LegendLayout19setAttachedGeometryERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def setDettachedGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void LegendLayout::setDettachedGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendlayout.html#setDettachedGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void LegendLayout::setDettachedGeometry(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12LegendLayout20setDettachedGeometryERK6QRectF',
        self._valueOf(rect),
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

  @overload(QLegend)
  @overload(NoneType)
  def __init__(self, legend: Optional[QLegend]) -> None:
    """
    Notes what was given, for Qt's 'LegendLayout::LegendLayout(QLegend
    *legend)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#LegendLayout

    Parameters
    ----------

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  LegendLayout::LegendLayout(QLegend *legend)
    self._noteCreation(LegendLayout, lambda: Rituals.call(
        'ritual_ZN12LegendLayoutC1EP7QLegend', self._addressOf(legend),
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void LegendLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#invalidate
    """
    #  void LegendLayout::invalidate()
    ritual = 'ritual_ZN12LegendLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12LegendLayout10invalidateEv'
    self.uglySide.call(ritual)

  @overload(int)
  def removeAt(self, a0: int) -> None:
    """
    Calls Qt's 'void LegendLayout::removeAt(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/legendlayout.html#removeAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void LegendLayout::removeAt(int a0)
    ritual = 'ritual_ZN12LegendLayout8removeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12LegendLayout8removeAtEi'
    self.uglySide.call(ritual, a0)

  @staticmethod
  def widthLongerThan(*__, **_) -> Never:
    """
    Qt's 'bool LegendLayout::widthLongerThan(const LegendWidthStruct *item1,
    const LegendWidthStruct *item2)': names
    'LegendLayout::LegendWidthStruct', which has no cute class yet.
    """
    raise NotImplementedError(
        "'LegendLayout.widthLongerThan' has no cute function yet. Qt's "
        "'bool LegendLayout::widthLongerThan(const LegendWidthStruct "
        "*item1, const LegendWidthStruct *item2)': names "
        "'LegendLayout::LegendWidthStruct', which has no cute class yet.")
