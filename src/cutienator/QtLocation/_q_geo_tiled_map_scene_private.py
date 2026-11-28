"""
QGeoTiledMapScenePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTiledMapScenePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGeoTiledMapScene


class QGeoTiledMapScenePrivate(QObjectPrivate):
  """
  The cute side of Qt's QGeoTiledMapScenePrivate: a plain Python object
  standing in front of one C++ QGeoTiledMapScenePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGeoTiledMapScenePrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMapScenePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'setupCamera',
  'isTiltedOrRotated'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGeoTiledMapScene *QGeoTiledMapScenePrivate::q_func() const':
    takes in Python what 'QGeoTiledMapScene
    *QGeoTiledMapScenePrivate::q_func()' takes.
  - Qt's 'QGeoTiledMapScenePrivate::~QGeoTiledMapScenePrivate()': the
    destructor: Python never removes a C++ QGeoTiledMapScenePrivate.
  - Qt's 'void QGeoTiledMapScenePrivate::addTile(const QGeoTileSpec &spec,
    QSharedPointer<QGeoTileTexture> texture)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QGeoTiledMapScenePrivate::setVisibleTiles(const
    QSet<QGeoTileSpec> &visibleTiles)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QGeoTiledMapScenePrivate::removeTiles(const QSet<QGeoTileSpec>
    &oldTiles)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QGeoTiledMapScenePrivate::buildGeometry(const QGeoTileSpec
    &spec, QSGImageNode *imageNode, bool &overzooming)': takes a number to
    change where it is.
  - Qt's 'void QGeoTiledMapScenePrivate::updateTileBounds(const
    QSet<QGeoTileSpec> &tiles)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QGeoTiledMapScenePrivate is created at the first use, not by
    'QGeoTiledMapScenePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMapScenePrivate.
  - Each name of Qt's QGeoTiledMapScenePrivate that has no cute function yet,
    'addTile', 'buildGeometry', 'removeTiles', 'setVisibleTiles',
    'updateTileBounds', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QGeoTiledMapScenePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isTiltedOrRotated(self) -> bool:
    """
    Calls Qt's 'bool QGeoTiledMapScenePrivate::isTiltedOrRotated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapsceneprivate.html#isTiltedOrRotated
    """
    #  bool QGeoTiledMapScenePrivate::isTiltedOrRotated() const
    return self.uglySide.call(
        'ritual_ZNK24QGeoTiledMapScenePrivate17isTiltedOrRotatedEv',
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
    'QGeoTiledMapScenePrivate::QGeoTiledMapScenePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapsceneprivate.html
    """
    #  QGeoTiledMapScenePrivate::QGeoTiledMapScenePrivate()
    self._noteCreation(QGeoTiledMapScenePrivate, lambda: Rituals.call(
        'ritual_ZN24QGeoTiledMapScenePrivateC1Ev',
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

  def q_func(self) -> Optional[QGeoTiledMapScene]:
    """
    Calls Qt's 'QGeoTiledMapScene *QGeoTiledMapScenePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapsceneprivate.html#q_func

    Returns
    -------

    Optional[QGeoTiledMapScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTiledMapScene *QGeoTiledMapScenePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QGeoTiledMapScenePrivate6q_funcEv',
    )
    from . import QGeoTiledMapScene
    return QGeoTiledMapScene._cuteAt(address)

  def setupCamera(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapScenePrivate::setupCamera()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapsceneprivate.html#setupCamera
    """
    #  void QGeoTiledMapScenePrivate::setupCamera()
    self.uglySide.call('ritual_ZN24QGeoTiledMapScenePrivate11setupCameraEv')

  @staticmethod
  def addTile(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMapScenePrivate::addTile(const QGeoTileSpec &spec,
    QSharedPointer<QGeoTileTexture> texture)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScenePrivate.addTile' has no cute function yet. Qt's "
        "'void QGeoTiledMapScenePrivate::addTile(const QGeoTileSpec &spec, "
        "QSharedPointer<QGeoTileTexture> texture)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def buildGeometry(*__, **_) -> Never:
    """
    Qt's 'bool QGeoTiledMapScenePrivate::buildGeometry(const QGeoTileSpec
    &spec, QSGImageNode *imageNode, bool &overzooming)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScenePrivate.buildGeometry' has no cute function yet. "
        "Qt's 'bool QGeoTiledMapScenePrivate::buildGeometry(const "
        "QGeoTileSpec &spec, QSGImageNode *imageNode, bool &overzooming)': "
        "takes a number to change where it is.")

  @staticmethod
  def removeTiles(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMapScenePrivate::removeTiles(const QSet<QGeoTileSpec>
    &oldTiles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScenePrivate.removeTiles' has no cute function yet. "
        "Qt's 'void QGeoTiledMapScenePrivate::removeTiles(const "
        "QSet<QGeoTileSpec> &oldTiles)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setVisibleTiles(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMapScenePrivate::setVisibleTiles(const
    QSet<QGeoTileSpec> &visibleTiles)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScenePrivate.setVisibleTiles' has no cute function "
        "yet. Qt's 'void QGeoTiledMapScenePrivate::setVisibleTiles(const "
        "QSet<QGeoTileSpec> &visibleTiles)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def updateTileBounds(*__, **_) -> Never:
    """
    Qt's 'void QGeoTiledMapScenePrivate::updateTileBounds(const
    QSet<QGeoTileSpec> &tiles)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QGeoTiledMapScenePrivate.updateTileBounds' has no cute function "
        "yet. Qt's 'void QGeoTiledMapScenePrivate::updateTileBounds(const "
        "QSet<QGeoTileSpec> &tiles)': takes a type Python has no way to "
        "hand over yet.")
