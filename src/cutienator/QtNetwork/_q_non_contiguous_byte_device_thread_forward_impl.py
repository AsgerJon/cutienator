"""
QNonContiguousByteDeviceThreadForwardImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNonContiguousByteDeviceThreadForwardImpl to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QNonContiguousByteDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QNonContiguousByteDeviceThreadForwardImpl(QNonContiguousByteDevice):
  """
  The cute side of Qt's QNonContiguousByteDeviceThreadForwardImpl: a plain
  Python object standing in front of one C++
  QNonContiguousByteDeviceThreadForwardImpl.

  It is built on the cute 'QNonContiguousByteDevice', as Qt's
  QNonContiguousByteDeviceThreadForwardImpl is built on Qt's
  QNonContiguousByteDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNonContiguousByteDeviceThreadForwardImpl that has a
  ritual and that Python can call so far, 9 names in all: 'metaObject',
  'pos', 'advanceReadPointer', 'atEnd', 'reset', 'size', 'haveDataSlot',
  'wantData', 'processedData'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNonContiguousByteDeviceThreadForwardImpl::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QNonContiguousByteDeviceThreadForwardImpl::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNonContiguousByteDeviceThreadForwardImpl::
    ~QNonContiguousByteDeviceThreadForwardImpl()': the destructor: Python
    never removes a C++ QNonContiguousByteDeviceThreadForwardImpl.
  - Qt's 'const char
    *QNonContiguousByteDeviceThreadForwardImpl::readPointer(qint64
    maximumLength, qint64 &len)': takes a number to change where it is.
  - Qt's 'void QNonContiguousByteDeviceThreadForwardImpl::resetData(bool
    *b)': takes a number to change where it is.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QNonContiguousByteDeviceThreadForwardImpl.

  What to expect
  --------------

  - The C++ QNonContiguousByteDeviceThreadForwardImpl is created at the first
    use, not by 'QNonContiguousByteDeviceThreadForwardImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNonContiguousByteDeviceThreadForwardImpl.
  - Qt tells when it has removed the C++
    QNonContiguousByteDeviceThreadForwardImpl. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QNonContiguousByteDeviceThreadForwardImpl that has no
    cute function yet, '__init__', 'resetData', holds a function that raises
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
  __qt_class__ = 'QNonContiguousByteDeviceThreadForwardImpl'

  #  A C++ QNonContiguousByteDeviceThreadForwardImpl Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNonContiguousByteDeviceThreadForwardImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QNonContiguousByteDeviceThreadForwardImpl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QNonContiguousByteDeviceThreadForwardImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl10metaObjectE'
        'v',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDeviceThreadForwardImpl::pos()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html#pos
    """
    #  qint64 QNonContiguousByteDeviceThreadForwardImpl::pos() const
    ritual = 'ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl3posEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl3posEv')
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDeviceThreadForwardImpl::atEnd()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html
    """
    #  bool QNonContiguousByteDeviceThreadForwardImpl::atEnd() const
    ritual = 'ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl5atEndEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl5atEndE'
          'v')
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDeviceThreadForwardImpl::size()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html
    """
    #  qint64 QNonContiguousByteDeviceThreadForwardImpl::size() const
    ritual = 'ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl4sizeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl4sizeEv')
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
    Qt's 'QNonContiguousByteDeviceThreadForwardImpl::
    QNonContiguousByteDeviceThreadForwardImpl(bool aE, qint64 s)': leans on
    'QNonContiguousByteDeviceThreadForwardImpl::qt_metacall(QMetaObject::
    Call, int, void**)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNonContiguousByteDeviceThreadForwardImpl.__init__' has no cute "
        "function yet. Qt's "
        "'QNonContiguousByteDeviceThreadForwardImpl::QNonContiguousByteDevic"
        "eThreadForwardImpl(bool aE, qint64 s)': leans on "
        "'QNonContiguousByteDeviceThreadForwardImpl::qt_metacall(QMetaObject"
        "::Call, int, void**)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

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
  def advanceReadPointer(self, a: int) -> bool:
    """
    Calls Qt's 'bool
    QNonContiguousByteDeviceThreadForwardImpl::advanceReadPointer(qint64 a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  bool QNonContiguousByteDeviceThreadForwardImpl::advanceReadPointer(
    #      qint64 a)
    return self.uglySide.call(
        'ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl18advanceReadP'
        'ointerEx',
        a,
    )

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDeviceThreadForwardImpl::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html
    """
    #  bool QNonContiguousByteDeviceThreadForwardImpl::reset()
    return self.uglySide.call(
        'ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl5resetEv',
    )

  @overload(int, QByteArray, bool, int)
  def haveDataSlot(
      self,
      pos: int,
      dataArray: QByteArray,
      dataAtEnd: bool,
      dataSize: int,
  ) -> None:
    """
    Calls Qt's 'void
    QNonContiguousByteDeviceThreadForwardImpl::haveDataSlot(qint64 pos, const
    QByteArray &dataArray, bool dataAtEnd, qint64 dataSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html

    Parameters
    ----------

    pos : int
      Passed on as it is.

    dataArray : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    dataAtEnd : bool
      Passed on as it is.

    dataSize : int
      Passed on as it is.
    """
    #  void QNonContiguousByteDeviceThreadForwardImpl::haveDataSlot(qint64
    #      pos, const QByteArray &dataArray, bool dataAtEnd, qint64 dataSize)
    self.uglySide.call(
        'ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl12haveDataSlot'
        'ExRK10QByteArraybx',
        pos, self._valueOf(dataArray), dataAtEnd, dataSize,
    )

  @overload(int)
  def wantData(self, a0: int) -> None:
    """
    Calls Qt's 'void
    QNonContiguousByteDeviceThreadForwardImpl::wantData(qint64 a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QNonContiguousByteDeviceThreadForwardImpl::wantData(qint64 a0)
    self.uglySide.call(
        'ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl8wantDataEx',
        a0,
    )

  @overload(int, int)
  def processedData(self, pos: int, amount: int) -> None:
    """
    Calls Qt's 'void
    QNonContiguousByteDeviceThreadForwardImpl::processedData(qint64 pos,
    qint64 amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicethreadforwardimpl.html

    Parameters
    ----------

    pos : int
      Passed on as it is.

    amount : int
      Passed on as it is.
    """
    #  void QNonContiguousByteDeviceThreadForwardImpl::processedData(qint64
    #      pos, qint64 amount)
    self.uglySide.call(
        'ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl13processedDat'
        'aExx',
        pos, amount,
    )

  @staticmethod
  def resetData(*__, **_) -> Never:
    """
    Qt's 'void QNonContiguousByteDeviceThreadForwardImpl::resetData(bool
    *b)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QNonContiguousByteDeviceThreadForwardImpl.resetData' has no cute "
        "function yet. Qt's 'void "
        "QNonContiguousByteDeviceThreadForwardImpl::resetData(bool *b)': "
        "takes a number to change where it is.")
