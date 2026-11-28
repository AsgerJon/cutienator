"""
QQuickToolBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktoolbar_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickToolBar to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickPane

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickToolBar(QQuickPane):
  """
  The cute side of Qt's QQuickToolBar: a plain Python object standing in
  front of one C++ QQuickToolBar.

  It is built on the cute 'QQuickPane', as Qt's QQuickToolBar is built on
  Qt's QQuickPane, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickToolBar that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'position', 'setPosition',
  'positionChanged', 'defaultFont', 'accessibleRole'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickToolBar::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickToolBar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickToolBarPrivate *QQuickToolBar::d_func()': gives
    'QQuickToolBarPrivate', which has no cute class yet.
  - Qt's 'const QQuickToolBarPrivate *QQuickToolBar::d_func() const': gives
    'QQuickToolBarPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickToolBar is created at the first use, not by
    'QQuickToolBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickToolBar.
  - Qt tells when it has removed the C++ QQuickToolBar. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickToolBar, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Position(CuteNum):
    """
    The enum 'QQuickToolBar::Position' of Qt, with the 2 names Qt gives in
    it.
    """

    Header = Kee[int](0)
    Footer = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickToolBar::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickToolBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickToolBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickToolBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickToolBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickToolBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickToolBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> Position:
    """
    Calls Qt's 'Position QQuickToolBar::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#position

    Returns
    -------

    Position
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Position(number)' gives.
    """
    #  Position QQuickToolBar::position() const
    return QQuickToolBar.Position(self.uglySide.call(
        'ritual_ZNK13QQuickToolBar8positionEv',
    ))

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickToolBar::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickToolBar::defaultFont() const
    ritual = 'ritual_ZNK13QQuickToolBar11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickToolBar11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickToolBar::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickToolBar::accessibleRole() const
    ritual = 'ritual_ZNK13QQuickToolBar14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickToolBar14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Position)
  def setPosition(self, position: Position) -> None:
    """
    Calls Qt's 'void QQuickToolBar::setPosition(Position position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#setPosition

    Parameters
    ----------

    position : Position
      Passed on as its number.
    """
    #  void QQuickToolBar::setPosition(Position position)
    self.uglySide.call(
        'ritual_ZN13QQuickToolBar11setPositionENS_8PositionE',
        position.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickToolBar::QQuickToolBar(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#QQuickToolBar

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickToolBar::QQuickToolBar(QQuickItem *parent)
    self._noteCreation(QQuickToolBar, lambda: Rituals.call(
        'ritual_ZN13QQuickToolBarC1EP10QQuickItem', self._addressOf(parent),
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolBar::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolbar.html#positionChanged
    """
    #  void QQuickToolBar::positionChanged()
    self.uglySide.call('ritual_ZN13QQuickToolBar15positionChangedEv')
