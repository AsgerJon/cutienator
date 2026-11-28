"""
QAccessibleAbstractScrollArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleAbstractScrollArea to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractScrollArea, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleAbstractScrollArea(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleAbstractScrollArea: a plain Python object
  standing in front of one C++ QAccessibleAbstractScrollArea.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleAbstractScrollArea is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleAbstractScrollArea that has a ritual and
  that Python can call so far, 9 names in all: 'child', 'childCount',
  'indexOfChild', 'isValid', 'childAt', 'abstractScrollArea',
  'accessibleChildren', 'elementType', 'isLeftToRight'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleAbstractScrollArea is created at the first use, not by
    'QAccessibleAbstractScrollArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleAbstractScrollArea.
  """

  #  The enums Qt writes inside QAccessibleAbstractScrollArea, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class AbstractScrollAreaElement(CuteNum):
    """
    The enum 'QAccessibleAbstractScrollArea::AbstractScrollAreaElement' of
    Qt, with the 6 names Qt gives in it.
    """

    Self = Kee[int](0)
    Viewport = Kee[int](1)
    HorizontalContainer = Kee[int](2)
    VerticalContainer = Kee[int](3)
    CornerWidget = Kee[int](4)
    Undefined = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleAbstractScrollArea'

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
    Calls Qt's 'QAccessibleInterface
    *QAccessibleAbstractScrollArea::child(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html#child

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
    #  QAccessibleInterface *QAccessibleAbstractScrollArea::child(int index)
    #      const
    ritual = 'ritual_ZNK29QAccessibleAbstractScrollArea5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QAccessibleAbstractScrollArea5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleAbstractScrollArea::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html#childCount
    """
    #  int QAccessibleAbstractScrollArea::childCount() const
    ritual = 'ritual_ZNK29QAccessibleAbstractScrollArea10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QAccessibleAbstractScrollArea10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleAbstractScrollArea::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleAbstractScrollArea::indexOfChild(const
    #      QAccessibleInterface *child) const
    ritual = (
        'ritual_ZNK29QAccessibleAbstractScrollArea12indexOfChildEPK20QAcces'
        'sibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QAccessibleAbstractScrollArea12indexOfChildEPK20'
          'QAccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleAbstractScrollArea::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html#isValid
    """
    #  bool QAccessibleAbstractScrollArea::isValid() const
    ritual = 'ritual_ZNK29QAccessibleAbstractScrollArea7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QAccessibleAbstractScrollArea7isValidEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QAccessibleAbstractScrollArea::childAt(int x, int y) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html#childAt

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
    #  QAccessibleInterface *QAccessibleAbstractScrollArea::childAt(int x,
    #      int y) const
    ritual = 'ritual_ZNK29QAccessibleAbstractScrollArea7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QAccessibleAbstractScrollArea7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  def abstractScrollArea(self) -> Optional[QAbstractScrollArea]:
    """
    Calls Qt's 'QAbstractScrollArea
    *QAccessibleAbstractScrollArea::abstractScrollArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html

    Returns
    -------

    Optional[QAbstractScrollArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractScrollArea
    #      *QAccessibleAbstractScrollArea::abstractScrollArea() const
    address = self.uglySide.call(
        'ritual_ZNK29QAccessibleAbstractScrollArea18abstractScrollAreaEv',
    )
    from . import QAbstractScrollArea
    return QAbstractScrollArea._cuteAt(address)

  def accessibleChildren(self) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    QAccessibleAbstractScrollArea::accessibleChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList QAccessibleAbstractScrollArea::accessibleChildren() const
    address = self.uglySide.call(
        'ritual_ZNK29QAccessibleAbstractScrollArea18accessibleChildrenEv',
    )
    from . import QWidget
    return QList[QWidget]._cuteOwning(address)

  @overload(QWidget)
  @overload(NoneType)
  def elementType(
      self,
      widget: Optional[QWidget],
  ) -> AbstractScrollAreaElement:
    """
    Calls Qt's 'AbstractScrollAreaElement
    QAccessibleAbstractScrollArea::elementType(QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html#elementType

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    AbstractScrollAreaElement
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AbstractScrollAreaElement(number)' gives.
    """
    #  AbstractScrollAreaElement
    #      QAccessibleAbstractScrollArea::elementType(QWidget *widget) const
    return QAccessibleAbstractScrollArea.AbstractScrollAreaElement(
        self.uglySide.call(
            'ritual_ZNK29QAccessibleAbstractScrollArea11elementTypeEP7QWidg'
            'et',
            self._addressOf(widget),
        ))

  def isLeftToRight(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleAbstractScrollArea::isLeftToRight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html#isLeftToRight
    """
    #  bool QAccessibleAbstractScrollArea::isLeftToRight() const
    return self.uglySide.call(
        'ritual_ZNK29QAccessibleAbstractScrollArea13isLeftToRightEv',
    )

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
    'QAccessibleAbstractScrollArea::QAccessibleAbstractScrollArea(QWidget
    *widget)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractscrollarea.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleAbstractScrollArea::QAccessibleAbstractScrollArea(QWidget
    #      *widget)
    self._noteCreation(QAccessibleAbstractScrollArea, lambda: Rituals.call(
        'ritual_ZN29QAccessibleAbstractScrollAreaC1EP7QWidget',
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
