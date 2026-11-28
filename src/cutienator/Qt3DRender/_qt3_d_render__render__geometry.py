"""
Qt3DRender::Render::Geometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/geometry_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Geometry to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Geometry(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Geometry: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Geometry.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Geometry is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Geometry that has a ritual and
  that Python can call so far, 8 names in all: 'cleanup', 'syncFromFrontEnd',
  'isDirty', 'boundingPositionAttribute', 'unsetDirty', 'min', 'max',
  'updateExtent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Geometry::~Geometry()': the destructor: Python
    never removes a C++ Qt3DRender::Render::Geometry.
  - Qt's 'QList<Qt3DCore::QNodeId> Qt3DRender::Render::Geometry::attributes()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Geometry is created at the first use, not by
    'Qt3DRender::Render::Geometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Geometry.
  - Each name of Qt's Qt3DRender::Render::Geometry that has no cute function
    yet, 'attributes', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Geometry'

  #  A C++ Qt3DRender::Render::Geometry Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Geometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Geometry::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#isDirty
    """
    #  bool Qt3DRender::Render::Geometry::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Geometry7isDirtyEv',
    )

  def boundingPositionAttribute(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::Geometry::boundingPositionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DRender::Render::Geometry::boundingPositionAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Geometry25boundingPositionAttributeE'
        'v',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def min(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::Geometry::min() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#min

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::Geometry::min() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Geometry3minEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def max(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::Geometry::max() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#max

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::Geometry::max() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Geometry3maxEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

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
    'Qt3DRender::Render::Geometry::Geometry()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#Geometry
    """
    #  Qt3DRender::Render::Geometry::Geometry()
    self._noteCreation(Geometry, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render8GeometryC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::Geometry::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#cleanup
    """
    #  void Qt3DRender::Render::Geometry::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render8Geometry7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Geometry::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Geometry::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render8Geometry16syncFromFrontEndEPKN8Qt3DCo'
        're5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render8Geometry16syncFromFrontEndEPKN8'
          'Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Geometry::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#unsetDirty
    """
    #  void Qt3DRender::Render::Geometry::unsetDirty()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render8Geometry10unsetDirtyEv')

  @overload(QVector3D, QVector3D)
  def updateExtent(self, min: QVector3D, max: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Geometry::updateExtent(const
    QVector3D &min, const QVector3D &max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometry.html#updateExtent

    Parameters
    ----------

    min : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    max : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::Geometry::updateExtent(const QVector3D &min,
    #      const QVector3D &max)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render8Geometry12updateExtentERK9QVector3DS4'
        '_',
        self._valueOf(min), self._valueOf(max),
    )

  @staticmethod
  def attributes(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId> Qt3DRender::Render::Geometry::attributes()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Geometry.attributes' has no cute function yet. "
        "Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::Geometry::attributes() const': gives a type "
        "Python has no way to take yet.")
