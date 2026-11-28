"""
Qt3DRender::Render::Buffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/buffer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Buffer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Buffer(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Buffer: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Buffer.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Buffer is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Buffer that has a ritual and
  that Python can call so far, 10 names in all: 'cleanup',
  'syncFromFrontEnd', 'setManager', 'updateDataFromGPUToCPU', 'usage',
  'data', 'isDirty', 'access', 'unsetDirty', 'forceDataUpload'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Buffer::~Buffer()': the destructor: Python
    never removes a C++ Qt3DRender::Render::Buffer.
  - Qt's 'std::vector<Qt3DCore::QBufferUpdate>
    &Qt3DRender::Render::Buffer::pendingBufferUpdates()': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Buffer is created at the first use, not by
    'Qt3DRender::Render::Buffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Buffer.
  - Each name of Qt's Qt3DRender::Render::Buffer that has no cute function
    yet, 'pendingBufferUpdates', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Buffer'

  #  A C++ Qt3DRender::Render::Buffer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Buffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def usage(self) -> Qt3DCore.QBuffer.UsageType:
    """
    Calls Qt's 'Qt3DCore::QBuffer::UsageType
    Qt3DRender::Render::Buffer::usage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#usage

    Returns
    -------

    Qt3DCore.QBuffer.UsageType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QBuffer.UsageType(number)' gives.
    """
    #  Qt3DCore::QBuffer::UsageType Qt3DRender::Render::Buffer::usage() const
    return Qt3DCore.QBuffer.UsageType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Buffer5usageEv',
    ))

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::Render::Buffer::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-buffer.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::Render::Buffer::data() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Buffer4dataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Buffer::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#isDirty
    """
    #  bool Qt3DRender::Render::Buffer::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Buffer7isDirtyEv',
    )

  def access(self) -> Qt3DCore.QBuffer.AccessType:
    """
    Calls Qt's 'Qt3DCore::QBuffer::AccessType
    Qt3DRender::Render::Buffer::access() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#access

    Returns
    -------

    Qt3DCore.QBuffer.AccessType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QBuffer.AccessType(number)' gives.
    """
    #  Qt3DCore::QBuffer::AccessType Qt3DRender::Render::Buffer::access()
    #      const
    return Qt3DCore.QBuffer.AccessType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Buffer6accessEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.BufferManager'])
  @overload(NoneType)
  def setManager(
      self,
      manager: Optional[Qt3DRender.Render.BufferManager],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Buffer::setManager(BufferManager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#setManager

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.BufferManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Buffer::setManager(BufferManager *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Buffer10setManagerEPNS0_13BufferManag'
        'erE',
        self._addressOf(manager),
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
    Notes what was given, for Qt's 'Qt3DRender::Render::Buffer::Buffer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#Buffer
    """
    #  Qt3DRender::Render::Buffer::Buffer()
    self._noteCreation(Buffer, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render6BufferC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Buffer::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#cleanup
    """
    #  void Qt3DRender::Render::Buffer::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render6Buffer7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Buffer::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Buffer::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render6Buffer16syncFromFrontEndEPKN8Qt3DCore'
        '5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render6Buffer16syncFromFrontEndEPKN8Qt'
          '3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(QByteArray)
  def updateDataFromGPUToCPU(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Buffer::updateDataFromGPUToCPU(QByteArray data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::Buffer::updateDataFromGPUToCPU(QByteArray
    #      data)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Buffer22updateDataFromGPUToCPUE10QByt'
        'eArray',
        self._valueOf(data),
    )

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Buffer::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#unsetDirty
    """
    #  void Qt3DRender::Render::Buffer::unsetDirty()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render6Buffer10unsetDirtyEv')

  def forceDataUpload(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Buffer::forceDataUpload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-buffer.html#forceDataUpload
    """
    #  void Qt3DRender::Render::Buffer::forceDataUpload()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Buffer15forceDataUploadEv',
    )

  @staticmethod
  def pendingBufferUpdates(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QBufferUpdate>
    &Qt3DRender::Render::Buffer::pendingBufferUpdates()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Buffer.pendingBufferUpdates' has no cute "
        "function yet. Qt's 'std::vector<Qt3DCore::QBufferUpdate> "
        "&Qt3DRender::Render::Buffer::pendingBufferUpdates()': gives a type "
        "Python has no way to take yet.")
