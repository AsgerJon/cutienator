"""
QQuickWebEngineView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineview_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineView to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from ..QtWebEngineCore import QWebEngineDownloadRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRect, QRectF, QSizeF, QUrl
  from ..QtGui import QColor, QDragEnterEvent, QDragLeaveEvent
  from ..QtGui import QDragMoveEvent, QDropEvent
  from ..QtQml import QJSValue, QQmlComponent
  from ..QtWebEngineCore import QWebEngineCertificateError
  from ..QtWebEngineCore import QWebEngineContextMenuRequest
  from ..QtWebEngineCore import QWebEngineDesktopMediaRequest
  from ..QtWebEngineCore import QWebEngineFileSystemAccessRequest
  from ..QtWebEngineCore import QWebEngineFindTextResult
  from ..QtWebEngineCore import QWebEngineFullScreenRequest
  from ..QtWebEngineCore import QWebEngineHistory, QWebEngineLoadingInfo
  from ..QtWebEngineCore import QWebEngineNavigationRequest
  from ..QtWebEngineCore import QWebEngineNewWindowRequest
  from ..QtWebEngineCore import QWebEnginePermission, QWebEngineQuotaRequest
  from ..QtWebEngineCore import QWebEngineRegisterProtocolHandlerRequest
  from ..QtWebEngineCore import QWebEngineWebAuthUxRequest
  from . import QQuickWebEngineAction
  from . import QQuickWebEngineAuthenticationDialogRequest
  from . import QQuickWebEngineClientCertificateSelection
  from . import QQuickWebEngineColorDialogRequest
  from . import QQuickWebEngineFileDialogRequest, QQuickWebEngineFrame
  from . import QQuickWebEngineJavaScriptDialogRequest
  from . import QQuickWebEngineNewWindowRequest, QQuickWebEngineProfile
  from . import QQuickWebEngineScriptCollection, QQuickWebEngineSettings
  from . import QQuickWebEngineTooltipRequest
  from . import QQuickWebEngineTouchSelectionMenuRequest
  from ..QtWebChannelQuick import QQmlWebChannel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QJSValue = WAIT['QJSValue']
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']
  QQmlWebChannel = WAIT['QQmlWebChannel']
  QQuickWebEngineAuthenticationDialogRequest = WAIT['QQuickWebEngineAuthenticationDialogRequest']
  QQuickWebEngineClientCertificateSelection = WAIT['QQuickWebEngineClientCertificateSelection']
  QQuickWebEngineColorDialogRequest = WAIT['QQuickWebEngineColorDialogRequest']
  QQuickWebEngineFileDialogRequest = WAIT['QQuickWebEngineFileDialogRequest']
  QQuickWebEngineFrame = WAIT['QQuickWebEngineFrame']
  QQuickWebEngineJavaScriptDialogRequest = WAIT['QQuickWebEngineJavaScriptDialogRequest']
  QQuickWebEngineNewWindowRequest = WAIT['QQuickWebEngineNewWindowRequest']
  QQuickWebEngineProfile = WAIT['QQuickWebEngineProfile']
  QQuickWebEngineTooltipRequest = WAIT['QQuickWebEngineTooltipRequest']
  QQuickWebEngineTouchSelectionMenuRequest = WAIT['QQuickWebEngineTouchSelectionMenuRequest']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QUrl = WAIT['QUrl']
  QWebEngineCertificateError = WAIT['QWebEngineCertificateError']
  QWebEngineContextMenuRequest = WAIT['QWebEngineContextMenuRequest']
  QWebEngineDesktopMediaRequest = WAIT['QWebEngineDesktopMediaRequest']
  QWebEngineFileSystemAccessRequest = WAIT['QWebEngineFileSystemAccessRequest']
  QWebEngineFindTextResult = WAIT['QWebEngineFindTextResult']
  QWebEngineFullScreenRequest = WAIT['QWebEngineFullScreenRequest']
  QWebEngineLoadingInfo = WAIT['QWebEngineLoadingInfo']
  QWebEngineNavigationRequest = WAIT['QWebEngineNavigationRequest']
  QWebEngineNewWindowRequest = WAIT['QWebEngineNewWindowRequest']
  QWebEnginePermission = WAIT['QWebEnginePermission']
  QWebEngineQuotaRequest = WAIT['QWebEngineQuotaRequest']
  QWebEngineRegisterProtocolHandlerRequest = WAIT['QWebEngineRegisterProtocolHandlerRequest']
  QWebEngineWebAuthUxRequest = WAIT['QWebEngineWebAuthUxRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineView(QQuickItem):
  """
  The cute side of Qt's QQuickWebEngineView: a plain Python object standing
  in front of one C++ QQuickWebEngineView.

  It is built on the cute 'QQuickItem', as Qt's QQuickWebEngineView is built
  on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineView that has a ritual and that
  Python can call so far, 121 names in all: 'metaObject', 'tr', 'url',
  'setUrl', 'icon', 'isLoading', 'loadProgress', 'title', 'canGoBack',
  'canGoForward', 'isFullScreen', 'zoomFactor', 'setZoomFactor',
  'backgroundColor', 'setBackgroundColor', 'contentsSize', 'scrollPosition',
  'componentComplete', 'profile', 'setProfile', 'userScripts', 'settings',
  'webChannel', 'setWebChannel', 'history', 'webChannelWorld',
  'setWebChannelWorld', 'action', 'acceptAsNewWindow', 'isAudioMuted',
  'setAudioMuted', 'recentlyAudible', 'renderProcessPid',
  'activeFocusOnPress', 'setInspectedView', 'inspectedView',
  'setDevToolsView', 'devToolsView', 'devToolsId', 'lifecycleState',
  'setLifecycleState', 'recommendedState', 'touchHandleDelegate',
  'setTouchHandleDelegate', 'mainFrame', 'findFrameByName', 'runJavaScript',
  'loadHtml', 'goBack', 'goForward', 'goBackOrForward', 'reload',
  'reloadAndBypassCache', 'stop', 'findText', 'fullScreenCancelled',
  'grantFeaturePermission', 'setActiveFocusOnPress', 'triggerWebAction',
  'printToPdf', 'replaceMisspelledWord', 'save', 'lazyInitialize',
  'titleChanged', 'urlChanged', 'iconChanged', 'loadingChanged',
  'loadProgressChanged', 'linkHovered', 'navigationRequested',
  'javaScriptConsoleMessage', 'certificateError', 'fullScreenRequested',
  'isFullScreenChanged', 'featurePermissionRequested', 'zoomFactorChanged',
  'profileChanged', 'webChannelChanged', 'activeFocusOnPressChanged',
  'backgroundColorChanged', 'renderProcessTerminated',
  'windowCloseRequested', 'contentsSizeChanged', 'scrollPositionChanged',
  'audioMutedChanged', 'recentlyAudibleChanged', 'webChannelWorldChanged',
  'contextMenuRequested', 'authenticationDialogRequested',
  'javaScriptDialogRequested', 'colorDialogRequested', 'fileDialogRequested',
  'pdfPrintingFinished', 'quotaRequested', 'geometryChangeRequested',
  'inspectedViewChanged', 'devToolsViewChanged',
  'registerProtocolHandlerRequested', 'printRequested',
  'selectClientCertificate', 'tooltipRequested', 'lifecycleStateChanged',
  'recommendedStateChanged', 'findTextFinished', 'renderProcessPidChanged',
  'canGoBackChanged', 'canGoForwardChanged', 'newWindowRequested',
  'touchSelectionMenuRequested', 'touchHandleDelegateChanged',
  'fileSystemAccessRequested', 'webAuthUxRequested', 'desktopMediaRequested',
  'printRequestedByFrame', 'permissionRequested', 'geometryChange',
  'itemChange', 'dragEnterEvent', 'dragLeaveEvent', 'dragMoveEvent',
  'dropEvent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineView::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWebEngineView::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWebEngineView::~QQuickWebEngineView()': the destructor:
    Python never removes a C++ QQuickWebEngineView.
  - Qt's 'void QQuickWebEngineView::runJavaScript(const QString &script,
    const std::function<void (const QVariant &)> &resultCallback)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQuickWebEngineViewPrivate *QQuickWebEngineView::d_func()': gives
    'QQuickWebEngineViewPrivate', which has no cute class yet.
  - Qt's 'const QQuickWebEngineViewPrivate *QQuickWebEngineView::d_func()
    const': gives 'QQuickWebEngineViewPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 132 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineView is created at the first use, not by
    'QQuickWebEngineView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineView.
  - Qt tells when it has removed the C++ QQuickWebEngineView. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWebEngineView, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ErrorDomain(CuteNum):
    """
    The enum 'QQuickWebEngineView::ErrorDomain' of Qt, with the 7 names Qt
    gives in it.
    """

    NoErrorDomain = Kee[int](0)
    InternalErrorDomain = Kee[int](1)
    ConnectionErrorDomain = Kee[int](2)
    CertificateErrorDomain = Kee[int](3)
    HttpErrorDomain = Kee[int](4)
    FtpErrorDomain = Kee[int](5)
    DnsErrorDomain = Kee[int](6)

  class Feature(CuteNum):
    """
    The enum 'QQuickWebEngineView::Feature' of Qt, with the 9 names Qt gives
    in it.
    """

    MediaAudioCapture = Kee[int](0)
    MediaVideoCapture = Kee[int](1)
    MediaAudioVideoCapture = Kee[int](2)
    Geolocation = Kee[int](3)
    DesktopVideoCapture = Kee[int](4)
    DesktopAudioVideoCapture = Kee[int](5)
    Notifications = Kee[int](6)
    ClipboardReadWrite = Kee[int](7)
    LocalFontsAccess = Kee[int](8)

  class FindFlag(CuteFlags):
    """
    The flags enum 'QQuickWebEngineView::FindFlag' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QQuickWebEngineView::FindFlags'.
    """

    FindBackward = 0x1
    FindCaseSensitively = 0x2

  FindFlags = FindFlag

  class JavaScriptConsoleMessageLevel(CuteNum):
    """
    The enum 'QQuickWebEngineView::JavaScriptConsoleMessageLevel' of Qt, with
    the 3 names Qt gives in it.
    """

    InfoMessageLevel = Kee[int](0)
    WarningMessageLevel = Kee[int](1)
    ErrorMessageLevel = Kee[int](2)

  class LifecycleState(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineView::LifecycleState' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Active = Kee[int](0)
    Frozen = Kee[int](1)
    Discarded = Kee[int](2)

  class LoadStatus(CuteNum):
    """
    The enum 'QQuickWebEngineView::LoadStatus' of Qt, with the 4 names Qt
    gives in it.
    """

    LoadStartedStatus = Kee[int](0)
    LoadStoppedStatus = Kee[int](1)
    LoadSucceededStatus = Kee[int](2)
    LoadFailedStatus = Kee[int](3)

  class NavigationRequestAction(CuteNum):
    """
    The enum 'QQuickWebEngineView::NavigationRequestAction' of Qt, with the 2
    names Qt gives in it.
    """

    AcceptRequest = Kee[int](0)
    IgnoreRequest = Kee[int](255)

  class NavigationType(CuteNum):
    """
    The enum 'QQuickWebEngineView::NavigationType' of Qt, with the 7 names Qt
    gives in it.
    """

    LinkClickedNavigation = Kee[int](0)
    TypedNavigation = Kee[int](1)
    FormSubmittedNavigation = Kee[int](2)
    BackForwardNavigation = Kee[int](3)
    ReloadNavigation = Kee[int](4)
    OtherNavigation = Kee[int](5)
    RedirectNavigation = Kee[int](6)

  class NewViewDestination(CuteNum):
    """
    The enum 'QQuickWebEngineView::NewViewDestination' of Qt, with the 4
    names Qt gives in it.
    """

    NewViewInWindow = Kee[int](0)
    NewViewInTab = Kee[int](1)
    NewViewInDialog = Kee[int](2)
    NewViewInBackgroundTab = Kee[int](3)

  class PrintedPageOrientation(CuteNum):
    """
    The enum 'QQuickWebEngineView::PrintedPageOrientation' of Qt, with the 2
    names Qt gives in it.
    """

    Portrait = Kee[int](0)
    Landscape = Kee[int](1)

  class PrintedPageSizeId(CuteNum):
    """
    The enum 'QQuickWebEngineView::PrintedPageSizeId' of Qt, with the 125
    names Qt gives in it.
    """

    Letter = Kee[int](0)
    Legal = Kee[int](1)
    Executive = Kee[int](2)
    A0 = Kee[int](3)
    A1 = Kee[int](4)
    A2 = Kee[int](5)
    A3 = Kee[int](6)
    A4 = Kee[int](7)
    A5 = Kee[int](8)
    A6 = Kee[int](9)
    A7 = Kee[int](10)
    A8 = Kee[int](11)
    A9 = Kee[int](12)
    A10 = Kee[int](13)
    B0 = Kee[int](14)
    B1 = Kee[int](15)
    B2 = Kee[int](16)
    B3 = Kee[int](17)
    B4 = Kee[int](18)
    B5 = Kee[int](19)
    B6 = Kee[int](20)
    B7 = Kee[int](21)
    B8 = Kee[int](22)
    B9 = Kee[int](23)
    B10 = Kee[int](24)
    C5E = Kee[int](25)
    Comm10E = Kee[int](26)
    DLE = Kee[int](27)
    Folio = Kee[int](28)
    Ledger = Kee[int](29)
    Tabloid = Kee[int](30)
    Custom = Kee[int](31)
    A3Extra = Kee[int](32)
    A4Extra = Kee[int](33)
    A4Plus = Kee[int](34)
    A4Small = Kee[int](35)
    A5Extra = Kee[int](36)
    B5Extra = Kee[int](37)
    JisB0 = Kee[int](38)
    JisB1 = Kee[int](39)
    JisB2 = Kee[int](40)
    JisB3 = Kee[int](41)
    JisB4 = Kee[int](42)
    JisB5 = Kee[int](43)
    JisB6 = Kee[int](44)
    JisB7 = Kee[int](45)
    JisB8 = Kee[int](46)
    JisB9 = Kee[int](47)
    JisB10 = Kee[int](48)
    AnsiC = Kee[int](49)
    AnsiD = Kee[int](50)
    AnsiE = Kee[int](51)
    LegalExtra = Kee[int](52)
    LetterExtra = Kee[int](53)
    LetterPlus = Kee[int](54)
    LetterSmall = Kee[int](55)
    TabloidExtra = Kee[int](56)
    ArchA = Kee[int](57)
    ArchB = Kee[int](58)
    ArchC = Kee[int](59)
    ArchD = Kee[int](60)
    ArchE = Kee[int](61)
    Imperial7x9 = Kee[int](62)
    Imperial8x10 = Kee[int](63)
    Imperial9x11 = Kee[int](64)
    Imperial9x12 = Kee[int](65)
    Imperial10x11 = Kee[int](66)
    Imperial10x13 = Kee[int](67)
    Imperial10x14 = Kee[int](68)
    Imperial12x11 = Kee[int](69)
    Imperial15x11 = Kee[int](70)
    ExecutiveStandard = Kee[int](71)
    Note = Kee[int](72)
    Quarto = Kee[int](73)
    Statement = Kee[int](74)
    SuperA = Kee[int](75)
    SuperB = Kee[int](76)
    Postcard = Kee[int](77)
    DoublePostcard = Kee[int](78)
    Prc16K = Kee[int](79)
    Prc32K = Kee[int](80)
    Prc32KBig = Kee[int](81)
    FanFoldUS = Kee[int](82)
    FanFoldGerman = Kee[int](83)
    FanFoldGermanLegal = Kee[int](84)
    EnvelopeB4 = Kee[int](85)
    EnvelopeB5 = Kee[int](86)
    EnvelopeB6 = Kee[int](87)
    EnvelopeC0 = Kee[int](88)
    EnvelopeC1 = Kee[int](89)
    EnvelopeC2 = Kee[int](90)
    EnvelopeC3 = Kee[int](91)
    EnvelopeC4 = Kee[int](92)
    EnvelopeC6 = Kee[int](93)
    EnvelopeC65 = Kee[int](94)
    EnvelopeC7 = Kee[int](95)
    Envelope9 = Kee[int](96)
    Envelope11 = Kee[int](97)
    Envelope12 = Kee[int](98)
    Envelope14 = Kee[int](99)
    EnvelopeMonarch = Kee[int](100)
    EnvelopePersonal = Kee[int](101)
    EnvelopeChou3 = Kee[int](102)
    EnvelopeChou4 = Kee[int](103)
    EnvelopeInvite = Kee[int](104)
    EnvelopeItalian = Kee[int](105)
    EnvelopeKaku2 = Kee[int](106)
    EnvelopeKaku3 = Kee[int](107)
    EnvelopePrc1 = Kee[int](108)
    EnvelopePrc2 = Kee[int](109)
    EnvelopePrc3 = Kee[int](110)
    EnvelopePrc4 = Kee[int](111)
    EnvelopePrc5 = Kee[int](112)
    EnvelopePrc6 = Kee[int](113)
    EnvelopePrc7 = Kee[int](114)
    EnvelopePrc8 = Kee[int](115)
    EnvelopePrc9 = Kee[int](116)
    EnvelopePrc10 = Kee[int](117)
    EnvelopeYou4 = Kee[int](118)
    LastPageSize = Kee[int](118)
    AnsiA = Kee[int](0)
    AnsiB = Kee[int](29)
    EnvelopeC5 = Kee[int](25)
    EnvelopeDL = Kee[int](27)
    Envelope10 = Kee[int](26)

  class RenderProcessTerminationStatus(CuteNum):
    """
    The enum 'QQuickWebEngineView::RenderProcessTerminationStatus' of Qt,
    with the 4 names Qt gives in it.
    """

    NormalTerminationStatus = Kee[int](0)
    AbnormalTerminationStatus = Kee[int](1)
    CrashedTerminationStatus = Kee[int](2)
    KilledTerminationStatus = Kee[int](3)

  class WebAction(CuteNum):
    """
    The enum 'QQuickWebEngineView::WebAction' of Qt, with the 49 names Qt
    gives in it.
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
    Calls Qt's 'QString QQuickWebEngineView::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#tr

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
    #  QString QQuickWebEngineView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickWebEngineView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineView'

  #  A C++ QQuickWebEngineView Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebEngineView::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebEngineView::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineView::url() const
    address = self.uglySide.call('ritual_ZNK19QQuickWebEngineView3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def icon(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebEngineView::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#icon

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineView::icon() const
    address = self.uglySide.call('ritual_ZNK19QQuickWebEngineView4iconEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineView::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#isLoading
    """
    #  bool QQuickWebEngineView::isLoading() const
    return self.uglySide.call('ritual_ZNK19QQuickWebEngineView9isLoadingEv')

  def loadProgress(self) -> int:
    """
    Calls Qt's 'int QQuickWebEngineView::loadProgress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#loadProgress
    """
    #  int QQuickWebEngineView::loadProgress() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView12loadProgressEv',
    )

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineView::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineView::title() const
    return self.uglySide.call('ritual_ZNK19QQuickWebEngineView5titleEv')

  def canGoBack(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineView::canGoBack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#canGoBack
    """
    #  bool QQuickWebEngineView::canGoBack() const
    return self.uglySide.call('ritual_ZNK19QQuickWebEngineView9canGoBackEv')

  def canGoForward(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineView::canGoForward() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#canGoForward
    """
    #  bool QQuickWebEngineView::canGoForward() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView12canGoForwardEv',
    )

  def isFullScreen(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineView::isFullScreen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#isFullScreen
    """
    #  bool QQuickWebEngineView::isFullScreen() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView12isFullScreenEv',
    )

  def zoomFactor(self) -> float:
    """
    Calls Qt's 'qreal QQuickWebEngineView::zoomFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#zoomFactor
    """
    #  qreal QQuickWebEngineView::zoomFactor() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView10zoomFactorEv',
    )

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickWebEngineView::backgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickWebEngineView::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def contentsSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickWebEngineView::contentsSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#contentsSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickWebEngineView::contentsSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView12contentsSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def scrollPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickWebEngineView::scrollPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#scrollPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickWebEngineView::scrollPosition() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView14scrollPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def history(self) -> Optional[QWebEngineHistory]:
    """
    Calls Qt's 'QWebEngineHistory *QQuickWebEngineView::history() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#history

    Returns
    -------

    Optional[QWebEngineHistory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistory *QQuickWebEngineView::history() const
    address = self.uglySide.call('ritual_ZNK19QQuickWebEngineView7historyEv')
    from ..QtWebEngineCore import QWebEngineHistory
    return QWebEngineHistory._cuteAt(address)

  def webChannelWorld(self) -> int:
    """
    Calls Qt's 'uint QQuickWebEngineView::webChannelWorld() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#webChannelWorld
    """
    #  uint QQuickWebEngineView::webChannelWorld() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView15webChannelWorldEv',
    )

  def isAudioMuted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineView::isAudioMuted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#isAudioMuted
    """
    #  bool QQuickWebEngineView::isAudioMuted() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView12isAudioMutedEv',
    )

  def recentlyAudible(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineView::recentlyAudible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#recentlyAudible
    """
    #  bool QQuickWebEngineView::recentlyAudible() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView15recentlyAudibleEv',
    )

  def renderProcessPid(self) -> int:
    """
    Calls Qt's 'qint64 QQuickWebEngineView::renderProcessPid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#renderProcessPid
    """
    #  qint64 QQuickWebEngineView::renderProcessPid() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView16renderProcessPidEv',
    )

  def activeFocusOnPress(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineView::activeFocusOnPress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#activeFocusOnPress
    """
    #  bool QQuickWebEngineView::activeFocusOnPress() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView18activeFocusOnPressEv',
    )

  def inspectedView(self) -> Optional[QQuickWebEngineView]:
    """
    Calls Qt's 'QQuickWebEngineView *QQuickWebEngineView::inspectedView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#inspectedView

    Returns
    -------

    Optional[QQuickWebEngineView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineView *QQuickWebEngineView::inspectedView() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView13inspectedViewEv',
    )
    return QQuickWebEngineView._cuteAt(address)

  def devToolsView(self) -> Optional[QQuickWebEngineView]:
    """
    Calls Qt's 'QQuickWebEngineView *QQuickWebEngineView::devToolsView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#devToolsView

    Returns
    -------

    Optional[QQuickWebEngineView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineView *QQuickWebEngineView::devToolsView() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView12devToolsViewEv',
    )
    return QQuickWebEngineView._cuteAt(address)

  def lifecycleState(self) -> LifecycleState:
    """
    Calls Qt's 'LifecycleState QQuickWebEngineView::lifecycleState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#lifecycleState

    Returns
    -------

    LifecycleState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LifecycleState(number)'
      gives.
    """
    #  LifecycleState QQuickWebEngineView::lifecycleState() const
    return QQuickWebEngineView.LifecycleState(self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView14lifecycleStateEv',
    ))

  def recommendedState(self) -> LifecycleState:
    """
    Calls Qt's 'LifecycleState QQuickWebEngineView::recommendedState()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#recommendedState

    Returns
    -------

    LifecycleState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LifecycleState(number)'
      gives.
    """
    #  LifecycleState QQuickWebEngineView::recommendedState() const
    return QQuickWebEngineView.LifecycleState(self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView16recommendedStateEv',
    ))

  def touchHandleDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickWebEngineView::touchHandleDelegate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#touchHandleDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickWebEngineView::touchHandleDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView19touchHandleDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setUrl(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#setUrl

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickWebEngineView::setUrl(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView6setUrlERK4QUrl', self._valueOf(a0),
    )

  @overload(float)
  def setZoomFactor(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setZoomFactor(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setZoomFactor

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWebEngineView::setZoomFactor(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView13setZoomFactorEd', arg,
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setBackgroundColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickWebEngineView::setBackgroundColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView18setBackgroundColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QQuickWebEngineProfile)
  @overload(NoneType)
  def setProfile(self, a0: Optional[QQuickWebEngineProfile]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setProfile(QQuickWebEngineProfile
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setProfile

    Parameters
    ----------

    a0 : Optional[QQuickWebEngineProfile]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::setProfile(QQuickWebEngineProfile *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView10setProfileEP22QQuickWebEngineProfi'
        'le',
        self._addressOf(a0),
    )

  @overload(QQmlWebChannel)
  @overload(NoneType)
  def setWebChannel(self, a0: Optional[QQmlWebChannel]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setWebChannel(QQmlWebChannel *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setWebChannel

    Parameters
    ----------

    a0 : Optional[QQmlWebChannel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::setWebChannel(QQmlWebChannel *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView13setWebChannelEP14QQmlWebChannel',
        self._addressOf(a0),
    )

  @overload(int)
  def setWebChannelWorld(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setWebChannelWorld(uint a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setWebChannelWorld

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickWebEngineView::setWebChannelWorld(uint a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView18setWebChannelWorldEj', a0,
    )

  @overload(bool)
  def setAudioMuted(self, muted: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setAudioMuted(bool muted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setAudioMuted

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineView::setAudioMuted(bool muted)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView13setAudioMutedEb', muted,
    )

  @overload(THIS)
  @overload(NoneType)
  def setInspectedView(self, a0: Optional[QQuickWebEngineView]) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::setInspectedView(QQuickWebEngineView *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setInspectedView

    Parameters
    ----------

    a0 : Optional[QQuickWebEngineView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::setInspectedView(QQuickWebEngineView *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView16setInspectedViewEPS_',
        self._addressOf(a0),
    )

  @overload(THIS)
  @overload(NoneType)
  def setDevToolsView(self, a0: Optional[QQuickWebEngineView]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setDevToolsView(QQuickWebEngineView
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setDevToolsView

    Parameters
    ----------

    a0 : Optional[QQuickWebEngineView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::setDevToolsView(QQuickWebEngineView *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView15setDevToolsViewEPS_',
        self._addressOf(a0),
    )

  @overload(LifecycleState)
  def setLifecycleState(self, state: LifecycleState) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setLifecycleState(LifecycleState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setLifecycleState

    Parameters
    ----------

    state : LifecycleState
      Passed on as its number.
    """
    #  void QQuickWebEngineView::setLifecycleState(LifecycleState state)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView17setLifecycleStateENS_14LifecycleSt'
        'ateE',
        state.value,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setTouchHandleDelegate(
      self,
      delegagte: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::setTouchHandleDelegate(QQmlComponent *delegagte)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setTouchHandleDelegate

    Parameters
    ----------

    delegagte : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::setTouchHandleDelegate(QQmlComponent
    #      *delegagte)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView22setTouchHandleDelegateEP13QQmlComp'
        'onent',
        self._addressOf(delegagte),
    )

  @overload(bool)
  def setActiveFocusOnPress(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::setActiveFocusOnPress(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#setActiveFocusOnPress

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineView::setActiveFocusOnPress(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView21setActiveFocusOnPressEb', arg,
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
    Notes what was given, for Qt's
    'QQuickWebEngineView::QQuickWebEngineView(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#QQuickWebEngineView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWebEngineView::QQuickWebEngineView(QQuickItem *parent)
    self._noteCreation(QQuickWebEngineView, lambda: Rituals.call(
        'ritual_ZN19QQuickWebEngineViewC1EP10QQuickItem',
        self._addressOf(parent),
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#componentComplete
    """
    #  void QQuickWebEngineView::componentComplete()
    ritual = 'ritual_ZN19QQuickWebEngineView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickWebEngineView17componentCompleteEv'
    self.uglySide.call(ritual)

  def profile(self) -> Optional[QQuickWebEngineProfile]:
    """
    Calls Qt's 'QQuickWebEngineProfile *QQuickWebEngineView::profile()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#profile

    Returns
    -------

    Optional[QQuickWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineProfile *QQuickWebEngineView::profile()
    address = self.uglySide.call('ritual_ZN19QQuickWebEngineView7profileEv')
    from . import QQuickWebEngineProfile
    return QQuickWebEngineProfile._cuteAt(address)

  def userScripts(self) -> Optional[QQuickWebEngineScriptCollection]:
    """
    Calls Qt's 'QQuickWebEngineScriptCollection
    *QQuickWebEngineView::userScripts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#userScripts

    Returns
    -------

    Optional[QQuickWebEngineScriptCollection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineScriptCollection *QQuickWebEngineView::userScripts()
    address = self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView11userScriptsEv',
    )
    from . import QQuickWebEngineScriptCollection
    return QQuickWebEngineScriptCollection._cuteAt(address)

  def settings(self) -> Optional[QQuickWebEngineSettings]:
    """
    Calls Qt's 'QQuickWebEngineSettings *QQuickWebEngineView::settings()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#settings

    Returns
    -------

    Optional[QQuickWebEngineSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineSettings *QQuickWebEngineView::settings()
    address = self.uglySide.call('ritual_ZN19QQuickWebEngineView8settingsEv')
    from . import QQuickWebEngineSettings
    return QQuickWebEngineSettings._cuteAt(address)

  def webChannel(self) -> Optional[QQmlWebChannel]:
    """
    Calls Qt's 'QQmlWebChannel *QQuickWebEngineView::webChannel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#webChannel

    Returns
    -------

    Optional[QQmlWebChannel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlWebChannel *QQuickWebEngineView::webChannel()
    address = self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView10webChannelEv',
    )
    from ..QtWebChannelQuick import QQmlWebChannel
    return QQmlWebChannel._cuteAt(address)

  @overload(WebAction)
  def action(self, action: WebAction) -> Optional[QQuickWebEngineAction]:
    """
    Calls Qt's 'QQuickWebEngineAction *QQuickWebEngineView::action(WebAction
    action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#action

    Parameters
    ----------

    action : WebAction
      Passed on as its number.

    Returns
    -------

    Optional[QQuickWebEngineAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineAction *QQuickWebEngineView::action(WebAction action)
    address = self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView6actionENS_9WebActionE', action.value,
    )
    from . import QQuickWebEngineAction
    return QQuickWebEngineAction._cuteAt(address)

  @overload(QWebEngineNewWindowRequest)
  @overload(NoneType)
  def acceptAsNewWindow(
      self,
      request: Optional[QWebEngineNewWindowRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::acceptAsNewWindow(QWebEngineNewWindowRequest
    *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#acceptAsNewWindow

    Parameters
    ----------

    request : Optional[QWebEngineNewWindowRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::acceptAsNewWindow(QWebEngineNewWindowRequest
    #      *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView17acceptAsNewWindowEP26QWebEngineNew'
        'WindowRequest',
        self._addressOf(request),
    )

  def devToolsId(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineView::devToolsId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#devToolsId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineView::devToolsId()
    return self.uglySide.call('ritual_ZN19QQuickWebEngineView10devToolsIdEv')

  def mainFrame(self) -> QQuickWebEngineFrame:
    """
    Calls Qt's 'QQuickWebEngineFrame QQuickWebEngineView::mainFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#mainFrame

    Returns
    -------

    QQuickWebEngineFrame
      A new cute QQuickWebEngineFrame around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickWebEngineFrame QQuickWebEngineView::mainFrame()
    address = self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView9mainFrameEv',
    )
    from . import QQuickWebEngineFrame
    return QQuickWebEngineFrame._cuteOwning(address)

  @overload(str)
  def findFrameByName(self, name: str) -> QQuickWebEngineFrame:
    """
    Calls Qt's 'QQuickWebEngineFrame
    QQuickWebEngineView::findFrameByName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#findFrameByName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQuickWebEngineFrame
      A new cute QQuickWebEngineFrame around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickWebEngineFrame QQuickWebEngineView::findFrameByName(const
    #      QString &name)
    address = self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView15findFrameByNameERK7QString', name,
    )
    from . import QQuickWebEngineFrame
    return QQuickWebEngineFrame._cuteOwning(address)

  @overload(str, QJSValue)
  def runJavaScript(self, a0: str, a1: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::runJavaScript(const QString &a0,
    const QJSValue &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#runJavaScript

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWebEngineView::runJavaScript(const QString &a0, const
    #      QJSValue &a1)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView13runJavaScriptERK7QStringRK8QJSValu'
        'e',
        a0, self._valueOf(a1),
    )

  @overload(str, int, QJSValue)
  def runJavaScript(self, a0: str, worldId: int, a2: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::runJavaScript(const QString &a0,
    quint32 worldId, const QJSValue &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#runJavaScript

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    worldId : int
      Passed on as it is.

    a2 : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWebEngineView::runJavaScript(const QString &a0, quint32
    #      worldId, const QJSValue &a2)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView13runJavaScriptERK7QStringjRK8QJSVal'
        'ue',
        a0, worldId, self._valueOf(a2),
    )

  @overload(str)
  @overload(str, QUrl)
  def loadHtml(self, html: str, baseUrl: Optional[QUrl] = None) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::loadHtml(const QString &html, const
    QUrl &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#loadHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    baseUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QQuickWebEngineView::loadHtml(const QString &html, const QUrl
    #      &baseUrl)
    if baseUrl is None:
      from ..QtCore import QUrl
      baseUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView8loadHtmlERK7QStringRK4QUrl',
        html, self._valueOf(baseUrl),
    )

  def goBack(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::goBack()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#goBack
    """
    #  void QQuickWebEngineView::goBack()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView6goBackEv')

  def goForward(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::goForward()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#goForward
    """
    #  void QQuickWebEngineView::goForward()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView9goForwardEv')

  @overload(int)
  def goBackOrForward(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::goBackOrForward(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#goBackOrForward

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickWebEngineView::goBackOrForward(int index)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView15goBackOrForwardEi', index,
    )

  def reload(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#reload
    """
    #  void QQuickWebEngineView::reload()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView6reloadEv')

  def reloadAndBypassCache(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::reloadAndBypassCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#reloadAndBypassCache
    """
    #  void QQuickWebEngineView::reloadAndBypassCache()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView20reloadAndBypassCacheEv',
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#stop
    """
    #  void QQuickWebEngineView::stop()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView4stopEv')

  @overload(str, FindFlags, QJSValue)
  def findText(
      self,
      subString: str,
      options: FindFlags,
      callback: QJSValue,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::findText(const QString &subString,
    FindFlags options, const QJSValue &callback)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#findText

    Parameters
    ----------

    subString : str
      Passed on as it is: a QString is made of it for the call.

    options : FindFlags
      Passed on as its number.

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWebEngineView::findText(const QString &subString, FindFlags
    #      options, const QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView8findTextERK7QString6QFlagsINS_8Find'
        'FlagEERK8QJSValue',
        subString, options.value, self._valueOf(callback),
    )

  def fullScreenCancelled(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::fullScreenCancelled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#fullScreenCancelled
    """
    #  void QQuickWebEngineView::fullScreenCancelled()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19fullScreenCancelledEv',
    )

  @overload(QUrl, Feature, bool)
  def grantFeaturePermission(
      self,
      securityOrigin: QUrl,
      a1: Feature,
      granted: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::grantFeaturePermission(const QUrl
    &securityOrigin, QQuickWebEngineView::Feature a1, bool granted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#grantFeaturePermission

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    a1 : Feature
      Passed on as its number.

    granted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineView::grantFeaturePermission(const QUrl
    #      &securityOrigin, QQuickWebEngineView::Feature a1, bool granted)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView22grantFeaturePermissionERK4QUrlNS_7'
        'FeatureEb',
        self._valueOf(securityOrigin), a1.value, granted,
    )

  @overload(WebAction)
  def triggerWebAction(self, action: WebAction) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::triggerWebAction(WebAction
    action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#triggerWebAction

    Parameters
    ----------

    action : WebAction
      Passed on as its number.
    """
    #  void QQuickWebEngineView::triggerWebAction(WebAction action)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView16triggerWebActionENS_9WebActionE',
        action.value,
    )

  @overload(str)
  @overload(str, PrintedPageSizeId)
  @overload(str, PrintedPageSizeId, PrintedPageOrientation)
  def printToPdf(
      self,
      filePath: str,
      pageSizeId: PrintedPageSizeId = PrintedPageSizeId.A4,
      orientation: PrintedPageOrientation = PrintedPageOrientation.Portrait,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::printToPdf(const QString &filePath,
    PrintedPageSizeId pageSizeId, PrintedPageOrientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#printToPdf

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    pageSizeId : PrintedPageSizeId
      Passed on as its number. May be left out, as in Qt: it is then
      PrintedPageSizeId.A4.

    orientation : PrintedPageOrientation
      Passed on as its number. May be left out, as in Qt: it is then
      PrintedPageOrientation.Portrait.
    """
    #  void QQuickWebEngineView::printToPdf(const QString &filePath,
    #      PrintedPageSizeId pageSizeId, PrintedPageOrientation orientation)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView10printToPdfERK7QStringNS_17PrintedP'
        'ageSizeIdENS_22PrintedPageOrientationE',
        filePath, pageSizeId.value, orientation.value,
    )

  @overload(QJSValue)
  @overload(QJSValue, PrintedPageSizeId)
  @overload(QJSValue, PrintedPageSizeId, PrintedPageOrientation)
  def printToPdf(
      self,
      callback: QJSValue,
      pageSizeId: PrintedPageSizeId = PrintedPageSizeId.A4,
      orientation: PrintedPageOrientation = PrintedPageOrientation.Portrait,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::printToPdf(const QJSValue
    &callback, PrintedPageSizeId pageSizeId, PrintedPageOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#printToPdf

    Parameters
    ----------

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    pageSizeId : PrintedPageSizeId
      Passed on as its number. May be left out, as in Qt: it is then
      PrintedPageSizeId.A4.

    orientation : PrintedPageOrientation
      Passed on as its number. May be left out, as in Qt: it is then
      PrintedPageOrientation.Portrait.
    """
    #  void QQuickWebEngineView::printToPdf(const QJSValue &callback,
    #      PrintedPageSizeId pageSizeId, PrintedPageOrientation orientation)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView10printToPdfERK8QJSValueNS_17Printed'
        'PageSizeIdENS_22PrintedPageOrientationE',
        self._valueOf(callback), pageSizeId.value, orientation.value,
    )

  @overload(str)
  def replaceMisspelledWord(self, replacement: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::replaceMisspelledWord(const QString
    &replacement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#replaceMisspelledWord

    Parameters
    ----------

    replacement : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineView::replaceMisspelledWord(const QString
    #      &replacement)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView21replaceMisspelledWordERK7QString',
        replacement,
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
    Calls Qt's 'void QQuickWebEngineView::save(const QString &filePath,
    QWebEngineDownloadRequest::SavePageFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#save

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    format : QWebEngineDownloadRequest.SavePageFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QWebEngineDownloadRequest.SavePageFormat.MimeHtmlSaveFormat.
    """
    #  void QQuickWebEngineView::save(const QString &filePath,
    #      QWebEngineDownloadRequest::SavePageFormat format) const
    self.uglySide.call(
        'ritual_ZNK19QQuickWebEngineView4saveERK7QStringN25QWebEngineDownlo'
        'adRequest14SavePageFormatE',
        filePath, format.value,
    )

  def lazyInitialize(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::lazyInitialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#lazyInitialize
    """
    #  void QQuickWebEngineView::lazyInitialize()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView14lazyInitializeEv')

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::titleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#titleChanged
    """
    #  void QQuickWebEngineView::titleChanged()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView12titleChangedEv')

  def urlChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::urlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#urlChanged
    """
    #  void QQuickWebEngineView::urlChanged()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView10urlChangedEv')

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::iconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#iconChanged
    """
    #  void QQuickWebEngineView::iconChanged()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView11iconChangedEv')

  @overload(QWebEngineLoadingInfo)
  def loadingChanged(self, loadingInfo: QWebEngineLoadingInfo) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::loadingChanged(const
    QWebEngineLoadingInfo &loadingInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#loadingChanged

    Parameters
    ----------

    loadingInfo : QWebEngineLoadingInfo
      Passed on as a value: Qt reads the C++ QWebEngineLoadingInfo, which
      stays Python's own.
    """
    #  void QQuickWebEngineView::loadingChanged(const QWebEngineLoadingInfo
    #      &loadingInfo)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView14loadingChangedERK21QWebEngineLoadi'
        'ngInfo',
        self._valueOf(loadingInfo),
    )

  def loadProgressChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::loadProgressChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#loadProgressChanged
    """
    #  void QQuickWebEngineView::loadProgressChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19loadProgressChangedEv',
    )

  @overload(QUrl)
  def linkHovered(self, hoveredUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::linkHovered(const QUrl
    &hoveredUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#linkHovered

    Parameters
    ----------

    hoveredUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickWebEngineView::linkHovered(const QUrl &hoveredUrl)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView11linkHoveredERK4QUrl',
        self._valueOf(hoveredUrl),
    )

  @overload(QWebEngineNavigationRequest)
  @overload(NoneType)
  def navigationRequested(
      self,
      request: Optional[QWebEngineNavigationRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::navigationRequested(QWebEngineNavigationRequest
    *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#navigationRequested

    Parameters
    ----------

    request : Optional[QWebEngineNavigationRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::navigationRequested(
    #      QWebEngineNavigationRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19navigationRequestedEP27QWebEngineN'
        'avigationRequest',
        self._addressOf(request),
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
    QQuickWebEngineView::javaScriptConsoleMessage(QQuickWebEngineView::
    JavaScriptConsoleMessageLevel level, const QString &message, int
    lineNumber, const QString &sourceID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#javaScriptConsoleMessage

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
    #  void QQuickWebEngineView::javaScriptConsoleMessage(
    #      QQuickWebEngineView::JavaScriptConsoleMessageLevel level, const
    #      QString &message, int lineNumber, const QString &sourceID)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView24javaScriptConsoleMessageENS_29Java'
        'ScriptConsoleMessageLevelERK7QStringiS3_',
        level.value, message, lineNumber, sourceID,
    )

  @overload(QWebEngineCertificateError)
  def certificateError(self, error: QWebEngineCertificateError) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::certificateError(const
    QWebEngineCertificateError &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#certificateError

    Parameters
    ----------

    error : QWebEngineCertificateError
      Passed on as a value: Qt reads the C++ QWebEngineCertificateError,
      which stays Python's own.
    """
    #  void QQuickWebEngineView::certificateError(const
    #      QWebEngineCertificateError &error)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView16certificateErrorERK26QWebEngineCer'
        'tificateError',
        self._valueOf(error),
    )

  @overload(QWebEngineFullScreenRequest)
  def fullScreenRequested(
      self,
      request: QWebEngineFullScreenRequest,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::fullScreenRequested(const
    QWebEngineFullScreenRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#fullScreenRequested

    Parameters
    ----------

    request : QWebEngineFullScreenRequest
      Passed on as a value: Qt reads the C++ QWebEngineFullScreenRequest,
      which stays Python's own.
    """
    #  void QQuickWebEngineView::fullScreenRequested(const
    #      QWebEngineFullScreenRequest &request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19fullScreenRequestedERK27QWebEngine'
        'FullScreenRequest',
        self._valueOf(request),
    )

  def isFullScreenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::isFullScreenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#isFullScreenChanged
    """
    #  void QQuickWebEngineView::isFullScreenChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19isFullScreenChangedEv',
    )

  @overload(QUrl, Feature)
  def featurePermissionRequested(
      self,
      securityOrigin: QUrl,
      feature: Feature,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::featurePermissionRequested(const
    QUrl &securityOrigin, QQuickWebEngineView::Feature feature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    feature : Feature
      Passed on as its number.
    """
    #  void QQuickWebEngineView::featurePermissionRequested(const QUrl
    #      &securityOrigin, QQuickWebEngineView::Feature feature)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView26featurePermissionRequestedERK4QUrl'
        'NS_7FeatureE',
        self._valueOf(securityOrigin), feature.value,
    )

  @overload(float)
  def zoomFactorChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::zoomFactorChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#zoomFactorChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWebEngineView::zoomFactorChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView17zoomFactorChangedEd', arg,
    )

  def profileChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::profileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#profileChanged
    """
    #  void QQuickWebEngineView::profileChanged()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView14profileChangedEv')

  def webChannelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::webChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#webChannelChanged
    """
    #  void QQuickWebEngineView::webChannelChanged()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView17webChannelChangedEv')

  @overload(bool)
  def activeFocusOnPressChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::activeFocusOnPressChanged(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#activeFocusOnPressChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineView::activeFocusOnPressChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView25activeFocusOnPressChangedEb', a0,
    )

  def backgroundColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::backgroundColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#backgroundColorChanged
    """
    #  void QQuickWebEngineView::backgroundColorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView22backgroundColorChangedEv',
    )

  @overload(RenderProcessTerminationStatus, int)
  def renderProcessTerminated(
      self,
      terminationStatus: RenderProcessTerminationStatus,
      exitCode: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::renderProcessTerminated(QQuickWebEngineView::
    RenderProcessTerminationStatus terminationStatus, int exitCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#renderProcessTerminated

    Parameters
    ----------

    terminationStatus : RenderProcessTerminationStatus
      Passed on as its number.

    exitCode : int
      Passed on as it is.
    """
    #  void QQuickWebEngineView::renderProcessTerminated(
    #      QQuickWebEngineView::RenderProcessTerminationStatus
    #      terminationStatus, int exitCode)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView23renderProcessTerminatedENS_30Rende'
        'rProcessTerminationStatusEi',
        terminationStatus.value, exitCode,
    )

  def windowCloseRequested(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::windowCloseRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#windowCloseRequested
    """
    #  void QQuickWebEngineView::windowCloseRequested()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView20windowCloseRequestedEv',
    )

  @overload(QSizeF)
  def contentsSizeChanged(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::contentsSizeChanged(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#contentsSizeChanged

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickWebEngineView::contentsSizeChanged(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19contentsSizeChangedERK6QSizeF',
        self._valueOf(size),
    )

  @overload(QPointF)
  def scrollPositionChanged(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::scrollPositionChanged(const QPointF
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#scrollPositionChanged

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickWebEngineView::scrollPositionChanged(const QPointF
    #      &position)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView21scrollPositionChangedERK7QPointF',
        self._valueOf(position, 'QPointF'),
    )

  @overload(bool)
  def audioMutedChanged(self, muted: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::audioMutedChanged(bool muted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#audioMutedChanged

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineView::audioMutedChanged(bool muted)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView17audioMutedChangedEb', muted,
    )

  @overload(bool)
  def recentlyAudibleChanged(self, recentlyAudible: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::recentlyAudibleChanged(bool
    recentlyAudible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#recentlyAudibleChanged

    Parameters
    ----------

    recentlyAudible : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineView::recentlyAudibleChanged(bool recentlyAudible)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView22recentlyAudibleChangedEb',
        recentlyAudible,
    )

  @overload(int)
  def webChannelWorldChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::webChannelWorldChanged(uint a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#webChannelWorldChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickWebEngineView::webChannelWorldChanged(uint a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView22webChannelWorldChangedEj', a0,
    )

  @overload(QWebEngineContextMenuRequest)
  @overload(NoneType)
  def contextMenuRequested(
      self,
      request: Optional[QWebEngineContextMenuRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::contextMenuRequested(QWebEngineContextMenuRequest
    *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#contextMenuRequested

    Parameters
    ----------

    request : Optional[QWebEngineContextMenuRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::contextMenuRequested(
    #      QWebEngineContextMenuRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView20contextMenuRequestedEP28QWebEngine'
        'ContextMenuRequest',
        self._addressOf(request),
    )

  @overload(QQuickWebEngineAuthenticationDialogRequest)
  @overload(NoneType)
  def authenticationDialogRequested(
      self,
      request: Optional[QQuickWebEngineAuthenticationDialogRequest],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::authenticationDialogRequested(
    QQuickWebEngineAuthenticationDialogRequest *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html

    Parameters
    ----------

    request : Optional[QQuickWebEngineAuthenticationDialogRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::authenticationDialogRequested(
    #      QQuickWebEngineAuthenticationDialogRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView29authenticationDialogRequestedEP42Q'
        'QuickWebEngineAuthenticationDialogRequest',
        self._addressOf(request),
    )

  @overload(QQuickWebEngineJavaScriptDialogRequest)
  @overload(NoneType)
  def javaScriptDialogRequested(
      self,
      request: Optional[QQuickWebEngineJavaScriptDialogRequest],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::javaScriptDialogRequested(
    QQuickWebEngineJavaScriptDialogRequest *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#javaScriptDialogRequested

    Parameters
    ----------

    request : Optional[QQuickWebEngineJavaScriptDialogRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::javaScriptDialogRequested(
    #      QQuickWebEngineJavaScriptDialogRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView25javaScriptDialogRequestedEP38QQuic'
        'kWebEngineJavaScriptDialogRequest',
        self._addressOf(request),
    )

  @overload(QQuickWebEngineColorDialogRequest)
  @overload(NoneType)
  def colorDialogRequested(
      self,
      request: Optional[QQuickWebEngineColorDialogRequest],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::colorDialogRequested(
    QQuickWebEngineColorDialogRequest *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#colorDialogRequested

    Parameters
    ----------

    request : Optional[QQuickWebEngineColorDialogRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::colorDialogRequested(
    #      QQuickWebEngineColorDialogRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView20colorDialogRequestedEP33QQuickWebE'
        'ngineColorDialogRequest',
        self._addressOf(request),
    )

  @overload(QQuickWebEngineFileDialogRequest)
  @overload(NoneType)
  def fileDialogRequested(
      self,
      request: Optional[QQuickWebEngineFileDialogRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::fileDialogRequested(QQuickWebEngineFileDialogRequest
    *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#fileDialogRequested

    Parameters
    ----------

    request : Optional[QQuickWebEngineFileDialogRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::fileDialogRequested(
    #      QQuickWebEngineFileDialogRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19fileDialogRequestedEP32QQuickWebEn'
        'gineFileDialogRequest',
        self._addressOf(request),
    )

  @overload(str, bool)
  def pdfPrintingFinished(self, filePath: str, success: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::pdfPrintingFinished(const QString
    &filePath, bool success)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#pdfPrintingFinished

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    success : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineView::pdfPrintingFinished(const QString &filePath,
    #      bool success)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19pdfPrintingFinishedERK7QStringb',
        filePath, success,
    )

  @overload(QWebEngineQuotaRequest)
  def quotaRequested(self, request: QWebEngineQuotaRequest) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::quotaRequested(const
    QWebEngineQuotaRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#quotaRequested

    Parameters
    ----------

    request : QWebEngineQuotaRequest
      Passed on as a value: Qt reads the C++ QWebEngineQuotaRequest, which
      stays Python's own.
    """
    #  void QQuickWebEngineView::quotaRequested(const QWebEngineQuotaRequest
    #      &request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView14quotaRequestedERK22QWebEngineQuota'
        'Request',
        self._valueOf(request),
    )

  @overload(QRect, QRect)
  def geometryChangeRequested(
      self,
      geometry: QRect,
      frameGeometry: QRect,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::geometryChangeRequested(const QRect
    &geometry, const QRect &frameGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#geometryChangeRequested

    Parameters
    ----------

    geometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    frameGeometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuickWebEngineView::geometryChangeRequested(const QRect
    #      &geometry, const QRect &frameGeometry)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView23geometryChangeRequestedERK5QRectS2'
        '_',
        self._valueOf(geometry), self._valueOf(frameGeometry),
    )

  def inspectedViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::inspectedViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#inspectedViewChanged
    """
    #  void QQuickWebEngineView::inspectedViewChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView20inspectedViewChangedEv',
    )

  def devToolsViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::devToolsViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#devToolsViewChanged
    """
    #  void QQuickWebEngineView::devToolsViewChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19devToolsViewChangedEv',
    )

  @overload(QWebEngineRegisterProtocolHandlerRequest)
  def registerProtocolHandlerRequested(
      self,
      request: QWebEngineRegisterProtocolHandlerRequest,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::registerProtocolHandlerRequested(const
    QWebEngineRegisterProtocolHandlerRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html

    Parameters
    ----------

    request : QWebEngineRegisterProtocolHandlerRequest
      Passed on as a value: Qt reads the C++
      QWebEngineRegisterProtocolHandlerRequest, which stays Python's own.
    """
    #  void QQuickWebEngineView::registerProtocolHandlerRequested(const
    #      QWebEngineRegisterProtocolHandlerRequest &request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView32registerProtocolHandlerRequestedER'
        'K40QWebEngineRegisterProtocolHandlerRequest',
        self._valueOf(request),
    )

  def printRequested(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::printRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#printRequested
    """
    #  void QQuickWebEngineView::printRequested()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView14printRequestedEv')

  @overload(QQuickWebEngineClientCertificateSelection)
  @overload(NoneType)
  def selectClientCertificate(
      self,
      clientCertSelection: Optional[QQuickWebEngineClientCertificateSelection],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::selectClientCertificate(
    QQuickWebEngineClientCertificateSelection *clientCertSelection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#selectClientCertificate

    Parameters
    ----------

    clientCertSelection : Optional[QQuickWebEngineClientCertificateSelection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::selectClientCertificate(
    #      QQuickWebEngineClientCertificateSelection *clientCertSelection)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView23selectClientCertificateEP41QQuickW'
        'ebEngineClientCertificateSelection',
        self._addressOf(clientCertSelection),
    )

  @overload(QQuickWebEngineTooltipRequest)
  @overload(NoneType)
  def tooltipRequested(
      self,
      request: Optional[QQuickWebEngineTooltipRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::tooltipRequested(QQuickWebEngineTooltipRequest
    *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#tooltipRequested

    Parameters
    ----------

    request : Optional[QQuickWebEngineTooltipRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::tooltipRequested(
    #      QQuickWebEngineTooltipRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView16tooltipRequestedEP29QQuickWebEngin'
        'eTooltipRequest',
        self._addressOf(request),
    )

  @overload(LifecycleState)
  def lifecycleStateChanged(self, state: LifecycleState) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::lifecycleStateChanged(QQuickWebEngineView::
    LifecycleState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#lifecycleStateChanged

    Parameters
    ----------

    state : LifecycleState
      Passed on as its number.
    """
    #  void QQuickWebEngineView::lifecycleStateChanged(QQuickWebEngineView::
    #      LifecycleState state)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView21lifecycleStateChangedENS_14Lifecyc'
        'leStateE',
        state.value,
    )

  @overload(LifecycleState)
  def recommendedStateChanged(self, state: LifecycleState) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::recommendedStateChanged(QQuickWebEngineView::
    LifecycleState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#recommendedStateChanged

    Parameters
    ----------

    state : LifecycleState
      Passed on as its number.
    """
    #  void QQuickWebEngineView::recommendedStateChanged(
    #      QQuickWebEngineView::LifecycleState state)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView23recommendedStateChangedENS_14Lifec'
        'ycleStateE',
        state.value,
    )

  @overload(QWebEngineFindTextResult)
  def findTextFinished(self, result: QWebEngineFindTextResult) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::findTextFinished(const
    QWebEngineFindTextResult &result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#findTextFinished

    Parameters
    ----------

    result : QWebEngineFindTextResult
      Passed on as a value: Qt reads the C++ QWebEngineFindTextResult, which
      stays Python's own.
    """
    #  void QQuickWebEngineView::findTextFinished(const
    #      QWebEngineFindTextResult &result)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView16findTextFinishedERK24QWebEngineFin'
        'dTextResult',
        self._valueOf(result),
    )

  @overload(int)
  def renderProcessPidChanged(self, pid: int) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::renderProcessPidChanged(qint64
    pid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#renderProcessPidChanged

    Parameters
    ----------

    pid : int
      Passed on as it is.
    """
    #  void QQuickWebEngineView::renderProcessPidChanged(qint64 pid)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView23renderProcessPidChangedEx', pid,
    )

  def canGoBackChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::canGoBackChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#canGoBackChanged
    """
    #  void QQuickWebEngineView::canGoBackChanged()
    self.uglySide.call('ritual_ZN19QQuickWebEngineView16canGoBackChangedEv')

  def canGoForwardChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::canGoForwardChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#canGoForwardChanged
    """
    #  void QQuickWebEngineView::canGoForwardChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19canGoForwardChangedEv',
    )

  @overload(QQuickWebEngineNewWindowRequest)
  @overload(NoneType)
  def newWindowRequested(
      self,
      request: Optional[QQuickWebEngineNewWindowRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::newWindowRequested(QQuickWebEngineNewWindowRequest
    *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#newWindowRequested

    Parameters
    ----------

    request : Optional[QQuickWebEngineNewWindowRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::newWindowRequested(
    #      QQuickWebEngineNewWindowRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView18newWindowRequestedEP31QQuickWebEng'
        'ineNewWindowRequest',
        self._addressOf(request),
    )

  @overload(QQuickWebEngineTouchSelectionMenuRequest)
  @overload(NoneType)
  def touchSelectionMenuRequested(
      self,
      request: Optional[QQuickWebEngineTouchSelectionMenuRequest],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::touchSelectionMenuRequested(
    QQuickWebEngineTouchSelectionMenuRequest *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html

    Parameters
    ----------

    request : Optional[QQuickWebEngineTouchSelectionMenuRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::touchSelectionMenuRequested(
    #      QQuickWebEngineTouchSelectionMenuRequest *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView27touchSelectionMenuRequestedEP40QQu'
        'ickWebEngineTouchSelectionMenuRequest',
        self._addressOf(request),
    )

  def touchHandleDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::touchHandleDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html
    """
    #  void QQuickWebEngineView::touchHandleDelegateChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView26touchHandleDelegateChangedEv',
    )

  @overload(QWebEngineFileSystemAccessRequest)
  def fileSystemAccessRequested(
      self,
      request: QWebEngineFileSystemAccessRequest,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::fileSystemAccessRequested(const
    QWebEngineFileSystemAccessRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#fileSystemAccessRequested

    Parameters
    ----------

    request : QWebEngineFileSystemAccessRequest
      Passed on as a value: Qt reads the C++
      QWebEngineFileSystemAccessRequest, which stays Python's own.
    """
    #  void QQuickWebEngineView::fileSystemAccessRequested(const
    #      QWebEngineFileSystemAccessRequest &request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView25fileSystemAccessRequestedERK33QWeb'
        'EngineFileSystemAccessRequest',
        self._valueOf(request),
    )

  @overload(QWebEngineWebAuthUxRequest)
  @overload(NoneType)
  def webAuthUxRequested(
      self,
      request: Optional[QWebEngineWebAuthUxRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::webAuthUxRequested(QWebEngineWebAuthUxRequest
    *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#webAuthUxRequested

    Parameters
    ----------

    request : Optional[QWebEngineWebAuthUxRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickWebEngineView::webAuthUxRequested(QWebEngineWebAuthUxRequest
    #      *request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView18webAuthUxRequestedEP26QWebEngineWe'
        'bAuthUxRequest',
        self._addressOf(request),
    )

  @overload(QWebEngineDesktopMediaRequest)
  def desktopMediaRequested(
      self,
      request: QWebEngineDesktopMediaRequest,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::desktopMediaRequested(const
    QWebEngineDesktopMediaRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#desktopMediaRequested

    Parameters
    ----------

    request : QWebEngineDesktopMediaRequest
      Passed on as a value: Qt reads the C++ QWebEngineDesktopMediaRequest,
      which stays Python's own.
    """
    #  void QQuickWebEngineView::desktopMediaRequested(const
    #      QWebEngineDesktopMediaRequest &request)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView21desktopMediaRequestedERK29QWebEngi'
        'neDesktopMediaRequest',
        self._valueOf(request),
    )

  @overload(QQuickWebEngineFrame)
  def printRequestedByFrame(self, frame: QQuickWebEngineFrame) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::printRequestedByFrame(QQuickWebEngineFrame frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#printRequestedByFrame

    Parameters
    ----------

    frame : QQuickWebEngineFrame
      Passed on as a value: Qt reads the C++ QQuickWebEngineFrame, which
      stays Python's own.
    """
    #  void QQuickWebEngineView::printRequestedByFrame(QQuickWebEngineFrame
    #      frame)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView21printRequestedByFrameE20QQuickWebE'
        'ngineFrame',
        self._valueOf(frame),
    )

  @overload(QWebEnginePermission)
  def permissionRequested(
      self,
      permissionRequest: QWebEnginePermission,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineView::permissionRequested(QWebEnginePermission
    permissionRequest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#permissionRequested

    Parameters
    ----------

    permissionRequest : QWebEnginePermission
      Passed on as a value: Qt reads the C++ QWebEnginePermission, which
      stays Python's own.
    """
    #  void QQuickWebEngineView::permissionRequested(QWebEnginePermission
    #      permissionRequest)
    self.uglySide.call(
        'ritual_ZN19QQuickWebEngineView19permissionRequestedE20QWebEnginePe'
        'rmission',
        self._valueOf(permissionRequest),
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickWebEngineView::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN19QQuickWebEngineView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWebEngineView14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickWebEngineView::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN19QQuickWebEngineView10itemChangeEN10QQuickItem10ItemChan'
        'geERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWebEngineView10itemChangeEN10QQuickItem10It'
          'emChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, e: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::dragEnterEvent(QDragEnterEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#dragEnterEvent

    Parameters
    ----------

    e : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::dragEnterEvent(QDragEnterEvent *e)
    ritual = (
        'ritual_ZN19QQuickWebEngineView14dragEnterEventEP15QDragEnterEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWebEngineView14dragEnterEventEP15QDragEnter'
          'Event')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::dragLeaveEvent(QDragLeaveEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#dragLeaveEvent

    Parameters
    ----------

    e : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
    ritual = (
        'ritual_ZN19QQuickWebEngineView14dragLeaveEventEP15QDragLeaveEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWebEngineView14dragLeaveEventEP15QDragLeave'
          'Event')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, e: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::dragMoveEvent(QDragMoveEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineview.html#dragMoveEvent

    Parameters
    ----------

    e : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::dragMoveEvent(QDragMoveEvent *e)
    ritual = (
        'ritual_ZN19QQuickWebEngineView13dragMoveEventEP14QDragMoveEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWebEngineView13dragMoveEventEP14QDragMoveEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, e: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineView::dropEvent(QDropEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineview.html#dropEvent

    Parameters
    ----------

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineView::dropEvent(QDropEvent *e)
    ritual = 'ritual_ZN19QQuickWebEngineView9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickWebEngineView9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(e))
