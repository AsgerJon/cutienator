"""
QVkCommandBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVkCommandBuffer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QRhiCommandBuffer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhiImplementation, QRhiNativeHandles
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVkCommandBuffer(QRhiCommandBuffer):
  """
  The cute side of Qt's QVkCommandBuffer: a plain Python object standing in
  front of one C++ QVkCommandBuffer.

  It is built on the cute 'QRhiCommandBuffer', as Qt's QVkCommandBuffer is
  built on Qt's QRhiCommandBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVkCommandBuffer that has a ritual and that Python
  can call so far, 6 names in all: 'destroy', 'nativeHandles', 'resetState',
  'resetPerPassState', 'resetCommands', 'resetPools'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVkCommandBuffer::~QVkCommandBuffer()': the destructor: Python
    never removes a C++ QVkCommandBuffer.

  What to expect
  --------------

  - The C++ QVkCommandBuffer is created at the first use, not by
    'QVkCommandBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVkCommandBuffer.
  """

  #  The enums Qt writes inside QVkCommandBuffer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PassType(CuteNum):
    """
    The enum 'QVkCommandBuffer::PassType' of Qt, with the 3 names Qt gives in
    it.
    """

    NoPass = Kee[int](0)
    RenderPass = Kee[int](1)
    ComputePass = Kee[int](2)

  #  The classes Qt writes inside QVkCommandBuffer, each a class in here as
  #  in C++.

  class Command(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVkCommandBuffer::Command: a plain Python object
    standing in front of one C++ QVkCommandBuffer::Command.

    C++ hands a QVkCommandBuffer::Command around as a copy, so every C++
    QVkCommandBuffer::Command behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QVkCommandBuffer::Command yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVkCommandBuffer::Command::~Command()': the destructor: Python
      removes its C++ QVkCommandBuffer::Command by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QVkCommandBuffer::Command is created at the first use, not by
      'QVkCommandBuffer::Command(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVkCommandBuffer::Command back gives a copy the
      ritual made for Python, in a new cute QVkCommandBuffer::Command.
    """

    #  The enums Qt writes inside QVkCommandBuffer::Command, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class Cmd(CuteNum):
      """
      The enum 'QVkCommandBuffer::Command::Cmd' of Qt, with the 30 names Qt
      gives in it.
      """

      CopyBuffer = Kee[int](0)
      CopyBufferToImage = Kee[int](1)
      CopyImage = Kee[int](2)
      CopyImageToBuffer = Kee[int](3)
      ImageBarrier = Kee[int](4)
      BufferBarrier = Kee[int](5)
      ImageAndBufferBarrier = Kee[int](6)
      BlitImage = Kee[int](7)
      BeginRenderPass = Kee[int](8)
      EndRenderPass = Kee[int](9)
      BindPipeline = Kee[int](10)
      BindDescriptorSet = Kee[int](11)
      BindVertexBuffer = Kee[int](12)
      BindIndexBuffer = Kee[int](13)
      SetViewport = Kee[int](14)
      SetScissor = Kee[int](15)
      SetBlendConstants = Kee[int](16)
      SetStencilRef = Kee[int](17)
      Draw = Kee[int](18)
      DrawIndexed = Kee[int](19)
      DrawIndirect = Kee[int](20)
      DrawIndexedIndirect = Kee[int](21)
      DebugMarkerBegin = Kee[int](22)
      DebugMarkerEnd = Kee[int](23)
      DebugMarkerInsert = Kee[int](24)
      TransitionPassResources = Kee[int](25)
      Dispatch = Kee[int](26)
      ExecuteSecondary = Kee[int](27)
      SetShadingRate = Kee[int](28)
      MemoryBarrier = Kee[int](29)

    #  The classes Qt writes inside QVkCommandBuffer::Command, each a class
    #  in here as in C++.

    class Args(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QVkCommandBuffer::Command::Args: a plain Python
      object standing in front of one C++ QVkCommandBuffer::Command::Args.

      C++ hands a QVkCommandBuffer::Command::Args around as a copy, so every
      C++ QVkCommandBuffer::Command::Args behind a cute one is Python's own:
      it is removed, by the ritual named in '__delete_ritual__', when the
      cute object goes.

      What exists
      -----------

      No function of Qt's QVkCommandBuffer::Command::Args yet. None can be
      made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QVkCommandBuffer::Command::Args::~Args()': the destructor:
        Python removes its C++ QVkCommandBuffer::Command::Args by it, and has
        no other use for it.

      What to expect
      --------------

      - The C++ QVkCommandBuffer::Command::Args is created at the first use,
        not by 'QVkCommandBuffer::Command::Args(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QVkCommandBuffer::Command::Args back gives a copy
        the ritual made for Python, in a new cute
        QVkCommandBuffer::Command::Args.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QVkCommandBuffer::Command::Args'

      #  Qt's '~QVkCommandBuffer::Command::Args()'. Naming it makes this a
      #  value class: Python owns every C++ QVkCommandBuffer::Command::Args
      #  behind a cute one, and removes it by this ritual.
      __delete_ritual__ = 'ritual_ZN16QVkCommandBuffer7Command4ArgsD1Ev'

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
    __qt_class__ = 'QVkCommandBuffer::Command'

    #  Qt's '~QVkCommandBuffer::Command()'. Naming it makes this a value
    #  class: Python owns every C++ QVkCommandBuffer::Command behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QVkCommandBuffer7CommandD1Ev'

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

  class ComputePassState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVkCommandBuffer::ComputePassState: a plain Python
    object standing in front of one C++ QVkCommandBuffer::ComputePassState.

    C++ hands a QVkCommandBuffer::ComputePassState around as a copy, so every
    C++ QVkCommandBuffer::ComputePassState behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QVkCommandBuffer::ComputePassState that has a
    ritual and that Python can call so far, 1 name in all: 'reset'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVkCommandBuffer::ComputePassState::~ComputePassState()': the
      destructor: Python removes its C++ QVkCommandBuffer::ComputePassState
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QVkCommandBuffer::ComputePassState is created at the first use,
      not by 'QVkCommandBuffer::ComputePassState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVkCommandBuffer::ComputePassState back gives a
      copy the ritual made for Python, in a new cute
      QVkCommandBuffer::ComputePassState.
    """

    #  The classes Qt writes inside QVkCommandBuffer::ComputePassState, each
    #  a class in here as in C++.

    class AccessFlagsAndIsNew(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew: a plain Python
      object standing in front of one C++
      QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew.

      C++ hands a QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew
      around as a copy, so every C++
      QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew behind a cute
      one is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's
      QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew yet. None can
      be made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew::
        ~AccessFlagsAndIsNew()': the destructor: Python removes its C++
        QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew by it, and
        has no other use for it.

      What to expect
      --------------

      - The C++ QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew is
        created at the first use, not by
        'QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew back gives a
        copy the ritual made for Python, in a new cute
        QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew'

      #  Qt's '~QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew()'.
      #  Naming it makes this a value class: Python owns every C++
      #  QVkCommandBuffer::ComputePassState::AccessFlagsAndIsNew behind a
      #  cute one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN16QVkCommandBuffer16ComputePassState19AccessFlagsAndIsNewD1Ev')

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
    __qt_class__ = 'QVkCommandBuffer::ComputePassState'

    #  Qt's '~QVkCommandBuffer::ComputePassState()'. Naming it makes this a
    #  value class: Python owns every C++ QVkCommandBuffer::ComputePassState
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QVkCommandBuffer16ComputePassStateD1Ev'

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

    def reset(self) -> None:
      """
      Calls Qt's 'void QVkCommandBuffer::ComputePassState::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qvkcommandbuffer-computepassstate.html#reset
      """
      #  void QVkCommandBuffer::ComputePassState::reset()
      self.uglySide.call(
          'ritual_ZN16QVkCommandBuffer16ComputePassState5resetEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVkCommandBuffer'

  #  A C++ QVkCommandBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVkCommandBuffer'

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

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QVkCommandBuffer::QVkCommandBuffer(QRhiImplementation *rhi)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkcommandbuffer.html#QVkCommandBuffer

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QVkCommandBuffer::QVkCommandBuffer(QRhiImplementation *rhi)
    self._noteCreation(QVkCommandBuffer, lambda: Rituals.call(
        'ritual_ZN16QVkCommandBufferC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QVkCommandBuffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkcommandbuffer.html#destroy
    """
    #  void QVkCommandBuffer::destroy()
    ritual = 'ritual_ZN16QVkCommandBuffer7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QVkCommandBuffer7destroyEv'
    self.uglySide.call(ritual)

  def nativeHandles(self) -> Optional[QRhiNativeHandles]:
    """
    Calls Qt's 'const QRhiNativeHandles *QVkCommandBuffer::nativeHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkcommandbuffer.html#nativeHandles

    Returns
    -------

    Optional[QRhiNativeHandles]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiNativeHandles *QVkCommandBuffer::nativeHandles()
    address = self.uglySide.call(
        'ritual_ZN16QVkCommandBuffer13nativeHandlesEv',
    )
    from . import QRhiNativeHandles
    return QRhiNativeHandles._cuteAt(address)

  def resetState(self) -> None:
    """
    Calls Qt's 'void QVkCommandBuffer::resetState()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkcommandbuffer.html#resetState
    """
    #  void QVkCommandBuffer::resetState()
    self.uglySide.call('ritual_ZN16QVkCommandBuffer10resetStateEv')

  def resetPerPassState(self) -> None:
    """
    Calls Qt's 'void QVkCommandBuffer::resetPerPassState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkcommandbuffer.html#resetPerPassState
    """
    #  void QVkCommandBuffer::resetPerPassState()
    self.uglySide.call('ritual_ZN16QVkCommandBuffer17resetPerPassStateEv')

  def resetCommands(self) -> None:
    """
    Calls Qt's 'void QVkCommandBuffer::resetCommands()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvkcommandbuffer.html#resetCommands
    """
    #  void QVkCommandBuffer::resetCommands()
    self.uglySide.call('ritual_ZN16QVkCommandBuffer13resetCommandsEv')

  def resetPools(self) -> None:
    """
    Calls Qt's 'void QVkCommandBuffer::resetPools()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkcommandbuffer.html#resetPools
    """
    #  void QVkCommandBuffer::resetPools()
    self.uglySide.call('ritual_ZN16QVkCommandBuffer10resetPoolsEv')
