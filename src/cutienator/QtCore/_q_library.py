"""
QLibrary binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlibrary.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLibrary(QObject):
  """
  The cute side of Qt's QLibrary: a plain Python object standing in front of
  one C++ QLibrary.

  It is built on the cute 'QObject', as Qt's QLibrary is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLibrary that has a ritual and that Python can call
  so far, 12 names in all: 'metaObject', 'tr', 'load', 'unload', 'isLoaded',
  'isLibrary', 'setFileName', 'fileName', 'setFileNameAndVersion',
  'errorString', 'setLoadHints', 'loadHints'. It can be made from Python, in
  4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLibrary::~QLibrary()': the destructor: Python never removes a C++
    QLibrary.

  What has no ritual
  ------------------

  10 of the 28 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QLibrary is created at the first use, not by 'QLibrary(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLibrary.
  - Qt tells when it has removed the C++ QLibrary. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QLibrary, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class LoadHint(CuteFlags):
    """
    The flags enum 'QLibrary::LoadHint' of Qt, with the 5 names Qt gives in
    it. Qt names the type of its combinations 'QLibrary::LoadHints'.
    """

    ResolveAllSymbolsHint = 0x1
    ExportExternalSymbolsHint = 0x2
    LoadArchiveMemberHint = 0x4
    PreventUnloadHint = 0x8
    DeepBindHint = 0x10

  LoadHints = LoadHint

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
    Calls Qt's 'QString QLibrary::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#tr

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
    #  QString QLibrary::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QLibrary2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def isLibrary(fileName: str) -> bool:
    """
    Calls Qt's 'bool QLibrary::isLibrary(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#isLibrary

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QLibrary::isLibrary(const QString &fileName)
    return Rituals.call('ritual_ZN8QLibrary9isLibraryERK7QString', fileName)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLibrary'

  #  A C++ QLibrary Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLibrary'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLibrary::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLibrary::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QLibrary10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isLoaded(self) -> bool:
    """
    Calls Qt's 'bool QLibrary::isLoaded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#isLoaded
    """
    #  bool QLibrary::isLoaded() const
    return self.uglySide.call('ritual_ZNK8QLibrary8isLoadedEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QLibrary::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLibrary::fileName() const
    return self.uglySide.call('ritual_ZNK8QLibrary8fileNameEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QLibrary::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLibrary::errorString() const
    return self.uglySide.call('ritual_ZNK8QLibrary11errorStringEv')

  def loadHints(self) -> LoadHints:
    """
    Calls Qt's 'LoadHints QLibrary::loadHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#loadHints

    Returns
    -------

    LoadHints
      The value standing for the combination Qt gave back.
    """
    #  LoadHints QLibrary::loadHints() const
    return QLibrary.LoadHints(self.uglySide.call(
        'ritual_ZNK8QLibrary9loadHintsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QLibrary::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLibrary::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN8QLibrary11setFileNameERK7QString', fileName,
    )

  @overload(str, int)
  def setFileNameAndVersion(self, fileName: str, verNum: int) -> None:
    """
    Calls Qt's 'void QLibrary::setFileNameAndVersion(const QString &fileName,
    int verNum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibrary.html#setFileNameAndVersion

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    verNum : int
      Passed on as it is.
    """
    #  void QLibrary::setFileNameAndVersion(const QString &fileName, int
    #      verNum)
    self.uglySide.call(
        'ritual_ZN8QLibrary21setFileNameAndVersionERK7QStringi',
        fileName, verNum,
    )

  @overload(str, str)
  def setFileNameAndVersion(self, fileName: str, version: str) -> None:
    """
    Calls Qt's 'void QLibrary::setFileNameAndVersion(const QString &fileName,
    const QString &version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibrary.html#setFileNameAndVersion

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    version : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLibrary::setFileNameAndVersion(const QString &fileName, const
    #      QString &version)
    self.uglySide.call(
        'ritual_ZN8QLibrary21setFileNameAndVersionERK7QStringS2_',
        fileName, version,
    )

  @overload(LoadHints)
  def setLoadHints(self, hints: LoadHints) -> None:
    """
    Calls Qt's 'void QLibrary::setLoadHints(LoadHints hints)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#setLoadHints

    Parameters
    ----------

    hints : LoadHints
      Passed on as its number.
    """
    #  void QLibrary::setLoadHints(LoadHints hints)
    self.uglySide.call(
        'ritual_ZN8QLibrary12setLoadHintsE6QFlagsINS_8LoadHintEE',
        hints.value,
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
    Notes what was given, for Qt's 'QLibrary::QLibrary(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#QLibrary

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLibrary::QLibrary(QObject *parent)
    self._noteCreation(QLibrary, lambda: Rituals.call(
        'ritual_ZN8QLibraryC1EP7QObject', self._addressOf(parent),
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
    Notes what was given, for Qt's 'QLibrary::QLibrary(const QString
    &fileName, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#QLibrary

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLibrary::QLibrary(const QString &fileName, QObject *parent)
    self._noteCreation(QLibrary, lambda: Rituals.call(
        'ritual_ZN8QLibraryC1ERK7QStringP7QObject',
        fileName, self._addressOf(parent),
    ))

  @overload(str, int)
  @overload(str, int, QObject)
  @overload(str, int, NoneType)
  def __init__(
      self,
      fileName: str,
      verNum: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLibrary::QLibrary(const QString
    &fileName, int verNum, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#QLibrary

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    verNum : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLibrary::QLibrary(const QString &fileName, int verNum, QObject
    #      *parent)
    self._noteCreation(QLibrary, lambda: Rituals.call(
        'ritual_ZN8QLibraryC1ERK7QStringiP7QObject',
        fileName, verNum, self._addressOf(parent),
    ))

  @overload(str, str)
  @overload(str, str, QObject)
  @overload(str, str, NoneType)
  def __init__(
      self,
      fileName: str,
      version: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLibrary::QLibrary(const QString
    &fileName, const QString &version, QObject *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#QLibrary

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    version : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLibrary::QLibrary(const QString &fileName, const QString &version,
    #      QObject *parent)
    self._noteCreation(QLibrary, lambda: Rituals.call(
        'ritual_ZN8QLibraryC1ERK7QStringS2_P7QObject',
        fileName, version, self._addressOf(parent),
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

  def load(self) -> bool:
    """
    Calls Qt's 'bool QLibrary::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#load
    """
    #  bool QLibrary::load()
    return self.uglySide.call('ritual_ZN8QLibrary4loadEv')

  def unload(self) -> bool:
    """
    Calls Qt's 'bool QLibrary::unload()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibrary.html#unload
    """
    #  bool QLibrary::unload()
    return self.uglySide.call('ritual_ZN8QLibrary6unloadEv')
