"""
QAccessibleMdiArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleMdiArea to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMdiArea, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleMdiArea(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleMdiArea: a plain Python object standing in
  front of one C++ QAccessibleMdiArea.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleMdiArea
  is built on Qt's QAccessibleWidgetV2, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleMdiArea that has a ritual and that Python
  can call so far, 4 names in all: 'childCount', 'child', 'indexOfChild',
  'mdiArea'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleMdiArea is created at the first use, not by
    'QAccessibleMdiArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleMdiArea.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleMdiArea'

  #  A C++ QAccessibleMdiArea Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleMdiArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleMdiArea::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemdiarea.html#childCount
    """
    #  int QAccessibleMdiArea::childCount() const
    ritual = 'ritual_ZNK18QAccessibleMdiArea10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleMdiArea10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMdiArea::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemdiarea.html#child

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
    #  QAccessibleInterface *QAccessibleMdiArea::child(int index) const
    ritual = 'ritual_ZNK18QAccessibleMdiArea5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleMdiArea5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleMdiArea::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemdiarea.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleMdiArea::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK18QAccessibleMdiArea12indexOfChildEPK20QAccessibleInterf'
        'ace')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAccessibleMdiArea12indexOfChildEPK20QAccessible'
          'Interface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def mdiArea(self) -> Optional[QMdiArea]:
    """
    Calls Qt's 'QMdiArea *QAccessibleMdiArea::mdiArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemdiarea.html#mdiArea

    Returns
    -------

    Optional[QMdiArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiArea *QAccessibleMdiArea::mdiArea() const
    address = self.uglySide.call('ritual_ZNK18QAccessibleMdiArea7mdiAreaEv')
    from . import QMdiArea
    return QMdiArea._cuteAt(address)

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
    'QAccessibleMdiArea::QAccessibleMdiArea(QWidget *widget)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemdiarea.html#QAccessibleMdiArea

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleMdiArea::QAccessibleMdiArea(QWidget *widget)
    self._noteCreation(QAccessibleMdiArea, lambda: Rituals.call(
        'ritual_ZN18QAccessibleMdiAreaC1EP7QWidget', self._addressOf(widget),
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
