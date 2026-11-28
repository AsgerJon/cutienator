"""
QSSGRhiBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiBuffer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtGui import QRhiCommandBuffer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiBuffer


class QSSGRhiBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiBuffer: a plain Python object standing in
  front of one C++ QSSGRhiBuffer.

  What exists
  -----------

  Every function of Qt's QSSGRhiBuffer that has a ritual and that Python can
  call so far, 4 names in all: 'buffer', 'stride', 'numVertices',
  'indexFormat'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiBuffer::QSSGRhiBuffer(QSSGRhiContext &context,
    QRhiBuffer::Type type, QRhiBuffer::UsageFlags usageMask, quint32 stride,
    qsizetype size, QRhiCommandBuffer::IndexFormat indexFormat)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGRhiBuffer::~QSSGRhiBuffer()': the destructor: Python never
    removes a C++ QSSGRhiBuffer.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRhiBuffer is created at the first use, not by
    'QSSGRhiBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRhiBuffer.
  - Each name of Qt's QSSGRhiBuffer that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def buffer(self) -> Optional[QRhiBuffer]:
    """
    Calls Qt's 'QRhiBuffer *QSSGRhiBuffer::buffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhibuffer.html#buffer

    Returns
    -------

    Optional[QRhiBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiBuffer *QSSGRhiBuffer::buffer() const
    address = self.uglySide.call('ritual_ZNK13QSSGRhiBuffer6bufferEv')
    from ..QtGui import QRhiBuffer
    return QRhiBuffer._cuteAt(address)

  def stride(self) -> int:
    """
    Calls Qt's 'quint32 QSSGRhiBuffer::stride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhibuffer.html#stride
    """
    #  quint32 QSSGRhiBuffer::stride() const
    return self.uglySide.call('ritual_ZNK13QSSGRhiBuffer6strideEv')

  def numVertices(self) -> int:
    """
    Calls Qt's 'quint32 QSSGRhiBuffer::numVertices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhibuffer.html#numVertices
    """
    #  quint32 QSSGRhiBuffer::numVertices() const
    return self.uglySide.call('ritual_ZNK13QSSGRhiBuffer11numVerticesEv')

  def indexFormat(self) -> QRhiCommandBuffer.IndexFormat:
    """
    Calls Qt's 'QRhiCommandBuffer::IndexFormat QSSGRhiBuffer::indexFormat()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhibuffer.html#indexFormat

    Returns
    -------

    QRhiCommandBuffer.IndexFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiCommandBuffer.IndexFormat(number)' gives.
    """
    #  QRhiCommandBuffer::IndexFormat QSSGRhiBuffer::indexFormat() const
    return QRhiCommandBuffer.IndexFormat(self.uglySide.call(
        'ritual_ZNK13QSSGRhiBuffer11indexFormatEv',
    ))

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
    Qt's 'QSSGRhiBuffer::QSSGRhiBuffer(QSSGRhiContext &context,
    QRhiBuffer::Type type, QRhiBuffer::UsageFlags usageMask, quint32 stride,
    qsizetype size, QRhiCommandBuffer::IndexFormat indexFormat)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiBuffer.__init__' has no cute function yet. Qt's "
        "'QSSGRhiBuffer::QSSGRhiBuffer(QSSGRhiContext &context, "
        "QRhiBuffer::Type type, QRhiBuffer::UsageFlags usageMask, quint32 "
        "stride, qsizetype size, QRhiCommandBuffer::IndexFormat "
        "indexFormat)': takes a type Python has no way to hand over yet.")

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
