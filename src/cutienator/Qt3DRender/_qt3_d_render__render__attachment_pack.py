"""
Qt3DRender::Render::AttachmentPack binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/attachmentpack_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::AttachmentPack to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class AttachmentPack(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::AttachmentPack: a plain Python
  object standing in front of one C++ Qt3DRender::Render::AttachmentPack.

  C++ hands a Qt3DRender::Render::AttachmentPack around as a copy, so every
  C++ Qt3DRender::Render::AttachmentPack behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::AttachmentPack that has a ritual
  and that Python can call so far, 1 name in all: 'getDrawBufferIndex'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::AttachmentPack::AttachmentPack(const
    RenderTarget *target, AttachmentManager *attachmentManager, const
    QList<QRenderTargetOutput::AttachmentPoint> &drawBuffers)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const std::vector<Attachment>
    &Qt3DRender::Render::AttachmentPack::attachments() const': gives a type
    Python has no way to take yet.
  - Qt's 'const std::vector<QRenderTargetOutput::AttachmentPoint>
    &Qt3DRender::Render::AttachmentPack::getDrawBuffers() const': gives a
    type Python has no way to take yet.
  - Qt's 'Qt3DRender::Render::AttachmentPack::~AttachmentPack()': the
    destructor: Python removes its C++ Qt3DRender::Render::AttachmentPack by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::AttachmentPack is created at the first use,
    not by 'Qt3DRender::Render::AttachmentPack(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::AttachmentPack back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::AttachmentPack.
  - Each name of Qt's Qt3DRender::Render::AttachmentPack that has no cute
    function yet, 'attachments', 'getDrawBuffers', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::AttachmentPack'

  #  Qt's '~Qt3DRender::Render::AttachmentPack()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::AttachmentPack
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render14AttachmentPackD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt3DRender.QRenderTargetOutput.AttachmentPoint)
  def getDrawBufferIndex(
      self,
      attachmentPoint: Qt3DRender.QRenderTargetOutput.AttachmentPoint,
  ) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::AttachmentPack::getDrawBufferIndex(
    QRenderTargetOutput::AttachmentPoint attachmentPoint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attachmentpack.html

    Parameters
    ----------

    attachmentPoint : Qt3DRender.QRenderTargetOutput.AttachmentPoint
      Passed on as its number.
    """
    #  int Qt3DRender::Render::AttachmentPack::getDrawBufferIndex(
    #      QRenderTargetOutput::AttachmentPoint attachmentPoint) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14AttachmentPack18getDrawBufferIndexE'
        'NS_19QRenderTargetOutput15AttachmentPointE',
        attachmentPoint.value,
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
    'Qt3DRender::Render::AttachmentPack::AttachmentPack()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-attachmentpack.html
    """
    #  Qt3DRender::Render::AttachmentPack::AttachmentPack()
    self._noteCreation(AttachmentPack, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render14AttachmentPackC1Ev',
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
  def attachments(*__, **_) -> Never:
    """
    Qt's 'const std::vector<Attachment>
    &Qt3DRender::Render::AttachmentPack::attachments() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.AttachmentPack.attachments' has no cute "
        "function yet. Qt's 'const std::vector<Attachment> "
        "&Qt3DRender::Render::AttachmentPack::attachments() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getDrawBuffers(*__, **_) -> Never:
    """
    Qt's 'const std::vector<QRenderTargetOutput::AttachmentPoint>
    &Qt3DRender::Render::AttachmentPack::getDrawBuffers() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.AttachmentPack.getDrawBuffers' has no cute "
        "function yet. Qt's 'const "
        "std::vector<QRenderTargetOutput::AttachmentPoint> "
        "&Qt3DRender::Render::AttachmentPack::getDrawBuffers() const': "
        "gives a type Python has no way to take yet.")
