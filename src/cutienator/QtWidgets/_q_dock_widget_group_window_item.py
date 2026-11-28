"""
QDockWidgetGroupWindowItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDockWidgetGroupWindowItem to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QWidgetItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QDockWidgetGroupWindow, QLayout, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDockWidgetGroupWindow = WAIT['QDockWidgetGroupWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockWidgetGroupWindowItem(QWidgetItem):
  """
  The cute side of Qt's QDockWidgetGroupWindowItem: a plain Python object
  standing in front of one C++ QDockWidgetGroupWindowItem.

  It is built on the cute 'QWidgetItem', as Qt's QDockWidgetGroupWindowItem
  is built on Qt's QWidgetItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDockWidgetGroupWindowItem that has a ritual and
  that Python can call so far, 5 names in all: 'minimumSize', 'maximumSize',
  'sizeHint', 'widget', 'lay'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QDockWidgetGroupWindowItem is created at the first use, not by
    'QDockWidgetGroupWindowItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDockWidgetGroupWindowItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockWidgetGroupWindowItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetGroupWindowItem::minimumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindowitem.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetGroupWindowItem::minimumSize() const
    ritual = 'ritual_ZNK26QDockWidgetGroupWindowItem11minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QDockWidgetGroupWindowItem11minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetGroupWindowItem::maximumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindowitem.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetGroupWindowItem::maximumSize() const
    ritual = 'ritual_ZNK26QDockWidgetGroupWindowItem11maximumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QDockWidgetGroupWindowItem11maximumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetGroupWindowItem::sizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindowitem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetGroupWindowItem::sizeHint() const
    ritual = 'ritual_ZNK26QDockWidgetGroupWindowItem8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QDockWidgetGroupWindowItem8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDockWidgetGroupWindowItem::widget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindowitem.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDockWidgetGroupWindowItem::widget() const
    ritual = 'ritual_ZNK26QDockWidgetGroupWindowItem6widgetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QDockWidgetGroupWindowItem6widgetEv'
    address = self.uglySide.call(ritual)
    from . import QWidget
    return QWidget._cuteAt(address)

  def lay(self) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QDockWidgetGroupWindowItem::lay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindowitem.html#lay

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QDockWidgetGroupWindowItem::lay() const
    address = self.uglySide.call(
        'ritual_ZNK26QDockWidgetGroupWindowItem3layEv',
    )
    from . import QLayout
    return QLayout._cuteAt(address)

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

  @overload(QDockWidgetGroupWindow)
  @overload(NoneType)
  def __init__(self, parent: Optional[QDockWidgetGroupWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QDockWidgetGroupWindowItem::QDockWidgetGroupWindowItem(
    QDockWidgetGroupWindow *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindowitem.html

    Parameters
    ----------

    parent : Optional[QDockWidgetGroupWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDockWidgetGroupWindowItem::QDockWidgetGroupWindowItem(
    #      QDockWidgetGroupWindow *parent)
    self._noteCreation(QDockWidgetGroupWindowItem, lambda: Rituals.call(
        'ritual_ZN26QDockWidgetGroupWindowItemC1EP22QDockWidgetGroupWindow',
        self._addressOf(parent),
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
