"""
QQuickWebEngineSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginesettings_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineSettings to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineSettings(QObject):
  """
  The cute side of Qt's QQuickWebEngineSettings: a plain Python object
  standing in front of one C++ QQuickWebEngineSettings.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineSettings is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineSettings that has a ritual and that
  Python can call so far, 126 names in all: 'metaObject', 'tr',
  'autoLoadImages', 'javascriptEnabled', 'javascriptCanOpenWindows',
  'javascriptCanAccessClipboard', 'linksIncludedInFocusChain',
  'localStorageEnabled', 'localContentCanAccessRemoteUrls',
  'spatialNavigationEnabled', 'localContentCanAccessFileUrls',
  'hyperlinkAuditingEnabled', 'errorPageEnabled', 'pluginsEnabled',
  'fullScreenSupportEnabled', 'defaultTextEncoding', 'screenCaptureEnabled',
  'webGLEnabled', 'accelerated2dCanvasEnabled', 'autoLoadIconsForPage',
  'touchIconsEnabled', 'focusOnNavigationEnabled', 'printElementBackgrounds',
  'allowRunningInsecureContent', 'allowGeolocationOnInsecureOrigins',
  'allowWindowActivationFromJavaScript', 'showScrollBars',
  'unknownUrlSchemePolicy', 'playbackRequiresUserGesture',
  'webRTCPublicInterfacesOnly', 'javascriptCanPaste', 'dnsPrefetchEnabled',
  'pdfViewerEnabled', 'navigateOnDropEnabled', 'readingFromCanvasEnabled',
  'forceDarkMode', 'scrollAnimatorEnabled', 'imageAnimationPolicy',
  'printHeaderAndFooter', 'preferCSSMarginsForPrinting',
  'touchEventsApiEnabled', 'backForwardCacheEnabled',
  'trimAccessibilityIdentifiers', 'setAutoLoadImages',
  'setJavascriptEnabled', 'setJavascriptCanOpenWindows',
  'setJavascriptCanAccessClipboard', 'setLinksIncludedInFocusChain',
  'setLocalStorageEnabled', 'setLocalContentCanAccessRemoteUrls',
  'setSpatialNavigationEnabled', 'setLocalContentCanAccessFileUrls',
  'setHyperlinkAuditingEnabled', 'setErrorPageEnabled', 'setPluginsEnabled',
  'setFullScreenSupportEnabled', 'setDefaultTextEncoding',
  'setScreenCaptureEnabled', 'setWebGLEnabled',
  'setAccelerated2dCanvasEnabled', 'setAutoLoadIconsForPage',
  'setTouchIconsEnabled', 'setFocusOnNavigationEnabled',
  'setPrintElementBackgrounds', 'setAllowRunningInsecureContent',
  'setAllowGeolocationOnInsecureOrigins',
  'setAllowWindowActivationFromJavaScript', 'setShowScrollBars',
  'setUnknownUrlSchemePolicy', 'setPlaybackRequiresUserGesture',
  'setWebRTCPublicInterfacesOnly', 'setJavascriptCanPaste',
  'setDnsPrefetchEnabled', 'setPdfViewerEnabled', 'setNavigateOnDropEnabled',
  'setReadingFromCanvasEnabled', 'setForceDarkMode',
  'setScrollAnimatorEnabled', 'setImageAnimationPolicy',
  'setPrintHeaderAndFooter', 'setPreferCSSMarginsForPrinting',
  'setTouchEventsApiEnabled', 'setBackForwardCacheEnabled',
  'setTrimAccessibilityIdentifiers', 'autoLoadImagesChanged',
  'javascriptEnabledChanged', 'javascriptCanOpenWindowsChanged',
  'javascriptCanAccessClipboardChanged', 'linksIncludedInFocusChainChanged',
  'localStorageEnabledChanged', 'localContentCanAccessRemoteUrlsChanged',
  'spatialNavigationEnabledChanged', 'localContentCanAccessFileUrlsChanged',
  'hyperlinkAuditingEnabledChanged', 'errorPageEnabledChanged',
  'pluginsEnabledChanged', 'fullScreenSupportEnabledChanged',
  'defaultTextEncodingChanged', 'screenCaptureEnabledChanged',
  'webGLEnabledChanged', 'accelerated2dCanvasEnabledChanged',
  'autoLoadIconsForPageChanged', 'touchIconsEnabledChanged',
  'focusOnNavigationEnabledChanged', 'printElementBackgroundsChanged',
  'allowRunningInsecureContentChanged',
  'allowGeolocationOnInsecureOriginsChanged',
  'allowWindowActivationFromJavaScriptChanged', 'showScrollBarsChanged',
  'unknownUrlSchemePolicyChanged', 'playbackRequiresUserGestureChanged',
  'webRTCPublicInterfacesOnlyChanged', 'javascriptCanPasteChanged',
  'dnsPrefetchEnabledChanged', 'pdfViewerEnabledChanged',
  'navigateOnDropEnabledChanged', 'readingFromCanvasEnabledChanged',
  'forceDarkModeChanged', 'scrollAnimatorEnabledChanged',
  'imageAnimationPolicyChanged', 'printHeaderAndFooterChanged',
  'preferCSSMarginsForPrintingChanged', 'touchEventsApiEnabledChanged',
  'backForwardCacheEnabledChanged', 'trimAccessibilityIdentifiersChanged',
  'setParentSettings'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineSettings::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWebEngineSettings::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineSettings::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickWebEngineSettings::~QQuickWebEngineSettings()': the
    destructor: Python never removes a C++ QQuickWebEngineSettings.

  What has no ritual
  ------------------

  4 of the 135 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWebEngineSettings is created at the first use, not by
    'QQuickWebEngineSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineSettings.
  - Qt tells when it has removed the C++ QQuickWebEngineSettings. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWebEngineSettings, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ImageAnimationPolicy(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineSettings::ImageAnimationPolicy' of Qt, with the
    3 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Allow = Kee[int](1)
    AnimateOnce = Kee[int](2)
    Disallow = Kee[int](3)

  class UnknownUrlSchemePolicy(CuteNum):
    """
    The enum 'QQuickWebEngineSettings::UnknownUrlSchemePolicy' of Qt, with
    the 3 names Qt gives in it.
    """

    DisallowUnknownUrlSchemes = Kee[int](1)
    AllowUnknownUrlSchemesFromUserInteraction = Kee[int](2)
    AllowAllUnknownUrlSchemes = Kee[int](3)

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
    Calls Qt's 'QString QQuickWebEngineSettings::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebenginesettings.html#tr

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
    #  QString QQuickWebEngineSettings::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickWebEngineSettings2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineSettings'

  #  A C++ QQuickWebEngineSettings Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebEngineSettings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineSettings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def autoLoadImages(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::autoLoadImages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#autoLoadImages
    """
    #  bool QQuickWebEngineSettings::autoLoadImages() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings14autoLoadImagesEv',
    )

  def javascriptEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::javascriptEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#javascriptEnabled
    """
    #  bool QQuickWebEngineSettings::javascriptEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings17javascriptEnabledEv',
    )

  def javascriptCanOpenWindows(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::javascriptCanOpenWindows()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::javascriptCanOpenWindows() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings24javascriptCanOpenWindowsEv',
    )

  def javascriptCanAccessClipboard(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::javascriptCanAccessClipboard()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::javascriptCanAccessClipboard() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings28javascriptCanAccessClipboardE'
        'v',
    )

  def linksIncludedInFocusChain(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::linksIncludedInFocusChain()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::linksIncludedInFocusChain() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings25linksIncludedInFocusChainEv',
    )

  def localStorageEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::localStorageEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#localStorageEnabled
    """
    #  bool QQuickWebEngineSettings::localStorageEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings19localStorageEnabledEv',
    )

  def localContentCanAccessRemoteUrls(self) -> bool:
    """
    Calls Qt's 'bool
    QQuickWebEngineSettings::localContentCanAccessRemoteUrls() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::localContentCanAccessRemoteUrls() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings31localContentCanAccessRemoteUr'
        'lsEv',
    )

  def spatialNavigationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::spatialNavigationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::spatialNavigationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings24spatialNavigationEnabledEv',
    )

  def localContentCanAccessFileUrls(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::localContentCanAccessFileUrls()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::localContentCanAccessFileUrls() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings29localContentCanAccessFileUrls'
        'Ev',
    )

  def hyperlinkAuditingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::hyperlinkAuditingEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::hyperlinkAuditingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings24hyperlinkAuditingEnabledEv',
    )

  def errorPageEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::errorPageEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#errorPageEnabled
    """
    #  bool QQuickWebEngineSettings::errorPageEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings16errorPageEnabledEv',
    )

  def pluginsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::pluginsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#pluginsEnabled
    """
    #  bool QQuickWebEngineSettings::pluginsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings14pluginsEnabledEv',
    )

  def fullScreenSupportEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::fullScreenSupportEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::fullScreenSupportEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings24fullScreenSupportEnabledEv',
    )

  def defaultTextEncoding(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineSettings::defaultTextEncoding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#defaultTextEncoding

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineSettings::defaultTextEncoding() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings19defaultTextEncodingEv',
    )

  def screenCaptureEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::screenCaptureEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#screenCaptureEnabled
    """
    #  bool QQuickWebEngineSettings::screenCaptureEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings20screenCaptureEnabledEv',
    )

  def webGLEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::webGLEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#webGLEnabled
    """
    #  bool QQuickWebEngineSettings::webGLEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings12webGLEnabledEv',
    )

  def accelerated2dCanvasEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::accelerated2dCanvasEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::accelerated2dCanvasEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings26accelerated2dCanvasEnabledEv',
    )

  def autoLoadIconsForPage(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::autoLoadIconsForPage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#autoLoadIconsForPage
    """
    #  bool QQuickWebEngineSettings::autoLoadIconsForPage() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings20autoLoadIconsForPageEv',
    )

  def touchIconsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::touchIconsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#touchIconsEnabled
    """
    #  bool QQuickWebEngineSettings::touchIconsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings17touchIconsEnabledEv',
    )

  def focusOnNavigationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::focusOnNavigationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::focusOnNavigationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings24focusOnNavigationEnabledEv',
    )

  def printElementBackgrounds(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::printElementBackgrounds()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::printElementBackgrounds() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings23printElementBackgroundsEv',
    )

  def allowRunningInsecureContent(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::allowRunningInsecureContent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::allowRunningInsecureContent() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings27allowRunningInsecureContentEv',
    )

  def allowGeolocationOnInsecureOrigins(self) -> bool:
    """
    Calls Qt's 'bool
    QQuickWebEngineSettings::allowGeolocationOnInsecureOrigins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::allowGeolocationOnInsecureOrigins()
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings33allowGeolocationOnInsecureOri'
        'ginsEv',
    )

  def allowWindowActivationFromJavaScript(self) -> bool:
    """
    Calls Qt's 'bool
    QQuickWebEngineSettings::allowWindowActivationFromJavaScript() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::allowWindowActivationFromJavaScript()
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings35allowWindowActivationFromJava'
        'ScriptEv',
    )

  def showScrollBars(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::showScrollBars() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#showScrollBars
    """
    #  bool QQuickWebEngineSettings::showScrollBars() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings14showScrollBarsEv',
    )

  def unknownUrlSchemePolicy(self) -> UnknownUrlSchemePolicy:
    """
    Calls Qt's 'UnknownUrlSchemePolicy
    QQuickWebEngineSettings::unknownUrlSchemePolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Returns
    -------

    UnknownUrlSchemePolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'UnknownUrlSchemePolicy(number)' gives.
    """
    #  UnknownUrlSchemePolicy
    #      QQuickWebEngineSettings::unknownUrlSchemePolicy() const
    return QQuickWebEngineSettings.UnknownUrlSchemePolicy(self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings22unknownUrlSchemePolicyEv',
    ))

  def playbackRequiresUserGesture(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::playbackRequiresUserGesture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::playbackRequiresUserGesture() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings27playbackRequiresUserGestureEv',
    )

  def webRTCPublicInterfacesOnly(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::webRTCPublicInterfacesOnly()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::webRTCPublicInterfacesOnly() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings26webRTCPublicInterfacesOnlyEv',
    )

  def javascriptCanPaste(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::javascriptCanPaste() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#javascriptCanPaste
    """
    #  bool QQuickWebEngineSettings::javascriptCanPaste() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings18javascriptCanPasteEv',
    )

  def dnsPrefetchEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::dnsPrefetchEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#dnsPrefetchEnabled
    """
    #  bool QQuickWebEngineSettings::dnsPrefetchEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings18dnsPrefetchEnabledEv',
    )

  def pdfViewerEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::pdfViewerEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#pdfViewerEnabled
    """
    #  bool QQuickWebEngineSettings::pdfViewerEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings16pdfViewerEnabledEv',
    )

  def navigateOnDropEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::navigateOnDropEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#navigateOnDropEnabled
    """
    #  bool QQuickWebEngineSettings::navigateOnDropEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings21navigateOnDropEnabledEv',
    )

  def readingFromCanvasEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::readingFromCanvasEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::readingFromCanvasEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings24readingFromCanvasEnabledEv',
    )

  def forceDarkMode(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::forceDarkMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#forceDarkMode
    """
    #  bool QQuickWebEngineSettings::forceDarkMode() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings13forceDarkModeEv',
    )

  def scrollAnimatorEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::scrollAnimatorEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#scrollAnimatorEnabled
    """
    #  bool QQuickWebEngineSettings::scrollAnimatorEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings21scrollAnimatorEnabledEv',
    )

  def imageAnimationPolicy(self) -> ImageAnimationPolicy:
    """
    Calls Qt's 'ImageAnimationPolicy
    QQuickWebEngineSettings::imageAnimationPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#imageAnimationPolicy

    Returns
    -------

    ImageAnimationPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ImageAnimationPolicy(number)' gives.
    """
    #  ImageAnimationPolicy QQuickWebEngineSettings::imageAnimationPolicy()
    #      const
    return QQuickWebEngineSettings.ImageAnimationPolicy(self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings20imageAnimationPolicyEv',
    ))

  def printHeaderAndFooter(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::printHeaderAndFooter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#printHeaderAndFooter
    """
    #  bool QQuickWebEngineSettings::printHeaderAndFooter() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings20printHeaderAndFooterEv',
    )

  def preferCSSMarginsForPrinting(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::preferCSSMarginsForPrinting()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::preferCSSMarginsForPrinting() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings27preferCSSMarginsForPrintingEv',
    )

  def touchEventsApiEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::touchEventsApiEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#touchEventsApiEnabled
    """
    #  bool QQuickWebEngineSettings::touchEventsApiEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings21touchEventsApiEnabledEv',
    )

  def backForwardCacheEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::backForwardCacheEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::backForwardCacheEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings23backForwardCacheEnabledEv',
    )

  def trimAccessibilityIdentifiers(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineSettings::trimAccessibilityIdentifiers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  bool QQuickWebEngineSettings::trimAccessibilityIdentifiers() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickWebEngineSettings28trimAccessibilityIdentifiersE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoLoadImages(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setAutoLoadImages(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setAutoLoadImages

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setAutoLoadImages(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings17setAutoLoadImagesEb', on,
    )

  @overload(bool)
  def setJavascriptEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setJavascriptEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setJavascriptEnabled

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setJavascriptEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings20setJavascriptEnabledEb', on,
    )

  @overload(bool)
  def setJavascriptCanOpenWindows(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setJavascriptCanOpenWindows(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setJavascriptCanOpenWindows(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27setJavascriptCanOpenWindowsEb',
        on,
    )

  @overload(bool)
  def setJavascriptCanAccessClipboard(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setJavascriptCanAccessClipboard(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setJavascriptCanAccessClipboard(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31setJavascriptCanAccessClipboar'
        'dEb',
        on,
    )

  @overload(bool)
  def setLinksIncludedInFocusChain(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setLinksIncludedInFocusChain(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setLinksIncludedInFocusChain(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings28setLinksIncludedInFocusChainEb',
        on,
    )

  @overload(bool)
  def setLocalStorageEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setLocalStorageEnabled(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setLocalStorageEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings22setLocalStorageEnabledEb', on,
    )

  @overload(bool)
  def setLocalContentCanAccessRemoteUrls(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setLocalContentCanAccessRemoteUrls(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setLocalContentCanAccessRemoteUrls(bool
    #      on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings34setLocalContentCanAccessRemote'
        'UrlsEb',
        on,
    )

  @overload(bool)
  def setSpatialNavigationEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setSpatialNavigationEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setSpatialNavigationEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27setSpatialNavigationEnabledEb',
        on,
    )

  @overload(bool)
  def setLocalContentCanAccessFileUrls(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setLocalContentCanAccessFileUrls(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setLocalContentCanAccessFileUrls(bool
    #      on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings32setLocalContentCanAccessFileUr'
        'lsEb',
        on,
    )

  @overload(bool)
  def setHyperlinkAuditingEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setHyperlinkAuditingEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setHyperlinkAuditingEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27setHyperlinkAuditingEnabledEb',
        on,
    )

  @overload(bool)
  def setErrorPageEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setErrorPageEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setErrorPageEnabled

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setErrorPageEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings19setErrorPageEnabledEb', on,
    )

  @overload(bool)
  def setPluginsEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setPluginsEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setPluginsEnabled

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setPluginsEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings17setPluginsEnabledEb', on,
    )

  @overload(bool)
  def setFullScreenSupportEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setFullScreenSupportEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setFullScreenSupportEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27setFullScreenSupportEnabledEb',
        on,
    )

  @overload(str)
  def setDefaultTextEncoding(self, encoding: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setDefaultTextEncoding(QString
    encoding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    encoding : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineSettings::setDefaultTextEncoding(QString encoding)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings22setDefaultTextEncodingE7QStrin'
        'g',
        encoding,
    )

  @overload(bool)
  def setScreenCaptureEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setScreenCaptureEnabled(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setScreenCaptureEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings23setScreenCaptureEnabledEb', on,
    )

  @overload(bool)
  def setWebGLEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setWebGLEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setWebGLEnabled

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setWebGLEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings15setWebGLEnabledEb', on,
    )

  @overload(bool)
  def setAccelerated2dCanvasEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setAccelerated2dCanvasEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setAccelerated2dCanvasEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings29setAccelerated2dCanvasEnabledE'
        'b',
        on,
    )

  @overload(bool)
  def setAutoLoadIconsForPage(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setAutoLoadIconsForPage(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setAutoLoadIconsForPage(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings23setAutoLoadIconsForPageEb', on,
    )

  @overload(bool)
  def setTouchIconsEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setTouchIconsEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setTouchIconsEnabled

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setTouchIconsEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings20setTouchIconsEnabledEb', on,
    )

  @overload(bool)
  def setFocusOnNavigationEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setFocusOnNavigationEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setFocusOnNavigationEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27setFocusOnNavigationEnabledEb',
        on,
    )

  @overload(bool)
  def setPrintElementBackgrounds(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setPrintElementBackgrounds(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setPrintElementBackgrounds(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings26setPrintElementBackgroundsEb',
        on,
    )

  @overload(bool)
  def setAllowRunningInsecureContent(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setAllowRunningInsecureContent(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setAllowRunningInsecureContent(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings30setAllowRunningInsecureContent'
        'Eb',
        on,
    )

  @overload(bool)
  def setAllowGeolocationOnInsecureOrigins(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setAllowGeolocationOnInsecureOrigins(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void
    #      QQuickWebEngineSettings::setAllowGeolocationOnInsecureOrigins(bool
    #      on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings36setAllowGeolocationOnInsecureO'
        'riginsEb',
        on,
    )

  @overload(bool)
  def setAllowWindowActivationFromJavaScript(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setAllowWindowActivationFromJavaScript(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setAllowWindowActivationFromJavaScript(
    #      bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings38setAllowWindowActivationFromJa'
        'vaScriptEb',
        on,
    )

  @overload(bool)
  def setShowScrollBars(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setShowScrollBars(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setShowScrollBars

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setShowScrollBars(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings17setShowScrollBarsEb', on,
    )

  @overload(UnknownUrlSchemePolicy)
  def setUnknownUrlSchemePolicy(
      self,
      policy: UnknownUrlSchemePolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setUnknownUrlSchemePolicy(UnknownUrlSchemePolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    policy : UnknownUrlSchemePolicy
      Passed on as its number.
    """
    #  void QQuickWebEngineSettings::setUnknownUrlSchemePolicy(
    #      UnknownUrlSchemePolicy policy)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings25setUnknownUrlSchemePolicyENS_2'
        '2UnknownUrlSchemePolicyE',
        policy.value,
    )

  @overload(bool)
  def setPlaybackRequiresUserGesture(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setPlaybackRequiresUserGesture(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setPlaybackRequiresUserGesture(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings30setPlaybackRequiresUserGesture'
        'Eb',
        on,
    )

  @overload(bool)
  def setWebRTCPublicInterfacesOnly(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setWebRTCPublicInterfacesOnly(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setWebRTCPublicInterfacesOnly(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings29setWebRTCPublicInterfacesOnlyE'
        'b',
        on,
    )

  @overload(bool)
  def setJavascriptCanPaste(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setJavascriptCanPaste(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setJavascriptCanPaste

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setJavascriptCanPaste(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings21setJavascriptCanPasteEb', on,
    )

  @overload(bool)
  def setDnsPrefetchEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setDnsPrefetchEnabled(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setDnsPrefetchEnabled

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setDnsPrefetchEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings21setDnsPrefetchEnabledEb', on,
    )

  @overload(bool)
  def setPdfViewerEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setPdfViewerEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setPdfViewerEnabled

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setPdfViewerEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings19setPdfViewerEnabledEb', on,
    )

  @overload(bool)
  def setNavigateOnDropEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setNavigateOnDropEnabled(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setNavigateOnDropEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings24setNavigateOnDropEnabledEb', on,
    )

  @overload(bool)
  def setReadingFromCanvasEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setReadingFromCanvasEnabled(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setReadingFromCanvasEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27setReadingFromCanvasEnabledEb',
        on,
    )

  @overload(bool)
  def setForceDarkMode(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setForceDarkMode(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setForceDarkMode

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setForceDarkMode(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings16setForceDarkModeEb', on,
    )

  @overload(bool)
  def setScrollAnimatorEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setScrollAnimatorEnabled(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setScrollAnimatorEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings24setScrollAnimatorEnabledEb', on,
    )

  @overload(ImageAnimationPolicy)
  def setImageAnimationPolicy(self, policy: ImageAnimationPolicy) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setImageAnimationPolicy(ImageAnimationPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    policy : ImageAnimationPolicy
      Passed on as its number.
    """
    #  void QQuickWebEngineSettings::setImageAnimationPolicy(
    #      ImageAnimationPolicy policy)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings23setImageAnimationPolicyENS_20I'
        'mageAnimationPolicyE',
        policy.value,
    )

  @overload(bool)
  def setPrintHeaderAndFooter(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setPrintHeaderAndFooter(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setPrintHeaderAndFooter(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings23setPrintHeaderAndFooterEb', on,
    )

  @overload(bool)
  def setPreferCSSMarginsForPrinting(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setPreferCSSMarginsForPrinting(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setPreferCSSMarginsForPrinting(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings30setPreferCSSMarginsForPrinting'
        'Eb',
        on,
    )

  @overload(bool)
  def setTouchEventsApiEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setTouchEventsApiEnabled(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setTouchEventsApiEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings24setTouchEventsApiEnabledEb', on,
    )

  @overload(bool)
  def setBackForwardCacheEnabled(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::setBackForwardCacheEnabled(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setBackForwardCacheEnabled(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings26setBackForwardCacheEnabledEb',
        on,
    )

  @overload(bool)
  def setTrimAccessibilityIdentifiers(self, on: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setTrimAccessibilityIdentifiers(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineSettings::setTrimAccessibilityIdentifiers(bool on)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31setTrimAccessibilityIdentifier'
        'sEb',
        on,
    )

  @overload(THIS)
  @overload(NoneType)
  def setParentSettings(
      self,
      parentSettings: Optional[QQuickWebEngineSettings],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::setParentSettings(QQuickWebEngineSettings
    *parentSettings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#setParentSettings

    Parameters
    ----------

    parentSettings : Optional[QQuickWebEngineSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickWebEngineSettings::setParentSettings(QQuickWebEngineSettings
    #      *parentSettings)
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings17setParentSettingsEPS_',
        self._addressOf(parentSettings),
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
  @overload(THIS)
  @overload(NoneType)
  def __init__(
      self,
      parentSettings: Optional[QQuickWebEngineSettings] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineSettings::QQuickWebEngineSettings(QQuickWebEngineSettings
    *parentSettings)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html

    Parameters
    ----------

    parentSettings : Optional[QQuickWebEngineSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWebEngineSettings::QQuickWebEngineSettings(
    #      QQuickWebEngineSettings *parentSettings)
    self._noteCreation(QQuickWebEngineSettings, lambda: Rituals.call(
        'ritual_ZN23QQuickWebEngineSettingsC1EPS_',
        self._addressOf(parentSettings),
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

  def autoLoadImagesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::autoLoadImagesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#autoLoadImagesChanged
    """
    #  void QQuickWebEngineSettings::autoLoadImagesChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings21autoLoadImagesChangedEv',
    )

  def javascriptEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::javascriptEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::javascriptEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings24javascriptEnabledChangedEv',
    )

  def javascriptCanOpenWindowsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::javascriptCanOpenWindowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::javascriptCanOpenWindowsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31javascriptCanOpenWindowsChange'
        'dEv',
    )

  def javascriptCanAccessClipboardChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::javascriptCanAccessClipboardChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::javascriptCanAccessClipboardChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings35javascriptCanAccessClipboardCh'
        'angedEv',
    )

  def linksIncludedInFocusChainChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::linksIncludedInFocusChainChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::linksIncludedInFocusChainChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings32linksIncludedInFocusChainChang'
        'edEv',
    )

  def localStorageEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::localStorageEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::localStorageEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings26localStorageEnabledChangedEv',
    )

  def localContentCanAccessRemoteUrlsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::localContentCanAccessRemoteUrlsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::localContentCanAccessRemoteUrlsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings38localContentCanAccessRemoteUrl'
        'sChangedEv',
    )

  def spatialNavigationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::spatialNavigationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::spatialNavigationEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31spatialNavigationEnabledChange'
        'dEv',
    )

  def localContentCanAccessFileUrlsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::localContentCanAccessFileUrlsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::localContentCanAccessFileUrlsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings36localContentCanAccessFileUrlsC'
        'hangedEv',
    )

  def hyperlinkAuditingEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::hyperlinkAuditingEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::hyperlinkAuditingEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31hyperlinkAuditingEnabledChange'
        'dEv',
    )

  def errorPageEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::errorPageEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::errorPageEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings23errorPageEnabledChangedEv',
    )

  def pluginsEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::pluginsEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#pluginsEnabledChanged
    """
    #  void QQuickWebEngineSettings::pluginsEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings21pluginsEnabledChangedEv',
    )

  def fullScreenSupportEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::fullScreenSupportEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::fullScreenSupportEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31fullScreenSupportEnabledChange'
        'dEv',
    )

  def defaultTextEncodingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::defaultTextEncodingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::defaultTextEncodingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings26defaultTextEncodingChangedEv',
    )

  def screenCaptureEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::screenCaptureEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::screenCaptureEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27screenCaptureEnabledChangedEv',
    )

  def webGLEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::webGLEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#webGLEnabledChanged
    """
    #  void QQuickWebEngineSettings::webGLEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings19webGLEnabledChangedEv',
    )

  def accelerated2dCanvasEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::accelerated2dCanvasEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::accelerated2dCanvasEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings33accelerated2dCanvasEnabledChan'
        'gedEv',
    )

  def autoLoadIconsForPageChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::autoLoadIconsForPageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::autoLoadIconsForPageChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27autoLoadIconsForPageChangedEv',
    )

  def touchIconsEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::touchIconsEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::touchIconsEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings24touchIconsEnabledChangedEv',
    )

  def focusOnNavigationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::focusOnNavigationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::focusOnNavigationEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31focusOnNavigationEnabledChange'
        'dEv',
    )

  def printElementBackgroundsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::printElementBackgroundsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::printElementBackgroundsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings30printElementBackgroundsChanged'
        'Ev',
    )

  def allowRunningInsecureContentChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::allowRunningInsecureContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::allowRunningInsecureContentChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings34allowRunningInsecureContentCha'
        'ngedEv',
    )

  def allowGeolocationOnInsecureOriginsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::allowGeolocationOnInsecureOriginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void
    #      QQuickWebEngineSettings::allowGeolocationOnInsecureOriginsChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings40allowGeolocationOnInsecureOrig'
        'insChangedEv',
    )

  def allowWindowActivationFromJavaScriptChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::allowWindowActivationFromJavaScriptChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::
    #      allowWindowActivationFromJavaScriptChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings42allowWindowActivationFromJavaS'
        'criptChangedEv',
    )

  def showScrollBarsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::showScrollBarsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#showScrollBarsChanged
    """
    #  void QQuickWebEngineSettings::showScrollBarsChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings21showScrollBarsChangedEv',
    )

  def unknownUrlSchemePolicyChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::unknownUrlSchemePolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::unknownUrlSchemePolicyChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings29unknownUrlSchemePolicyChangedE'
        'v',
    )

  def playbackRequiresUserGestureChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::playbackRequiresUserGestureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::playbackRequiresUserGestureChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings34playbackRequiresUserGestureCha'
        'ngedEv',
    )

  def webRTCPublicInterfacesOnlyChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::webRTCPublicInterfacesOnlyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::webRTCPublicInterfacesOnlyChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings33webRTCPublicInterfacesOnlyChan'
        'gedEv',
    )

  def javascriptCanPasteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::javascriptCanPasteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::javascriptCanPasteChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings25javascriptCanPasteChangedEv',
    )

  def dnsPrefetchEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::dnsPrefetchEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::dnsPrefetchEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings25dnsPrefetchEnabledChangedEv',
    )

  def pdfViewerEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::pdfViewerEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::pdfViewerEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings23pdfViewerEnabledChangedEv',
    )

  def navigateOnDropEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::navigateOnDropEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::navigateOnDropEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings28navigateOnDropEnabledChangedEv',
    )

  def readingFromCanvasEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::readingFromCanvasEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::readingFromCanvasEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings31readingFromCanvasEnabledChange'
        'dEv',
    )

  def forceDarkModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::forceDarkModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html#forceDarkModeChanged
    """
    #  void QQuickWebEngineSettings::forceDarkModeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings20forceDarkModeChangedEv',
    )

  def scrollAnimatorEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::scrollAnimatorEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::scrollAnimatorEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings28scrollAnimatorEnabledChangedEv',
    )

  def imageAnimationPolicyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::imageAnimationPolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::imageAnimationPolicyChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27imageAnimationPolicyChangedEv',
    )

  def printHeaderAndFooterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineSettings::printHeaderAndFooterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::printHeaderAndFooterChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings27printHeaderAndFooterChangedEv',
    )

  def preferCSSMarginsForPrintingChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::preferCSSMarginsForPrintingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::preferCSSMarginsForPrintingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings34preferCSSMarginsForPrintingCha'
        'ngedEv',
    )

  def touchEventsApiEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::touchEventsApiEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::touchEventsApiEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings28touchEventsApiEnabledChangedEv',
    )

  def backForwardCacheEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::backForwardCacheEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::backForwardCacheEnabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings30backForwardCacheEnabledChanged'
        'Ev',
    )

  def trimAccessibilityIdentifiersChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineSettings::trimAccessibilityIdentifiersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginesettings.html
    """
    #  void QQuickWebEngineSettings::trimAccessibilityIdentifiersChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickWebEngineSettings35trimAccessibilityIdentifiersCh'
        'angedEv',
    )
