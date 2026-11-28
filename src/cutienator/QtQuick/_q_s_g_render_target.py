"""
QSGRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGRenderTarget to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QPaintDevice, QRhiCommandBuffer
  from ..QtGui import QRhiRenderPassDescriptor, QRhiRenderTarget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintDevice = WAIT['QPaintDevice']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRenderTarget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGRenderTarget: a plain Python object standing in
  front of one C++ QSGRenderTarget.

  C++ hands a QSGRenderTarget around as a copy, so every C++ QSGRenderTarget
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSGRenderTarget yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGRenderTarget::~QSGRenderTarget()': the destructor: Python
    removes its C++ QSGRenderTarget by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGRenderTarget is created at the first use, not by
    'QSGRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGRenderTarget back gives a copy the ritual made for
    Python, in a new cute QSGRenderTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRenderTarget'

  #  Qt's '~QSGRenderTarget()'. Naming it makes this a value class: Python
  #  owns every C++ QSGRenderTarget behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSGRenderTargetD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSGRenderTarget::QSGRenderTarget()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendertarget.html#QSGRenderTarget
    """
    #  QSGRenderTarget::QSGRenderTarget()
    self._noteCreation(QSGRenderTarget, lambda: Rituals.call(
        'ritual_ZN15QSGRenderTargetC1Ev',
    ))

  @overload(QRhiRenderTarget, QRhiRenderPassDescriptor, QRhiCommandBuffer)
  @overload(QRhiRenderTarget, QRhiRenderPassDescriptor, NoneType)
  @overload(QRhiRenderTarget, NoneType, QRhiCommandBuffer)
  @overload(QRhiRenderTarget, NoneType, NoneType)
  @overload(NoneType, QRhiRenderPassDescriptor, QRhiCommandBuffer)
  @overload(NoneType, QRhiRenderPassDescriptor, NoneType)
  @overload(NoneType, NoneType, QRhiCommandBuffer)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      rt: Optional[QRhiRenderTarget],
      rpDesc: Optional[QRhiRenderPassDescriptor],
      cb: Optional[QRhiCommandBuffer],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSGRenderTarget::QSGRenderTarget(QRhiRenderTarget *rt,
    QRhiRenderPassDescriptor *rpDesc, QRhiCommandBuffer *cb)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendertarget.html#QSGRenderTarget

    Parameters
    ----------

    rt : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rpDesc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGRenderTarget::QSGRenderTarget(QRhiRenderTarget *rt,
    #      QRhiRenderPassDescriptor *rpDesc, QRhiCommandBuffer *cb)
    self._noteCreation(QSGRenderTarget, lambda: Rituals.call(
        'ritual_ZN15QSGRenderTargetC1EP16QRhiRenderTargetP24QRhiRenderPassD'
        'escriptorP17QRhiCommandBuffer',
        self._addressOf(rt), self._addressOf(rpDesc), self._addressOf(cb),
    ))

  @overload(QPaintDevice)
  @overload(NoneType)
  def __init__(self, paintDevice: Optional[QPaintDevice]) -> None:
    """
    Notes what was given, for Qt's
    'QSGRenderTarget::QSGRenderTarget(QPaintDevice *paintDevice)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendertarget.html#QSGRenderTarget

    Parameters
    ----------

    paintDevice : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGRenderTarget::QSGRenderTarget(QPaintDevice *paintDevice)
    self._noteCreation(QSGRenderTarget, lambda: Rituals.call(
        'ritual_ZN15QSGRenderTargetC1EP12QPaintDevice',
        self._addressOf(paintDevice, 'QPaintDevice'),
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
