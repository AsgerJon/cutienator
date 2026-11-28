"""
QGraphicsFrameCaptureMetal binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgraphicsframecapturemetal_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsFrameCaptureMetal to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QGraphicsFrameCapturePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhi
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsFrameCaptureMetal(QGraphicsFrameCapturePrivate):
  """
  The cute side of Qt's QGraphicsFrameCaptureMetal: a plain Python object
  standing in front of one C++ QGraphicsFrameCaptureMetal.

  It is built on the cute 'QGraphicsFrameCapturePrivate', as Qt's
  QGraphicsFrameCaptureMetal is built on Qt's QGraphicsFrameCapturePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsFrameCaptureMetal that has a ritual and
  that Python can call so far, 6 names in all: 'setRhi', 'startCaptureFrame',
  'endCaptureFrame', 'initialized', 'isCapturing', 'openCapture'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QGraphicsFrameCaptureMetal is created at the first use, not by
    'QGraphicsFrameCaptureMetal(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsFrameCaptureMetal.
  - Each name of Qt's QGraphicsFrameCaptureMetal that has no cute function
    yet, '__init__', 'updateCaptureFileName', holds a function that raises
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
  __qt_class__ = 'QGraphicsFrameCaptureMetal'

  #  A C++ QGraphicsFrameCaptureMetal Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsFrameCaptureMetal'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def initialized(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsFrameCaptureMetal::initialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapturemetal.html#initialized
    """
    #  bool QGraphicsFrameCaptureMetal::initialized() const
    ritual = 'ritual_ZNK26QGraphicsFrameCaptureMetal11initializedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QGraphicsFrameCaptureMetal11initializedEv'
    return self.uglySide.call(ritual)

  def isCapturing(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsFrameCaptureMetal::isCapturing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapturemetal.html#isCapturing
    """
    #  bool QGraphicsFrameCaptureMetal::isCapturing() const
    ritual = 'ritual_ZNK26QGraphicsFrameCaptureMetal11isCapturingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QGraphicsFrameCaptureMetal11isCapturingEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhi)
  @overload(NoneType)
  def setRhi(self, rhi: Optional[QRhi]) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCaptureMetal::setRhi(QRhi *rhi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapturemetal.html#setRhi

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsFrameCaptureMetal::setRhi(QRhi *rhi)
    ritual = 'ritual_ZN26QGraphicsFrameCaptureMetal6setRhiEP4QRhi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QGraphicsFrameCaptureMetal6setRhiEP4QRhi'
    self.uglySide.call(ritual, self._addressOf(rhi))

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
    Qt's 'QGraphicsFrameCaptureMetal::QGraphicsFrameCaptureMetal()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QGraphicsFrameCaptureMetal.__init__' has no cute function yet. "
        "Qt's 'QGraphicsFrameCaptureMetal::QGraphicsFrameCaptureMetal()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

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

  def startCaptureFrame(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCaptureMetal::startCaptureFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapturemetal.html#startCaptureFrame
    """
    #  void QGraphicsFrameCaptureMetal::startCaptureFrame()
    ritual = 'ritual_ZN26QGraphicsFrameCaptureMetal17startCaptureFrameEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QGraphicsFrameCaptureMetal17startCaptureFrameEv')
    self.uglySide.call(ritual)

  def endCaptureFrame(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCaptureMetal::endCaptureFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapturemetal.html#endCaptureFrame
    """
    #  void QGraphicsFrameCaptureMetal::endCaptureFrame()
    ritual = 'ritual_ZN26QGraphicsFrameCaptureMetal15endCaptureFrameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QGraphicsFrameCaptureMetal15endCaptureFrameEv'
    self.uglySide.call(ritual)

  def openCapture(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCaptureMetal::openCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapturemetal.html#openCapture
    """
    #  void QGraphicsFrameCaptureMetal::openCapture()
    ritual = 'ritual_ZN26QGraphicsFrameCaptureMetal11openCaptureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QGraphicsFrameCaptureMetal11openCaptureEv'
    self.uglySide.call(ritual)

  @staticmethod
  def updateCaptureFileName(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsFrameCaptureMetal::updateCaptureFileName()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QGraphicsFrameCaptureMetal.updateCaptureFileName' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsFrameCaptureMetal::updateCaptureFileName()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
