"""
QAccessibleWindowContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleWindowContainer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWidget, QWindowContainer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleWindowContainer(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleWindowContainer: a plain Python object
  standing in front of one C++ QAccessibleWindowContainer.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleWindowContainer is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleWindowContainer that has a ritual and
  that Python can call so far, 5 names in all: 'text', 'childCount',
  'indexOfChild', 'child', 'container'. It can be made from Python, in 1 way;
  see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleWindowContainer is created at the first use, not by
    'QAccessibleWindowContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleWindowContainer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleWindowContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text)
  def text(self, a0: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleWindowContainer::text(QAccessible::Text
    a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewindowcontainer.html#text

    Parameters
    ----------

    a0 : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleWindowContainer::text(QAccessible::Text a0) const
    ritual = (
        'ritual_ZNK26QAccessibleWindowContainer4textEN11QAccessible4TextE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleWindowContainer4textEN11QAccessible4T'
          'extE')
    return self.uglySide.call(ritual, a0.value)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleWindowContainer::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewindowcontainer.html#childCount
    """
    #  int QAccessibleWindowContainer::childCount() const
    ritual = 'ritual_ZNK26QAccessibleWindowContainer10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleWindowContainer10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleWindowContainer::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewindowcontainer.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleWindowContainer::indexOfChild(const
    #      QAccessibleInterface *child) const
    ritual = (
        'ritual_ZNK26QAccessibleWindowContainer12indexOfChildEPK20QAccessib'
        'leInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleWindowContainer12indexOfChildEPK20QAc'
          'cessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  @overload(int)
  def child(self, i: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleWindowContainer::child(int
    i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewindowcontainer.html#child

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleWindowContainer::child(int i) const
    ritual = 'ritual_ZNK26QAccessibleWindowContainer5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleWindowContainer5childEi'
    address = self.uglySide.call(ritual, i)
    return QAccessibleInterface._cuteAt(address)

  def container(self) -> Optional[QWindowContainer]:
    """
    Calls Qt's 'QWindowContainer *QAccessibleWindowContainer::container()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewindowcontainer.html#container

    Returns
    -------

    Optional[QWindowContainer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowContainer *QAccessibleWindowContainer::container() const
    address = self.uglySide.call(
        'ritual_ZNK26QAccessibleWindowContainer9containerEv',
    )
    from . import QWindowContainer
    return QWindowContainer._cuteAt(address)

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
  def __init__(self, w: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleWindowContainer::QAccessibleWindowContainer(QWidget *w)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewindowcontainer.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleWindowContainer::QAccessibleWindowContainer(QWidget *w)
    self._noteCreation(QAccessibleWindowContainer, lambda: Rituals.call(
        'ritual_ZN26QAccessibleWindowContainerC1EP7QWidget',
        self._addressOf(w),
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
