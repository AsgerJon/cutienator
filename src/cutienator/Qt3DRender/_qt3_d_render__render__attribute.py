"""
Qt3DRender::Render::Attribute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/attribute_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::Attribute to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Attribute(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Attribute: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Attribute.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Attribute is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Attribute that has a ritual and
  that Python can call so far, 14 names in all: 'cleanup',
  'syncFromFrontEnd', 'bufferId', 'name', 'nameId', 'vertexBaseType',
  'vertexSize', 'count', 'byteStride', 'byteOffset', 'divisor',
  'attributeType', 'isDirty', 'unsetDirty'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Attribute::~Attribute()': the destructor:
    Python never removes a C++ Qt3DRender::Render::Attribute.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Attribute is created at the first use, not by
    'Qt3DRender::Render::Attribute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Attribute.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Attribute'

  #  A C++ Qt3DRender::Render::Attribute Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Attribute'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bufferId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId Qt3DRender::Render::Attribute::bufferId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#bufferId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::Attribute::bufferId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute8bufferIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::Attribute::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::Attribute::name() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute4nameEv',
    )

  def nameId(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::Attribute::nameId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#nameId
    """
    #  int Qt3DRender::Render::Attribute::nameId() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute6nameIdEv',
    )

  def vertexBaseType(self) -> Qt3DCore.QAttribute.VertexBaseType:
    """
    Calls Qt's 'Qt3DCore::QAttribute::VertexBaseType
    Qt3DRender::Render::Attribute::vertexBaseType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#vertexBaseType

    Returns
    -------

    Qt3DCore.QAttribute.VertexBaseType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QAttribute.VertexBaseType(number)' gives.
    """
    #  Qt3DCore::QAttribute::VertexBaseType
    #      Qt3DRender::Render::Attribute::vertexBaseType() const
    return Qt3DCore.QAttribute.VertexBaseType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute14vertexBaseTypeEv',
    ))

  def vertexSize(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::Render::Attribute::vertexSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#vertexSize
    """
    #  uint Qt3DRender::Render::Attribute::vertexSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute10vertexSizeEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::Render::Attribute::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#count
    """
    #  uint Qt3DRender::Render::Attribute::count() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute5countEv',
    )

  def byteStride(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::Render::Attribute::byteStride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#byteStride
    """
    #  uint Qt3DRender::Render::Attribute::byteStride() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute10byteStrideEv',
    )

  def byteOffset(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::Render::Attribute::byteOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#byteOffset
    """
    #  uint Qt3DRender::Render::Attribute::byteOffset() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute10byteOffsetEv',
    )

  def divisor(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::Render::Attribute::divisor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#divisor
    """
    #  uint Qt3DRender::Render::Attribute::divisor() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute7divisorEv',
    )

  def attributeType(self) -> Qt3DCore.QAttribute.AttributeType:
    """
    Calls Qt's 'Qt3DCore::QAttribute::AttributeType
    Qt3DRender::Render::Attribute::attributeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#attributeType

    Returns
    -------

    Qt3DCore.QAttribute.AttributeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QAttribute.AttributeType(number)' gives.
    """
    #  Qt3DCore::QAttribute::AttributeType
    #      Qt3DRender::Render::Attribute::attributeType() const
    return Qt3DCore.QAttribute.AttributeType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute13attributeTypeEv',
    ))

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Attribute::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#isDirty
    """
    #  bool Qt3DRender::Render::Attribute::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Attribute7isDirtyEv',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::Attribute::Attribute()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#Attribute
    """
    #  Qt3DRender::Render::Attribute::Attribute()
    self._noteCreation(Attribute, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render9AttributeC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Attribute::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#cleanup
    """
    #  void Qt3DRender::Render::Attribute::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render9Attribute7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Attribute::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Attribute::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render9Attribute16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render9Attribute16syncFromFrontEndEPKN'
          '8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Attribute::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attribute.html#unsetDirty
    """
    #  void Qt3DRender::Render::Attribute::unsetDirty()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Attribute10unsetDirtyEv',
    )
