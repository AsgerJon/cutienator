"""
QGles2Buffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2Buffer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from . import QRhiBuffer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGles2Buffer(QRhiBuffer):
  """
  The cute side of Qt's QGles2Buffer: a plain Python object standing in front
  of one C++ QGles2Buffer.

  It is built on the cute 'QRhiBuffer', as Qt's QGles2Buffer is built on Qt's
  QRhiBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2Buffer that has a ritual and that Python can
  call so far, 4 names in all: 'destroy', 'create', 'nativeBuffer',
  'endFullDynamicBufferUpdateForCurrentFrame'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2Buffer::~QGles2Buffer()': the destructor: Python never
    removes a C++ QGles2Buffer.
  - Qt's 'char *QGles2Buffer::beginFullDynamicBufferUpdateForCurrentFrame()':
    gives 'char', which has no cute class yet.
  - Qt's 'void QGles2Buffer::fullDynamicBufferUpdateForCurrentFrame(const
    void *data, quint32 size)': names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'QRhiGles2.

  What to expect
  --------------

  - The C++ QGles2Buffer is created at the first use, not by
    'QGles2Buffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2Buffer.
  - Each name of Qt's QGles2Buffer that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QGles2Buffer, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Access(CuteNum):
    """
    The enum 'QGles2Buffer::Access' of Qt, with the 9 names Qt gives in it.
    """

    AccessNone = Kee[int](0)
    AccessVertex = Kee[int](1)
    AccessIndex = Kee[int](2)
    AccessUniform = Kee[int](3)
    AccessStorageRead = Kee[int](4)
    AccessStorageWrite = Kee[int](5)
    AccessStorageReadWrite = Kee[int](6)
    AccessUpdate = Kee[int](7)
    AccessIndirectDraw = Kee[int](8)

  #  The classes Qt writes inside QGles2Buffer, each a class in here as in
  #  C++.

  class UsageState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGles2Buffer::UsageState: a plain Python object
    standing in front of one C++ QGles2Buffer::UsageState.

    C++ hands a QGles2Buffer::UsageState around as a copy, so every C++
    QGles2Buffer::UsageState behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QGles2Buffer::UsageState yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGles2Buffer::UsageState::~UsageState()': the destructor: Python
      removes its C++ QGles2Buffer::UsageState by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QGles2Buffer::UsageState is created at the first use, not by
      'QGles2Buffer::UsageState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGles2Buffer::UsageState back gives a copy the
      ritual made for Python, in a new cute QGles2Buffer::UsageState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGles2Buffer::UsageState'

    #  Qt's '~QGles2Buffer::UsageState()'. Naming it makes this a value
    #  class: Python owns every C++ QGles2Buffer::UsageState behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QGles2Buffer10UsageStateD1Ev'

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
  __qt_class__ = 'QGles2Buffer'

  #  A C++ QGles2Buffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2Buffer'

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
    Qt's 'QGles2Buffer::QGles2Buffer(QRhiImplementation *rhi, Type type,
    UsageFlags usage, quint32 size)': leans on
    'QRhiGles2::ensureContext(QSurface*) const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGles2Buffer.__init__' has no cute function yet. Qt's "
        "'QGles2Buffer::QGles2Buffer(QRhiImplementation *rhi, Type type, "
        "UsageFlags usage, quint32 size)': leans on "
        "'QRhiGles2::ensureContext(QSurface*) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'void QGles2Buffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2buffer.html#destroy
    """
    #  void QGles2Buffer::destroy()
    ritual = 'ritual_ZN12QGles2Buffer7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGles2Buffer7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QGles2Buffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2buffer.html#create
    """
    #  bool QGles2Buffer::create()
    return self.uglySide.call('ritual_ZN12QGles2Buffer6createEv')

  def nativeBuffer(self) -> QRhiBuffer.NativeBuffer:
    """
    Calls Qt's 'QRhiBuffer::NativeBuffer QGles2Buffer::nativeBuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2buffer.html#nativeBuffer

    Returns
    -------

    QRhiBuffer.NativeBuffer
      A new cute QRhiBuffer::NativeBuffer around the copy Qt gave back.
      Python owns it.
    """
    #  QRhiBuffer::NativeBuffer QGles2Buffer::nativeBuffer()
    ritual = 'ritual_ZN12QGles2Buffer12nativeBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QGles2Buffer12nativeBufferEv'
    address = self.uglySide.call(ritual)
    return QRhiBuffer.NativeBuffer._cuteOwning(address)

  def endFullDynamicBufferUpdateForCurrentFrame(self) -> None:
    """
    Calls Qt's 'void
    QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2buffer.html
    """
    #  void QGles2Buffer::endFullDynamicBufferUpdateForCurrentFrame()
    ritual = (
        'ritual_ZN12QGles2Buffer41endFullDynamicBufferUpdateForCurrentFrame'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QGles2Buffer41endFullDynamicBufferUpdateForCurren'
          'tFrameEv')
    self.uglySide.call(ritual)
