"""
QSSGShaderDefaultMaterialKeyProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderDefaultMaterialKeyProperties to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGShaderDefaultMaterialKeyProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderDefaultMaterialKeyProperties: a plain
  Python object standing in front of one C++
  QSSGShaderDefaultMaterialKeyProperties.

  C++ hands a QSSGShaderDefaultMaterialKeyProperties around as a copy, so
  every C++ QSSGShaderDefaultMaterialKeyProperties behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderDefaultMaterialKeyProperties that has a
  ritual and that Python can call so far, 1 name in all: 'init'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShaderDefaultMaterialKeyProperties::
    ~QSSGShaderDefaultMaterialKeyProperties()': the destructor: Python
    removes its C++ QSSGShaderDefaultMaterialKeyProperties by it, and has no
    other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QSSGShaderDefaultMaterialKeyProperties is created at the first
    use, not by 'QSSGShaderDefaultMaterialKeyProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderDefaultMaterialKeyProperties back gives a
    copy the ritual made for Python, in a new cute
    QSSGShaderDefaultMaterialKeyProperties.
  - Each name of Qt's QSSGShaderDefaultMaterialKeyProperties that has no cute
    function yet, 'visitProperties', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGShaderDefaultMaterialKeyProperties, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ImageChannelNames(CuteNum):
    """
    The enum 'QSSGShaderDefaultMaterialKeyProperties::ImageChannelNames' of
    Qt, with the 13 names Qt gives in it.
    """

    OpacityChannel = Kee[int](0)
    RoughnessChannel = Kee[int](1)
    MetalnessChannel = Kee[int](2)
    OcclusionChannel = Kee[int](3)
    TranslucencyChannel = Kee[int](4)
    HeightChannel = Kee[int](5)
    ClearcoatChannel = Kee[int](6)
    ClearcoatRoughnessChannel = Kee[int](7)
    TransmissionChannel = Kee[int](8)
    ThicknessChannel = Kee[int](9)
    BaseColorChannel = Kee[int](10)
    SpecularAmountChannel = Kee[int](11)
    EmissiveChannel = Kee[int](12)

  class ImageMapNames(CuteNum):
    """
    The enum 'QSSGShaderDefaultMaterialKeyProperties::ImageMapNames' of Qt,
    with the 20 names Qt gives in it.
    """

    DiffuseMap = Kee[int](0)
    BumpMap = Kee[int](1)
    SpecularMap = Kee[int](2)
    NormalMap = Kee[int](3)
    ClearcoatNormalMap = Kee[int](4)
    OpacityMap = Kee[int](5)
    RoughnessMap = Kee[int](6)
    MetalnessMap = Kee[int](7)
    OcclusionMap = Kee[int](8)
    TranslucencyMap = Kee[int](9)
    HeightMap = Kee[int](10)
    ClearcoatMap = Kee[int](11)
    ClearcoatRoughnessMap = Kee[int](12)
    TransmissionMap = Kee[int](13)
    ThicknessMap = Kee[int](14)
    BaseColorMap = Kee[int](15)
    SpecularAmountMap = Kee[int](16)
    EmissiveMap = Kee[int](17)
    ImageMapCount = Kee[int](18)
    SingleChannelImagesFirst = Kee[int](5)

  #  The classes Qt writes inside QSSGShaderDefaultMaterialKeyProperties,
  #  each a class in here as in C++.

  class InitVisitor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSSGShaderDefaultMaterialKeyProperties::InitVisitor: a plain Python
    object standing in front of one C++
    QSSGShaderDefaultMaterialKeyProperties::InitVisitor.

    C++ hands a QSSGShaderDefaultMaterialKeyProperties::InitVisitor around as
    a copy, so every C++ QSSGShaderDefaultMaterialKeyProperties::InitVisitor
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGShaderDefaultMaterialKeyProperties::InitVisitor
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGShaderDefaultMaterialKeyProperties::InitVisitor::~InitVisitor()':
      the destructor: Python removes its C++
      QSSGShaderDefaultMaterialKeyProperties::InitVisitor by it, and has no
      other use for it.

    What has no ritual
    ------------------

    1 of the 2 functions Qt declares: 1 a template.

    What to expect
    --------------

    - The C++ QSSGShaderDefaultMaterialKeyProperties::InitVisitor is created
      at the first use, not by
      'QSSGShaderDefaultMaterialKeyProperties::InitVisitor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGShaderDefaultMaterialKeyProperties::InitVisitor
      back gives a copy the ritual made for Python, in a new cute
      QSSGShaderDefaultMaterialKeyProperties::InitVisitor.
    - Each name of Qt's QSSGShaderDefaultMaterialKeyProperties::InitVisitor
      that has no cute function yet, 'visit', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderDefaultMaterialKeyProperties::InitVisitor'

    #  Qt's '~QSSGShaderDefaultMaterialKeyProperties::InitVisitor()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QSSGShaderDefaultMaterialKeyProperties::InitVisitor behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN38QSSGShaderDefaultMaterialKeyProperties11InitVisitorD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def visit(*__, **_) -> Never:
      """
      Qt's 'QSSGShaderDefaultMaterialKeyProperties::InitVisitor::visit': a
      template: a pattern and no single function.
      """
      raise NotImplementedError(
          "'QSSGShaderDefaultMaterialKeyProperties.InitVisitor.visit' has "
          "no cute function yet. Qt's "
          "'QSSGShaderDefaultMaterialKeyProperties::InitVisitor::visit': a "
          "template: a pattern and no single function.")

  class OffsetVisitor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor: a plain Python
    object standing in front of one C++
    QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor.

    C++ hands a QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor around
    as a copy, so every C++
    QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor
    yet. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor::~OffsetVisitor(
      )': the destructor: Python removes its C++
      QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor by it, and has no
      other use for it.

    What has no ritual
    ------------------

    1 of the 3 functions Qt declares: 1 a template.

    What to expect
    --------------

    - The C++ QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor is
      created at the first use, not by
      'QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor back gives a copy
      the ritual made for Python, in a new cute
      QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor.
    - Each name of Qt's QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor
      that has no cute function yet, 'visit', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor'

    #  Qt's '~QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN38QSSGShaderDefaultMaterialKeyProperties13OffsetVisitorD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor::OffsetVisitor(
      )', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgshaderdefaultmaterialkeyproperties-offsetvisitor.html
      """
      #  QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor::
      #      OffsetVisitor()
      self._noteCreation(
          QSSGShaderDefaultMaterialKeyProperties.OffsetVisitor, lambda: Rituals.call(
              'ritual_ZN38QSSGShaderDefaultMaterialKeyProperties13OffsetVis'
              'itorC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def visit(*__, **_) -> Never:
      """
      Qt's 'QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor::visit': a
      template: a pattern and no single function.
      """
      raise NotImplementedError(
          "'QSSGShaderDefaultMaterialKeyProperties.OffsetVisitor.visit' has "
          "no cute function yet. Qt's "
          "'QSSGShaderDefaultMaterialKeyProperties::OffsetVisitor::visit': "
          "a template: a pattern and no single function.")

  class StringSizeVisitor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor: a plain Python
    object standing in front of one C++
    QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor.

    C++ hands a QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor
    around as a copy, so every C++
    QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor::
      ~StringSizeVisitor()': the destructor: Python removes its C++
      QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor by it, and
      has no other use for it.

    What has no ritual
    ------------------

    1 of the 2 functions Qt declares: 1 a template.

    What to expect
    --------------

    - The C++ QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor is
      created at the first use, not by
      'QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor back gives a
      copy the ritual made for Python, in a new cute
      QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor.
    - Each name of Qt's
      QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor that has no
      cute function yet, 'visit', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor'

    #  Qt's '~QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN38QSSGShaderDefaultMaterialKeyProperties17StringSizeVisitorD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def visit(*__, **_) -> Never:
      """
      Qt's
      'QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor::visit': a
      template: a pattern and no single function.
      """
      raise NotImplementedError(
          "'QSSGShaderDefaultMaterialKeyProperties.StringSizeVisitor.visit' "
          "has no cute function yet. Qt's "
          "'QSSGShaderDefaultMaterialKeyProperties::StringSizeVisitor::visit"
          "': a template: a pattern and no single function.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderDefaultMaterialKeyProperties'

  #  Qt's '~QSSGShaderDefaultMaterialKeyProperties()'. Naming it makes this a
  #  value class: Python owns every C++
  #  QSSGShaderDefaultMaterialKeyProperties behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN38QSSGShaderDefaultMaterialKeyPropertiesD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGShaderDefaultMaterialKeyProperties::
    QSSGShaderDefaultMaterialKeyProperties()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialkeyproperties.html
    """
    #  QSSGShaderDefaultMaterialKeyProperties::
    #      QSSGShaderDefaultMaterialKeyProperties()
    self._noteCreation(
        QSSGShaderDefaultMaterialKeyProperties, lambda: Rituals.call(
            'ritual_ZN38QSSGShaderDefaultMaterialKeyPropertiesC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QSSGShaderDefaultMaterialKeyProperties::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialkeyproperties.html#init
    """
    #  void QSSGShaderDefaultMaterialKeyProperties::init()
    self.uglySide.call(
        'ritual_ZN38QSSGShaderDefaultMaterialKeyProperties4initEv',
    )

  @staticmethod
  def visitProperties(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderDefaultMaterialKeyProperties::visitProperties': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QSSGShaderDefaultMaterialKeyProperties.visitProperties' has no "
        "cute function yet. Qt's "
        "'QSSGShaderDefaultMaterialKeyProperties::visitProperties': a "
        "template: a pattern and no single function.")
