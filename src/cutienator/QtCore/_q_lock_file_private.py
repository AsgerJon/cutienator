"""
QLockFilePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlockfile_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QLockFilePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QLockFile
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLockFile = WAIT['QLockFile']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLockFilePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLockFilePrivate: a plain Python object standing in
  front of one C++ QLockFilePrivate.

  C++ hands a QLockFilePrivate around as a copy, so every C++
  QLockFilePrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLockFilePrivate that has a ritual and that Python
  can call so far, 3 names in all: 'lockFileContents', 'processNameByPid',
  'getLockFileHandle'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLockFilePrivate::~QLockFilePrivate()': the destructor: Python
    removes its C++ QLockFilePrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 11 functions Qt declares: 4 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QLockFilePrivate.

  What to expect
  --------------

  - The C++ QLockFilePrivate is created at the first use, not by
    'QLockFilePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLockFilePrivate back gives a copy the ritual made
    for Python, in a new cute QLockFilePrivate.
  - Each name of Qt's QLockFilePrivate that has no cute function yet,
    'getLockInfo_helper', 'isApparentlyStale', 'isProcessRunning',
    'openNewFileDescriptor', 'removeStaleLock', 'tryLock_sys', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QLockFilePrivate, each a class in here as
  #  in C++.

  class LockFileInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLockFilePrivate::LockFileInfo: a plain Python
    object standing in front of one C++ QLockFilePrivate::LockFileInfo.

    C++ hands a QLockFilePrivate::LockFileInfo around as a copy, so every C++
    QLockFilePrivate::LockFileInfo behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QLockFilePrivate::LockFileInfo yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLockFilePrivate::LockFileInfo::~LockFileInfo()': the destructor:
      Python removes its C++ QLockFilePrivate::LockFileInfo by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QLockFilePrivate::LockFileInfo is created at the first use, not
      by 'QLockFilePrivate::LockFileInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLockFilePrivate::LockFileInfo back gives a copy
      the ritual made for Python, in a new cute
      QLockFilePrivate::LockFileInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLockFilePrivate::LockFileInfo'

    #  Qt's '~QLockFilePrivate::LockFileInfo()'. Naming it makes this a value
    #  class: Python owns every C++ QLockFilePrivate::LockFileInfo behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QLockFilePrivate12LockFileInfoD1Ev'

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
  @overload(int)
  def processNameByPid(pid: int) -> str:
    """
    Calls Qt's 'QString QLockFilePrivate::processNameByPid(qint64 pid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlockfileprivate.html#processNameByPid

    Parameters
    ----------

    pid : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLockFilePrivate::processNameByPid(qint64 pid)
    return Rituals.call(
        'ritual_ZN16QLockFilePrivate16processNameByPidEx', pid,
    )

  @staticmethod
  @overload(QLockFile)
  @overload(NoneType)
  def getLockFileHandle(f: Optional[QLockFile]) -> int:
    """
    Calls Qt's 'int QLockFilePrivate::getLockFileHandle(QLockFile *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlockfileprivate.html#getLockFileHandle

    Parameters
    ----------

    f : Optional[QLockFile]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QLockFilePrivate::getLockFileHandle(QLockFile *f)
    return Rituals.call(
        'ritual_ZN16QLockFilePrivate17getLockFileHandleEP9QLockFile',
        CuteMixin._addressOf(f),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLockFilePrivate'

  #  Qt's '~QLockFilePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QLockFilePrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QLockFilePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lockFileContents(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLockFilePrivate::lockFileContents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlockfileprivate.html#lockFileContents

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLockFilePrivate::lockFileContents() const
    address = self.uglySide.call(
        'ritual_ZNK16QLockFilePrivate16lockFileContentsEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload(str)
  def __init__(self, fn: str) -> None:
    """
    Notes what was given, for Qt's 'QLockFilePrivate::QLockFilePrivate(const
    QString &fn)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlockfileprivate.html#QLockFilePrivate

    Parameters
    ----------

    fn : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QLockFilePrivate::QLockFilePrivate(const QString &fn)
    self._noteCreation(QLockFilePrivate, lambda: Rituals.call(
        'ritual_ZN16QLockFilePrivateC1ERK7QString', fn,
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
  def getLockInfo_helper(*__, **_) -> Never:
    """
    Qt's 'bool QLockFilePrivate::getLockInfo_helper(const QString &fileName,
    LockFileInfo *info)': leans on
    'QLockFilePrivate::openNewFileDescriptor(QString const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QLockFilePrivate.getLockInfo_helper' has no cute function yet. "
        "Qt's 'bool QLockFilePrivate::getLockInfo_helper(const QString "
        "&fileName, LockFileInfo *info)': leans on "
        "'QLockFilePrivate::openNewFileDescriptor(QString const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def isApparentlyStale(*__, **_) -> Never:
    """
    Qt's 'bool QLockFilePrivate::isApparentlyStale() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'machineName'.
    """
    raise NotImplementedError(
        "'QLockFilePrivate.isApparentlyStale' has no cute function yet. "
        "Qt's 'bool QLockFilePrivate::isApparentlyStale() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'machineName'.")

  @staticmethod
  def isProcessRunning(*__, **_) -> Never:
    """
    Qt's 'bool QLockFilePrivate::isProcessRunning(qint64 pid, const QString
    &appname)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLockFilePrivate.isProcessRunning' has no cute function yet. Qt's "
        "'bool QLockFilePrivate::isProcessRunning(qint64 pid, const QString "
        "&appname)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def openNewFileDescriptor(*__, **_) -> Never:
    """
    Qt's 'int QLockFilePrivate::openNewFileDescriptor(const QString
    &fileName)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLockFilePrivate.openNewFileDescriptor' has no cute function yet. "
        "Qt's 'int QLockFilePrivate::openNewFileDescriptor(const QString "
        "&fileName)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def removeStaleLock(*__, **_) -> Never:
    """
    Qt's 'bool QLockFilePrivate::removeStaleLock()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLockFilePrivate.removeStaleLock' has no cute function yet. Qt's "
        "'bool QLockFilePrivate::removeStaleLock()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def tryLock_sys(*__, **_) -> Never:
    """
    Qt's 'QLockFile::LockError QLockFilePrivate::tryLock_sys()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QLockFilePrivate.tryLock_sys' has no cute function yet. Qt's "
        "'QLockFile::LockError QLockFilePrivate::tryLock_sys()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
