"""
QSGShaderEffectNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGShaderEffectNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSGVisitableNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from . import QSGNodeVisitorEx
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGNodeVisitorEx = WAIT['QSGNodeVisitorEx']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGShaderEffectNode(QObject, QSGVisitableNode):
  """
  The cute side of Qt's QSGShaderEffectNode: a plain Python object standing
  in front of one C++ QSGShaderEffectNode.

  It is built on the cute 'QObject', as Qt's QSGShaderEffectNode is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QSGVisitableNode' as well, as Qt's QSGShaderEffectNode is built on Qt's
  QSGVisitableNode too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGShaderEffectNode that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'updateNormalizedTextureSubRect', 'syncMaterial', 'accept',
  'textureChanged'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGShaderEffectNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSGShaderEffectNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGShaderEffectNode::~QSGShaderEffectNode()': the destructor:
    Python never removes a C++ QSGShaderEffectNode.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGShaderEffectNode is created at the first use, not by
    'QSGShaderEffectNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGShaderEffectNode.
  - Qt tells when it has removed the C++ QSGShaderEffectNode. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSGShaderEffectNode, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CullMode(CuteNum):
    """
    The enum 'QSGShaderEffectNode::CullMode' of Qt, with the 3 names Qt gives
    in it.
    """

    NoCulling = Kee[int](0)
    BackFaceCulling = Kee[int](1)
    FrontFaceCulling = Kee[int](2)

  class DirtyShaderFlag(CuteFlags):
    """
    The flags enum 'QSGShaderEffectNode::DirtyShaderFlag' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QSGShaderEffectNode::DirtyShaderFlags'.
    """

    DirtyShaders = 0x1
    DirtyShaderConstant = 0x2
    DirtyShaderTexture = 0x4
    DirtyShaderGeometry = 0x8
    DirtyShaderMesh = 0x10
    DirtyShaderAll = 0xff

  DirtyShaderFlags = DirtyShaderFlag

  #  The classes Qt writes inside QSGShaderEffectNode, each a class in here
  #  as in C++.

  class ShaderData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGShaderEffectNode::ShaderData: a plain Python
    object standing in front of one C++ QSGShaderEffectNode::ShaderData.

    C++ hands a QSGShaderEffectNode::ShaderData around as a copy, so every
    C++ QSGShaderEffectNode::ShaderData behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSGShaderEffectNode::ShaderData yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGShaderEffectNode::ShaderData::~ShaderData()': the destructor:
      Python removes its C++ QSGShaderEffectNode::ShaderData by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QSGShaderEffectNode::ShaderData is created at the first use,
      not by 'QSGShaderEffectNode::ShaderData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGShaderEffectNode::ShaderData back gives a copy
      the ritual made for Python, in a new cute
      QSGShaderEffectNode::ShaderData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGShaderEffectNode::ShaderData'

    #  Qt's '~QSGShaderEffectNode::ShaderData()'. Naming it makes this a
    #  value class: Python owns every C++ QSGShaderEffectNode::ShaderData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QSGShaderEffectNode10ShaderDataD1Ev'

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
      'QSGShaderEffectNode::ShaderData::ShaderData()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgshadereffectnode-shaderdata.html#ShaderData
      """
      #  QSGShaderEffectNode::ShaderData::ShaderData()
      self._noteCreation(
          QSGShaderEffectNode.ShaderData, lambda: Rituals.call(
              'ritual_ZN19QSGShaderEffectNode10ShaderDataC1Ev',
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

  class SyncData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGShaderEffectNode::SyncData: a plain Python
    object standing in front of one C++ QSGShaderEffectNode::SyncData.

    C++ hands a QSGShaderEffectNode::SyncData around as a copy, so every C++
    QSGShaderEffectNode::SyncData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSGShaderEffectNode::SyncData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGShaderEffectNode::SyncData::~SyncData()': the destructor:
      Python removes its C++ QSGShaderEffectNode::SyncData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSGShaderEffectNode::SyncData is created at the first use, not
      by 'QSGShaderEffectNode::SyncData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGShaderEffectNode::SyncData back gives a copy the
      ritual made for Python, in a new cute QSGShaderEffectNode::SyncData.
    """

    #  The classes Qt writes inside QSGShaderEffectNode::SyncData, each a
    #  class in here as in C++.

    class ShaderSyncData(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QSGShaderEffectNode::SyncData::ShaderSyncData: a
      plain Python object standing in front of one C++
      QSGShaderEffectNode::SyncData::ShaderSyncData.

      C++ hands a QSGShaderEffectNode::SyncData::ShaderSyncData around as a
      copy, so every C++ QSGShaderEffectNode::SyncData::ShaderSyncData behind
      a cute one is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QSGShaderEffectNode::SyncData::ShaderSyncData yet.
      None can be made from Python: one comes out of a function of another
      class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's
        'QSGShaderEffectNode::SyncData::ShaderSyncData::~ShaderSyncData()':
        the destructor: Python removes its C++
        QSGShaderEffectNode::SyncData::ShaderSyncData by it, and has no other
        use for it.

      What to expect
      --------------

      - The C++ QSGShaderEffectNode::SyncData::ShaderSyncData is created at
        the first use, not by
        'QSGShaderEffectNode::SyncData::ShaderSyncData(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QSGShaderEffectNode::SyncData::ShaderSyncData
        back gives a copy the ritual made for Python, in a new cute
        QSGShaderEffectNode::SyncData::ShaderSyncData.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QSGShaderEffectNode::SyncData::ShaderSyncData'

      #  Qt's '~QSGShaderEffectNode::SyncData::ShaderSyncData()'. Naming it
      #  makes this a value class: Python owns every C++
      #  QSGShaderEffectNode::SyncData::ShaderSyncData behind a cute one, and
      #  removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN19QSGShaderEffectNode8SyncData14ShaderSyncDataD1Ev')

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
    __qt_class__ = 'QSGShaderEffectNode::SyncData'

    #  Qt's '~QSGShaderEffectNode::SyncData()'. Naming it makes this a value
    #  class: Python owns every C++ QSGShaderEffectNode::SyncData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QSGShaderEffectNode8SyncDataD1Ev'

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

  class VariableData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGShaderEffectNode::VariableData: a plain Python
    object standing in front of one C++ QSGShaderEffectNode::VariableData.

    C++ hands a QSGShaderEffectNode::VariableData around as a copy, so every
    C++ QSGShaderEffectNode::VariableData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSGShaderEffectNode::VariableData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGShaderEffectNode::VariableData::~VariableData()': the
      destructor: Python removes its C++ QSGShaderEffectNode::VariableData by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSGShaderEffectNode::VariableData is created at the first use,
      not by 'QSGShaderEffectNode::VariableData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGShaderEffectNode::VariableData back gives a copy
      the ritual made for Python, in a new cute
      QSGShaderEffectNode::VariableData.
    """

    #  The enums Qt writes inside QSGShaderEffectNode::VariableData, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class SpecialType(CuteNum):
      """
      The enum 'QSGShaderEffectNode::VariableData::SpecialType' of Qt, with
      the 6 names Qt gives in it.
      """

      NULL = Kee[int](0)
      Unused = Kee[int](1)
      Source = Kee[int](2)
      SubRect = Kee[int](3)
      Opacity = Kee[int](4)
      Matrix = Kee[int](5)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGShaderEffectNode::VariableData'

    #  Qt's '~QSGShaderEffectNode::VariableData()'. Naming it makes this a
    #  value class: Python owns every C++ QSGShaderEffectNode::VariableData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QSGShaderEffectNode12VariableDataD1Ev'

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
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QSGShaderEffectNode::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgshadereffectnode.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSGShaderEffectNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QSGShaderEffectNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGShaderEffectNode'

  #  Qt's QSGShaderEffectNode is built on more than one class. The part of a
  #  C++ QSGShaderEffectNode that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGVisitableNode': 'ritual_cast_QSGShaderEffectNode_QSGVisitableNode',
  }

  #  A C++ QSGShaderEffectNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGShaderEffectNode'

  #  The functions Qt calls itself that QSGShaderEffectNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateNormalizedTextureSubRect': (
          ('_ZN19QSGShaderEffectNode30updateNormalizedTextureSubRectEb',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('bool', 'number', ''),
           )),
      ),
      'syncMaterial': (
          ('_ZN19QSGShaderEffectNode12syncMaterialEPNS_8SyncDataE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuick:QSGShaderEffectNode.SyncData'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGShaderEffectNode::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgshadereffectnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGShaderEffectNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGShaderEffectNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(bool)
  def updateNormalizedTextureSubRect(
      self,
      supportsAtlasTextures: bool,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF
    QSGShaderEffectNode::updateNormalizedTextureSubRect(bool
    supportsAtlasTextures)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgshadereffectnode.html

    Parameters
    ----------

    supportsAtlasTextures : bool
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGShaderEffectNode::updateNormalizedTextureSubRect(bool
    #      supportsAtlasTextures)
    address = self.uglySide.call(
        'ritual_ZN19QSGShaderEffectNode30updateNormalizedTextureSubRectEb',
        supportsAtlasTextures,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(SyncData)
  @overload(NoneType)
  def syncMaterial(self, syncData: Optional[SyncData]) -> None:
    """
    Calls Qt's 'void QSGShaderEffectNode::syncMaterial(SyncData *syncData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgshadereffectnode.html#syncMaterial

    Parameters
    ----------

    syncData : Optional[SyncData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGShaderEffectNode::syncMaterial(SyncData *syncData)
    self.uglySide.call(
        'ritual_ZN19QSGShaderEffectNode12syncMaterialEPNS_8SyncDataE',
        self._addressOf(syncData),
    )

  @overload(QSGNodeVisitorEx)
  @overload(NoneType)
  def accept(self, visitor: Optional[QSGNodeVisitorEx]) -> None:
    """
    Calls Qt's 'void QSGShaderEffectNode::accept(QSGNodeVisitorEx *visitor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgshadereffectnode.html#accept

    Parameters
    ----------

    visitor : Optional[QSGNodeVisitorEx]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGShaderEffectNode::accept(QSGNodeVisitorEx *visitor)
    ritual = 'ritual_ZN19QSGShaderEffectNode6acceptEP16QSGNodeVisitorEx'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGShaderEffectNode6acceptEP16QSGNodeVisitorEx')
    self.uglySide.call(ritual, self._addressOf(visitor))

  def textureChanged(self) -> None:
    """
    Calls Qt's 'void QSGShaderEffectNode::textureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgshadereffectnode.html#textureChanged
    """
    #  void QSGShaderEffectNode::textureChanged()
    self.uglySide.call('ritual_ZN19QSGShaderEffectNode14textureChangedEv')
