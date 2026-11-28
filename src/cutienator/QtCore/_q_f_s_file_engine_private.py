"""
QFSFileEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfsfileengine_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFSFileEnginePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QAbstractFileEnginePrivate, QIODeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractFileEngine, QFSFileEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractFileEngine = WAIT['QAbstractFileEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFSFileEnginePrivate(QAbstractFileEnginePrivate):
  """
  The cute side of Qt's QFSFileEnginePrivate: a plain Python object standing
  in front of one C++ QFSFileEnginePrivate.

  It is built on the cute 'QAbstractFileEnginePrivate', as Qt's
  QFSFileEnginePrivate is built on Qt's QAbstractFileEnginePrivate, and has
  everything that class has.

  C++ hands a QFSFileEnginePrivate around as a copy, so every C++
  QFSFileEnginePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFSFileEnginePrivate that has a ritual and that
  Python can call so far, 9 names in all: 'q_func', 'openFd', 'closeFdFh',
  'flushFh', 'posFdFh', 'seekFdFh', 'openModeCanCreate',
  'openModeToOpenFlags', 'init'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFSFileEngine *QFSFileEnginePrivate::q_func() const': takes
    in Python what 'QFSFileEngine *QFSFileEnginePrivate::q_func()' takes.
  - Qt's 'bool QFSFileEnginePrivate::openFh(QIODevice::OpenMode flags, FILE
    *fh)': names 'FILE', which has no cute class yet.
  - Qt's 'qint64 QFSFileEnginePrivate::readLineFdFh(char *data, qint64
    maxlen)': names 'char', which has no cute class yet.
  - Qt's 'QFSFileEnginePrivate::~QFSFileEnginePrivate()': the destructor:
    Python removes its C++ QFSFileEnginePrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  23 of the 37 functions Qt declares: 16 cannot be called and cannot be
  called through the meta-object and cannot be copied; 3 leans on
  'QFSFileEnginePrivate; 2 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file; 1 leans on
  'QFileSystemEngine; 1 leans on 'QFileSystemMetaData.

  What to expect
  --------------

  - The C++ QFSFileEnginePrivate is created at the first use, not by
    'QFSFileEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFSFileEnginePrivate back gives a copy the ritual
    made for Python, in a new cute QFSFileEnginePrivate.
  - Each name of Qt's QFSFileEnginePrivate that has no cute function yet,
    'doStat', 'getPermissions', 'isSequentialFdFh', 'isSymlink', 'map',
    'nativeClose', 'nativeFlush', 'nativeHandle', 'nativeIsSequential',
    'nativeOpen', 'nativeOpenImpl', 'nativePos', 'nativeRead',
    'nativeReadLine', 'nativeSeek', 'nativeSize', 'nativeSyncToDisk',
    'nativeWrite', 'openFh', 'readFdFh', 'readLineFdFh', 'sizeFdFh', 'unmap',
    'unmapAll', 'writeFdFh', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFSFileEnginePrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class LastIOCommand(CuteNum):
    """
    The enum 'QFSFileEnginePrivate::LastIOCommand' of Qt, with the 3 names Qt
    gives in it.
    """

    IOFlushCommand = Kee[int](0)
    IOReadCommand = Kee[int](1)
    IOWriteCommand = Kee[int](2)

  #  The classes Qt writes inside QFSFileEnginePrivate, each a class in here
  #  as in C++.

  class StartAndLength(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFSFileEnginePrivate::StartAndLength: a plain
    Python object standing in front of one C++
    QFSFileEnginePrivate::StartAndLength.

    C++ hands a QFSFileEnginePrivate::StartAndLength around as a copy, so
    every C++ QFSFileEnginePrivate::StartAndLength behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QFSFileEnginePrivate::StartAndLength yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFSFileEnginePrivate::StartAndLength::~StartAndLength()': the
      destructor: Python removes its C++ QFSFileEnginePrivate::StartAndLength
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QFSFileEnginePrivate::StartAndLength is created at the first
      use, not by 'QFSFileEnginePrivate::StartAndLength(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFSFileEnginePrivate::StartAndLength back gives a
      copy the ritual made for Python, in a new cute
      QFSFileEnginePrivate::StartAndLength.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFSFileEnginePrivate::StartAndLength'

    #  Qt's '~QFSFileEnginePrivate::StartAndLength()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QFSFileEnginePrivate::StartAndLength behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN20QFSFileEnginePrivate14StartAndLengthD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QIODeviceBase.OpenMode)
  def openModeCanCreate(openMode: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool
    QFSFileEnginePrivate::openModeCanCreate(QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfsfileengineprivate.html#openModeCanCreate

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QFSFileEnginePrivate::openModeCanCreate(QIODevice::OpenMode
    #      openMode)
    return Rituals.call(
        'ritual_ZN20QFSFileEnginePrivate17openModeCanCreateE6QFlagsIN13QIOD'
        'eviceBase12OpenModeFlagEE',
        openMode.value,
    )

  @staticmethod
  @overload(QIODeviceBase.OpenMode)
  def openModeToOpenFlags(mode: QIODeviceBase.OpenMode) -> int:
    """
    Calls Qt's 'int
    QFSFileEnginePrivate::openModeToOpenFlags(QIODevice::OpenMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfsfileengineprivate.html#openModeToOpenFlags

    Parameters
    ----------

    mode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  int QFSFileEnginePrivate::openModeToOpenFlags(QIODevice::OpenMode
    #      mode)
    return Rituals.call(
        'ritual_ZN20QFSFileEnginePrivate19openModeToOpenFlagsE6QFlagsIN13QI'
        'ODeviceBase12OpenModeFlagEE',
        mode.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFSFileEnginePrivate'

  #  Qt's '~QFSFileEnginePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QFSFileEnginePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QFSFileEnginePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def posFdFh(self) -> int:
    """
    Calls Qt's 'qint64 QFSFileEnginePrivate::posFdFh() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengineprivate.html#posFdFh
    """
    #  qint64 QFSFileEnginePrivate::posFdFh() const
    return self.uglySide.call('ritual_ZNK20QFSFileEnginePrivate7posFdFhEv')

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

  @overload(QAbstractFileEngine)
  @overload(NoneType)
  def __init__(self, q: Optional[QAbstractFileEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QFSFileEnginePrivate::QFSFileEnginePrivate(QAbstractFileEngine *q)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfsfileengineprivate.html#QFSFileEnginePrivate

    Parameters
    ----------

    q : Optional[QAbstractFileEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QFSFileEnginePrivate::QFSFileEnginePrivate(QAbstractFileEngine *q)
    self._noteCreation(QFSFileEnginePrivate, lambda: Rituals.call(
        'ritual_ZN20QFSFileEnginePrivateC1EP19QAbstractFileEngine',
        self._addressOf(q),
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

  def q_func(self) -> Optional[QFSFileEngine]:
    """
    Calls Qt's 'QFSFileEngine *QFSFileEnginePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengineprivate.html#q_func

    Returns
    -------

    Optional[QFSFileEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFSFileEngine *QFSFileEnginePrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QFSFileEnginePrivate6q_funcEv')
    from . import QFSFileEngine
    return QFSFileEngine._cuteAt(address)

  @overload(QIODeviceBase.OpenMode, int)
  def openFd(self, flags: QIODeviceBase.OpenMode, fd: int) -> bool:
    """
    Calls Qt's 'bool QFSFileEnginePrivate::openFd(QIODevice::OpenMode flags,
    int fd)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengineprivate.html#openFd

    Parameters
    ----------

    flags : QIODeviceBase.OpenMode
      Passed on as its number.

    fd : int
      Passed on as it is.
    """
    #  bool QFSFileEnginePrivate::openFd(QIODevice::OpenMode flags, int fd)
    return self.uglySide.call(
        'ritual_ZN20QFSFileEnginePrivate6openFdE6QFlagsIN13QIODeviceBase12O'
        'penModeFlagEEi',
        flags.value, fd,
    )

  def closeFdFh(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEnginePrivate::closeFdFh()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfsfileengineprivate.html#closeFdFh
    """
    #  bool QFSFileEnginePrivate::closeFdFh()
    return self.uglySide.call('ritual_ZN20QFSFileEnginePrivate9closeFdFhEv')

  def flushFh(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEnginePrivate::flushFh()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengineprivate.html#flushFh
    """
    #  bool QFSFileEnginePrivate::flushFh()
    return self.uglySide.call('ritual_ZN20QFSFileEnginePrivate7flushFhEv')

  @overload(int)
  def seekFdFh(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QFSFileEnginePrivate::seekFdFh(qint64 a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengineprivate.html#seekFdFh

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QFSFileEnginePrivate::seekFdFh(qint64 a0)
    return self.uglySide.call(
        'ritual_ZN20QFSFileEnginePrivate8seekFdFhEx', a0,
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QFSFileEnginePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengineprivate.html#init
    """
    #  void QFSFileEnginePrivate::init()
    self.uglySide.call('ritual_ZN20QFSFileEnginePrivate4initEv')

  @staticmethod
  def doStat(*__, **_) -> Never:
    """
    Qt's 'bool
    QFSFileEnginePrivate::doStat(QFileSystemMetaData::MetaDataFlags flags)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.doStat' has no cute function yet. Qt's 'bool "
        "QFSFileEnginePrivate::doStat(QFileSystemMetaData::MetaDataFlags "
        "flags) const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def getPermissions(*__, **_) -> Never:
    """
    Qt's 'QAbstractFileEngine::FileFlags
    QFSFileEnginePrivate::getPermissions(QAbstractFileEngine::FileFlags type)
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.getPermissions' has no cute function yet. "
        "Qt's 'QAbstractFileEngine::FileFlags "
        "QFSFileEnginePrivate::getPermissions(QAbstractFileEngine::FileFlags"
        " type) const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def isSequentialFdFh(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::isSequentialFdFh() const': leans on
    'QFSFileEnginePrivate::doStat(QFlags<QFileSystemMetaData::MetaDataFlag>)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.isSequentialFdFh' has no cute function yet. "
        "Qt's 'bool QFSFileEnginePrivate::isSequentialFdFh() const': leans "
        "on "
        "'QFSFileEnginePrivate::doStat(QFlags<QFileSystemMetaData::MetaDataF"
        "lag>) const', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def isSymlink(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::isSymlink() const': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.isSymlink' has no cute function yet. Qt's "
        "'bool QFSFileEnginePrivate::isSymlink() const': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def map(*__, **_) -> Never:
    """
    Qt's 'uchar *QFSFileEnginePrivate::map(qint64 offset, qint64 size,
    QFile::MemoryMapFlags flags)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.map' has no cute function yet. Qt's 'uchar "
        "*QFSFileEnginePrivate::map(qint64 offset, qint64 size, "
        "QFile::MemoryMapFlags flags)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def nativeClose(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::nativeClose()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeClose' has no cute function yet. Qt's "
        "'bool QFSFileEnginePrivate::nativeClose()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def nativeFlush(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::nativeFlush()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeFlush' has no cute function yet. Qt's "
        "'bool QFSFileEnginePrivate::nativeFlush()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def nativeHandle(*__, **_) -> Never:
    """
    Qt's 'int QFSFileEnginePrivate::nativeHandle() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeHandle' has no cute function yet. Qt's "
        "'int QFSFileEnginePrivate::nativeHandle() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def nativeIsSequential(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::nativeIsSequential() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeIsSequential' has no cute function "
        "yet. Qt's 'bool QFSFileEnginePrivate::nativeIsSequential() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def nativeOpen(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::nativeOpen(QIODevice::OpenMode openMode,
    std::optional<QFile::Permissions> permissions)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeOpen' has no cute function yet. Qt's "
        "'bool QFSFileEnginePrivate::nativeOpen(QIODevice::OpenMode "
        "openMode, std::optional<QFile::Permissions> permissions)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeOpenImpl(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::nativeOpenImpl(QIODevice::OpenMode
    openMode, mode_t mode)': leans on
    'QFileSystemMetaData::fillFromStatxBuf(statx const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeOpenImpl' has no cute function yet. "
        "Qt's 'bool "
        "QFSFileEnginePrivate::nativeOpenImpl(QIODevice::OpenMode openMode, "
        "mode_t mode)': leans on "
        "'QFileSystemMetaData::fillFromStatxBuf(statx const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def nativePos(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::nativePos() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativePos' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::nativePos() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def nativeRead(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::nativeRead(char *data, qint64
    maxlen)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeRead' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::nativeRead(char *data, qint64 "
        "maxlen)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def nativeReadLine(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::nativeReadLine(char *data, qint64
    maxlen)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeReadLine' has no cute function yet. "
        "Qt's 'qint64 QFSFileEnginePrivate::nativeReadLine(char *data, "
        "qint64 maxlen)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def nativeSeek(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::nativeSeek(qint64 a0)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeSeek' has no cute function yet. Qt's "
        "'bool QFSFileEnginePrivate::nativeSeek(qint64 a0)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeSize(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::nativeSize() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeSize' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::nativeSize() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeSyncToDisk(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::nativeSyncToDisk()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeSyncToDisk' has no cute function yet. "
        "Qt's 'bool QFSFileEnginePrivate::nativeSyncToDisk()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeWrite(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::nativeWrite(const char *data, qint64
    len)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.nativeWrite' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::nativeWrite(const char *data, qint64 "
        "len)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def openFh(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::openFh(QIODevice::OpenMode flags, FILE
    *fh)': names 'FILE', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.openFh' has no cute function yet. Qt's 'bool "
        "QFSFileEnginePrivate::openFh(QIODevice::OpenMode flags, FILE "
        "*fh)': names 'FILE', which has no cute class yet.")

  @staticmethod
  def readFdFh(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::readFdFh(char *data, qint64 maxlen)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'SignedIOType'.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.readFdFh' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::readFdFh(char *data, qint64 "
        "maxlen)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'SignedIOType'.")

  @staticmethod
  def readLineFdFh(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::readLineFdFh(char *data, qint64
    maxlen)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.readLineFdFh' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::readLineFdFh(char *data, qint64 "
        "maxlen)': names 'char', which has no cute class yet.")

  @staticmethod
  def sizeFdFh(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::sizeFdFh() const': leans on
    'QFSFileEnginePrivate::doStat(QFlags<QFileSystemMetaData::MetaDataFlag>)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.sizeFdFh' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::sizeFdFh() const': leans on "
        "'QFSFileEnginePrivate::doStat(QFlags<QFileSystemMetaData::MetaDataF"
        "lag>) const', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def unmap(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEnginePrivate::unmap(uchar *ptr)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.unmap' has no cute function yet. Qt's 'bool "
        "QFSFileEnginePrivate::unmap(uchar *ptr)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def unmapAll(*__, **_) -> Never:
    """
    Qt's 'void QFSFileEnginePrivate::unmapAll()': leans on
    'QFSFileEnginePrivate::unmap(unsigned char*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.unmapAll' has no cute function yet. Qt's "
        "'void QFSFileEnginePrivate::unmapAll()': leans on "
        "'QFSFileEnginePrivate::unmap(unsigned char*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def writeFdFh(*__, **_) -> Never:
    """
    Qt's 'qint64 QFSFileEnginePrivate::writeFdFh(const char *data, qint64
    len)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: unknown type name 'SignedIOType'.
    """
    raise NotImplementedError(
        "'QFSFileEnginePrivate.writeFdFh' has no cute function yet. Qt's "
        "'qint64 QFSFileEnginePrivate::writeFdFh(const char *data, qint64 "
        "len)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'SignedIOType'.")
