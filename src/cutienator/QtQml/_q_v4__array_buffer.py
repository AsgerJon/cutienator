"""
QV4::ArrayBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ArrayBuffer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ArrayBuffer(QV4.SharedArrayBuffer):
  """
  The cute side of Qt's QV4::ArrayBuffer: a plain Python object standing in
  front of one C++ QV4::ArrayBuffer.

  It is built on the cute 'QV4::SharedArrayBuffer', as Qt's QV4::ArrayBuffer
  is built on Qt's QV4::SharedArrayBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ArrayBuffer that has a ritual and that Python
  can call so far, 11 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'defaultPrototype', 'asByteArray', 'arrayDataLength',
  'constArrayData', 'hasSharedArrayData', 'detachArrayData', 'detach'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::ArrayBuffer::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'char *QV4::ArrayBuffer::dataData()': gives 'char', which has no
    cute class yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::ArrayBuffer is created at the first use, not by
    'QV4::ArrayBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ArrayBuffer.
  - Each name of Qt's QV4::ArrayBuffer that has no cute function yet,
    'dataData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::ArrayBuffer::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybuffer.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ArrayBuffer::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV411ArrayBuffer14virtualDestroyEPNS_4Heap4BaseE',
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
    *QV4::ArrayBuffer::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybuffer.html#defaultPrototype

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
    #  QV4::Object *QV4::ArrayBuffer::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV411ArrayBuffer16defaultPrototypeEPNS_15ExecutionEngine'
        'E',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ArrayBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ArrayBuffer]:
    """
    Calls Qt's 'QV4::Heap::ArrayBuffer *QV4::ArrayBuffer::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraybuffer.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ArrayBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArrayBuffer *QV4::ArrayBuffer::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV411ArrayBuffer11d_uncheckedEv',
    )
    return QV4.Heap.ArrayBuffer._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ArrayBuffer]:
    """
    Calls Qt's 'QV4::Heap::ArrayBuffer *QV4::ArrayBuffer::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraybuffer.html#d

    Returns
    -------

    Optional[QV4.Heap.ArrayBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArrayBuffer *QV4::ArrayBuffer::d() const
    address = self.uglySide.call('ritual_ZNK3QV411ArrayBuffer1dEv')
    return QV4.Heap.ArrayBuffer._cuteAt(address)

  def asByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QV4::ArrayBuffer::asByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraybuffer.html#asByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QV4::ArrayBuffer::asByteArray() const
    address = self.uglySide.call(
        'ritual_ZNK3QV411ArrayBuffer11asByteArrayEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def arrayDataLength(self) -> int:
    """
    Calls Qt's 'uint QV4::ArrayBuffer::arrayDataLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybuffer.html#arrayDataLength
    """
    #  uint QV4::ArrayBuffer::arrayDataLength() const
    return self.uglySide.call(
        'ritual_ZNK3QV411ArrayBuffer15arrayDataLengthEv',
    )

  def constArrayData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QV4::ArrayBuffer::constArrayData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybuffer.html#constArrayData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QV4::ArrayBuffer::constArrayData() const
    chars = self.uglySide.call(
        'ritual_ZNK3QV411ArrayBuffer14constArrayDataEv',
    )
    return None if chars is None else chars.decode()

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
    Calls Qt's 'void QV4::ArrayBuffer::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraybuffer.html#__dataTest
    """
    #  void QV4::ArrayBuffer::__dataTest()
    self.uglySide.call('ritual_ZN3QV411ArrayBuffer10__dataTestEv')

  def hasSharedArrayData(self) -> bool:
    """
    Calls Qt's 'bool QV4::ArrayBuffer::hasSharedArrayData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybuffer.html#hasSharedArrayData
    """
    #  bool QV4::ArrayBuffer::hasSharedArrayData()
    return self.uglySide.call(
        'ritual_ZN3QV411ArrayBuffer18hasSharedArrayDataEv',
    )

  def detachArrayData(self) -> None:
    """
    Calls Qt's 'void QV4::ArrayBuffer::detachArrayData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraybuffer.html#detachArrayData
    """
    #  void QV4::ArrayBuffer::detachArrayData()
    self.uglySide.call('ritual_ZN3QV411ArrayBuffer15detachArrayDataEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QV4::ArrayBuffer::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraybuffer.html#detach
    """
    #  void QV4::ArrayBuffer::detach()
    self.uglySide.call('ritual_ZN3QV411ArrayBuffer6detachEv')

  @staticmethod
  def dataData(*__, **_) -> Never:
    """
    Qt's 'char *QV4::ArrayBuffer::dataData()': gives 'char', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ArrayBuffer.dataData' has no cute function yet. Qt's 'char "
        "*QV4::ArrayBuffer::dataData()': gives 'char', which has no cute "
        "class yet.")
