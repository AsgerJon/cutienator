"""
QSpirvShader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtShaderTools/6.12.0/QtShaderTools/private/qspirvshader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSpirvShader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QString
  from ..QtGui import QShaderDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpirvShader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSpirvShader: a plain Python object standing in front
  of one C++ QSpirvShader.

  What exists
  -----------

  Every function of Qt's QSpirvShader that has a ritual and that Python can
  call so far, 5 names in all: 'setSpirvBinary', 'shaderDescription',
  'spirvBinary', 'remappedSpirvBinary', 'translationErrorMessage'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSpirvShader::~QSpirvShader()': the destructor: Python never
    removes a C++ QSpirvShader.
  - Qt's 'QByteArray QSpirvShader::translateToGLSL(int version, GlslFlags
    flags, QShader::Stage stage, const MultiViewInfo &multiViewInfo,
    QVector<SeparateToCombinedImageSamplerMapping>
    *separateToCombinedImageSamplerMappings) const': names
    'QVector<QSpirvShader::SeparateToCombinedImageSamplerMapping>', which has
    no cute class yet.
  - Qt's 'QByteArray QSpirvShader::translateToHLSL(int version,
    QShader::NativeResourceBindingMap *nativeBindings) const': names
    'QShader::NativeResourceBindingMap', which has no cute class yet.
  - Qt's 'QByteArray QSpirvShader::translateToMSL(int version, MslFlags
    flags, QShader::Stage stage, QShader::NativeResourceBindingMap
    *nativeBindings, QShader::NativeShaderInfo *shaderInfo, const
    MultiViewInfo &multiViewInfo, const TessellationInfo &tessInfo) const':
    names 'QShader::NativeResourceBindingMap', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSpirvShader is created at the first use, not by
    'QSpirvShader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpirvShader.
  - Each name of Qt's QSpirvShader that has no cute function yet,
    'translateToGLSL', 'translateToHLSL', 'translateToMSL', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSpirvShader, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class GlslFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSpirvShader::GlslFlag' of Qt, with the 3 names Qt gives
    in it. Qt names the type of its combinations 'QSpirvShader::GlslFlags'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    GlslEs = 0x1
    FixClipSpace = 0x2
    EsFragDefaultFloatPrecisionMedium = 0x4

  GlslFlags = GlslFlag

  class MslFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSpirvShader::MslFlag' of Qt, with the 3 names Qt gives
    in it. Qt names the type of its combinations 'QSpirvShader::MslFlags'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    VertexAsCompute = 0x1
    WithUInt16Index = 0x2
    WithUInt32Index = 0x4

  MslFlags = MslFlag

  class RemapFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSpirvShader::RemapFlag' of Qt, with the 1 names Qt gives
    in it. Qt names the type of its combinations 'QSpirvShader::RemapFlags'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    StripOnly = 0x1

  RemapFlags = RemapFlag

  #  The classes Qt writes inside QSpirvShader, each a class in here as in
  #  C++.

  class MultiViewInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSpirvShader::MultiViewInfo: a plain Python object
    standing in front of one C++ QSpirvShader::MultiViewInfo.

    C++ hands a QSpirvShader::MultiViewInfo around as a copy, so every C++
    QSpirvShader::MultiViewInfo behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSpirvShader::MultiViewInfo yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSpirvShader::MultiViewInfo::~MultiViewInfo()': the destructor:
      Python removes its C++ QSpirvShader::MultiViewInfo by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSpirvShader::MultiViewInfo is created at the first use, not by
      'QSpirvShader::MultiViewInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSpirvShader::MultiViewInfo back gives a copy the
      ritual made for Python, in a new cute QSpirvShader::MultiViewInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSpirvShader::MultiViewInfo'

    #  Qt's '~QSpirvShader::MultiViewInfo()'. Naming it makes this a value
    #  class: Python owns every C++ QSpirvShader::MultiViewInfo behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QSpirvShader13MultiViewInfoD1Ev'

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

  class SeparateToCombinedImageSamplerMapping(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSpirvShader::SeparateToCombinedImageSamplerMapping: a plain Python
    object standing in front of one C++
    QSpirvShader::SeparateToCombinedImageSamplerMapping.

    C++ hands a QSpirvShader::SeparateToCombinedImageSamplerMapping around as
    a copy, so every C++ QSpirvShader::SeparateToCombinedImageSamplerMapping
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSpirvShader::SeparateToCombinedImageSamplerMapping
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSpirvShader::SeparateToCombinedImageSamplerMapping::
      ~SeparateToCombinedImageSamplerMapping()': the destructor: Python
      removes its C++ QSpirvShader::SeparateToCombinedImageSamplerMapping by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSpirvShader::SeparateToCombinedImageSamplerMapping is created
      at the first use, not by
      'QSpirvShader::SeparateToCombinedImageSamplerMapping(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSpirvShader::SeparateToCombinedImageSamplerMapping
      back gives a copy the ritual made for Python, in a new cute
      QSpirvShader::SeparateToCombinedImageSamplerMapping.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSpirvShader::SeparateToCombinedImageSamplerMapping'

    #  Qt's '~QSpirvShader::SeparateToCombinedImageSamplerMapping()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QSpirvShader::SeparateToCombinedImageSamplerMapping behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN12QSpirvShader37SeparateToCombinedImageSamplerMappingD1Ev')

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

  class TessellationInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSpirvShader::TessellationInfo: a plain Python
    object standing in front of one C++ QSpirvShader::TessellationInfo.

    C++ hands a QSpirvShader::TessellationInfo around as a copy, so every C++
    QSpirvShader::TessellationInfo behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSpirvShader::TessellationInfo yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSpirvShader::TessellationInfo::~TessellationInfo()': the
      destructor: Python removes its C++ QSpirvShader::TessellationInfo by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSpirvShader::TessellationInfo is created at the first use, not
      by 'QSpirvShader::TessellationInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSpirvShader::TessellationInfo back gives a copy
      the ritual made for Python, in a new cute
      QSpirvShader::TessellationInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSpirvShader::TessellationInfo'

    #  Qt's '~QSpirvShader::TessellationInfo()'. Naming it makes this a value
    #  class: Python owns every C++ QSpirvShader::TessellationInfo behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QSpirvShader16TessellationInfoD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpirvShader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shaderDescription(self) -> QShaderDescription:
    """
    Calls Qt's 'QShaderDescription QSpirvShader::shaderDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvshader.html#shaderDescription

    Returns
    -------

    QShaderDescription
      A new cute QShaderDescription around the copy Qt gave back. Python owns
      it.
    """
    #  QShaderDescription QSpirvShader::shaderDescription() const
    address = self.uglySide.call(
        'ritual_ZNK12QSpirvShader17shaderDescriptionEv',
    )
    from ..QtGui import QShaderDescription
    return QShaderDescription._cuteOwning(address)

  def spirvBinary(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSpirvShader::spirvBinary() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspirvshader.html#spirvBinary

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSpirvShader::spirvBinary() const
    address = self.uglySide.call('ritual_ZNK12QSpirvShader11spirvBinaryEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(RemapFlags)
  @overload(RemapFlags, QString)
  @overload(RemapFlags, NoneType)
  def remappedSpirvBinary(
      self,
      flags: RemapFlags = RemapFlags(),
      errorMessage: Optional[QString] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSpirvShader::remappedSpirvBinary(RemapFlags
    flags, QString *errorMessage) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvshader.html#remappedSpirvBinary

    Parameters
    ----------

    flags : RemapFlags
      Passed on as its number. May be left out, as in Qt: it is then
      RemapFlags().

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSpirvShader::remappedSpirvBinary(RemapFlags flags, QString
    #      *errorMessage) const
    address = self.uglySide.call(
        'ritual_ZNK12QSpirvShader19remappedSpirvBinaryE6QFlagsINS_9RemapFla'
        'gEEP7QString',
        flags.value, self._addressOf(errorMessage),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def translationErrorMessage(self) -> str:
    """
    Calls Qt's 'QString QSpirvShader::translationErrorMessage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvshader.html#translationErrorMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSpirvShader::translationErrorMessage() const
    return self.uglySide.call(
        'ritual_ZNK12QSpirvShader23translationErrorMessageEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray, QShader.Stage)
  def setSpirvBinary(self, spirv: QByteArray, stage: QShader.Stage) -> None:
    """
    Calls Qt's 'void QSpirvShader::setSpirvBinary(const QByteArray &spirv,
    QShader::Stage stage)'.

    Qt's own words: https://doc.qt.io/qt-6/qspirvshader.html#setSpirvBinary

    Parameters
    ----------

    spirv : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    stage : QShader.Stage
      Passed on as its number.
    """
    #  void QSpirvShader::setSpirvBinary(const QByteArray &spirv,
    #      QShader::Stage stage)
    self.uglySide.call(
        'ritual_ZN12QSpirvShader14setSpirvBinaryERK10QByteArrayN7QShader5St'
        'ageE',
        self._valueOf(spirv), stage.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSpirvShader::QSpirvShader()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qspirvshader.html#QSpirvShader
    """
    #  QSpirvShader::QSpirvShader()
    self._noteCreation(QSpirvShader, lambda: Rituals.call(
        'ritual_ZN12QSpirvShaderC1Ev',
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
  def translateToGLSL(*__, **_) -> Never:
    """
    Qt's 'QByteArray QSpirvShader::translateToGLSL(int version, GlslFlags
    flags, QShader::Stage stage, const MultiViewInfo &multiViewInfo,
    QVector<SeparateToCombinedImageSamplerMapping>
    *separateToCombinedImageSamplerMappings) const': names
    'QVector<QSpirvShader::SeparateToCombinedImageSamplerMapping>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QSpirvShader.translateToGLSL' has no cute function yet. Qt's "
        "'QByteArray QSpirvShader::translateToGLSL(int version, GlslFlags "
        "flags, QShader::Stage stage, const MultiViewInfo &multiViewInfo, "
        "QVector<SeparateToCombinedImageSamplerMapping> "
        "*separateToCombinedImageSamplerMappings) const': names "
        "'QVector<QSpirvShader::SeparateToCombinedImageSamplerMapping>', "
        "which has no cute class yet.")

  @staticmethod
  def translateToHLSL(*__, **_) -> Never:
    """
    Qt's 'QByteArray QSpirvShader::translateToHLSL(int version,
    QShader::NativeResourceBindingMap *nativeBindings) const': names
    'QShader::NativeResourceBindingMap', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSpirvShader.translateToHLSL' has no cute function yet. Qt's "
        "'QByteArray QSpirvShader::translateToHLSL(int version, "
        "QShader::NativeResourceBindingMap *nativeBindings) const': names "
        "'QShader::NativeResourceBindingMap', which has no cute class yet.")

  @staticmethod
  def translateToMSL(*__, **_) -> Never:
    """
    Qt's 'QByteArray QSpirvShader::translateToMSL(int version, MslFlags
    flags, QShader::Stage stage, QShader::NativeResourceBindingMap
    *nativeBindings, QShader::NativeShaderInfo *shaderInfo, const
    MultiViewInfo &multiViewInfo, const TessellationInfo &tessInfo) const':
    names 'QShader::NativeResourceBindingMap', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSpirvShader.translateToMSL' has no cute function yet. Qt's "
        "'QByteArray QSpirvShader::translateToMSL(int version, MslFlags "
        "flags, QShader::Stage stage, QShader::NativeResourceBindingMap "
        "*nativeBindings, QShader::NativeShaderInfo *shaderInfo, const "
        "MultiViewInfo &multiViewInfo, const TessellationInfo &tessInfo) "
        "const': names 'QShader::NativeResourceBindingMap', which has no "
        "cute class yet.")
