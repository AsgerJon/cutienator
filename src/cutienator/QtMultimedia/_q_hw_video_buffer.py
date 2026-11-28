"""
QHwVideoBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHwVideoBuffer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QAbstractVideoBuffer, QVideoFrame, QVideoFrameTexturesHandles

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4, QRhi
  from . import QVideoFrameFormat


class QHwVideoBuffer(QAbstractVideoBuffer, QVideoFrameTexturesHandles):
  """
  The cute side of Qt's QHwVideoBuffer: a plain Python object standing in
  front of one C++ QHwVideoBuffer.

  It is built on the cute 'QAbstractVideoBuffer', as Qt's QHwVideoBuffer is
  built on Qt's QAbstractVideoBuffer, and has everything that class has. It
  is built on the cute 'QVideoFrameTexturesHandles' as well, as Qt's
  QHwVideoBuffer is built on Qt's QVideoFrameTexturesHandles too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHwVideoBuffer that has a ritual and that Python can
  call so far, 5 names in all: 'handleType', 'associatedCurrentThreadRhi',
  'format', 'externalTextureMatrix', 'isDmaBuf'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHwVideoBuffer::~QHwVideoBuffer()': the destructor: Python never
    removes a C++ QHwVideoBuffer.
  - Qt's 'QVideoFrameTexturesUPtr QHwVideoBuffer::mapTextures(QRhi &a0,
    QVideoFrameTexturesUPtr &a1)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QHwVideoBuffer::initTextureConverter(QRhi &a0)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QHwVideoBuffer is created at the first use, not by
    'QHwVideoBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHwVideoBuffer.
  - Each name of Qt's QHwVideoBuffer that has no cute function yet,
    'initTextureConverter', 'mapTextures', holds a function that raises
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
  __qt_class__ = 'QHwVideoBuffer'

  #  Qt's QHwVideoBuffer is built on more than one class. The part of a C++
  #  QHwVideoBuffer that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QVideoFrameTexturesHandles':
          'ritual_cast_QHwVideoBuffer_QVideoFrameTexturesHandles',
  }

  #  A C++ QHwVideoBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHwVideoBuffer'

  #  The functions Qt calls itself that QHwVideoBuffer is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'mapTextures': (
          'QVideoFrameTexturesUPtr QHwVideoBuffer::mapTextures(QRhi &, '
          'QVideoFrameTexturesUPtr &)',
      ),
      'initTextureConverter': (
          'void QHwVideoBuffer::initTextureConverter(QRhi &)',
      ),
  }

  #  The functions Qt calls itself that QHwVideoBuffer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'associatedCurrentThreadRhi': (
          ('_ZNK14QHwVideoBuffer26associatedCurrentThreadRhiEv',
           ('address', 'address', 'QtGui:QRhi'),
           ()),
      ),
      'externalTextureMatrix': (
          ('_ZNK14QHwVideoBuffer21externalTextureMatrixEv',
           ('address', 'value', 'QtGui:QMatrix4x4'),
           ()),
      ),
      'isDmaBuf': (
          ('_ZNK14QHwVideoBuffer8isDmaBufEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def handleType(self) -> QVideoFrame.HandleType:
    """
    Calls Qt's 'QVideoFrame::HandleType QHwVideoBuffer::handleType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhwvideobuffer.html#handleType

    Returns
    -------

    QVideoFrame.HandleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QVideoFrame.HandleType(number)' gives.
    """
    #  QVideoFrame::HandleType QHwVideoBuffer::handleType() const
    return QVideoFrame.HandleType(self.uglySide.call(
        'ritual_ZNK14QHwVideoBuffer10handleTypeEv',
    ))

  def associatedCurrentThreadRhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QHwVideoBuffer::associatedCurrentThreadRhi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhwvideobuffer.html#associatedCurrentThreadRhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QHwVideoBuffer::associatedCurrentThreadRhi() const
    ritual = 'ritual_ZNK14QHwVideoBuffer26associatedCurrentThreadRhiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHwVideoBuffer26associatedCurrentThreadRhiEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def format(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QHwVideoBuffer::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhwvideobuffer.html#format

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QHwVideoBuffer::format() const
    ritual = 'ritual_ZNK14QHwVideoBuffer6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHwVideoBuffer6formatEv'
    address = self.uglySide.call(ritual)
    from . import QVideoFrameFormat
    return QVideoFrameFormat._cuteOwning(address)

  def externalTextureMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QHwVideoBuffer::externalTextureMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhwvideobuffer.html#externalTextureMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QHwVideoBuffer::externalTextureMatrix() const
    ritual = 'ritual_ZNK14QHwVideoBuffer21externalTextureMatrixEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHwVideoBuffer21externalTextureMatrixEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def isDmaBuf(self) -> bool:
    """
    Calls Qt's 'bool QHwVideoBuffer::isDmaBuf() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhwvideobuffer.html#isDmaBuf
    """
    #  bool QHwVideoBuffer::isDmaBuf() const
    ritual = 'ritual_ZNK14QHwVideoBuffer8isDmaBufEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHwVideoBuffer8isDmaBufEv'
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

  @overload(QVideoFrame.HandleType)
  def __init__(self, type: QVideoFrame.HandleType) -> None:
    """
    Notes what was given, for Qt's
    'QHwVideoBuffer::QHwVideoBuffer(QVideoFrame::HandleType type)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhwvideobuffer.html#QHwVideoBuffer

    Parameters
    ----------

    type : QVideoFrame.HandleType
      Passed on as its number.
    """
    #  QHwVideoBuffer::QHwVideoBuffer(QVideoFrame::HandleType type)
    self._noteCreation(QHwVideoBuffer, lambda: Rituals.call(
        'ritual_ZN14QHwVideoBufferC1EN11QVideoFrame10HandleTypeE',
        type.value,
    ))

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

  @staticmethod
  def initTextureConverter(*__, **_) -> Never:
    """
    Qt's 'void QHwVideoBuffer::initTextureConverter(QRhi &a0)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHwVideoBuffer.initTextureConverter' has no cute function yet. "
        "Qt's 'void QHwVideoBuffer::initTextureConverter(QRhi &a0)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def mapTextures(*__, **_) -> Never:
    """
    Qt's 'QVideoFrameTexturesUPtr QHwVideoBuffer::mapTextures(QRhi &a0,
    QVideoFrameTexturesUPtr &a1)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QHwVideoBuffer.mapTextures' has no cute function yet. Qt's "
        "'QVideoFrameTexturesUPtr QHwVideoBuffer::mapTextures(QRhi &a0, "
        "QVideoFrameTexturesUPtr &a1)': takes a type Python has no way to "
        "hand over yet.")
