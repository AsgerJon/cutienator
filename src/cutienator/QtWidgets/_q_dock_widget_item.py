"""
QDockWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDockWidgetItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLayoutItem, QWidgetItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QDockWidget, QDockWidgetLayout
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDockWidget = WAIT['QDockWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockWidgetItem(QWidgetItem):
  """
  The cute side of Qt's QDockWidgetItem: a plain Python object standing in
  front of one C++ QDockWidgetItem.

  It is built on the cute 'QWidgetItem', as Qt's QDockWidgetItem is built on
  Qt's QWidgetItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDockWidgetItem that has a ritual and that Python
  can call so far, 5 names in all: 'minimumSize', 'maximumSize', 'sizeHint',
  'dockWidgetChildItem', 'dockWidgetLayout'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QDockWidgetItem is created at the first use, not by
    'QDockWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDockWidgetItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockWidgetItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetItem::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetitem.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetItem::minimumSize() const
    ritual = 'ritual_ZNK15QDockWidgetItem11minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDockWidgetItem11minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetItem::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetitem.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetItem::maximumSize() const
    ritual = 'ritual_ZNK15QDockWidgetItem11maximumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDockWidgetItem11maximumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetItem::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetitem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetItem::sizeHint() const
    ritual = 'ritual_ZNK15QDockWidgetItem8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDockWidgetItem8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def dockWidgetChildItem(self) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QDockWidgetItem::dockWidgetChildItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetitem.html#dockWidgetChildItem

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QDockWidgetItem::dockWidgetChildItem() const
    address = self.uglySide.call(
        'ritual_ZNK15QDockWidgetItem19dockWidgetChildItemEv',
    )
    return QLayoutItem._cuteAt(address)

  def dockWidgetLayout(self) -> Optional[QDockWidgetLayout]:
    """
    Calls Qt's 'QDockWidgetLayout *QDockWidgetItem::dockWidgetLayout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetitem.html#dockWidgetLayout

    Returns
    -------

    Optional[QDockWidgetLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockWidgetLayout *QDockWidgetItem::dockWidgetLayout() const
    address = self.uglySide.call(
        'ritual_ZNK15QDockWidgetItem16dockWidgetLayoutEv',
    )
    from . import QDockWidgetLayout
    return QDockWidgetLayout._cuteAt(address)

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

  @overload(QDockWidget)
  @overload(NoneType)
  def __init__(self, dockWidget: Optional[QDockWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetitem.html#QDockWidgetItem

    Parameters
    ----------

    dockWidget : Optional[QDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
    self._noteCreation(QDockWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QDockWidgetItemC1EP11QDockWidget',
        self._addressOf(dockWidget),
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
