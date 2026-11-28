"""
QQuick3DRenderPassTargetBlend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DRenderPassTargetBlend to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from ..QtGui import QRhiGraphicsPipeline


class QQuick3DRenderPassTargetBlend(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DRenderPassTargetBlend: a plain Python object
  standing in front of one C++ QQuick3DRenderPassTargetBlend.

  C++ hands a QQuick3DRenderPassTargetBlend around as a copy, so every C++
  QQuick3DRenderPassTargetBlend behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuick3DRenderPassTargetBlend that has a ritual and
  that Python can call so far, 2 names in all: '__eq__', 'toRhiTargetBlend'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DRenderPassTargetBlend::~QQuick3DRenderPassTargetBlend()':
    the destructor: Python removes its C++ QQuick3DRenderPassTargetBlend by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DRenderPassTargetBlend is created at the first use, not by
    'QQuick3DRenderPassTargetBlend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DRenderPassTargetBlend back gives a copy the
    ritual made for Python, in a new cute QQuick3DRenderPassTargetBlend.
  """

  #  The enums Qt writes inside QQuick3DRenderPassTargetBlend, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class BlendFactor(CuteNum, scoped=True):
    """
    The enum 'QQuick3DRenderPassTargetBlend::BlendFactor' of Qt, with the 19
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Zero = Kee[int](0)
    One = Kee[int](1)
    SrcColor = Kee[int](2)
    OneMinusSrcColor = Kee[int](3)
    DstColor = Kee[int](4)
    OneMinusDstColor = Kee[int](5)
    SrcAlpha = Kee[int](6)
    OneMinusSrcAlpha = Kee[int](7)
    DstAlpha = Kee[int](8)
    OneMinusDstAlpha = Kee[int](9)
    ConstantColor = Kee[int](10)
    OneMinusConstantColor = Kee[int](11)
    ConstantAlpha = Kee[int](12)
    OneMinusConstantAlpha = Kee[int](13)
    SrcAlphaSaturate = Kee[int](14)
    Src1Color = Kee[int](15)
    OneMinusSrc1Color = Kee[int](16)
    Src1Alpha = Kee[int](17)
    OneMinusSrc1Alpha = Kee[int](18)

  class BlendOperation(CuteNum, scoped=True):
    """
    The enum 'QQuick3DRenderPassTargetBlend::BlendOperation' of Qt, with the
    5 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Add = Kee[int](0)
    Subtract = Kee[int](1)
    ReverseSubtract = Kee[int](2)
    Min = Kee[int](3)
    Max = Kee[int](4)

  class ColorMaskComponent(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QQuick3DRenderPassTargetBlend::ColorMaskComponent' of Qt,
    with the 4 names Qt gives in it. Qt names the type of its combinations
    'QQuick3DRenderPassTargetBlend::ColorMask'.
    """

    R = 0x1
    G = 0x2
    B = 0x4
    A = 0x8

  ColorMask = ColorMaskComponent

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRenderPassTargetBlend'

  #  Qt's '~QQuick3DRenderPassTargetBlend()'. Naming it makes this a value
  #  class: Python owns every C++ QQuick3DRenderPassTargetBlend behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QQuick3DRenderPassTargetBlendD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toRhiTargetBlend(self) -> QRhiGraphicsPipeline.TargetBlend:
    """
    Calls Qt's 'QRhiGraphicsPipeline::TargetBlend
    QQuick3DRenderPassTargetBlend::toRhiTargetBlend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpasstargetblend.html

    Returns
    -------

    QRhiGraphicsPipeline.TargetBlend
      A new cute QRhiGraphicsPipeline::TargetBlend around the copy Qt gave
      back. Python owns it.
    """
    #  QRhiGraphicsPipeline::TargetBlend
    #      QQuick3DRenderPassTargetBlend::toRhiTargetBlend() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DRenderPassTargetBlend16toRhiTargetBlendEv',
    )
    return QRhiGraphicsPipeline.TargetBlend._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QQuick3DRenderPassTargetBlend) -> bool:
    """
    Calls Qt's 'bool QQuick3DRenderPassTargetBlend::operator==(const
    QQuick3DRenderPassTargetBlend &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpasstargetblend.html#operator==

    Parameters
    ----------

    other : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  bool QQuick3DRenderPassTargetBlend::operator==(const
    #      QQuick3DRenderPassTargetBlend &other) const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DRenderPassTargetBlendeqERKS_',
        self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRenderPassTargetBlend::QQuick3DRenderPassTargetBlend()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpasstargetblend.html
    """
    #  QQuick3DRenderPassTargetBlend::QQuick3DRenderPassTargetBlend()
    self._noteCreation(QQuick3DRenderPassTargetBlend, lambda: Rituals.call(
        'ritual_ZN29QQuick3DRenderPassTargetBlendC1Ev',
    ))

  @overload(QRhiGraphicsPipeline.TargetBlend)
  def __init__(self, targetBlend: QRhiGraphicsPipeline.TargetBlend) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRenderPassTargetBlend::QQuick3DRenderPassTargetBlend(
    QRhiGraphicsPipeline::TargetBlend targetBlend)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpasstargetblend.html

    Parameters
    ----------

    targetBlend : QRhiGraphicsPipeline.TargetBlend
      Passed on as a value: Qt reads the C++
      QRhiGraphicsPipeline::TargetBlend, which stays Python's own.
    """
    #  QQuick3DRenderPassTargetBlend::QQuick3DRenderPassTargetBlend(
    #      QRhiGraphicsPipeline::TargetBlend targetBlend)
    self._noteCreation(QQuick3DRenderPassTargetBlend, lambda: Rituals.call(
        'ritual_ZN29QQuick3DRenderPassTargetBlendC1EN20QRhiGraphicsPipeline'
        '11TargetBlendE',
        self._valueOf(targetBlend),
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
