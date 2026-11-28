"""
QNullTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullTexture to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNullTexture(QRhiTexture):
  """
  The cute side of Qt's QNullTexture: a plain Python object standing in front
  of one C++ QNullTexture.

  It is built on the cute 'QRhiTexture', as Qt's QNullTexture is built on
  Qt's QRhiTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNullTexture that has a ritual and that Python can
  call so far, 3 names in all: 'destroy', 'create', 'createFrom'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullTexture::~QNullTexture()': the destructor: Python never
    removes a C++ QNullTexture.

  What to expect
  --------------

  - The C++ QNullTexture is created at the first use, not by
    'QNullTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullTexture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullTexture'

  #  A C++ QNullTexture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullTexture'

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

  @overload(
      QRhiImplementation, QRhiTexture.Format, QSize, int, int, int,
      QRhiTexture.Flags,
  )
  @overload(
      NoneType, QRhiTexture.Format, QSize, int, int, int, QRhiTexture.Flags,
  )
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      format: QRhiTexture.Format,
      pixelSize: QSize,
      depth: int,
      arraySize: int,
      sampleCount: int,
      flags: QRhiTexture.Flags,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNullTexture::QNullTexture(QRhiImplementation *rhi, Format format, const
    QSize &pixelSize, int depth, int arraySize, int sampleCount, Flags
    flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnulltexture.html#QNullTexture

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QRhiTexture.Format
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    depth : int
      Passed on as it is.

    arraySize : int
      Passed on as it is.

    sampleCount : int
      Passed on as it is.

    flags : QRhiTexture.Flags
      Passed on as its number.
    """
    #  QNullTexture::QNullTexture(QRhiImplementation *rhi, Format format,
    #      const QSize &pixelSize, int depth, int arraySize, int sampleCount,
    #      Flags flags)
    self._noteCreation(QNullTexture, lambda: Rituals.call(
        'ritual_ZN12QNullTextureC1EP18QRhiImplementationN11QRhiTexture6Form'
        'atERK5QSizeiii6QFlagsINS2_4FlagEE',
        self._addressOf(rhi), format.value, self._valueOf(pixelSize), depth,
        arraySize, sampleCount, flags.value,
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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QNullTexture::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qnulltexture.html#destroy
    """
    #  void QNullTexture::destroy()
    ritual = 'ritual_ZN12QNullTexture7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QNullTexture7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QNullTexture::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qnulltexture.html#create
    """
    #  bool QNullTexture::create()
    ritual = 'ritual_ZN12QNullTexture6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QNullTexture6createEv'
    return self.uglySide.call(ritual)

  @overload(QRhiTexture.NativeTexture)
  def createFrom(self, src: QRhiTexture.NativeTexture) -> bool:
    """
    Calls Qt's 'bool QNullTexture::createFrom(NativeTexture src)'.

    Qt's own words: https://doc.qt.io/qt-6/qnulltexture.html#createFrom

    Parameters
    ----------

    src : QRhiTexture.NativeTexture
      Passed on as a value: Qt reads the C++ QRhiTexture::NativeTexture,
      which stays Python's own.
    """
    #  bool QNullTexture::createFrom(NativeTexture src)
    ritual = (
        'ritual_ZN12QNullTexture10createFromEN11QRhiTexture13NativeTextureE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QNullTexture10createFromEN11QRhiTexture13NativeTe'
          'xtureE')
    return self.uglySide.call(ritual, self._valueOf(src))
