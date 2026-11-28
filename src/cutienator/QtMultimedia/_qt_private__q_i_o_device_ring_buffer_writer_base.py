"""
QtPrivate::QIODeviceRingBufferWriterBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudio_qiodevice_support_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtPrivate::QIODeviceRingBufferWriterBase to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QIODevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QIODeviceRingBufferWriterBase(QIODevice):
  """
  The cute side of Qt's QtPrivate::QIODeviceRingBufferWriterBase: a plain
  Python object standing in front of one C++
  QtPrivate::QIODeviceRingBufferWriterBase.

  It is built on the cute 'QIODevice', as Qt's
  QtPrivate::QIODeviceRingBufferWriterBase is built on Qt's QIODevice, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtPrivate::QIODeviceRingBufferWriterBase that has a
  ritual and that Python can call so far, 2 names in all:
  'bytesConsumedFromRingbuffer', 'isSequential'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QtPrivate::QIODeviceRingBufferWriterBase is created at the first
    use, not by 'QtPrivate::QIODeviceRingBufferWriterBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPrivate::QIODeviceRingBufferWriterBase.
  - Qt tells when it has removed the C++
    QtPrivate::QIODeviceRingBufferWriterBase. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QtPrivate::QIODeviceRingBufferWriterBase that has no
    cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QtPrivate::QIODeviceRingBufferWriterBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QIODeviceRingBufferWriterBase::isSequential()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiodeviceringbufferwriterbase.html
    """
    #  bool QtPrivate::QIODeviceRingBufferWriterBase::isSequential() const
    ritual = (
        'ritual_ZNK9QtPrivate29QIODeviceRingBufferWriterBase12isSequentialE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9QtPrivate29QIODeviceRingBufferWriterBase12isSeque'
          'ntialEv')
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
    Qt's
    'QtPrivate::QIODeviceRingBufferWriterBase::QIODeviceRingBufferWriterBase(
    QObject *parent)': the class is abstract, so C++ cannot make one, and the
    C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QtPrivate.QIODeviceRingBufferWriterBase.__init__' has no cute "
        "function yet. Qt's "
        "'QtPrivate::QIODeviceRingBufferWriterBase::QIODeviceRingBufferWrite"
        "rBase(QObject *parent)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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
  def bytesConsumedFromRingbuffer(self, bytes: int) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QIODeviceRingBufferWriterBase::bytesConsumedFromRingbuffer(
    qint64 bytes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiodeviceringbufferwriterbase.html

    Parameters
    ----------

    bytes : int
      Passed on as it is.
    """
    #  void QtPrivate::QIODeviceRingBufferWriterBase::
    #      bytesConsumedFromRingbuffer(qint64 bytes)
    self.uglySide.call(
        'ritual_ZN9QtPrivate29QIODeviceRingBufferWriterBase27bytesConsumedF'
        'romRingbufferEx',
        bytes,
    )
