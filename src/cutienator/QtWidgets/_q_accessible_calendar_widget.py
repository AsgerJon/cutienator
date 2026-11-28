"""
QAccessibleCalendarWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleCalendarWidget to be private: it declares the class in
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

  from . import QAbstractItemView, QCalendarWidget, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleCalendarWidget(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleCalendarWidget: a plain Python object
  standing in front of one C++ QAccessibleCalendarWidget.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleCalendarWidget is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleCalendarWidget that has a ritual and that
  Python can call so far, 6 names in all: 'childCount', 'indexOfChild',
  'child', 'calendarWidget', 'calendarView', 'navigationBar'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleCalendarWidget is created at the first use, not by
    'QAccessibleCalendarWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleCalendarWidget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleCalendarWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleCalendarWidget::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecalendarwidget.html#childCount
    """
    #  int QAccessibleCalendarWidget::childCount() const
    ritual = 'ritual_ZNK25QAccessibleCalendarWidget10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleCalendarWidget10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleCalendarWidget::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecalendarwidget.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleCalendarWidget::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK25QAccessibleCalendarWidget12indexOfChildEPK20QAccessibl'
        'eInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAccessibleCalendarWidget12indexOfChildEPK20QAcc'
          'essibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleCalendarWidget::child(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecalendarwidget.html#child

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
    #  QAccessibleInterface *QAccessibleCalendarWidget::child(int index)
    #      const
    ritual = 'ritual_ZNK25QAccessibleCalendarWidget5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleCalendarWidget5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def calendarWidget(self) -> Optional[QCalendarWidget]:
    """
    Calls Qt's 'QCalendarWidget *QAccessibleCalendarWidget::calendarWidget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecalendarwidget.html#calendarWidget

    Returns
    -------

    Optional[QCalendarWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCalendarWidget *QAccessibleCalendarWidget::calendarWidget() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleCalendarWidget14calendarWidgetEv',
    )
    from . import QCalendarWidget
    return QCalendarWidget._cuteAt(address)

  def calendarView(self) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QAccessibleCalendarWidget::calendarView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecalendarwidget.html#calendarView

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QAccessibleCalendarWidget::calendarView() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleCalendarWidget12calendarViewEv',
    )
    from . import QAbstractItemView
    return QAbstractItemView._cuteAt(address)

  def navigationBar(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAccessibleCalendarWidget::navigationBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecalendarwidget.html#navigationBar

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAccessibleCalendarWidget::navigationBar() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleCalendarWidget13navigationBarEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

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
    'QAccessibleCalendarWidget::QAccessibleCalendarWidget(QWidget *widget)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecalendarwidget.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleCalendarWidget::QAccessibleCalendarWidget(QWidget *widget)
    self._noteCreation(QAccessibleCalendarWidget, lambda: Rituals.call(
        'ritual_ZN25QAccessibleCalendarWidgetC1EP7QWidget',
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
