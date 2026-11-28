"""
QWebEngineSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginesettings.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineSettings(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineSettings: a plain Python object standing in
  front of one C++ QWebEngineSettings.

  What exists
  -----------

  Every function of Qt's QWebEngineSettings that has a ritual and that Python
  can call so far, 18 names in all: 'setFontFamily', 'fontFamily',
  'resetFontFamily', 'setFontSize', 'fontSize', 'resetFontSize',
  'setAttribute', 'testAttribute', 'resetAttribute',
  'setDefaultTextEncoding', 'defaultTextEncoding', 'unknownUrlSchemePolicy',
  'setUnknownUrlSchemePolicy', 'resetUnknownUrlSchemePolicy',
  'setImageAnimationPolicy', 'imageAnimationPolicy',
  'resetImageAnimationPolicy', 'setParentSettings'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineSettings::~QWebEngineSettings()': the destructor: Python
    never removes a C++ QWebEngineSettings.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineSettings is created at the first use, not by
    'QWebEngineSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineSettings.
  """

  #  The enums Qt writes inside QWebEngineSettings, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class FontFamily(CuteNum):
    """
    The enum 'QWebEngineSettings::FontFamily' of Qt, with the 7 names Qt
    gives in it.
    """

    StandardFont = Kee[int](0)
    FixedFont = Kee[int](1)
    SerifFont = Kee[int](2)
    SansSerifFont = Kee[int](3)
    CursiveFont = Kee[int](4)
    FantasyFont = Kee[int](5)
    PictographFont = Kee[int](6)

  class FontSize(CuteNum):
    """
    The enum 'QWebEngineSettings::FontSize' of Qt, with the 4 names Qt gives
    in it.
    """

    MinimumFontSize = Kee[int](0)
    MinimumLogicalFontSize = Kee[int](1)
    DefaultFontSize = Kee[int](2)
    DefaultFixedFontSize = Kee[int](3)

  class ImageAnimationPolicy(CuteNum, scoped=True):
    """
    The enum 'QWebEngineSettings::ImageAnimationPolicy' of Qt, with the 4
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Inherited = Kee[int](0)
    Allow = Kee[int](1)
    AnimateOnce = Kee[int](2)
    Disallow = Kee[int](3)

  class UnknownUrlSchemePolicy(CuteNum):
    """
    The enum 'QWebEngineSettings::UnknownUrlSchemePolicy' of Qt, with the 4
    names Qt gives in it.
    """

    InheritedUnknownUrlSchemePolicy = Kee[int](0)
    DisallowUnknownUrlSchemes = Kee[int](1)
    AllowUnknownUrlSchemesFromUserInteraction = Kee[int](2)
    AllowAllUnknownUrlSchemes = Kee[int](3)

  class WebAttribute(CuteNum):
    """
    The enum 'QWebEngineSettings::WebAttribute' of Qt, with the 39 names Qt
    gives in it.
    """

    AutoLoadImages = Kee[int](0)
    JavascriptEnabled = Kee[int](1)
    JavascriptCanOpenWindows = Kee[int](2)
    JavascriptCanAccessClipboard = Kee[int](3)
    LinksIncludedInFocusChain = Kee[int](4)
    LocalStorageEnabled = Kee[int](5)
    LocalContentCanAccessRemoteUrls = Kee[int](6)
    XSSAuditingEnabled = Kee[int](7)
    SpatialNavigationEnabled = Kee[int](8)
    LocalContentCanAccessFileUrls = Kee[int](9)
    HyperlinkAuditingEnabled = Kee[int](10)
    ScrollAnimatorEnabled = Kee[int](11)
    ErrorPageEnabled = Kee[int](12)
    PluginsEnabled = Kee[int](13)
    FullScreenSupportEnabled = Kee[int](14)
    ScreenCaptureEnabled = Kee[int](15)
    WebGLEnabled = Kee[int](16)
    Accelerated2dCanvasEnabled = Kee[int](17)
    AutoLoadIconsForPage = Kee[int](18)
    TouchIconsEnabled = Kee[int](19)
    FocusOnNavigationEnabled = Kee[int](20)
    PrintElementBackgrounds = Kee[int](21)
    AllowRunningInsecureContent = Kee[int](22)
    AllowGeolocationOnInsecureOrigins = Kee[int](23)
    AllowWindowActivationFromJavaScript = Kee[int](24)
    ShowScrollBars = Kee[int](25)
    PlaybackRequiresUserGesture = Kee[int](26)
    WebRTCPublicInterfacesOnly = Kee[int](27)
    JavascriptCanPaste = Kee[int](28)
    DnsPrefetchEnabled = Kee[int](29)
    PdfViewerEnabled = Kee[int](30)
    NavigateOnDropEnabled = Kee[int](31)
    ReadingFromCanvasEnabled = Kee[int](32)
    ForceDarkMode = Kee[int](33)
    PrintHeaderAndFooter = Kee[int](34)
    PreferCSSMarginsForPrinting = Kee[int](35)
    TouchEventsApiEnabled = Kee[int](36)
    BackForwardCacheEnabled = Kee[int](37)
    TrimAccessibilityIdentifiers = Kee[int](38)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FontFamily)
  def fontFamily(self, which: FontFamily) -> str:
    """
    Calls Qt's 'QString QWebEngineSettings::fontFamily(FontFamily which)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginesettings.html#fontFamily

    Parameters
    ----------

    which : FontFamily
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineSettings::fontFamily(FontFamily which) const
    return self.uglySide.call(
        'ritual_ZNK18QWebEngineSettings10fontFamilyENS_10FontFamilyE',
        which.value,
    )

  @overload(FontSize)
  def fontSize(self, type: FontSize) -> int:
    """
    Calls Qt's 'int QWebEngineSettings::fontSize(FontSize type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginesettings.html#fontSize

    Parameters
    ----------

    type : FontSize
      Passed on as its number.
    """
    #  int QWebEngineSettings::fontSize(FontSize type) const
    return self.uglySide.call(
        'ritual_ZNK18QWebEngineSettings8fontSizeENS_8FontSizeE', type.value,
    )

  @overload(WebAttribute)
  def testAttribute(self, attr: WebAttribute) -> bool:
    """
    Calls Qt's 'bool QWebEngineSettings::testAttribute(WebAttribute attr)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#testAttribute

    Parameters
    ----------

    attr : WebAttribute
      Passed on as its number.
    """
    #  bool QWebEngineSettings::testAttribute(WebAttribute attr) const
    return self.uglySide.call(
        'ritual_ZNK18QWebEngineSettings13testAttributeENS_12WebAttributeE',
        attr.value,
    )

  def defaultTextEncoding(self) -> str:
    """
    Calls Qt's 'QString QWebEngineSettings::defaultTextEncoding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#defaultTextEncoding

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineSettings::defaultTextEncoding() const
    return self.uglySide.call(
        'ritual_ZNK18QWebEngineSettings19defaultTextEncodingEv',
    )

  def unknownUrlSchemePolicy(self) -> UnknownUrlSchemePolicy:
    """
    Calls Qt's 'UnknownUrlSchemePolicy
    QWebEngineSettings::unknownUrlSchemePolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#unknownUrlSchemePolicy

    Returns
    -------

    UnknownUrlSchemePolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'UnknownUrlSchemePolicy(number)' gives.
    """
    #  UnknownUrlSchemePolicy QWebEngineSettings::unknownUrlSchemePolicy()
    #      const
    return QWebEngineSettings.UnknownUrlSchemePolicy(self.uglySide.call(
        'ritual_ZNK18QWebEngineSettings22unknownUrlSchemePolicyEv',
    ))

  def imageAnimationPolicy(self) -> ImageAnimationPolicy:
    """
    Calls Qt's 'ImageAnimationPolicy
    QWebEngineSettings::imageAnimationPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#imageAnimationPolicy

    Returns
    -------

    ImageAnimationPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ImageAnimationPolicy(number)' gives.
    """
    #  ImageAnimationPolicy QWebEngineSettings::imageAnimationPolicy() const
    return QWebEngineSettings.ImageAnimationPolicy(self.uglySide.call(
        'ritual_ZNK18QWebEngineSettings20imageAnimationPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FontFamily, str)
  def setFontFamily(self, which: FontFamily, family: str) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::setFontFamily(FontFamily which,
    const QString &family)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#setFontFamily

    Parameters
    ----------

    which : FontFamily
      Passed on as its number.

    family : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineSettings::setFontFamily(FontFamily which, const QString
    #      &family)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings13setFontFamilyENS_10FontFamilyERK7QS'
        'tring',
        which.value, family,
    )

  @overload(FontSize, int)
  def setFontSize(self, type: FontSize, size: int) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::setFontSize(FontSize type, int
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#setFontSize

    Parameters
    ----------

    type : FontSize
      Passed on as its number.

    size : int
      Passed on as it is.
    """
    #  void QWebEngineSettings::setFontSize(FontSize type, int size)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings11setFontSizeENS_8FontSizeEi',
        type.value, size,
    )

  @overload(WebAttribute, bool)
  def setAttribute(self, attr: WebAttribute, on: bool) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::setAttribute(WebAttribute attr, bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#setAttribute

    Parameters
    ----------

    attr : WebAttribute
      Passed on as its number.

    on : bool
      Passed on as it is.
    """
    #  void QWebEngineSettings::setAttribute(WebAttribute attr, bool on)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings12setAttributeENS_12WebAttributeEb',
        attr.value, on,
    )

  @overload(str)
  def setDefaultTextEncoding(self, encoding: str) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::setDefaultTextEncoding(const QString
    &encoding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#setDefaultTextEncoding

    Parameters
    ----------

    encoding : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineSettings::setDefaultTextEncoding(const QString
    #      &encoding)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings22setDefaultTextEncodingERK7QString',
        encoding,
    )

  @overload(UnknownUrlSchemePolicy)
  def setUnknownUrlSchemePolicy(
      self,
      policy: UnknownUrlSchemePolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QWebEngineSettings::setUnknownUrlSchemePolicy(UnknownUrlSchemePolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#setUnknownUrlSchemePolicy

    Parameters
    ----------

    policy : UnknownUrlSchemePolicy
      Passed on as its number.
    """
    #  void QWebEngineSettings::setUnknownUrlSchemePolicy(
    #      UnknownUrlSchemePolicy policy)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings25setUnknownUrlSchemePolicyENS_22Unkn'
        'ownUrlSchemePolicyE',
        policy.value,
    )

  @overload(ImageAnimationPolicy)
  def setImageAnimationPolicy(self, policy: ImageAnimationPolicy) -> None:
    """
    Calls Qt's 'void
    QWebEngineSettings::setImageAnimationPolicy(ImageAnimationPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#setImageAnimationPolicy

    Parameters
    ----------

    policy : ImageAnimationPolicy
      Passed on as its number.
    """
    #  void QWebEngineSettings::setImageAnimationPolicy(ImageAnimationPolicy
    #      policy)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings23setImageAnimationPolicyENS_20ImageA'
        'nimationPolicyE',
        policy.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setParentSettings(
      self,
      parentSettings: Optional[QWebEngineSettings],
  ) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::setParentSettings(QWebEngineSettings
    *parentSettings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#setParentSettings

    Parameters
    ----------

    parentSettings : Optional[QWebEngineSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineSettings::setParentSettings(QWebEngineSettings
    #      *parentSettings)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings17setParentSettingsEPS_',
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
      parentSettings: Optional[QWebEngineSettings] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineSettings::QWebEngineSettings(QWebEngineSettings
    *parentSettings)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#QWebEngineSettings

    Parameters
    ----------

    parentSettings : Optional[QWebEngineSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineSettings::QWebEngineSettings(QWebEngineSettings
    #      *parentSettings)
    self._noteCreation(QWebEngineSettings, lambda: Rituals.call(
        'ritual_ZN18QWebEngineSettingsC1EPS_',
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

  @overload(FontFamily)
  def resetFontFamily(self, which: FontFamily) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::resetFontFamily(FontFamily which)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#resetFontFamily

    Parameters
    ----------

    which : FontFamily
      Passed on as its number.
    """
    #  void QWebEngineSettings::resetFontFamily(FontFamily which)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings15resetFontFamilyENS_10FontFamilyE',
        which.value,
    )

  @overload(FontSize)
  def resetFontSize(self, type: FontSize) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::resetFontSize(FontSize type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#resetFontSize

    Parameters
    ----------

    type : FontSize
      Passed on as its number.
    """
    #  void QWebEngineSettings::resetFontSize(FontSize type)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings13resetFontSizeENS_8FontSizeE',
        type.value,
    )

  @overload(WebAttribute)
  def resetAttribute(self, attr: WebAttribute) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::resetAttribute(WebAttribute attr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#resetAttribute

    Parameters
    ----------

    attr : WebAttribute
      Passed on as its number.
    """
    #  void QWebEngineSettings::resetAttribute(WebAttribute attr)
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings14resetAttributeENS_12WebAttributeE',
        attr.value,
    )

  def resetUnknownUrlSchemePolicy(self) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::resetUnknownUrlSchemePolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html
    """
    #  void QWebEngineSettings::resetUnknownUrlSchemePolicy()
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings27resetUnknownUrlSchemePolicyEv',
    )

  def resetImageAnimationPolicy(self) -> None:
    """
    Calls Qt's 'void QWebEngineSettings::resetImageAnimationPolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginesettings.html#resetImageAnimationPolicy
    """
    #  void QWebEngineSettings::resetImageAnimationPolicy()
    self.uglySide.call(
        'ritual_ZN18QWebEngineSettings25resetImageAnimationPolicyEv',
    )
