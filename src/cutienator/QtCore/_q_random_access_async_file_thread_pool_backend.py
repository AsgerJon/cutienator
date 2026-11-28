"""
QRandomAccessAsyncFileThreadPoolBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QRandomAccessAsyncFileThreadPoolBackend to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QIODeviceBase, QRandomAccessAsyncFileBackend

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIOOperation, QIOReadOperation, QIOWriteOperation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIOOperation = WAIT['QIOOperation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRandomAccessAsyncFileThreadPoolBackend(QRandomAccessAsyncFileBackend):
  """
  The cute side of Qt's QRandomAccessAsyncFileThreadPoolBackend: a plain
  Python object standing in front of one C++
  QRandomAccessAsyncFileThreadPoolBackend.

  It is built on the cute 'QRandomAccessAsyncFileBackend', as Qt's
  QRandomAccessAsyncFileThreadPoolBackend is built on Qt's
  QRandomAccessAsyncFileBackend, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRandomAccessAsyncFileThreadPoolBackend that has a
  ritual and that Python can call so far, 8 names in all: 'init',
  'cancelAndWait', 'close', 'size', 'open', 'flush', 'read', 'write'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIOWriteOperation
    *QRandomAccessAsyncFileThreadPoolBackend::write(qint64 offset, QByteArray
    &&data)': takes a type Python has no way to hand over yet.
  - Qt's 'QIOVectoredReadOperation
    *QRandomAccessAsyncFileThreadPoolBackend::readInto(qint64 offset,
    QSpan<std::byte> buffer)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QIOVectoredWriteOperation
    *QRandomAccessAsyncFileThreadPoolBackend::writeFrom(qint64 offset,
    QSpan<const std::byte> buffer)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QIOVectoredReadOperation
    *QRandomAccessAsyncFileThreadPoolBackend::readInto(qint64 offset,
    QSpan<const QSpan<std::byte>> buffers)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QIOVectoredWriteOperation
    *QRandomAccessAsyncFileThreadPoolBackend::writeFrom(qint64 offset,
    QSpan<const QSpan<const std::byte>> buffers)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  11 of the 24 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 forbidden;
  2 leans on 'QRandomAccessAsyncFileThreadPoolBackend.

  What to expect
  --------------

  - The C++ QRandomAccessAsyncFileThreadPoolBackend is created at the first
    use, not by 'QRandomAccessAsyncFileThreadPoolBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRandomAccessAsyncFileThreadPoolBackend.
  - Each name of Qt's QRandomAccessAsyncFileThreadPoolBackend that has no
    cute function yet, '__init__', 'executeNextOperation',
    'operationComplete', 'processBufferAt', 'processFlush', 'processOpen',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QRandomAccessAsyncFileThreadPoolBackend,
  #  each a class in here as in C++.

  class OperationResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QRandomAccessAsyncFileThreadPoolBackend::OperationResult: a plain Python
    object standing in front of one C++
    QRandomAccessAsyncFileThreadPoolBackend::OperationResult.

    C++ hands a QRandomAccessAsyncFileThreadPoolBackend::OperationResult
    around as a copy, so every C++
    QRandomAccessAsyncFileThreadPoolBackend::OperationResult behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QRandomAccessAsyncFileThreadPoolBackend::OperationResult yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRandomAccessAsyncFileThreadPoolBackend::OperationResult::
      ~OperationResult()': the destructor: Python removes its C++
      QRandomAccessAsyncFileThreadPoolBackend::OperationResult by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QRandomAccessAsyncFileThreadPoolBackend::OperationResult is
      created at the first use, not by
      'QRandomAccessAsyncFileThreadPoolBackend::OperationResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QRandomAccessAsyncFileThreadPoolBackend::OperationResult back gives a
      copy the ritual made for Python, in a new cute
      QRandomAccessAsyncFileThreadPoolBackend::OperationResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRandomAccessAsyncFileThreadPoolBackend::OperationResult'

    #  Qt's '~QRandomAccessAsyncFileThreadPoolBackend::OperationResult()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QRandomAccessAsyncFileThreadPoolBackend::OperationResult behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend15OperationResultD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRandomAccessAsyncFileThreadPoolBackend'

  #  A C++ QRandomAccessAsyncFileThreadPoolBackend Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRandomAccessAsyncFileThreadPoolBackend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QRandomAccessAsyncFileThreadPoolBackend::size()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html#size
    """
    #  qint64 QRandomAccessAsyncFileThreadPoolBackend::size() const
    ritual = 'ritual_ZNK39QRandomAccessAsyncFileThreadPoolBackend4sizeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK39QRandomAccessAsyncFileThreadPoolBackend4sizeEv')
    return self.uglySide.call(ritual)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QRandomAccessAsyncFileThreadPoolBackend::
    QRandomAccessAsyncFileThreadPoolBackend(QRandomAccessAsyncFile *owner)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'asyncFileThreadPool'.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileThreadPoolBackend.__init__' has no cute "
        "function yet. Qt's "
        "'QRandomAccessAsyncFileThreadPoolBackend::QRandomAccessAsyncFileThr"
        "eadPoolBackend(QRandomAccessAsyncFile *owner)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'asyncFileThreadPool'.")

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

  def init(self) -> bool:
    """
    Calls Qt's 'bool QRandomAccessAsyncFileThreadPoolBackend::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html#init
    """
    #  bool QRandomAccessAsyncFileThreadPoolBackend::init()
    return self.uglySide.call(
        'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend4initEv',
    )

  @overload(QIOOperation)
  @overload(NoneType)
  def cancelAndWait(self, op: Optional[QIOOperation]) -> None:
    """
    Calls Qt's 'void
    QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(QIOOperation
    *op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html

    Parameters
    ----------

    op : Optional[QIOOperation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(
    #      QIOOperation *op)
    ritual = (
        'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend13cancelAndWaitE'
        'P12QIOOperation')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN39QRandomAccessAsyncFileThreadPoolBackend13cancelAn'
          'dWaitEP12QIOOperation')
    self.uglySide.call(ritual, self._addressOf(op))

  def close(self) -> None:
    """
    Calls Qt's 'void QRandomAccessAsyncFileThreadPoolBackend::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html#close
    """
    #  void QRandomAccessAsyncFileThreadPoolBackend::close()
    ritual = 'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend5closeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN39QRandomAccessAsyncFileThreadPoolBackend5closeEv')
    self.uglySide.call(ritual)

  @overload(str, QIODeviceBase.OpenMode)
  def open(
      self,
      path: str,
      mode: QIODeviceBase.OpenMode,
  ) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation
    *QRandomAccessAsyncFileThreadPoolBackend::open(const QString &path,
    QIODeviceBase::OpenMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html#open

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
    #  QIOOperation *QRandomAccessAsyncFileThreadPoolBackend::open(const
    #      QString &path, QIODeviceBase::OpenMode mode)
    address = self.uglySide.call(
        'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend4openERK7QString'
        '6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        path, mode.value,
    )
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  def flush(self) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation
    *QRandomAccessAsyncFileThreadPoolBackend::flush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html#flush

    Returns
    -------

    Optional[QIOOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperation *QRandomAccessAsyncFileThreadPoolBackend::flush()
    address = self.uglySide.call(
        'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend5flushEv',
    )
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  @overload(int, int)
  def read(self, offset: int, maxSize: int) -> Optional[QIOReadOperation]:
    """
    Calls Qt's 'QIOReadOperation
    *QRandomAccessAsyncFileThreadPoolBackend::read(qint64 offset, qint64
    maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html#read

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
    #  QIOReadOperation *QRandomAccessAsyncFileThreadPoolBackend::read(qint64
    #      offset, qint64 maxSize)
    address = self.uglySide.call(
        'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend4readExx',
        offset, maxSize,
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
    *QRandomAccessAsyncFileThreadPoolBackend::write(qint64 offset, const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilethreadpoolbackend.html#write

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
    #  QIOWriteOperation
    #      *QRandomAccessAsyncFileThreadPoolBackend::write(qint64 offset,
    #      const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend5writeExRK10QByt'
        'eArray',
        offset, self._valueOf(data),
    )
    from . import QIOWriteOperation
    return QIOWriteOperation._cuteAt(address)

  @staticmethod
  def executeNextOperation(*__, **_) -> Never:
    """
    Qt's 'void
    QRandomAccessAsyncFileThreadPoolBackend::executeNextOperation()': leans
    on 'QRandomAccessAsyncFileThreadPoolBackend::processOpen()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileThreadPoolBackend.executeNextOperation' has "
        "no cute function yet. Qt's 'void "
        "QRandomAccessAsyncFileThreadPoolBackend::executeNextOperation()': "
        "leans on 'QRandomAccessAsyncFileThreadPoolBackend::processOpen()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def operationComplete(*__, **_) -> Never:
    """
    Qt's 'void QRandomAccessAsyncFileThreadPoolBackend::operationComplete()':
    leans on 'QRandomAccessAsyncFileThreadPoolBackend::processOpen()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileThreadPoolBackend.operationComplete' has no "
        "cute function yet. Qt's 'void "
        "QRandomAccessAsyncFileThreadPoolBackend::operationComplete()': "
        "leans on 'QRandomAccessAsyncFileThreadPoolBackend::processOpen()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def processBufferAt(*__, **_) -> Never:
    """
    Qt's 'void
    QRandomAccessAsyncFileThreadPoolBackend::processBufferAt(qsizetype idx)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'asyncFileThreadPool'.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileThreadPoolBackend.processBufferAt' has no "
        "cute function yet. Qt's 'void "
        "QRandomAccessAsyncFileThreadPoolBackend::processBufferAt(qsizetype "
        "idx)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'asyncFileThreadPool'.")

  @staticmethod
  def processFlush(*__, **_) -> Never:
    """
    Qt's 'void QRandomAccessAsyncFileThreadPoolBackend::processFlush()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'asyncFileThreadPool'.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileThreadPoolBackend.processFlush' has no cute "
        "function yet. Qt's 'void "
        "QRandomAccessAsyncFileThreadPoolBackend::processFlush()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'asyncFileThreadPool'.")

  @staticmethod
  def processOpen(*__, **_) -> Never:
    """
    Qt's 'void QRandomAccessAsyncFileThreadPoolBackend::processOpen()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'asyncFileThreadPool'.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileThreadPoolBackend.processOpen' has no cute "
        "function yet. Qt's 'void "
        "QRandomAccessAsyncFileThreadPoolBackend::processOpen()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'asyncFileThreadPool'.")
