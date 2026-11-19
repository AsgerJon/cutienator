"""
QUrl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qurl.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_byte_array import QByteArray
from ._q_byte_array_view import QByteArrayView
from ._q_url_ace_processing_option import AceProcessingOption
from ._q_url_component_formatting_option import ComponentFormattingOption
from ._q_url_parsing_mode import ParsingMode
from ._q_url_url_formatting_option import UrlFormattingOption
from ._q_url_user_input_resolution_option import UserInputResolutionOption

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QUrl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUrl: a plain Python object standing in front of one
  C++ QUrl.

  C++ hands a QUrl around as a copy, so every C++ QUrl behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUrl that has a ritual and that Python can call so
  far, 42 names in all: 'setUrl', 'fromEncoded', 'fromUserInput', 'isValid',
  'errorString', 'isEmpty', 'clear', 'setScheme', 'scheme', 'setAuthority',
  'authority', 'setUserInfo', 'userInfo', 'setUserName', 'userName',
  'setPassword', 'password', 'setHost', 'host', 'setPort', 'port', 'setPath',
  'path', 'fileName', 'hasQuery', 'setQuery', 'query', 'hasFragment',
  'fragment', 'setFragment', 'resolved', 'isRelative', 'isParentOf',
  'isLocalFile', 'fromLocalFile', 'toLocalFile', 'detach', 'isDetached',
  'fromPercentEncoding', 'toPercentEncoding', 'fromAce', 'toAce'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUrl::~QUrl()': the destructor: Python removes its C++ QUrl by it,
    and has no other use for it.
  - Qt's 'void QUrl::setQuery(const QUrlQuery &query)': names 'QUrlQuery',
    which has no cute class yet.

  What has no ritual
  ------------------

  17 of the 64 functions Qt declares: 16 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QUrl is created at the first use, not by 'QUrl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUrl back gives a copy the ritual made for Python, in
    a new cute QUrl.
  """

  #  The enums Qt writes inside QUrl, and the names Qt has for the
  #  combinations of its flags enums.
  AceProcessingOption = AceProcessingOption
  AceProcessingOptions = AceProcessingOption
  ComponentFormattingOption = ComponentFormattingOption
  ComponentFormattingOptions = ComponentFormattingOption
  ParsingMode = ParsingMode
  UrlFormattingOption = UrlFormattingOption
  UserInputResolutionOption = UserInputResolutionOption
  UserInputResolutionOptions = UserInputResolutionOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArrayView)
  @overload(QByteArrayView, ParsingMode)
  def fromEncoded(
      input: QByteArrayView,
      mode: ParsingMode = ParsingMode.TolerantMode,
  ) -> QUrl:
    """
    Calls Qt's 'QUrl QUrl::fromEncoded(QByteArrayView input, ParsingMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#fromEncoded

    Parameters
    ----------

    input : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.TolerantMode.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QUrl::fromEncoded(QByteArrayView input, ParsingMode mode)
    address = Rituals.call(
        'ritual_ZN4QUrl11fromEncodedE14QByteArrayViewNS_11ParsingModeE',
        CuteMixin._valueOf(input), mode.value,
    )
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, str)
  @overload(str, str, UserInputResolutionOptions)
  def fromUserInput(
      userInput: str,
      workingDirectory: str = '',
      options: UserInputResolutionOptions = (
          UserInputResolutionOptions.DefaultResolution),
  ) -> QUrl:
    """
    Calls Qt's 'QUrl QUrl::fromUserInput(const QString &userInput, const
    QString &workingDirectory, UserInputResolutionOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#fromUserInput

    Parameters
    ----------

    userInput : str
      Passed on as it is: a QString is made of it for the call.

    workingDirectory : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    options : UserInputResolutionOptions
      Passed on as its number. May be left out, as in Qt: it is then
      UserInputResolutionOptions.DefaultResolution.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QUrl::fromUserInput(const QString &userInput, const QString
    #      &workingDirectory, UserInputResolutionOptions options)
    address = Rituals.call(
        'ritual_ZN4QUrl13fromUserInputERK7QStringS2_6QFlagsINS_25UserInputR'
        'esolutionOptionEE',
        userInput, workingDirectory, options.value,
    )
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(str)
  def fromLocalFile(localfile: str) -> QUrl:
    """
    Calls Qt's 'QUrl QUrl::fromLocalFile(const QString &localfile)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#fromLocalFile

    Parameters
    ----------

    localfile : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QUrl::fromLocalFile(const QString &localfile)
    address = Rituals.call(
        'ritual_ZN4QUrl13fromLocalFileERK7QString', localfile,
    )
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def fromPercentEncoding(a0: QByteArray) -> str:
    """
    Calls Qt's 'QString QUrl::fromPercentEncoding(const QByteArray &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#fromPercentEncoding

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::fromPercentEncoding(const QByteArray &a0)
    return Rituals.call(
        'ritual_ZN4QUrl19fromPercentEncodingERK10QByteArray',
        CuteMixin._valueOf(a0),
    )

  @staticmethod
  @overload(str)
  @overload(str, QByteArray)
  @overload(str, QByteArray, QByteArray)
  def toPercentEncoding(
      a0: str,
      exclude: Optional[QByteArray] = None,
      include: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QUrl::toPercentEncoding(const QString &a0, const
    QByteArray &exclude, const QByteArray &include)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#toPercentEncoding

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    exclude : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    include : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QUrl::toPercentEncoding(const QString &a0, const QByteArray
    #      &exclude, const QByteArray &include)
    if exclude is None:
      exclude = QByteArray()
    if include is None:
      include = QByteArray()
    address = Rituals.call(
        'ritual_ZN4QUrl17toPercentEncodingERK7QStringRK10QByteArrayS5_',
        a0, CuteMixin._valueOf(exclude), CuteMixin._valueOf(include),
    )
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  @overload(QByteArray, AceProcessingOptions)
  def fromAce(
      domain: QByteArray,
      options: AceProcessingOptions = AceProcessingOptions(),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::fromAce(const QByteArray &domain,
    AceProcessingOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#fromAce

    Parameters
    ----------

    domain : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    options : AceProcessingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      AceProcessingOptions().

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::fromAce(const QByteArray &domain, AceProcessingOptions
    #      options)
    return Rituals.call(
        'ritual_ZN4QUrl7fromAceERK10QByteArray6QFlagsINS_19AceProcessingOpt'
        'ionEE',
        CuteMixin._valueOf(domain), options.value,
    )

  @staticmethod
  @overload(str)
  @overload(str, AceProcessingOptions)
  def toAce(
      domain: str,
      options: AceProcessingOptions = AceProcessingOptions(),
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QUrl::toAce(const QString &domain,
    AceProcessingOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#toAce

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    options : AceProcessingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      AceProcessingOptions().

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QUrl::toAce(const QString &domain, AceProcessingOptions
    #      options)
    address = Rituals.call(
        'ritual_ZN4QUrl5toAceERK7QString6QFlagsINS_19AceProcessingOptionEE',
        domain, options.value,
    )
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUrl'

  #  Qt's '~QUrl()'. Naming it makes this a value class: Python owns every
  #  C++ QUrl behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QUrlD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QUrl::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#isValid
    """
    #  bool QUrl::isValid() const
    return self.uglySide.call('ritual_ZNK4QUrl7isValidEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QUrl::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::errorString() const
    return self.uglySide.call('ritual_ZNK4QUrl11errorStringEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QUrl::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#isEmpty
    """
    #  bool QUrl::isEmpty() const
    return self.uglySide.call('ritual_ZNK4QUrl7isEmptyEv')

  def scheme(self) -> str:
    """
    Calls Qt's 'QString QUrl::scheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#scheme

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::scheme() const
    return self.uglySide.call('ritual_ZNK4QUrl6schemeEv')

  @overload()
  @overload(ComponentFormattingOptions)
  def authority(
      self,
      options: ComponentFormattingOptions = (
          ComponentFormattingOptions.PrettyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::authority(ComponentFormattingOptions options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#authority

    Parameters
    ----------

    options : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.PrettyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::authority(ComponentFormattingOptions options) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl9authorityE6QFlagsINS_25ComponentFormattingOptionEE',
        options.value,
    )

  @overload()
  @overload(ComponentFormattingOptions)
  def userInfo(
      self,
      options: ComponentFormattingOptions = (
          ComponentFormattingOptions.PrettyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::userInfo(ComponentFormattingOptions options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#userInfo

    Parameters
    ----------

    options : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.PrettyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::userInfo(ComponentFormattingOptions options) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl8userInfoE6QFlagsINS_25ComponentFormattingOptionEE',
        options.value,
    )

  @overload()
  @overload(ComponentFormattingOptions)
  def userName(
      self,
      options: ComponentFormattingOptions = (
          ComponentFormattingOptions.FullyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::userName(ComponentFormattingOptions options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#userName

    Parameters
    ----------

    options : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.FullyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::userName(ComponentFormattingOptions options) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl8userNameE6QFlagsINS_25ComponentFormattingOptionEE',
        options.value,
    )

  @overload()
  @overload(ComponentFormattingOptions)
  def password(
      self,
      a0: ComponentFormattingOptions = (
          ComponentFormattingOptions.FullyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::password(ComponentFormattingOptions a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#password

    Parameters
    ----------

    a0 : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.FullyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::password(ComponentFormattingOptions a0) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl8passwordE6QFlagsINS_25ComponentFormattingOptionEE',
        a0.value,
    )

  @overload()
  @overload(ComponentFormattingOptions)
  def host(
      self,
      a0: ComponentFormattingOptions = (
          ComponentFormattingOptions.FullyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::host(ComponentFormattingOptions a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#host

    Parameters
    ----------

    a0 : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.FullyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::host(ComponentFormattingOptions a0) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl4hostE6QFlagsINS_25ComponentFormattingOptionEE',
        a0.value,
    )

  @overload()
  @overload(int)
  def port(self, defaultPort: int = -1) -> int:
    """
    Calls Qt's 'int QUrl::port(int defaultPort) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#port

    Parameters
    ----------

    defaultPort : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QUrl::port(int defaultPort) const
    return self.uglySide.call('ritual_ZNK4QUrl4portEi', defaultPort)

  @overload()
  @overload(ComponentFormattingOptions)
  def path(
      self,
      options: ComponentFormattingOptions = (
          ComponentFormattingOptions.FullyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::path(ComponentFormattingOptions options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#path

    Parameters
    ----------

    options : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.FullyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::path(ComponentFormattingOptions options) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl4pathE6QFlagsINS_25ComponentFormattingOptionEE',
        options.value,
    )

  @overload()
  @overload(ComponentFormattingOptions)
  def fileName(
      self,
      options: ComponentFormattingOptions = (
          ComponentFormattingOptions.FullyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::fileName(ComponentFormattingOptions options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#fileName

    Parameters
    ----------

    options : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.FullyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::fileName(ComponentFormattingOptions options) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl8fileNameE6QFlagsINS_25ComponentFormattingOptionEE',
        options.value,
    )

  def hasQuery(self) -> bool:
    """
    Calls Qt's 'bool QUrl::hasQuery() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#hasQuery
    """
    #  bool QUrl::hasQuery() const
    return self.uglySide.call('ritual_ZNK4QUrl8hasQueryEv')

  @overload()
  @overload(ComponentFormattingOptions)
  def query(
      self,
      a0: ComponentFormattingOptions = (
          ComponentFormattingOptions.PrettyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::query(ComponentFormattingOptions a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#query

    Parameters
    ----------

    a0 : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.PrettyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::query(ComponentFormattingOptions a0) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl5queryE6QFlagsINS_25ComponentFormattingOptionEE',
        a0.value,
    )

  def hasFragment(self) -> bool:
    """
    Calls Qt's 'bool QUrl::hasFragment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#hasFragment
    """
    #  bool QUrl::hasFragment() const
    return self.uglySide.call('ritual_ZNK4QUrl11hasFragmentEv')

  @overload()
  @overload(ComponentFormattingOptions)
  def fragment(
      self,
      options: ComponentFormattingOptions = (
          ComponentFormattingOptions.PrettyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrl::fragment(ComponentFormattingOptions options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#fragment

    Parameters
    ----------

    options : ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ComponentFormattingOptions.PrettyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::fragment(ComponentFormattingOptions options) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl8fragmentE6QFlagsINS_25ComponentFormattingOptionEE',
        options.value,
    )

  @overload(THIS)
  def resolved(self, relative: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QUrl::resolved(const QUrl &relative) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#resolved

    Parameters
    ----------

    relative : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QUrl::resolved(const QUrl &relative) const
    address = self.uglySide.call(
        'ritual_ZNK4QUrl8resolvedERKS_', self._valueOf(relative),
    )
    return QUrl._cuteOwning(address)

  def isRelative(self) -> bool:
    """
    Calls Qt's 'bool QUrl::isRelative() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#isRelative
    """
    #  bool QUrl::isRelative() const
    return self.uglySide.call('ritual_ZNK4QUrl10isRelativeEv')

  @overload(THIS)
  def isParentOf(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QUrl::isParentOf(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#isParentOf

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QUrl::isParentOf(const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK4QUrl10isParentOfERKS_', self._valueOf(url),
    )

  def isLocalFile(self) -> bool:
    """
    Calls Qt's 'bool QUrl::isLocalFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#isLocalFile
    """
    #  bool QUrl::isLocalFile() const
    return self.uglySide.call('ritual_ZNK4QUrl11isLocalFileEv')

  def toLocalFile(self) -> str:
    """
    Calls Qt's 'QString QUrl::toLocalFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#toLocalFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrl::toLocalFile() const
    return self.uglySide.call('ritual_ZNK4QUrl11toLocalFileEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QUrl::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#isDetached
    """
    #  bool QUrl::isDetached() const
    return self.uglySide.call('ritual_ZNK4QUrl10isDetachedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, ParsingMode)
  def setUrl(
      self,
      url: str,
      mode: ParsingMode = ParsingMode.TolerantMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setUrl(const QString &url, ParsingMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setUrl

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.TolerantMode.
    """
    #  void QUrl::setUrl(const QString &url, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl6setUrlERK7QStringNS_11ParsingModeE', url, mode.value,
    )

  @overload(str)
  def setScheme(self, scheme: str) -> None:
    """
    Calls Qt's 'void QUrl::setScheme(const QString &scheme)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setScheme

    Parameters
    ----------

    scheme : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUrl::setScheme(const QString &scheme)
    self.uglySide.call('ritual_ZN4QUrl9setSchemeERK7QString', scheme)

  @overload(str)
  @overload(str, ParsingMode)
  def setAuthority(
      self,
      authority: str,
      mode: ParsingMode = ParsingMode.TolerantMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setAuthority(const QString &authority, ParsingMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setAuthority

    Parameters
    ----------

    authority : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.TolerantMode.
    """
    #  void QUrl::setAuthority(const QString &authority, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl12setAuthorityERK7QStringNS_11ParsingModeE',
        authority, mode.value,
    )

  @overload(str)
  @overload(str, ParsingMode)
  def setUserInfo(
      self,
      userInfo: str,
      mode: ParsingMode = ParsingMode.TolerantMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setUserInfo(const QString &userInfo, ParsingMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setUserInfo

    Parameters
    ----------

    userInfo : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.TolerantMode.
    """
    #  void QUrl::setUserInfo(const QString &userInfo, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl11setUserInfoERK7QStringNS_11ParsingModeE',
        userInfo, mode.value,
    )

  @overload(str)
  @overload(str, ParsingMode)
  def setUserName(
      self,
      userName: str,
      mode: ParsingMode = ParsingMode.DecodedMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setUserName(const QString &userName, ParsingMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setUserName

    Parameters
    ----------

    userName : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.DecodedMode.
    """
    #  void QUrl::setUserName(const QString &userName, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl11setUserNameERK7QStringNS_11ParsingModeE',
        userName, mode.value,
    )

  @overload(str)
  @overload(str, ParsingMode)
  def setPassword(
      self,
      password: str,
      mode: ParsingMode = ParsingMode.DecodedMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setPassword(const QString &password, ParsingMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.DecodedMode.
    """
    #  void QUrl::setPassword(const QString &password, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl11setPasswordERK7QStringNS_11ParsingModeE',
        password, mode.value,
    )

  @overload(str)
  @overload(str, ParsingMode)
  def setHost(
      self,
      host: str,
      mode: ParsingMode = ParsingMode.DecodedMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setHost(const QString &host, ParsingMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setHost

    Parameters
    ----------

    host : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.DecodedMode.
    """
    #  void QUrl::setHost(const QString &host, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl7setHostERK7QStringNS_11ParsingModeE',
        host, mode.value,
    )

  @overload(int)
  def setPort(self, port: int) -> None:
    """
    Calls Qt's 'void QUrl::setPort(int port)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QUrl::setPort(int port)
    self.uglySide.call('ritual_ZN4QUrl7setPortEi', port)

  @overload(str)
  @overload(str, ParsingMode)
  def setPath(
      self,
      path: str,
      mode: ParsingMode = ParsingMode.DecodedMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setPath(const QString &path, ParsingMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.DecodedMode.
    """
    #  void QUrl::setPath(const QString &path, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl7setPathERK7QStringNS_11ParsingModeE',
        path, mode.value,
    )

  @overload(str)
  @overload(str, ParsingMode)
  def setQuery(
      self,
      query: str,
      mode: ParsingMode = ParsingMode.TolerantMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setQuery(const QString &query, ParsingMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setQuery

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.TolerantMode.
    """
    #  void QUrl::setQuery(const QString &query, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl8setQueryERK7QStringNS_11ParsingModeE',
        query, mode.value,
    )

  @overload(str)
  @overload(str, ParsingMode)
  def setFragment(
      self,
      fragment: str,
      mode: ParsingMode = ParsingMode.TolerantMode,
  ) -> None:
    """
    Calls Qt's 'void QUrl::setFragment(const QString &fragment, ParsingMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#setFragment

    Parameters
    ----------

    fragment : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.TolerantMode.
    """
    #  void QUrl::setFragment(const QString &fragment, ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN4QUrl11setFragmentERK7QStringNS_11ParsingModeE',
        fragment, mode.value,
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
    Notes what was given, for Qt's 'QUrl::QUrl()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#QUrl
    """
    #  QUrl::QUrl()
    self._noteCreation(QUrl, lambda: Rituals.call('ritual_ZN4QUrlC1Ev'))

  @overload(THIS)
  def __init__(self, copy: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QUrl::QUrl(const QUrl &copy)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#QUrl

    Parameters
    ----------

    copy : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QUrl::QUrl(const QUrl &copy)
    self._noteCreation(QUrl, lambda: Rituals.call(
        'ritual_ZN4QUrlC1ERKS_', self._valueOf(copy),
    ))

  @overload(str)
  @overload(str, ParsingMode)
  def __init__(
      self,
      url: str,
      mode: ParsingMode = ParsingMode.TolerantMode,
  ) -> None:
    """
    Notes what was given, for Qt's 'QUrl::QUrl(const QString &url,
    ParsingMode mode)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#QUrl

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.

    mode : ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      ParsingMode.TolerantMode.
    """
    #  QUrl::QUrl(const QString &url, ParsingMode mode)
    self._noteCreation(QUrl, lambda: Rituals.call(
        'ritual_ZN4QUrlC1ERK7QStringNS_11ParsingModeE', url, mode.value,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QUrl::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#clear
    """
    #  void QUrl::clear()
    self.uglySide.call('ritual_ZN4QUrl5clearEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QUrl::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qurl.html#detach
    """
    #  void QUrl::detach()
    self.uglySide.call('ritual_ZN4QUrl6detachEv')
