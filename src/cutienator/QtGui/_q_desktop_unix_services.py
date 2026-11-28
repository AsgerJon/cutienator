"""
QDesktopUnixServices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdesktopunixservices_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDesktopUnixServices to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QPlatformServices

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QUrl
  from . import QPlatformServiceColorPicker, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesktopUnixServices(QPlatformServices):
  """
  The cute side of Qt's QDesktopUnixServices: a plain Python object standing
  in front of one C++ QDesktopUnixServices.

  It is built on the cute 'QPlatformServices', as Qt's QDesktopUnixServices
  is built on Qt's QPlatformServices, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesktopUnixServices that has a ritual and that
  Python can call so far, 10 names in all: 'desktopEnvironment',
  'hasCapability', 'openUrl', 'openDocument', 'colorPicker',
  'setApplicationBadge', 'portalWindowIdentifier',
  'registerDBusMenuForWindow', 'unregisterDBusMenuForWindow',
  'portalFocusWindowIdentifier'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesktopUnixServices::~QDesktopUnixServices()': the destructor:
    Python never removes a C++ QDesktopUnixServices.

  What has no ritual
  ------------------

  6 of the 18 functions Qt declares: 4 leans on 'QDesktopUnixServices; 1 a
  template; 1 Qt's library has no name for it, and its code in Qt's source
  does not compile apart from its file.

  What to expect
  --------------

  - The C++ QDesktopUnixServices is created at the first use, not by
    'QDesktopUnixServices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesktopUnixServices.
  - Each name of Qt's QDesktopUnixServices that has no cute function yet,
    'launchProcess', 'openDocumentWithPortal', 'openDocumentWithoutPortal',
    'openUrlWithPortal', 'openUrlWithoutPortal', 'runWithXdgActivationToken',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QDesktopUnixServices, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class LaunchType(CuteNum, scoped=True):
    """
    The enum 'QDesktopUnixServices::LaunchType' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Browser = Kee[int](0)
    Document = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesktopUnixServices'

  #  A C++ QDesktopUnixServices Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesktopUnixServices'

  #  The functions Qt calls itself that QDesktopUnixServices is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'portalWindowIdentifier': (
          ('_ZN20QDesktopUnixServices22portalWindowIdentifierEP7QWindow',
           ('address', 'text', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'registerDBusMenuForWindow': (
          ('_ZN20QDesktopUnixServices25registerDBusMenuForWindowEP7QWindowR'
           'K7QStringS4_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'unregisterDBusMenuForWindow': (
          ('_ZN20QDesktopUnixServices27unregisterDBusMenuForWindowEP7QWindo'
           'w',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def desktopEnvironment(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QDesktopUnixServices::desktopEnvironment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html#desktopEnvironment

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDesktopUnixServices::desktopEnvironment() const
    ritual = 'ritual_ZNK20QDesktopUnixServices18desktopEnvironmentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesktopUnixServices18desktopEnvironmentEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QPlatformServices.Capability)
  def hasCapability(self, capability: QPlatformServices.Capability) -> bool:
    """
    Calls Qt's 'bool QDesktopUnixServices::hasCapability(Capability
    capability) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html#hasCapability

    Parameters
    ----------

    capability : QPlatformServices.Capability
      Passed on as its number.
    """
    #  bool QDesktopUnixServices::hasCapability(Capability capability) const
    ritual = (
        'ritual_ZNK20QDesktopUnixServices13hasCapabilityEN17QPlatformServic'
        'es10CapabilityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QDesktopUnixServices13hasCapabilityEN17QPlatform'
          'Services10CapabilityE')
    return self.uglySide.call(ritual, capability.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setApplicationBadge(self, number: int) -> None:
    """
    Calls Qt's 'void QDesktopUnixServices::setApplicationBadge(qint64
    number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html#setApplicationBadge

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void QDesktopUnixServices::setApplicationBadge(qint64 number)
    self.uglySide.call(
        'ritual_ZN20QDesktopUnixServices19setApplicationBadgeEx', number,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDesktopUnixServices::QDesktopUnixServices()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html#QDesktopUnixServices
    """
    #  QDesktopUnixServices::QDesktopUnixServices()
    self._noteCreation(QDesktopUnixServices, lambda: Rituals.call(
        'ritual_ZN20QDesktopUnixServicesC1Ev',
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

  @overload(QUrl)
  def openUrl(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QDesktopUnixServices::openUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesktopunixservices.html#openUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QDesktopUnixServices::openUrl(const QUrl &url)
    ritual = 'ritual_ZN20QDesktopUnixServices7openUrlERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDesktopUnixServices7openUrlERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(url))

  @overload(QUrl)
  def openDocument(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QDesktopUnixServices::openDocument(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html#openDocument

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QDesktopUnixServices::openDocument(const QUrl &url)
    ritual = 'ritual_ZN20QDesktopUnixServices12openDocumentERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDesktopUnixServices12openDocumentERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(url))

  @overload()
  @overload(QWindow)
  @overload(NoneType)
  def colorPicker(
      self,
      parent: Optional[QWindow] = None,
  ) -> Optional[QPlatformServiceColorPicker]:
    """
    Calls Qt's 'QPlatformServiceColorPicker
    *QDesktopUnixServices::colorPicker(QWindow *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html#colorPicker

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QPlatformServiceColorPicker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformServiceColorPicker *QDesktopUnixServices::colorPicker(QWindow
    #      *parent)
    ritual = 'ritual_ZN20QDesktopUnixServices11colorPickerEP7QWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDesktopUnixServices11colorPickerEP7QWindow'
    address = self.uglySide.call(ritual, self._addressOf(parent))
    from . import QPlatformServiceColorPicker
    return QPlatformServiceColorPicker._cuteAt(address)

  @overload(QWindow)
  @overload(NoneType)
  def portalWindowIdentifier(self, window: Optional[QWindow]) -> str:
    """
    Calls Qt's 'QString QDesktopUnixServices::portalWindowIdentifier(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html#portalWindowIdentifier

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesktopUnixServices::portalWindowIdentifier(QWindow *window)
    ritual = (
        'ritual_ZN20QDesktopUnixServices22portalWindowIdentifierEP7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesktopUnixServices22portalWindowIdentifierEP7QW'
          'indow')
    return self.uglySide.call(ritual, self._addressOf(window))

  @overload(QWindow, str, str)
  @overload(NoneType, str, str)
  def registerDBusMenuForWindow(
      self,
      window: Optional[QWindow],
      service: str,
      path: str,
  ) -> None:
    """
    Calls Qt's 'void QDesktopUnixServices::registerDBusMenuForWindow(QWindow
    *window, const QString &service, const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesktopUnixServices::registerDBusMenuForWindow(QWindow *window,
    #      const QString &service, const QString &path)
    ritual = (
        'ritual_ZN20QDesktopUnixServices25registerDBusMenuForWindowEP7QWind'
        'owRK7QStringS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesktopUnixServices25registerDBusMenuForWindowEP'
          '7QWindowRK7QStringS4_')
    self.uglySide.call(ritual, self._addressOf(window), service, path)

  @overload(QWindow)
  @overload(NoneType)
  def unregisterDBusMenuForWindow(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void
    QDesktopUnixServices::unregisterDBusMenuForWindow(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesktopUnixServices::unregisterDBusMenuForWindow(QWindow
    #      *window)
    ritual = (
        'ritual_ZN20QDesktopUnixServices27unregisterDBusMenuForWindowEP7QWi'
        'ndow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesktopUnixServices27unregisterDBusMenuForWindow'
          'EP7QWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  def portalFocusWindowIdentifier(self) -> str:
    """
    Calls Qt's 'QString QDesktopUnixServices::portalFocusWindowIdentifier()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopunixservices.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesktopUnixServices::portalFocusWindowIdentifier()
    return self.uglySide.call(
        'ritual_ZN20QDesktopUnixServices27portalFocusWindowIdentifierEv',
    )

  @staticmethod
  def launchProcess(*__, **_) -> Never:
    """
    Qt's 'bool QDesktopUnixServices::launchProcess(LaunchType type, const
    QUrl &url, const QString &xdgActivationToken)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'detectWebBrowser'.
    """
    raise NotImplementedError(
        "'QDesktopUnixServices.launchProcess' has no cute function yet. "
        "Qt's 'bool QDesktopUnixServices::launchProcess(LaunchType type, "
        "const QUrl &url, const QString &xdgActivationToken)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'detectWebBrowser'.")

  @staticmethod
  def openDocumentWithPortal(*__, **_) -> Never:
    """
    Qt's 'bool QDesktopUnixServices::openDocumentWithPortal(const QUrl &url,
    const QString &xdgActivationToken)': leans on
    'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchType,
    QUrl const&, QString const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDesktopUnixServices.openDocumentWithPortal' has no cute function "
        "yet. Qt's 'bool QDesktopUnixServices::openDocumentWithPortal(const "
        "QUrl &url, const QString &xdgActivationToken)': leans on "
        "'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchTy"
        "pe, QUrl const&, QString const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def openDocumentWithoutPortal(*__, **_) -> Never:
    """
    Qt's 'bool QDesktopUnixServices::openDocumentWithoutPortal(const QUrl
    &url, const QString &xdgActivationToken)': leans on
    'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchType,
    QUrl const&, QString const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDesktopUnixServices.openDocumentWithoutPortal' has no cute "
        "function yet. Qt's 'bool "
        "QDesktopUnixServices::openDocumentWithoutPortal(const QUrl &url, "
        "const QString &xdgActivationToken)': leans on "
        "'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchTy"
        "pe, QUrl const&, QString const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def openUrlWithPortal(*__, **_) -> Never:
    """
    Qt's 'bool QDesktopUnixServices::openUrlWithPortal(const QUrl &url, const
    QString &xdgActivationToken)': leans on
    'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchType,
    QUrl const&, QString const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDesktopUnixServices.openUrlWithPortal' has no cute function yet. "
        "Qt's 'bool QDesktopUnixServices::openUrlWithPortal(const QUrl "
        "&url, const QString &xdgActivationToken)': leans on "
        "'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchTy"
        "pe, QUrl const&, QString const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def openUrlWithoutPortal(*__, **_) -> Never:
    """
    Qt's 'bool QDesktopUnixServices::openUrlWithoutPortal(const QUrl &url,
    const QString &xdgActivationToken)': leans on
    'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchType,
    QUrl const&, QString const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDesktopUnixServices.openUrlWithoutPortal' has no cute function "
        "yet. Qt's 'bool QDesktopUnixServices::openUrlWithoutPortal(const "
        "QUrl &url, const QString &xdgActivationToken)': leans on "
        "'QDesktopUnixServices::launchProcess(QDesktopUnixServices::LaunchTy"
        "pe, QUrl const&, QString const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def runWithXdgActivationToken(*__, **_) -> Never:
    """
    Qt's 'QDesktopUnixServices::runWithXdgActivationToken': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QDesktopUnixServices.runWithXdgActivationToken' has no cute "
        "function yet. Qt's "
        "'QDesktopUnixServices::runWithXdgActivationToken': a template: a "
        "pattern and no single function.")
