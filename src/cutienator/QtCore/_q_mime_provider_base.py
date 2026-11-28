"""
QMimeProviderBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimeprovider_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeProviderBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMimeProviderBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeProviderBase: a plain Python object standing in
  front of one C++ QMimeProviderBase.

  What exists
  -----------

  Every function of Qt's QMimeProviderBase that has a ritual and that Python
  can call so far, 13 names in all: 'isValid', 'isInternalDatabase',
  'knowsMimeType', 'resolveAlias', 'hasGlobDeleteAll', 'globPatterns',
  'icon', 'genericIcon', 'ensureLoaded', 'directory', 'overrideProvider',
  'setOverrideProvider', 'isMimeTypeGlobsExcluded'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMimeProviderBase::~QMimeProviderBase()': the destructor: Python
    never removes a C++ QMimeProviderBase.
  - Qt's 'void QMimeProviderBase::addFileNameMatches(const QString &fileName,
    QMimeGlobMatchResult &result)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QMimeProviderBase::addParents(const QString &mime, QStringList
    &result)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMimeProviderBase::addAliases(const QString &name, QStringList
    &result)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMimeProviderBase::findByMagic(const QByteArray &data,
    QMimeMagicResult &result)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QMimeProviderBase::addAllMimeTypes(QList<QMimeType> &result)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMimeTypePrivate::LocaleHash
    QMimeProviderBase::localeComments(const QString &name)': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 2 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QMimeProviderBase is created at the first use, not by
    'QMimeProviderBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeProviderBase.
  - Each name of Qt's QMimeProviderBase that has no cute function yet,
    '__init__', 'addAliases', 'addAllMimeTypes', 'addFileNameMatches',
    'addParents', 'findByMagic', 'localeComments', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeProviderBase'

  #  A C++ QMimeProviderBase Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMimeProviderBase'

  #  The functions Qt calls itself that QMimeProviderBase is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'addFileNameMatches': (
          'void QMimeProviderBase::addFileNameMatches(const QString &, '
          'QMimeGlobMatchResult &)',
      ),
      'addParents': (
          'void QMimeProviderBase::addParents(const QString &, QStringList '
          '&)',
      ),
      'addAliases': (
          'void QMimeProviderBase::addAliases(const QString &, QStringList '
          '&)',
      ),
      'findByMagic': (
          'void QMimeProviderBase::findByMagic(const QByteArray &, '
          'QMimeMagicResult &)',
      ),
      'addAllMimeTypes': (
          'void QMimeProviderBase::addAllMimeTypes(QList<QMimeType> &)',
      ),
      'localeComments': (
          'QMimeTypePrivate::LocaleHash '
          'QMimeProviderBase::localeComments(const QString &)',
      ),
      'globPatterns': (
          'QStringList QMimeProviderBase::globPatterns(const QString &)',
      ),
  }

  #  The functions Qt calls itself that QMimeProviderBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isValid': (
          ('_ZN17QMimeProviderBase7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isInternalDatabase': (
          ('_ZNK17QMimeProviderBase18isInternalDatabaseEv',
           ('bool', 'number', ''),
           ()),
      ),
      'knowsMimeType': (
          ('_ZN17QMimeProviderBase13knowsMimeTypeERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'resolveAlias': (
          ('_ZN17QMimeProviderBase12resolveAliasERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'hasGlobDeleteAll': (
          ('_ZN17QMimeProviderBase16hasGlobDeleteAllERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'icon': (
          ('_ZN17QMimeProviderBase4iconERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'genericIcon': (
          ('_ZN17QMimeProviderBase11genericIconERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'ensureLoaded': (
          ('_ZN17QMimeProviderBase12ensureLoadedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInternalDatabase(self) -> bool:
    """
    Calls Qt's 'bool QMimeProviderBase::isInternalDatabase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#isInternalDatabase
    """
    #  bool QMimeProviderBase::isInternalDatabase() const
    return self.uglySide.call(
        'ritual_ZNK17QMimeProviderBase18isInternalDatabaseEv',
    )

  def directory(self) -> str:
    """
    Calls Qt's 'QString QMimeProviderBase::directory() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeproviderbase.html#directory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeProviderBase::directory() const
    return self.uglySide.call('ritual_ZNK17QMimeProviderBase9directoryEv')

  def overrideProvider(self) -> Optional[QMimeProviderBase]:
    """
    Calls Qt's 'QMimeProviderBase *QMimeProviderBase::overrideProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#overrideProvider

    Returns
    -------

    Optional[QMimeProviderBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeProviderBase *QMimeProviderBase::overrideProvider() const
    address = self.uglySide.call(
        'ritual_ZNK17QMimeProviderBase16overrideProviderEv',
    )
    return QMimeProviderBase._cuteAt(address)

  @overload(str)
  def isMimeTypeGlobsExcluded(self, name: str) -> bool:
    """
    Calls Qt's 'bool QMimeProviderBase::isMimeTypeGlobsExcluded(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#isMimeTypeGlobsExcluded

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeProviderBase::isMimeTypeGlobsExcluded(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QMimeProviderBase23isMimeTypeGlobsExcludedERK7QString',
        name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setOverrideProvider(
      self,
      provider: Optional[QMimeProviderBase],
  ) -> None:
    """
    Calls Qt's 'void QMimeProviderBase::setOverrideProvider(QMimeProviderBase
    *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#setOverrideProvider

    Parameters
    ----------

    provider : Optional[QMimeProviderBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMimeProviderBase::setOverrideProvider(QMimeProviderBase
    #      *provider)
    self.uglySide.call(
        'ritual_ZN17QMimeProviderBase19setOverrideProviderEPS_',
        self._addressOf(provider),
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
    Qt's 'QMimeProviderBase::QMimeProviderBase(QMimeDatabasePrivate *db,
    const QString &directory)': the class is abstract, so C++ cannot make
    one, and the C++ class of ours does not fill in every function it leaves
    open.
    """
    raise NotImplementedError(
        "'QMimeProviderBase.__init__' has no cute function yet. Qt's "
        "'QMimeProviderBase::QMimeProviderBase(QMimeDatabasePrivate *db, "
        "const QString &directory)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMimeProviderBase::isValid()'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeproviderbase.html#isValid
    """
    #  bool QMimeProviderBase::isValid()
    return self.uglySide.call('ritual_ZN17QMimeProviderBase7isValidEv')

  @overload(str)
  def knowsMimeType(self, name: str) -> bool:
    """
    Calls Qt's 'bool QMimeProviderBase::knowsMimeType(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#knowsMimeType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeProviderBase::knowsMimeType(const QString &name)
    return self.uglySide.call(
        'ritual_ZN17QMimeProviderBase13knowsMimeTypeERK7QString', name,
    )

  @overload(str)
  def resolveAlias(self, name: str) -> str:
    """
    Calls Qt's 'QString QMimeProviderBase::resolveAlias(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#resolveAlias

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeProviderBase::resolveAlias(const QString &name)
    return self.uglySide.call(
        'ritual_ZN17QMimeProviderBase12resolveAliasERK7QString', name,
    )

  @overload(str)
  def hasGlobDeleteAll(self, name: str) -> bool:
    """
    Calls Qt's 'bool QMimeProviderBase::hasGlobDeleteAll(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#hasGlobDeleteAll

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeProviderBase::hasGlobDeleteAll(const QString &name)
    return self.uglySide.call(
        'ritual_ZN17QMimeProviderBase16hasGlobDeleteAllERK7QString', name,
    )

  @overload(str)
  def globPatterns(self, name: str) -> QStringList:
    """
    Calls Qt's 'QStringList QMimeProviderBase::globPatterns(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#globPatterns

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QMimeProviderBase::globPatterns(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN17QMimeProviderBase12globPatternsERK7QString', name,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def icon(self, name: str) -> str:
    """
    Calls Qt's 'QString QMimeProviderBase::icon(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeproviderbase.html#icon

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeProviderBase::icon(const QString &name)
    return self.uglySide.call(
        'ritual_ZN17QMimeProviderBase4iconERK7QString', name,
    )

  @overload(str)
  def genericIcon(self, name: str) -> str:
    """
    Calls Qt's 'QString QMimeProviderBase::genericIcon(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeproviderbase.html#genericIcon

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeProviderBase::genericIcon(const QString &name)
    return self.uglySide.call(
        'ritual_ZN17QMimeProviderBase11genericIconERK7QString', name,
    )

  def ensureLoaded(self) -> None:
    """
    Calls Qt's 'void QMimeProviderBase::ensureLoaded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeproviderbase.html#ensureLoaded
    """
    #  void QMimeProviderBase::ensureLoaded()
    ritual = 'ritual_ZN17QMimeProviderBase12ensureLoadedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QMimeProviderBase12ensureLoadedEv'
    self.uglySide.call(ritual)

  @staticmethod
  def addAliases(*__, **_) -> Never:
    """
    Qt's 'void QMimeProviderBase::addAliases(const QString &name, QStringList
    &result)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeProviderBase.addAliases' has no cute function yet. Qt's "
        "'void QMimeProviderBase::addAliases(const QString &name, "
        "QStringList &result)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def addAllMimeTypes(*__, **_) -> Never:
    """
    Qt's 'void QMimeProviderBase::addAllMimeTypes(QList<QMimeType> &result)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeProviderBase.addAllMimeTypes' has no cute function yet. Qt's "
        "'void QMimeProviderBase::addAllMimeTypes(QList<QMimeType> "
        "&result)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def addFileNameMatches(*__, **_) -> Never:
    """
    Qt's 'void QMimeProviderBase::addFileNameMatches(const QString &fileName,
    QMimeGlobMatchResult &result)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QMimeProviderBase.addFileNameMatches' has no cute function yet. "
        "Qt's 'void QMimeProviderBase::addFileNameMatches(const QString "
        "&fileName, QMimeGlobMatchResult &result)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def addParents(*__, **_) -> Never:
    """
    Qt's 'void QMimeProviderBase::addParents(const QString &mime, QStringList
    &result)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeProviderBase.addParents' has no cute function yet. Qt's "
        "'void QMimeProviderBase::addParents(const QString &mime, "
        "QStringList &result)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def findByMagic(*__, **_) -> Never:
    """
    Qt's 'void QMimeProviderBase::findByMagic(const QByteArray &data,
    QMimeMagicResult &result)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QMimeProviderBase.findByMagic' has no cute function yet. Qt's "
        "'void QMimeProviderBase::findByMagic(const QByteArray &data, "
        "QMimeMagicResult &result)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def localeComments(*__, **_) -> Never:
    """
    Qt's 'QMimeTypePrivate::LocaleHash
    QMimeProviderBase::localeComments(const QString &name)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMimeProviderBase.localeComments' has no cute function yet. Qt's "
        "'QMimeTypePrivate::LocaleHash "
        "QMimeProviderBase::localeComments(const QString &name)': gives a "
        "type Python has no way to take yet.")
