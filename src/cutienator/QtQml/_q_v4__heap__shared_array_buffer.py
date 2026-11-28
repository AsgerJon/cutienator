"""
QV4::Heap::SharedArrayBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::SharedArrayBuffer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class SharedArrayBuffer(QV4.Heap.Object):
  """
  The cute side of Qt's QV4::Heap::SharedArrayBuffer: a plain Python object
  standing in front of one C++ QV4::Heap::SharedArrayBuffer.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::SharedArrayBuffer is built on Qt's QV4::Heap::Object, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::SharedArrayBuffer that has a ritual and
  that Python can call so far, 10 names in all: 'init', 'destroy',
  'setSharedArrayBuffer', 'isSharedArrayBuffer', 'constArrayData',
  'arrayDataLength', 'hasSharedArrayData', 'hasDetachedArrayData',
  'detachArrayData', 'arrayDataNeedsDetach'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char *QV4::Heap::SharedArrayBuffer::arrayData()': gives 'char',
    which has no cute class yet.
  - Qt's 'const QArrayDataPointer<const char>
    &QV4::Heap::SharedArrayBuffer::constArrayDataPointer() const': gives a
    type Python has no way to take yet.
  - Qt's 'QArrayDataPointer<char>
    &QV4::Heap::SharedArrayBuffer::arrayDataPointer()': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QV4::Heap::SharedArrayBuffer is created at the first use, not by
    'QV4::Heap::SharedArrayBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::SharedArrayBuffer.
  - Each name of Qt's QV4::Heap::SharedArrayBuffer that has no cute function
    yet, 'arrayDataPointer', 'constArrayDataPointer', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::SharedArrayBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSharedArrayBuffer(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::SharedArrayBuffer::isSharedArrayBuffer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html
    """
    #  bool QV4::Heap::SharedArrayBuffer::isSharedArrayBuffer() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap17SharedArrayBuffer19isSharedArrayBufferEv',
    )

  def constArrayData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QV4::Heap::SharedArrayBuffer::constArrayData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html#constArrayData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QV4::Heap::SharedArrayBuffer::constArrayData() const
    chars = self.uglySide.call(
        'ritual_ZNK3QV44Heap17SharedArrayBuffer14constArrayDataEv',
    )
    return None if chars is None else chars.decode()

  def arrayDataLength(self) -> int:
    """
    Calls Qt's 'uint QV4::Heap::SharedArrayBuffer::arrayDataLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html#arrayDataLength
    """
    #  uint QV4::Heap::SharedArrayBuffer::arrayDataLength() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap17SharedArrayBuffer15arrayDataLengthEv',
    )

  def hasSharedArrayData(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::SharedArrayBuffer::hasSharedArrayData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html#hasSharedArrayData
    """
    #  bool QV4::Heap::SharedArrayBuffer::hasSharedArrayData() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap17SharedArrayBuffer18hasSharedArrayDataEv',
    )

  def hasDetachedArrayData(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::SharedArrayBuffer::hasDetachedArrayData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html
    """
    #  bool QV4::Heap::SharedArrayBuffer::hasDetachedArrayData() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap17SharedArrayBuffer20hasDetachedArrayDataEv',
    )

  def arrayDataNeedsDetach(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::SharedArrayBuffer::arrayDataNeedsDetach()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html
    """
    #  bool QV4::Heap::SharedArrayBuffer::arrayDataNeedsDetach() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap17SharedArrayBuffer20arrayDataNeedsDetachEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSharedArrayBuffer(self, shared: bool) -> None:
    """
    Calls Qt's 'void QV4::Heap::SharedArrayBuffer::setSharedArrayBuffer(bool
    shared)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html

    Parameters
    ----------

    shared : bool
      Passed on as it is.
    """
    #  void QV4::Heap::SharedArrayBuffer::setSharedArrayBuffer(bool shared)
    self.uglySide.call(
        'ritual_ZN3QV44Heap17SharedArrayBuffer20setSharedArrayBufferEb',
        shared,
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

  @overload(int)
  def init(self, length: int) -> None:
    """
    Calls Qt's 'void QV4::Heap::SharedArrayBuffer::init(size_t length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html#init

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QV4::Heap::SharedArrayBuffer::init(size_t length)
    self.uglySide.call(
        'ritual_ZN3QV44Heap17SharedArrayBuffer4initEm', length,
    )

  @overload(QByteArray)
  def init(self, array: QByteArray) -> None:
    """
    Calls Qt's 'void QV4::Heap::SharedArrayBuffer::init(const QByteArray
    &array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html#init

    Parameters
    ----------

    array : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QV4::Heap::SharedArrayBuffer::init(const QByteArray &array)
    self.uglySide.call(
        'ritual_ZN3QV44Heap17SharedArrayBuffer4initERK10QByteArray',
        self._valueOf(array),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::SharedArrayBuffer::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html#destroy
    """
    #  void QV4::Heap::SharedArrayBuffer::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap17SharedArrayBuffer7destroyEv')

  def detachArrayData(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::SharedArrayBuffer::detachArrayData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-sharedarraybuffer.html#detachArrayData
    """
    #  void QV4::Heap::SharedArrayBuffer::detachArrayData()
    self.uglySide.call(
        'ritual_ZN3QV44Heap17SharedArrayBuffer15detachArrayDataEv',
    )

  @staticmethod
  def arrayDataPointer(*__, **_) -> Never:
    """
    Qt's 'QArrayDataPointer<char>
    &QV4::Heap::SharedArrayBuffer::arrayDataPointer()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.SharedArrayBuffer.arrayDataPointer' has no cute function "
        "yet. Qt's 'QArrayDataPointer<char> "
        "&QV4::Heap::SharedArrayBuffer::arrayDataPointer()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constArrayDataPointer(*__, **_) -> Never:
    """
    Qt's 'const QArrayDataPointer<const char>
    &QV4::Heap::SharedArrayBuffer::constArrayDataPointer() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.SharedArrayBuffer.constArrayDataPointer' has no cute "
        "function yet. Qt's 'const QArrayDataPointer<const char> "
        "&QV4::Heap::SharedArrayBuffer::constArrayDataPointer() const': "
        "gives a type Python has no way to take yet.")
