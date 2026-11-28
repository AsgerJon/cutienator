"""
QSSGShaderResourceMergeContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshaderresourcemergecontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderResourceMergeContext to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QSSGRenderShaderMetadata

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSSGShaderResourceMergeContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderResourceMergeContext: a plain Python object
  standing in front of one C++ QSSGShaderResourceMergeContext.

  C++ hands a QSSGShaderResourceMergeContext around as a copy, so every C++
  QSSGShaderResourceMergeContext behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderResourceMergeContext that has a ritual and
  that Python can call so far, 3 names in all: 'registerSampler',
  'registerImage', 'registerUniformMember'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QSSGShaderResourceMergeContext::registerInput(QSSGShaderGeneratorStage
    stage, const QByteArray &type, const QByteArray &name, bool flat)': names
    the enum 'QSSGShaderGeneratorStage', whose class cannot be named here.
  - Qt's 'void
    QSSGShaderResourceMergeContext::registerOutput(QSSGShaderGeneratorStage
    stage, const QByteArray &type, const QByteArray &name, bool flat)': names
    the enum 'QSSGShaderGeneratorStage', whose class cannot be named here.
  - Qt's 'QSSGShaderResourceMergeContext::~QSSGShaderResourceMergeContext()':
    the destructor: Python removes its C++ QSSGShaderResourceMergeContext by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 3 leans on
  'QSSGShaderResourceMergeContext.

  What to expect
  --------------

  - The C++ QSSGShaderResourceMergeContext is created at the first use, not
    by 'QSSGShaderResourceMergeContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderResourceMergeContext back gives a copy the
    ritual made for Python, in a new cute QSSGShaderResourceMergeContext.
  - Each name of Qt's QSSGShaderResourceMergeContext that has no cute
    function yet, '__init__', 'rearrangeResources', 'registerInput',
    'registerOutput', 'setAdditionalBufferAmount', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSSGShaderResourceMergeContext, each a
  #  class in here as in C++.

  class BlockMember(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGShaderResourceMergeContext::BlockMember: a
    plain Python object standing in front of one C++
    QSSGShaderResourceMergeContext::BlockMember.

    C++ hands a QSSGShaderResourceMergeContext::BlockMember around as a copy,
    so every C++ QSSGShaderResourceMergeContext::BlockMember behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGShaderResourceMergeContext::BlockMember yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderResourceMergeContext::BlockMember::~BlockMember()': the
      destructor: Python removes its C++
      QSSGShaderResourceMergeContext::BlockMember by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGShaderResourceMergeContext::BlockMember is created at the
      first use, not by 'QSSGShaderResourceMergeContext::BlockMember(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGShaderResourceMergeContext::BlockMember back
      gives a copy the ritual made for Python, in a new cute
      QSSGShaderResourceMergeContext::BlockMember.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderResourceMergeContext::BlockMember'

    #  Qt's '~QSSGShaderResourceMergeContext::BlockMember()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGShaderResourceMergeContext::BlockMember behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QSSGShaderResourceMergeContext11BlockMemberD1Ev')

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

  class Image(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGShaderResourceMergeContext::Image: a plain
    Python object standing in front of one C++
    QSSGShaderResourceMergeContext::Image.

    C++ hands a QSSGShaderResourceMergeContext::Image around as a copy, so
    every C++ QSSGShaderResourceMergeContext::Image behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGShaderResourceMergeContext::Image yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderResourceMergeContext::Image::~Image()': the destructor:
      Python removes its C++ QSSGShaderResourceMergeContext::Image by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QSSGShaderResourceMergeContext::Image is created at the first
      use, not by 'QSSGShaderResourceMergeContext::Image(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGShaderResourceMergeContext::Image back gives a
      copy the ritual made for Python, in a new cute
      QSSGShaderResourceMergeContext::Image.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderResourceMergeContext::Image'

    #  Qt's '~QSSGShaderResourceMergeContext::Image()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QSSGShaderResourceMergeContext::Image behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN30QSSGShaderResourceMergeContext5ImageD1Ev'

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

  class InOutVar(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGShaderResourceMergeContext::InOutVar: a plain
    Python object standing in front of one C++
    QSSGShaderResourceMergeContext::InOutVar.

    C++ hands a QSSGShaderResourceMergeContext::InOutVar around as a copy, so
    every C++ QSSGShaderResourceMergeContext::InOutVar behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGShaderResourceMergeContext::InOutVar yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderResourceMergeContext::InOutVar::~InOutVar()': the
      destructor: Python removes its C++
      QSSGShaderResourceMergeContext::InOutVar by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGShaderResourceMergeContext::InOutVar is created at the
      first use, not by 'QSSGShaderResourceMergeContext::InOutVar(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGShaderResourceMergeContext::InOutVar back gives
      a copy the ritual made for Python, in a new cute
      QSSGShaderResourceMergeContext::InOutVar.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderResourceMergeContext::InOutVar'

    #  Qt's '~QSSGShaderResourceMergeContext::InOutVar()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGShaderResourceMergeContext::InOutVar behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QSSGShaderResourceMergeContext8InOutVarD1Ev')

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

  class Sampler(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGShaderResourceMergeContext::Sampler: a plain
    Python object standing in front of one C++
    QSSGShaderResourceMergeContext::Sampler.

    C++ hands a QSSGShaderResourceMergeContext::Sampler around as a copy, so
    every C++ QSSGShaderResourceMergeContext::Sampler behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGShaderResourceMergeContext::Sampler yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderResourceMergeContext::Sampler::~Sampler()': the
      destructor: Python removes its C++
      QSSGShaderResourceMergeContext::Sampler by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGShaderResourceMergeContext::Sampler is created at the first
      use, not by 'QSSGShaderResourceMergeContext::Sampler(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGShaderResourceMergeContext::Sampler back gives
      a copy the ritual made for Python, in a new cute
      QSSGShaderResourceMergeContext::Sampler.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderResourceMergeContext::Sampler'

    #  Qt's '~QSSGShaderResourceMergeContext::Sampler()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGShaderResourceMergeContext::Sampler behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QSSGShaderResourceMergeContext7SamplerD1Ev')

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
  __qt_class__ = 'QSSGShaderResourceMergeContext'

  #  Qt's '~QSSGShaderResourceMergeContext()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGShaderResourceMergeContext behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QSSGShaderResourceMergeContextD1Ev'

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
    Qt's 'QSSGShaderResourceMergeContext::QSSGShaderResourceMergeContext()':
    leans on 'QSSGShaderResourceMergeContext::s_additionalBuffers', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QSSGShaderResourceMergeContext.__init__' has no cute function "
        "yet. Qt's "
        "'QSSGShaderResourceMergeContext::QSSGShaderResourceMergeContext()':"
        " leans on 'QSSGShaderResourceMergeContext::s_additionalBuffers', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QByteArray, QByteArray)
  @overload(
      QByteArray, QByteArray, QSSGRenderShaderMetadata.Uniform.Condition,
  )
  @overload(
      QByteArray, QByteArray, QSSGRenderShaderMetadata.Uniform.Condition,
      QByteArray,
  )
  def registerSampler(
      self,
      type: QByteArray,
      name: QByteArray,
      conditionType: QSSGRenderShaderMetadata.Uniform.Condition = (
          QSSGRenderShaderMetadata.Uniform.Condition.NULL),
      conditionName: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void QSSGShaderResourceMergeContext::registerSampler(const
    QByteArray &type, const QByteArray &name,
    QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
    QByteArray &conditionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderresourcemergecontext.html

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    conditionType : QSSGRenderShaderMetadata.Uniform.Condition
      Passed on as its number. May be left out, as in Qt: it is then
      QSSGRenderShaderMetadata.Uniform.Condition.NULL.

    conditionName : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QSSGShaderResourceMergeContext::registerSampler(const QByteArray
    #      &type, const QByteArray &name,
    #      QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
    #      QByteArray &conditionName)
    if conditionName is None:
      from ..QtCore import QByteArray
      conditionName = QByteArray()
    self.uglySide.call(
        'ritual_ZN30QSSGShaderResourceMergeContext15registerSamplerERK10QBy'
        'teArrayS2_N24QSSGRenderShaderMetadata7Uniform9ConditionES2_',
        self._valueOf(type), self._valueOf(name), conditionType.value,
        self._valueOf(conditionName),
    )

  @overload(QByteArray, QByteArray, QByteArray, QByteArray)
  @overload(
      QByteArray, QByteArray, QByteArray, QByteArray,
      QSSGRenderShaderMetadata.Uniform.Condition,
  )
  @overload(
      QByteArray, QByteArray, QByteArray, QByteArray,
      QSSGRenderShaderMetadata.Uniform.Condition, QByteArray,
  )
  def registerImage(
      self,
      type: QByteArray,
      name: QByteArray,
      imgtype: QByteArray,
      qualifiers: QByteArray,
      conditionType: QSSGRenderShaderMetadata.Uniform.Condition = (
          QSSGRenderShaderMetadata.Uniform.Condition.NULL),
      conditionName: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void QSSGShaderResourceMergeContext::registerImage(const
    QByteArray &type, const QByteArray &name, const QByteArray &imgtype,
    const QByteArray &qualifiers,
    QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
    QByteArray &conditionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderresourcemergecontext.html#registerImage

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    imgtype : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    qualifiers : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    conditionType : QSSGRenderShaderMetadata.Uniform.Condition
      Passed on as its number. May be left out, as in Qt: it is then
      QSSGRenderShaderMetadata.Uniform.Condition.NULL.

    conditionName : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QSSGShaderResourceMergeContext::registerImage(const QByteArray
    #      &type, const QByteArray &name, const QByteArray &imgtype, const
    #      QByteArray &qualifiers,
    #      QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
    #      QByteArray &conditionName)
    if conditionName is None:
      from ..QtCore import QByteArray
      conditionName = QByteArray()
    self.uglySide.call(
        'ritual_ZN30QSSGShaderResourceMergeContext13registerImageERK10QByte'
        'ArrayS2_S2_S2_N24QSSGRenderShaderMetadata7Uniform9ConditionES2_',
        self._valueOf(type), self._valueOf(name), self._valueOf(imgtype),
        self._valueOf(qualifiers), conditionType.value,
        self._valueOf(conditionName),
    )

  @overload(QByteArray, QByteArray)
  @overload(
      QByteArray, QByteArray, QSSGRenderShaderMetadata.Uniform.Condition,
  )
  @overload(
      QByteArray, QByteArray, QSSGRenderShaderMetadata.Uniform.Condition,
      QByteArray,
  )
  def registerUniformMember(
      self,
      type: QByteArray,
      name: QByteArray,
      conditionType: QSSGRenderShaderMetadata.Uniform.Condition = (
          QSSGRenderShaderMetadata.Uniform.Condition.NULL),
      conditionName: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QSSGShaderResourceMergeContext::registerUniformMember(const QByteArray
    &type, const QByteArray &name,
    QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
    QByteArray &conditionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderresourcemergecontext.html

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    conditionType : QSSGRenderShaderMetadata.Uniform.Condition
      Passed on as its number. May be left out, as in Qt: it is then
      QSSGRenderShaderMetadata.Uniform.Condition.NULL.

    conditionName : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QSSGShaderResourceMergeContext::registerUniformMember(const
    #      QByteArray &type, const QByteArray &name,
    #      QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
    #      QByteArray &conditionName)
    if conditionName is None:
      from ..QtCore import QByteArray
      conditionName = QByteArray()
    self.uglySide.call(
        'ritual_ZN30QSSGShaderResourceMergeContext21registerUniformMemberER'
        'K10QByteArrayS2_N24QSSGRenderShaderMetadata7Uniform9ConditionES2_',
        self._valueOf(type), self._valueOf(name), conditionType.value,
        self._valueOf(conditionName),
    )

  @staticmethod
  def rearrangeResources(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderResourceMergeContext::rearrangeResources()': leans
    on 'QSSGShaderResourceMergeContext::s_additionalBuffers', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSSGShaderResourceMergeContext.rearrangeResources' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderResourceMergeContext::rearrangeResources()': leans on "
        "'QSSGShaderResourceMergeContext::s_additionalBuffers', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def registerInput(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderResourceMergeContext::registerInput(QSSGShaderGeneratorStage
    stage, const QByteArray &type, const QByteArray &name, bool flat)': names
    the enum 'QSSGShaderGeneratorStage', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGShaderResourceMergeContext.registerInput' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderResourceMergeContext::registerInput(QSSGShaderGeneratorSt"
        "age stage, const QByteArray &type, const QByteArray &name, bool "
        "flat)': names the enum 'QSSGShaderGeneratorStage', whose class "
        "cannot be named here.")

  @staticmethod
  def registerOutput(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderResourceMergeContext::registerOutput(QSSGShaderGeneratorStage
    stage, const QByteArray &type, const QByteArray &name, bool flat)': names
    the enum 'QSSGShaderGeneratorStage', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGShaderResourceMergeContext.registerOutput' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderResourceMergeContext::registerOutput(QSSGShaderGeneratorS"
        "tage stage, const QByteArray &type, const QByteArray &name, bool "
        "flat)': names the enum 'QSSGShaderGeneratorStage', whose class "
        "cannot be named here.")

  @staticmethod
  def setAdditionalBufferAmount(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderResourceMergeContext::setAdditionalBufferAmount(int
    amount)': leans on 'QSSGShaderResourceMergeContext::s_additionalBuffers',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QSSGShaderResourceMergeContext.setAdditionalBufferAmount' has no "
        "cute function yet. Qt's 'void "
        "QSSGShaderResourceMergeContext::setAdditionalBufferAmount(int "
        "amount)': leans on "
        "'QSSGShaderResourceMergeContext::s_additionalBuffers', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
