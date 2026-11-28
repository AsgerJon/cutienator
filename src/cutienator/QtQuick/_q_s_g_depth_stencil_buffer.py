"""
QSGDepthStencilBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultrendercontext_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDepthStencilBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhiRenderBuffer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiRenderBuffer = WAIT['QRhiRenderBuffer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDepthStencilBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGDepthStencilBuffer: a plain Python object standing
  in front of one C++ QSGDepthStencilBuffer.

  C++ hands a QSGDepthStencilBuffer around as a copy, so every C++
  QSGDepthStencilBuffer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSGDepthStencilBuffer yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDepthStencilBuffer::~QSGDepthStencilBuffer()': the destructor:
    Python removes its C++ QSGDepthStencilBuffer by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSGDepthStencilBuffer is created at the first use, not by
    'QSGDepthStencilBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGDepthStencilBuffer back gives a copy the ritual
    made for Python, in a new cute QSGDepthStencilBuffer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDepthStencilBuffer'

  #  Qt's '~QSGDepthStencilBuffer()'. Naming it makes this a value class:
  #  Python owns every C++ QSGDepthStencilBuffer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSGDepthStencilBufferD1Ev'

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
    Notes what was given, for Qt's
    'QSGDepthStencilBuffer::QSGDepthStencilBuffer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdepthstencilbuffer.html#QSGDepthStencilBuffer
    """
    #  QSGDepthStencilBuffer::QSGDepthStencilBuffer()
    self._noteCreation(QSGDepthStencilBuffer, lambda: Rituals.call(
        'ritual_ZN21QSGDepthStencilBufferC1Ev',
    ))

  @overload(QRhiRenderBuffer)
  @overload(NoneType)
  def __init__(self, ds: Optional[QRhiRenderBuffer]) -> None:
    """
    Notes what was given, for Qt's
    'QSGDepthStencilBuffer::QSGDepthStencilBuffer(QRhiRenderBuffer *ds)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdepthstencilbuffer.html#QSGDepthStencilBuffer

    Parameters
    ----------

    ds : Optional[QRhiRenderBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGDepthStencilBuffer::QSGDepthStencilBuffer(QRhiRenderBuffer *ds)
    self._noteCreation(QSGDepthStencilBuffer, lambda: Rituals.call(
        'ritual_ZN21QSGDepthStencilBufferC1EP16QRhiRenderBuffer',
        self._addressOf(ds),
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
