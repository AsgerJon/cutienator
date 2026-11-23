"""
QStorageInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstorageinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QByteArray, QDebug, QDir
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QDir = WAIT['QDir']


class QStorageInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStorageInfo: a plain Python object standing in front
  of one C++ QStorageInfo.

  C++ hands a QStorageInfo around as a copy, so every C++ QStorageInfo behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStorageInfo that has a ritual and that Python can
  call so far, 21 names in all: 'setPath', 'rootPath', 'device', 'subvolume',
  'fileSystemType', 'name', 'displayName', 'bytesTotal', 'bytesFree',
  'bytesAvailable', 'blockSize', 'isRoot', 'isReadOnly', 'isReady',
  'isValid', 'refresh', 'mountedVolumes', 'root', '__eq__', '__ne__',
  '__rlshift__'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStorageInfo::~QStorageInfo()': the destructor: Python removes its
    C++ QStorageInfo by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 31 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStorageInfo is created at the first use, not by
    'QStorageInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStorageInfo back gives a copy the ritual made for
    Python, in a new cute QStorageInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def mountedVolumes() -> QList[QStorageInfo]:
    """
    Calls Qt's 'QList<QStorageInfo> QStorageInfo::mountedVolumes()'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#mountedVolumes

    Returns
    -------

    QList[QStorageInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStorageInfo> QStorageInfo::mountedVolumes()
    address = Rituals.call('ritual_ZN12QStorageInfo14mountedVolumesEv')
    return QList[QStorageInfo]._cuteOwning(address)

  @staticmethod
  def root() -> QStorageInfo:
    """
    Calls Qt's 'QStorageInfo QStorageInfo::root()'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#root

    Returns
    -------

    QStorageInfo
      A new cute QStorageInfo around the copy Qt gave back. Python owns it.
    """
    #  QStorageInfo QStorageInfo::root()
    address = Rituals.call('ritual_ZN12QStorageInfo4rootEv')
    return QStorageInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStorageInfo'

  #  Qt's '~QStorageInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QStorageInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QStorageInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rootPath(self) -> str:
    """
    Calls Qt's 'QString QStorageInfo::rootPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#rootPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStorageInfo::rootPath() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo8rootPathEv')

  def device(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStorageInfo::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#device

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStorageInfo::device() const
    address = self.uglySide.call('ritual_ZNK12QStorageInfo6deviceEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def subvolume(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStorageInfo::subvolume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#subvolume

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStorageInfo::subvolume() const
    address = self.uglySide.call('ritual_ZNK12QStorageInfo9subvolumeEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def fileSystemType(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStorageInfo::fileSystemType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#fileSystemType

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStorageInfo::fileSystemType() const
    address = self.uglySide.call(
        'ritual_ZNK12QStorageInfo14fileSystemTypeEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QStorageInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStorageInfo::name() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo4nameEv')

  def displayName(self) -> str:
    """
    Calls Qt's 'QString QStorageInfo::displayName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#displayName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStorageInfo::displayName() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo11displayNameEv')

  def bytesTotal(self) -> int:
    """
    Calls Qt's 'qint64 QStorageInfo::bytesTotal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#bytesTotal
    """
    #  qint64 QStorageInfo::bytesTotal() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo10bytesTotalEv')

  def bytesFree(self) -> int:
    """
    Calls Qt's 'qint64 QStorageInfo::bytesFree() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#bytesFree
    """
    #  qint64 QStorageInfo::bytesFree() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo9bytesFreeEv')

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QStorageInfo::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#bytesAvailable
    """
    #  qint64 QStorageInfo::bytesAvailable() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo14bytesAvailableEv')

  def blockSize(self) -> int:
    """
    Calls Qt's 'int QStorageInfo::blockSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#blockSize
    """
    #  int QStorageInfo::blockSize() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo9blockSizeEv')

  def isRoot(self) -> bool:
    """
    Calls Qt's 'bool QStorageInfo::isRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#isRoot
    """
    #  bool QStorageInfo::isRoot() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo6isRootEv')

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QStorageInfo::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#isReadOnly
    """
    #  bool QStorageInfo::isReadOnly() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo10isReadOnlyEv')

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QStorageInfo::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#isReady
    """
    #  bool QStorageInfo::isReady() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo7isReadyEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QStorageInfo::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#isValid
    """
    #  bool QStorageInfo::isValid() const
    return self.uglySide.call('ritual_ZNK12QStorageInfo7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPath(self, path: str) -> None:
    """
    Calls Qt's 'void QStorageInfo::setPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#setPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStorageInfo::setPath(const QString &path)
    self.uglySide.call('ritual_ZN12QStorageInfo7setPathERK7QString', path)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QStorageInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QStorageInfo &lhs, const QStorageInfo
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#operator==

    Parameters
    ----------

    rhs : QStorageInfo
      Passed on as a value: Qt reads the C++ QStorageInfo, which stays
      Python's own.
    """
    #  bool operator==(const QStorageInfo &lhs, const QStorageInfo &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QStorageInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QStorageInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QStorageInfo &lhs, const QStorageInfo
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#operator!=

    Parameters
    ----------

    rhs : QStorageInfo
      Passed on as a value: Qt reads the C++ QStorageInfo, which stays
      Python's own.
    """
    #  bool operator!=(const QStorageInfo &lhs, const QStorageInfo &rhs)
    return Rituals.call(
        'ritual_ZneRK12QStorageInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QStorageInfo &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QStorageInfo &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK12QStorageInfo',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from . import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStorageInfo::QStorageInfo()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo
    """
    #  QStorageInfo::QStorageInfo()
    self._noteCreation(QStorageInfo, lambda: Rituals.call(
        'ritual_ZN12QStorageInfoC1Ev',
    ))

  @overload(str)
  def __init__(self, path: str) -> None:
    """
    Notes what was given, for Qt's 'QStorageInfo::QStorageInfo(const QString
    &path)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QStorageInfo::QStorageInfo(const QString &path)
    self._noteCreation(QStorageInfo, lambda: Rituals.call(
        'ritual_ZN12QStorageInfoC1ERK7QString', path,
    ))

  @overload(QDir)
  def __init__(self, dir: QDir) -> None:
    """
    Notes what was given, for Qt's 'QStorageInfo::QStorageInfo(const QDir
    &dir)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo

    Parameters
    ----------

    dir : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  QStorageInfo::QStorageInfo(const QDir &dir)
    self._noteCreation(QStorageInfo, lambda: Rituals.call(
        'ritual_ZN12QStorageInfoC1ERK4QDir', self._valueOf(dir),
    ))

  @overload(THIS)
  def __init__(self, other: QStorageInfo) -> None:
    """
    Notes what was given, for Qt's 'QStorageInfo::QStorageInfo(const
    QStorageInfo &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#QStorageInfo

    Parameters
    ----------

    other : QStorageInfo
      Passed on as a value: Qt reads the C++ QStorageInfo, which stays
      Python's own.
    """
    #  QStorageInfo::QStorageInfo(const QStorageInfo &other)
    self._noteCreation(QStorageInfo, lambda: Rituals.call(
        'ritual_ZN12QStorageInfoC1ERKS_', self._valueOf(other),
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

  def refresh(self) -> None:
    """
    Calls Qt's 'void QStorageInfo::refresh()'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfo.html#refresh
    """
    #  void QStorageInfo::refresh()
    self.uglySide.call('ritual_ZN12QStorageInfo7refreshEv')


#  Qt's 'QList<QStorageInfo>': the list of QStorageInfo, which
#  'QList[QStorageInfo]' gives. It is made here, so that there is one as soon
#  as there can be a QStorageInfo.
QList.createKind(
    QStorageInfo, 'value',
    make='ritual_list_make_QStorageInfo',
    add='ritual_list_add_QStorageInfo',
    size='ritual_list_size_QStorageInfo',
    at='ritual_list_at_QStorageInfo',
    drop='ritual_list_drop_QStorageInfo',
)
