"""
QQuickWebEngineViewAccessible binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengine_accessible_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineViewAccessible to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessible, QAccessibleInterface, QAccessibleObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineViewAccessible(QAccessibleObject):
  """
  The cute side of Qt's QQuickWebEngineViewAccessible: a plain Python object
  standing in front of one C++ QQuickWebEngineViewAccessible.

  It is built on the cute 'QAccessibleObject', as Qt's
  QQuickWebEngineViewAccessible is built on Qt's QAccessibleObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineViewAccessible that has a ritual and
  that Python can call so far, 9 names in all: 'isValid', 'parent',
  'focusChild', 'childCount', 'child', 'indexOfChild', 'text', 'role',
  'state'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickWebEngineViewAccessible is created at the first use, not by
    'QQuickWebEngineViewAccessible(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineViewAccessible.
  - Each name of Qt's QQuickWebEngineViewAccessible that has no cute function
    yet, '__init__', 'engineView', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineViewAccessible'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineViewAccessible::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#isValid
    """
    #  bool QQuickWebEngineViewAccessible::isValid() const
    ritual = 'ritual_ZNK29QQuickWebEngineViewAccessible7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickWebEngineViewAccessible7isValidEv'
    return self.uglySide.call(ritual)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QQuickWebEngineViewAccessible::parent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QQuickWebEngineViewAccessible::parent() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineViewAccessible6parentEv',
    )
    return QAccessibleInterface._cuteAt(address)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QQuickWebEngineViewAccessible::focusChild() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QQuickWebEngineViewAccessible::focusChild()
    #      const
    ritual = 'ritual_ZNK29QQuickWebEngineViewAccessible10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickWebEngineViewAccessible10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QQuickWebEngineViewAccessible::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#childCount
    """
    #  int QQuickWebEngineViewAccessible::childCount() const
    ritual = 'ritual_ZNK29QQuickWebEngineViewAccessible10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickWebEngineViewAccessible10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QQuickWebEngineViewAccessible::child(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#child

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
    #  QAccessibleInterface *QQuickWebEngineViewAccessible::child(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineViewAccessible5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QQuickWebEngineViewAccessible::indexOfChild(const
    QAccessibleInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickWebEngineViewAccessible::indexOfChild(const
    #      QAccessibleInterface *a0) const
    ritual = (
        'ritual_ZNK29QQuickWebEngineViewAccessible12indexOfChildEPK20QAcces'
        'sibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QQuickWebEngineViewAccessible12indexOfChildEPK20'
          'QAccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QAccessibleInterface'),
    )

  @overload(QAccessible.Text)
  def text(self, a0: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineViewAccessible::text(QAccessible::Text
    a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#text

    Parameters
    ----------

    a0 : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineViewAccessible::text(QAccessible::Text a0)
    #      const
    ritual = (
        'ritual_ZNK29QQuickWebEngineViewAccessible4textEN11QAccessible4Text'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QQuickWebEngineViewAccessible4textEN11QAccessibl'
          'e4TextE')
    return self.uglySide.call(ritual, a0.value)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickWebEngineViewAccessible::role()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickWebEngineViewAccessible::role() const
    ritual = 'ritual_ZNK29QQuickWebEngineViewAccessible4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickWebEngineViewAccessible4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QQuickWebEngineViewAccessible::state()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineviewaccessible.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QQuickWebEngineViewAccessible::state() const
    ritual = 'ritual_ZNK29QQuickWebEngineViewAccessible5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickWebEngineViewAccessible5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

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
    Qt's 'QQuickWebEngineViewAccessible::QQuickWebEngineViewAccessible(
    QQuickWebEngineView *o)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: no matching
    constructor for initialization of 'QAccessibleObject'.
    """
    raise NotImplementedError(
        "'QQuickWebEngineViewAccessible.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickWebEngineViewAccessible::QQuickWebEngineViewAccessible(QQuic"
        "kWebEngineView *o)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: no matching "
        "constructor for initialization of 'QAccessibleObject'.")

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

  @staticmethod
  def engineView(*__, **_) -> Never:
    """
    Qt's 'QQuickWebEngineView *QQuickWebEngineViewAccessible::engineView()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: static_cast from 'QObject *' to
    'QQuickWebEngineView *', which are not related by inheritance, is not
    allowed.
    """
    raise NotImplementedError(
        "'QQuickWebEngineViewAccessible.engineView' has no cute function "
        "yet. Qt's 'QQuickWebEngineView "
        "*QQuickWebEngineViewAccessible::engineView() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: static_cast from 'QObject *' to "
        "'QQuickWebEngineView *', which are not related by inheritance, is "
        "not allowed.")
