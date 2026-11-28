"""
QWebEngineViewAccessible binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/qwebengine_accessible_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineViewAccessible to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessibleInterface
from ..QtWidgets import QAccessibleWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWebEngineView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineView = WAIT['QWebEngineView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineViewAccessible(QAccessibleWidget):
  """
  The cute side of Qt's QWebEngineViewAccessible: a plain Python object
  standing in front of one C++ QWebEngineViewAccessible.

  It is built on the cute 'QAccessibleWidget', as Qt's
  QWebEngineViewAccessible is built on Qt's QAccessibleWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineViewAccessible that has a ritual and that
  Python can call so far, 6 names in all: 'isValid', 'focusChild',
  'childCount', 'child', 'indexOfChild', 'view'. It can be made from Python,
  in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QWebEngineViewAccessible is created at the first use, not by
    'QWebEngineViewAccessible(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineViewAccessible.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineViewAccessible'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineViewAccessible::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineviewaccessible.html#isValid
    """
    #  bool QWebEngineViewAccessible::isValid() const
    return self.uglySide.call(
        'ritual_ZNK24QWebEngineViewAccessible7isValidEv',
    )

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QWebEngineViewAccessible::focusChild()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineviewaccessible.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QWebEngineViewAccessible::focusChild() const
    ritual = 'ritual_ZNK24QWebEngineViewAccessible10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QWebEngineViewAccessible10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QWebEngineViewAccessible::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineviewaccessible.html#childCount
    """
    #  int QWebEngineViewAccessible::childCount() const
    ritual = 'ritual_ZNK24QWebEngineViewAccessible10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QWebEngineViewAccessible10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QWebEngineViewAccessible::child(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineviewaccessible.html#child

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
    #  QAccessibleInterface *QWebEngineViewAccessible::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineViewAccessible5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QWebEngineViewAccessible::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineviewaccessible.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QWebEngineViewAccessible::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK24QWebEngineViewAccessible12indexOfChildEPK20QAccessible'
        'Interface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QWebEngineViewAccessible12indexOfChildEPK20QAcce'
          'ssibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def view(self) -> Optional[QWebEngineView]:
    """
    Calls Qt's 'QWebEngineView *QWebEngineViewAccessible::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineviewaccessible.html#view

    Returns
    -------

    Optional[QWebEngineView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineView *QWebEngineViewAccessible::view() const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineViewAccessible4viewEv',
    )
    from . import QWebEngineView
    return QWebEngineView._cuteAt(address)

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

  @overload(QWebEngineView)
  @overload(NoneType)
  def __init__(self, o: Optional[QWebEngineView]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineViewAccessible::QWebEngineViewAccessible(QWebEngineView *o)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineviewaccessible.html

    Parameters
    ----------

    o : Optional[QWebEngineView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineViewAccessible::QWebEngineViewAccessible(QWebEngineView *o)
    self._noteCreation(QWebEngineViewAccessible, lambda: Rituals.call(
        'ritual_ZN24QWebEngineViewAccessibleC1EP14QWebEngineView',
        self._addressOf(o),
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
