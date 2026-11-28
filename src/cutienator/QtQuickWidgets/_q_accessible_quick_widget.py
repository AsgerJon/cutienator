"""
QAccessibleQuickWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickWidgets/6.12.0/QtQuickWidgets/private/qaccessiblequickwidget_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAccessibleQuickWidget to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessibleInterface
from ..QtWidgets import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWidget = WAIT['QQuickWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickWidget(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleQuickWidget: a plain Python object
  standing in front of one C++ QAccessibleQuickWidget.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleQuickWidget is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickWidget that has a ritual and that
  Python can call so far, 5 names in all: 'child', 'childCount',
  'indexOfChild', 'childAt', 'repairWindow'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleQuickWidget::~QAccessibleQuickWidget()': the destructor:
    Python never removes a C++ QAccessibleQuickWidget.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QAccessibleQuickWidget is created at the first use, not by
    'QAccessibleQuickWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickWidget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickWidget'

  #  A C++ QAccessibleQuickWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleQuickWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickWidget::child(int
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickwidget.html#child

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
    #  QAccessibleInterface *QAccessibleQuickWidget::child(int index) const
    ritual = 'ritual_ZNK22QAccessibleQuickWidget5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWidget5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleQuickWidget::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidget.html#childCount
    """
    #  int QAccessibleQuickWidget::childCount() const
    ritual = 'ritual_ZNK22QAccessibleQuickWidget10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWidget10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleQuickWidget::indexOfChild(const
    QAccessibleInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidget.html#indexOfChild

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleQuickWidget::indexOfChild(const QAccessibleInterface
    #      *iface) const
    ritual = (
        'ritual_ZNK22QAccessibleQuickWidget12indexOfChildEPK20QAccessibleIn'
        'terface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QAccessibleQuickWidget12indexOfChildEPK20QAccess'
          'ibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(iface, 'QAccessibleInterface'),
    )

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickWidget::childAt(int x,
    int y) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidget.html#childAt

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
    #  QAccessibleInterface *QAccessibleQuickWidget::childAt(int x, int y)
    #      const
    ritual = 'ritual_ZNK22QAccessibleQuickWidget7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleQuickWidget7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

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

  @overload(QQuickWidget)
  @overload(NoneType)
  def __init__(self, widget: Optional[QQuickWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickWidget::QAccessibleQuickWidget(QQuickWidget *widget)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidget.html#QAccessibleQuickWidget

    Parameters
    ----------

    widget : Optional[QQuickWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickWidget::QAccessibleQuickWidget(QQuickWidget *widget)
    self._noteCreation(QAccessibleQuickWidget, lambda: Rituals.call(
        'ritual_ZN22QAccessibleQuickWidgetC1EP12QQuickWidget',
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

  def repairWindow(self) -> None:
    """
    Calls Qt's 'void QAccessibleQuickWidget::repairWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickwidget.html#repairWindow
    """
    #  void QAccessibleQuickWidget::repairWindow()
    self.uglySide.call('ritual_ZN22QAccessibleQuickWidget12repairWindowEv')
