"""
QQuickWebEngineProfilePrototype binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineprofileprototype_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineProfilePrototype to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..QtQml import QQmlParserStatus
from . import QQuickWebEngineProfile

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineProfilePrototype(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickWebEngineProfilePrototype: a plain Python
  object standing in front of one C++ QQuickWebEngineProfilePrototype.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineProfilePrototype
  is built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's
  QQuickWebEngineProfilePrototype is built on Qt's QQmlParserStatus too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineProfilePrototype that has a ritual
  and that Python can call so far, 21 names in all: 'metaObject', 'tr',
  'storageName', 'setStorageName', 'persistentStoragePath',
  'setPersistentStoragePath', 'cachePath', 'setCachePath', 'httpCacheType',
  'setHttpCacheType', 'persistentCookiesPolicy',
  'setPersistentCookiesPolicy', 'setHttpCacheMaximumSize',
  'httpCacheMaximumSize', 'persistentPermissionsPolicy',
  'setPersistentPermissionsPolicy', 'additionalTrustedCertificateFiles',
  'setAdditionalTrustedCertificateFiles', 'instance', 'componentComplete',
  'classBegin'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineProfilePrototype::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineProfilePrototype::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QQuickWebEngineProfilePrototype::~QQuickWebEngineProfilePrototype()':
    the destructor: Python never removes a C++
    QQuickWebEngineProfilePrototype.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineProfilePrototype is created at the first use, not
    by 'QQuickWebEngineProfilePrototype(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineProfilePrototype.
  - Qt tells when it has removed the C++ QQuickWebEngineProfilePrototype.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickWebEngineProfilePrototype::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#tr

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
    #  QString QQuickWebEngineProfilePrototype::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineProfilePrototype'

  #  Qt's QQuickWebEngineProfilePrototype is built on more than one class.
  #  The part of a C++ QQuickWebEngineProfilePrototype that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuickWebEngineProfilePrototype_QQmlParserStatus',
  }

  #  A C++ QQuickWebEngineProfilePrototype Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineProfilePrototype'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickWebEngineProfilePrototype::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineProfilePrototype::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def storageName(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfilePrototype::storageName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#storageName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfilePrototype::storageName() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype11storageNameEv',
    )

  def persistentStoragePath(self) -> str:
    """
    Calls Qt's 'QString
    QQuickWebEngineProfilePrototype::persistentStoragePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfilePrototype::persistentStoragePath() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype21persistentStoragePath'
        'Ev',
    )

  def cachePath(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfilePrototype::cachePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#cachePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfilePrototype::cachePath() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype9cachePathEv',
    )

  def httpCacheType(self) -> QQuickWebEngineProfile.HttpCacheType:
    """
    Calls Qt's 'QQuickWebEngineProfile::HttpCacheType
    QQuickWebEngineProfilePrototype::httpCacheType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#httpCacheType

    Returns
    -------

    QQuickWebEngineProfile.HttpCacheType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickWebEngineProfile.HttpCacheType(number)' gives.
    """
    #  QQuickWebEngineProfile::HttpCacheType
    #      QQuickWebEngineProfilePrototype::httpCacheType() const
    return QQuickWebEngineProfile.HttpCacheType(self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype13httpCacheTypeEv',
    ))

  def persistentCookiesPolicy(
      self,
  ) -> QQuickWebEngineProfile.PersistentCookiesPolicy:
    """
    Calls Qt's 'QQuickWebEngineProfile::PersistentCookiesPolicy
    QQuickWebEngineProfilePrototype::persistentCookiesPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Returns
    -------

    QQuickWebEngineProfile.PersistentCookiesPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickWebEngineProfile.PersistentCookiesPolicy(number)' gives.
    """
    #  QQuickWebEngineProfile::PersistentCookiesPolicy
    #      QQuickWebEngineProfilePrototype::persistentCookiesPolicy() const
    return QQuickWebEngineProfile.PersistentCookiesPolicy(self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype23persistentCookiesPoli'
        'cyEv',
    ))

  def httpCacheMaximumSize(self) -> int:
    """
    Calls Qt's 'int QQuickWebEngineProfilePrototype::httpCacheMaximumSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html
    """
    #  int QQuickWebEngineProfilePrototype::httpCacheMaximumSize() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype20httpCacheMaximumSizeE'
        'v',
    )

  def persistentPermissionsPolicy(
      self,
  ) -> QQuickWebEngineProfile.PersistentPermissionsPolicy:
    """
    Calls Qt's 'QQuickWebEngineProfile::PersistentPermissionsPolicy
    QQuickWebEngineProfilePrototype::persistentPermissionsPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Returns
    -------

    QQuickWebEngineProfile.PersistentPermissionsPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickWebEngineProfile.PersistentPermissionsPolicy(number)' gives.
    """
    #  QQuickWebEngineProfile::PersistentPermissionsPolicy
    #      QQuickWebEngineProfilePrototype::persistentPermissionsPolicy()
    #      const
    return QQuickWebEngineProfile.PersistentPermissionsPolicy(
        self.uglySide.call(
            'ritual_ZNK31QQuickWebEngineProfilePrototype27persistentPermiss'
            'ionsPolicyEv',
        ))

  def additionalTrustedCertificateFiles(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QQuickWebEngineProfilePrototype::additionalTrustedCertificateFiles()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickWebEngineProfilePrototype::
    #      additionalTrustedCertificateFiles() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineProfilePrototype33additionalTrustedCert'
        'ificateFilesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setStorageName(self, storageName: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfilePrototype::setStorageName(const
    QString &storageName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    storageName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfilePrototype::setStorageName(const QString
    #      &storageName)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype14setStorageNameERK7QStr'
        'ing',
        storageName,
    )

  @overload(str)
  def setPersistentStoragePath(self, path: str) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfilePrototype::setPersistentStoragePath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfilePrototype::setPersistentStoragePath(const
    #      QString &path)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype24setPersistentStoragePa'
        'thERK7QString',
        path,
    )

  @overload(str)
  def setCachePath(self, path: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfilePrototype::setCachePath(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#setCachePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfilePrototype::setCachePath(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype12setCachePathERK7QStrin'
        'g',
        path,
    )

  @overload(QQuickWebEngineProfile.HttpCacheType)
  def setHttpCacheType(
      self,
      httpCacheType: QQuickWebEngineProfile.HttpCacheType,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfilePrototype::setHttpCacheType(
    QQuickWebEngineProfile::HttpCacheType httpCacheType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    httpCacheType : QQuickWebEngineProfile.HttpCacheType
      Passed on as its number.
    """
    #  void QQuickWebEngineProfilePrototype::setHttpCacheType(
    #      QQuickWebEngineProfile::HttpCacheType httpCacheType)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype16setHttpCacheTypeEN22QQ'
        'uickWebEngineProfile13HttpCacheTypeE',
        httpCacheType.value,
    )

  @overload(QQuickWebEngineProfile.PersistentCookiesPolicy)
  def setPersistentCookiesPolicy(
      self,
      persistentCookiesPolicy: QQuickWebEngineProfile.PersistentCookiesPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfilePrototype::setPersistentCookiesPolicy(
    QQuickWebEngineProfile::PersistentCookiesPolicy
    persistentCookiesPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    persistentCookiesPolicy : QQuickWebEngineProfile.PersistentCookiesPolicy
      Passed on as its number.
    """
    #  void QQuickWebEngineProfilePrototype::setPersistentCookiesPolicy(
    #      QQuickWebEngineProfile::PersistentCookiesPolicy
    #      persistentCookiesPolicy)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype26setPersistentCookiesPo'
        'licyEN22QQuickWebEngineProfile23PersistentCookiesPolicyE',
        persistentCookiesPolicy.value,
    )

  @overload(int)
  def setHttpCacheMaximumSize(self, maxSizeInBytes: int) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfilePrototype::setHttpCacheMaximumSize(int
    maxSizeInBytes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    maxSizeInBytes : int
      Passed on as it is.
    """
    #  void QQuickWebEngineProfilePrototype::setHttpCacheMaximumSize(int
    #      maxSizeInBytes)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype23setHttpCacheMaximumSiz'
        'eEi',
        maxSizeInBytes,
    )

  @overload(QQuickWebEngineProfile.PersistentPermissionsPolicy)
  def setPersistentPermissionsPolicy(
      self,
      persistentPermissionsPolicy: QQuickWebEngineProfile.PersistentPermissionsPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfilePrototype::setPersistentPermissionsPolicy(
    QQuickWebEngineProfile::PersistentPermissionsPolicy
    persistentPermissionsPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    persistentPermissionsPolicy : QQuickWebEngineProfile.PersistentPermissionsPolicy
      Passed on as its number.
    """
    #  void QQuickWebEngineProfilePrototype::setPersistentPermissionsPolicy(
    #      QQuickWebEngineProfile::PersistentPermissionsPolicy
    #      persistentPermissionsPolicy)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype30setPersistentPermissio'
        'nsPolicyEN22QQuickWebEngineProfile27PersistentPermissionsPolicyE',
        persistentPermissionsPolicy.value,
    )

  @overload(QStringList)
  def setAdditionalTrustedCertificateFiles(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfilePrototype::setAdditionalTrustedCertificateFiles(
    const QStringList &paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickWebEngineProfilePrototype::
    #      setAdditionalTrustedCertificateFiles(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype36setAdditionalTrustedCe'
        'rtificateFilesERK5QListI7QStringE',
        self._valueOf(paths),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineProfilePrototype::QQuickWebEngineProfilePrototype(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWebEngineProfilePrototype::QQuickWebEngineProfilePrototype(
    #      QObject *parent)
    self._noteCreation(QQuickWebEngineProfilePrototype, lambda: Rituals.call(
        'ritual_ZN31QQuickWebEngineProfilePrototypeC1EP7QObject',
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

  def instance(self) -> Optional[QQuickWebEngineProfile]:
    """
    Calls Qt's 'QQuickWebEngineProfile
    *QQuickWebEngineProfilePrototype::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#instance

    Returns
    -------

    Optional[QQuickWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineProfile *QQuickWebEngineProfilePrototype::instance()
    address = self.uglySide.call(
        'ritual_ZN31QQuickWebEngineProfilePrototype8instanceEv',
    )
    return QQuickWebEngineProfile._cuteAt(address)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfilePrototype::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html
    """
    #  void QQuickWebEngineProfilePrototype::componentComplete()
    ritual = (
        'ritual_ZN31QQuickWebEngineProfilePrototype17componentCompleteEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQuickWebEngineProfilePrototype17componentComplet'
          'eEv')
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfilePrototype::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofileprototype.html#classBegin
    """
    #  void QQuickWebEngineProfilePrototype::classBegin()
    ritual = 'ritual_ZN31QQuickWebEngineProfilePrototype10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN31QQuickWebEngineProfilePrototype10classBeginEv'
    self.uglySide.call(ritual)
