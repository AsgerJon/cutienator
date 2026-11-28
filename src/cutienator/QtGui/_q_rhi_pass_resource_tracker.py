"""
QRhiPassResourceTracker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiPassResourceTracker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QRhiShaderResourceBinding

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRhiPassResourceTracker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiPassResourceTracker: a plain Python object
  standing in front of one C++ QRhiPassResourceTracker.

  C++ hands a QRhiPassResourceTracker around as a copy, so every C++
  QRhiPassResourceTracker behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiPassResourceTracker that has a ritual and that
  Python can call so far, 4 names in all: 'isEmpty', 'reset',
  'toPassTrackerBufferStage', 'toPassTrackerTextureStage'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QRhiPassResourceTracker::registerBuffer(QRhiBuffer *buf, int
    slot, BufferAccess *access, BufferStage *stage, const UsageState
    &state)': names 'QRhiPassResourceTracker::BufferAccess', which has no
    cute class yet.
  - Qt's 'const QVarLengthFlatMap<QRhiBuffer *, Buffer, 12>
    &QRhiPassResourceTracker::buffers() const': gives a type Python has no
    way to take yet.
  - Qt's 'const QVarLengthFlatMap<QRhiTexture *, Texture, 12>
    &QRhiPassResourceTracker::textures() const': gives a type Python has no
    way to take yet.
  - Qt's 'QRhiPassResourceTracker::~QRhiPassResourceTracker()': the
    destructor: Python removes its C++ QRhiPassResourceTracker by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QRhiPassResourceTracker is created at the first use, not by
    'QRhiPassResourceTracker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiPassResourceTracker back gives a copy the ritual
    made for Python, in a new cute QRhiPassResourceTracker.
  - Each name of Qt's QRhiPassResourceTracker that has no cute function yet,
    'buffers', 'registerBuffer', 'registerTexture', 'textures', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhiPassResourceTracker, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BufferAccess(CuteNum):
    """
    The enum 'QRhiPassResourceTracker::BufferAccess' of Qt, with the 7 names
    Qt gives in it.
    """

    BufIndirectDraw = Kee[int](0)
    BufVertexInput = Kee[int](1)
    BufIndexRead = Kee[int](2)
    BufUniformRead = Kee[int](3)
    BufStorageLoad = Kee[int](4)
    BufStorageStore = Kee[int](5)
    BufStorageLoadStore = Kee[int](6)

  class BufferStage(CuteNum):
    """
    The enum 'QRhiPassResourceTracker::BufferStage' of Qt, with the 8 names
    Qt gives in it.
    """

    BufIndirectDrawStage = Kee[int](0)
    BufVertexInputStage = Kee[int](1)
    BufVertexStage = Kee[int](2)
    BufTCStage = Kee[int](3)
    BufTEStage = Kee[int](4)
    BufFragmentStage = Kee[int](5)
    BufComputeStage = Kee[int](6)
    BufGeometryStage = Kee[int](7)

  class TextureAccess(CuteNum):
    """
    The enum 'QRhiPassResourceTracker::TextureAccess' of Qt, with the 8 names
    Qt gives in it.
    """

    TexSample = Kee[int](0)
    TexColorOutput = Kee[int](1)
    TexDepthOutput = Kee[int](2)
    TexDepthResolveOutput = Kee[int](3)
    TexStorageLoad = Kee[int](4)
    TexStorageStore = Kee[int](5)
    TexStorageLoadStore = Kee[int](6)
    TexShadingRate = Kee[int](7)

  class TextureStage(CuteNum):
    """
    The enum 'QRhiPassResourceTracker::TextureStage' of Qt, with the 8 names
    Qt gives in it.
    """

    TexVertexStage = Kee[int](0)
    TexTCStage = Kee[int](1)
    TexTEStage = Kee[int](2)
    TexFragmentStage = Kee[int](3)
    TexColorOutputStage = Kee[int](4)
    TexDepthOutputStage = Kee[int](5)
    TexComputeStage = Kee[int](6)
    TexGeometryStage = Kee[int](7)

  #  The classes Qt writes inside QRhiPassResourceTracker, each a class in
  #  here as in C++.

  class Buffer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiPassResourceTracker::Buffer: a plain Python
    object standing in front of one C++ QRhiPassResourceTracker::Buffer.

    C++ hands a QRhiPassResourceTracker::Buffer around as a copy, so every
    C++ QRhiPassResourceTracker::Buffer behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QRhiPassResourceTracker::Buffer yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiPassResourceTracker::Buffer::~Buffer()': the destructor:
      Python removes its C++ QRhiPassResourceTracker::Buffer by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QRhiPassResourceTracker::Buffer is created at the first use,
      not by 'QRhiPassResourceTracker::Buffer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiPassResourceTracker::Buffer back gives a copy
      the ritual made for Python, in a new cute
      QRhiPassResourceTracker::Buffer.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiPassResourceTracker::Buffer'

    #  Qt's '~QRhiPassResourceTracker::Buffer()'. Naming it makes this a
    #  value class: Python owns every C++ QRhiPassResourceTracker::Buffer
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QRhiPassResourceTracker6BufferD1Ev'

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

  class Texture(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiPassResourceTracker::Texture: a plain Python
    object standing in front of one C++ QRhiPassResourceTracker::Texture.

    C++ hands a QRhiPassResourceTracker::Texture around as a copy, so every
    C++ QRhiPassResourceTracker::Texture behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QRhiPassResourceTracker::Texture yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiPassResourceTracker::Texture::~Texture()': the destructor:
      Python removes its C++ QRhiPassResourceTracker::Texture by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QRhiPassResourceTracker::Texture is created at the first use,
      not by 'QRhiPassResourceTracker::Texture(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiPassResourceTracker::Texture back gives a copy
      the ritual made for Python, in a new cute
      QRhiPassResourceTracker::Texture.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiPassResourceTracker::Texture'

    #  Qt's '~QRhiPassResourceTracker::Texture()'. Naming it makes this a
    #  value class: Python owns every C++ QRhiPassResourceTracker::Texture
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QRhiPassResourceTracker7TextureD1Ev'

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

  class UsageState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiPassResourceTracker::UsageState: a plain Python
    object standing in front of one C++ QRhiPassResourceTracker::UsageState.

    C++ hands a QRhiPassResourceTracker::UsageState around as a copy, so
    every C++ QRhiPassResourceTracker::UsageState behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiPassResourceTracker::UsageState yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiPassResourceTracker::UsageState::~UsageState()': the
      destructor: Python removes its C++ QRhiPassResourceTracker::UsageState
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiPassResourceTracker::UsageState is created at the first
      use, not by 'QRhiPassResourceTracker::UsageState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiPassResourceTracker::UsageState back gives a
      copy the ritual made for Python, in a new cute
      QRhiPassResourceTracker::UsageState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiPassResourceTracker::UsageState'

    #  Qt's '~QRhiPassResourceTracker::UsageState()'. Naming it makes this a
    #  value class: Python owns every C++ QRhiPassResourceTracker::UsageState
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QRhiPassResourceTracker10UsageStateD1Ev'

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
  @overload(QRhiShaderResourceBinding.StageFlags)
  def toPassTrackerBufferStage(
      stages: QRhiShaderResourceBinding.StageFlags,
  ) -> BufferStage:
    """
    Calls Qt's 'BufferStage
    QRhiPassResourceTracker::toPassTrackerBufferStage(
    QRhiShaderResourceBinding::StageFlags stages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhipassresourcetracker.html

    Parameters
    ----------

    stages : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    Returns
    -------

    BufferStage
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BufferStage(number)'
      gives.
    """
    #  BufferStage QRhiPassResourceTracker::toPassTrackerBufferStage(
    #      QRhiShaderResourceBinding::StageFlags stages)
    return QRhiPassResourceTracker.BufferStage(Rituals.call(
        'ritual_ZN23QRhiPassResourceTracker24toPassTrackerBufferStageE6QFla'
        'gsIN25QRhiShaderResourceBinding9StageFlagEE',
        stages.value,
    ))

  @staticmethod
  @overload(QRhiShaderResourceBinding.StageFlags)
  def toPassTrackerTextureStage(
      stages: QRhiShaderResourceBinding.StageFlags,
  ) -> TextureStage:
    """
    Calls Qt's 'TextureStage
    QRhiPassResourceTracker::toPassTrackerTextureStage(
    QRhiShaderResourceBinding::StageFlags stages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhipassresourcetracker.html

    Parameters
    ----------

    stages : QRhiShaderResourceBinding.StageFlags
      Passed on as its number.

    Returns
    -------

    TextureStage
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureStage(number)'
      gives.
    """
    #  TextureStage QRhiPassResourceTracker::toPassTrackerTextureStage(
    #      QRhiShaderResourceBinding::StageFlags stages)
    return QRhiPassResourceTracker.TextureStage(Rituals.call(
        'ritual_ZN23QRhiPassResourceTracker25toPassTrackerTextureStageE6QFl'
        'agsIN25QRhiShaderResourceBinding9StageFlagEE',
        stages.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiPassResourceTracker'

  #  Qt's '~QRhiPassResourceTracker()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiPassResourceTracker behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QRhiPassResourceTrackerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QRhiPassResourceTracker::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhipassresourcetracker.html#isEmpty
    """
    #  bool QRhiPassResourceTracker::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK23QRhiPassResourceTracker7isEmptyEv',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QRhiPassResourceTracker::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhipassresourcetracker.html#reset
    """
    #  void QRhiPassResourceTracker::reset()
    self.uglySide.call('ritual_ZN23QRhiPassResourceTracker5resetEv')

  @staticmethod
  def buffers(*__, **_) -> Never:
    """
    Qt's 'const QVarLengthFlatMap<QRhiBuffer *, Buffer, 12>
    &QRhiPassResourceTracker::buffers() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QRhiPassResourceTracker.buffers' has no cute function yet. Qt's "
        "'const QVarLengthFlatMap<QRhiBuffer *, Buffer, 12> "
        "&QRhiPassResourceTracker::buffers() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def registerBuffer(*__, **_) -> Never:
    """
    Qt's 'void QRhiPassResourceTracker::registerBuffer(QRhiBuffer *buf, int
    slot, BufferAccess *access, BufferStage *stage, const UsageState
    &state)': names 'QRhiPassResourceTracker::BufferAccess', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QRhiPassResourceTracker.registerBuffer' has no cute function yet. "
        "Qt's 'void QRhiPassResourceTracker::registerBuffer(QRhiBuffer "
        "*buf, int slot, BufferAccess *access, BufferStage *stage, const "
        "UsageState &state)': names "
        "'QRhiPassResourceTracker::BufferAccess', which has no cute class "
        "yet.")

  @staticmethod
  def registerTexture(*__, **_) -> Never:
    """
    Qt's 'void QRhiPassResourceTracker::registerTexture(QRhiTexture *tex,
    TextureAccess *access, TextureStage *stage, const UsageState &state)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'earlierStage'.
    """
    raise NotImplementedError(
        "'QRhiPassResourceTracker.registerTexture' has no cute function "
        "yet. Qt's 'void "
        "QRhiPassResourceTracker::registerTexture(QRhiTexture *tex, "
        "TextureAccess *access, TextureStage *stage, const UsageState "
        "&state)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'earlierStage'.")

  @staticmethod
  def textures(*__, **_) -> Never:
    """
    Qt's 'const QVarLengthFlatMap<QRhiTexture *, Texture, 12>
    &QRhiPassResourceTracker::textures() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QRhiPassResourceTracker.textures' has no cute function yet. Qt's "
        "'const QVarLengthFlatMap<QRhiTexture *, Texture, 12> "
        "&QRhiPassResourceTracker::textures() const': gives a type Python "
        "has no way to take yet.")
