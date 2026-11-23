"""
QSystemTrayIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qsystemtrayicon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRect
  from ..QtGui import QIcon
  from . import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QIcon = WAIT['QIcon']
  QMenu = WAIT['QMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSystemTrayIcon(QObject):
  """
  The cute side of Qt's QSystemTrayIcon: a plain Python object standing in
  front of one C++ QSystemTrayIcon.

  It is built on the cute 'QObject', as Qt's QSystemTrayIcon is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSystemTrayIcon that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'setContextMenu',
  'contextMenu', 'icon', 'setIcon', 'toolTip', 'setToolTip',
  'isSystemTrayAvailable', 'supportsMessages', 'geometry', 'isVisible',
  'setVisible', 'show', 'hide', 'showMessage', 'event'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSystemTrayIcon::~QSystemTrayIcon()': the destructor: Python never
    removes a C++ QSystemTrayIcon.

  What has no ritual
  ------------------

  10 of the 31 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QSystemTrayIcon is created at the first use, not by
    'QSystemTrayIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSystemTrayIcon.
  - Qt tells when it has removed the C++ QSystemTrayIcon. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSystemTrayIcon, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ActivationReason(CuteNum):
    """
    The enum 'QSystemTrayIcon::ActivationReason' of Qt, with the 5 names Qt
    gives in it.
    """

    Unknown = Kee[int](0)
    Context = Kee[int](1)
    DoubleClick = Kee[int](2)
    Trigger = Kee[int](3)
    MiddleClick = Kee[int](4)

  class MessageIcon(CuteNum):
    """
    The enum 'QSystemTrayIcon::MessageIcon' of Qt, with the 4 names Qt gives
    in it.
    """

    NoIcon = Kee[int](0)
    Information = Kee[int](1)
    Warning = Kee[int](2)
    Critical = Kee[int](3)

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
    Calls Qt's 'QString QSystemTrayIcon::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#tr

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
    #  QString QSystemTrayIcon::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QSystemTrayIcon2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def isSystemTrayAvailable() -> bool:
    """
    Calls Qt's 'bool QSystemTrayIcon::isSystemTrayAvailable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayicon.html#isSystemTrayAvailable
    """
    #  bool QSystemTrayIcon::isSystemTrayAvailable()
    return Rituals.call(
        'ritual_ZN15QSystemTrayIcon21isSystemTrayAvailableEv',
    )

  @staticmethod
  def supportsMessages() -> bool:
    """
    Calls Qt's 'bool QSystemTrayIcon::supportsMessages()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayicon.html#supportsMessages
    """
    #  bool QSystemTrayIcon::supportsMessages()
    return Rituals.call('ritual_ZN15QSystemTrayIcon16supportsMessagesEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSystemTrayIcon'

  #  A C++ QSystemTrayIcon Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSystemTrayIcon'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSystemTrayIcon::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSystemTrayIcon::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QSystemTrayIcon10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def contextMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QSystemTrayIcon::contextMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#contextMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QSystemTrayIcon::contextMenu() const
    address = self.uglySide.call(
        'ritual_ZNK15QSystemTrayIcon11contextMenuEv',
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QSystemTrayIcon::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QSystemTrayIcon::icon() const
    address = self.uglySide.call('ritual_ZNK15QSystemTrayIcon4iconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QSystemTrayIcon::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSystemTrayIcon::toolTip() const
    return self.uglySide.call('ritual_ZNK15QSystemTrayIcon7toolTipEv')

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QSystemTrayIcon::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSystemTrayIcon::geometry() const
    address = self.uglySide.call('ritual_ZNK15QSystemTrayIcon8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QSystemTrayIcon::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#isVisible
    """
    #  bool QSystemTrayIcon::isVisible() const
    return self.uglySide.call('ritual_ZNK15QSystemTrayIcon9isVisibleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMenu)
  @overload(NoneType)
  def setContextMenu(self, menu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::setContextMenu(QMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayicon.html#setContextMenu

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSystemTrayIcon::setContextMenu(QMenu *menu)
    self.uglySide.call(
        'ritual_ZN15QSystemTrayIcon14setContextMenuEP5QMenu',
        self._addressOf(menu),
    )

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QSystemTrayIcon::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN15QSystemTrayIcon7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(str)
  def setToolTip(self, tip: str) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::setToolTip(const QString &tip)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#setToolTip

    Parameters
    ----------

    tip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSystemTrayIcon::setToolTip(const QString &tip)
    self.uglySide.call(
        'ritual_ZN15QSystemTrayIcon10setToolTipERK7QString', tip,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QSystemTrayIcon::setVisible(bool visible)
    self.uglySide.call('ritual_ZN15QSystemTrayIcon10setVisibleEb', visible)

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
    Notes what was given, for Qt's 'QSystemTrayIcon::QSystemTrayIcon(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayicon.html#QSystemTrayIcon

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSystemTrayIcon::QSystemTrayIcon(QObject *parent)
    self._noteCreation(QSystemTrayIcon, lambda: Rituals.call(
        'ritual_ZN15QSystemTrayIconC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QIcon)
  @overload(QIcon, QObject)
  @overload(QIcon, NoneType)
  def __init__(self, icon: QIcon, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSystemTrayIcon::QSystemTrayIcon(const
    QIcon &icon, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemtrayicon.html#QSystemTrayIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSystemTrayIcon::QSystemTrayIcon(const QIcon &icon, QObject *parent)
    self._noteCreation(QSystemTrayIcon, lambda: Rituals.call(
        'ritual_ZN15QSystemTrayIconC1ERK5QIconP7QObject',
        self._valueOf(icon), self._addressOf(parent, 'QObject'),
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

  def show(self) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#show
    """
    #  void QSystemTrayIcon::show()
    self.uglySide.call('ritual_ZN15QSystemTrayIcon4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#hide
    """
    #  void QSystemTrayIcon::hide()
    self.uglySide.call('ritual_ZN15QSystemTrayIcon4hideEv')

  @overload(str, str, QIcon)
  @overload(str, str, QIcon, int)
  def showMessage(
      self,
      title: str,
      msg: str,
      icon: QIcon,
      msecs: int = 10000,
  ) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::showMessage(const QString &title, const
    QString &msg, const QIcon &icon, int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#showMessage

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 10000.
    """
    #  void QSystemTrayIcon::showMessage(const QString &title, const QString
    #      &msg, const QIcon &icon, int msecs)
    self.uglySide.call(
        'ritual_ZN15QSystemTrayIcon11showMessageERK7QStringS2_RK5QIconi',
        title, msg, self._valueOf(icon), msecs,
    )

  @overload(str, str)
  @overload(str, str, MessageIcon)
  @overload(str, str, MessageIcon, int)
  def showMessage(
      self,
      title: str,
      msg: str,
      icon: MessageIcon = MessageIcon.Information,
      msecs: int = 10000,
  ) -> None:
    """
    Calls Qt's 'void QSystemTrayIcon::showMessage(const QString &title, const
    QString &msg, QSystemTrayIcon::MessageIcon icon, int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#showMessage

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    icon : MessageIcon
      Passed on as its number. May be left out, as in Qt: it is then
      MessageIcon.Information.

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 10000.
    """
    #  void QSystemTrayIcon::showMessage(const QString &title, const QString
    #      &msg, QSystemTrayIcon::MessageIcon icon, int msecs)
    self.uglySide.call(
        'ritual_ZN15QSystemTrayIcon11showMessageERK7QStringS2_NS_11MessageI'
        'conEi',
        title, msg, icon.value, msecs,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSystemTrayIcon::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemtrayicon.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSystemTrayIcon::event(QEvent *event)
    ritual = 'ritual_ZN15QSystemTrayIcon5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QSystemTrayIcon5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))
