"""
qdesigner_internal::Grid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/grid_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means qdesigner_internal::Grid to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QVariant
  from ..QtGui import QPaintEvent
  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Grid(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::Grid: a plain Python object
  standing in front of one C++ qdesigner_internal::Grid.

  C++ hands a qdesigner_internal::Grid around as a copy, so every C++
  qdesigner_internal::Grid behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::Grid that has a ritual and that
  Python can call so far, 19 names in all: 'fromVariantMap', 'toVariantMap',
  'visible', 'setVisible', 'snapX', 'setSnapX', 'snapY', 'setSnapY',
  'deltaX', 'setDeltaX', 'deltaY', 'setDeltaY', 'paint', 'snapPoint',
  'widgetHandleAdjustX', 'widgetHandleAdjustY', '__eq__', '__ne__',
  'snapValue'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void qdesigner_internal::Grid::addToVariantMap(QVariantMap &vm,
    bool forceKeys) const': takes a type Python has no way to hand over yet.
  - Qt's 'void qdesigner_internal::Grid::paint(QPainter &p, const QWidget
    *widget, QPaintEvent *e) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'qdesigner_internal::Grid::~Grid()': the destructor: Python removes
    its C++ qdesigner_internal::Grid by it, and has no other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::Grid is created at the first use, not by
    'qdesigner_internal::Grid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::Grid back gives a copy the ritual
    made for Python, in a new cute qdesigner_internal::Grid.
  - Each name of Qt's qdesigner_internal::Grid that has no cute function yet,
    'addToVariantMap', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'qdesigner_internal::Grid'

  #  Qt's '~qdesigner_internal::Grid()'. Naming it makes this a value class:
  #  Python owns every C++ qdesigner_internal::Grid behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal4GridD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  def toVariantMap(self, forceKeys: bool = False) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap qdesigner_internal::Grid::toVariantMap(bool
    forceKeys) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#toVariantMap

    Parameters
    ----------

    forceKeys : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap qdesigner_internal::Grid::toVariantMap(bool forceKeys)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal4Grid12toVariantMapEb', forceKeys,
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def visible(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Grid::visible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#visible
    """
    #  bool qdesigner_internal::Grid::visible() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal4Grid7visibleEv',
    )

  def snapX(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Grid::snapX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesigner_internal-grid.html#snapX
    """
    #  bool qdesigner_internal::Grid::snapX() const
    return self.uglySide.call('ritual_ZNK18qdesigner_internal4Grid5snapXEv')

  def snapY(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Grid::snapY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesigner_internal-grid.html#snapY
    """
    #  bool qdesigner_internal::Grid::snapY() const
    return self.uglySide.call('ritual_ZNK18qdesigner_internal4Grid5snapYEv')

  def deltaX(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::Grid::deltaX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#deltaX
    """
    #  int qdesigner_internal::Grid::deltaX() const
    return self.uglySide.call('ritual_ZNK18qdesigner_internal4Grid6deltaXEv')

  def deltaY(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::Grid::deltaY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#deltaY
    """
    #  int qdesigner_internal::Grid::deltaY() const
    return self.uglySide.call('ritual_ZNK18qdesigner_internal4Grid6deltaYEv')

  @overload(QPoint)
  def snapPoint(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint qdesigner_internal::Grid::snapPoint(const QPoint &p)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#snapPoint

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint qdesigner_internal::Grid::snapPoint(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal4Grid9snapPointERK6QPoint',
        self._valueOf(p),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(int)
  def widgetHandleAdjustX(self, x: int) -> int:
    """
    Calls Qt's 'int qdesigner_internal::Grid::widgetHandleAdjustX(int x)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#widgetHandleAdjustX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  int qdesigner_internal::Grid::widgetHandleAdjustX(int x) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal4Grid19widgetHandleAdjustXEi', x,
    )

  @overload(int)
  def widgetHandleAdjustY(self, y: int) -> int:
    """
    Calls Qt's 'int qdesigner_internal::Grid::widgetHandleAdjustY(int y)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#widgetHandleAdjustY

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  int qdesigner_internal::Grid::widgetHandleAdjustY(int y) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal4Grid19widgetHandleAdjustYEi', y,
    )

  @overload(int, int)
  def snapValue(self, value: int, grid: int) -> int:
    """
    Calls Qt's 'int qdesigner_internal::Grid::snapValue(int value, int grid)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#snapValue

    Parameters
    ----------

    value : int
      Passed on as it is.

    grid : int
      Passed on as it is.
    """
    #  int qdesigner_internal::Grid::snapValue(int value, int grid) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal4Grid9snapValueEii', value, grid,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Grid::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::Grid::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal4Grid10setVisibleEb', visible,
    )

  @overload(bool)
  def setSnapX(self, snap: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Grid::setSnapX(bool snap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#setSnapX

    Parameters
    ----------

    snap : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::Grid::setSnapX(bool snap)
    self.uglySide.call('ritual_ZN18qdesigner_internal4Grid8setSnapXEb', snap)

  @overload(bool)
  def setSnapY(self, snap: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Grid::setSnapY(bool snap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#setSnapY

    Parameters
    ----------

    snap : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::Grid::setSnapY(bool snap)
    self.uglySide.call('ritual_ZN18qdesigner_internal4Grid8setSnapYEb', snap)

  @overload(int)
  def setDeltaX(self, dx: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Grid::setDeltaX(int dx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#setDeltaX

    Parameters
    ----------

    dx : int
      Passed on as it is.
    """
    #  void qdesigner_internal::Grid::setDeltaX(int dx)
    self.uglySide.call('ritual_ZN18qdesigner_internal4Grid9setDeltaXEi', dx)

  @overload(int)
  def setDeltaY(self, dy: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Grid::setDeltaY(int dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#setDeltaY

    Parameters
    ----------

    dy : int
      Passed on as it is.
    """
    #  void qdesigner_internal::Grid::setDeltaY(int dy)
    self.uglySide.call('ritual_ZN18qdesigner_internal4Grid9setDeltaYEi', dy)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: Grid) -> bool:
    """
    Calls Qt's 'bool operator==(const Grid &lhs, const Grid &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#operator==

    Parameters
    ----------

    rhs : Grid
      Passed on as a value: Qt reads the C++ qdesigner_internal::Grid, which
      stays Python's own.
    """
    #  bool operator==(const Grid &lhs, const Grid &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_4GridES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: Grid) -> bool:
    """
    Calls Qt's 'bool operator!=(const Grid &lhs, const Grid &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#operator!=

    Parameters
    ----------

    rhs : Grid
      Passed on as a value: Qt reads the C++ qdesigner_internal::Grid, which
      stays Python's own.
    """
    #  bool operator!=(const Grid &lhs, const Grid &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_4GridES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'qdesigner_internal::Grid::Grid()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdesigner_internal-grid.html#Grid
    """
    #  qdesigner_internal::Grid::Grid()
    self._noteCreation(Grid, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal4GridC1Ev',
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

  @overload(QMap[str, QVariant])
  def fromVariantMap(self, vm: QMap[str, QVariant]) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Grid::fromVariantMap(const
    QVariantMap &vm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-grid.html#fromVariantMap

    Parameters
    ----------

    vm : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool qdesigner_internal::Grid::fromVariantMap(const QVariantMap &vm)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal4Grid14fromVariantMapERK4QMapI7QStrin'
        'g8QVariantE',
        self._valueOf(vm),
    )

  @overload(QWidget, QPaintEvent)
  @overload(QWidget, NoneType)
  @overload(NoneType, QPaintEvent)
  @overload(NoneType, NoneType)
  def paint(
      self,
      widget: Optional[QWidget],
      e: Optional[QPaintEvent],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Grid::paint(QWidget *widget,
    QPaintEvent *e) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesigner_internal-grid.html#paint

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::Grid::paint(QWidget *widget, QPaintEvent *e)
    #      const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal4Grid5paintEP7QWidgetP11QPaintEvent',
        self._addressOf(widget), self._addressOf(e),
    )

  @staticmethod
  def addToVariantMap(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::Grid::addToVariantMap(QVariantMap &vm,
    bool forceKeys) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.Grid.addToVariantMap' has no cute function "
        "yet. Qt's 'void "
        "qdesigner_internal::Grid::addToVariantMap(QVariantMap &vm, bool "
        "forceKeys) const': takes a type Python has no way to hand over yet."
    )
