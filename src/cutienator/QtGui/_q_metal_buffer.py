"""
QMetalBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMetalBuffer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QRhiBuffer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMetalBuffer(QRhiBuffer):
  """
  The cute side of Qt's QMetalBuffer: a plain Python object standing in front
  of one C++ QMetalBuffer.

  It is built on the cute 'QRhiBuffer', as Qt's QMetalBuffer is built on Qt's
  QRhiBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMetalBuffer that has a ritual and that Python can
  call so far, 4 names in all: 'destroy', 'create', 'nativeBuffer',
  'endFullDynamicBufferUpdateForCurrentFrame'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char *QMetalBuffer::beginFullDynamicBufferUpdateForCurrentFrame()':
    gives 'char', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QMetalBuffer is created at the first use, not by
    'QMetalBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetalBuffer.
  - Each name of Qt's QMetalBuffer that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetalBuffer'

  #  A C++ QMetalBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMetalBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QMetalBuffer::QMetalBuffer(QRhiImplementation *rhi, Type type,
    UsageFlags usage, quint32 size)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QMetalBuffer.__init__' has no cute function yet. Qt's "
        "'QMetalBuffer::QMetalBuffer(QRhiImplementation *rhi, Type type, "
        "UsageFlags usage, quint32 size)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QMetalBuffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetalbuffer.html#destroy
    """
    #  void QMetalBuffer::destroy()
    self.uglySide.call('ritual_ZN12QMetalBuffer7destroyEv')

  def create(self) -> bool:
    """
    Calls Qt's 'bool QMetalBuffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetalbuffer.html#create
    """
    #  bool QMetalBuffer::create()
    return self.uglySide.call('ritual_ZN12QMetalBuffer6createEv')

  def nativeBuffer(self) -> QRhiBuffer.NativeBuffer:
    """
    Calls Qt's 'QRhiBuffer::NativeBuffer QMetalBuffer::nativeBuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qmetalbuffer.html#nativeBuffer

    Returns
    -------

    QRhiBuffer.NativeBuffer
      A new cute QRhiBuffer::NativeBuffer around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiBuffer::NativeBuffer QMetalBuffer::nativeBuffer()
    address = self.uglySide.call('ritual_ZN12QMetalBuffer12nativeBufferEv')
    return QRhiBuffer.NativeBuffer._cuteOwning(address)

  def endFullDynamicBufferUpdateForCurrentFrame(self) -> None:
    """
    Calls Qt's 'void
    QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetalbuffer.html
    """
    #  void QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame()
    self.uglySide.call(
        'ritual_ZN12QMetalBuffer41endFullDynamicBufferUpdateForCurrentFrame'
        'Ev',
    )
