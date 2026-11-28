"""
QSSGRhiContextStats binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiContextStats to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiTextureRenderTarget
  from . import QSSGRenderLayer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiTextureRenderTarget = WAIT['QRhiTextureRenderTarget']
  QSSGRenderLayer = WAIT['QSSGRenderLayer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiContextStats(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiContextStats: a plain Python object standing
  in front of one C++ QSSGRhiContextStats.

  C++ hands a QSSGRhiContextStats around as a copy, so every C++
  QSSGRhiContextStats behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiContextStats that has a ritual and that
  Python can call so far, 17 names in all: 'profilingEnabled',
  'rendererDebugEnabled', 'isEnabled', 'drawIndexed', 'draw',
  'meshDataSizeChanges', 'imageDataSizeChanges',
  'registerMaterialShaderGenerationTime',
  'registerEffectShaderGenerationTime', 'totalDrawCallCountForPass',
  'totalVertexCountForPass', 'start', 'stop', 'beginRenderPass',
  'endRenderPass', 'printRenderPass', 'cleanupLayerInfo'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiContextStats &QSSGRhiContextStats::get(QSSGRhiContext
    &rhiCtx)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSSGRhiContextStats &QSSGRhiContextStats::get(const
    QSSGRhiContext &rhiCtx)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGRhiContextStats::QSSGRhiContextStats(QSSGRhiContext &context)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiContextStats::~QSSGRhiContextStats()': the destructor:
    Python removes its C++ QSSGRhiContextStats by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGRhiContextStats is created at the first use, not by
    'QSSGRhiContextStats(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiContextStats back gives a copy the ritual made
    for Python, in a new cute QSSGRhiContextStats.
  - Each name of Qt's QSSGRhiContextStats that has no cute function yet,
    '__init__', 'get', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QSSGRhiContextStats, each a class in here
  #  as in C++.

  class DrawInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRhiContextStats::DrawInfo: a plain Python
    object standing in front of one C++ QSSGRhiContextStats::DrawInfo.

    C++ hands a QSSGRhiContextStats::DrawInfo around as a copy, so every C++
    QSSGRhiContextStats::DrawInfo behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGRhiContextStats::DrawInfo yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRhiContextStats::DrawInfo::~DrawInfo()': the destructor:
      Python removes its C++ QSSGRhiContextStats::DrawInfo by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGRhiContextStats::DrawInfo is created at the first use, not
      by 'QSSGRhiContextStats::DrawInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRhiContextStats::DrawInfo back gives a copy the
      ritual made for Python, in a new cute QSSGRhiContextStats::DrawInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRhiContextStats::DrawInfo'

    #  Qt's '~QSSGRhiContextStats::DrawInfo()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGRhiContextStats::DrawInfo behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QSSGRhiContextStats8DrawInfoD1Ev'

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

  class GlobalInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRhiContextStats::GlobalInfo: a plain Python
    object standing in front of one C++ QSSGRhiContextStats::GlobalInfo.

    C++ hands a QSSGRhiContextStats::GlobalInfo around as a copy, so every
    C++ QSSGRhiContextStats::GlobalInfo behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSSGRhiContextStats::GlobalInfo yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRhiContextStats::GlobalInfo::~GlobalInfo()': the destructor:
      Python removes its C++ QSSGRhiContextStats::GlobalInfo by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QSSGRhiContextStats::GlobalInfo is created at the first use,
      not by 'QSSGRhiContextStats::GlobalInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRhiContextStats::GlobalInfo back gives a copy
      the ritual made for Python, in a new cute
      QSSGRhiContextStats::GlobalInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRhiContextStats::GlobalInfo'

    #  Qt's '~QSSGRhiContextStats::GlobalInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRhiContextStats::GlobalInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QSSGRhiContextStats10GlobalInfoD1Ev'

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

  class InstancedDrawInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRhiContextStats::InstancedDrawInfo: a plain
    Python object standing in front of one C++
    QSSGRhiContextStats::InstancedDrawInfo.

    C++ hands a QSSGRhiContextStats::InstancedDrawInfo around as a copy, so
    every C++ QSSGRhiContextStats::InstancedDrawInfo behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRhiContextStats::InstancedDrawInfo yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRhiContextStats::InstancedDrawInfo::~InstancedDrawInfo()':
      the destructor: Python removes its C++
      QSSGRhiContextStats::InstancedDrawInfo by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGRhiContextStats::InstancedDrawInfo is created at the first
      use, not by 'QSSGRhiContextStats::InstancedDrawInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRhiContextStats::InstancedDrawInfo back gives a
      copy the ritual made for Python, in a new cute
      QSSGRhiContextStats::InstancedDrawInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRhiContextStats::InstancedDrawInfo'

    #  Qt's '~QSSGRhiContextStats::InstancedDrawInfo()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QSSGRhiContextStats::InstancedDrawInfo behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QSSGRhiContextStats17InstancedDrawInfoD1Ev')

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

  class PerLayerInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRhiContextStats::PerLayerInfo: a plain Python
    object standing in front of one C++ QSSGRhiContextStats::PerLayerInfo.

    C++ hands a QSSGRhiContextStats::PerLayerInfo around as a copy, so every
    C++ QSSGRhiContextStats::PerLayerInfo behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSSGRhiContextStats::PerLayerInfo yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRhiContextStats::PerLayerInfo::~PerLayerInfo()': the
      destructor: Python removes its C++ QSSGRhiContextStats::PerLayerInfo by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRhiContextStats::PerLayerInfo is created at the first use,
      not by 'QSSGRhiContextStats::PerLayerInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRhiContextStats::PerLayerInfo back gives a copy
      the ritual made for Python, in a new cute
      QSSGRhiContextStats::PerLayerInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRhiContextStats::PerLayerInfo'

    #  Qt's '~QSSGRhiContextStats::PerLayerInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRhiContextStats::PerLayerInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QSSGRhiContextStats12PerLayerInfoD1Ev'

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
      'QSSGRhiContextStats::PerLayerInfo::PerLayerInfo()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrhicontextstats-perlayerinfo.html
      """
      #  QSSGRhiContextStats::PerLayerInfo::PerLayerInfo()
      self._noteCreation(
          QSSGRhiContextStats.PerLayerInfo, lambda: Rituals.call(
              'ritual_ZN19QSSGRhiContextStats12PerLayerInfoC1Ev',
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

  class RenderPassInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRhiContextStats::RenderPassInfo: a plain Python
    object standing in front of one C++ QSSGRhiContextStats::RenderPassInfo.

    C++ hands a QSSGRhiContextStats::RenderPassInfo around as a copy, so
    every C++ QSSGRhiContextStats::RenderPassInfo behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRhiContextStats::RenderPassInfo yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRhiContextStats::RenderPassInfo::~RenderPassInfo()': the
      destructor: Python removes its C++ QSSGRhiContextStats::RenderPassInfo
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRhiContextStats::RenderPassInfo is created at the first
      use, not by 'QSSGRhiContextStats::RenderPassInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRhiContextStats::RenderPassInfo back gives a
      copy the ritual made for Python, in a new cute
      QSSGRhiContextStats::RenderPassInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRhiContextStats::RenderPassInfo'

    #  Qt's '~QSSGRhiContextStats::RenderPassInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRhiContextStats::RenderPassInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QSSGRhiContextStats14RenderPassInfoD1Ev'

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
  def profilingEnabled() -> bool:
    """
    Calls Qt's 'bool QSSGRhiContextStats::profilingEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#profilingEnabled
    """
    #  bool QSSGRhiContextStats::profilingEnabled()
    return Rituals.call('ritual_ZN19QSSGRhiContextStats16profilingEnabledEv')

  @staticmethod
  def rendererDebugEnabled() -> bool:
    """
    Calls Qt's 'bool QSSGRhiContextStats::rendererDebugEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#rendererDebugEnabled
    """
    #  bool QSSGRhiContextStats::rendererDebugEnabled()
    return Rituals.call(
        'ritual_ZN19QSSGRhiContextStats20rendererDebugEnabledEv',
    )

  @staticmethod
  @overload(RenderPassInfo)
  def totalDrawCallCountForPass(pass_: RenderPassInfo) -> int:
    """
    Calls Qt's 'quint64 QSSGRhiContextStats::totalDrawCallCountForPass(const
    QSSGRhiContextStats::RenderPassInfo &pass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#totalDrawCallCountForPass

    Parameters
    ----------

    pass_ : RenderPassInfo
      Passed on as a value: Qt reads the C++
      QSSGRhiContextStats::RenderPassInfo, which stays Python's own.
    """
    #  quint64 QSSGRhiContextStats::totalDrawCallCountForPass(const
    #      QSSGRhiContextStats::RenderPassInfo &pass)
    return Rituals.call(
        'ritual_ZN19QSSGRhiContextStats25totalDrawCallCountForPassERKNS_14R'
        'enderPassInfoE',
        CuteMixin._valueOf(pass_),
    )

  @staticmethod
  @overload(RenderPassInfo)
  def totalVertexCountForPass(pass_: RenderPassInfo) -> int:
    """
    Calls Qt's 'quint64 QSSGRhiContextStats::totalVertexCountForPass(const
    QSSGRhiContextStats::RenderPassInfo &pass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#totalVertexCountForPass

    Parameters
    ----------

    pass_ : RenderPassInfo
      Passed on as a value: Qt reads the C++
      QSSGRhiContextStats::RenderPassInfo, which stays Python's own.
    """
    #  quint64 QSSGRhiContextStats::totalVertexCountForPass(const
    #      QSSGRhiContextStats::RenderPassInfo &pass)
    return Rituals.call(
        'ritual_ZN19QSSGRhiContextStats23totalVertexCountForPassERKNS_14Ren'
        'derPassInfoE',
        CuteMixin._valueOf(pass_),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiContextStats'

  #  Qt's '~QSSGRhiContextStats()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRhiContextStats behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGRhiContextStatsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRhiContextStats::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontextstats.html#isEnabled
    """
    #  bool QSSGRhiContextStats::isEnabled() const
    return self.uglySide.call('ritual_ZNK19QSSGRhiContextStats9isEnabledEv')

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
    Qt's 'QSSGRhiContextStats::QSSGRhiContextStats(QSSGRhiContext &context)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextStats.__init__' has no cute function yet. Qt's "
        "'QSSGRhiContextStats::QSSGRhiContextStats(QSSGRhiContext "
        "&context)': takes a type Python has no way to hand over yet.")

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
  def drawIndexed(self, indexCount: int, instanceCount: int) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::drawIndexed(quint32 indexCount,
    quint32 instanceCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#drawIndexed

    Parameters
    ----------

    indexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is.
    """
    #  void QSSGRhiContextStats::drawIndexed(quint32 indexCount, quint32
    #      instanceCount)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats11drawIndexedEjj',
        indexCount, instanceCount,
    )

  @overload(int, int)
  def draw(self, vertexCount: int, instanceCount: int) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::draw(quint32 vertexCount, quint32
    instanceCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontextstats.html#draw

    Parameters
    ----------

    vertexCount : int
      Passed on as it is.

    instanceCount : int
      Passed on as it is.
    """
    #  void QSSGRhiContextStats::draw(quint32 vertexCount, quint32
    #      instanceCount)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats4drawEjj', vertexCount, instanceCount,
    )

  @overload(int)
  def meshDataSizeChanges(self, newSize: int) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::meshDataSizeChanges(quint64
    newSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#meshDataSizeChanges

    Parameters
    ----------

    newSize : int
      Passed on as it is.
    """
    #  void QSSGRhiContextStats::meshDataSizeChanges(quint64 newSize)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats19meshDataSizeChangesEy', newSize,
    )

  @overload(int)
  def imageDataSizeChanges(self, newSize: int) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::imageDataSizeChanges(quint64
    newSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#imageDataSizeChanges

    Parameters
    ----------

    newSize : int
      Passed on as it is.
    """
    #  void QSSGRhiContextStats::imageDataSizeChanges(quint64 newSize)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats20imageDataSizeChangesEy', newSize,
    )

  @overload(int)
  def registerMaterialShaderGenerationTime(self, ms: int) -> None:
    """
    Calls Qt's 'void
    QSSGRhiContextStats::registerMaterialShaderGenerationTime(qint64 ms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html

    Parameters
    ----------

    ms : int
      Passed on as it is.
    """
    #  void QSSGRhiContextStats::registerMaterialShaderGenerationTime(qint64
    #      ms)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats36registerMaterialShaderGenerationTi'
        'meEx',
        ms,
    )

  @overload(int)
  def registerEffectShaderGenerationTime(self, ms: int) -> None:
    """
    Calls Qt's 'void
    QSSGRhiContextStats::registerEffectShaderGenerationTime(qint64 ms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html

    Parameters
    ----------

    ms : int
      Passed on as it is.
    """
    #  void QSSGRhiContextStats::registerEffectShaderGenerationTime(qint64
    #      ms)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats34registerEffectShaderGenerationTime'
        'Ex',
        ms,
    )

  @overload(QSSGRenderLayer)
  @overload(NoneType)
  def start(self, layer: Optional[QSSGRenderLayer]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::start(QSSGRenderLayer *layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontextstats.html#start

    Parameters
    ----------

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextStats::start(QSSGRenderLayer *layer)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats5startEP15QSSGRenderLayer',
        self._addressOf(layer),
    )

  @overload(QSSGRenderLayer)
  @overload(NoneType)
  def stop(self, layer: Optional[QSSGRenderLayer]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::stop(QSSGRenderLayer *layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontextstats.html#stop

    Parameters
    ----------

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextStats::stop(QSSGRenderLayer *layer)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats4stopEP15QSSGRenderLayer',
        self._addressOf(layer),
    )

  @overload(QRhiTextureRenderTarget)
  @overload(NoneType)
  def beginRenderPass(self, rt: Optional[QRhiTextureRenderTarget]) -> None:
    """
    Calls Qt's 'void
    QSSGRhiContextStats::beginRenderPass(QRhiTextureRenderTarget *rt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#beginRenderPass

    Parameters
    ----------

    rt : Optional[QRhiTextureRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextStats::beginRenderPass(QRhiTextureRenderTarget *rt)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats15beginRenderPassEP23QRhiTextureRend'
        'erTarget',
        self._addressOf(rt),
    )

  def endRenderPass(self) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::endRenderPass()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#endRenderPass
    """
    #  void QSSGRhiContextStats::endRenderPass()
    self.uglySide.call('ritual_ZN19QSSGRhiContextStats13endRenderPassEv')

  @overload(RenderPassInfo)
  def printRenderPass(self, rp: RenderPassInfo) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::printRenderPass(const
    RenderPassInfo &rp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#printRenderPass

    Parameters
    ----------

    rp : RenderPassInfo
      Passed on as a value: Qt reads the C++
      QSSGRhiContextStats::RenderPassInfo, which stays Python's own.
    """
    #  void QSSGRhiContextStats::printRenderPass(const RenderPassInfo &rp)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats15printRenderPassERKNS_14RenderPassI'
        'nfoE',
        self._valueOf(rp),
    )

  @overload(QSSGRenderLayer)
  @overload(NoneType)
  def cleanupLayerInfo(self, layer: Optional[QSSGRenderLayer]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextStats::cleanupLayerInfo(QSSGRenderLayer
    *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextstats.html#cleanupLayerInfo

    Parameters
    ----------

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextStats::cleanupLayerInfo(QSSGRenderLayer *layer)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiContextStats16cleanupLayerInfoEP15QSSGRenderLaye'
        'r',
        self._addressOf(layer),
    )

  @staticmethod
  def get(*__, **_) -> Never:
    """
    - Qt's 'QSSGRhiContextStats &QSSGRhiContextStats::get(QSSGRhiContext
      &rhiCtx)': takes a type Python has no way to hand over yet.
    - Qt's 'const QSSGRhiContextStats &QSSGRhiContextStats::get(const
      QSSGRhiContext &rhiCtx)': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextStats.get' has no cute function yet. Qt's "
        "'QSSGRhiContextStats &QSSGRhiContextStats::get(QSSGRhiContext "
        "&rhiCtx)': takes a type Python has no way to hand over yet. Qt's "
        "'const QSSGRhiContextStats &QSSGRhiContextStats::get(const "
        "QSSGRhiContext &rhiCtx)': takes a type Python has no way to hand "
        "over yet.")
