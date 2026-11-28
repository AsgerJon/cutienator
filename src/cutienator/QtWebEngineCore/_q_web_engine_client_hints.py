"""
QWebEngineClientHints binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineclienthints.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineClientHints(QObject):
  """
  The cute side of Qt's QWebEngineClientHints: a plain Python object standing
  in front of one C++ QWebEngineClientHints.

  It is built on the cute 'QObject', as Qt's QWebEngineClientHints is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineClientHints that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'arch',
  'platform', 'model', 'isMobile', 'fullVersion', 'platformVersion',
  'bitness', 'fullVersionList', 'isWow64', 'formFactors', 'setArch',
  'setPlatform', 'setModel', 'setIsMobile', 'setFullVersion',
  'setPlatformVersion', 'setBitness', 'setFullVersionList', 'setIsWow64',
  'setFormFactors', 'isAllClientHintsEnabled', 'setAllClientHintsEnabled',
  'resetAll'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineClientHints::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWebEngineClientHints::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineClientHints::~QWebEngineClientHints()': the destructor:
    Python never removes a C++ QWebEngineClientHints.
  - Qt's 'QWebEngineClientHints::QWebEngineClientHints(QtWebEngineCore::
    ProfileAdapter *profileAdapter)': names
    'QtWebEngineCore::ProfileAdapter', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineClientHints is created at the first use, not by
    'QWebEngineClientHints(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineClientHints.
  - Qt tells when it has removed the C++ QWebEngineClientHints. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineClientHints that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QWebEngineClientHints::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineclienthints.html#tr

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
    #  QString QWebEngineClientHints::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QWebEngineClientHints2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineClientHints'

  #  A C++ QWebEngineClientHints Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineClientHints'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineClientHints::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineClientHints::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineClientHints10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def arch(self) -> str:
    """
    Calls Qt's 'QString QWebEngineClientHints::arch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineclienthints.html#arch

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineClientHints::arch() const
    return self.uglySide.call('ritual_ZNK21QWebEngineClientHints4archEv')

  def platform(self) -> str:
    """
    Calls Qt's 'QString QWebEngineClientHints::platform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#platform

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineClientHints::platform() const
    return self.uglySide.call('ritual_ZNK21QWebEngineClientHints8platformEv')

  def model(self) -> str:
    """
    Calls Qt's 'QString QWebEngineClientHints::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineclienthints.html#model

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineClientHints::model() const
    return self.uglySide.call('ritual_ZNK21QWebEngineClientHints5modelEv')

  def isMobile(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineClientHints::isMobile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#isMobile
    """
    #  bool QWebEngineClientHints::isMobile() const
    return self.uglySide.call('ritual_ZNK21QWebEngineClientHints8isMobileEv')

  def fullVersion(self) -> str:
    """
    Calls Qt's 'QString QWebEngineClientHints::fullVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#fullVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineClientHints::fullVersion() const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineClientHints11fullVersionEv',
    )

  def platformVersion(self) -> str:
    """
    Calls Qt's 'QString QWebEngineClientHints::platformVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#platformVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineClientHints::platformVersion() const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineClientHints15platformVersionEv',
    )

  def bitness(self) -> str:
    """
    Calls Qt's 'QString QWebEngineClientHints::bitness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineclienthints.html#bitness

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineClientHints::bitness() const
    return self.uglySide.call('ritual_ZNK21QWebEngineClientHints7bitnessEv')

  def fullVersionList(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QWebEngineClientHints::fullVersionList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#fullVersionList

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QWebEngineClientHints::fullVersionList() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineClientHints15fullVersionListEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def isWow64(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineClientHints::isWow64() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineclienthints.html#isWow64
    """
    #  bool QWebEngineClientHints::isWow64() const
    return self.uglySide.call('ritual_ZNK21QWebEngineClientHints7isWow64Ev')

  def formFactors(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebEngineClientHints::formFactors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#formFactors

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebEngineClientHints::formFactors() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineClientHints11formFactorsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setArch(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setArch(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineclienthints.html#setArch

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineClientHints::setArch(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints7setArchERK7QString', a0,
    )

  @overload(str)
  def setPlatform(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setPlatform(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setPlatform

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineClientHints::setPlatform(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints11setPlatformERK7QString', a0,
    )

  @overload(str)
  def setModel(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setModel(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setModel

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineClientHints::setModel(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints8setModelERK7QString', a0,
    )

  @overload(bool)
  def setIsMobile(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setIsMobile(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setIsMobile

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWebEngineClientHints::setIsMobile(bool a0)
    self.uglySide.call('ritual_ZN21QWebEngineClientHints11setIsMobileEb', a0)

  @overload(str)
  def setFullVersion(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setFullVersion(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setFullVersion

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineClientHints::setFullVersion(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints14setFullVersionERK7QString', a0,
    )

  @overload(str)
  def setPlatformVersion(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setPlatformVersion(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setPlatformVersion

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineClientHints::setPlatformVersion(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints18setPlatformVersionERK7QString',
        a0,
    )

  @overload(str)
  def setBitness(self, a0: str) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setBitness(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setBitness

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineClientHints::setBitness(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints10setBitnessERK7QString', a0,
    )

  @overload(QMap[str, QVariant])
  def setFullVersionList(self, a0: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setFullVersionList(const
    QVariantMap &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setFullVersionList

    Parameters
    ----------

    a0 : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QWebEngineClientHints::setFullVersionList(const QVariantMap &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints18setFullVersionListERK4QMapI7QStr'
        'ing8QVariantE',
        self._valueOf(a0),
    )

  @overload(bool)
  def setIsWow64(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setIsWow64(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setIsWow64

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWebEngineClientHints::setIsWow64(bool a0)
    self.uglySide.call('ritual_ZN21QWebEngineClientHints10setIsWow64Eb', a0)

  @overload(QStringList)
  def setFormFactors(self, a0: QStringList) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setFormFactors(const QStringList
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#setFormFactors

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebEngineClientHints::setFormFactors(const QStringList &a0)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints14setFormFactorsERK5QListI7QString'
        'E',
        self._valueOf(a0),
    )

  @overload(bool)
  def setAllClientHintsEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::setAllClientHintsEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWebEngineClientHints::setAllClientHintsEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints24setAllClientHintsEnabledEb',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebEngineClientHints::QWebEngineClientHints(QtWebEngineCore::
    ProfileAdapter *profileAdapter)': names
    'QtWebEngineCore::ProfileAdapter', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineClientHints.__init__' has no cute function yet. Qt's "
        "'QWebEngineClientHints::QWebEngineClientHints(QtWebEngineCore::Prof"
        "ileAdapter *profileAdapter)': names "
        "'QtWebEngineCore::ProfileAdapter', which has no cute class yet.")

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

  def isAllClientHintsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineClientHints::isAllClientHintsEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#isAllClientHintsEnabled
    """
    #  bool QWebEngineClientHints::isAllClientHintsEnabled()
    return self.uglySide.call(
        'ritual_ZN21QWebEngineClientHints23isAllClientHintsEnabledEv',
    )

  def resetAll(self) -> None:
    """
    Calls Qt's 'void QWebEngineClientHints::resetAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclienthints.html#resetAll
    """
    #  void QWebEngineClientHints::resetAll()
    self.uglySide.call('ritual_ZN21QWebEngineClientHints8resetAllEv')
