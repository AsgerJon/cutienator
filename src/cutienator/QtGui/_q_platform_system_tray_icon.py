"""
QPlatformSystemTrayIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformsystemtrayicon.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect
  from . import QIcon, QPlatformMenu, QPlatformScreen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QPlatformMenu = WAIT['QPlatformMenu']
  QPlatformScreen = WAIT['QPlatformScreen']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformSystemTrayIcon(QObject):
  """
  The cute side of Qt's QPlatformSystemTrayIcon: a plain Python object
  standing in front of one C++ QPlatformSystemTrayIcon.

  It is built on the cute 'QObject', as Qt's QPlatformSystemTrayIcon is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformSystemTrayIcon that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'init',
  'cleanup', 'updateIcon', 'updateToolTip', 'updateMenu', 'geometry',
  'showMessage', 'isSystemTrayAvailable', 'supportsMessages', 'createMenu',
  'activated', 'contextMenuRequested', 'messageClicked'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformSystemTrayIcon::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformSystemTrayIcon::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformSystemTrayIcon::~QPlatformSystemTrayIcon()': the
    destructor: Python never removes a C++ QPlatformSystemTrayIcon.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformSystemTrayIcon is created at the first use, not by
    'QPlatformSystemTrayIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformSystemTrayIcon.
  - Qt tells when it has removed the C++ QPlatformSystemTrayIcon. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPlatformSystemTrayIcon, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ActivationReason(CuteNum):
    """
    The enum 'QPlatformSystemTrayIcon::ActivationReason' of Qt, with the 5
    names Qt gives in it.
    """

    Unknown = Kee[int](0)
    Context = Kee[int](1)
    DoubleClick = Kee[int](2)
    Trigger = Kee[int](3)
    MiddleClick = Kee[int](4)

  class MessageIcon(CuteNum):
    """
    The enum 'QPlatformSystemTrayIcon::MessageIcon' of Qt, with the 4 names
    Qt gives in it.
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
    Calls Qt's 'QString QPlatformSystemTrayIcon::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#tr

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
    #  QString QPlatformSystemTrayIcon::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QPlatformSystemTrayIcon2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformSystemTrayIcon'

  #  A C++ QPlatformSystemTrayIcon Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformSystemTrayIcon'

  #  The functions Qt calls itself that QPlatformSystemTrayIcon is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'init': (
          ('_ZN23QPlatformSystemTrayIcon4initEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'cleanup': (
          ('_ZN23QPlatformSystemTrayIcon7cleanupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateIcon': (
          ('_ZN23QPlatformSystemTrayIcon10updateIconERK5QIcon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QIcon'),
           )),
      ),
      'updateToolTip': (
          ('_ZN23QPlatformSystemTrayIcon13updateToolTipERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'updateMenu': (
          ('_ZN23QPlatformSystemTrayIcon10updateMenuEP13QPlatformMenu',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformMenu'),
           )),
      ),
      'geometry': (
          ('_ZNK23QPlatformSystemTrayIcon8geometryEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
      'showMessage': (
          ('_ZN23QPlatformSystemTrayIcon11showMessageERK7QStringS2_RK5QIcon'
           'NS_11MessageIconEi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'value', 'QtGui:QIcon'),
               ('int', 'enum', 'QtGui:QPlatformSystemTrayIcon.MessageIcon'),
               ('int', 'number', ''),
           )),
      ),
      'isSystemTrayAvailable': (
          ('_ZNK23QPlatformSystemTrayIcon21isSystemTrayAvailableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'supportsMessages': (
          ('_ZNK23QPlatformSystemTrayIcon16supportsMessagesEv',
           ('bool', 'number', ''),
           ()),
      ),
      'createMenu': (
          ('_ZNK23QPlatformSystemTrayIcon10createMenuEv',
           ('address', 'address', 'QtGui:QPlatformMenu'),
           ()),
      ),
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
    Calls Qt's 'const QMetaObject *QPlatformSystemTrayIcon::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformSystemTrayIcon::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformSystemTrayIcon10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformSystemTrayIcon::geometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformSystemTrayIcon::geometry() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformSystemTrayIcon8geometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isSystemTrayAvailable(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSystemTrayIcon::isSystemTrayAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#isSystemTrayAvailable
    """
    #  bool QPlatformSystemTrayIcon::isSystemTrayAvailable() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformSystemTrayIcon21isSystemTrayAvailableEv',
    )

  def supportsMessages(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSystemTrayIcon::supportsMessages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#supportsMessages
    """
    #  bool QPlatformSystemTrayIcon::supportsMessages() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformSystemTrayIcon16supportsMessagesEv',
    )

  def createMenu(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QPlatformSystemTrayIcon::createMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#createMenu

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QPlatformSystemTrayIcon::createMenu() const
    ritual = 'ritual_ZNK23QPlatformSystemTrayIcon10createMenuEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformSystemTrayIcon10createMenuEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformSystemTrayIcon::QPlatformSystemTrayIcon()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html
    """
    #  QPlatformSystemTrayIcon::QPlatformSystemTrayIcon()
    self._noteCreation(QPlatformSystemTrayIcon, lambda: Rituals.call(
        'ritual_ZN23QPlatformSystemTrayIconC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#init
    """
    #  void QPlatformSystemTrayIcon::init()
    self.uglySide.call('ritual_ZN23QPlatformSystemTrayIcon4initEv')

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#cleanup
    """
    #  void QPlatformSystemTrayIcon::cleanup()
    self.uglySide.call('ritual_ZN23QPlatformSystemTrayIcon7cleanupEv')

  @overload(QIcon)
  def updateIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::updateIcon(const QIcon &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#updateIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QPlatformSystemTrayIcon::updateIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN23QPlatformSystemTrayIcon10updateIconERK5QIcon',
        self._valueOf(icon),
    )

  @overload(str)
  def updateToolTip(self, tooltip: str) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::updateToolTip(const QString
    &tooltip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#updateToolTip

    Parameters
    ----------

    tooltip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformSystemTrayIcon::updateToolTip(const QString &tooltip)
    self.uglySide.call(
        'ritual_ZN23QPlatformSystemTrayIcon13updateToolTipERK7QString',
        tooltip,
    )

  @overload(QPlatformMenu)
  @overload(NoneType)
  def updateMenu(self, menu: Optional[QPlatformMenu]) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::updateMenu(QPlatformMenu
    *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#updateMenu

    Parameters
    ----------

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformSystemTrayIcon::updateMenu(QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN23QPlatformSystemTrayIcon10updateMenuEP13QPlatformMenu',
        self._addressOf(menu),
    )

  @overload(str, str, QIcon, MessageIcon, int)
  def showMessage(
      self,
      title: str,
      msg: str,
      icon: QIcon,
      iconType: MessageIcon,
      msecs: int,
  ) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::showMessage(const QString
    &title, const QString &msg, const QIcon &icon, MessageIcon iconType, int
    msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#showMessage

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    iconType : MessageIcon
      Passed on as its number.

    msecs : int
      Passed on as it is.
    """
    #  void QPlatformSystemTrayIcon::showMessage(const QString &title, const
    #      QString &msg, const QIcon &icon, MessageIcon iconType, int msecs)
    self.uglySide.call(
        'ritual_ZN23QPlatformSystemTrayIcon11showMessageERK7QStringS2_RK5QI'
        'conNS_11MessageIconEi',
        title, msg, self._valueOf(icon), iconType.value, msecs,
    )

  @overload(ActivationReason)
  def activated(self, reason: ActivationReason) -> None:
    """
    Calls Qt's 'void
    QPlatformSystemTrayIcon::activated(QPlatformSystemTrayIcon::
    ActivationReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#activated

    Parameters
    ----------

    reason : ActivationReason
      Passed on as its number.
    """
    #  void QPlatformSystemTrayIcon::activated(QPlatformSystemTrayIcon::
    #      ActivationReason reason)
    self.uglySide.call(
        'ritual_ZN23QPlatformSystemTrayIcon9activatedENS_16ActivationReason'
        'E',
        reason.value,
    )

  @overload(QPoint, QPlatformScreen)
  @overload(QPoint, NoneType)
  def contextMenuRequested(
      self,
      globalPos: QPoint,
      screen: Optional[QPlatformScreen],
  ) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::contextMenuRequested(QPoint
    globalPos, const QPlatformScreen *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#contextMenuRequested

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    screen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformSystemTrayIcon::contextMenuRequested(QPoint globalPos,
    #      const QPlatformScreen *screen)
    self.uglySide.call(
        'ritual_ZN23QPlatformSystemTrayIcon20contextMenuRequestedE6QPointPK'
        '15QPlatformScreen',
        self._valueOf(globalPos), self._addressOf(screen),
    )

  def messageClicked(self) -> None:
    """
    Calls Qt's 'void QPlatformSystemTrayIcon::messageClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsystemtrayicon.html#messageClicked
    """
    #  void QPlatformSystemTrayIcon::messageClicked()
    self.uglySide.call(
        'ritual_ZN23QPlatformSystemTrayIcon14messageClickedEv',
    )
