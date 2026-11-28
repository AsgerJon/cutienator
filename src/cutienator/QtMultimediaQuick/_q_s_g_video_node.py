"""
QSGVideoNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideonode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGVideoNode to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtMultimedia import QVideoFrameFormat
from ..QtQuick import QSGGeometryNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSGVideoNode(QSGGeometryNode):
  """
  The cute side of Qt's QSGVideoNode: a plain Python object standing in front
  of one C++ QSGVideoNode.

  It is built on the cute 'QSGGeometryNode', as Qt's QSGVideoNode is built on
  Qt's QSGGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGVideoNode that has a ritual and that Python can
  call so far, 1 name in all: 'pixelFormat'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGVideoNode::~QSGVideoNode()': the destructor: Python never
    removes a C++ QSGVideoNode.

  What has no ritual
  ------------------

  8 of the 10 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QSGVideoNode.

  What to expect
  --------------

  - The C++ QSGVideoNode is created at the first use, not by
    'QSGVideoNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGVideoNode.
  - Each name of Qt's QSGVideoNode that has no cute function yet, '__init__',
    'setCurrentFrame', 'setHdrInfo', 'setSubtitleGeometry',
    'setSurfaceFormat', 'setTexturedRectGeometry', 'texturePool',
    'updateSubtitle', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGVideoNode'

  #  A C++ QSGVideoNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGVideoNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelFormat(self) -> QVideoFrameFormat.PixelFormat:
    """
    Calls Qt's 'QVideoFrameFormat::PixelFormat QSGVideoNode::pixelFormat()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgvideonode.html#pixelFormat

    Returns
    -------

    QVideoFrameFormat.PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QVideoFrameFormat.PixelFormat(number)' gives.
    """
    #  QVideoFrameFormat::PixelFormat QSGVideoNode::pixelFormat() const
    return QVideoFrameFormat.PixelFormat(self.uglySide.call(
        'ritual_ZNK12QSGVideoNode11pixelFormatEv',
    ))

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
    Qt's 'QSGVideoNode::QSGVideoNode(QQuickVideoOutput *parent, const
    QVideoFrameFormat &videoFormat, QRhi *rhi)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    cannot initialize a parameter of type 'QSGMaterial *' with an lvalue of
    type 'QSGVideoMaterial *'.
    """
    raise NotImplementedError(
        "'QSGVideoNode.__init__' has no cute function yet. Qt's "
        "'QSGVideoNode::QSGVideoNode(QQuickVideoOutput *parent, const "
        "QVideoFrameFormat &videoFormat, QRhi *rhi)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: cannot initialize a parameter of type 'QSGMaterial "
        "*' with an lvalue of type 'QSGVideoMaterial *'.")

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
  def setCurrentFrame(*__, **_) -> Never:
    """
    Qt's 'void QSGVideoNode::setCurrentFrame(const QVideoFrame &frame)':
    leans on 'QSGVideoNode::texturePool() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGVideoNode.setCurrentFrame' has no cute function yet. Qt's "
        "'void QSGVideoNode::setCurrentFrame(const QVideoFrame &frame)': "
        "leans on 'QSGVideoNode::texturePool() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setHdrInfo(*__, **_) -> Never:
    """
    Qt's 'void QSGVideoNode::setHdrInfo(const QRhiSwapChainHdrInfo
    &hdrInfo)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QSGVideoMaterial'.
    """
    raise NotImplementedError(
        "'QSGVideoNode.setHdrInfo' has no cute function yet. Qt's 'void "
        "QSGVideoNode::setHdrInfo(const QRhiSwapChainHdrInfo &hdrInfo)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QSGVideoMaterial'.")

  @staticmethod
  def setSubtitleGeometry(*__, **_) -> Never:
    """
    Qt's 'void QSGVideoNode::setSubtitleGeometry()': leans on
    'QSGVideoNode::texturePool() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGVideoNode.setSubtitleGeometry' has no cute function yet. Qt's "
        "'void QSGVideoNode::setSubtitleGeometry()': leans on "
        "'QSGVideoNode::texturePool() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSurfaceFormat(*__, **_) -> Never:
    """
    Qt's 'void QSGVideoNode::setSurfaceFormat(const QRhiSwapChain::Format
    surfaceFormat)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QSGVideoMaterial'.
    """
    raise NotImplementedError(
        "'QSGVideoNode.setSurfaceFormat' has no cute function yet. Qt's "
        "'void QSGVideoNode::setSurfaceFormat(const QRhiSwapChain::Format "
        "surfaceFormat)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QSGVideoMaterial'.")

  @staticmethod
  def setTexturedRectGeometry(*__, **_) -> Never:
    """
    Qt's 'void QSGVideoNode::setTexturedRectGeometry(const QRectF
    &boundingRect, const QRectF &textureRect, VideoTransformation
    videoOutputTransformation)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qSetGeom'.
    """
    raise NotImplementedError(
        "'QSGVideoNode.setTexturedRectGeometry' has no cute function yet. "
        "Qt's 'void QSGVideoNode::setTexturedRectGeometry(const QRectF "
        "&boundingRect, const QRectF &textureRect, VideoTransformation "
        "videoOutputTransformation)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'qSetGeom'.")

  @staticmethod
  def texturePool(*__, **_) -> Never:
    """
    Qt's 'const QVideoFrameTexturePoolPtr &QSGVideoNode::texturePool()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'QSGVideoMaterial'.
    """
    raise NotImplementedError(
        "'QSGVideoNode.texturePool' has no cute function yet. Qt's 'const "
        "QVideoFrameTexturePoolPtr &QSGVideoNode::texturePool() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QSGVideoMaterial'.")

  @staticmethod
  def updateSubtitle(*__, **_) -> Never:
    """
    Qt's 'void QSGVideoNode::updateSubtitle(const QVideoFrame &frame)': leans
    on 'QSGVideoNode::texturePool() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGVideoNode.updateSubtitle' has no cute function yet. Qt's 'void "
        "QSGVideoNode::updateSubtitle(const QVideoFrame &frame)': leans on "
        "'QSGVideoNode::texturePool() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
