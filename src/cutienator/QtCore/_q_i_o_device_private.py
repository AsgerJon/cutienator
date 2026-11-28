"""
QIODevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qiodevice_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QIODevicePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QIODevice

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIODevicePrivate(QObjectPrivate):
  """
  The cute side of Qt's QIODevicePrivate: a plain Python object standing in
  front of one C++ QIODevicePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QIODevicePrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIODevicePrivate that has a ritual and that Python
  can call so far, 14 names in all: 'q_func', 'isSequential',
  'isBufferEmpty', 'allWriteBuffersEmpty', 'seekBuffer',
  'setCurrentReadChannel', 'setCurrentWriteChannel', 'setReadChannelCount',
  'setWriteChannelCount', 'peek', 'skipByReading', 'skipLine', 'write',
  'isWriteChunkCached'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QIODevice *QIODevicePrivate::q_func() const': takes in Python
    what 'QIODevice *QIODevicePrivate::q_func()' takes.
  - Qt's 'QIODevicePrivate::QIODevicePrivate(decltype(QObjectPrivateVersion)
    version)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
  - Qt's 'QIODevicePrivate::~QIODevicePrivate()': the destructor: Python
    never removes a C++ QIODevicePrivate.
  - Qt's 'bool QIODevicePrivate::putCharHelper(char c)': takes a single
    letter as C has it.
  - Qt's 'qint64 QIODevicePrivate::read(char *data, qint64 maxSize, bool
    peeking)': names 'char', which has no cute class yet.
  - Qt's 'qint64 QIODevicePrivate::readLine(char *data, qint64 maxSize,
    ReadLineOption option)': names 'char', which has no cute class yet.
  - Qt's 'qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)': names
    'char', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QIODevicePrivate is created at the first use, not by
    'QIODevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIODevicePrivate.
  - Each name of Qt's QIODevicePrivate that has no cute function yet,
    '__init__', 'putCharHelper', 'read', 'readLine', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QIODevicePrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AccessMode(CuteNum):
    """
    The enum 'QIODevicePrivate::AccessMode' of Qt, with the 3 names Qt gives
    in it.
    """

    Unset = Kee[int](0)
    Sequential = Kee[int](1)
    RandomAccess = Kee[int](2)

  class ReadLineOption(CuteFlags, scoped=True):
    """
    The flags enum 'QIODevicePrivate::ReadLineOption' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QIODevicePrivate::ReadLineOptions'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NotNullTerminated = 0x0
    NullTerminated = 0x1

  ReadLineOptions = ReadLineOption

  #  The classes Qt writes inside QIODevicePrivate, each a class in here as
  #  in C++.

  class QRingBufferRef(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QIODevicePrivate::QRingBufferRef: a plain Python
    object standing in front of one C++ QIODevicePrivate::QRingBufferRef.

    C++ hands a QIODevicePrivate::QRingBufferRef around as a copy, so every
    C++ QIODevicePrivate::QRingBufferRef behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QIODevicePrivate::QRingBufferRef that has a ritual
    and that Python can call so far, 15 names in all: 'setChunkSize',
    'chunkSize', 'nextDataBlockSize', 'readPointer', 'free', 'truncate',
    'chop', 'isEmpty', 'getChar', 'size', 'clear', 'read', 'append', 'skip',
    'canReadLine'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'const char
      *QIODevicePrivate::QRingBufferRef::readPointerAtPosition(qint64 pos,
      qint64 &length) const': takes a number to change where it is.
    - Qt's 'char *QIODevicePrivate::QRingBufferRef::reserve(qint64 bytes)':
      gives 'char', which has no cute class yet.
    - Qt's 'char *QIODevicePrivate::QRingBufferRef::reserveFront(qint64
      bytes)': gives 'char', which has no cute class yet.
    - Qt's 'void QIODevicePrivate::QRingBufferRef::putChar(char c)': takes a
      single letter as C has it.
    - Qt's 'void QIODevicePrivate::QRingBufferRef::ungetChar(char c)': takes
      a single letter as C has it.
    - Qt's 'qint64 QIODevicePrivate::QRingBufferRef::indexOf(char c) const':
      takes a single letter as C has it.
    - Qt's 'qint64 QIODevicePrivate::QRingBufferRef::indexOf(char c, qint64
      maxLength, qint64 pos) const': takes a single letter as C has it.
    - Qt's 'qint64 QIODevicePrivate::QRingBufferRef::read(char *data, qint64
      maxLength)': names 'char', which has no cute class yet.
    - Qt's 'qint64 QIODevicePrivate::QRingBufferRef::peek(char *data, qint64
      maxLength, qint64 pos) const': names 'char', which has no cute class
      yet.
    - Qt's 'qint64 QIODevicePrivate::QRingBufferRef::readLine(char *data,
      qint64 maxLength, ReadLineOptions option)': names 'char', which has no
      cute class yet.
    - Qt's 'QIODevicePrivate::QRingBufferRef::~QRingBufferRef()': the
      destructor: Python removes its C++ QIODevicePrivate::QRingBufferRef by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QIODevicePrivate::QRingBufferRef is created at the first use,
      not by 'QIODevicePrivate::QRingBufferRef(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QIODevicePrivate::QRingBufferRef back gives a copy
      the ritual made for Python, in a new cute
      QIODevicePrivate::QRingBufferRef.
    - Each name of Qt's QIODevicePrivate::QRingBufferRef that has no cute
      function yet, 'indexOf', 'peek', 'putChar', 'readLine',
      'readPointerAtPosition', 'reserve', 'reserveFront', 'ungetChar', holds
      a function that raises 'NotImplementedError', and its docstring says
      why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QIODevicePrivate::QRingBufferRef'

    #  Qt's '~QIODevicePrivate::QRingBufferRef()'. Naming it makes this a
    #  value class: Python owns every C++ QIODevicePrivate::QRingBufferRef
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QIODevicePrivate14QRingBufferRefD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def chunkSize(self) -> int:
      """
      Calls Qt's 'int QIODevicePrivate::QRingBufferRef::chunkSize() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#chunkSize
      """
      #  int QIODevicePrivate::QRingBufferRef::chunkSize() const
      return self.uglySide.call(
          'ritual_ZNK16QIODevicePrivate14QRingBufferRef9chunkSizeEv',
      )

    def nextDataBlockSize(self) -> int:
      """
      Calls Qt's 'qint64
      QIODevicePrivate::QRingBufferRef::nextDataBlockSize() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html
      """
      #  qint64 QIODevicePrivate::QRingBufferRef::nextDataBlockSize() const
      return self.uglySide.call(
          'ritual_ZNK16QIODevicePrivate14QRingBufferRef17nextDataBlockSizeE'
          'v',
      )

    def readPointer(self) -> Optional[str]:
      """
      Calls Qt's 'const char *QIODevicePrivate::QRingBufferRef::readPointer()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#readPointer

      Returns
      -------

      Optional[str]
        The text Qt gave back. None when Qt gave back no text.
      """
      #  const char *QIODevicePrivate::QRingBufferRef::readPointer() const
      chars = self.uglySide.call(
          'ritual_ZNK16QIODevicePrivate14QRingBufferRef11readPointerEv',
      )
      return None if chars is None else chars.decode()

    def isEmpty(self) -> bool:
      """
      Calls Qt's 'bool QIODevicePrivate::QRingBufferRef::isEmpty() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#isEmpty
      """
      #  bool QIODevicePrivate::QRingBufferRef::isEmpty() const
      return self.uglySide.call(
          'ritual_ZNK16QIODevicePrivate14QRingBufferRef7isEmptyEv',
      )

    def size(self) -> int:
      """
      Calls Qt's 'qint64 QIODevicePrivate::QRingBufferRef::size() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#size
      """
      #  qint64 QIODevicePrivate::QRingBufferRef::size() const
      return self.uglySide.call(
          'ritual_ZNK16QIODevicePrivate14QRingBufferRef4sizeEv',
      )

    def canReadLine(self) -> bool:
      """
      Calls Qt's 'bool QIODevicePrivate::QRingBufferRef::canReadLine()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#canReadLine
      """
      #  bool QIODevicePrivate::QRingBufferRef::canReadLine() const
      return self.uglySide.call(
          'ritual_ZNK16QIODevicePrivate14QRingBufferRef11canReadLineEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def setChunkSize(self, size: int) -> None:
      """
      Calls Qt's 'void QIODevicePrivate::QRingBufferRef::setChunkSize(int
      size)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html

      Parameters
      ----------

      size : int
        Passed on as it is.
      """
      #  void QIODevicePrivate::QRingBufferRef::setChunkSize(int size)
      self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef12setChunkSizeEi',
          size,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QIODevicePrivate::QRingBufferRef::QRingBufferRef()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html
      """
      #  QIODevicePrivate::QRingBufferRef::QRingBufferRef()
      self._noteCreation(
          QIODevicePrivate.QRingBufferRef, lambda: Rituals.call(
              'ritual_ZN16QIODevicePrivate14QRingBufferRefC1Ev',
          ))

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

    @overload(int)
    def free(self, bytes: int) -> None:
      """
      Calls Qt's 'void QIODevicePrivate::QRingBufferRef::free(qint64 bytes)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#free

      Parameters
      ----------

      bytes : int
        Passed on as it is.
      """
      #  void QIODevicePrivate::QRingBufferRef::free(qint64 bytes)
      self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef4freeEx', bytes,
      )

    @overload(int)
    def truncate(self, pos: int) -> None:
      """
      Calls Qt's 'void QIODevicePrivate::QRingBufferRef::truncate(qint64
      pos)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#truncate

      Parameters
      ----------

      pos : int
        Passed on as it is.
      """
      #  void QIODevicePrivate::QRingBufferRef::truncate(qint64 pos)
      self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef8truncateEx', pos,
      )

    @overload(int)
    def chop(self, bytes: int) -> None:
      """
      Calls Qt's 'void QIODevicePrivate::QRingBufferRef::chop(qint64 bytes)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#chop

      Parameters
      ----------

      bytes : int
        Passed on as it is.
      """
      #  void QIODevicePrivate::QRingBufferRef::chop(qint64 bytes)
      self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef4chopEx', bytes,
      )

    def getChar(self) -> int:
      """
      Calls Qt's 'int QIODevicePrivate::QRingBufferRef::getChar()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#getChar
      """
      #  int QIODevicePrivate::QRingBufferRef::getChar()
      return self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef7getCharEv',
      )

    def clear(self) -> None:
      """
      Calls Qt's 'void QIODevicePrivate::QRingBufferRef::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#clear
      """
      #  void QIODevicePrivate::QRingBufferRef::clear()
      self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef5clearEv',
      )

    def read(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QIODevicePrivate::QRingBufferRef::read()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#read

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QIODevicePrivate::QRingBufferRef::read()
      address = self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef4readEv',
      )
      from . import QByteArray
      return QByteArray._cuteOwning(address)

    @overload(str, int)
    @overload(NoneType, int)
    def append(self, data: Optional[str], size: int) -> None:
      """
      Calls Qt's 'void QIODevicePrivate::QRingBufferRef::append(const char
      *data, qint64 size)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#append

      Parameters
      ----------

      data : Optional[str]
        Passed on as the bytes of the text. None is passed on as no text.

      size : int
        Passed on as it is.
      """
      #  void QIODevicePrivate::QRingBufferRef::append(const char *data,
      #      qint64 size)
      self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef6appendEPKcx',
          self._bytesOf(data), size,
      )

    @overload(QByteArray)
    def append(self, qba: QByteArray) -> None:
      """
      Calls Qt's 'void QIODevicePrivate::QRingBufferRef::append(const
      QByteArray &qba)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#append

      Parameters
      ----------

      qba : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.
      """
      #  void QIODevicePrivate::QRingBufferRef::append(const QByteArray &qba)
      self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef6appendERK10QByteArra'
          'y',
          self._valueOf(qba),
      )

    @overload(int)
    def skip(self, length: int) -> int:
      """
      Calls Qt's 'qint64 QIODevicePrivate::QRingBufferRef::skip(qint64
      length)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiodeviceprivate-qringbufferref.html#skip

      Parameters
      ----------

      length : int
        Passed on as it is.
      """
      #  qint64 QIODevicePrivate::QRingBufferRef::skip(qint64 length)
      return self.uglySide.call(
          'ritual_ZN16QIODevicePrivate14QRingBufferRef4skipEx', length,
      )

    @staticmethod
    def indexOf(*__, **_) -> Never:
      """
      - Qt's 'qint64 QIODevicePrivate::QRingBufferRef::indexOf(char c)
        const': takes a single letter as C has it.
      - Qt's 'qint64 QIODevicePrivate::QRingBufferRef::indexOf(char c, qint64
        maxLength, qint64 pos) const': takes a single letter as C has it.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.indexOf' has no cute function "
          "yet. Qt's 'qint64 QIODevicePrivate::QRingBufferRef::indexOf(char "
          "c) const': takes a single letter as C has it. Qt's 'qint64 "
          "QIODevicePrivate::QRingBufferRef::indexOf(char c, qint64 "
          "maxLength, qint64 pos) const': takes a single letter as C has it."
      )

    @staticmethod
    def peek(*__, **_) -> Never:
      """
      Qt's 'qint64 QIODevicePrivate::QRingBufferRef::peek(char *data, qint64
      maxLength, qint64 pos) const': names 'char', which has no cute class
      yet.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.peek' has no cute function yet. "
          "Qt's 'qint64 QIODevicePrivate::QRingBufferRef::peek(char *data, "
          "qint64 maxLength, qint64 pos) const': names 'char', which has no "
          "cute class yet.")

    @staticmethod
    def putChar(*__, **_) -> Never:
      """
      Qt's 'void QIODevicePrivate::QRingBufferRef::putChar(char c)': takes a
      single letter as C has it.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.putChar' has no cute function "
          "yet. Qt's 'void QIODevicePrivate::QRingBufferRef::putChar(char "
          "c)': takes a single letter as C has it.")

    @staticmethod
    def readLine(*__, **_) -> Never:
      """
      Qt's 'qint64 QIODevicePrivate::QRingBufferRef::readLine(char *data,
      qint64 maxLength, ReadLineOptions option)': names 'char', which has no
      cute class yet.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.readLine' has no cute function "
          "yet. Qt's 'qint64 "
          "QIODevicePrivate::QRingBufferRef::readLine(char *data, qint64 "
          "maxLength, ReadLineOptions option)': names 'char', which has no "
          "cute class yet.")

    @staticmethod
    def readPointerAtPosition(*__, **_) -> Never:
      """
      Qt's 'const char
      *QIODevicePrivate::QRingBufferRef::readPointerAtPosition(qint64 pos,
      qint64 &length) const': takes a number to change where it is.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.readPointerAtPosition' has no "
          "cute function yet. Qt's 'const char "
          "*QIODevicePrivate::QRingBufferRef::readPointerAtPosition(qint64 "
          "pos, qint64 &length) const': takes a number to change where it "
          "is.")

    @staticmethod
    def reserve(*__, **_) -> Never:
      """
      Qt's 'char *QIODevicePrivate::QRingBufferRef::reserve(qint64 bytes)':
      gives 'char', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.reserve' has no cute function "
          "yet. Qt's 'char "
          "*QIODevicePrivate::QRingBufferRef::reserve(qint64 bytes)': gives "
          "'char', which has no cute class yet.")

    @staticmethod
    def reserveFront(*__, **_) -> Never:
      """
      Qt's 'char *QIODevicePrivate::QRingBufferRef::reserveFront(qint64
      bytes)': gives 'char', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.reserveFront' has no cute "
          "function yet. Qt's 'char "
          "*QIODevicePrivate::QRingBufferRef::reserveFront(qint64 bytes)': "
          "gives 'char', which has no cute class yet.")

    @staticmethod
    def ungetChar(*__, **_) -> Never:
      """
      Qt's 'void QIODevicePrivate::QRingBufferRef::ungetChar(char c)': takes
      a single letter as C has it.
      """
      raise NotImplementedError(
          "'QIODevicePrivate.QRingBufferRef.ungetChar' has no cute function "
          "yet. Qt's 'void QIODevicePrivate::QRingBufferRef::ungetChar(char "
          "c)': takes a single letter as C has it.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIODevicePrivate'

  #  A C++ QIODevicePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIODevicePrivate'

  #  The functions Qt calls itself that QIODevicePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'putCharHelper': (
          ('_ZN16QIODevicePrivate13putCharHelperEc',
           ('bool', 'number', ''),
           (
               ('char', 'number', ''),
           )),
      ),
      'peek': (
          ('_ZN16QIODevicePrivate4peekEx',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('long long', 'number', ''),
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

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QIODevicePrivate::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodeviceprivate.html#isSequential
    """
    #  bool QIODevicePrivate::isSequential() const
    return self.uglySide.call('ritual_ZNK16QIODevicePrivate12isSequentialEv')

  def isBufferEmpty(self) -> bool:
    """
    Calls Qt's 'bool QIODevicePrivate::isBufferEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#isBufferEmpty
    """
    #  bool QIODevicePrivate::isBufferEmpty() const
    return self.uglySide.call(
        'ritual_ZNK16QIODevicePrivate13isBufferEmptyEv',
    )

  def allWriteBuffersEmpty(self) -> bool:
    """
    Calls Qt's 'bool QIODevicePrivate::allWriteBuffersEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#allWriteBuffersEmpty
    """
    #  bool QIODevicePrivate::allWriteBuffersEmpty() const
    return self.uglySide.call(
        'ritual_ZNK16QIODevicePrivate20allWriteBuffersEmptyEv',
    )

  @overload(str, int)
  @overload(NoneType, int)
  def isWriteChunkCached(self, data: Optional[str], size: int) -> bool:
    """
    Calls Qt's 'bool QIODevicePrivate::isWriteChunkCached(const char *data,
    qint64 size) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#isWriteChunkCached

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.
    """
    #  bool QIODevicePrivate::isWriteChunkCached(const char *data, qint64
    #      size) const
    return self.uglySide.call(
        'ritual_ZNK16QIODevicePrivate18isWriteChunkCachedEPKcx',
        self._bytesOf(data), size,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentReadChannel(self, channel: int) -> None:
    """
    Calls Qt's 'void QIODevicePrivate::setCurrentReadChannel(int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#setCurrentReadChannel

    Parameters
    ----------

    channel : int
      Passed on as it is.
    """
    #  void QIODevicePrivate::setCurrentReadChannel(int channel)
    self.uglySide.call(
        'ritual_ZN16QIODevicePrivate21setCurrentReadChannelEi', channel,
    )

  @overload(int)
  def setCurrentWriteChannel(self, channel: int) -> None:
    """
    Calls Qt's 'void QIODevicePrivate::setCurrentWriteChannel(int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#setCurrentWriteChannel

    Parameters
    ----------

    channel : int
      Passed on as it is.
    """
    #  void QIODevicePrivate::setCurrentWriteChannel(int channel)
    self.uglySide.call(
        'ritual_ZN16QIODevicePrivate22setCurrentWriteChannelEi', channel,
    )

  @overload(int)
  def setReadChannelCount(self, count: int) -> None:
    """
    Calls Qt's 'void QIODevicePrivate::setReadChannelCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#setReadChannelCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QIODevicePrivate::setReadChannelCount(int count)
    self.uglySide.call(
        'ritual_ZN16QIODevicePrivate19setReadChannelCountEi', count,
    )

  @overload(int)
  def setWriteChannelCount(self, count: int) -> None:
    """
    Calls Qt's 'void QIODevicePrivate::setWriteChannelCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#setWriteChannelCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QIODevicePrivate::setWriteChannelCount(int count)
    self.uglySide.call(
        'ritual_ZN16QIODevicePrivate20setWriteChannelCountEi', count,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QIODevicePrivate::QIODevicePrivate(decltype(QObjectPrivateVersion)
    version)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QIODevicePrivate.__init__' has no cute function yet. Qt's "
        "'QIODevicePrivate::QIODevicePrivate(decltype(QObjectPrivateVersion)"
        " version)': names the enum 'QtPrivate_6_12_0', whose class cannot "
        "be named here.")

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

  def q_func(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QIODevicePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodeviceprivate.html#q_func

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QIODevicePrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QIODevicePrivate6q_funcEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  @overload(int)
  def seekBuffer(self, newPos: int) -> None:
    """
    Calls Qt's 'void QIODevicePrivate::seekBuffer(qint64 newPos)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodeviceprivate.html#seekBuffer

    Parameters
    ----------

    newPos : int
      Passed on as it is.
    """
    #  void QIODevicePrivate::seekBuffer(qint64 newPos)
    self.uglySide.call('ritual_ZN16QIODevicePrivate10seekBufferEx', newPos)

  @overload(int)
  def peek(self, maxSize: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIODevicePrivate::peek(qint64 maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodeviceprivate.html#peek

    Parameters
    ----------

    maxSize : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIODevicePrivate::peek(qint64 maxSize)
    ritual = 'ritual_ZN16QIODevicePrivate4peekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QIODevicePrivate4peekEx'
    address = self.uglySide.call(ritual, maxSize)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def skipByReading(self, maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QIODevicePrivate::skipByReading(qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodeviceprivate.html#skipByReading

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QIODevicePrivate::skipByReading(qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN16QIODevicePrivate13skipByReadingEx', maxSize,
    )

  def skipLine(self) -> int:
    """
    Calls Qt's 'qint64 QIODevicePrivate::skipLine()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodeviceprivate.html#skipLine
    """
    #  qint64 QIODevicePrivate::skipLine()
    return self.uglySide.call('ritual_ZN16QIODevicePrivate8skipLineEv')

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, data: Optional[str], size: int) -> None:
    """
    Calls Qt's 'void QIODevicePrivate::write(const char *data, qint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodeviceprivate.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.
    """
    #  void QIODevicePrivate::write(const char *data, qint64 size)
    self.uglySide.call(
        'ritual_ZN16QIODevicePrivate5writeEPKcx', self._bytesOf(data), size,
    )

  @staticmethod
  def putCharHelper(*__, **_) -> Never:
    """
    Qt's 'bool QIODevicePrivate::putCharHelper(char c)': takes a single
    letter as C has it.
    """
    raise NotImplementedError(
        "'QIODevicePrivate.putCharHelper' has no cute function yet. Qt's "
        "'bool QIODevicePrivate::putCharHelper(char c)': takes a single "
        "letter as C has it.")

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'qint64 QIODevicePrivate::read(char *data, qint64 maxSize, bool
    peeking)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QIODevicePrivate.read' has no cute function yet. Qt's 'qint64 "
        "QIODevicePrivate::read(char *data, qint64 maxSize, bool peeking)': "
        "names 'char', which has no cute class yet.")

  @staticmethod
  def readLine(*__, **_) -> Never:
    """
    Qt's 'qint64 QIODevicePrivate::readLine(char *data, qint64 maxSize,
    ReadLineOption option)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QIODevicePrivate.readLine' has no cute function yet. Qt's 'qint64 "
        "QIODevicePrivate::readLine(char *data, qint64 maxSize, "
        "ReadLineOption option)': names 'char', which has no cute class yet."
    )
