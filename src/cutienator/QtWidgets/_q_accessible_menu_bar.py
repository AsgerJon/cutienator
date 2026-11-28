"""
QAccessibleMenuBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleMenuBar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMenuBar

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleMenuBar(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleMenuBar: a plain Python object standing in
  front of one C++ QAccessibleMenuBar.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleMenuBar
  is built on Qt's QAccessibleWidgetV2, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleMenuBar that has a ritual and that Python
  can call so far, 4 names in all: 'child', 'childCount', 'indexOfChild',
  'menuBar'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'QAccessibleMenuItem.

  What to expect
  --------------

  - The C++ QAccessibleMenuBar is created at the first use, not by
    'QAccessibleMenuBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleMenuBar.
  - Each name of Qt's QAccessibleMenuBar that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleMenuBar'

  #  A C++ QAccessibleMenuBar Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleMenuBar'

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
    Calls Qt's 'QAccessibleInterface *QAccessibleMenuBar::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenubar.html#child

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
    #  QAccessibleInterface *QAccessibleMenuBar::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QAccessibleMenuBar5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleMenuBar::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenubar.html#childCount
    """
    #  int QAccessibleMenuBar::childCount() const
    ritual = 'ritual_ZNK18QAccessibleMenuBar10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleMenuBar10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleMenuBar::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemenubar.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleMenuBar::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK18QAccessibleMenuBar12indexOfChildEPK20QAccessibleInterf'
        'ace')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAccessibleMenuBar12indexOfChildEPK20QAccessible'
          'Interface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def menuBar(self) -> Optional[QMenuBar]:
    """
    Calls Qt's 'QMenuBar *QAccessibleMenuBar::menuBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemenubar.html#menuBar

    Returns
    -------

    Optional[QMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenuBar *QAccessibleMenuBar::menuBar() const
    address = self.uglySide.call('ritual_ZNK18QAccessibleMenuBar7menuBarEv')
    from . import QMenuBar
    return QMenuBar._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAccessibleMenuBar::QAccessibleMenuBar(QWidget *w)': leans on
    'QAccessibleMenuItem::text(QAccessible::Text) const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QAccessibleMenuBar.__init__' has no cute function yet. Qt's "
        "'QAccessibleMenuBar::QAccessibleMenuBar(QWidget *w)': leans on "
        "'QAccessibleMenuItem::text(QAccessible::Text) const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
