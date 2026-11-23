"""
QNonContiguousByteDeviceByteArrayImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNonContiguousByteDeviceByteArrayImpl to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QNonContiguousByteDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject


class QNonContiguousByteDeviceByteArrayImpl(QNonContiguousByteDevice):
  """
  The cute side of Qt's QNonContiguousByteDeviceByteArrayImpl: a plain Python
  object standing in front of one C++ QNonContiguousByteDeviceByteArrayImpl.

  It is built on the cute 'QNonContiguousByteDevice', as Qt's
  QNonContiguousByteDeviceByteArrayImpl is built on Qt's
  QNonContiguousByteDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNonContiguousByteDeviceByteArrayImpl that has a
  ritual and that Python can call so far, 6 names in all: 'metaObject',
  'advanceReadPointer', 'atEnd', 'reset', 'size', 'pos'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNonContiguousByteDeviceByteArrayImpl::
    ~QNonContiguousByteDeviceByteArrayImpl()': the destructor: Python never
    removes a C++ QNonContiguousByteDeviceByteArrayImpl.
  - Qt's 'const char
    *QNonContiguousByteDeviceByteArrayImpl::readPointer(qint64 maximumLength,
    qint64 &len)': takes a number to change where it is.

  What has no ritual
  ------------------

  7 of the 15 functions Qt declares: 3 leans on
  'QNonContiguousByteDeviceByteArrayImpl; 2 takes or gives a type that cannot
  be passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QNonContiguousByteDeviceByteArrayImpl is created at the first
    use, not by 'QNonContiguousByteDeviceByteArrayImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNonContiguousByteDeviceByteArrayImpl.
  - Qt tells when it has removed the C++
    QNonContiguousByteDeviceByteArrayImpl. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNonContiguousByteDeviceByteArrayImpl'

  #  A C++ QNonContiguousByteDeviceByteArrayImpl Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNonContiguousByteDeviceByteArrayImpl'

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
    *QNonContiguousByteDeviceByteArrayImpl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicebytearrayimpl.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNonContiguousByteDeviceByteArrayImpl::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDeviceByteArrayImpl::atEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicebytearrayimpl.html#atEnd
    """
    #  bool QNonContiguousByteDeviceByteArrayImpl::atEnd() const
    ritual = 'ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl5atEndEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK37QNonContiguousByteDeviceByteArrayImpl5atEndEv')
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDeviceByteArrayImpl::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicebytearrayimpl.html#size
    """
    #  qint64 QNonContiguousByteDeviceByteArrayImpl::size() const
    ritual = 'ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK37QNonContiguousByteDeviceByteArrayImpl4sizeEv'
    return self.uglySide.call(ritual)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QNonContiguousByteDeviceByteArrayImpl::pos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicebytearrayimpl.html#pos
    """
    #  qint64 QNonContiguousByteDeviceByteArrayImpl::pos() const
    ritual = 'ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK37QNonContiguousByteDeviceByteArrayImpl3posEv'
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
    QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(qint64
    amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicebytearrayimpl.html

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  bool QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(qint64
    #      amount)
    ritual = (
        'ritual_ZN37QNonContiguousByteDeviceByteArrayImpl18advanceReadPoint'
        'erEx')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QNonContiguousByteDeviceByteArrayImpl18advanceRea'
          'dPointerEx')
    return self.uglySide.call(ritual, amount)

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QNonContiguousByteDeviceByteArrayImpl::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnoncontiguousbytedevicebytearrayimpl.html#reset
    """
    #  bool QNonContiguousByteDeviceByteArrayImpl::reset()
    ritual = 'ritual_ZN37QNonContiguousByteDeviceByteArrayImpl5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN37QNonContiguousByteDeviceByteArrayImpl5resetEv'
    return self.uglySide.call(ritual)
