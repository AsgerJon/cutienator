"""
QFactoryLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfactoryloader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFactoryLoader to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt, QLibrary, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCborArray, QLibraryPrivate, QObject, QPluginParsedMetaData

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFactoryLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFactoryLoader: a plain Python object standing in
  front of one C++ QFactoryLoader.

  What exists
  -----------

  Every function of Qt's QFactoryLoader that has a ritual and that Python can
  call so far, 10 names in all: 'tr', 'setLoadHints', 'update', 'refreshAll',
  'library', 'setExtraSearchPath', 'indexOf', 'metaData', 'metaDataKeys',
  'instance'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFactoryLoader::~QFactoryLoader()': the destructor: Python never
    removes a C++ QFactoryLoader.
  - Qt's 'QMultiMap<int, QString> QFactoryLoader::keyMap() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QFactoryLoader is created at the first use, not by
    'QFactoryLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFactoryLoader.
  - Each name of Qt's QFactoryLoader that has no cute function yet,
    'instanceHelper_locked', 'keyMap', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QFactoryLoader::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFactoryLoader::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN14QFactoryLoader2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  def refreshAll() -> None:
    """
    Calls Qt's 'void QFactoryLoader::refreshAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#refreshAll
    """
    #  void QFactoryLoader::refreshAll()
    Rituals.call('ritual_ZN14QFactoryLoader10refreshAllEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFactoryLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def library(self, key: str) -> Optional[QLibraryPrivate]:
    """
    Calls Qt's 'QLibraryPrivate *QFactoryLoader::library(const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#library

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QLibraryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLibraryPrivate *QFactoryLoader::library(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK14QFactoryLoader7libraryERK7QString', key,
    )
    from . import QLibraryPrivate
    return QLibraryPrivate._cuteAt(address)

  @overload(str)
  def indexOf(self, needle: str) -> int:
    """
    Calls Qt's 'int QFactoryLoader::indexOf(const QString &needle) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#indexOf

    Parameters
    ----------

    needle : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QFactoryLoader::indexOf(const QString &needle) const
    return self.uglySide.call(
        'ritual_ZNK14QFactoryLoader7indexOfERK7QString', needle,
    )

  def metaData(self) -> QList[QPluginParsedMetaData]:
    """
    Calls Qt's 'MetaDataList QFactoryLoader::metaData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#metaData

    Returns
    -------

    QList[QPluginParsedMetaData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  MetaDataList QFactoryLoader::metaData() const
    address = self.uglySide.call('ritual_ZNK14QFactoryLoader8metaDataEv')
    from . import QPluginParsedMetaData
    return QList[QPluginParsedMetaData]._cuteOwning(address)

  def metaDataKeys(self) -> QList[QCborArray]:
    """
    Calls Qt's 'QList<QCborArray> QFactoryLoader::metaDataKeys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#metaDataKeys

    Returns
    -------

    QList[QCborArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCborArray> QFactoryLoader::metaDataKeys() const
    address = self.uglySide.call(
        'ritual_ZNK14QFactoryLoader12metaDataKeysEv',
    )
    from . import QCborArray
    return QList[QCborArray]._cuteOwning(address)

  @overload(int)
  def instance(self, index: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QFactoryLoader::instance(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#instance

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QFactoryLoader::instance(int index) const
    address = self.uglySide.call(
        'ritual_ZNK14QFactoryLoader8instanceEi', index,
    )
    from . import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLibrary.LoadHints)
  def setLoadHints(self, hints: QLibrary.LoadHints) -> None:
    """
    Calls Qt's 'void QFactoryLoader::setLoadHints(QLibrary::LoadHints
    hints)'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#setLoadHints

    Parameters
    ----------

    hints : QLibrary.LoadHints
      Passed on as its number.
    """
    #  void QFactoryLoader::setLoadHints(QLibrary::LoadHints hints)
    self.uglySide.call(
        'ritual_ZN14QFactoryLoader12setLoadHintsE6QFlagsIN8QLibrary8LoadHin'
        'tEE',
        hints.value,
    )

  @overload(str)
  def setExtraSearchPath(self, path: str) -> None:
    """
    Calls Qt's 'void QFactoryLoader::setExtraSearchPath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfactoryloader.html#setExtraSearchPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFactoryLoader::setExtraSearchPath(const QString &path)
    self.uglySide.call(
        'ritual_ZN14QFactoryLoader18setExtraSearchPathERK7QString', path,
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

  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(NoneType, str)
  @overload(str, str, Qt.CaseSensitivity)
  @overload(NoneType, str, Qt.CaseSensitivity)
  def __init__(
      self,
      iid: Optional[str],
      suffix: str = '',
      a2: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> None:
    """
    Notes what was given, for Qt's 'QFactoryLoader::QFactoryLoader(const char
    *iid, const QString &suffix, Qt::CaseSensitivity a2)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#QFactoryLoader

    Parameters
    ----------

    iid : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    suffix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    a2 : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  QFactoryLoader::QFactoryLoader(const char *iid, const QString &suffix,
    #      Qt::CaseSensitivity a2)
    self._noteCreation(QFactoryLoader, lambda: Rituals.call(
        'ritual_ZN14QFactoryLoaderC1EPKcRK7QStringN2Qt15CaseSensitivityE',
        self._bytesOf(iid), suffix, a2.value,
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

  def update(self) -> None:
    """
    Calls Qt's 'void QFactoryLoader::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qfactoryloader.html#update
    """
    #  void QFactoryLoader::update()
    self.uglySide.call('ritual_ZN14QFactoryLoader6updateEv')

  @staticmethod
  def instanceHelper_locked(*__, **_) -> Never:
    """
    Qt's 'QObject *QFactoryLoader::instanceHelper_locked(int index) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'isIidMatch'.
    """
    raise NotImplementedError(
        "'QFactoryLoader.instanceHelper_locked' has no cute function yet. "
        "Qt's 'QObject *QFactoryLoader::instanceHelper_locked(int index) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'isIidMatch'.")

  @staticmethod
  def keyMap(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<int, QString> QFactoryLoader::keyMap() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFactoryLoader.keyMap' has no cute function yet. Qt's "
        "'QMultiMap<int, QString> QFactoryLoader::keyMap() const': gives a "
        "type Python has no way to take yet.")
