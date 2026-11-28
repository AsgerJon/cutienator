"""
QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengine_accessible_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible to
#  be private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessible, QAccessibleInterface, QAccessibleObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderWidgetHostViewQtDelegateQuickAccessible(QAccessibleObject):
  """
  The cute side of Qt's
  QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible: a plain
  Python object standing in front of one C++
  QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible.

  It is built on the cute 'QAccessibleObject', as Qt's
  QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible is built on
  Qt's QAccessibleObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible that has a
  ritual and that Python can call so far, 9 names in all: 'isValid',
  'parent', 'text', 'role', 'state', 'focusChild', 'childCount', 'child',
  'indexOfChild'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible is
    created at the first use, not by
    'QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible.
  - Each name of Qt's
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible that has
    no cute function yet, '__init__', 'viewAccessible', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::isValid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html
    """
    #  bool QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      isValid() const
    return self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible7isValidEv',
    )

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::parent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface
    #      *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      parent() const
    address = self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible6parentEv',
    )
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::text(
    QAccessible::Text t) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      text(QAccessible::Text t) const
    ritual = (
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible4textEN11QAccessible4TextE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQ'
          'uickAccessible4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, t.value)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::role()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role
    #      QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      role() const
    ritual = (
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible4roleEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQ'
          'uickAccessible4roleEv')
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::state()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State
    #      QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      state() const
    address = self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible5stateEv',
    )
    return QAccessible.State._cuteOwning(address)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    focusChild() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface
    #      *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      focusChild() const
    address = self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible10focusChildEv',
    )
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html
    """
    #  int QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      childCount() const
    return self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible10childCountEv',
    )

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::child(
    int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html

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
    #  QAccessibleInterface
    #      *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible5childEi',
        index,
    )
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int
    QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    indexOfChild(const QAccessibleInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatequickaccessible.html

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    #      indexOfChild(const QAccessibleInterface *a0) const
    return self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAc'
        'cessible12indexOfChildEPK20QAccessibleInterface',
        self._addressOf(a0, 'QAccessibleInterface'),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    RenderWidgetHostViewQtDelegateQuickAccessible(QObject *o,
    QQuickWebEngineView *view)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: no matching
    constructor for initialization of 'QWeakPointer<QObjectType>' (aka
    'QWeakPointer<QObject>').
    """
    raise NotImplementedError(
        "'QtWebEngineCore.RenderWidgetHostViewQtDelegateQuickAccessible.__in"
        "it__' has no cute function yet. Qt's "
        "'QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::Re"
        "nderWidgetHostViewQtDelegateQuickAccessible(QObject *o, "
        "QQuickWebEngineView *view)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: no "
        "matching constructor for initialization of "
        "'QWeakPointer<QObjectType>' (aka 'QWeakPointer<QObject>').")

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
  def viewAccessible(*__, **_) -> Never:
    """
    Qt's 'QQuickWebEngineViewAccessible
    *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::
    viewAccessible() const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: no viable conversion
    from 'const QPointer<QQuickWebEngineView>' to 'QObject *'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.RenderWidgetHostViewQtDelegateQuickAccessible.view"
        "Accessible' has no cute function yet. Qt's "
        "'QQuickWebEngineViewAccessible "
        "*QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::vi"
        "ewAccessible() const': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: no "
        "viable conversion from 'const QPointer<QQuickWebEngineView>' to "
        "'QObject *'.")
