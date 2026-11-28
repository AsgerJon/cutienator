"""
Qt3DRender::Render::CoordinateReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/trianglesvisitor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::CoordinateReader to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QVector4D

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CoordinateReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::CoordinateReader: a plain Python
  object standing in front of one C++ Qt3DRender::Render::CoordinateReader.

  C++ hands a Qt3DRender::Render::CoordinateReader around as a copy, so every
  C++ Qt3DRender::Render::CoordinateReader behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::CoordinateReader that has a
  ritual and that Python can call so far, 2 names in all: 'setGeometry',
  'getCoordinate'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::CoordinateReader::~CoordinateReader()': the
    destructor: Python removes its C++ Qt3DRender::Render::CoordinateReader
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::CoordinateReader is created at the first use,
    not by 'Qt3DRender::Render::CoordinateReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::CoordinateReader back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::CoordinateReader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::CoordinateReader'

  #  Qt's '~Qt3DRender::Render::CoordinateReader()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::CoordinateReader
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render16CoordinateReaderD1Ev'

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

  @overload(WAIT['Qt3DRender.Render.GeometryRenderer'], str)
  @overload(NoneType, str)
  def setGeometry(
      self,
      renderer: Optional[Qt3DRender.Render.GeometryRenderer],
      attributeName: str,
  ) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::CoordinateReader::setGeometry(const
    GeometryRenderer *renderer, const QString &attributeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-coordinatereader.html

    Parameters
    ----------

    renderer : Optional[Qt3DRender.Render.GeometryRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attributeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool Qt3DRender::Render::CoordinateReader::setGeometry(const
    #      GeometryRenderer *renderer, const QString &attributeName)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16CoordinateReader11setGeometryEPKNS0_'
        '16GeometryRendererERK7QString',
        self._addressOf(renderer), attributeName,
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

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def __init__(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::CoordinateReader::CoordinateReader(NodeManagers
    *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-coordinatereader.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::CoordinateReader::CoordinateReader(NodeManagers
    #      *manager)
    self._noteCreation(CoordinateReader, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render16CoordinateReaderC1EPNS0_12NodeManage'
        'rsE',
        self._addressOf(manager),
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
  def getCoordinate(self, vertexIndex: int) -> QVector4D:
    """
    Calls Qt's 'Vector4D
    Qt3DRender::Render::CoordinateReader::getCoordinate(uint vertexIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-coordinatereader.html

    Parameters
    ----------

    vertexIndex : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  Vector4D Qt3DRender::Render::CoordinateReader::getCoordinate(uint
    #      vertexIndex)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16CoordinateReader13getCoordinateEj',
        vertexIndex,
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)
