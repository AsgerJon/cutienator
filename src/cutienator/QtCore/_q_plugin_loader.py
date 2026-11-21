"""
QPluginLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpluginloader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QLibrary, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QJsonObject, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPluginLoader(QObject):
  """
  The cute side of Qt's QPluginLoader: a plain Python object standing in
  front of one C++ QPluginLoader.

  It is built on the cute 'QObject', as Qt's QPluginLoader is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPluginLoader that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'instance', 'metaData',
  'load', 'unload', 'isLoaded', 'setFileName', 'fileName', 'errorString',
  'setLoadHints', 'loadHints'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPluginLoader::~QPluginLoader()': the destructor: Python never
    removes a C++ QPluginLoader.

  What has no ritual
  ------------------

  8 of the 23 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QPluginLoader is created at the first use, not by
    'QPluginLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPluginLoader.
  - Qt tells when it has removed the C++ QPluginLoader. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPluginLoader::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#tr

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
    #  QString QPluginLoader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPluginLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPluginLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPluginLoader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPluginLoader::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPluginLoader10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def metaData(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QPluginLoader::metaData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#metaData

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QPluginLoader::metaData() const
    address = self.uglySide.call('ritual_ZNK13QPluginLoader8metaDataEv')
    from . import QJsonObject
    return QJsonObject._cuteOwning(address)

  def isLoaded(self) -> bool:
    """
    Calls Qt's 'bool QPluginLoader::isLoaded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#isLoaded
    """
    #  bool QPluginLoader::isLoaded() const
    return self.uglySide.call('ritual_ZNK13QPluginLoader8isLoadedEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QPluginLoader::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPluginLoader::fileName() const
    return self.uglySide.call('ritual_ZNK13QPluginLoader8fileNameEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPluginLoader::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPluginLoader::errorString() const
    return self.uglySide.call('ritual_ZNK13QPluginLoader11errorStringEv')

  def loadHints(self) -> QLibrary.LoadHints:
    """
    Calls Qt's 'QLibrary::LoadHints QPluginLoader::loadHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#loadHints

    Returns
    -------

    QLibrary.LoadHints
      The value standing for the combination Qt gave back.
    """
    #  QLibrary::LoadHints QPluginLoader::loadHints() const
    return QLibrary.LoadHints(self.uglySide.call(
        'ritual_ZNK13QPluginLoader9loadHintsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QPluginLoader::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPluginLoader::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN13QPluginLoader11setFileNameERK7QString', fileName,
    )

  @overload(QLibrary.LoadHints)
  def setLoadHints(self, loadHints: QLibrary.LoadHints) -> None:
    """
    Calls Qt's 'void QPluginLoader::setLoadHints(QLibrary::LoadHints
    loadHints)'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#setLoadHints

    Parameters
    ----------

    loadHints : QLibrary.LoadHints
      Passed on as its number.
    """
    #  void QPluginLoader::setLoadHints(QLibrary::LoadHints loadHints)
    self.uglySide.call(
        'ritual_ZN13QPluginLoader12setLoadHintsE6QFlagsIN8QLibrary8LoadHint'
        'EE',
        loadHints.value,
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
    Notes what was given, for Qt's 'QPluginLoader::QPluginLoader(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#QPluginLoader

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPluginLoader::QPluginLoader(QObject *parent)
    self._noteCreation(QPluginLoader, lambda: Rituals.call(
        'ritual_ZN13QPluginLoaderC1EP7QObject', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      fileName: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPluginLoader::QPluginLoader(const
    QString &fileName, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#QPluginLoader

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPluginLoader::QPluginLoader(const QString &fileName, QObject *parent)
    self._noteCreation(QPluginLoader, lambda: Rituals.call(
        'ritual_ZN13QPluginLoaderC1ERK7QStringP7QObject',
        fileName, self._addressOf(parent),
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

  def instance(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QPluginLoader::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#instance

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QPluginLoader::instance()
    address = self.uglySide.call('ritual_ZN13QPluginLoader8instanceEv')
    return QObject._cuteAt(address)

  def load(self) -> bool:
    """
    Calls Qt's 'bool QPluginLoader::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#load
    """
    #  bool QPluginLoader::load()
    return self.uglySide.call('ritual_ZN13QPluginLoader4loadEv')

  def unload(self) -> bool:
    """
    Calls Qt's 'bool QPluginLoader::unload()'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginloader.html#unload
    """
    #  bool QPluginLoader::unload()
    return self.uglySide.call('ritual_ZN13QPluginLoader6unloadEv')
