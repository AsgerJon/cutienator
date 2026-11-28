"""
QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/qwebengine_accessible_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible
#  to be private: it declares the class in a header it calls private.
#  cutienator does not care. Qt hands objects of the class out all the same,
#  and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessibleInterface
from ..QtWidgets import QAccessibleWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
  from . import QWebEngineView, QWebEngineViewAccessible
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineView = WAIT['QWebEngineView']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderWidgetHostViewQtDelegateWidgetAccessible(QAccessibleWidget):
  """
  The cute side of Qt's
  QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible: a plain
  Python object standing in front of one C++
  QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible.

  It is built on the cute 'QAccessibleWidget', as Qt's
  QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible is built on
  Qt's QAccessibleWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible that has a
  ritual and that Python can call so far, 6 names in all: 'isValid',
  'focusChild', 'childCount', 'child', 'indexOfChild', 'viewAccessible'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible
    is created at the first use, not by
    'QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible'

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
    QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::isValid(
    ) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatewidgetaccessible.html
    """
    #  bool QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    #      isValid() const
    ritual = (
        'ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetA'
        'ccessible7isValidEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateW'
          'idgetAccessible7isValidEv')
    return self.uglySide.call(ritual)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    focusChild() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatewidgetaccessible.html

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QtWebEngineCore::
    #      RenderWidgetHostViewQtDelegateWidgetAccessible::focusChild() const
    ritual = (
        'ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetA'
        'ccessible10focusChildEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateW'
          'idgetAccessible10focusChildEv')
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int
    QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatewidgetaccessible.html
    """
    #  int QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    #      childCount() const
    ritual = (
        'ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetA'
        'ccessible10childCountEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateW'
          'idgetAccessible10childCountEv')
    return self.uglySide.call(ritual)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::child(
    int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatewidgetaccessible.html

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
    #  QAccessibleInterface *QtWebEngineCore::
    #      RenderWidgetHostViewQtDelegateWidgetAccessible::child(int index)
    #      const
    ritual = (
        'ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetA'
        'ccessible5childEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateW'
          'idgetAccessible5childEi')
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int
    QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    indexOfChild(const QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatewidgetaccessible.html

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    #      indexOfChild(const QAccessibleInterface *child) const
    ritual = (
        'ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetA'
        'ccessible12indexOfChildEPK20QAccessibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateW'
          'idgetAccessible12indexOfChildEPK20QAccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def viewAccessible(self) -> Optional[QWebEngineViewAccessible]:
    """
    Calls Qt's 'QWebEngineViewAccessible
    *QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    viewAccessible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatewidgetaccessible.html

    Returns
    -------

    Optional[QWebEngineViewAccessible]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineViewAccessible *QtWebEngineCore::
    #      RenderWidgetHostViewQtDelegateWidgetAccessible::viewAccessible()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetA'
        'ccessible14viewAccessibleEv',
    )
    from . import QWebEngineViewAccessible
    return QWebEngineViewAccessible._cuteAt(address)

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

  @overload(QWidget, QWebEngineView)
  @overload(QWidget, NoneType)
  @overload(NoneType, QWebEngineView)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      o: Optional[QWidget],
      view: Optional[QWebEngineView],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    RenderWidgetHostViewQtDelegateWidgetAccessible(QWidget *o, QWebEngineView
    *view)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-renderwidgethostviewqtdelegatewidgetaccessible.html

    Parameters
    ----------

    o : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    view : Optional[QWebEngineView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::
    #      RenderWidgetHostViewQtDelegateWidgetAccessible(QWidget *o,
    #      QWebEngineView *view)
    self._noteCreation(
        RenderWidgetHostViewQtDelegateWidgetAccessible, lambda: Rituals.call(
            'ritual_ZN15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidg'
            'etAccessibleC1EP7QWidgetP14QWebEngineView',
            self._addressOf(o), self._addressOf(view),
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
