"""
QQuickWebViewSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebviewsettings_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebViewSettings to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWebView import QWebViewSettings
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebViewSettings = WAIT['QWebViewSettings']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebViewSettings(QObject):
  """
  The cute side of Qt's QQuickWebViewSettings: a plain Python object standing
  in front of one C++ QQuickWebViewSettings.

  It is built on the cute 'QObject', as Qt's QQuickWebViewSettings is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebViewSettings that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr',
  'localStorageEnabled', 'javaScriptEnabled',
  'localContentCanAccessFileUrls', 'allowFileAccess',
  'setLocalStorageEnabled', 'setJavaScriptEnabled', 'setAllowFileAccess',
  'setLocalContentCanAccessFileUrls', 'localStorageEnabledChanged',
  'javaScriptEnabledChanged', 'allowFileAccessChanged',
  'localContentCanAccessFileUrlsChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebViewSettings::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWebViewSettings::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebViewSettings::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickWebViewSettings::~QQuickWebViewSettings()': the destructor:
    Python never removes a C++ QQuickWebViewSettings.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebViewSettings is created at the first use, not by
    'QQuickWebViewSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebViewSettings.
  - Qt tells when it has removed the C++ QQuickWebViewSettings. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickWebViewSettings::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebviewsettings.html#tr

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
    #  QString QQuickWebViewSettings::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickWebViewSettings2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebViewSettings'

  #  A C++ QQuickWebViewSettings Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebViewSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebViewSettings::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebViewSettings::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickWebViewSettings10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def localStorageEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebViewSettings::localStorageEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#localStorageEnabled
    """
    #  bool QQuickWebViewSettings::localStorageEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickWebViewSettings19localStorageEnabledEv',
    )

  def javaScriptEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebViewSettings::javaScriptEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#javaScriptEnabled
    """
    #  bool QQuickWebViewSettings::javaScriptEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickWebViewSettings17javaScriptEnabledEv',
    )

  def localContentCanAccessFileUrls(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebViewSettings::localContentCanAccessFileUrls()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html
    """
    #  bool QQuickWebViewSettings::localContentCanAccessFileUrls() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickWebViewSettings29localContentCanAccessFileUrlsEv',
    )

  def allowFileAccess(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebViewSettings::allowFileAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#allowFileAccess
    """
    #  bool QQuickWebViewSettings::allowFileAccess() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickWebViewSettings15allowFileAccessEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setLocalStorageEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickWebViewSettings::setLocalStorageEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#setLocalStorageEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickWebViewSettings::setLocalStorageEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings22setLocalStorageEnabledEb',
        enabled,
    )

  @overload(bool)
  def setJavaScriptEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickWebViewSettings::setJavaScriptEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#setJavaScriptEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickWebViewSettings::setJavaScriptEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings20setJavaScriptEnabledEb', enabled,
    )

  @overload(bool)
  def setAllowFileAccess(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickWebViewSettings::setAllowFileAccess(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#setAllowFileAccess

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickWebViewSettings::setAllowFileAccess(bool enabled)
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings18setAllowFileAccessEb', enabled,
    )

  @overload(bool)
  def setLocalContentCanAccessFileUrls(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebViewSettings::setLocalContentCanAccessFileUrls(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickWebViewSettings::setLocalContentCanAccessFileUrls(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings32setLocalContentCanAccessFileUrls'
        'Eb',
        enabled,
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

  @overload(QWebViewSettings)
  @overload(NoneType)
  def __init__(self, webviewsettings: Optional[QWebViewSettings]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebViewSettings::QQuickWebViewSettings(QWebViewSettings
    *webviewsettings)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#QQuickWebViewSettings

    Parameters
    ----------

    webviewsettings : Optional[QWebViewSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWebViewSettings::QQuickWebViewSettings(QWebViewSettings
    #      *webviewsettings)
    self._noteCreation(QQuickWebViewSettings, lambda: Rituals.call(
        'ritual_ZN21QQuickWebViewSettingsC1EP16QWebViewSettings',
        self._addressOf(webviewsettings),
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

  def localStorageEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebViewSettings::localStorageEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html
    """
    #  void QQuickWebViewSettings::localStorageEnabledChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings26localStorageEnabledChangedEv',
    )

  def javaScriptEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebViewSettings::javaScriptEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html
    """
    #  void QQuickWebViewSettings::javaScriptEnabledChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings24javaScriptEnabledChangedEv',
    )

  def allowFileAccessChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebViewSettings::allowFileAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html#allowFileAccessChanged
    """
    #  void QQuickWebViewSettings::allowFileAccessChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings22allowFileAccessChangedEv',
    )

  def localContentCanAccessFileUrlsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebViewSettings::localContentCanAccessFileUrlsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewsettings.html
    """
    #  void QQuickWebViewSettings::localContentCanAccessFileUrlsChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickWebViewSettings36localContentCanAccessFileUrlsCha'
        'ngedEv',
    )
