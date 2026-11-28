"""
Qt3DRender::Render::RenderCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/rendercapture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::RenderCapture to be private: it declares the
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

  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderCapture(Qt3DRender.Render.FrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::Render::RenderCapture: a plain Python
  object standing in front of one C++ Qt3DRender::Render::RenderCapture.

  It is built on the cute 'Qt3DRender::Render::FrameGraphNode', as Qt's
  Qt3DRender::Render::RenderCapture is built on Qt's
  Qt3DRender::Render::FrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderCapture that has a ritual
  and that Python can call so far, 6 names in all: 'requestCapture',
  'wasCaptureRequested', 'takeCaptureRequest', 'addRenderCapture',
  'syncFromFrontEnd', 'syncRenderCapturesToFrontend'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderCapture is created at the first use,
    not by 'Qt3DRender::Render::RenderCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RenderCapture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def wasCaptureRequested(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::RenderCapture::wasCaptureRequested()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendercapture.html
    """
    #  bool Qt3DRender::Render::RenderCapture::wasCaptureRequested() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13RenderCapture19wasCaptureRequestedE'
        'v',
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
    'Qt3DRender::Render::RenderCapture::RenderCapture()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendercapture.html#RenderCapture
    """
    #  Qt3DRender::Render::RenderCapture::RenderCapture()
    self._noteCreation(RenderCapture, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13RenderCaptureC1Ev',
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

  @overload(WAIT['Qt3DRender.QRenderCaptureRequest'])
  def requestCapture(
      self,
      request: Qt3DRender.QRenderCaptureRequest,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RenderCapture::requestCapture(const
    QRenderCaptureRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendercapture.html

    Parameters
    ----------

    request : Qt3DRender.QRenderCaptureRequest
      Passed on as a value: Qt reads the C++
      Qt3DRender::QRenderCaptureRequest, which stays Python's own.
    """
    #  void Qt3DRender::Render::RenderCapture::requestCapture(const
    #      QRenderCaptureRequest &request)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13RenderCapture14requestCaptureERKNS_2'
        '1QRenderCaptureRequestE',
        self._valueOf(request),
    )

  def takeCaptureRequest(self) -> Qt3DRender.QRenderCaptureRequest:
    """
    Calls Qt's 'QRenderCaptureRequest
    Qt3DRender::Render::RenderCapture::takeCaptureRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendercapture.html

    Returns
    -------

    Qt3DRender.QRenderCaptureRequest
      A new cute Qt3DRender::QRenderCaptureRequest around the copy Qt gave
      back. Python owns it.
    """
    #  QRenderCaptureRequest
    #      Qt3DRender::Render::RenderCapture::takeCaptureRequest()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13RenderCapture18takeCaptureRequestEv',
    )
    return Qt3DRender.QRenderCaptureRequest._cuteOwning(address)

  @overload(int, QImage)
  def addRenderCapture(self, captureId: int, image: QImage) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RenderCapture::addRenderCapture(int
    captureId, const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendercapture.html

    Parameters
    ----------

    captureId : int
      Passed on as it is.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::RenderCapture::addRenderCapture(int
    #      captureId, const QImage &image)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13RenderCapture16addRenderCaptureEiRK6'
        'QImage',
        captureId, self._valueOf(image),
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderCapture::syncFromFrontEnd(const Qt3DCore::QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendercapture.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::RenderCapture::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render13RenderCapture16syncFromFrontEndEPKN8'
        'Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render13RenderCapture16syncFromFrontEn'
          'dEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DCore.QAspectManager'])
  @overload(NoneType)
  def syncRenderCapturesToFrontend(
      self,
      manager: Optional[Qt3DCore.QAspectManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderCapture::syncRenderCapturesToFrontend(
    Qt3DCore::QAspectManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendercapture.html

    Parameters
    ----------

    manager : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::RenderCapture::syncRenderCapturesToFrontend(
    #      Qt3DCore::QAspectManager *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13RenderCapture28syncRenderCapturesToF'
        'rontendEPN8Qt3DCore14QAspectManagerE',
        self._addressOf(manager),
    )
