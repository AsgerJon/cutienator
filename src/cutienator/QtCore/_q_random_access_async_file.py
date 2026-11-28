"""
QRandomAccessAsyncFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QRandomAccessAsyncFile to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIOOperation, QIOReadOperation, QIOWriteOperation
  from . import QMetaObject, QRandomAccessAsyncFilePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRandomAccessAsyncFile(QObject):
  """
  The cute side of Qt's QRandomAccessAsyncFile: a plain Python object
  standing in front of one C++ QRandomAccessAsyncFile.

  It is built on the cute 'QObject', as Qt's QRandomAccessAsyncFile is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRandomAccessAsyncFile that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'close',
  'size', 'open', 'flush', 'read', 'write', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRandomAccessAsyncFile::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QRandomAccessAsyncFile::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QRandomAccessAsyncFile::~QRandomAccessAsyncFile()': the destructor:
    Python never removes a C++ QRandomAccessAsyncFile.
  - Qt's 'QIOWriteOperation *QRandomAccessAsyncFile::write(qint64 offset,
    QByteArray &&data)': takes a type Python has no way to hand over yet.
  - Qt's 'QIOVectoredReadOperation *QRandomAccessAsyncFile::readInto(qint64
    offset, QSpan<std::byte> buffer)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QIOVectoredWriteOperation *QRandomAccessAsyncFile::writeFrom(qint64
    offset, QSpan<const std::byte> buffer)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QIOVectoredReadOperation *QRandomAccessAsyncFile::readInto(qint64
    offset, QSpan<const QSpan<std::byte>> buffers)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QIOVectoredWriteOperation *QRandomAccessAsyncFile::writeFrom(qint64
    offset, QSpan<const QSpan<const std::byte>> buffers)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QRandomAccessAsyncFilePrivate
    *QRandomAccessAsyncFile::d_func() const': takes in Python what
    'QRandomAccessAsyncFilePrivate *QRandomAccessAsyncFile::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 25 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QRandomAccessAsyncFile is created at the first use, not by
    'QRandomAccessAsyncFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRandomAccessAsyncFile.
  - Qt tells when it has removed the C++ QRandomAccessAsyncFile. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRandomAccessAsyncFile that has no cute function yet,
    'readInto', 'writeFrom', holds a function that raises
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
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QRandomAccessAsyncFile::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#tr

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
    #  QString QRandomAccessAsyncFile::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QRandomAccessAsyncFile2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRandomAccessAsyncFile'

  #  A C++ QRandomAccessAsyncFile Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRandomAccessAsyncFile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRandomAccessAsyncFile::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRandomAccessAsyncFile::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QRandomAccessAsyncFile10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QRandomAccessAsyncFile::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#size
    """
    #  qint64 QRandomAccessAsyncFile::size() const
    return self.uglySide.call('ritual_ZNK22QRandomAccessAsyncFile4sizeEv')

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QRandomAccessAsyncFile::QRandomAccessAsyncFile(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#QRandomAccessAsyncFile

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRandomAccessAsyncFile::QRandomAccessAsyncFile(QObject *parent)
    self._noteCreation(QRandomAccessAsyncFile, lambda: Rituals.call(
        'ritual_ZN22QRandomAccessAsyncFileC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def close(self) -> None:
    """
    Calls Qt's 'void QRandomAccessAsyncFile::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#close
    """
    #  void QRandomAccessAsyncFile::close()
    self.uglySide.call('ritual_ZN22QRandomAccessAsyncFile5closeEv')

  @overload(str, QIODeviceBase.OpenMode)
  def open(
      self,
      filePath: str,
      mode: QIODeviceBase.OpenMode,
  ) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation *QRandomAccessAsyncFile::open(const QString
    &filePath, QIODeviceBase::OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#open

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number.

    Returns
    -------

    Optional[QIOOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperation *QRandomAccessAsyncFile::open(const QString &filePath,
    #      QIODeviceBase::OpenMode mode)
    address = self.uglySide.call(
        'ritual_ZN22QRandomAccessAsyncFile4openERK7QString6QFlagsIN13QIODev'
        'iceBase12OpenModeFlagEE',
        filePath, mode.value,
    )
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  def flush(self) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation *QRandomAccessAsyncFile::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#flush

    Returns
    -------

    Optional[QIOOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperation *QRandomAccessAsyncFile::flush()
    address = self.uglySide.call('ritual_ZN22QRandomAccessAsyncFile5flushEv')
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  @overload(int, int)
  def read(self, offset: int, maxSize: int) -> Optional[QIOReadOperation]:
    """
    Calls Qt's 'QIOReadOperation *QRandomAccessAsyncFile::read(qint64 offset,
    qint64 maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#read

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
    #  QIOReadOperation *QRandomAccessAsyncFile::read(qint64 offset, qint64
    #      maxSize)
    address = self.uglySide.call(
        'ritual_ZN22QRandomAccessAsyncFile4readExx', offset, maxSize,
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
    Calls Qt's 'QIOWriteOperation *QRandomAccessAsyncFile::write(qint64
    offset, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#write

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
    #  QIOWriteOperation *QRandomAccessAsyncFile::write(qint64 offset, const
    #      QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN22QRandomAccessAsyncFile5writeExRK10QByteArray',
        offset, self._valueOf(data),
    )
    from . import QIOWriteOperation
    return QIOWriteOperation._cuteAt(address)

  def d_func(self) -> Optional[QRandomAccessAsyncFilePrivate]:
    """
    Calls Qt's 'QRandomAccessAsyncFilePrivate
    *QRandomAccessAsyncFile::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomaccessasyncfile.html#d_func

    Returns
    -------

    Optional[QRandomAccessAsyncFilePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRandomAccessAsyncFilePrivate *QRandomAccessAsyncFile::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QRandomAccessAsyncFile6d_funcEv',
    )
    from . import QRandomAccessAsyncFilePrivate
    return QRandomAccessAsyncFilePrivate._cuteAt(address)

  @staticmethod
  def readInto(*__, **_) -> Never:
    """
    - Qt's 'QIOVectoredReadOperation *QRandomAccessAsyncFile::readInto(qint64
      offset, QSpan<std::byte> buffer)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QIOVectoredReadOperation *QRandomAccessAsyncFile::readInto(qint64
      offset, QSpan<const QSpan<std::byte>> buffers)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFile.readInto' has no cute function yet. Qt's "
        "'QIOVectoredReadOperation *QRandomAccessAsyncFile::readInto(qint64 "
        "offset, QSpan<std::byte> buffer)': takes a type Python has no way "
        "to hand over yet. Qt's 'QIOVectoredReadOperation "
        "*QRandomAccessAsyncFile::readInto(qint64 offset, QSpan<const "
        "QSpan<std::byte>> buffers)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def writeFrom(*__, **_) -> Never:
    """
    - Qt's 'QIOVectoredWriteOperation
      *QRandomAccessAsyncFile::writeFrom(qint64 offset, QSpan<const
      std::byte> buffer)': takes a type Python has no way to hand over yet.
    - Qt's 'QIOVectoredWriteOperation
      *QRandomAccessAsyncFile::writeFrom(qint64 offset, QSpan<const
      QSpan<const std::byte>> buffers)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFile.writeFrom' has no cute function yet. Qt's "
        "'QIOVectoredWriteOperation "
        "*QRandomAccessAsyncFile::writeFrom(qint64 offset, QSpan<const "
        "std::byte> buffer)': takes a type Python has no way to hand over "
        "yet. Qt's 'QIOVectoredWriteOperation "
        "*QRandomAccessAsyncFile::writeFrom(qint64 offset, QSpan<const "
        "QSpan<const std::byte>> buffers)': takes a type Python has no way "
        "to hand over yet.")
