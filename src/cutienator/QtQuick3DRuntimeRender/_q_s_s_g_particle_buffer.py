"""
QSSGParticleBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGParticleBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QSize
  from ..QtQuick3DUtils import QSSGBounds3
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGBounds3 = WAIT['QSSGBounds3']


class QSSGParticleBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGParticleBuffer: a plain Python object standing in
  front of one C++ QSSGParticleBuffer.

  C++ hands a QSSGParticleBuffer around as a copy, so every C++
  QSSGParticleBuffer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGParticleBuffer that has a ritual and that Python
  can call so far, 14 names in all: 'resize', 'resizeLine', 'setBounds',
  'pointer', 'particlesPerSlice', 'sliceStride', 'particleCount',
  'sliceCount', 'size', 'data', 'bounds', 'bufferSize', 'serial', 'segments'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char *QSSGParticleBuffer::pointer()': gives 'char', which has no
    cute class yet.
  - Qt's 'QSSGParticleBuffer::~QSSGParticleBuffer()': the destructor: Python
    removes its C++ QSSGParticleBuffer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGParticleBuffer is created at the first use, not by
    'QSSGParticleBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGParticleBuffer back gives a copy the ritual made
    for Python, in a new cute QSSGParticleBuffer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGParticleBuffer'

  #  Qt's '~QSSGParticleBuffer()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGParticleBuffer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSSGParticleBufferD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pointer(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGParticleBuffer::pointer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#pointer

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGParticleBuffer::pointer() const
    chars = self.uglySide.call('ritual_ZNK18QSSGParticleBuffer7pointerEv')
    return None if chars is None else chars.decode()

  def particlesPerSlice(self) -> int:
    """
    Calls Qt's 'int QSSGParticleBuffer::particlesPerSlice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgparticlebuffer.html#particlesPerSlice
    """
    #  int QSSGParticleBuffer::particlesPerSlice() const
    return self.uglySide.call(
        'ritual_ZNK18QSSGParticleBuffer17particlesPerSliceEv',
    )

  def sliceStride(self) -> int:
    """
    Calls Qt's 'int QSSGParticleBuffer::sliceStride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgparticlebuffer.html#sliceStride
    """
    #  int QSSGParticleBuffer::sliceStride() const
    return self.uglySide.call(
        'ritual_ZNK18QSSGParticleBuffer11sliceStrideEv',
    )

  def particleCount(self) -> int:
    """
    Calls Qt's 'int QSSGParticleBuffer::particleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgparticlebuffer.html#particleCount
    """
    #  int QSSGParticleBuffer::particleCount() const
    return self.uglySide.call(
        'ritual_ZNK18QSSGParticleBuffer13particleCountEv',
    )

  def sliceCount(self) -> int:
    """
    Calls Qt's 'int QSSGParticleBuffer::sliceCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#sliceCount
    """
    #  int QSSGParticleBuffer::sliceCount() const
    return self.uglySide.call('ritual_ZNK18QSSGParticleBuffer10sliceCountEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSSGParticleBuffer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSSGParticleBuffer::size() const
    address = self.uglySide.call('ritual_ZNK18QSSGParticleBuffer4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSSGParticleBuffer::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSSGParticleBuffer::data() const
    address = self.uglySide.call('ritual_ZNK18QSSGParticleBuffer4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def bounds(self) -> QSSGBounds3:
    """
    Calls Qt's 'QSSGBounds3 QSSGParticleBuffer::bounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#bounds

    Returns
    -------

    QSSGBounds3
      A new cute QSSGBounds3 around the copy Qt gave back. Python owns it.
    """
    #  QSSGBounds3 QSSGParticleBuffer::bounds() const
    address = self.uglySide.call('ritual_ZNK18QSSGParticleBuffer6boundsEv')
    from ..QtQuick3DUtils import QSSGBounds3
    return QSSGBounds3._cuteOwning(address)

  def bufferSize(self) -> int:
    """
    Calls Qt's 'int QSSGParticleBuffer::bufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#bufferSize
    """
    #  int QSSGParticleBuffer::bufferSize() const
    return self.uglySide.call('ritual_ZNK18QSSGParticleBuffer10bufferSizeEv')

  def serial(self) -> int:
    """
    Calls Qt's 'int QSSGParticleBuffer::serial() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#serial
    """
    #  int QSSGParticleBuffer::serial() const
    return self.uglySide.call('ritual_ZNK18QSSGParticleBuffer6serialEv')

  def segments(self) -> int:
    """
    Calls Qt's 'int QSSGParticleBuffer::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#segments
    """
    #  int QSSGParticleBuffer::segments() const
    return self.uglySide.call('ritual_ZNK18QSSGParticleBuffer8segmentsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGBounds3)
  def setBounds(self, bounds: QSSGBounds3) -> None:
    """
    Calls Qt's 'void QSSGParticleBuffer::setBounds(const QSSGBounds3
    &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#setBounds

    Parameters
    ----------

    bounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.
    """
    #  void QSSGParticleBuffer::setBounds(const QSSGBounds3 &bounds)
    self.uglySide.call(
        'ritual_ZN18QSSGParticleBuffer9setBoundsERK11QSSGBounds3',
        self._valueOf(bounds),
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

  @overload(int, int)
  def resize(self, particleCount: int, particleSize: int) -> None:
    """
    Calls Qt's 'void QSSGParticleBuffer::resize(int particleCount, int
    particleSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#resize

    Parameters
    ----------

    particleCount : int
      Passed on as it is.

    particleSize : int
      Passed on as it is.
    """
    #  void QSSGParticleBuffer::resize(int particleCount, int particleSize)
    self.uglySide.call(
        'ritual_ZN18QSSGParticleBuffer6resizeEii',
        particleCount, particleSize,
    )

  @overload(int, int)
  def resizeLine(self, particleCount: int, segmentCount: int) -> None:
    """
    Calls Qt's 'void QSSGParticleBuffer::resizeLine(int particleCount, int
    segmentCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgparticlebuffer.html#resizeLine

    Parameters
    ----------

    particleCount : int
      Passed on as it is.

    segmentCount : int
      Passed on as it is.
    """
    #  void QSSGParticleBuffer::resizeLine(int particleCount, int
    #      segmentCount)
    self.uglySide.call(
        'ritual_ZN18QSSGParticleBuffer10resizeLineEii',
        particleCount, segmentCount,
    )
