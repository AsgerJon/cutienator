"""
QAccessibleQuickListView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qaccessiblequicklistview_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleQuickListView to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleViewportInterface
from . import QAccessibleQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QSizeF
  from . import QQuickListView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickListView = WAIT['QQuickListView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickListView(QAccessibleQuickItem, QAccessibleViewportInterface):
  """
  The cute side of Qt's QAccessibleQuickListView: a plain Python object
  standing in front of one C++ QAccessibleQuickListView.

  It is built on the cute 'QAccessibleQuickItem', as Qt's
  QAccessibleQuickListView is built on Qt's QAccessibleQuickItem, and has
  everything that class has. It is built on the cute
  'QAccessibleViewportInterface' as well, as Qt's QAccessibleQuickListView is
  built on Qt's QAccessibleViewportInterface too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickListView that has a ritual and that
  Python can call so far, 6 names in all: 'contentSize', 'position',
  'viewportSize', 'isIndexed', 'setPosition', 'listView'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleQuickListView::interface_cast(QAccessible::InterfaceType t)':
    gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickListView is created at the first use, not by
    'QAccessibleQuickListView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickListView.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickListView'

  #  Qt's QAccessibleQuickListView is built on more than one class. The part
  #  of a C++ QAccessibleQuickListView that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleViewportInterface':
          'ritual_cast_QAccessibleQuickListView_QAccessibleViewportInterface',
  }

  #  A C++ QAccessibleQuickListView Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleQuickListView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleQuickListView::contentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicklistview.html#contentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleQuickListView::contentSize() const
    ritual = 'ritual_ZNK24QAccessibleQuickListView11contentSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAccessibleQuickListView11contentSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QAccessibleQuickListView::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicklistview.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QAccessibleQuickListView::position() const
    ritual = 'ritual_ZNK24QAccessibleQuickListView8positionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAccessibleQuickListView8positionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def viewportSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleQuickListView::viewportSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicklistview.html#viewportSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleQuickListView::viewportSize() const
    ritual = 'ritual_ZNK24QAccessibleQuickListView12viewportSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAccessibleQuickListView12viewportSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isIndexed(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleQuickListView::isIndexed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicklistview.html#isIndexed
    """
    #  bool QAccessibleQuickListView::isIndexed() const
    ritual = 'ritual_ZNK24QAccessibleQuickListView9isIndexedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAccessibleQuickListView9isIndexedEv'
    return self.uglySide.call(ritual)

  def listView(self) -> Optional[QQuickListView]:
    """
    Calls Qt's 'QQuickListView *QAccessibleQuickListView::listView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicklistview.html#listView

    Returns
    -------

    Optional[QQuickListView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickListView *QAccessibleQuickListView::listView() const
    address = self.uglySide.call(
        'ritual_ZNK24QAccessibleQuickListView8listViewEv',
    )
    from . import QQuickListView
    return QQuickListView._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPosition(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QAccessibleQuickListView::setPosition(QPointF
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicklistview.html#setPosition

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAccessibleQuickListView::setPosition(QPointF position)
    ritual = 'ritual_ZN24QAccessibleQuickListView11setPositionE7QPointF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAccessibleQuickListView11setPositionE7QPointF')
    self.uglySide.call(ritual, self._valueOf(position, 'QPointF'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickListView)
  @overload(NoneType)
  def __init__(self, listView: Optional[QQuickListView]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickListView::QAccessibleQuickListView(QQuickListView
    *listView)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequicklistview.html

    Parameters
    ----------

    listView : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickListView::QAccessibleQuickListView(QQuickListView
    #      *listView)
    self._noteCreation(QAccessibleQuickListView, lambda: Rituals.call(
        'ritual_ZN24QAccessibleQuickListViewC1EP14QQuickListView',
        self._addressOf(listView),
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
