"""
Qt3DRender::Render::ClearBuffers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/clearbuffers_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::ClearBuffers to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor, QVector4D

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ClearBuffers(Qt3DRender.Render.FrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::Render::ClearBuffers: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ClearBuffers.

  It is built on the cute 'Qt3DRender::Render::FrameGraphNode', as Qt's
  Qt3DRender::Render::ClearBuffers is built on Qt's
  Qt3DRender::Render::FrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ClearBuffers that has a ritual
  and that Python can call so far, 8 names in all: 'type', 'clearDepthValue',
  'clearStencilValue', 'bufferId', 'clearColor', 'clearColorAsColor',
  'clearsAllColorBuffers', 'syncFromFrontEnd'. It can be made from Python, in
  1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ClearBuffers is created at the first use, not
    by 'Qt3DRender::Render::ClearBuffers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::ClearBuffers.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ClearBuffers'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Qt3DRender.QClearBuffers.BufferType:
    """
    Calls Qt's 'QClearBuffers::BufferType
    Qt3DRender::Render::ClearBuffers::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html#type

    Returns
    -------

    Qt3DRender.QClearBuffers.BufferType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QClearBuffers.BufferType(number)' gives.
    """
    #  QClearBuffers::BufferType Qt3DRender::Render::ClearBuffers::type()
    #      const
    return Qt3DRender.QClearBuffers.BufferType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ClearBuffers4typeEv',
    ))

  def clearDepthValue(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::ClearBuffers::clearDepthValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html
    """
    #  float Qt3DRender::Render::ClearBuffers::clearDepthValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ClearBuffers15clearDepthValueEv',
    )

  def clearStencilValue(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::ClearBuffers::clearStencilValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html
    """
    #  int Qt3DRender::Render::ClearBuffers::clearStencilValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ClearBuffers17clearStencilValueEv',
    )

  def bufferId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::ClearBuffers::bufferId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html#bufferId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::ClearBuffers::bufferId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ClearBuffers8bufferIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def clearColor(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D Qt3DRender::Render::ClearBuffers::clearColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html#clearColor

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Qt3DRender::Render::ClearBuffers::clearColor() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ClearBuffers10clearColorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def clearColorAsColor(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DRender::Render::ClearBuffers::clearColorAsColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DRender::Render::ClearBuffers::clearColorAsColor() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ClearBuffers17clearColorAsColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def clearsAllColorBuffers(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::ClearBuffers::clearsAllColorBuffers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html
    """
    #  bool Qt3DRender::Render::ClearBuffers::clearsAllColorBuffers() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ClearBuffers21clearsAllColorBuffers'
        'Ev',
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
    'Qt3DRender::Render::ClearBuffers::ClearBuffers()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html#ClearBuffers
    """
    #  Qt3DRender::Render::ClearBuffers::ClearBuffers()
    self._noteCreation(ClearBuffers, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12ClearBuffersC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ClearBuffers::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-clearbuffers.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ClearBuffers::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render12ClearBuffers16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render12ClearBuffers16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
