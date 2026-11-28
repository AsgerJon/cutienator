"""
QWebEnginePage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginepage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QWebEngineDownloadRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject, QPointF, QRect
  from ..QtCore import QSizeF, QString, QUrl
  from ..QtGui import QAction, QColor, QIcon, QPageLayout, QPageRanges
  from ..QtNetwork import QAuthenticator
  from . import QWebEngineCertificateError
  from . import QWebEngineClientCertificateSelection
  from . import QWebEngineDesktopMediaRequest
  from . import QWebEngineFileSystemAccessRequest, QWebEngineFindTextResult
  from . import QWebEngineFrame, QWebEngineFullScreenRequest
  from . import QWebEngineHistory, QWebEngineHttpRequest
  from . import QWebEngineLoadingInfo, QWebEnginePermission
  from . import QWebEngineProfile, QWebEngineQuotaRequest
  from . import QWebEngineRegisterProtocolHandlerRequest, QWebEngineSettings
  from . import QWebEngineUrlRequestInterceptor, QWebEngineWebAuthUxRequest
  from ..QtWebChannel import QWebChannel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QEvent = WAIT['QEvent']
  QIcon = WAIT['QIcon']
  QPageLayout = WAIT['QPageLayout']
  QPageRanges = WAIT['QPageRanges']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QSizeF = WAIT['QSizeF']
  QString = WAIT['QString']
  QUrl = WAIT['QUrl']
  QWebChannel = WAIT['QWebChannel']
  QWebEngineCertificateError = WAIT['QWebEngineCertificateError']
  QWebEngineClientCertificateSelection = WAIT['QWebEngineClientCertificateSelection']
  QWebEngineDesktopMediaRequest = WAIT['QWebEngineDesktopMediaRequest']
  QWebEngineFileSystemAccessRequest = WAIT['QWebEngineFileSystemAccessRequest']
  QWebEngineFindTextResult = WAIT['QWebEngineFindTextResult']
  QWebEngineFrame = WAIT['QWebEngineFrame']
  QWebEngineFullScreenRequest = WAIT['QWebEngineFullScreenRequest']
  QWebEngineHttpRequest = WAIT['QWebEngineHttpRequest']
  QWebEngineLoadingInfo = WAIT['QWebEngineLoadingInfo']
  QWebEnginePermission = WAIT['QWebEnginePermission']
  QWebEngineProfile = WAIT['QWebEngineProfile']
  QWebEngineQuotaRequest = WAIT['QWebEngineQuotaRequest']
  QWebEngineRegisterProtocolHandlerRequest = WAIT['QWebEngineRegisterProtocolHandlerRequest']
  QWebEngineUrlRequestInterceptor = WAIT['QWebEngineUrlRequestInterceptor']
  QWebEngineWebAuthUxRequest = WAIT['QWebEngineWebAuthUxRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEnginePage(QObject):
  """
  The cute side of Qt's QWebEnginePage: a plain Python object standing in
  front of one C++ QWebEnginePage.

  It is built on the cute 'QObject', as Qt's QWebEnginePage is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEnginePage that has a ritual and that Python can
  call so far, 97 names in all: 'metaObject', 'tr', 'history',
  'hasSelection', 'selectedText', 'profile', 'action', 'triggerAction',
  'replaceMisspelledWord', 'event', 'setFeaturePermission', 'isLoading',
  'load', 'download', 'setHtml', 'setContent', 'title', 'setUrl', 'url',
  'requestedUrl', 'iconUrl', 'icon', 'zoomFactor', 'setZoomFactor',
  'scrollPosition', 'contentsSize', 'runJavaScript', 'settings',
  'webChannel', 'setWebChannel', 'backgroundColor', 'setBackgroundColor',
  'save', 'isAudioMuted', 'setAudioMuted', 'recentlyAudible',
  'renderProcessPid', 'printToPdf', 'setInspectedPage', 'inspectedPage',
  'setDevToolsPage', 'devToolsPage', 'devToolsId',
  'setUrlRequestInterceptor', 'lifecycleState', 'setLifecycleState',
  'recommendedState', 'isVisible', 'setVisible', 'mainFrame', 'loadStarted',
  'loadProgress', 'loadFinished', 'loadingChanged', 'linkHovered',
  'selectionChanged', 'geometryChangeRequested', 'windowCloseRequested',
  'featurePermissionRequested', 'featurePermissionRequestCanceled',
  'fullScreenRequested', 'permissionRequested', 'quotaRequested',
  'registerProtocolHandlerRequested', 'fileSystemAccessRequested',
  'selectClientCertificate', 'authenticationRequired',
  'proxyAuthenticationRequired', 'renderProcessTerminated',
  'desktopMediaRequested', 'certificateError', 'titleChanged', 'urlChanged',
  'iconUrlChanged', 'iconChanged', 'zoomFactorChanged',
  'scrollPositionChanged', 'contentsSizeChanged', 'audioMutedChanged',
  'recentlyAudibleChanged', 'renderProcessPidChanged', 'pdfPrintingFinished',
  'printRequested', 'printRequestedByFrame', 'visibleChanged',
  'lifecycleStateChanged', 'recommendedStateChanged', 'findTextFinished',
  '_q_aboutToDelete', 'webAuthUxRequested', 'createWindow', 'chooseFiles',
  'javaScriptAlert', 'javaScriptConfirm', 'javaScriptPrompt',
  'javaScriptConsoleMessage', 'acceptNavigationRequest'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEnginePage::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWebEnginePage::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEnginePage::~QWebEnginePage()': the destructor: Python never
    removes a C++ QWebEnginePage.
  - Qt's 'void QWebEnginePage::findText(const QString &subString, FindFlags
    options, const std::function<void (const QWebEngineFindTextResult &)>
    &resultCallback)': takes a type Python has no way to hand over yet.
  - Qt's 'void QWebEnginePage::toHtml(const std::function<void (const QString
    &)> &resultCallback) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QWebEnginePage::toPlainText(const std::function<void (const
    QString &)> &resultCallback) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QWebEngineScriptCollection &QWebEnginePage::scripts()': gives a
    type Python has no way to take yet.
  - Qt's 'void QWebEnginePage::printToPdf(const std::function<void (const
    QByteArray &)> &resultCallback, const QPageLayout &layout, const
    QPageRanges &ranges)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QWebEngineFrame>
    QWebEnginePage::findFrameByName(QAnyStringView name)': gives a type
    Python has no way to take yet.
  - Qt's 'void QWebEnginePage::acceptAsNewWindow(QWebEngineNewWindowRequest
    &request)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QWebEnginePage::navigationRequested(QWebEngineNavigationRequest
    &request)': takes a type Python has no way to hand over yet.
  - Qt's 'void QWebEnginePage::newWindowRequested(QWebEngineNewWindowRequest
    &request)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEnginePagePrivate *QWebEnginePage::d_func()': gives
    'QWebEnginePagePrivate', which has no cute class yet.
  - Qt's 'const QWebEnginePagePrivate *QWebEnginePage::d_func() const': gives
    'QWebEnginePagePrivate', which has no cute class yet.
  - Qt's 'void QWebEnginePage::runJavaScriptImpl(const QString &scriptSource,
    quint32 worldId, QtPrivate::QSlotObjectBase *callback)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 121 functions Qt declares: 2 not a gap; 2 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEnginePage is created at the first use, not by
    'QWebEnginePage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEnginePage.
  - Qt tells when it has removed the C++ QWebEnginePage. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEnginePage that has no cute function yet,
    'acceptAsNewWindow', 'findFrameByName', 'findText',
    'navigationRequested', 'newWindowRequested', 'runJavaScriptImpl',
    'scripts', 'toHtml', 'toPlainText', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWebEnginePage, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Feature(CuteNum):
    """
    The enum 'QWebEnginePage::Feature' of Qt, with the 10 names Qt gives in
    it.
    """

    Notifications = Kee[int](0)
    Geolocation = Kee[int](1)
    MediaAudioCapture = Kee[int](2)
    MediaVideoCapture = Kee[int](3)
    MediaAudioVideoCapture = Kee[int](4)
    MouseLock = Kee[int](5)
    DesktopVideoCapture = Kee[int](6)
    DesktopAudioVideoCapture = Kee[int](7)
    ClipboardReadWrite = Kee[int](8)
    LocalFontsAccess = Kee[int](9)

  class FileSelectionMode(CuteNum):
    """
    The enum 'QWebEnginePage::FileSelectionMode' of Qt, with the 4 names Qt
    gives in it.
    """

    FileSelectOpen = Kee[int](0)
    FileSelectOpenMultiple = Kee[int](1)
    FileSelectUploadFolder = Kee[int](2)
    FileSelectSave = Kee[int](3)

  class FindFlag(CuteFlags):
    """
    The flags enum 'QWebEnginePage::FindFlag' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QWebEnginePage::FindFlags'.
    """

    FindBackward = 0x1
    FindCaseSensitively = 0x2

  FindFlags = FindFlag

  class JavaScriptConsoleMessageLevel(CuteNum):
    """
    The enum 'QWebEnginePage::JavaScriptConsoleMessageLevel' of Qt, with the
    3 names Qt gives in it.
    """

    InfoMessageLevel = Kee[int](0)
    WarningMessageLevel = Kee[int](1)
    ErrorMessageLevel = Kee[int](2)

  class LifecycleState(CuteNum, scoped=True):
    """
    The enum 'QWebEnginePage::LifecycleState' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Active = Kee[int](0)
    Frozen = Kee[int](1)
    Discarded = Kee[int](2)

  class NavigationType(CuteNum):
    """
    The enum 'QWebEnginePage::NavigationType' of Qt, with the 7 names Qt
    gives in it.
    """

    NavigationTypeLinkClicked = Kee[int](0)
    NavigationTypeTyped = Kee[int](1)
    NavigationTypeFormSubmitted = Kee[int](2)
    NavigationTypeBackForward = Kee[int](3)
    NavigationTypeReload = Kee[int](4)
    NavigationTypeOther = Kee[int](5)
    NavigationTypeRedirect = Kee[int](6)

  class PermissionPolicy(CuteNum):
    """
    The enum 'QWebEnginePage::PermissionPolicy' of Qt, with the 3 names Qt
    gives in it.
    """

    PermissionUnknown = Kee[int](0)
    PermissionGrantedByUser = Kee[int](1)
    PermissionDeniedByUser = Kee[int](2)

  class RenderProcessTerminationStatus(CuteNum):
    """
    The enum 'QWebEnginePage::RenderProcessTerminationStatus' of Qt, with the
    4 names Qt gives in it.
    """

    NormalTerminationStatus = Kee[int](0)
    AbnormalTerminationStatus = Kee[int](1)
    CrashedTerminationStatus = Kee[int](2)
    KilledTerminationStatus = Kee[int](3)

  class WebAction(CuteNum):
    """
    The enum 'QWebEnginePage::WebAction' of Qt, with the 49 names Qt gives in
    it.
    """

    NoWebAction = Kee[int](-1)
    Back = Kee[int](0)
    Forward = Kee[int](1)
    Stop = Kee[int](2)
    Reload = Kee[int](3)
    Cut = Kee[int](4)
    Copy = Kee[int](5)
    Paste = Kee[int](6)
    Undo = Kee[int](7)
    Redo = Kee[int](8)
    SelectAll = Kee[int](9)
    ReloadAndBypassCache = Kee[int](10)
    PasteAndMatchStyle = Kee[int](11)
    OpenLinkInThisWindow = Kee[int](12)
    OpenLinkInNewWindow = Kee[int](13)
    OpenLinkInNewTab = Kee[int](14)
    CopyLinkToClipboard = Kee[int](15)
    DownloadLinkToDisk = Kee[int](16)
    CopyImageToClipboard = Kee[int](17)
    CopyImageUrlToClipboard = Kee[int](18)
    DownloadImageToDisk = Kee[int](19)
    CopyMediaUrlToClipboard = Kee[int](20)
    ToggleMediaControls = Kee[int](21)
    ToggleMediaLoop = Kee[int](22)
    ToggleMediaPlayPause = Kee[int](23)
    ToggleMediaMute = Kee[int](24)
    DownloadMediaToDisk = Kee[int](25)
    InspectElement = Kee[int](26)
    ExitFullScreen = Kee[int](27)
    RequestClose = Kee[int](28)
    Unselect = Kee[int](29)
    SavePage = Kee[int](30)
    OpenLinkInNewBackgroundTab = Kee[int](31)
    ViewSource = Kee[int](32)
    ToggleBold = Kee[int](33)
    ToggleItalic = Kee[int](34)
    ToggleUnderline = Kee[int](35)
    ToggleStrikethrough = Kee[int](36)
    AlignLeft = Kee[int](37)
    AlignCenter = Kee[int](38)
    AlignRight = Kee[int](39)
    AlignJustified = Kee[int](40)
    Indent = Kee[int](41)
    Outdent = Kee[int](42)
    InsertOrderedList = Kee[int](43)
    InsertUnorderedList = Kee[int](44)
    ChangeTextDirectionLTR = Kee[int](45)
    ChangeTextDirectionRTL = Kee[int](46)
    WebActionCount = Kee[int](47)

  class WebWindowType(CuteNum):
    """
    The enum 'QWebEnginePage::WebWindowType' of Qt, with the 4 names Qt gives
    in it.
    """

    WebBrowserWindow = Kee[int](0)
    WebBrowserTab = Kee[int](1)
    WebDialog = Kee[int](2)
    WebBrowserBackgroundTab = Kee[int](3)

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
    Calls Qt's 'QString QWebEnginePage::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#tr

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
    #  QString QWebEnginePage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QWebEnginePage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEnginePage'

  #  A C++ QWebEnginePage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEnginePage'

  #  The functions Qt calls itself that QWebEnginePage is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'chooseFiles': (
          'QStringList QWebEnginePage::chooseFiles(FileSelectionMode, '
          'const QStringList &, const QStringList &)',
      ),
  }

  #  The functions Qt calls itself that QWebEnginePage is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'triggerAction': (
          ('_ZN14QWebEnginePage13triggerActionENS_9WebActionEb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWebEngineCore:QWebEnginePage.WebAction'),
               ('bool', 'number', ''),
           )),
      ),
      'createWindow': (
          ('_ZN14QWebEnginePage12createWindowENS_13WebWindowTypeE',
           ('address', 'address', 'QtWebEngineCore:QWebEnginePage'),
           (
               ('int', 'enum',
                'QtWebEngineCore:QWebEnginePage.WebWindowType'),
           )),
      ),
      'javaScriptAlert': (
          ('_ZN14QWebEnginePage15javaScriptAlertERK4QUrlRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'text', ''),
           )),
      ),
      'javaScriptConfirm': (
          ('_ZN14QWebEnginePage17javaScriptConfirmERK4QUrlRK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'text', ''),
           )),
      ),
      'javaScriptPrompt': (
          ('_ZN14QWebEnginePage16javaScriptPromptERK4QUrlRK7QStringS5_PS3_',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
      'javaScriptConsoleMessage': (
          ('_ZN14QWebEnginePage24javaScriptConsoleMessageENS_29JavaScriptCo'
           'nsoleMessageLevelERK7QStringiS3_',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtWebEngineCore:QWebEnginePage.JavaScriptConsoleMessageLevel'),
               ('address', 'text', ''),
               ('int', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'acceptNavigationRequest': (
          ('_ZN14QWebEnginePage23acceptNavigationRequestERK4QUrlNS_14Naviga'
           'tionTypeEb',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('int', 'enum',
                'QtWebEngineCore:QWebEnginePage.NavigationType'),
               ('bool', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEnginePage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEnginePage::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def history(self) -> Optional[QWebEngineHistory]:
    """
    Calls Qt's 'QWebEngineHistory *QWebEnginePage::history() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#history

    Returns
    -------

    Optional[QWebEngineHistory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistory *QWebEnginePage::history() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage7historyEv')
    from . import QWebEngineHistory
    return QWebEngineHistory._cuteAt(address)

  def hasSelection(self) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::hasSelection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#hasSelection
    """
    #  bool QWebEnginePage::hasSelection() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage12hasSelectionEv')

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QWebEnginePage::selectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEnginePage::selectedText() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage12selectedTextEv')

  def profile(self) -> Optional[QWebEngineProfile]:
    """
    Calls Qt's 'QWebEngineProfile *QWebEnginePage::profile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#profile

    Returns
    -------

    Optional[QWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineProfile *QWebEnginePage::profile() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage7profileEv')
    from . import QWebEngineProfile
    return QWebEngineProfile._cuteAt(address)

  @overload(WebAction)
  def action(self, action: WebAction) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWebEnginePage::action(WebAction action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#action

    Parameters
    ----------

    action : WebAction
      Passed on as its number.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWebEnginePage::action(WebAction action) const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEnginePage6actionENS_9WebActionE', action.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#isLoading
    """
    #  bool QWebEnginePage::isLoading() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage9isLoadingEv')

  def title(self) -> str:
    """
    Calls Qt's 'QString QWebEnginePage::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEnginePage::title() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage5titleEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEnginePage::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEnginePage::url() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def requestedUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEnginePage::requestedUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#requestedUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEnginePage::requestedUrl() const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEnginePage12requestedUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def iconUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEnginePage::iconUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#iconUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEnginePage::iconUrl() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage7iconUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QWebEnginePage::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QWebEnginePage::icon() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage4iconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def zoomFactor(self) -> float:
    """
    Calls Qt's 'qreal QWebEnginePage::zoomFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#zoomFactor
    """
    #  qreal QWebEnginePage::zoomFactor() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage10zoomFactorEv')

  def scrollPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QWebEnginePage::scrollPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#scrollPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QWebEnginePage::scrollPosition() const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEnginePage14scrollPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def contentsSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QWebEnginePage::contentsSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#contentsSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QWebEnginePage::contentsSize() const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEnginePage12contentsSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def settings(self) -> Optional[QWebEngineSettings]:
    """
    Calls Qt's 'QWebEngineSettings *QWebEnginePage::settings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#settings

    Returns
    -------

    Optional[QWebEngineSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineSettings *QWebEnginePage::settings() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage8settingsEv')
    from . import QWebEngineSettings
    return QWebEngineSettings._cuteAt(address)

  def webChannel(self) -> Optional[QWebChannel]:
    """
    Calls Qt's 'QWebChannel *QWebEnginePage::webChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#webChannel

    Returns
    -------

    Optional[QWebChannel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebChannel *QWebEnginePage::webChannel() const
    address = self.uglySide.call('ritual_ZNK14QWebEnginePage10webChannelEv')
    from ..QtWebChannel import QWebChannel
    return QWebChannel._cuteAt(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QWebEnginePage::backgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QWebEnginePage::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEnginePage15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isAudioMuted(self) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::isAudioMuted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#isAudioMuted
    """
    #  bool QWebEnginePage::isAudioMuted() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage12isAudioMutedEv')

  def recentlyAudible(self) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::recentlyAudible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#recentlyAudible
    """
    #  bool QWebEnginePage::recentlyAudible() const
    return self.uglySide.call(
        'ritual_ZNK14QWebEnginePage15recentlyAudibleEv',
    )

  def renderProcessPid(self) -> int:
    """
    Calls Qt's 'qint64 QWebEnginePage::renderProcessPid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#renderProcessPid
    """
    #  qint64 QWebEnginePage::renderProcessPid() const
    return self.uglySide.call(
        'ritual_ZNK14QWebEnginePage16renderProcessPidEv',
    )

  def inspectedPage(self) -> Optional[QWebEnginePage]:
    """
    Calls Qt's 'QWebEnginePage *QWebEnginePage::inspectedPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#inspectedPage

    Returns
    -------

    Optional[QWebEnginePage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEnginePage *QWebEnginePage::inspectedPage() const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEnginePage13inspectedPageEv',
    )
    return QWebEnginePage._cuteAt(address)

  def devToolsPage(self) -> Optional[QWebEnginePage]:
    """
    Calls Qt's 'QWebEnginePage *QWebEnginePage::devToolsPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#devToolsPage

    Returns
    -------

    Optional[QWebEnginePage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEnginePage *QWebEnginePage::devToolsPage() const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEnginePage12devToolsPageEv',
    )
    return QWebEnginePage._cuteAt(address)

  def devToolsId(self) -> str:
    """
    Calls Qt's 'QString QWebEnginePage::devToolsId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#devToolsId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEnginePage::devToolsId() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage10devToolsIdEv')

  def lifecycleState(self) -> LifecycleState:
    """
    Calls Qt's 'LifecycleState QWebEnginePage::lifecycleState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#lifecycleState

    Returns
    -------

    LifecycleState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LifecycleState(number)'
      gives.
    """
    #  LifecycleState QWebEnginePage::lifecycleState() const
    return QWebEnginePage.LifecycleState(self.uglySide.call(
        'ritual_ZNK14QWebEnginePage14lifecycleStateEv',
    ))

  def recommendedState(self) -> LifecycleState:
    """
    Calls Qt's 'LifecycleState QWebEnginePage::recommendedState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#recommendedState

    Returns
    -------

    LifecycleState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LifecycleState(number)'
      gives.
    """
    #  LifecycleState QWebEnginePage::recommendedState() const
    return QWebEnginePage.LifecycleState(self.uglySide.call(
        'ritual_ZNK14QWebEnginePage16recommendedStateEv',
    ))

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#isVisible
    """
    #  bool QWebEnginePage::isVisible() const
    return self.uglySide.call('ritual_ZNK14QWebEnginePage9isVisibleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl, Feature, PermissionPolicy)
  def setFeaturePermission(
      self,
      securityOrigin: QUrl,
      feature: Feature,
      policy: PermissionPolicy,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setFeaturePermission(const QUrl
    &securityOrigin, Feature feature, PermissionPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#setFeaturePermission

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    feature : Feature
      Passed on as its number.

    policy : PermissionPolicy
      Passed on as its number.
    """
    #  void QWebEnginePage::setFeaturePermission(const QUrl &securityOrigin,
    #      Feature feature, PermissionPolicy policy)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage20setFeaturePermissionERK4QUrlNS_7Feature'
        'ENS_16PermissionPolicyE',
        self._valueOf(securityOrigin), feature.value, policy.value,
    )

  @overload(str)
  @overload(str, QUrl)
  def setHtml(self, html: str, baseUrl: Optional[QUrl] = None) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setHtml(const QString &html, const QUrl
    &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#setHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    baseUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QWebEnginePage::setHtml(const QString &html, const QUrl &baseUrl)
    if baseUrl is None:
      from ..QtCore import QUrl
      baseUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage7setHtmlERK7QStringRK4QUrl',
        html, self._valueOf(baseUrl),
    )

  @overload(QByteArray)
  @overload(QByteArray, str)
  @overload(QByteArray, str, QUrl)
  def setContent(
      self,
      data: QByteArray,
      mimeType: str = '',
      baseUrl: Optional[QUrl] = None,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setContent(const QByteArray &data, const
    QString &mimeType, const QUrl &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#setContent

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    mimeType : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    baseUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QWebEnginePage::setContent(const QByteArray &data, const QString
    #      &mimeType, const QUrl &baseUrl)
    if baseUrl is None:
      from ..QtCore import QUrl
      baseUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage10setContentERK10QByteArrayRK7QStringRK4Q'
        'Url',
        self._valueOf(data), mimeType, self._valueOf(baseUrl),
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEnginePage::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(float)
  def setZoomFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setZoomFactor(qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#setZoomFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QWebEnginePage::setZoomFactor(qreal factor)
    self.uglySide.call('ritual_ZN14QWebEnginePage13setZoomFactorEd', factor)

  @overload(QWebChannel)
  @overload(NoneType)
  @overload(QWebChannel, int)
  @overload(NoneType, int)
  def setWebChannel(
      self,
      a0: Optional[QWebChannel],
      worldId: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setWebChannel(QWebChannel *a0, quint32
    worldId)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#setWebChannel

    Parameters
    ----------

    a0 : Optional[QWebChannel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    worldId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QWebEnginePage::setWebChannel(QWebChannel *a0, quint32 worldId)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage13setWebChannelEP11QWebChannelj',
        self._addressOf(a0), worldId,
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setBackgroundColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QWebEnginePage::setBackgroundColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage18setBackgroundColorERK6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setAudioMuted(self, muted: bool) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setAudioMuted(bool muted)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#setAudioMuted

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QWebEnginePage::setAudioMuted(bool muted)
    self.uglySide.call('ritual_ZN14QWebEnginePage13setAudioMutedEb', muted)

  @overload(THIS)
  @overload(NoneType)
  def setInspectedPage(self, page: Optional[QWebEnginePage]) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setInspectedPage(QWebEnginePage *page)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#setInspectedPage

    Parameters
    ----------

    page : Optional[QWebEnginePage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEnginePage::setInspectedPage(QWebEnginePage *page)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage16setInspectedPageEPS_',
        self._addressOf(page),
    )

  @overload(THIS)
  @overload(NoneType)
  def setDevToolsPage(self, page: Optional[QWebEnginePage]) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setDevToolsPage(QWebEnginePage *page)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#setDevToolsPage

    Parameters
    ----------

    page : Optional[QWebEnginePage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEnginePage::setDevToolsPage(QWebEnginePage *page)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage15setDevToolsPageEPS_',
        self._addressOf(page),
    )

  @overload(QWebEngineUrlRequestInterceptor)
  @overload(NoneType)
  def setUrlRequestInterceptor(
      self,
      interceptor: Optional[QWebEngineUrlRequestInterceptor],
  ) -> None:
    """
    Calls Qt's 'void
    QWebEnginePage::setUrlRequestInterceptor(QWebEngineUrlRequestInterceptor
    *interceptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#setUrlRequestInterceptor

    Parameters
    ----------

    interceptor : Optional[QWebEngineUrlRequestInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEnginePage::setUrlRequestInterceptor(
    #      QWebEngineUrlRequestInterceptor *interceptor)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage24setUrlRequestInterceptorEP31QWebEngineU'
        'rlRequestInterceptor',
        self._addressOf(interceptor),
    )

  @overload(LifecycleState)
  def setLifecycleState(self, state: LifecycleState) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setLifecycleState(LifecycleState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#setLifecycleState

    Parameters
    ----------

    state : LifecycleState
      Passed on as its number.
    """
    #  void QWebEnginePage::setLifecycleState(LifecycleState state)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage17setLifecycleStateENS_14LifecycleStateE',
        state.value,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QWebEnginePage::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QWebEnginePage::setVisible(bool visible)
    self.uglySide.call('ritual_ZN14QWebEnginePage10setVisibleEb', visible)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWebEngineProfile)
  @overload(QWebEngineProfile, QObject)
  @overload(QWebEngineProfile, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      profile: Optional[QWebEngineProfile],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebEnginePage::QWebEnginePage(QWebEngineProfile *profile, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#QWebEnginePage

    Parameters
    ----------

    profile : Optional[QWebEngineProfile]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEnginePage::QWebEnginePage(QWebEngineProfile *profile, QObject
    #      *parent)
    self._noteCreation(QWebEnginePage, lambda: Rituals.call(
        'ritual_ZN14QWebEnginePageC1EP17QWebEngineProfileP7QObject',
        self._addressOf(profile), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QWebEnginePage::QWebEnginePage(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#QWebEnginePage

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEnginePage::QWebEnginePage(QObject *parent)
    self._noteCreation(QWebEnginePage, lambda: Rituals.call(
        'ritual_ZN14QWebEnginePageC1EP7QObject',
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

  @overload(WebAction)
  @overload(WebAction, bool)
  def triggerAction(self, action: WebAction, checked: bool = False) -> None:
    """
    Calls Qt's 'void QWebEnginePage::triggerAction(WebAction action, bool
    checked)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#triggerAction

    Parameters
    ----------

    action : WebAction
      Passed on as its number.

    checked : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWebEnginePage::triggerAction(WebAction action, bool checked)
    ritual = 'ritual_ZN14QWebEnginePage13triggerActionENS_9WebActionEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWebEnginePage13triggerActionENS_9WebActionEb'
    self.uglySide.call(ritual, action.value, checked)

  @overload(str)
  def replaceMisspelledWord(self, replacement: str) -> None:
    """
    Calls Qt's 'void QWebEnginePage::replaceMisspelledWord(const QString
    &replacement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#replaceMisspelledWord

    Parameters
    ----------

    replacement : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEnginePage::replaceMisspelledWord(const QString &replacement)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage21replaceMisspelledWordERK7QString',
        replacement,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWebEnginePage::event(QEvent *a0)
    ritual = 'ritual_ZN14QWebEnginePage5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWebEnginePage5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QUrl)
  def load(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEnginePage::load(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#load

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEnginePage::load(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage4loadERK4QUrl', self._valueOf(url),
    )

  @overload(QWebEngineHttpRequest)
  def load(self, request: QWebEngineHttpRequest) -> None:
    """
    Calls Qt's 'void QWebEnginePage::load(const QWebEngineHttpRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#load

    Parameters
    ----------

    request : QWebEngineHttpRequest
      Passed on as a value: Qt reads the C++ QWebEngineHttpRequest, which
      stays Python's own.
    """
    #  void QWebEnginePage::load(const QWebEngineHttpRequest &request)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage4loadERK21QWebEngineHttpRequest',
        self._valueOf(request),
    )

  @overload(QUrl)
  @overload(QUrl, str)
  def download(self, url: QUrl, filename: str = '') -> None:
    """
    Calls Qt's 'void QWebEnginePage::download(const QUrl &url, const QString
    &filename)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#download

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    filename : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QWebEnginePage::download(const QUrl &url, const QString
    #      &filename)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage8downloadERK4QUrlRK7QString',
        self._valueOf(url), filename,
    )

  @overload(str)
  @overload(str, int)
  def runJavaScript(self, scriptSource: str, worldId: int = 0) -> None:
    """
    Calls Qt's 'void QWebEnginePage::runJavaScript(const QString
    &scriptSource, quint32 worldId)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#runJavaScript

    Parameters
    ----------

    scriptSource : str
      Passed on as it is: a QString is made of it for the call.

    worldId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QWebEnginePage::runJavaScript(const QString &scriptSource,
    #      quint32 worldId)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage13runJavaScriptERK7QStringj',
        scriptSource, worldId,
    )

  @overload(str)
  @overload(str, QWebEngineDownloadRequest.SavePageFormat)
  def save(
      self,
      filePath: str,
      format: QWebEngineDownloadRequest.SavePageFormat = (
          QWebEngineDownloadRequest.SavePageFormat.MimeHtmlSaveFormat),
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::save(const QString &filePath,
    QWebEngineDownloadRequest::SavePageFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#save

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    format : QWebEngineDownloadRequest.SavePageFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QWebEngineDownloadRequest.SavePageFormat.MimeHtmlSaveFormat.
    """
    #  void QWebEnginePage::save(const QString &filePath,
    #      QWebEngineDownloadRequest::SavePageFormat format) const
    self.uglySide.call(
        'ritual_ZNK14QWebEnginePage4saveERK7QStringN25QWebEngineDownloadReq'
        'uest14SavePageFormatE',
        filePath, format.value,
    )

  @overload(str, QPageLayout)
  @overload(str, QPageLayout, QPageRanges)
  def printToPdf(
      self,
      filePath: str,
      layout: QPageLayout,
      ranges: Optional[QPageRanges] = None,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::printToPdf(const QString &filePath,
    const QPageLayout &layout, const QPageRanges &ranges)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#printToPdf

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    layout : QPageLayout
      Passed on as a value: Qt reads the C++ QPageLayout, which stays
      Python's own.

    ranges : Optional[QPageRanges]
      Passed on as a value: Qt reads the C++ QPageRanges, which stays
      Python's own. May be left out, as in Qt: a new 'QPageRanges()' is then
      passed on.
    """
    #  void QWebEnginePage::printToPdf(const QString &filePath, const
    #      QPageLayout &layout, const QPageRanges &ranges)
    if ranges is None:
      from ..QtGui import QPageRanges
      ranges = QPageRanges()
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage10printToPdfERK7QStringRK11QPageLayoutRK1'
        '1QPageRanges',
        filePath, self._valueOf(layout), self._valueOf(ranges),
    )

  def mainFrame(self) -> QWebEngineFrame:
    """
    Calls Qt's 'QWebEngineFrame QWebEnginePage::mainFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#mainFrame

    Returns
    -------

    QWebEngineFrame
      A new cute QWebEngineFrame around the copy Qt gave back. Python owns
      it.
    """
    #  QWebEngineFrame QWebEnginePage::mainFrame()
    address = self.uglySide.call('ritual_ZN14QWebEnginePage9mainFrameEv')
    from . import QWebEngineFrame
    return QWebEngineFrame._cuteOwning(address)

  def loadStarted(self) -> None:
    """
    Calls Qt's 'void QWebEnginePage::loadStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#loadStarted
    """
    #  void QWebEnginePage::loadStarted()
    self.uglySide.call('ritual_ZN14QWebEnginePage11loadStartedEv')

  @overload(int)
  def loadProgress(self, progress: int) -> None:
    """
    Calls Qt's 'void QWebEnginePage::loadProgress(int progress)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#loadProgress

    Parameters
    ----------

    progress : int
      Passed on as it is.
    """
    #  void QWebEnginePage::loadProgress(int progress)
    self.uglySide.call('ritual_ZN14QWebEnginePage12loadProgressEi', progress)

  @overload(bool)
  def loadFinished(self, ok: bool) -> None:
    """
    Calls Qt's 'void QWebEnginePage::loadFinished(bool ok)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#loadFinished

    Parameters
    ----------

    ok : bool
      Passed on as it is.
    """
    #  void QWebEnginePage::loadFinished(bool ok)
    self.uglySide.call('ritual_ZN14QWebEnginePage12loadFinishedEb', ok)

  @overload(QWebEngineLoadingInfo)
  def loadingChanged(self, loadingInfo: QWebEngineLoadingInfo) -> None:
    """
    Calls Qt's 'void QWebEnginePage::loadingChanged(const
    QWebEngineLoadingInfo &loadingInfo)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#loadingChanged

    Parameters
    ----------

    loadingInfo : QWebEngineLoadingInfo
      Passed on as a value: Qt reads the C++ QWebEngineLoadingInfo, which
      stays Python's own.
    """
    #  void QWebEnginePage::loadingChanged(const QWebEngineLoadingInfo
    #      &loadingInfo)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage14loadingChangedERK21QWebEngineLoadingInf'
        'o',
        self._valueOf(loadingInfo),
    )

  @overload(str)
  def linkHovered(self, url: str) -> None:
    """
    Calls Qt's 'void QWebEnginePage::linkHovered(const QString &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#linkHovered

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEnginePage::linkHovered(const QString &url)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage11linkHoveredERK7QString', url,
    )

  def selectionChanged(self) -> None:
    """
    Calls Qt's 'void QWebEnginePage::selectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#selectionChanged
    """
    #  void QWebEnginePage::selectionChanged()
    self.uglySide.call('ritual_ZN14QWebEnginePage16selectionChangedEv')

  @overload(QRect)
  def geometryChangeRequested(self, geom: QRect) -> None:
    """
    Calls Qt's 'void QWebEnginePage::geometryChangeRequested(const QRect
    &geom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#geometryChangeRequested

    Parameters
    ----------

    geom : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWebEnginePage::geometryChangeRequested(const QRect &geom)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage23geometryChangeRequestedERK5QRect',
        self._valueOf(geom),
    )

  def windowCloseRequested(self) -> None:
    """
    Calls Qt's 'void QWebEnginePage::windowCloseRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#windowCloseRequested
    """
    #  void QWebEnginePage::windowCloseRequested()
    self.uglySide.call('ritual_ZN14QWebEnginePage20windowCloseRequestedEv')

  @overload(QUrl, Feature)
  def featurePermissionRequested(
      self,
      securityOrigin: QUrl,
      feature: Feature,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::featurePermissionRequested(const QUrl
    &securityOrigin, QWebEnginePage::Feature feature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#featurePermissionRequested

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    feature : Feature
      Passed on as its number.
    """
    #  void QWebEnginePage::featurePermissionRequested(const QUrl
    #      &securityOrigin, QWebEnginePage::Feature feature)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage26featurePermissionRequestedERK4QUrlNS_7F'
        'eatureE',
        self._valueOf(securityOrigin), feature.value,
    )

  @overload(QUrl, Feature)
  def featurePermissionRequestCanceled(
      self,
      securityOrigin: QUrl,
      feature: Feature,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::featurePermissionRequestCanceled(const
    QUrl &securityOrigin, QWebEnginePage::Feature feature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    feature : Feature
      Passed on as its number.
    """
    #  void QWebEnginePage::featurePermissionRequestCanceled(const QUrl
    #      &securityOrigin, QWebEnginePage::Feature feature)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage32featurePermissionRequestCanceledERK4QUr'
        'lNS_7FeatureE',
        self._valueOf(securityOrigin), feature.value,
    )

  @overload(QWebEngineFullScreenRequest)
  def fullScreenRequested(
      self,
      fullScreenRequest: QWebEngineFullScreenRequest,
  ) -> None:
    """
    Calls Qt's 'void
    QWebEnginePage::fullScreenRequested(QWebEngineFullScreenRequest
    fullScreenRequest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#fullScreenRequested

    Parameters
    ----------

    fullScreenRequest : QWebEngineFullScreenRequest
      Passed on as a value: Qt reads the C++ QWebEngineFullScreenRequest,
      which stays Python's own.
    """
    #  void QWebEnginePage::fullScreenRequested(QWebEngineFullScreenRequest
    #      fullScreenRequest)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage19fullScreenRequestedE27QWebEngineFullScr'
        'eenRequest',
        self._valueOf(fullScreenRequest),
    )

  @overload(QWebEnginePermission)
  def permissionRequested(
      self,
      permissionRequest: QWebEnginePermission,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::permissionRequested(QWebEnginePermission
    permissionRequest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#permissionRequested

    Parameters
    ----------

    permissionRequest : QWebEnginePermission
      Passed on as a value: Qt reads the C++ QWebEnginePermission, which
      stays Python's own.
    """
    #  void QWebEnginePage::permissionRequested(QWebEnginePermission
    #      permissionRequest)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage19permissionRequestedE20QWebEnginePermiss'
        'ion',
        self._valueOf(permissionRequest),
    )

  @overload(QWebEngineQuotaRequest)
  def quotaRequested(self, quotaRequest: QWebEngineQuotaRequest) -> None:
    """
    Calls Qt's 'void QWebEnginePage::quotaRequested(QWebEngineQuotaRequest
    quotaRequest)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#quotaRequested

    Parameters
    ----------

    quotaRequest : QWebEngineQuotaRequest
      Passed on as a value: Qt reads the C++ QWebEngineQuotaRequest, which
      stays Python's own.
    """
    #  void QWebEnginePage::quotaRequested(QWebEngineQuotaRequest
    #      quotaRequest)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage14quotaRequestedE22QWebEngineQuotaRequest',
        self._valueOf(quotaRequest),
    )

  @overload(QWebEngineRegisterProtocolHandlerRequest)
  def registerProtocolHandlerRequested(
      self,
      request: QWebEngineRegisterProtocolHandlerRequest,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::registerProtocolHandlerRequested(
    QWebEngineRegisterProtocolHandlerRequest request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html

    Parameters
    ----------

    request : QWebEngineRegisterProtocolHandlerRequest
      Passed on as a value: Qt reads the C++
      QWebEngineRegisterProtocolHandlerRequest, which stays Python's own.
    """
    #  void QWebEnginePage::registerProtocolHandlerRequested(
    #      QWebEngineRegisterProtocolHandlerRequest request)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage32registerProtocolHandlerRequestedE40QWeb'
        'EngineRegisterProtocolHandlerRequest',
        self._valueOf(request),
    )

  @overload(QWebEngineFileSystemAccessRequest)
  def fileSystemAccessRequested(
      self,
      request: QWebEngineFileSystemAccessRequest,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::fileSystemAccessRequested(
    QWebEngineFileSystemAccessRequest request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#fileSystemAccessRequested

    Parameters
    ----------

    request : QWebEngineFileSystemAccessRequest
      Passed on as a value: Qt reads the C++
      QWebEngineFileSystemAccessRequest, which stays Python's own.
    """
    #  void QWebEnginePage::fileSystemAccessRequested(
    #      QWebEngineFileSystemAccessRequest request)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage25fileSystemAccessRequestedE33QWebEngineF'
        'ileSystemAccessRequest',
        self._valueOf(request),
    )

  @overload(QWebEngineClientCertificateSelection)
  def selectClientCertificate(
      self,
      clientCertSelection: QWebEngineClientCertificateSelection,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::selectClientCertificate(
    QWebEngineClientCertificateSelection clientCertSelection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#selectClientCertificate

    Parameters
    ----------

    clientCertSelection : QWebEngineClientCertificateSelection
      Passed on as a value: Qt reads the C++
      QWebEngineClientCertificateSelection, which stays Python's own.
    """
    #  void QWebEnginePage::selectClientCertificate(
    #      QWebEngineClientCertificateSelection clientCertSelection)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage23selectClientCertificateE36QWebEngineCli'
        'entCertificateSelection',
        self._valueOf(clientCertSelection),
    )

  @overload(QUrl, QAuthenticator)
  @overload(QUrl, NoneType)
  def authenticationRequired(
      self,
      requestUrl: QUrl,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::authenticationRequired(const QUrl
    &requestUrl, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#authenticationRequired

    Parameters
    ----------

    requestUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEnginePage::authenticationRequired(const QUrl &requestUrl,
    #      QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage22authenticationRequiredERK4QUrlP14QAuthe'
        'nticator',
        self._valueOf(requestUrl), self._addressOf(authenticator),
    )

  @overload(QUrl, QAuthenticator, str)
  @overload(QUrl, NoneType, str)
  def proxyAuthenticationRequired(
      self,
      requestUrl: QUrl,
      authenticator: Optional[QAuthenticator],
      proxyHost: str,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::proxyAuthenticationRequired(const QUrl
    &requestUrl, QAuthenticator *authenticator, const QString &proxyHost)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#proxyAuthenticationRequired

    Parameters
    ----------

    requestUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    proxyHost : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEnginePage::proxyAuthenticationRequired(const QUrl
    #      &requestUrl, QAuthenticator *authenticator, const QString
    #      &proxyHost)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage27proxyAuthenticationRequiredERK4QUrlP14Q'
        'AuthenticatorRK7QString',
        self._valueOf(requestUrl), self._addressOf(authenticator), proxyHost,
    )

  @overload(RenderProcessTerminationStatus, int)
  def renderProcessTerminated(
      self,
      terminationStatus: RenderProcessTerminationStatus,
      exitCode: int,
  ) -> None:
    """
    Calls Qt's 'void
    QWebEnginePage::renderProcessTerminated(RenderProcessTerminationStatus
    terminationStatus, int exitCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#renderProcessTerminated

    Parameters
    ----------

    terminationStatus : RenderProcessTerminationStatus
      Passed on as its number.

    exitCode : int
      Passed on as it is.
    """
    #  void QWebEnginePage::renderProcessTerminated(
    #      RenderProcessTerminationStatus terminationStatus, int exitCode)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage23renderProcessTerminatedENS_30RenderProc'
        'essTerminationStatusEi',
        terminationStatus.value, exitCode,
    )

  @overload(QWebEngineDesktopMediaRequest)
  def desktopMediaRequested(
      self,
      request: QWebEngineDesktopMediaRequest,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::desktopMediaRequested(const
    QWebEngineDesktopMediaRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#desktopMediaRequested

    Parameters
    ----------

    request : QWebEngineDesktopMediaRequest
      Passed on as a value: Qt reads the C++ QWebEngineDesktopMediaRequest,
      which stays Python's own.
    """
    #  void QWebEnginePage::desktopMediaRequested(const
    #      QWebEngineDesktopMediaRequest &request)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage21desktopMediaRequestedERK29QWebEngineDes'
        'ktopMediaRequest',
        self._valueOf(request),
    )

  @overload(QWebEngineCertificateError)
  def certificateError(
      self,
      certificateError: QWebEngineCertificateError,
  ) -> None:
    """
    Calls Qt's 'void QWebEnginePage::certificateError(const
    QWebEngineCertificateError &certificateError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#certificateError

    Parameters
    ----------

    certificateError : QWebEngineCertificateError
      Passed on as a value: Qt reads the C++ QWebEngineCertificateError,
      which stays Python's own.
    """
    #  void QWebEnginePage::certificateError(const QWebEngineCertificateError
    #      &certificateError)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage16certificateErrorERK26QWebEngineCertific'
        'ateError',
        self._valueOf(certificateError),
    )

  @overload(str)
  def titleChanged(self, title: str) -> None:
    """
    Calls Qt's 'void QWebEnginePage::titleChanged(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#titleChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEnginePage::titleChanged(const QString &title)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage12titleChangedERK7QString', title,
    )

  @overload(QUrl)
  def urlChanged(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEnginePage::urlChanged(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#urlChanged

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEnginePage::urlChanged(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage10urlChangedERK4QUrl', self._valueOf(url),
    )

  @overload(QUrl)
  def iconUrlChanged(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEnginePage::iconUrlChanged(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#iconUrlChanged

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEnginePage::iconUrlChanged(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage14iconUrlChangedERK4QUrl',
        self._valueOf(url),
    )

  @overload(QIcon)
  def iconChanged(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QWebEnginePage::iconChanged(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#iconChanged

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QWebEnginePage::iconChanged(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage11iconChangedERK5QIcon',
        self._valueOf(icon),
    )

  @overload(float)
  def zoomFactorChanged(self, factor: float) -> None:
    """
    Calls Qt's 'void QWebEnginePage::zoomFactorChanged(qreal factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#zoomFactorChanged

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QWebEnginePage::zoomFactorChanged(qreal factor)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage17zoomFactorChangedEd', factor,
    )

  @overload(QPointF)
  def scrollPositionChanged(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QWebEnginePage::scrollPositionChanged(const QPointF
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#scrollPositionChanged

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWebEnginePage::scrollPositionChanged(const QPointF &position)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage21scrollPositionChangedERK7QPointF',
        self._valueOf(position, 'QPointF'),
    )

  @overload(QSizeF)
  def contentsSizeChanged(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QWebEnginePage::contentsSizeChanged(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#contentsSizeChanged

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QWebEnginePage::contentsSizeChanged(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage19contentsSizeChangedERK6QSizeF',
        self._valueOf(size),
    )

  @overload(bool)
  def audioMutedChanged(self, muted: bool) -> None:
    """
    Calls Qt's 'void QWebEnginePage::audioMutedChanged(bool muted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#audioMutedChanged

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QWebEnginePage::audioMutedChanged(bool muted)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage17audioMutedChangedEb', muted,
    )

  @overload(bool)
  def recentlyAudibleChanged(self, recentlyAudible: bool) -> None:
    """
    Calls Qt's 'void QWebEnginePage::recentlyAudibleChanged(bool
    recentlyAudible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#recentlyAudibleChanged

    Parameters
    ----------

    recentlyAudible : bool
      Passed on as it is.
    """
    #  void QWebEnginePage::recentlyAudibleChanged(bool recentlyAudible)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage22recentlyAudibleChangedEb',
        recentlyAudible,
    )

  @overload(int)
  def renderProcessPidChanged(self, pid: int) -> None:
    """
    Calls Qt's 'void QWebEnginePage::renderProcessPidChanged(qint64 pid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#renderProcessPidChanged

    Parameters
    ----------

    pid : int
      Passed on as it is.
    """
    #  void QWebEnginePage::renderProcessPidChanged(qint64 pid)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage23renderProcessPidChangedEx', pid,
    )

  @overload(str, bool)
  def pdfPrintingFinished(self, filePath: str, success: bool) -> None:
    """
    Calls Qt's 'void QWebEnginePage::pdfPrintingFinished(const QString
    &filePath, bool success)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#pdfPrintingFinished

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    success : bool
      Passed on as it is.
    """
    #  void QWebEnginePage::pdfPrintingFinished(const QString &filePath, bool
    #      success)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage19pdfPrintingFinishedERK7QStringb',
        filePath, success,
    )

  def printRequested(self) -> None:
    """
    Calls Qt's 'void QWebEnginePage::printRequested()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#printRequested
    """
    #  void QWebEnginePage::printRequested()
    self.uglySide.call('ritual_ZN14QWebEnginePage14printRequestedEv')

  @overload(QWebEngineFrame)
  def printRequestedByFrame(self, frame: QWebEngineFrame) -> None:
    """
    Calls Qt's 'void QWebEnginePage::printRequestedByFrame(QWebEngineFrame
    frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#printRequestedByFrame

    Parameters
    ----------

    frame : QWebEngineFrame
      Passed on as a value: Qt reads the C++ QWebEngineFrame, which stays
      Python's own.
    """
    #  void QWebEnginePage::printRequestedByFrame(QWebEngineFrame frame)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage21printRequestedByFrameE15QWebEngineFrame',
        self._valueOf(frame),
    )

  @overload(bool)
  def visibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QWebEnginePage::visibleChanged(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#visibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QWebEnginePage::visibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage14visibleChangedEb', visible,
    )

  @overload(LifecycleState)
  def lifecycleStateChanged(self, state: LifecycleState) -> None:
    """
    Calls Qt's 'void QWebEnginePage::lifecycleStateChanged(LifecycleState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#lifecycleStateChanged

    Parameters
    ----------

    state : LifecycleState
      Passed on as its number.
    """
    #  void QWebEnginePage::lifecycleStateChanged(LifecycleState state)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage21lifecycleStateChangedENS_14LifecycleSta'
        'teE',
        state.value,
    )

  @overload(LifecycleState)
  def recommendedStateChanged(self, state: LifecycleState) -> None:
    """
    Calls Qt's 'void QWebEnginePage::recommendedStateChanged(LifecycleState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#recommendedStateChanged

    Parameters
    ----------

    state : LifecycleState
      Passed on as its number.
    """
    #  void QWebEnginePage::recommendedStateChanged(LifecycleState state)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage23recommendedStateChangedENS_14LifecycleS'
        'tateE',
        state.value,
    )

  @overload(QWebEngineFindTextResult)
  def findTextFinished(self, result: QWebEngineFindTextResult) -> None:
    """
    Calls Qt's 'void QWebEnginePage::findTextFinished(const
    QWebEngineFindTextResult &result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#findTextFinished

    Parameters
    ----------

    result : QWebEngineFindTextResult
      Passed on as a value: Qt reads the C++ QWebEngineFindTextResult, which
      stays Python's own.
    """
    #  void QWebEnginePage::findTextFinished(const QWebEngineFindTextResult
    #      &result)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage16findTextFinishedERK24QWebEngineFindText'
        'Result',
        self._valueOf(result),
    )

  def _q_aboutToDelete(self) -> None:
    """
    Calls Qt's 'void QWebEnginePage::_q_aboutToDelete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#_q_aboutToDelete
    """
    #  void QWebEnginePage::_q_aboutToDelete()
    self.uglySide.call('ritual_ZN14QWebEnginePage16_q_aboutToDeleteEv')

  @overload(QWebEngineWebAuthUxRequest)
  @overload(NoneType)
  def webAuthUxRequested(
      self,
      request: Optional[QWebEngineWebAuthUxRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QWebEnginePage::webAuthUxRequested(QWebEngineWebAuthUxRequest *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#webAuthUxRequested

    Parameters
    ----------

    request : Optional[QWebEngineWebAuthUxRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEnginePage::webAuthUxRequested(QWebEngineWebAuthUxRequest
    #      *request)
    self.uglySide.call(
        'ritual_ZN14QWebEnginePage18webAuthUxRequestedEP26QWebEngineWebAuth'
        'UxRequest',
        self._addressOf(request),
    )

  @overload(WebWindowType)
  def createWindow(self, type: WebWindowType) -> Optional[QWebEnginePage]:
    """
    Calls Qt's 'QWebEnginePage *QWebEnginePage::createWindow(WebWindowType
    type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#createWindow

    Parameters
    ----------

    type : WebWindowType
      Passed on as its number.

    Returns
    -------

    Optional[QWebEnginePage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEnginePage *QWebEnginePage::createWindow(WebWindowType type)
    ritual = 'ritual_ZN14QWebEnginePage12createWindowENS_13WebWindowTypeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEnginePage12createWindowENS_13WebWindowTypeE')
    address = self.uglySide.call(ritual, type.value)
    return QWebEnginePage._cuteAt(address)

  @overload(FileSelectionMode, QStringList, QStringList)
  def chooseFiles(
      self,
      mode: FileSelectionMode,
      oldFiles: QStringList,
      acceptedMimeTypes: QStringList,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QWebEnginePage::chooseFiles(FileSelectionMode
    mode, const QStringList &oldFiles, const QStringList
    &acceptedMimeTypes)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepage.html#chooseFiles

    Parameters
    ----------

    mode : FileSelectionMode
      Passed on as its number.

    oldFiles : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    acceptedMimeTypes : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebEnginePage::chooseFiles(FileSelectionMode mode, const
    #      QStringList &oldFiles, const QStringList &acceptedMimeTypes)
    address = self.uglySide.call(
        'ritual_ZN14QWebEnginePage11chooseFilesENS_17FileSelectionModeERK5Q'
        'ListI7QStringES5_',
        mode.value, self._valueOf(oldFiles),
        self._valueOf(acceptedMimeTypes),
    )
    return QStringList._cuteOwning(address)

  @overload(QUrl, str)
  def javaScriptAlert(self, securityOrigin: QUrl, msg: str) -> None:
    """
    Calls Qt's 'void QWebEnginePage::javaScriptAlert(const QUrl
    &securityOrigin, const QString &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#javaScriptAlert

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEnginePage::javaScriptAlert(const QUrl &securityOrigin, const
    #      QString &msg)
    ritual = 'ritual_ZN14QWebEnginePage15javaScriptAlertERK4QUrlRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEnginePage15javaScriptAlertERK4QUrlRK7QString')
    self.uglySide.call(ritual, self._valueOf(securityOrigin), msg)

  @overload(QUrl, str)
  def javaScriptConfirm(self, securityOrigin: QUrl, msg: str) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::javaScriptConfirm(const QUrl
    &securityOrigin, const QString &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#javaScriptConfirm

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QWebEnginePage::javaScriptConfirm(const QUrl &securityOrigin,
    #      const QString &msg)
    ritual = 'ritual_ZN14QWebEnginePage17javaScriptConfirmERK4QUrlRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEnginePage17javaScriptConfirmERK4QUrlRK7QStri'
          'ng')
    return self.uglySide.call(ritual, self._valueOf(securityOrigin), msg)

  @overload(QUrl, str, str, QString)
  @overload(QUrl, str, str, NoneType)
  def javaScriptPrompt(
      self,
      securityOrigin: QUrl,
      msg: str,
      defaultValue: str,
      result: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::javaScriptPrompt(const QUrl
    &securityOrigin, const QString &msg, const QString &defaultValue, QString
    *result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#javaScriptPrompt

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : str
      Passed on as it is: a QString is made of it for the call.

    result : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWebEnginePage::javaScriptPrompt(const QUrl &securityOrigin,
    #      const QString &msg, const QString &defaultValue, QString *result)
    ritual = (
        'ritual_ZN14QWebEnginePage16javaScriptPromptERK4QUrlRK7QStringS5_PS'
        '3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEnginePage16javaScriptPromptERK4QUrlRK7QStrin'
          'gS5_PS3_')
    return self.uglySide.call(
        ritual,
        self._valueOf(securityOrigin), msg, defaultValue,
        self._addressOf(result),
    )

  @overload(JavaScriptConsoleMessageLevel, str, int, str)
  def javaScriptConsoleMessage(
      self,
      level: JavaScriptConsoleMessageLevel,
      message: str,
      lineNumber: int,
      sourceID: str,
  ) -> None:
    """
    Calls Qt's 'void
    QWebEnginePage::javaScriptConsoleMessage(JavaScriptConsoleMessageLevel
    level, const QString &message, int lineNumber, const QString &sourceID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#javaScriptConsoleMessage

    Parameters
    ----------

    level : JavaScriptConsoleMessageLevel
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.

    lineNumber : int
      Passed on as it is.

    sourceID : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEnginePage::javaScriptConsoleMessage(
    #      JavaScriptConsoleMessageLevel level, const QString &message, int
    #      lineNumber, const QString &sourceID)
    ritual = (
        'ritual_ZN14QWebEnginePage24javaScriptConsoleMessageENS_29JavaScrip'
        'tConsoleMessageLevelERK7QStringiS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEnginePage24javaScriptConsoleMessageENS_29Jav'
          'aScriptConsoleMessageLevelERK7QStringiS3_')
    self.uglySide.call(ritual, level.value, message, lineNumber, sourceID)

  @overload(QUrl, NavigationType, bool)
  def acceptNavigationRequest(
      self,
      url: QUrl,
      type: NavigationType,
      isMainFrame: bool,
  ) -> bool:
    """
    Calls Qt's 'bool QWebEnginePage::acceptNavigationRequest(const QUrl &url,
    NavigationType type, bool isMainFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepage.html#acceptNavigationRequest

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : NavigationType
      Passed on as its number.

    isMainFrame : bool
      Passed on as it is.
    """
    #  bool QWebEnginePage::acceptNavigationRequest(const QUrl &url,
    #      NavigationType type, bool isMainFrame)
    ritual = (
        'ritual_ZN14QWebEnginePage23acceptNavigationRequestERK4QUrlNS_14Nav'
        'igationTypeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEnginePage23acceptNavigationRequestERK4QUrlNS'
          '_14NavigationTypeEb')
    return self.uglySide.call(
        ritual, self._valueOf(url), type.value, isMainFrame,
    )

  @staticmethod
  def acceptAsNewWindow(*__, **_) -> Never:
    """
    Qt's 'void QWebEnginePage::acceptAsNewWindow(QWebEngineNewWindowRequest
    &request)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.acceptAsNewWindow' has no cute function yet. Qt's "
        "'void QWebEnginePage::acceptAsNewWindow(QWebEngineNewWindowRequest "
        "&request)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def findFrameByName(*__, **_) -> Never:
    """
    Qt's 'std::optional<QWebEngineFrame>
    QWebEnginePage::findFrameByName(QAnyStringView name)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.findFrameByName' has no cute function yet. Qt's "
        "'std::optional<QWebEngineFrame> "
        "QWebEnginePage::findFrameByName(QAnyStringView name)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def findText(*__, **_) -> Never:
    """
    Qt's 'void QWebEnginePage::findText(const QString &subString, FindFlags
    options, const std::function<void (const QWebEngineFindTextResult &)>
    &resultCallback)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.findText' has no cute function yet. Qt's 'void "
        "QWebEnginePage::findText(const QString &subString, FindFlags "
        "options, const std::function<void (const QWebEngineFindTextResult "
        "&)> &resultCallback)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def navigationRequested(*__, **_) -> Never:
    """
    Qt's 'void
    QWebEnginePage::navigationRequested(QWebEngineNavigationRequest
    &request)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.navigationRequested' has no cute function yet. "
        "Qt's 'void "
        "QWebEnginePage::navigationRequested(QWebEngineNavigationRequest "
        "&request)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def newWindowRequested(*__, **_) -> Never:
    """
    Qt's 'void QWebEnginePage::newWindowRequested(QWebEngineNewWindowRequest
    &request)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.newWindowRequested' has no cute function yet. Qt's "
        "'void "
        "QWebEnginePage::newWindowRequested(QWebEngineNewWindowRequest "
        "&request)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def runJavaScriptImpl(*__, **_) -> Never:
    """
    Qt's 'void QWebEnginePage::runJavaScriptImpl(const QString &scriptSource,
    quint32 worldId, QtPrivate::QSlotObjectBase *callback)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.runJavaScriptImpl' has no cute function yet. Qt's "
        "'void QWebEnginePage::runJavaScriptImpl(const QString "
        "&scriptSource, quint32 worldId, QtPrivate::QSlotObjectBase "
        "*callback)': names 'QtPrivate::QSlotObjectBase', which has no cute "
        "class yet.")

  @staticmethod
  def scripts(*__, **_) -> Never:
    """
    Qt's 'QWebEngineScriptCollection &QWebEnginePage::scripts()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.scripts' has no cute function yet. Qt's "
        "'QWebEngineScriptCollection &QWebEnginePage::scripts()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def toHtml(*__, **_) -> Never:
    """
    Qt's 'void QWebEnginePage::toHtml(const std::function<void (const QString
    &)> &resultCallback) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.toHtml' has no cute function yet. Qt's 'void "
        "QWebEnginePage::toHtml(const std::function<void (const QString &)> "
        "&resultCallback) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def toPlainText(*__, **_) -> Never:
    """
    Qt's 'void QWebEnginePage::toPlainText(const std::function<void (const
    QString &)> &resultCallback) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QWebEnginePage.toPlainText' has no cute function yet. Qt's 'void "
        "QWebEnginePage::toPlainText(const std::function<void (const "
        "QString &)> &resultCallback) const': takes a type Python has no "
        "way to hand over yet.")
