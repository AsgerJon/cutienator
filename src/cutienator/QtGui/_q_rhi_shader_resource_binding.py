"""
QRhiShaderResourceBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiBuffer, QRhiSampler, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiBuffer = WAIT['QRhiBuffer']
  QRhiSampler = WAIT['QRhiSampler']
  QRhiTexture = WAIT['QRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiShaderResourceBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiShaderResourceBinding: a plain Python object
  standing in front of one C++ QRhiShaderResourceBinding.

  C++ hands a QRhiShaderResourceBinding around as a copy, so every C++
  QRhiShaderResourceBinding behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiShaderResourceBinding that has a ritual and that
  Python can call so far, 13 names in all: 'isLayoutCompatible',
  'uniformBuffer', 'uniformBufferWithDynamicOffset', 'sampledTexture',
  'sampledTextures', 'texture', 'sampler', 'imageLoad', 'imageStore',
  'imageLoadStore', 'bufferLoad', 'bufferStore', 'bufferLoadStore'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiShaderResourceBinding QRhiShaderResourceBinding::textures(int
    binding, StageFlags stage, int count, QRhiTexture **tex)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QRhiShaderResourceBinding::~QRhiShaderResourceBinding()': the
    destructor: Python removes its C++ QRhiShaderResourceBinding by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QRhiShaderResourceBinding is created at the first use, not by
    'QRhiShaderResourceBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiShaderResourceBinding back gives a copy the
    ritual made for Python, in a new cute QRhiShaderResourceBinding.
  - Each name of Qt's QRhiShaderResourceBinding that has no cute function
    yet, 'serializeLayoutDescription', 'textures', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhiShaderResourceBinding, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StageFlag(CuteFlags):
    """
    The flags enum 'QRhiShaderResourceBinding::StageFlag' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QRhiShaderResourceBinding::StageFlags'.
    """

    VertexStage = 0x1
    TessellationControlStage = 0x2
    TessellationEvaluationStage = 0x4
    GeometryStage = 0x8
    FragmentStage = 0x10
    ComputeStage = 0x20

  StageFlags = StageFlag

  class Type(CuteNum):
    """
    The enum 'QRhiShaderResourceBinding::Type' of Qt, with the 10 names Qt
    gives in it.
    """

    UniformBuffer = Kee[int](0)
    SampledTexture = Kee[int](1)
    Texture = Kee[int](2)
    Sampler = Kee[int](3)
    ImageLoad = Kee[int](4)
    ImageStore = Kee[int](5)
    ImageLoadStore = Kee[int](6)
    BufferLoad = Kee[int](7)
    BufferStore = Kee[int](8)
    BufferLoadStore = Kee[int](9)

  #  The classes Qt writes inside QRhiShaderResourceBinding, each a class in
  #  here as in C++.

  class Data(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiShaderResourceBinding::Data: a plain Python
    object standing in front of one C++ QRhiShaderResourceBinding::Data.

    C++ hands a QRhiShaderResourceBinding::Data around as a copy, so every
    C++ QRhiShaderResourceBinding::Data behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QRhiShaderResourceBinding::Data that has a ritual
    and that Python can call so far, 1 name in all: 'arraySize'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiShaderResourceBinding::Data::~Data()': the destructor: Python
      removes its C++ QRhiShaderResourceBinding::Data by it, and has no other
      use for it.

    What has no ritual
    ------------------

    1 of the 3 functions Qt declares: 1 a template.

    What to expect
    --------------

    - The C++ QRhiShaderResourceBinding::Data is created at the first use,
      not by 'QRhiShaderResourceBinding::Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiShaderResourceBinding::Data back gives a copy
      the ritual made for Python, in a new cute
      QRhiShaderResourceBinding::Data.
    - Each name of Qt's QRhiShaderResourceBinding::Data that has no cute
      function yet, 'serialize', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The classes Qt writes inside QRhiShaderResourceBinding::Data, each a
    #  class in here as in C++.

    class StorageBufferData(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QRhiShaderResourceBinding::Data::StorageBufferData: a plain Python
      object standing in front of one C++
      QRhiShaderResourceBinding::Data::StorageBufferData.

      C++ hands a QRhiShaderResourceBinding::Data::StorageBufferData around
      as a copy, so every C++
      QRhiShaderResourceBinding::Data::StorageBufferData behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QRhiShaderResourceBinding::Data::StorageBufferData
      yet. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiShaderResourceBinding::Data::StorageBufferData::
        ~StorageBufferData()': the destructor: Python removes its C++
        QRhiShaderResourceBinding::Data::StorageBufferData by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QRhiShaderResourceBinding::Data::StorageBufferData is created
        at the first use, not by
        'QRhiShaderResourceBinding::Data::StorageBufferData(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QRhiShaderResourceBinding::Data::StorageBufferData back gives a copy
        the ritual made for Python, in a new cute
        QRhiShaderResourceBinding::Data::StorageBufferData.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiShaderResourceBinding::Data::StorageBufferData'

      #  Qt's '~QRhiShaderResourceBinding::Data::StorageBufferData()'. Naming
      #  it makes this a value class: Python owns every C++
      #  QRhiShaderResourceBinding::Data::StorageBufferData behind a cute
      #  one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN25QRhiShaderResourceBinding4Data17StorageBufferDataD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    class StorageImageData(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QRhiShaderResourceBinding::Data::StorageImageData: a plain Python
      object standing in front of one C++
      QRhiShaderResourceBinding::Data::StorageImageData.

      C++ hands a QRhiShaderResourceBinding::Data::StorageImageData around as
      a copy, so every C++ QRhiShaderResourceBinding::Data::StorageImageData
      behind a cute one is Python's own: it is removed, by the ritual named
      in '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QRhiShaderResourceBinding::Data::StorageImageData
      yet. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiShaderResourceBinding::Data::StorageImageData::
        ~StorageImageData()': the destructor: Python removes its C++
        QRhiShaderResourceBinding::Data::StorageImageData by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QRhiShaderResourceBinding::Data::StorageImageData is created
        at the first use, not by
        'QRhiShaderResourceBinding::Data::StorageImageData(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QRhiShaderResourceBinding::Data::StorageImageData
        back gives a copy the ritual made for Python, in a new cute
        QRhiShaderResourceBinding::Data::StorageImageData.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiShaderResourceBinding::Data::StorageImageData'

      #  Qt's '~QRhiShaderResourceBinding::Data::StorageImageData()'. Naming
      #  it makes this a value class: Python owns every C++
      #  QRhiShaderResourceBinding::Data::StorageImageData behind a cute one,
      #  and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN25QRhiShaderResourceBinding4Data16StorageImageDataD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    class TextureAndOrSamplerData(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QRhiShaderResourceBinding::Data::TextureAndOrSamplerData: a plain
      Python object standing in front of one C++
      QRhiShaderResourceBinding::Data::TextureAndOrSamplerData.

      C++ hands a QRhiShaderResourceBinding::Data::TextureAndOrSamplerData
      around as a copy, so every C++
      QRhiShaderResourceBinding::Data::TextureAndOrSamplerData behind a cute
      one is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's
      QRhiShaderResourceBinding::Data::TextureAndOrSamplerData yet. None can
      be made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiShaderResourceBinding::Data::TextureAndOrSamplerData::
        ~TextureAndOrSamplerData()': the destructor: Python removes its C++
        QRhiShaderResourceBinding::Data::TextureAndOrSamplerData by it, and
        has no other use for it.

      What to expect
      --------------

      - The C++ QRhiShaderResourceBinding::Data::TextureAndOrSamplerData is
        created at the first use, not by
        'QRhiShaderResourceBinding::Data::TextureAndOrSamplerData(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QRhiShaderResourceBinding::Data::TextureAndOrSamplerData back gives a
        copy the ritual made for Python, in a new cute
        QRhiShaderResourceBinding::Data::TextureAndOrSamplerData.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiShaderResourceBinding::Data::TextureAndOrSamplerData'

      #  Qt's '~QRhiShaderResourceBinding::Data::TextureAndOrSamplerData()'.
      #  Naming it makes this a value class: Python owns every C++
      #  QRhiShaderResourceBinding::Data::TextureAndOrSamplerData behind a
      #  cute one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN25QRhiShaderResourceBinding4Data23TextureAndOrSamplerDataD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    class UniformBufferData(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QRhiShaderResourceBinding::Data::UniformBufferData: a plain Python
      object standing in front of one C++
      QRhiShaderResourceBinding::Data::UniformBufferData.

      C++ hands a QRhiShaderResourceBinding::Data::UniformBufferData around
      as a copy, so every C++
      QRhiShaderResourceBinding::Data::UniformBufferData behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QRhiShaderResourceBinding::Data::UniformBufferData
      yet. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QRhiShaderResourceBinding::Data::UniformBufferData::
        ~UniformBufferData()': the destructor: Python removes its C++
        QRhiShaderResourceBinding::Data::UniformBufferData by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QRhiShaderResourceBinding::Data::UniformBufferData is created
        at the first use, not by
        'QRhiShaderResourceBinding::Data::UniformBufferData(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QRhiShaderResourceBinding::Data::UniformBufferData back gives a copy
        the ritual made for Python, in a new cute
        QRhiShaderResourceBinding::Data::UniformBufferData.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QRhiShaderResourceBinding::Data::UniformBufferData'

      #  Qt's '~QRhiShaderResourceBinding::Data::UniformBufferData()'. Naming
      #  it makes this a value class: Python owns every C++
      #  QRhiShaderResourceBinding::Data::UniformBufferData behind a cute
      #  one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN25QRhiShaderResourceBinding4Data17UniformBufferDataD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiShaderResourceBinding::Data'

    #  Qt's '~QRhiShaderResourceBinding::Data()'. Naming it makes this a
    #  value class: Python owns every C++ QRhiShaderResourceBinding::Data
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN25QRhiShaderResourceBinding4DataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def arraySize(self) -> int:
      """
      Calls Qt's 'int QRhiShaderResourceBinding::Data::arraySize() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhishaderresourcebinding-data.html#arraySize
      """
      #  int QRhiShaderResourceBinding::Data::arraySize() const
      return self.uglySide.call(
          'ritual_ZNK25QRhiShaderResourceBinding4Data9arraySizeEv',
      )

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
    def serialize(*__, **_) -> Never:
      """
      Qt's 'QRhiShaderResourceBinding::Data::serialize': a template: a
      pattern and no single function.
      """
      raise NotImplementedError(
          "'QRhiShaderResourceBinding.Data.serialize' has no cute function "
          "yet. Qt's 'QRhiShaderResourceBinding::Data::serialize': a "
          "template: a pattern and no single function.")

  class TextureAndSampler(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiShaderResourceBinding::TextureAndSampler: a
    plain Python object standing in front of one C++
    QRhiShaderResourceBinding::TextureAndSampler.

    C++ hands a QRhiShaderResourceBinding::TextureAndSampler around as a
    copy, so every C++ QRhiShaderResourceBinding::TextureAndSampler behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiShaderResourceBinding::TextureAndSampler yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QRhiShaderResourceBinding::TextureAndSampler::~TextureAndSampler()':
      the destructor: Python removes its C++
      QRhiShaderResourceBinding::TextureAndSampler by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QRhiShaderResourceBinding::TextureAndSampler is created at the
      first use, not by 'QRhiShaderResourceBinding::TextureAndSampler(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiShaderResourceBinding::TextureAndSampler back
      gives a copy the ritual made for Python, in a new cute
      QRhiShaderResourceBinding::TextureAndSampler.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiShaderResourceBinding::TextureAndSampler'

    #  Qt's '~QRhiShaderResourceBinding::TextureAndSampler()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QRhiShaderResourceBinding::TextureAndSampler behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QRhiShaderResourceBinding17TextureAndSamplerD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer)
  @overload(int, StageFlags, NoneType)
  def uniformBuffer(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::uniformBuffer(int binding, StageFlags stage,
    QRhiBuffer *buf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#uniformBuffer

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::uniformBuffer(int
    #      binding, StageFlags stage, QRhiBuffer *buf)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding13uniformBufferEi6QFlagsINS_9S'
        'tageFlagEEP10QRhiBuffer',
        binding, stage.value, CuteMixin._addressOf(buf),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer, int, int)
  @overload(int, StageFlags, NoneType, int, int)
  def uniformBuffer(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
      offset: int,
      size: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::uniformBuffer(int binding, StageFlags stage,
    QRhiBuffer *buf, quint32 offset, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#uniformBuffer

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::uniformBuffer(int
    #      binding, StageFlags stage, QRhiBuffer *buf, quint32 offset,
    #      quint32 size)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding13uniformBufferEi6QFlagsINS_9S'
        'tageFlagEEP10QRhiBufferjj',
        binding, stage.value, CuteMixin._addressOf(buf), offset, size,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer, int)
  @overload(int, StageFlags, NoneType, int)
  def uniformBufferWithDynamicOffset(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
      size: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::uniformBufferWithDynamicOffset(int binding,
    StageFlags stage, QRhiBuffer *buf, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding
    #      QRhiShaderResourceBinding::uniformBufferWithDynamicOffset(int
    #      binding, StageFlags stage, QRhiBuffer *buf, quint32 size)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding30uniformBufferWithDynamicOffs'
        'etEi6QFlagsINS_9StageFlagEEP10QRhiBufferj',
        binding, stage.value, CuteMixin._addressOf(buf), size,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiTexture, QRhiSampler)
  @overload(int, StageFlags, QRhiTexture, NoneType)
  @overload(int, StageFlags, NoneType, QRhiSampler)
  @overload(int, StageFlags, NoneType, NoneType)
  def sampledTexture(
      binding: int,
      stage: StageFlags,
      tex: Optional[QRhiTexture],
      sampler: Optional[QRhiSampler],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::sampledTexture(int binding, StageFlags stage,
    QRhiTexture *tex, QRhiSampler *sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#sampledTexture

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sampler : Optional[QRhiSampler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding
    #      QRhiShaderResourceBinding::sampledTexture(int binding, StageFlags
    #      stage, QRhiTexture *tex, QRhiSampler *sampler)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding14sampledTextureEi6QFlagsINS_9'
        'StageFlagEEP11QRhiTextureP11QRhiSampler',
        binding, stage.value, CuteMixin._addressOf(tex),
        CuteMixin._addressOf(sampler),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, int, TextureAndSampler)
  @overload(int, StageFlags, int, NoneType)
  def sampledTextures(
      binding: int,
      stage: StageFlags,
      count: int,
      texSamplers: Optional[TextureAndSampler],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::sampledTextures(int binding, StageFlags stage,
    int count, const TextureAndSampler *texSamplers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#sampledTextures

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    count : int
      Passed on as it is.

    texSamplers : Optional[TextureAndSampler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding
    #      QRhiShaderResourceBinding::sampledTextures(int binding, StageFlags
    #      stage, int count, const TextureAndSampler *texSamplers)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding15sampledTexturesEi6QFlagsINS_'
        '9StageFlagEEiPKNS_17TextureAndSamplerE',
        binding, stage.value, count, CuteMixin._addressOf(texSamplers),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiTexture)
  @overload(int, StageFlags, NoneType)
  def texture(
      binding: int,
      stage: StageFlags,
      tex: Optional[QRhiTexture],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::texture(int binding, StageFlags stage,
    QRhiTexture *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#texture

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::texture(int
    #      binding, StageFlags stage, QRhiTexture *tex)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding7textureEi6QFlagsINS_9StageFla'
        'gEEP11QRhiTexture',
        binding, stage.value, CuteMixin._addressOf(tex),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiSampler)
  @overload(int, StageFlags, NoneType)
  def sampler(
      binding: int,
      stage: StageFlags,
      sampler: Optional[QRhiSampler],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::sampler(int binding, StageFlags stage,
    QRhiSampler *sampler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#sampler

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    sampler : Optional[QRhiSampler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::sampler(int
    #      binding, StageFlags stage, QRhiSampler *sampler)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding7samplerEi6QFlagsINS_9StageFla'
        'gEEP11QRhiSampler',
        binding, stage.value, CuteMixin._addressOf(sampler),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiTexture, int)
  @overload(int, StageFlags, NoneType, int)
  def imageLoad(
      binding: int,
      stage: StageFlags,
      tex: Optional[QRhiTexture],
      level: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::imageLoad(int binding, StageFlags stage,
    QRhiTexture *tex, int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#imageLoad

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::imageLoad(int
    #      binding, StageFlags stage, QRhiTexture *tex, int level)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding9imageLoadEi6QFlagsINS_9StageF'
        'lagEEP11QRhiTexturei',
        binding, stage.value, CuteMixin._addressOf(tex), level,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiTexture, int)
  @overload(int, StageFlags, NoneType, int)
  def imageStore(
      binding: int,
      stage: StageFlags,
      tex: Optional[QRhiTexture],
      level: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::imageStore(int binding, StageFlags stage,
    QRhiTexture *tex, int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#imageStore

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::imageStore(int
    #      binding, StageFlags stage, QRhiTexture *tex, int level)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding10imageStoreEi6QFlagsINS_9Stag'
        'eFlagEEP11QRhiTexturei',
        binding, stage.value, CuteMixin._addressOf(tex), level,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiTexture, int)
  @overload(int, StageFlags, NoneType, int)
  def imageLoadStore(
      binding: int,
      stage: StageFlags,
      tex: Optional[QRhiTexture],
      level: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::imageLoadStore(int binding, StageFlags stage,
    QRhiTexture *tex, int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#imageLoadStore

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding
    #      QRhiShaderResourceBinding::imageLoadStore(int binding, StageFlags
    #      stage, QRhiTexture *tex, int level)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding14imageLoadStoreEi6QFlagsINS_9'
        'StageFlagEEP11QRhiTexturei',
        binding, stage.value, CuteMixin._addressOf(tex), level,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer)
  @overload(int, StageFlags, NoneType)
  def bufferLoad(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::bufferLoad(int binding, StageFlags stage,
    QRhiBuffer *buf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#bufferLoad

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferLoad(int
    #      binding, StageFlags stage, QRhiBuffer *buf)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding10bufferLoadEi6QFlagsINS_9Stag'
        'eFlagEEP10QRhiBuffer',
        binding, stage.value, CuteMixin._addressOf(buf),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer, int, int)
  @overload(int, StageFlags, NoneType, int, int)
  def bufferLoad(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
      offset: int,
      size: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::bufferLoad(int binding, StageFlags stage,
    QRhiBuffer *buf, quint32 offset, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#bufferLoad

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferLoad(int
    #      binding, StageFlags stage, QRhiBuffer *buf, quint32 offset,
    #      quint32 size)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding10bufferLoadEi6QFlagsINS_9Stag'
        'eFlagEEP10QRhiBufferjj',
        binding, stage.value, CuteMixin._addressOf(buf), offset, size,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer)
  @overload(int, StageFlags, NoneType)
  def bufferStore(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::bufferStore(int binding, StageFlags stage,
    QRhiBuffer *buf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#bufferStore

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferStore(int
    #      binding, StageFlags stage, QRhiBuffer *buf)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding11bufferStoreEi6QFlagsINS_9Sta'
        'geFlagEEP10QRhiBuffer',
        binding, stage.value, CuteMixin._addressOf(buf),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer, int, int)
  @overload(int, StageFlags, NoneType, int, int)
  def bufferStore(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
      offset: int,
      size: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::bufferStore(int binding, StageFlags stage,
    QRhiBuffer *buf, quint32 offset, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#bufferStore

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferStore(int
    #      binding, StageFlags stage, QRhiBuffer *buf, quint32 offset,
    #      quint32 size)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding11bufferStoreEi6QFlagsINS_9Sta'
        'geFlagEEP10QRhiBufferjj',
        binding, stage.value, CuteMixin._addressOf(buf), offset, size,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer)
  @overload(int, StageFlags, NoneType)
  def bufferLoadStore(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::bufferLoadStore(int binding, StageFlags stage,
    QRhiBuffer *buf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#bufferLoadStore

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding
    #      QRhiShaderResourceBinding::bufferLoadStore(int binding, StageFlags
    #      stage, QRhiBuffer *buf)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding15bufferLoadStoreEi6QFlagsINS_'
        '9StageFlagEEP10QRhiBuffer',
        binding, stage.value, CuteMixin._addressOf(buf),
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  @staticmethod
  @overload(int, StageFlags, QRhiBuffer, int, int)
  @overload(int, StageFlags, NoneType, int, int)
  def bufferLoadStore(
      binding: int,
      stage: StageFlags,
      buf: Optional[QRhiBuffer],
      offset: int,
      size: int,
  ) -> QRhiShaderResourceBinding:
    """
    Calls Qt's 'QRhiShaderResourceBinding
    QRhiShaderResourceBinding::bufferLoadStore(int binding, StageFlags stage,
    QRhiBuffer *buf, quint32 offset, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#bufferLoadStore

    Parameters
    ----------

    binding : int
      Passed on as it is.

    stage : StageFlags
      Passed on as its number.

    buf : Optional[QRhiBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.

    Returns
    -------

    QRhiShaderResourceBinding
      A new cute QRhiShaderResourceBinding around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiShaderResourceBinding
    #      QRhiShaderResourceBinding::bufferLoadStore(int binding, StageFlags
    #      stage, QRhiBuffer *buf, quint32 offset, quint32 size)
    address = Rituals.call(
        'ritual_ZN25QRhiShaderResourceBinding15bufferLoadStoreEi6QFlagsINS_'
        '9StageFlagEEP10QRhiBufferjj',
        binding, stage.value, CuteMixin._addressOf(buf), offset, size,
    )
    return QRhiShaderResourceBinding._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiShaderResourceBinding'

  #  Qt's '~QRhiShaderResourceBinding()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiShaderResourceBinding behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QRhiShaderResourceBindingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def isLayoutCompatible(self, other: QRhiShaderResourceBinding) -> bool:
    """
    Calls Qt's 'bool QRhiShaderResourceBinding::isLayoutCompatible(const
    QRhiShaderResourceBinding &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html#isLayoutCompatible

    Parameters
    ----------

    other : QRhiShaderResourceBinding
      Passed on as a value: Qt reads the C++ QRhiShaderResourceBinding, which
      stays Python's own.
    """
    #  bool QRhiShaderResourceBinding::isLayoutCompatible(const
    #      QRhiShaderResourceBinding &other) const
    return self.uglySide.call(
        'ritual_ZNK25QRhiShaderResourceBinding18isLayoutCompatibleERKS_',
        self._valueOf(other),
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
    'QRhiShaderResourceBinding::QRhiShaderResourceBinding()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebinding.html
    """
    #  QRhiShaderResourceBinding::QRhiShaderResourceBinding()
    self._noteCreation(QRhiShaderResourceBinding, lambda: Rituals.call(
        'ritual_ZN25QRhiShaderResourceBindingC1Ev',
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
  def serializeLayoutDescription(*__, **_) -> Never:
    """
    Qt's 'QRhiShaderResourceBinding::serializeLayoutDescription': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'QRhiShaderResourceBinding.serializeLayoutDescription' has no cute "
        "function yet. Qt's "
        "'QRhiShaderResourceBinding::serializeLayoutDescription': a "
        "template: a pattern and no single function.")

  @staticmethod
  def textures(*__, **_) -> Never:
    """
    Qt's 'QRhiShaderResourceBinding QRhiShaderResourceBinding::textures(int
    binding, StageFlags stage, int count, QRhiTexture **tex)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRhiShaderResourceBinding.textures' has no cute function yet. "
        "Qt's 'QRhiShaderResourceBinding "
        "QRhiShaderResourceBinding::textures(int binding, StageFlags stage, "
        "int count, QRhiTexture **tex)': takes a type Python has no way to "
        "hand over yet.")
