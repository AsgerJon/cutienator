"""
QRandomAccessAsyncFilePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QRandomAccessAsyncFilePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QIODeviceBase, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIOOperation, QIOReadOperation, QIOWriteOperation
  from . import QRandomAccessAsyncFile
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIOOperation = WAIT['QIOOperation']
  QRandomAccessAsyncFile = WAIT['QRandomAccessAsyncFile']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRandomAccessAsyncFilePrivate(QObjectPrivate):
  """
  The cute side of Qt's QRandomAccessAsyncFilePrivate: a plain Python object
  standing in front of one C++ QRandomAccessAsyncFilePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QRandomAccessAsyncFilePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QRandomAccessAsyncFilePrivate that has a ritual and
  that Python can call so far, 10 names in all: 'q_func', 'get',
  'cancelAndWait', 'close', 'size', 'open', 'flush', 'read', 'write',
  'checkValid'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRandomAccessAsyncFile
    *QRandomAccessAsyncFilePrivate::q_func() const': takes in Python what
    'QRandomAccessAsyncFile *QRandomAccessAsyncFilePrivate::q_func()' takes.
  - Qt's 'QRandomAccessAsyncFilePrivate::~QRandomAccessAsyncFilePrivate()':
    the destructor: Python never removes a C++ QRandomAccessAsyncFilePrivate.
  - Qt's 'QIOWriteOperation *QRandomAccessAsyncFilePrivate::write(qint64
    offset, QByteArray &&data)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QIOVectoredReadOperation
    *QRandomAccessAsyncFilePrivate::readInto(qint64 offset, QSpan<std::byte>
    buffer)': takes a type Python has no way to hand over yet.
  - Qt's 'QIOVectoredWriteOperation
    *QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, QSpan<const
    std::byte> buffer)': takes a type Python has no way to hand over yet.
  - Qt's 'QIOVectoredReadOperation
    *QRandomAccessAsyncFilePrivate::readInto(qint64 offset, QSpan<const
    QSpan<std::byte>> buffers)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QIOVectoredWriteOperation
    *QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, QSpan<const
    QSpan<const std::byte>> buffers)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  5 of the 23 functions Qt declares: 4 forbidden; 1 leans on
  'QRandomAccessAsyncFileThreadPoolBackend.

  What to expect
  --------------

  - The C++ QRandomAccessAsyncFilePrivate is created at the first use, not by
    'QRandomAccessAsyncFilePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRandomAccessAsyncFilePrivate.
  - Each name of Qt's QRandomAccessAsyncFilePrivate that has no cute function
    yet, 'init', 'readInto', 'writeFrom', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRandomAccessAsyncFile)
  @overload(NoneType)
  def get(
      file: Optional[QRandomAccessAsyncFile],
  ) -> Optional[QRandomAccessAsyncFilePrivate]:
    """
    Calls Qt's 'QRandomAccessAsyncFilePrivate
    *QRandomAccessAsyncFilePrivate::get(QRandomAccessAsyncFile *file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#get

    Parameters
    ----------

    file : Optional[QRandomAccessAsyncFile]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRandomAccessAsyncFilePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRandomAccessAsyncFilePrivate
    #      *QRandomAccessAsyncFilePrivate::get(QRandomAccessAsyncFile *file)
    address = Rituals.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivate3getEP22QRandomAccessAsync'
        'File',
        CuteMixin._addressOf(file),
    )
    return QRandomAccessAsyncFilePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRandomAccessAsyncFilePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QRandomAccessAsyncFilePrivate::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#size
    """
    #  qint64 QRandomAccessAsyncFilePrivate::size() const
    return self.uglySide.call(
        'ritual_ZNK29QRandomAccessAsyncFilePrivate4sizeEv',
    )

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
    'QRandomAccessAsyncFilePrivate::QRandomAccessAsyncFilePrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html
    """
    #  QRandomAccessAsyncFilePrivate::QRandomAccessAsyncFilePrivate()
    self._noteCreation(QRandomAccessAsyncFilePrivate, lambda: Rituals.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivateC1Ev',
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

  def q_func(self) -> Optional[QRandomAccessAsyncFile]:
    """
    Calls Qt's 'QRandomAccessAsyncFile
    *QRandomAccessAsyncFilePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#q_func

    Returns
    -------

    Optional[QRandomAccessAsyncFile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRandomAccessAsyncFile *QRandomAccessAsyncFilePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivate6q_funcEv',
    )
    from . import QRandomAccessAsyncFile
    return QRandomAccessAsyncFile._cuteAt(address)

  @overload(QIOOperation)
  @overload(NoneType)
  def cancelAndWait(self, op: Optional[QIOOperation]) -> None:
    """
    Calls Qt's 'void
    QRandomAccessAsyncFilePrivate::cancelAndWait(QIOOperation *op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#cancelAndWait

    Parameters
    ----------

    op : Optional[QIOOperation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRandomAccessAsyncFilePrivate::cancelAndWait(QIOOperation *op)
    self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivate13cancelAndWaitEP12QIOOper'
        'ation',
        self._addressOf(op),
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QRandomAccessAsyncFilePrivate::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#close
    """
    #  void QRandomAccessAsyncFilePrivate::close()
    self.uglySide.call('ritual_ZN29QRandomAccessAsyncFilePrivate5closeEv')

  @overload(str, QIODeviceBase.OpenMode)
  def open(
      self,
      path: str,
      mode: QIODeviceBase.OpenMode,
  ) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation *QRandomAccessAsyncFilePrivate::open(const
    QString &path, QIODeviceBase::OpenMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#open

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number.

    Returns
    -------

    Optional[QIOOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperation *QRandomAccessAsyncFilePrivate::open(const QString &path,
    #      QIODeviceBase::OpenMode mode)
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivate4openERK7QString6QFlagsIN1'
        '3QIODeviceBase12OpenModeFlagEE',
        path, mode.value,
    )
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  def flush(self) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation *QRandomAccessAsyncFilePrivate::flush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#flush

    Returns
    -------

    Optional[QIOOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperation *QRandomAccessAsyncFilePrivate::flush()
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivate5flushEv',
    )
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  @overload(int, int)
  def read(self, offset: int, maxSize: int) -> Optional[QIOReadOperation]:
    """
    Calls Qt's 'QIOReadOperation *QRandomAccessAsyncFilePrivate::read(qint64
    offset, qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#read

    Parameters
    ----------

    offset : int
      Passed on as it is.

    maxSize : int
      Passed on as it is.

    Returns
    -------

    Optional[QIOReadOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOReadOperation *QRandomAccessAsyncFilePrivate::read(qint64 offset,
    #      qint64 maxSize)
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivate4readExx', offset, maxSize,
    )
    from . import QIOReadOperation
    return QIOReadOperation._cuteAt(address)

  @overload(int, QByteArray)
  def write(
      self,
      offset: int,
      data: QByteArray,
  ) -> Optional[QIOWriteOperation]:
    """
    Calls Qt's 'QIOWriteOperation
    *QRandomAccessAsyncFilePrivate::write(qint64 offset, const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#write

    Parameters
    ----------

    offset : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QIOWriteOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOWriteOperation *QRandomAccessAsyncFilePrivate::write(qint64 offset,
    #      const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFilePrivate5writeExRK10QByteArray',
        offset, self._valueOf(data),
    )
    from . import QIOWriteOperation
    return QIOWriteOperation._cuteAt(address)

  def checkValid(self) -> None:
    """
    Calls Qt's 'void QRandomAccessAsyncFilePrivate::checkValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfileprivate.html#checkValid
    """
    #  void QRandomAccessAsyncFilePrivate::checkValid() const
    self.uglySide.call(
        'ritual_ZNK29QRandomAccessAsyncFilePrivate10checkValidEv',
    )

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QRandomAccessAsyncFilePrivate::init()': leans on
    'QRandomAccessAsyncFileThreadPoolBackend::
    QRandomAccessAsyncFileThreadPoolBackend(QRandomAccessAsyncFile*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFilePrivate.init' has no cute function yet. "
        "Qt's 'void QRandomAccessAsyncFilePrivate::init()': leans on "
        "'QRandomAccessAsyncFileThreadPoolBackend::QRandomAccessAsyncFileThr"
        "eadPoolBackend(QRandomAccessAsyncFile*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def readInto(*__, **_) -> Never:
    """
    - Qt's 'QIOVectoredReadOperation
      *QRandomAccessAsyncFilePrivate::readInto(qint64 offset,
      QSpan<std::byte> buffer)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QIOVectoredReadOperation
      *QRandomAccessAsyncFilePrivate::readInto(qint64 offset, QSpan<const
      QSpan<std::byte>> buffers)': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFilePrivate.readInto' has no cute function yet. "
        "Qt's 'QIOVectoredReadOperation "
        "*QRandomAccessAsyncFilePrivate::readInto(qint64 offset, "
        "QSpan<std::byte> buffer)': takes a type Python has no way to hand "
        "over yet. Qt's 'QIOVectoredReadOperation "
        "*QRandomAccessAsyncFilePrivate::readInto(qint64 offset, "
        "QSpan<const QSpan<std::byte>> buffers)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def writeFrom(*__, **_) -> Never:
    """
    - Qt's 'QIOVectoredWriteOperation
      *QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, QSpan<const
      std::byte> buffer)': takes a type Python has no way to hand over yet.
    - Qt's 'QIOVectoredWriteOperation
      *QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, QSpan<const
      QSpan<const std::byte>> buffers)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFilePrivate.writeFrom' has no cute function "
        "yet. Qt's 'QIOVectoredWriteOperation "
        "*QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, "
        "QSpan<const std::byte> buffer)': takes a type Python has no way to "
        "hand over yet. Qt's 'QIOVectoredWriteOperation "
        "*QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, "
        "QSpan<const QSpan<const std::byte>> buffers)': takes a type Python "
        "has no way to hand over yet.")
