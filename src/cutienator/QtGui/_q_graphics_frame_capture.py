"""
QGraphicsFrameCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgraphicsframecapture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsFrameCapture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhi
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsFrameCapture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsFrameCapture: a plain Python object standing
  in front of one C++ QGraphicsFrameCapture.

  What exists
  -----------

  Every function of Qt's QGraphicsFrameCapture that has a ritual and that
  Python can call so far, 12 names in all: 'setRhi', 'startCaptureFrame',
  'endCaptureFrame', 'capturePath', 'setCapturePath', 'capturePrefix',
  'setCapturePrefix', 'capturedFileName', 'capturedFilesNames', 'isLoaded',
  'isCapturing', 'openCapture'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsFrameCapture::~QGraphicsFrameCapture()': the destructor:
    Python never removes a C++ QGraphicsFrameCapture.

  What to expect
  --------------

  - The C++ QGraphicsFrameCapture is created at the first use, not by
    'QGraphicsFrameCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsFrameCapture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsFrameCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def capturePath(self) -> str:
    """
    Calls Qt's 'QString QGraphicsFrameCapture::capturePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#capturePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsFrameCapture::capturePath() const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsFrameCapture11capturePathEv',
    )

  def capturePrefix(self) -> str:
    """
    Calls Qt's 'QString QGraphicsFrameCapture::capturePrefix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#capturePrefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsFrameCapture::capturePrefix() const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsFrameCapture13capturePrefixEv',
    )

  def isLoaded(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsFrameCapture::isLoaded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#isLoaded
    """
    #  bool QGraphicsFrameCapture::isLoaded() const
    return self.uglySide.call('ritual_ZNK21QGraphicsFrameCapture8isLoadedEv')

  def isCapturing(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsFrameCapture::isCapturing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#isCapturing
    """
    #  bool QGraphicsFrameCapture::isCapturing() const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsFrameCapture11isCapturingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhi)
  @overload(NoneType)
  def setRhi(self, rhi: Optional[QRhi]) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapture::setRhi(QRhi *rhi)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsframecapture.html#setRhi

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsFrameCapture::setRhi(QRhi *rhi)
    self.uglySide.call(
        'ritual_ZN21QGraphicsFrameCapture6setRhiEP4QRhi',
        self._addressOf(rhi),
    )

  @overload(str)
  def setCapturePath(self, path: str) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapture::setCapturePath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#setCapturePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsFrameCapture::setCapturePath(const QString &path)
    self.uglySide.call(
        'ritual_ZN21QGraphicsFrameCapture14setCapturePathERK7QString', path,
    )

  @overload(str)
  def setCapturePrefix(self, prefix: str) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapture::setCapturePrefix(const QString
    &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#setCapturePrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsFrameCapture::setCapturePrefix(const QString &prefix)
    self.uglySide.call(
        'ritual_ZN21QGraphicsFrameCapture16setCapturePrefixERK7QString',
        prefix,
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
    'QGraphicsFrameCapture::QGraphicsFrameCapture()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#QGraphicsFrameCapture
    """
    #  QGraphicsFrameCapture::QGraphicsFrameCapture()
    self._noteCreation(QGraphicsFrameCapture, lambda: Rituals.call(
        'ritual_ZN21QGraphicsFrameCaptureC1Ev',
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

  def startCaptureFrame(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapture::startCaptureFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#startCaptureFrame
    """
    #  void QGraphicsFrameCapture::startCaptureFrame()
    self.uglySide.call(
        'ritual_ZN21QGraphicsFrameCapture17startCaptureFrameEv',
    )

  def endCaptureFrame(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapture::endCaptureFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#endCaptureFrame
    """
    #  void QGraphicsFrameCapture::endCaptureFrame()
    self.uglySide.call('ritual_ZN21QGraphicsFrameCapture15endCaptureFrameEv')

  def capturedFileName(self) -> str:
    """
    Calls Qt's 'QString QGraphicsFrameCapture::capturedFileName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#capturedFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsFrameCapture::capturedFileName()
    return self.uglySide.call(
        'ritual_ZN21QGraphicsFrameCapture16capturedFileNameEv',
    )

  def capturedFilesNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QGraphicsFrameCapture::capturedFilesNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#capturedFilesNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGraphicsFrameCapture::capturedFilesNames()
    address = self.uglySide.call(
        'ritual_ZN21QGraphicsFrameCapture18capturedFilesNamesEv',
    )
    return QStringList._cuteOwning(address)

  def openCapture(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapture::openCapture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecapture.html#openCapture
    """
    #  void QGraphicsFrameCapture::openCapture() const
    self.uglySide.call('ritual_ZNK21QGraphicsFrameCapture11openCaptureEv')
