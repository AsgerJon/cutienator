"""
QWebEngineProfileBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineprofilebuilder.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QWebEngineProfile

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineProfileBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineProfileBuilder: a plain Python object
  standing in front of one C++ QWebEngineProfileBuilder.

  What exists
  -----------

  Every function of Qt's QWebEngineProfileBuilder that has a ritual and that
  Python can call so far, 2 names in all: 'createProfile',
  'createOffTheRecordProfile'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineProfileBuilder::~QWebEngineProfileBuilder()': the
    destructor: Python never removes a C++ QWebEngineProfileBuilder.
  - Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setPersistentStoragePath(const QString
    &path)': gives a type Python has no way to take yet.
  - Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setCachePath(const QString &path)': gives a
    type Python has no way to take yet.
  - Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setHttpCacheType(QWebEngineProfile::
    HttpCacheType httpCacheType)': gives a type Python has no way to take
    yet.
  - Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setPersistentCookiesPolicy(
    QWebEngineProfile::PersistentCookiesPolicy persistentCookiesPolicy)':
    gives a type Python has no way to take yet.
  - Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setHttpCacheMaximumSize(int maxSizeInBytes)':
    gives a type Python has no way to take yet.
  - Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setPersistentPermissionsPolicy(
    QWebEngineProfile::PersistentPermissionsPolicy
    persistentPermissionPolicy)': gives a type Python has no way to take yet.
  - Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setAdditionalTrustedCertificates(const
    QList<QSslCertificate> &additionalTrustedCertificates)': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineProfileBuilder is created at the first use, not by
    'QWebEngineProfileBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineProfileBuilder.
  - Each name of Qt's QWebEngineProfileBuilder that has no cute function yet,
    'setAdditionalTrustedCertificates', 'setCachePath',
    'setHttpCacheMaximumSize', 'setHttpCacheType',
    'setPersistentCookiesPolicy', 'setPersistentPermissionsPolicy',
    'setPersistentStoragePath', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  @overload(QObject)
  @overload(NoneType)
  def createOffTheRecordProfile(
      parent: Optional[QObject] = None,
  ) -> Optional[QWebEngineProfile]:
    """
    Calls Qt's 'QWebEngineProfile
    *QWebEngineProfileBuilder::createOffTheRecordProfile(QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofilebuilder.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineProfile
    #      *QWebEngineProfileBuilder::createOffTheRecordProfile(QObject
    #      *parent)
    address = Rituals.call(
        'ritual_ZN24QWebEngineProfileBuilder25createOffTheRecordProfileEP7Q'
        'Object',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QWebEngineProfile._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineProfileBuilder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def createProfile(
      self,
      storageName: str,
      parent: Optional[QObject] = None,
  ) -> Optional[QWebEngineProfile]:
    """
    Calls Qt's 'QWebEngineProfile
    *QWebEngineProfileBuilder::createProfile(const QString &storageName,
    QObject *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofilebuilder.html#createProfile

    Parameters
    ----------

    storageName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineProfile *QWebEngineProfileBuilder::createProfile(const
    #      QString &storageName, QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineProfileBuilder13createProfileERK7QStringP7QO'
        'bject',
        storageName, self._addressOf(parent, 'QObject'),
    )
    return QWebEngineProfile._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QWebEngineProfileBuilder::QWebEngineProfileBuilder()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofilebuilder.html
    """
    #  QWebEngineProfileBuilder::QWebEngineProfileBuilder()
    self._noteCreation(QWebEngineProfileBuilder, lambda: Rituals.call(
        'ritual_ZN24QWebEngineProfileBuilderC1Ev',
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

  @staticmethod
  def setAdditionalTrustedCertificates(*__, **_) -> Never:
    """
    Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setAdditionalTrustedCertificates(const
    QList<QSslCertificate> &additionalTrustedCertificates)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfileBuilder.setAdditionalTrustedCertificates' has no "
        "cute function yet. Qt's 'QWebEngineProfileBuilder "
        "&QWebEngineProfileBuilder::setAdditionalTrustedCertificates(const "
        "QList<QSslCertificate> &additionalTrustedCertificates)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setCachePath(*__, **_) -> Never:
    """
    Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setCachePath(const QString &path)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfileBuilder.setCachePath' has no cute function yet. "
        "Qt's 'QWebEngineProfileBuilder "
        "&QWebEngineProfileBuilder::setCachePath(const QString &path)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setHttpCacheMaximumSize(*__, **_) -> Never:
    """
    Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setHttpCacheMaximumSize(int maxSizeInBytes)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfileBuilder.setHttpCacheMaximumSize' has no cute "
        "function yet. Qt's 'QWebEngineProfileBuilder "
        "&QWebEngineProfileBuilder::setHttpCacheMaximumSize(int "
        "maxSizeInBytes)': gives a type Python has no way to take yet.")

  @staticmethod
  def setHttpCacheType(*__, **_) -> Never:
    """
    Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setHttpCacheType(QWebEngineProfile::
    HttpCacheType httpCacheType)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfileBuilder.setHttpCacheType' has no cute function "
        "yet. Qt's 'QWebEngineProfileBuilder "
        "&QWebEngineProfileBuilder::setHttpCacheType(QWebEngineProfile::Http"
        "CacheType httpCacheType)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def setPersistentCookiesPolicy(*__, **_) -> Never:
    """
    Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setPersistentCookiesPolicy(
    QWebEngineProfile::PersistentCookiesPolicy persistentCookiesPolicy)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfileBuilder.setPersistentCookiesPolicy' has no cute "
        "function yet. Qt's 'QWebEngineProfileBuilder "
        "&QWebEngineProfileBuilder::setPersistentCookiesPolicy(QWebEnginePro"
        "file::PersistentCookiesPolicy persistentCookiesPolicy)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setPersistentPermissionsPolicy(*__, **_) -> Never:
    """
    Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setPersistentPermissionsPolicy(
    QWebEngineProfile::PersistentPermissionsPolicy
    persistentPermissionPolicy)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfileBuilder.setPersistentPermissionsPolicy' has no "
        "cute function yet. Qt's 'QWebEngineProfileBuilder "
        "&QWebEngineProfileBuilder::setPersistentPermissionsPolicy(QWebEngin"
        "eProfile::PersistentPermissionsPolicy "
        "persistentPermissionPolicy)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def setPersistentStoragePath(*__, **_) -> Never:
    """
    Qt's 'QWebEngineProfileBuilder
    &QWebEngineProfileBuilder::setPersistentStoragePath(const QString
    &path)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfileBuilder.setPersistentStoragePath' has no cute "
        "function yet. Qt's 'QWebEngineProfileBuilder "
        "&QWebEngineProfileBuilder::setPersistentStoragePath(const QString "
        "&path)': gives a type Python has no way to take yet.")
