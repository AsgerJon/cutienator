"""
QSSGRenderImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderImage to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum
from ..occult import Rituals
from . import QSSGRenderGraphObject


class QSSGRenderImage(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderImage: a plain Python object standing in
  front of one C++ QSSGRenderImage.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's QSSGRenderImage is
  built on Qt's QSSGRenderGraphObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderImage that has a ritual and that Python
  can call so far, 3 names in all: 'clearDirty', 'calculateTextureTransform',
  'isImageTransformIdentity'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderImage::~QSSGRenderImage()': the destructor: Python never
    removes a C++ QSSGRenderImage.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderImage is created at the first use, not by
    'QSSGRenderImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderImage.
  """

  #  The enums Qt writes inside QSSGRenderImage, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags, scoped=True):
    """
    The flags enum 'QSSGRenderImage::Flag' of Qt, with the 2 names Qt gives
    in it. Qt names the type of its combinations 'QSSGRenderImage::Flags'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Dirty = 0x1
    TransformDirty = 0x2

  Flags = Flag

  class MappingModes(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderImage::MappingModes' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Normal = Kee[int](0)
    Environment = Kee[int](1)
    LightProbe = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isImageTransformIdentity(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderImage::isImageTransformIdentity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimage.html#isImageTransformIdentity
    """
    #  bool QSSGRenderImage::isImageTransformIdentity() const
    return self.uglySide.call(
        'ritual_ZNK15QSSGRenderImage24isImageTransformIdentityEv',
    )

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

  @overload()
  @overload(QSSGRenderGraphObject.Type)
  def __init__(
      self,
      type: QSSGRenderGraphObject.Type = QSSGRenderGraphObject.Type.Image2D,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderImage::QSSGRenderImage(QSSGRenderGraphObject::Type type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimage.html#QSSGRenderImage

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QSSGRenderGraphObject.Type.Image2D.
    """
    #  QSSGRenderImage::QSSGRenderImage(QSSGRenderGraphObject::Type type)
    self._noteCreation(QSSGRenderImage, lambda: Rituals.call(
        'ritual_ZN15QSSGRenderImageC1EN21QSSGRenderGraphObject4TypeE',
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

  def clearDirty(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderImage::clearDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderimage.html#clearDirty
    """
    #  bool QSSGRenderImage::clearDirty()
    return self.uglySide.call('ritual_ZN15QSSGRenderImage10clearDirtyEv')

  def calculateTextureTransform(self) -> None:
    """
    Calls Qt's 'void QSSGRenderImage::calculateTextureTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderimage.html#calculateTextureTransform
    """
    #  void QSSGRenderImage::calculateTextureTransform()
    self.uglySide.call(
        'ritual_ZN15QSSGRenderImage25calculateTextureTransformEv',
    )
