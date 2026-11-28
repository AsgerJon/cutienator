"""
QGles2CommandBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2CommandBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QRhiCommandBuffer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGles2CommandBuffer(QRhiCommandBuffer):
  """
  The cute side of Qt's QGles2CommandBuffer: a plain Python object standing
  in front of one C++ QGles2CommandBuffer.

  It is built on the cute 'QRhiCommandBuffer', as Qt's QGles2CommandBuffer is
  built on Qt's QRhiCommandBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2CommandBuffer that has a ritual and that
  Python can call so far, 4 names in all: 'destroy', 'resetCommands',
  'resetState', 'resetCachedState'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2CommandBuffer::~QGles2CommandBuffer()': the destructor:
    Python never removes a C++ QGles2CommandBuffer.
  - Qt's 'const void *QGles2CommandBuffer::retainData(const QByteArray
    &data)': gives 'void', which has no cute class yet.
  - Qt's 'const uchar *QGles2CommandBuffer::retainBufferData(const
    QRhiBufferData &data)': gives 'unsigned char', which has no cute class
    yet.
  - Qt's 'const void *QGles2CommandBuffer::retainImage(const QImage &image)':
    gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QGles2CommandBuffer is created at the first use, not by
    'QGles2CommandBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2CommandBuffer.
  - Each name of Qt's QGles2CommandBuffer that has no cute function yet,
    'retainBufferData', 'retainData', 'retainImage', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGles2CommandBuffer, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class PassType(CuteNum):
    """
    The enum 'QGles2CommandBuffer::PassType' of Qt, with the 3 names Qt gives
    in it.
    """

    NoPass = Kee[int](0)
    RenderPass = Kee[int](1)
    ComputePass = Kee[int](2)

  #  The classes Qt writes inside QGles2CommandBuffer, each a class in here
  #  as in C++.

  class Command(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGles2CommandBuffer::Command: a plain Python object
    standing in front of one C++ QGles2CommandBuffer::Command.

    C++ hands a QGles2CommandBuffer::Command around as a copy, so every C++
    QGles2CommandBuffer::Command behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QGles2CommandBuffer::Command yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGles2CommandBuffer::Command::~Command()': the destructor: Python
      removes its C++ QGles2CommandBuffer::Command by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QGles2CommandBuffer::Command is created at the first use, not
      by 'QGles2CommandBuffer::Command(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGles2CommandBuffer::Command back gives a copy the
      ritual made for Python, in a new cute QGles2CommandBuffer::Command.
    """

    #  The enums Qt writes inside QGles2CommandBuffer::Command, each a class
    #  in here as in C++, and the names Qt has for the combinations of its
    #  flags enums.

    class Cmd(CuteNum):
      """
      The enum 'QGles2CommandBuffer::Command::Cmd' of Qt, with the 32 names
      Qt gives in it.
      """

      BeginFrame = Kee[int](0)
      EndFrame = Kee[int](1)
      ResetFrame = Kee[int](2)
      Viewport = Kee[int](3)
      Scissor = Kee[int](4)
      BlendConstants = Kee[int](5)
      StencilRef = Kee[int](6)
      BindVertexBuffer = Kee[int](7)
      BindIndexBuffer = Kee[int](8)
      Draw = Kee[int](9)
      DrawIndexed = Kee[int](10)
      DrawIndirect = Kee[int](11)
      DrawIndexedIndirect = Kee[int](12)
      BindGraphicsPipeline = Kee[int](13)
      BindShaderResources = Kee[int](14)
      BindFramebuffer = Kee[int](15)
      Clear = Kee[int](16)
      BufferSubData = Kee[int](17)
      GetBufferSubData = Kee[int](18)
      CopyTex = Kee[int](19)
      ReadPixels = Kee[int](20)
      SubImage = Kee[int](21)
      CompressedImage = Kee[int](22)
      CompressedSubImage = Kee[int](23)
      BlitFromRenderbuffer = Kee[int](24)
      BlitFromTexture = Kee[int](25)
      GenMip = Kee[int](26)
      BindComputePipeline = Kee[int](27)
      Dispatch = Kee[int](28)
      BarriersForPass = Kee[int](29)
      Barrier = Kee[int](30)
      InvalidateFramebuffer = Kee[int](31)

    #  The classes Qt writes inside QGles2CommandBuffer::Command, each a
    #  class in here as in C++.

    class Args(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QGles2CommandBuffer::Command::Args: a plain
      Python object standing in front of one C++
      QGles2CommandBuffer::Command::Args.

      C++ hands a QGles2CommandBuffer::Command::Args around as a copy, so
      every C++ QGles2CommandBuffer::Command::Args behind a cute one is
      Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QGles2CommandBuffer::Command::Args yet. None can be
      made from Python: one comes out of a function of another class that
      gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QGles2CommandBuffer::Command::Args::~Args()': the destructor:
        Python removes its C++ QGles2CommandBuffer::Command::Args by it, and
        has no other use for it.

      What to expect
      --------------

      - The C++ QGles2CommandBuffer::Command::Args is created at the first
        use, not by 'QGles2CommandBuffer::Command::Args(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QGles2CommandBuffer::Command::Args back gives a
        copy the ritual made for Python, in a new cute
        QGles2CommandBuffer::Command::Args.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QGles2CommandBuffer::Command::Args'

      #  Qt's '~QGles2CommandBuffer::Command::Args()'. Naming it makes this a
      #  value class: Python owns every C++
      #  QGles2CommandBuffer::Command::Args behind a cute one, and removes it
      #  by this ritual.
      __delete_ritual__ = 'ritual_ZN19QGles2CommandBuffer7Command4ArgsD1Ev'

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
    __qt_class__ = 'QGles2CommandBuffer::Command'

    #  Qt's '~QGles2CommandBuffer::Command()'. Naming it makes this a value
    #  class: Python owns every C++ QGles2CommandBuffer::Command behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QGles2CommandBuffer7CommandD1Ev'

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
    The cute side of Qt's QGles2CommandBuffer::ComputePassState: a plain
    Python object standing in front of one C++
    QGles2CommandBuffer::ComputePassState.

    C++ hands a QGles2CommandBuffer::ComputePassState around as a copy, so
    every C++ QGles2CommandBuffer::ComputePassState behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QGles2CommandBuffer::ComputePassState that has a
    ritual and that Python can call so far, 1 name in all: 'reset'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGles2CommandBuffer::ComputePassState::~ComputePassState()': the
      destructor: Python removes its C++
      QGles2CommandBuffer::ComputePassState by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QGles2CommandBuffer::ComputePassState is created at the first
      use, not by 'QGles2CommandBuffer::ComputePassState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGles2CommandBuffer::ComputePassState back gives a
      copy the ritual made for Python, in a new cute
      QGles2CommandBuffer::ComputePassState.
    """

    #  The enums Qt writes inside QGles2CommandBuffer::ComputePassState, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class Access(CuteNum):
      """
      The enum 'QGles2CommandBuffer::ComputePassState::Access' of Qt, with
      the 2 names Qt gives in it.
      """

      Read = Kee[int](1)
      Write = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGles2CommandBuffer::ComputePassState'

    #  Qt's '~QGles2CommandBuffer::ComputePassState()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QGles2CommandBuffer::ComputePassState behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QGles2CommandBuffer16ComputePassStateD1Ev')

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
      Calls Qt's 'void QGles2CommandBuffer::ComputePassState::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgles2commandbuffer-computepassstate.html#reset
      """
      #  void QGles2CommandBuffer::ComputePassState::reset()
      self.uglySide.call(
          'ritual_ZN19QGles2CommandBuffer16ComputePassState5resetEv',
      )

  class GraphicsPassState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGles2CommandBuffer::GraphicsPassState: a plain
    Python object standing in front of one C++
    QGles2CommandBuffer::GraphicsPassState.

    C++ hands a QGles2CommandBuffer::GraphicsPassState around as a copy, so
    every C++ QGles2CommandBuffer::GraphicsPassState behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QGles2CommandBuffer::GraphicsPassState that has a
    ritual and that Python can call so far, 1 name in all: 'reset'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGles2CommandBuffer::GraphicsPassState::~GraphicsPassState()':
      the destructor: Python removes its C++
      QGles2CommandBuffer::GraphicsPassState by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QGles2CommandBuffer::GraphicsPassState is created at the first
      use, not by 'QGles2CommandBuffer::GraphicsPassState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGles2CommandBuffer::GraphicsPassState back gives a
      copy the ritual made for Python, in a new cute
      QGles2CommandBuffer::GraphicsPassState.
    """

    #  The classes Qt writes inside QGles2CommandBuffer::GraphicsPassState,
    #  each a class in here as in C++.

    class Blend(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's QGles2CommandBuffer::GraphicsPassState::Blend: a
      plain Python object standing in front of one C++
      QGles2CommandBuffer::GraphicsPassState::Blend.

      C++ hands a QGles2CommandBuffer::GraphicsPassState::Blend around as a
      copy, so every C++ QGles2CommandBuffer::GraphicsPassState::Blend behind
      a cute one is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QGles2CommandBuffer::GraphicsPassState::Blend yet.
      None can be made from Python: one comes out of a function of another
      class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QGles2CommandBuffer::GraphicsPassState::Blend::~Blend()': the
        destructor: Python removes its C++
        QGles2CommandBuffer::GraphicsPassState::Blend by it, and has no other
        use for it.

      What to expect
      --------------

      - The C++ QGles2CommandBuffer::GraphicsPassState::Blend is created at
        the first use, not by
        'QGles2CommandBuffer::GraphicsPassState::Blend(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QGles2CommandBuffer::GraphicsPassState::Blend
        back gives a copy the ritual made for Python, in a new cute
        QGles2CommandBuffer::GraphicsPassState::Blend.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QGles2CommandBuffer::GraphicsPassState::Blend'

      #  Qt's '~QGles2CommandBuffer::GraphicsPassState::Blend()'. Naming it
      #  makes this a value class: Python owns every C++
      #  QGles2CommandBuffer::GraphicsPassState::Blend behind a cute one, and
      #  removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN19QGles2CommandBuffer17GraphicsPassState5BlendD1Ev')

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

    class ColorMask(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QGles2CommandBuffer::GraphicsPassState::ColorMask: a plain Python
      object standing in front of one C++
      QGles2CommandBuffer::GraphicsPassState::ColorMask.

      C++ hands a QGles2CommandBuffer::GraphicsPassState::ColorMask around as
      a copy, so every C++ QGles2CommandBuffer::GraphicsPassState::ColorMask
      behind a cute one is Python's own: it is removed, by the ritual named
      in '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QGles2CommandBuffer::GraphicsPassState::ColorMask
      yet. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's
        'QGles2CommandBuffer::GraphicsPassState::ColorMask::~ColorMask()':
        the destructor: Python removes its C++
        QGles2CommandBuffer::GraphicsPassState::ColorMask by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QGles2CommandBuffer::GraphicsPassState::ColorMask is created
        at the first use, not by
        'QGles2CommandBuffer::GraphicsPassState::ColorMask(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QGles2CommandBuffer::GraphicsPassState::ColorMask
        back gives a copy the ritual made for Python, in a new cute
        QGles2CommandBuffer::GraphicsPassState::ColorMask.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QGles2CommandBuffer::GraphicsPassState::ColorMask'

      #  Qt's '~QGles2CommandBuffer::GraphicsPassState::ColorMask()'. Naming
      #  it makes this a value class: Python owns every C++
      #  QGles2CommandBuffer::GraphicsPassState::ColorMask behind a cute one,
      #  and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN19QGles2CommandBuffer17GraphicsPassState9ColorMaskD1Ev')

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

    class StencilFace(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QGles2CommandBuffer::GraphicsPassState::StencilFace: a plain Python
      object standing in front of one C++
      QGles2CommandBuffer::GraphicsPassState::StencilFace.

      C++ hands a QGles2CommandBuffer::GraphicsPassState::StencilFace around
      as a copy, so every C++
      QGles2CommandBuffer::GraphicsPassState::StencilFace behind a cute one
      is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QGles2CommandBuffer::GraphicsPassState::StencilFace
      yet. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's
        'QGles2CommandBuffer::GraphicsPassState::StencilFace::~StencilFace(
        )': the destructor: Python removes its C++
        QGles2CommandBuffer::GraphicsPassState::StencilFace by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QGles2CommandBuffer::GraphicsPassState::StencilFace is
        created at the first use, not by
        'QGles2CommandBuffer::GraphicsPassState::StencilFace(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QGles2CommandBuffer::GraphicsPassState::StencilFace back gives a copy
        the ritual made for Python, in a new cute
        QGles2CommandBuffer::GraphicsPassState::StencilFace.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QGles2CommandBuffer::GraphicsPassState::StencilFace'

      #  Qt's '~QGles2CommandBuffer::GraphicsPassState::StencilFace()'.
      #  Naming it makes this a value class: Python owns every C++
      #  QGles2CommandBuffer::GraphicsPassState::StencilFace behind a cute
      #  one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN19QGles2CommandBuffer17GraphicsPassState11StencilFaceD1Ev')

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
    __qt_class__ = 'QGles2CommandBuffer::GraphicsPassState'

    #  Qt's '~QGles2CommandBuffer::GraphicsPassState()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QGles2CommandBuffer::GraphicsPassState behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QGles2CommandBuffer17GraphicsPassStateD1Ev')

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
      Calls Qt's 'void QGles2CommandBuffer::GraphicsPassState::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgles2commandbuffer-graphicspassstate.html#reset
      """
      #  void QGles2CommandBuffer::GraphicsPassState::reset()
      self.uglySide.call(
          'ritual_ZN19QGles2CommandBuffer17GraphicsPassState5resetEv',
      )

  class TextureUnitState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGles2CommandBuffer::TextureUnitState: a plain
    Python object standing in front of one C++
    QGles2CommandBuffer::TextureUnitState.

    C++ hands a QGles2CommandBuffer::TextureUnitState around as a copy, so
    every C++ QGles2CommandBuffer::TextureUnitState behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QGles2CommandBuffer::TextureUnitState yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGles2CommandBuffer::TextureUnitState::~TextureUnitState()': the
      destructor: Python removes its C++
      QGles2CommandBuffer::TextureUnitState by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QGles2CommandBuffer::TextureUnitState is created at the first
      use, not by 'QGles2CommandBuffer::TextureUnitState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGles2CommandBuffer::TextureUnitState back gives a
      copy the ritual made for Python, in a new cute
      QGles2CommandBuffer::TextureUnitState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGles2CommandBuffer::TextureUnitState'

    #  Qt's '~QGles2CommandBuffer::TextureUnitState()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QGles2CommandBuffer::TextureUnitState behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QGles2CommandBuffer16TextureUnitStateD1Ev')

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
  __qt_class__ = 'QGles2CommandBuffer'

  #  A C++ QGles2CommandBuffer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2CommandBuffer'

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
    'QGles2CommandBuffer::QGles2CommandBuffer(QRhiImplementation *rhi)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2commandbuffer.html#QGles2CommandBuffer

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGles2CommandBuffer::QGles2CommandBuffer(QRhiImplementation *rhi)
    self._noteCreation(QGles2CommandBuffer, lambda: Rituals.call(
        'ritual_ZN19QGles2CommandBufferC1EP18QRhiImplementation',
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
    Calls Qt's 'void QGles2CommandBuffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2commandbuffer.html#destroy
    """
    #  void QGles2CommandBuffer::destroy()
    ritual = 'ritual_ZN19QGles2CommandBuffer7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGles2CommandBuffer7destroyEv'
    self.uglySide.call(ritual)

  def resetCommands(self) -> None:
    """
    Calls Qt's 'void QGles2CommandBuffer::resetCommands()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2commandbuffer.html#resetCommands
    """
    #  void QGles2CommandBuffer::resetCommands()
    self.uglySide.call('ritual_ZN19QGles2CommandBuffer13resetCommandsEv')

  def resetState(self) -> None:
    """
    Calls Qt's 'void QGles2CommandBuffer::resetState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2commandbuffer.html#resetState
    """
    #  void QGles2CommandBuffer::resetState()
    self.uglySide.call('ritual_ZN19QGles2CommandBuffer10resetStateEv')

  def resetCachedState(self) -> None:
    """
    Calls Qt's 'void QGles2CommandBuffer::resetCachedState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2commandbuffer.html#resetCachedState
    """
    #  void QGles2CommandBuffer::resetCachedState()
    self.uglySide.call('ritual_ZN19QGles2CommandBuffer16resetCachedStateEv')

  @staticmethod
  def retainBufferData(*__, **_) -> Never:
    """
    Qt's 'const uchar *QGles2CommandBuffer::retainBufferData(const
    QRhiBufferData &data)': gives 'unsigned char', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QGles2CommandBuffer.retainBufferData' has no cute function yet. "
        "Qt's 'const uchar *QGles2CommandBuffer::retainBufferData(const "
        "QRhiBufferData &data)': gives 'unsigned char', which has no cute "
        "class yet.")

  @staticmethod
  def retainData(*__, **_) -> Never:
    """
    Qt's 'const void *QGles2CommandBuffer::retainData(const QByteArray
    &data)': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGles2CommandBuffer.retainData' has no cute function yet. Qt's "
        "'const void *QGles2CommandBuffer::retainData(const QByteArray "
        "&data)': gives 'void', which has no cute class yet.")

  @staticmethod
  def retainImage(*__, **_) -> Never:
    """
    Qt's 'const void *QGles2CommandBuffer::retainImage(const QImage &image)':
    gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGles2CommandBuffer.retainImage' has no cute function yet. Qt's "
        "'const void *QGles2CommandBuffer::retainImage(const QImage "
        "&image)': gives 'void', which has no cute class yet.")
