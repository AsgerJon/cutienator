"""
QGeoTileRequestManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotilerequestmanager_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoTileRequestManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGeoTileSpec, QGeoTiledMap, QGeoTiledMappingManagerEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoTileSpec = WAIT['QGeoTileSpec']
  QGeoTiledMap = WAIT['QGeoTiledMap']
  QGeoTiledMappingManagerEngine = WAIT['QGeoTiledMappingManagerEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTileRequestManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoTileRequestManager: a plain Python object
  standing in front of one C++ QGeoTileRequestManager.

  What exists
  -----------

  Every function of Qt's QGeoTileRequestManager that has a ritual and that
  Python can call so far, 2 names in all: 'tileError', 'tileFetched'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoTileRequestManager::~QGeoTileRequestManager()': the destructor:
    Python never removes a C++ QGeoTileRequestManager.
  - Qt's 'QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>>
    QGeoTileRequestManager::requestTiles(const QSet<QGeoTileSpec> &tiles)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoTileRequestManager::tileTexture(const QGeoTileSpec &spec)': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoTileRequestManager is created at the first use, not by
    'QGeoTileRequestManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTileRequestManager.
  - Each name of Qt's QGeoTileRequestManager that has no cute function yet,
    'requestTiles', 'tileTexture', holds a function that raises
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
  __qt_class__ = 'QGeoTileRequestManager'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoTiledMap, QGeoTiledMappingManagerEngine)
  @overload(QGeoTiledMap, NoneType)
  @overload(NoneType, QGeoTiledMappingManagerEngine)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      map: Optional[QGeoTiledMap],
      engine: Optional[QGeoTiledMappingManagerEngine],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTileRequestManager::QGeoTileRequestManager(QGeoTiledMap *map,
    QGeoTiledMappingManagerEngine *engine)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilerequestmanager.html#QGeoTileRequestManager

    Parameters
    ----------

    map : Optional[QGeoTiledMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QGeoTiledMappingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoTileRequestManager::QGeoTileRequestManager(QGeoTiledMap *map,
    #      QGeoTiledMappingManagerEngine *engine)
    self._noteCreation(QGeoTileRequestManager, lambda: Rituals.call(
        'ritual_ZN22QGeoTileRequestManagerC1EP12QGeoTiledMapP29QGeoTiledMap'
        'pingManagerEngine',
        self._addressOf(map), self._addressOf(engine),
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

  @overload(QGeoTileSpec, str)
  def tileError(self, tile: QGeoTileSpec, errorString: str) -> None:
    """
    Calls Qt's 'void QGeoTileRequestManager::tileError(const QGeoTileSpec
    &tile, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilerequestmanager.html#tileError

    Parameters
    ----------

    tile : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTileRequestManager::tileError(const QGeoTileSpec &tile, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN22QGeoTileRequestManager9tileErrorERK12QGeoTileSpecRK7QSt'
        'ring',
        self._valueOf(tile), errorString,
    )

  @overload(QGeoTileSpec)
  def tileFetched(self, spec: QGeoTileSpec) -> None:
    """
    Calls Qt's 'void QGeoTileRequestManager::tileFetched(const QGeoTileSpec
    &spec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilerequestmanager.html#tileFetched

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  void QGeoTileRequestManager::tileFetched(const QGeoTileSpec &spec)
    self.uglySide.call(
        'ritual_ZN22QGeoTileRequestManager11tileFetchedERK12QGeoTileSpec',
        self._valueOf(spec),
    )

  @staticmethod
  def requestTiles(*__, **_) -> Never:
    """
    Qt's 'QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>>
    QGeoTileRequestManager::requestTiles(const QSet<QGeoTileSpec> &tiles)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTileRequestManager.requestTiles' has no cute function yet. "
        "Qt's 'QMap<QGeoTileSpec, QSharedPointer<QGeoTileTexture>> "
        "QGeoTileRequestManager::requestTiles(const QSet<QGeoTileSpec> "
        "&tiles)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def tileTexture(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QGeoTileTexture>
    QGeoTileRequestManager::tileTexture(const QGeoTileSpec &spec)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoTileRequestManager.tileTexture' has no cute function yet. "
        "Qt's 'QSharedPointer<QGeoTileTexture> "
        "QGeoTileRequestManager::tileTexture(const QGeoTileSpec &spec)': "
        "gives a type Python has no way to take yet.")
