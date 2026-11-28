"""
Qt3DRender::Render::RayCaster binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/raycaster_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::RayCaster to be private: it declares the
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

  from ..QtCore import QPoint
  from ..QtGui import QVector3D

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RayCaster(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::RayCaster: a plain Python object
  standing in front of one C++ Qt3DRender::Render::RayCaster.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::RayCaster is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RayCaster that has a ritual and
  that Python can call so far, 10 names in all: 'type', 'runMode', 'origin',
  'direction', 'length', 'position', 'filterMode', 'syncFromFrontEnd',
  'cleanup', 'notifyJob'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::RayCaster::~RayCaster()': the destructor:
    Python never removes a C++ Qt3DRender::Render::RayCaster.
  - Qt's 'Qt3DCore::QNodeIdVector Qt3DRender::Render::RayCaster::layerIds()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RayCaster is created at the first use, not by
    'Qt3DRender::Render::RayCaster(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RayCaster.
  - Each name of Qt's Qt3DRender::Render::RayCaster that has no cute function
    yet, 'layerIds', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'Qt3DRender::Render::RayCaster'

  #  A C++ Qt3DRender::Render::RayCaster Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_RayCaster'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Qt3DRender.QAbstractRayCasterPrivate.RayCasterType:
    """
    Calls Qt's 'QAbstractRayCasterPrivate::RayCasterType
    Qt3DRender::Render::RayCaster::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#type

    Returns
    -------

    Qt3DRender.QAbstractRayCasterPrivate.RayCasterType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractRayCasterPrivate.RayCasterType(number)' gives.
    """
    #  QAbstractRayCasterPrivate::RayCasterType
    #      Qt3DRender::Render::RayCaster::type() const
    return Qt3DRender.QAbstractRayCasterPrivate.RayCasterType(
        self.uglySide.call('ritual_ZNK10Qt3DRender6Render9RayCaster4typeEv'))

  def runMode(self) -> Qt3DRender.QAbstractRayCaster.RunMode:
    """
    Calls Qt's 'QAbstractRayCaster::RunMode
    Qt3DRender::Render::RayCaster::runMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#runMode

    Returns
    -------

    Qt3DRender.QAbstractRayCaster.RunMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractRayCaster.RunMode(number)' gives.
    """
    #  QAbstractRayCaster::RunMode Qt3DRender::Render::RayCaster::runMode()
    #      const
    return Qt3DRender.QAbstractRayCaster.RunMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9RayCaster7runModeEv',
    ))

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::RayCaster::origin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::RayCaster::origin() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9RayCaster6originEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def direction(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::RayCaster::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#direction

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::RayCaster::direction() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9RayCaster9directionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def length(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::RayCaster::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#length
    """
    #  float Qt3DRender::Render::RayCaster::length() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9RayCaster6lengthEv',
    )

  def position(self) -> QPoint:
    """
    Calls Qt's 'QPoint Qt3DRender::Render::RayCaster::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#position

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Qt3DRender::Render::RayCaster::position() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9RayCaster8positionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def filterMode(self) -> Qt3DRender.QAbstractRayCaster.FilterMode:
    """
    Calls Qt's 'QAbstractRayCaster::FilterMode
    Qt3DRender::Render::RayCaster::filterMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#filterMode

    Returns
    -------

    Qt3DRender.QAbstractRayCaster.FilterMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractRayCaster.FilterMode(number)' gives.
    """
    #  QAbstractRayCaster::FilterMode
    #      Qt3DRender::Render::RayCaster::filterMode() const
    return Qt3DRender.QAbstractRayCaster.FilterMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9RayCaster10filterModeEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::RayCaster::RayCaster()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#RayCaster
    """
    #  Qt3DRender::Render::RayCaster::RayCaster()
    self._noteCreation(RayCaster, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render9RayCasterC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::RayCaster::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::RayCaster::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render9RayCaster16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render9RayCaster16syncFromFrontEndEPKN'
          '8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RayCaster::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#cleanup
    """
    #  void Qt3DRender::Render::RayCaster::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render9RayCaster7cleanupEv')

  def notifyJob(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RayCaster::notifyJob()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycaster.html#notifyJob
    """
    #  void Qt3DRender::Render::RayCaster::notifyJob()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render9RayCaster9notifyJobEv')

  @staticmethod
  def layerIds(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeIdVector Qt3DRender::Render::RayCaster::layerIds()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RayCaster.layerIds' has no cute function yet. "
        "Qt's 'Qt3DCore::QNodeIdVector "
        "Qt3DRender::Render::RayCaster::layerIds() const': gives a type "
        "Python has no way to take yet.")
