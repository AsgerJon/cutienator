"""
RCCResourceLibrary binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/rcc_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means RCCResourceLibrary to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RCCResourceLibrary(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's RCCResourceLibrary: a plain Python object standing in
  front of one C++ RCCResourceLibrary.

  What exists
  -----------

  Every function of Qt's RCCResourceLibrary that has a ritual and that Python
  can call so far, 38 names in all: 'setFormat', 'format', 'setInputFiles',
  'inputFiles', 'setVerbose', 'verbose', 'setInitName', 'initName',
  'setOutputName', 'outputName', 'parseCompressionAlgorithm',
  'setCompressionAlgorithm', 'compressionAlgorithm', 'parseCompressionLevel',
  'setCompressLevel', 'compressLevel', 'setCompressThreshold',
  'compressThreshold', 'setResourceRoot', 'resourceRoot', 'setUseNameSpace',
  'useNameSpace', 'failedResources', 'formatVersion', 'setNoZstd', 'noZstd',
  'reset', 'writeHeader', 'writeMangleNamespaceFunction',
  'writeAddNamespaceFunction', 'writeDecimal', 'writeHex', 'writeNumber2',
  'writeNumber4', 'writeNumber8', 'writeByteArray', 'write', 'writeString'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'RCCResourceLibrary::~RCCResourceLibrary()': the destructor: Python
    never removes a C++ RCCResourceLibrary.
  - Qt's 'ResourceDataFileMap RCCResourceLibrary::resourceDataFileMap()
    const': gives a type Python has no way to take yet.
  - Qt's 'void RCCResourceLibrary::writeChar(char c)': takes a single letter
    as C has it.

  What has no ritual
  ------------------

  12 of the 54 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'RCCResourceLibrary; 1 not a gap; 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ RCCResourceLibrary is created at the first use, not by
    'RCCResourceLibrary(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ RCCResourceLibrary.
  - Each name of Qt's RCCResourceLibrary that has no cute function yet,
    'addFile', 'dataFiles', 'interpretResourceFile', 'output', 'readFiles',
    'resourceDataFileMap', 'write2HexDigits', 'writeChar', 'writeDataBlobs',
    'writeDataNames', 'writeDataStructure', 'writeInitializer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside RCCResourceLibrary, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CompressionAlgorithm(CuteNum, scoped=True):
    """
    The enum 'RCCResourceLibrary::CompressionAlgorithm' of Qt, with the 4
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Zlib = Kee[int](0)
    Zstd = Kee[int](1)
    Best = Kee[int](99)
    NULL = Kee[int](-1)

  class Format(CuteNum):
    """
    The enum 'RCCResourceLibrary::Format' of Qt, with the 5 names Qt gives in
    it.
    """

    Binary = Kee[int](0)
    C_Code = Kee[int](1)
    Pass1 = Kee[int](2)
    Pass2 = Kee[int](3)
    Python_Code = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, QString)
  @overload(str, NoneType)
  def parseCompressionAlgorithm(
      algo: str,
      errorMsg: Optional[QString],
  ) -> CompressionAlgorithm:
    """
    Calls Qt's 'CompressionAlgorithm
    RCCResourceLibrary::parseCompressionAlgorithm(QStringView algo, QString
    *errorMsg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#parseCompressionAlgorithm

    Parameters
    ----------

    algo : str
      Passed on as it is: a QString is made of it for the call.

    errorMsg : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    CompressionAlgorithm
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CompressionAlgorithm(number)' gives.
    """
    #  CompressionAlgorithm
    #      RCCResourceLibrary::parseCompressionAlgorithm(QStringView algo,
    #      QString *errorMsg)
    return RCCResourceLibrary.CompressionAlgorithm(Rituals.call(
        'ritual_ZN18RCCResourceLibrary25parseCompressionAlgorithmE11QString'
        'ViewP7QString',
        algo, CuteMixin._addressOf(errorMsg),
    ))

  @staticmethod
  @overload(CompressionAlgorithm, str, QString)
  @overload(CompressionAlgorithm, str, NoneType)
  def parseCompressionLevel(
      algo: CompressionAlgorithm,
      level: str,
      errorMsg: Optional[QString],
  ) -> int:
    """
    Calls Qt's 'int
    RCCResourceLibrary::parseCompressionLevel(CompressionAlgorithm algo,
    const QString &level, QString *errorMsg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#parseCompressionLevel

    Parameters
    ----------

    algo : CompressionAlgorithm
      Passed on as its number.

    level : str
      Passed on as it is: a QString is made of it for the call.

    errorMsg : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int RCCResourceLibrary::parseCompressionLevel(CompressionAlgorithm
    #      algo, const QString &level, QString *errorMsg)
    return Rituals.call(
        'ritual_ZN18RCCResourceLibrary21parseCompressionLevelENS_20Compress'
        'ionAlgorithmERK7QStringPS1_',
        algo.value, level, CuteMixin._addressOf(errorMsg),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'RCCResourceLibrary'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> Format:
    """
    Calls Qt's 'Format RCCResourceLibrary::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format RCCResourceLibrary::format() const
    return RCCResourceLibrary.Format(self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary6formatEv',
    ))

  def inputFiles(self) -> QStringList:
    """
    Calls Qt's 'QStringList RCCResourceLibrary::inputFiles() const'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#inputFiles

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList RCCResourceLibrary::inputFiles() const
    address = self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary10inputFilesEv',
    )
    return QStringList._cuteOwning(address)

  def verbose(self) -> bool:
    """
    Calls Qt's 'bool RCCResourceLibrary::verbose() const'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#verbose
    """
    #  bool RCCResourceLibrary::verbose() const
    return self.uglySide.call('ritual_ZNK18RCCResourceLibrary7verboseEv')

  def initName(self) -> str:
    """
    Calls Qt's 'QString RCCResourceLibrary::initName() const'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#initName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString RCCResourceLibrary::initName() const
    return self.uglySide.call('ritual_ZNK18RCCResourceLibrary8initNameEv')

  def outputName(self) -> str:
    """
    Calls Qt's 'QString RCCResourceLibrary::outputName() const'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#outputName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString RCCResourceLibrary::outputName() const
    return self.uglySide.call('ritual_ZNK18RCCResourceLibrary10outputNameEv')

  def compressionAlgorithm(self) -> CompressionAlgorithm:
    """
    Calls Qt's 'CompressionAlgorithm
    RCCResourceLibrary::compressionAlgorithm() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#compressionAlgorithm

    Returns
    -------

    CompressionAlgorithm
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CompressionAlgorithm(number)' gives.
    """
    #  CompressionAlgorithm RCCResourceLibrary::compressionAlgorithm() const
    return RCCResourceLibrary.CompressionAlgorithm(self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary20compressionAlgorithmEv',
    ))

  def compressLevel(self) -> int:
    """
    Calls Qt's 'int RCCResourceLibrary::compressLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#compressLevel
    """
    #  int RCCResourceLibrary::compressLevel() const
    return self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary13compressLevelEv',
    )

  def compressThreshold(self) -> int:
    """
    Calls Qt's 'int RCCResourceLibrary::compressThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#compressThreshold
    """
    #  int RCCResourceLibrary::compressThreshold() const
    return self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary17compressThresholdEv',
    )

  def resourceRoot(self) -> str:
    """
    Calls Qt's 'QString RCCResourceLibrary::resourceRoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#resourceRoot

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString RCCResourceLibrary::resourceRoot() const
    return self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary12resourceRootEv',
    )

  def useNameSpace(self) -> bool:
    """
    Calls Qt's 'bool RCCResourceLibrary::useNameSpace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#useNameSpace
    """
    #  bool RCCResourceLibrary::useNameSpace() const
    return self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary12useNameSpaceEv',
    )

  def failedResources(self) -> QStringList:
    """
    Calls Qt's 'QStringList RCCResourceLibrary::failedResources() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#failedResources

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList RCCResourceLibrary::failedResources() const
    address = self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary15failedResourcesEv',
    )
    return QStringList._cuteOwning(address)

  def formatVersion(self) -> int:
    """
    Calls Qt's 'int RCCResourceLibrary::formatVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#formatVersion
    """
    #  int RCCResourceLibrary::formatVersion() const
    return self.uglySide.call(
        'ritual_ZNK18RCCResourceLibrary13formatVersionEv',
    )

  def noZstd(self) -> bool:
    """
    Calls Qt's 'bool RCCResourceLibrary::noZstd() const'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#noZstd
    """
    #  bool RCCResourceLibrary::noZstd() const
    return self.uglySide.call('ritual_ZNK18RCCResourceLibrary6noZstdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Format)
  def setFormat(self, f: Format) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setFormat(Format f)'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#setFormat

    Parameters
    ----------

    f : Format
      Passed on as its number.
    """
    #  void RCCResourceLibrary::setFormat(Format f)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary9setFormatENS_6FormatE', f.value,
    )

  @overload(QStringList)
  def setInputFiles(self, files: QStringList) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setInputFiles(const QStringList
    &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setInputFiles

    Parameters
    ----------

    files : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void RCCResourceLibrary::setInputFiles(const QStringList &files)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary13setInputFilesERK5QListI7QStringE',
        self._valueOf(files),
    )

  @overload(bool)
  def setVerbose(self, b: bool) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setVerbose(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#setVerbose

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void RCCResourceLibrary::setVerbose(bool b)
    self.uglySide.call('ritual_ZN18RCCResourceLibrary10setVerboseEb', b)

  @overload(str)
  def setInitName(self, name: str) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setInitName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setInitName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void RCCResourceLibrary::setInitName(const QString &name)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary11setInitNameERK7QString', name,
    )

  @overload(str)
  def setOutputName(self, name: str) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setOutputName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setOutputName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void RCCResourceLibrary::setOutputName(const QString &name)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary13setOutputNameERK7QString', name,
    )

  @overload(CompressionAlgorithm)
  def setCompressionAlgorithm(self, algo: CompressionAlgorithm) -> None:
    """
    Calls Qt's 'void
    RCCResourceLibrary::setCompressionAlgorithm(CompressionAlgorithm algo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setCompressionAlgorithm

    Parameters
    ----------

    algo : CompressionAlgorithm
      Passed on as its number.
    """
    #  void RCCResourceLibrary::setCompressionAlgorithm(CompressionAlgorithm
    #      algo)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary23setCompressionAlgorithmENS_20Compre'
        'ssionAlgorithmE',
        algo.value,
    )

  @overload(int)
  def setCompressLevel(self, c: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setCompressLevel(int c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setCompressLevel

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::setCompressLevel(int c)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary16setCompressLevelEi', c,
    )

  @overload(int)
  def setCompressThreshold(self, t: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setCompressThreshold(int t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setCompressThreshold

    Parameters
    ----------

    t : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::setCompressThreshold(int t)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary20setCompressThresholdEi', t,
    )

  @overload(str)
  def setResourceRoot(self, root: str) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setResourceRoot(const QString
    &root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setResourceRoot

    Parameters
    ----------

    root : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void RCCResourceLibrary::setResourceRoot(const QString &root)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary15setResourceRootERK7QString', root,
    )

  @overload(bool)
  def setUseNameSpace(self, v: bool) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setUseNameSpace(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#setUseNameSpace

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void RCCResourceLibrary::setUseNameSpace(bool v)
    self.uglySide.call('ritual_ZN18RCCResourceLibrary15setUseNameSpaceEb', v)

  @overload(bool)
  def setNoZstd(self, v: bool) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::setNoZstd(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#setNoZstd

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void RCCResourceLibrary::setNoZstd(bool v)
    self.uglySide.call('ritual_ZN18RCCResourceLibrary9setNoZstdEb', v)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __init__(self, formatVersion: int) -> None:
    """
    Notes what was given, for Qt's
    'RCCResourceLibrary::RCCResourceLibrary(quint8 formatVersion)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#RCCResourceLibrary

    Parameters
    ----------

    formatVersion : int
      Passed on as it is.
    """
    #  RCCResourceLibrary::RCCResourceLibrary(quint8 formatVersion)
    self._noteCreation(RCCResourceLibrary, lambda: Rituals.call(
        'ritual_ZN18RCCResourceLibraryC1Eh', formatVersion,
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

  def reset(self) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#reset
    """
    #  void RCCResourceLibrary::reset()
    self.uglySide.call('ritual_ZN18RCCResourceLibrary5resetEv')

  def writeHeader(self) -> bool:
    """
    Calls Qt's 'bool RCCResourceLibrary::writeHeader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeHeader
    """
    #  bool RCCResourceLibrary::writeHeader()
    return self.uglySide.call('ritual_ZN18RCCResourceLibrary11writeHeaderEv')

  @overload(QByteArray)
  def writeMangleNamespaceFunction(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeMangleNamespaceFunction(const
    QByteArray &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void RCCResourceLibrary::writeMangleNamespaceFunction(const QByteArray
    #      &name)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary28writeMangleNamespaceFunctionERK10QB'
        'yteArray',
        self._valueOf(name),
    )

  @overload(QByteArray)
  def writeAddNamespaceFunction(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeAddNamespaceFunction(const
    QByteArray &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeAddNamespaceFunction

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void RCCResourceLibrary::writeAddNamespaceFunction(const QByteArray
    #      &name)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary25writeAddNamespaceFunctionERK10QByte'
        'Array',
        self._valueOf(name),
    )

  @overload(int)
  def writeDecimal(self, value: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeDecimal(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeDecimal

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::writeDecimal(int value)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary12writeDecimalEi', value,
    )

  @overload(int)
  def writeHex(self, number: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeHex(quint8 number)'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#writeHex

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::writeHex(quint8 number)
    self.uglySide.call('ritual_ZN18RCCResourceLibrary8writeHexEh', number)

  @overload(int)
  def writeNumber2(self, number: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeNumber2(quint16 number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeNumber2

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::writeNumber2(quint16 number)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary12writeNumber2Et', number,
    )

  @overload(int)
  def writeNumber4(self, number: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeNumber4(quint32 number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeNumber4

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::writeNumber4(quint32 number)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary12writeNumber4Ej', number,
    )

  @overload(int)
  def writeNumber8(self, number: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeNumber8(quint64 number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeNumber8

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::writeNumber8(quint64 number)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary12writeNumber8Ey', number,
    )

  @overload(QByteArray)
  def writeByteArray(self, a0: QByteArray) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeByteArray(const QByteArray
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeByteArray

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void RCCResourceLibrary::writeByteArray(const QByteArray &a0)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary14writeByteArrayERK10QByteArray',
        self._valueOf(a0),
    )

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, a0: Optional[str], len: int) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::write(const char *a0, int len)'.

    Qt's own words: https://doc.qt.io/qt-6/rccresourcelibrary.html#write

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void RCCResourceLibrary::write(const char *a0, int len)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary5writeEPKci', self._bytesOf(a0), len,
    )

  @overload(str)
  @overload(NoneType)
  def writeString(self, s: Optional[str]) -> None:
    """
    Calls Qt's 'void RCCResourceLibrary::writeString(const char *s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rccresourcelibrary.html#writeString

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void RCCResourceLibrary::writeString(const char *s)
    self.uglySide.call(
        'ritual_ZN18RCCResourceLibrary11writeStringEPKc', self._bytesOf(s),
    )

  @staticmethod
  def addFile(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::addFile(const QString &alias, RCCFileInfo
    file)': the compiler refuses its ritual as it would be written here:
    argument type 'RCCFileInfo' is incomplete.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.addFile' has no cute function yet. Qt's 'bool "
        "RCCResourceLibrary::addFile(const QString &alias, RCCFileInfo "
        "file)': the compiler refuses its ritual as it would be written "
        "here: argument type 'RCCFileInfo' is incomplete.")

  @staticmethod
  def dataFiles(*__, **_) -> Never:
    """
    Qt's 'QStringList RCCResourceLibrary::dataFiles() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'RCCFileInfo'.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.dataFiles' has no cute function yet. Qt's "
        "'QStringList RCCResourceLibrary::dataFiles() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'RCCFileInfo'.")

  @staticmethod
  def interpretResourceFile(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::interpretResourceFile(QIODevice
    *inputDevice, const QString &file, QString currentPath, bool listMode)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'RccTag'.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.interpretResourceFile' has no cute function "
        "yet. Qt's 'bool "
        "RCCResourceLibrary::interpretResourceFile(QIODevice *inputDevice, "
        "const QString &file, QString currentPath, bool listMode)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'RccTag'."
    )

  @staticmethod
  def output(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::output(QIODevice &outDevice, QIODevice
    &tempDevice, QIODevice &errorDevice)': leans on
    'RCCResourceLibrary::writeDataStructure()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.output' has no cute function yet. Qt's 'bool "
        "RCCResourceLibrary::output(QIODevice &outDevice, QIODevice "
        "&tempDevice, QIODevice &errorDevice)': leans on "
        "'RCCResourceLibrary::writeDataStructure()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def readFiles(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::readFiles(bool listMode, QIODevice
    &errorDevice)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'msgOpenReadFailed'.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.readFiles' has no cute function yet. Qt's "
        "'bool RCCResourceLibrary::readFiles(bool listMode, QIODevice "
        "&errorDevice)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'msgOpenReadFailed'.")

  @staticmethod
  def resourceDataFileMap(*__, **_) -> Never:
    """
    Qt's 'ResourceDataFileMap RCCResourceLibrary::resourceDataFileMap()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.resourceDataFileMap' has no cute function yet. "
        "Qt's 'ResourceDataFileMap "
        "RCCResourceLibrary::resourceDataFileMap() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def write2HexDigits(*__, **_) -> Never:
    """
    Qt's 'void RCCResourceLibrary::write2HexDigits(quint8 number)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'hexDigits'.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.write2HexDigits' has no cute function yet. "
        "Qt's 'void RCCResourceLibrary::write2HexDigits(quint8 number)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'hexDigits'.")

  @staticmethod
  def writeChar(*__, **_) -> Never:
    """
    Qt's 'void RCCResourceLibrary::writeChar(char c)': takes a single letter
    as C has it.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.writeChar' has no cute function yet. Qt's "
        "'void RCCResourceLibrary::writeChar(char c)': takes a single "
        "letter as C has it.")

  @staticmethod
  def writeDataBlobs(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::writeDataBlobs()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'RCCFileInfo'.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.writeDataBlobs' has no cute function yet. Qt's "
        "'bool RCCResourceLibrary::writeDataBlobs()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'RCCFileInfo'.")

  @staticmethod
  def writeDataNames(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::writeDataNames()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'RCCFileInfo'.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.writeDataNames' has no cute function yet. Qt's "
        "'bool RCCResourceLibrary::writeDataNames()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'RCCFileInfo'.")

  @staticmethod
  def writeDataStructure(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::writeDataStructure()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'RCCFileInfo'.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.writeDataStructure' has no cute function yet. "
        "Qt's 'bool RCCResourceLibrary::writeDataStructure()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'RCCFileInfo'.")

  @staticmethod
  def writeInitializer(*__, **_) -> Never:
    """
    Qt's 'bool RCCResourceLibrary::writeInitializer()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: incomplete type 'RCCFileInfo' named in nested name specifier.
    """
    raise NotImplementedError(
        "'RCCResourceLibrary.writeInitializer' has no cute function yet. "
        "Qt's 'bool RCCResourceLibrary::writeInitializer()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: incomplete type 'RCCFileInfo' named in nested "
        "name specifier.")
