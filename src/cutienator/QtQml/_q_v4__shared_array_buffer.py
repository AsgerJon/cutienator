"""
QV4::SharedArrayBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::SharedArrayBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SharedArrayBuffer(QV4.Object):
  """
  The cute side of Qt's QV4::SharedArrayBuffer: a plain Python object
  standing in front of one C++ QV4::SharedArrayBuffer.

  It is built on the cute 'QV4::Object', as Qt's QV4::SharedArrayBuffer is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::SharedArrayBuffer that has a ritual and that
  Python can call so far, 10 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'defaultPrototype', 'arrayDataLength', 'constArrayData',
  'hasSharedArrayData', 'hasDetachedArrayData', 'isSharedArrayBuffer'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::SharedArrayBuffer::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'char *QV4::SharedArrayBuffer::arrayData()': gives 'char', which has
    no cute class yet.

  What has no ritual
  ------------------

  5 of the 17 functions Qt declares: 3 forbidden; 1 not a gap; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QV4::SharedArrayBuffer is created at the first use, not by
    'QV4::SharedArrayBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::SharedArrayBuffer.
  - Each name of Qt's QV4::SharedArrayBuffer that has no cute function yet,
    'asByteArray', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::SharedArrayBuffer::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SharedArrayBuffer::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV417SharedArrayBuffer14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::SharedArrayBuffer::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object
    #      *QV4::SharedArrayBuffer::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV417SharedArrayBuffer16defaultPrototypeEPNS_15Execution'
        'EngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SharedArrayBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.SharedArrayBuffer]:
    """
    Calls Qt's 'QV4::Heap::SharedArrayBuffer
    *QV4::SharedArrayBuffer::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.SharedArrayBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::SharedArrayBuffer *QV4::SharedArrayBuffer::d_unchecked()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV417SharedArrayBuffer11d_uncheckedEv',
    )
    return QV4.Heap.SharedArrayBuffer._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.SharedArrayBuffer]:
    """
    Calls Qt's 'QV4::Heap::SharedArrayBuffer *QV4::SharedArrayBuffer::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#d

    Returns
    -------

    Optional[QV4.Heap.SharedArrayBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::SharedArrayBuffer *QV4::SharedArrayBuffer::d() const
    address = self.uglySide.call('ritual_ZNK3QV417SharedArrayBuffer1dEv')
    return QV4.Heap.SharedArrayBuffer._cuteAt(address)

  def arrayDataLength(self) -> int:
    """
    Calls Qt's 'uint QV4::SharedArrayBuffer::arrayDataLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#arrayDataLength
    """
    #  uint QV4::SharedArrayBuffer::arrayDataLength() const
    return self.uglySide.call(
        'ritual_ZNK3QV417SharedArrayBuffer15arrayDataLengthEv',
    )

  def constArrayData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QV4::SharedArrayBuffer::constArrayData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#constArrayData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QV4::SharedArrayBuffer::constArrayData() const
    chars = self.uglySide.call(
        'ritual_ZNK3QV417SharedArrayBuffer14constArrayDataEv',
    )
    return None if chars is None else chars.decode()

  def hasDetachedArrayData(self) -> bool:
    """
    Calls Qt's 'bool QV4::SharedArrayBuffer::hasDetachedArrayData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#hasDetachedArrayData
    """
    #  bool QV4::SharedArrayBuffer::hasDetachedArrayData() const
    return self.uglySide.call(
        'ritual_ZNK3QV417SharedArrayBuffer20hasDetachedArrayDataEv',
    )

  def isSharedArrayBuffer(self) -> bool:
    """
    Calls Qt's 'bool QV4::SharedArrayBuffer::isSharedArrayBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#isSharedArrayBuffer
    """
    #  bool QV4::SharedArrayBuffer::isSharedArrayBuffer() const
    return self.uglySide.call(
        'ritual_ZNK3QV417SharedArrayBuffer19isSharedArrayBufferEv',
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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::SharedArrayBuffer::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#__dataTest
    """
    #  void QV4::SharedArrayBuffer::__dataTest()
    self.uglySide.call('ritual_ZN3QV417SharedArrayBuffer10__dataTestEv')

  def hasSharedArrayData(self) -> bool:
    """
    Calls Qt's 'bool QV4::SharedArrayBuffer::hasSharedArrayData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sharedarraybuffer.html#hasSharedArrayData
    """
    #  bool QV4::SharedArrayBuffer::hasSharedArrayData()
    return self.uglySide.call(
        'ritual_ZN3QV417SharedArrayBuffer18hasSharedArrayDataEv',
    )

  @staticmethod
  def asByteArray(*__, **_) -> Never:
    """
    Qt's 'QByteArray QV4::SharedArrayBuffer::asByteArray() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QV4.SharedArrayBuffer.asByteArray' has no cute function yet. Qt's "
        "'QByteArray QV4::SharedArrayBuffer::asByteArray() const': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
