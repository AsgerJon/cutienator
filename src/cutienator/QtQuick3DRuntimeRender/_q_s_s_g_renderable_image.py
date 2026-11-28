"""
QSSGRenderableImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableimage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderableImage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderableImage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderableImage: a plain Python object standing
  in front of one C++ QSSGRenderableImage.

  C++ hands a QSSGRenderableImage around as a copy, so every C++
  QSSGRenderableImage behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGRenderableImage yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderableImage::QSSGRenderableImage(Type inMapType, const
    QSSGRenderImage &inImageNode, const QSSGRenderImageTexture &inTexture)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRenderableImage::~QSSGRenderableImage()': the destructor:
    Python removes its C++ QSSGRenderableImage by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGRenderableImage is created at the first use, not by
    'QSSGRenderableImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderableImage back gives a copy the ritual made
    for Python, in a new cute QSSGRenderableImage.
  - Each name of Qt's QSSGRenderableImage that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderableImage, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderableImage::Type' of Qt, with the 19 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unknown = Kee[int](0)
    Diffuse = Kee[int](1)
    Opacity = Kee[int](2)
    Specular = Kee[int](3)
    Emissive = Kee[int](4)
    Bump = Kee[int](5)
    SpecularAmountMap = Kee[int](6)
    Normal = Kee[int](7)
    Translucency = Kee[int](8)
    Roughness = Kee[int](9)
    BaseColor = Kee[int](10)
    Metalness = Kee[int](11)
    Occlusion = Kee[int](12)
    Height = Kee[int](13)
    Clearcoat = Kee[int](14)
    ClearcoatRoughness = Kee[int](15)
    ClearcoatNormal = Kee[int](16)
    Transmission = Kee[int](17)
    Thickness = Kee[int](18)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderableImage'

  #  Qt's '~QSSGRenderableImage()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRenderableImage behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGRenderableImageD1Ev'

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
    Qt's 'QSSGRenderableImage::QSSGRenderableImage(Type inMapType, const
    QSSGRenderImage &inImageNode, const QSSGRenderImageTexture &inTexture)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderableImage.__init__' has no cute function yet. Qt's "
        "'QSSGRenderableImage::QSSGRenderableImage(Type inMapType, const "
        "QSSGRenderImage &inImageNode, const QSSGRenderImageTexture "
        "&inTexture)': takes a type Python has no way to hand over yet.")

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
