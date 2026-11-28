"""
QNonContiguousByteDeviceIoDeviceImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNonContiguousByteDeviceIoDeviceImpl to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QNonContiguousByteDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject


class QNonContiguousByteDeviceIoDeviceImpl(QNonContiguousByteDevice):
  """
  The cute side of Qt's QNonContiguousByteDeviceIoDeviceImpl: a plain Python
  object standing in front of one C++ QNonContiguousByteDeviceIoDeviceImpl.

  It is built on the cute 'QNonContiguousByteDevice', as Qt's
  QNonContiguousByteDeviceIoDeviceImpl is built on Qt's
  QNonContiguousByteDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNonContiguousByteDeviceIoDeviceImpl that has a
  ritual and that Python can call so far, 6 names in all: 'metaObject',
  'advanceReadPointer', 'atEnd', 'reset', 'size', 'pos'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNonContiguousByteDeviceIoDeviceImpl::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QNonContiguousByteDeviceIoDeviceImpl::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNonContiguousByteDeviceIoDeviceImpl::
    ~QNonContiguousByteDeviceIoDeviceImpl()': the destructor: Python never
    removes a C++ QNonContiguousByteDeviceIoDeviceImpl.
  - Qt's 'const char
    *QNonContiguousByteDeviceIoDeviceImpl::readPointer(qint64 maximumLength,
    qint64 &len)': takes a number to change where it is.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QNonContiguousByteDeviceIoDeviceImpl.

  What to expect
  --------------

  - The C++ QNonContiguousByteDeviceIoDeviceImpl is created at the first use,
    not by 'QNonContiguousByteDeviceIoDeviceImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNonContiguousByteDeviceIoDeviceImpl.
  - Qt tells when it has removed the C++
    QNonContiguousByteDeviceIoDeviceImpl. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's QNonContiguousByteDeviceIoDeviceImpl that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QNonContiguousByteDeviceIoDeviceImpl'

  #  A C++ QNonContiguousByteDeviceIoDeviceImpl Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNonContiguousByteDeviceIoDeviceImpl'

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
    *QNonContiguousByteDeviceIoDeviceImpl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedeviceiodeviceimpl.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNonContiguousByteDeviceIoDeviceImpl::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDeviceIoDeviceImpl::atEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedeviceiodeviceimpl.html#atEnd
    """
    #  bool QNonContiguousByteDeviceIoDeviceImpl::atEnd() const
    ritual = 'ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK36QNonContiguousByteDeviceIoDeviceImpl5atEndEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDeviceIoDeviceImpl::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedeviceiodeviceimpl.html#size
    """
    #  qint64 QNonContiguousByteDeviceIoDeviceImpl::size() const
    ritual = 'ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK36QNonContiguousByteDeviceIoDeviceImpl4sizeEv'
    return self.uglySide.call(ritual)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDeviceIoDeviceImpl::pos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedeviceiodeviceimpl.html#pos
    """
    #  qint64 QNonContiguousByteDeviceIoDeviceImpl::pos() const
    ritual = 'ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK36QNonContiguousByteDeviceIoDeviceImpl3posEv'
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
    Qt's 'QNonContiguousByteDeviceIoDeviceImpl::
    QNonContiguousByteDeviceIoDeviceImpl(QIODevice *d)': leans on
    'QNonContiguousByteDeviceIoDeviceImpl::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNonContiguousByteDeviceIoDeviceImpl.__init__' has no cute "
        "function yet. Qt's "
        "'QNonContiguousByteDeviceIoDeviceImpl::QNonContiguousByteDeviceIoDe"
        "viceImpl(QIODevice *d)': leans on "
        "'QNonContiguousByteDeviceIoDeviceImpl::qt_metacall(QMetaObject::Cal"
        "l, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
  def advanceReadPointer(self, amount: int) -> bool:
    """
    Calls Qt's 'bool
    QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(qint64 amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedeviceiodeviceimpl.html

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  bool QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(qint64
    #      amount)
    ritual = (
        'ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl18advanceReadPointe'
        'rEx')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QNonContiguousByteDeviceIoDeviceImpl18advanceRead'
          'PointerEx')
    return self.uglySide.call(ritual, amount)

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDeviceIoDeviceImpl::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedeviceiodeviceimpl.html#reset
    """
    #  bool QNonContiguousByteDeviceIoDeviceImpl::reset()
    ritual = 'ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN36QNonContiguousByteDeviceIoDeviceImpl5resetEv'
    return self.uglySide.call(ritual)
