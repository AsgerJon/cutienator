"""
QQuickContextMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontextmenu_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickContextMenu to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPointF
  from . import QQuickMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPointF = WAIT['QPointF']
  QQuickMenu = WAIT['QQuickMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContextMenu(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickContextMenu: a plain Python object standing in
  front of one C++ QQuickContextMenu.

  It is built on the cute 'QObject', as Qt's QQuickContextMenu is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickContextMenu is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickContextMenu that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'menu', 'setMenu', 'menuChanged', 'requested',
  'event', 'classBegin', 'componentComplete'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickContextMenu::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickContextMenu::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickContextMenu::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickContextMenu::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QQuickContextMenuPrivate *QQuickContextMenu::d_func()': gives
    'QQuickContextMenuPrivate', which has no cute class yet.
  - Qt's 'const QQuickContextMenuPrivate *QQuickContextMenu::d_func() const':
    gives 'QQuickContextMenuPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickContextMenu is created at the first use, not by
    'QQuickContextMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContextMenu.
  - Qt tells when it has removed the C++ QQuickContextMenu. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QQuickContextMenu::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#tr

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
    #  QString QQuickContextMenu::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickContextMenu2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickContextMenu]:
    """
    Calls Qt's 'QQuickContextMenu
    *QQuickContextMenu::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontextmenu.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickContextMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContextMenu *QQuickContextMenu::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN17QQuickContextMenu21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQuickContextMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContextMenu'

  #  Qt's QQuickContextMenu is built on more than one class. The part of a
  #  C++ QQuickContextMenu that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickContextMenu_QQmlParserStatus',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickContextMenu::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickContextMenu::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickContextMenu10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def menu(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickContextMenu::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#menu

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickContextMenu::menu() const
    address = self.uglySide.call('ritual_ZNK17QQuickContextMenu4menuEv')
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickMenu)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickContextMenu::setMenu(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#setMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContextMenu::setMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN17QQuickContextMenu7setMenuEP10QQuickMenu',
        self._addressOf(menu),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickContextMenu::QQuickContextMenu(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontextmenu.html#QQuickContextMenu

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickContextMenu::QQuickContextMenu(QObject *parent)
    self._noteCreation(QQuickContextMenu, lambda: Rituals.call(
        'ritual_ZN17QQuickContextMenuC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def menuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickContextMenu::menuChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#menuChanged
    """
    #  void QQuickContextMenu::menuChanged()
    self.uglySide.call('ritual_ZN17QQuickContextMenu11menuChangedEv')

  @overload(QPointF)
  def requested(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QQuickContextMenu::requested(QPointF position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#requested

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickContextMenu::requested(QPointF position)
    self.uglySide.call(
        'ritual_ZN17QQuickContextMenu9requestedE7QPointF',
        self._valueOf(position, 'QPointF'),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickContextMenu::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickContextMenu::event(QEvent *a0)
    ritual = 'ritual_ZN17QQuickContextMenu5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickContextMenu5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickContextMenu::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontextmenu.html#classBegin
    """
    #  void QQuickContextMenu::classBegin()
    ritual = 'ritual_ZN17QQuickContextMenu10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickContextMenu10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickContextMenu::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontextmenu.html#componentComplete
    """
    #  void QQuickContextMenu::componentComplete()
    ritual = 'ritual_ZN17QQuickContextMenu17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickContextMenu17componentCompleteEv'
    self.uglySide.call(ritual)
