"""
QWebEngineUrlRequestInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineurlrequestinfo.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QUrl
  from . import QWebEngineUrlRequestInfoPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']
  QWebEngineUrlRequestInfoPrivate = WAIT['QWebEngineUrlRequestInfoPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineUrlRequestInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineUrlRequestInfo: a plain Python object
  standing in front of one C++ QWebEngineUrlRequestInfo.

  What exists
  -----------

  Every function of Qt's QWebEngineUrlRequestInfo that has a ritual and that
  Python can call so far, 14 names in all: 'resourceType', 'navigationType',
  'requestUrl', 'firstPartyUrl', 'initiator', 'requestMethod', 'requestBody',
  'changed', 'isDownload', 'block', 'redirect', 'setHttpHeader', 'd_func',
  'resetChanged'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHash<QByteArray, QByteArray>
    QWebEngineUrlRequestInfo::httpHeaders() const': gives a type Python has
    no way to take yet.
  - Qt's 'const QWebEngineUrlRequestInfoPrivate
    *QWebEngineUrlRequestInfo::d_func() const': takes in Python what
    'QWebEngineUrlRequestInfoPrivate *QWebEngineUrlRequestInfo::d_func()'
    takes.
  - Qt's 'QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo(
    QWebEngineUrlRequestInfo &&p)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QWebEngineUrlRequestInfo
    &QWebEngineUrlRequestInfo::operator=(QWebEngineUrlRequestInfo &&p)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineUrlRequestInfo::~QWebEngineUrlRequestInfo()': the
    destructor: Python never removes a C++ QWebEngineUrlRequestInfo.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineUrlRequestInfo is created at the first use, not by
    'QWebEngineUrlRequestInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineUrlRequestInfo.
  - Each name of Qt's QWebEngineUrlRequestInfo that has no cute function yet,
    'httpHeaders', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineUrlRequestInfo, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class NavigationType(CuteNum):
    """
    The enum 'QWebEngineUrlRequestInfo::NavigationType' of Qt, with the 7
    names Qt gives in it.
    """

    NavigationTypeLink = Kee[int](0)
    NavigationTypeTyped = Kee[int](1)
    NavigationTypeFormSubmitted = Kee[int](2)
    NavigationTypeBackForward = Kee[int](3)
    NavigationTypeReload = Kee[int](4)
    NavigationTypeOther = Kee[int](5)
    NavigationTypeRedirect = Kee[int](6)

  class ResourceType(CuteNum):
    """
    The enum 'QWebEngineUrlRequestInfo::ResourceType' of Qt, with the 24
    names Qt gives in it.
    """

    ResourceTypeMainFrame = Kee[int](0)
    ResourceTypeSubFrame = Kee[int](1)
    ResourceTypeStylesheet = Kee[int](2)
    ResourceTypeScript = Kee[int](3)
    ResourceTypeImage = Kee[int](4)
    ResourceTypeFontResource = Kee[int](5)
    ResourceTypeSubResource = Kee[int](6)
    ResourceTypeObject = Kee[int](7)
    ResourceTypeMedia = Kee[int](8)
    ResourceTypeWorker = Kee[int](9)
    ResourceTypeSharedWorker = Kee[int](10)
    ResourceTypePrefetch = Kee[int](11)
    ResourceTypeFavicon = Kee[int](12)
    ResourceTypeXhr = Kee[int](13)
    ResourceTypePing = Kee[int](14)
    ResourceTypeServiceWorker = Kee[int](15)
    ResourceTypeCspReport = Kee[int](16)
    ResourceTypePluginResource = Kee[int](17)
    ResourceTypeNavigationPreloadMainFrame = Kee[int](19)
    ResourceTypeNavigationPreloadSubFrame = Kee[int](20)
    ResourceTypeJson = Kee[int](21)
    ResourceTypeLast = Kee[int](21)
    ResourceTypeWebSocket = Kee[int](254)
    ResourceTypeUnknown = Kee[int](255)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineUrlRequestInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceType(self) -> ResourceType:
    """
    Calls Qt's 'ResourceType QWebEngineUrlRequestInfo::resourceType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#resourceType

    Returns
    -------

    ResourceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ResourceType(number)'
      gives.
    """
    #  ResourceType QWebEngineUrlRequestInfo::resourceType() const
    return QWebEngineUrlRequestInfo.ResourceType(self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo12resourceTypeEv',
    ))

  def navigationType(self) -> NavigationType:
    """
    Calls Qt's 'NavigationType QWebEngineUrlRequestInfo::navigationType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#navigationType

    Returns
    -------

    NavigationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NavigationType(number)'
      gives.
    """
    #  NavigationType QWebEngineUrlRequestInfo::navigationType() const
    return QWebEngineUrlRequestInfo.NavigationType(self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo14navigationTypeEv',
    ))

  def requestUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineUrlRequestInfo::requestUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#requestUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineUrlRequestInfo::requestUrl() const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo10requestUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def firstPartyUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineUrlRequestInfo::firstPartyUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#firstPartyUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineUrlRequestInfo::firstPartyUrl() const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo13firstPartyUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def initiator(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineUrlRequestInfo::initiator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#initiator

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineUrlRequestInfo::initiator() const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo9initiatorEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def requestMethod(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWebEngineUrlRequestInfo::requestMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#requestMethod

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWebEngineUrlRequestInfo::requestMethod() const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo13requestMethodEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def requestBody(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QWebEngineUrlRequestInfo::requestBody() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#requestBody

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QWebEngineUrlRequestInfo::requestBody() const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo11requestBodyEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def changed(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineUrlRequestInfo::changed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#changed
    """
    #  bool QWebEngineUrlRequestInfo::changed() const
    return self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo7changedEv',
    )

  def isDownload(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineUrlRequestInfo::isDownload() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#isDownload
    """
    #  bool QWebEngineUrlRequestInfo::isDownload() const
    return self.uglySide.call(
        'ritual_ZNK24QWebEngineUrlRequestInfo10isDownloadEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray, QByteArray)
  def setHttpHeader(self, name: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QWebEngineUrlRequestInfo::setHttpHeader(const QByteArray
    &name, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#setHttpHeader

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebEngineUrlRequestInfo::setHttpHeader(const QByteArray &name,
    #      const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN24QWebEngineUrlRequestInfo13setHttpHeaderERK10QByteArrayS'
        '2_',
        self._valueOf(name), self._valueOf(value),
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
    'QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html
    """
    #  QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo()
    self._noteCreation(QWebEngineUrlRequestInfo, lambda: Rituals.call(
        'ritual_ZN24QWebEngineUrlRequestInfoC1Ev',
    ))

  @overload(QWebEngineUrlRequestInfoPrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QWebEngineUrlRequestInfoPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo(
    QWebEngineUrlRequestInfoPrivate *p)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html

    Parameters
    ----------

    p : Optional[QWebEngineUrlRequestInfoPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo(
    #      QWebEngineUrlRequestInfoPrivate *p)
    self._noteCreation(QWebEngineUrlRequestInfo, lambda: Rituals.call(
        'ritual_ZN24QWebEngineUrlRequestInfoC1EP31QWebEngineUrlRequestInfoP'
        'rivate',
        self._addressOf(p),
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

  @overload(bool)
  def block(self, shouldBlock: bool) -> None:
    """
    Calls Qt's 'void QWebEngineUrlRequestInfo::block(bool shouldBlock)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#block

    Parameters
    ----------

    shouldBlock : bool
      Passed on as it is.
    """
    #  void QWebEngineUrlRequestInfo::block(bool shouldBlock)
    self.uglySide.call(
        'ritual_ZN24QWebEngineUrlRequestInfo5blockEb', shouldBlock,
    )

  @overload(QUrl)
  def redirect(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineUrlRequestInfo::redirect(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#redirect

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineUrlRequestInfo::redirect(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN24QWebEngineUrlRequestInfo8redirectERK4QUrl',
        self._valueOf(url),
    )

  def d_func(self) -> Optional[QWebEngineUrlRequestInfoPrivate]:
    """
    Calls Qt's 'QWebEngineUrlRequestInfoPrivate
    *QWebEngineUrlRequestInfo::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#d_func

    Returns
    -------

    Optional[QWebEngineUrlRequestInfoPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineUrlRequestInfoPrivate *QWebEngineUrlRequestInfo::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QWebEngineUrlRequestInfo6d_funcEv',
    )
    from . import QWebEngineUrlRequestInfoPrivate
    return QWebEngineUrlRequestInfoPrivate._cuteAt(address)

  def resetChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineUrlRequestInfo::resetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfo.html#resetChanged
    """
    #  void QWebEngineUrlRequestInfo::resetChanged()
    self.uglySide.call('ritual_ZN24QWebEngineUrlRequestInfo12resetChangedEv')

  @staticmethod
  def httpHeaders(*__, **_) -> Never:
    """
    Qt's 'QHash<QByteArray, QByteArray>
    QWebEngineUrlRequestInfo::httpHeaders() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineUrlRequestInfo.httpHeaders' has no cute function yet. "
        "Qt's 'QHash<QByteArray, QByteArray> "
        "QWebEngineUrlRequestInfo::httpHeaders() const': gives a type "
        "Python has no way to take yet.")
