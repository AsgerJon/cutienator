"""
QAccessibleStackedWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleStackedWidget to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QStackedWidget, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleStackedWidget(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleStackedWidget: a plain Python object
  standing in front of one C++ QAccessibleStackedWidget.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleStackedWidget is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleStackedWidget that has a ritual and that
  Python can call so far, 5 names in all: 'childAt', 'childCount',
  'indexOfChild', 'child', 'stackedWidget'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleStackedWidget is created at the first use, not by
    'QAccessibleStackedWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleStackedWidget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleStackedWidget'

  #  A C++ QAccessibleStackedWidget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleStackedWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleStackedWidget::childAt(int
    x, int y) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestackedwidget.html#childAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleStackedWidget::childAt(int x, int y)
    #      const
    ritual = 'ritual_ZNK24QAccessibleStackedWidget7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAccessibleStackedWidget7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleStackedWidget::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestackedwidget.html#childCount
    """
    #  int QAccessibleStackedWidget::childCount() const
    ritual = 'ritual_ZNK24QAccessibleStackedWidget10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAccessibleStackedWidget10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleStackedWidget::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestackedwidget.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleStackedWidget::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK24QAccessibleStackedWidget12indexOfChildEPK20QAccessible'
        'Interface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAccessibleStackedWidget12indexOfChildEPK20QAcce'
          'ssibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleStackedWidget::child(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestackedwidget.html#child

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleStackedWidget::child(int index) const
    ritual = 'ritual_ZNK24QAccessibleStackedWidget5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAccessibleStackedWidget5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def stackedWidget(self) -> Optional[QStackedWidget]:
    """
    Calls Qt's 'QStackedWidget *QAccessibleStackedWidget::stackedWidget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestackedwidget.html#stackedWidget

    Returns
    -------

    Optional[QStackedWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStackedWidget *QAccessibleStackedWidget::stackedWidget() const
    address = self.uglySide.call(
        'ritual_ZNK24QAccessibleStackedWidget13stackedWidgetEv',
    )
    from . import QStackedWidget
    return QStackedWidget._cuteAt(address)

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

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, widget: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleStackedWidget::QAccessibleStackedWidget(QWidget *widget)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblestackedwidget.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleStackedWidget::QAccessibleStackedWidget(QWidget *widget)
    self._noteCreation(QAccessibleStackedWidget, lambda: Rituals.call(
        'ritual_ZN24QAccessibleStackedWidgetC1EP7QWidget',
        self._addressOf(widget),
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
