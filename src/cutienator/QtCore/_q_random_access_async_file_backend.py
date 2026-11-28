"""
QRandomAccessAsyncFileBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QRandomAccessAsyncFileBackend to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QIODeviceBase

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


class QRandomAccessAsyncFileBackend(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRandomAccessAsyncFileBackend: a plain Python object
  standing in front of one C++ QRandomAccessAsyncFileBackend.

  What exists
  -----------

  Every function of Qt's QRandomAccessAsyncFileBackend that has a ritual and
  that Python can call so far, 8 names in all: 'init', 'cancelAndWait',
  'close', 'size', 'open', 'flush', 'read', 'write'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRandomAccessAsyncFileBackend::~QRandomAccessAsyncFileBackend()':
    the destructor: Python never removes a C++ QRandomAccessAsyncFileBackend.
  - Qt's 'QIOWriteOperation *QRandomAccessAsyncFileBackend::write(qint64
    offset, QByteArray &&data)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QIOVectoredReadOperation
    *QRandomAccessAsyncFileBackend::readInto(qint64 offset, QSpan<std::byte>
    buffer)': takes a type Python has no way to hand over yet.
  - Qt's 'QIOVectoredWriteOperation
    *QRandomAccessAsyncFileBackend::writeFrom(qint64 offset, QSpan<const
    std::byte> buffer)': takes a type Python has no way to hand over yet.
  - Qt's 'QIOVectoredReadOperation
    *QRandomAccessAsyncFileBackend::readInto(qint64 offset, QSpan<const
    QSpan<std::byte>> buffers)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QIOVectoredWriteOperation
    *QRandomAccessAsyncFileBackend::writeFrom(qint64 offset, QSpan<const
    QSpan<const std::byte>> buffers)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  5 of the 19 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QRandomAccessAsyncFileBackend is created at the first use, not by
    'QRandomAccessAsyncFileBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRandomAccessAsyncFileBackend.
  - Each name of Qt's QRandomAccessAsyncFileBackend that has no cute function
    yet, '__init__', 'readInto', 'writeFrom', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRandomAccessAsyncFileBackend'

  #  A C++ QRandomAccessAsyncFileBackend Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRandomAccessAsyncFileBackend'

  #  The functions Qt calls itself that QRandomAccessAsyncFileBackend is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'readInto': (
          'QIOVectoredReadOperation '
          '*QRandomAccessAsyncFileBackend::readInto(qint64, '
          'QSpan<std::byte>)',
          'QIOVectoredReadOperation '
          '*QRandomAccessAsyncFileBackend::readInto(qint64, QSpan<const '
          'QSpan<std::byte>>)',
      ),
      'writeFrom': (
          'QIOVectoredWriteOperation '
          '*QRandomAccessAsyncFileBackend::writeFrom(qint64, QSpan<const '
          'std::byte>)',
          'QIOVectoredWriteOperation '
          '*QRandomAccessAsyncFileBackend::writeFrom(qint64, QSpan<const '
          'QSpan<const std::byte>>)',
      ),
  }

  #  The functions Qt calls itself that QRandomAccessAsyncFileBackend is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'init': (
          ('_ZN29QRandomAccessAsyncFileBackend4initEv',
           ('bool', 'number', ''),
           ()),
      ),
      'cancelAndWait': (
          ('_ZN29QRandomAccessAsyncFileBackend13cancelAndWaitEP12QIOOperati'
           'on',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QIOOperation'),
           )),
      ),
      'close': (
          ('_ZN29QRandomAccessAsyncFileBackend5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'size': (
          ('_ZNK29QRandomAccessAsyncFileBackend4sizeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'open': (
          ('_ZN29QRandomAccessAsyncFileBackend4openERK7QString6QFlagsIN13QI'
           'ODeviceBase12OpenModeFlagEE',
           ('address', 'address', 'QtCore:QIOOperation'),
           (
               ('address', 'text', ''),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
           )),
      ),
      'flush': (
          ('_ZN29QRandomAccessAsyncFileBackend5flushEv',
           ('address', 'address', 'QtCore:QIOOperation'),
           ()),
      ),
      'read': (
          ('_ZN29QRandomAccessAsyncFileBackend4readExx',
           ('address', 'address', 'QtCore:QIOReadOperation'),
           (
               ('long long', 'number', ''),
               ('long long', 'number', ''),
           )),
      ),
      'write': (
          ('_ZN29QRandomAccessAsyncFileBackend5writeExRK10QByteArray',
           ('address', 'address', 'QtCore:QIOWriteOperation'),
           (
               ('long long', 'number', ''),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QRandomAccessAsyncFileBackend::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#size
    """
    #  qint64 QRandomAccessAsyncFileBackend::size() const
    return self.uglySide.call(
        'ritual_ZNK29QRandomAccessAsyncFileBackend4sizeEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QRandomAccessAsyncFileBackend::QRandomAccessAsyncFileBackend(
    QRandomAccessAsyncFile *owner)': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileBackend.__init__' has no cute function yet. "
        "Qt's "
        "'QRandomAccessAsyncFileBackend::QRandomAccessAsyncFileBackend(QRand"
        "omAccessAsyncFile *owner)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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
    Calls Qt's 'bool QRandomAccessAsyncFileBackend::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#init
    """
    #  bool QRandomAccessAsyncFileBackend::init()
    return self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFileBackend4initEv',
    )

  @overload(QIOOperation)
  @overload(NoneType)
  def cancelAndWait(self, op: Optional[QIOOperation]) -> None:
    """
    Calls Qt's 'void
    QRandomAccessAsyncFileBackend::cancelAndWait(QIOOperation *op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#cancelAndWait

    Parameters
    ----------

    op : Optional[QIOOperation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRandomAccessAsyncFileBackend::cancelAndWait(QIOOperation *op)
    self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFileBackend13cancelAndWaitEP12QIOOper'
        'ation',
        self._addressOf(op),
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QRandomAccessAsyncFileBackend::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#close
    """
    #  void QRandomAccessAsyncFileBackend::close()
    self.uglySide.call('ritual_ZN29QRandomAccessAsyncFileBackend5closeEv')

  @overload(str, QIODeviceBase.OpenMode)
  def open(
      self,
      path: str,
      mode: QIODeviceBase.OpenMode,
  ) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation *QRandomAccessAsyncFileBackend::open(const
    QString &path, QIODeviceBase::OpenMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#open

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
    #  QIOOperation *QRandomAccessAsyncFileBackend::open(const QString &path,
    #      QIODeviceBase::OpenMode mode)
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFileBackend4openERK7QString6QFlagsIN1'
        '3QIODeviceBase12OpenModeFlagEE',
        path, mode.value,
    )
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  def flush(self) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation *QRandomAccessAsyncFileBackend::flush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#flush

    Returns
    -------

    Optional[QIOOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperation *QRandomAccessAsyncFileBackend::flush()
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFileBackend5flushEv',
    )
    from . import QIOOperation
    return QIOOperation._cuteAt(address)

  @overload(int, int)
  def read(self, offset: int, maxSize: int) -> Optional[QIOReadOperation]:
    """
    Calls Qt's 'QIOReadOperation *QRandomAccessAsyncFileBackend::read(qint64
    offset, qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#read

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
    #  QIOReadOperation *QRandomAccessAsyncFileBackend::read(qint64 offset,
    #      qint64 maxSize)
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFileBackend4readExx', offset, maxSize,
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
    *QRandomAccessAsyncFileBackend::write(qint64 offset, const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomaccessasyncfilebackend.html#write

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
    #  QIOWriteOperation *QRandomAccessAsyncFileBackend::write(qint64 offset,
    #      const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN29QRandomAccessAsyncFileBackend5writeExRK10QByteArray',
        offset, self._valueOf(data),
    )
    from . import QIOWriteOperation
    return QIOWriteOperation._cuteAt(address)

  @staticmethod
  def readInto(*__, **_) -> Never:
    """
    - Qt's 'QIOVectoredReadOperation
      *QRandomAccessAsyncFileBackend::readInto(qint64 offset,
      QSpan<std::byte> buffer)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QIOVectoredReadOperation
      *QRandomAccessAsyncFileBackend::readInto(qint64 offset, QSpan<const
      QSpan<std::byte>> buffers)': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileBackend.readInto' has no cute function yet. "
        "Qt's 'QIOVectoredReadOperation "
        "*QRandomAccessAsyncFileBackend::readInto(qint64 offset, "
        "QSpan<std::byte> buffer)': takes a type Python has no way to hand "
        "over yet. Qt's 'QIOVectoredReadOperation "
        "*QRandomAccessAsyncFileBackend::readInto(qint64 offset, "
        "QSpan<const QSpan<std::byte>> buffers)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def writeFrom(*__, **_) -> Never:
    """
    - Qt's 'QIOVectoredWriteOperation
      *QRandomAccessAsyncFileBackend::writeFrom(qint64 offset, QSpan<const
      std::byte> buffer)': takes a type Python has no way to hand over yet.
    - Qt's 'QIOVectoredWriteOperation
      *QRandomAccessAsyncFileBackend::writeFrom(qint64 offset, QSpan<const
      QSpan<const std::byte>> buffers)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QRandomAccessAsyncFileBackend.writeFrom' has no cute function "
        "yet. Qt's 'QIOVectoredWriteOperation "
        "*QRandomAccessAsyncFileBackend::writeFrom(qint64 offset, "
        "QSpan<const std::byte> buffer)': takes a type Python has no way to "
        "hand over yet. Qt's 'QIOVectoredWriteOperation "
        "*QRandomAccessAsyncFileBackend::writeFrom(qint64 offset, "
        "QSpan<const QSpan<const std::byte>> buffers)': takes a type Python "
        "has no way to hand over yet.")
