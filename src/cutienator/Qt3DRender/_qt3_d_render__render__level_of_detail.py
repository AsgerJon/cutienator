"""
Qt3DRender::Render::LevelOfDetail binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/levelofdetail_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::LevelOfDetail to be private: it declares the
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
  from typing import Never, Optional

  from ..QtGui import QVector3D

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LevelOfDetail(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::LevelOfDetail: a plain Python
  object standing in front of one C++ Qt3DRender::Render::LevelOfDetail.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::LevelOfDetail is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::LevelOfDetail that has a ritual
  and that Python can call so far, 9 names in all: 'cleanup',
  'syncFromFrontEnd', 'camera', 'currentIndex', 'thresholdType', 'radius',
  'center', 'hasBoundingVolumeOverride', 'setCurrentIndex'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::LevelOfDetail::~LevelOfDetail()': the
    destructor: Python never removes a C++ Qt3DRender::Render::LevelOfDetail.
  - Qt's 'QList<qreal> Qt3DRender::Render::LevelOfDetail::thresholds()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::LevelOfDetail is created at the first use,
    not by 'Qt3DRender::Render::LevelOfDetail(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::LevelOfDetail.
  - Each name of Qt's Qt3DRender::Render::LevelOfDetail that has no cute
    function yet, 'thresholds', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::LevelOfDetail'

  #  A C++ Qt3DRender::Render::LevelOfDetail Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_LevelOfDetail'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def camera(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId Qt3DRender::Render::LevelOfDetail::camera()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html#camera

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::LevelOfDetail::camera() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13LevelOfDetail6cameraEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::LevelOfDetail::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html#currentIndex
    """
    #  int Qt3DRender::Render::LevelOfDetail::currentIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13LevelOfDetail12currentIndexEv',
    )

  def thresholdType(self) -> Qt3DRender.QLevelOfDetail.ThresholdType:
    """
    Calls Qt's 'QLevelOfDetail::ThresholdType
    Qt3DRender::Render::LevelOfDetail::thresholdType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html#thresholdType

    Returns
    -------

    Qt3DRender.QLevelOfDetail.ThresholdType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QLevelOfDetail.ThresholdType(number)' gives.
    """
    #  QLevelOfDetail::ThresholdType
    #      Qt3DRender::Render::LevelOfDetail::thresholdType() const
    return Qt3DRender.QLevelOfDetail.ThresholdType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13LevelOfDetail13thresholdTypeEv',
    ))

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::LevelOfDetail::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html#radius
    """
    #  float Qt3DRender::Render::LevelOfDetail::radius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13LevelOfDetail6radiusEv',
    )

  def center(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::LevelOfDetail::center() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html#center

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::LevelOfDetail::center() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13LevelOfDetail6centerEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def hasBoundingVolumeOverride(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::LevelOfDetail::hasBoundingVolumeOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html
    """
    #  bool Qt3DRender::Render::LevelOfDetail::hasBoundingVolumeOverride()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13LevelOfDetail25hasBoundingVolumeOve'
        'rrideEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentIndex(self, currentIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::LevelOfDetail::setCurrentIndex(int
    currentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  void Qt3DRender::Render::LevelOfDetail::setCurrentIndex(int
    #      currentIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13LevelOfDetail15setCurrentIndexEi',
        currentIndex,
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
    'Qt3DRender::Render::LevelOfDetail::LevelOfDetail()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html#LevelOfDetail
    """
    #  Qt3DRender::Render::LevelOfDetail::LevelOfDetail()
    self._noteCreation(LevelOfDetail, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13LevelOfDetailC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::LevelOfDetail::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html#cleanup
    """
    #  void Qt3DRender::Render::LevelOfDetail::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13LevelOfDetail7cleanupEv',
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
    Qt3DRender::Render::LevelOfDetail::syncFromFrontEnd(const Qt3DCore::QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-levelofdetail.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::LevelOfDetail::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render13LevelOfDetail16syncFromFrontEndEPKN8'
        'Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render13LevelOfDetail16syncFromFrontEn'
          'dEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def thresholds(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> Qt3DRender::Render::LevelOfDetail::thresholds()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LevelOfDetail.thresholds' has no cute function "
        "yet. Qt's 'QList<qreal> "
        "Qt3DRender::Render::LevelOfDetail::thresholds() const': gives a "
        "type Python has no way to take yet.")
