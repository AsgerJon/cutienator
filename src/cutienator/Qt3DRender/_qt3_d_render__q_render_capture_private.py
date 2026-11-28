"""
Qt3DRender::QRenderCapturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrendercapture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QRenderCapturePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderCapturePrivate(Qt3DRender.QFrameGraphNodePrivate):
  """
  The cute side of Qt's Qt3DRender::QRenderCapturePrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderCapturePrivate.

  It is built on the cute 'Qt3DRender::QFrameGraphNodePrivate', as Qt's
  Qt3DRender::QRenderCapturePrivate is built on Qt's
  Qt3DRender::QFrameGraphNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderCapturePrivate that has a ritual
  and that Python can call so far, 5 names in all: 'createReply',
  'takeReply', 'setImage', 'replyDestroyed', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QRenderCapturePrivate::~QRenderCapturePrivate()': the
    destructor: Python never removes a C++ Qt3DRender::QRenderCapturePrivate.
  - Qt's 'const QRenderCapture *Qt3DRender::QRenderCapturePrivate::q_func()
    const': takes in Python what 'QRenderCapture
    *Qt3DRender::QRenderCapturePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderCapturePrivate is created at the first use,
    not by 'Qt3DRender::QRenderCapturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderCapturePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderCapturePrivate'

  #  A C++ Qt3DRender::QRenderCapturePrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderCapturePrivate'

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

  @overload(WAIT['Qt3DRender.QRenderCaptureReply'], QImage)
  @overload(NoneType, QImage)
  def setImage(
      self,
      reply: Optional[Qt3DRender.QRenderCaptureReply],
      image: QImage,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderCapturePrivate::setImage(QRenderCaptureReply *reply,
    const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercaptureprivate.html#setImage

    Parameters
    ----------

    reply : Optional[Qt3DRender.QRenderCaptureReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void Qt3DRender::QRenderCapturePrivate::setImage(QRenderCaptureReply
    #      *reply, const QImage &image)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QRenderCapturePrivate8setImageEPNS_19QRende'
        'rCaptureReplyERK6QImage',
        self._addressOf(reply), self._valueOf(image),
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
    Notes what was given, for Qt's
    'Qt3DRender::QRenderCapturePrivate::QRenderCapturePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercaptureprivate.html
    """
    #  Qt3DRender::QRenderCapturePrivate::QRenderCapturePrivate()
    self._noteCreation(QRenderCapturePrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender21QRenderCapturePrivateC1Ev',
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

  @overload(int)
  def createReply(
      self,
      captureId: int,
  ) -> Optional[Qt3DRender.QRenderCaptureReply]:
    """
    Calls Qt's 'QRenderCaptureReply
    *Qt3DRender::QRenderCapturePrivate::createReply(int captureId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercaptureprivate.html#createReply

    Parameters
    ----------

    captureId : int
      Passed on as it is.

    Returns
    -------

    Optional[Qt3DRender.QRenderCaptureReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCaptureReply
    #      *Qt3DRender::QRenderCapturePrivate::createReply(int captureId)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QRenderCapturePrivate11createReplyEi',
        captureId,
    )
    return Qt3DRender.QRenderCaptureReply._cuteAt(address)

  @overload(int)
  def takeReply(
      self,
      captureId: int,
  ) -> Optional[Qt3DRender.QRenderCaptureReply]:
    """
    Calls Qt's 'QRenderCaptureReply
    *Qt3DRender::QRenderCapturePrivate::takeReply(int captureId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercaptureprivate.html#takeReply

    Parameters
    ----------

    captureId : int
      Passed on as it is.

    Returns
    -------

    Optional[Qt3DRender.QRenderCaptureReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCaptureReply *Qt3DRender::QRenderCapturePrivate::takeReply(int
    #      captureId)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QRenderCapturePrivate9takeReplyEi',
        captureId,
    )
    return Qt3DRender.QRenderCaptureReply._cuteAt(address)

  @overload(WAIT['Qt3DRender.QRenderCaptureReply'])
  @overload(NoneType)
  def replyDestroyed(
      self,
      reply: Optional[Qt3DRender.QRenderCaptureReply],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderCapturePrivate::replyDestroyed(QRenderCaptureReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercaptureprivate.html

    Parameters
    ----------

    reply : Optional[Qt3DRender.QRenderCaptureReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderCapturePrivate::replyDestroyed(
    #      QRenderCaptureReply *reply)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QRenderCapturePrivate14replyDestroyedEPNS_1'
        '9QRenderCaptureReplyE',
        self._addressOf(reply),
    )

  def q_func(self) -> Optional[Qt3DRender.QRenderCapture]:
    """
    Calls Qt's 'QRenderCapture *Qt3DRender::QRenderCapturePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercaptureprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QRenderCapture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCapture *Qt3DRender::QRenderCapturePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QRenderCapturePrivate6q_funcEv',
    )
    return Qt3DRender.QRenderCapture._cuteAt(address)
