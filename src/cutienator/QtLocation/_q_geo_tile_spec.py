"""
QGeoTileSpec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoTileSpec to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGeoTileSpec(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoTileSpec: a plain Python object standing in front
  of one C++ QGeoTileSpec.

  C++ hands a QGeoTileSpec around as a copy, so every C++ QGeoTileSpec behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoTileSpec that has a ritual and that Python can
  call so far, 17 names in all: 'plugin', 'setZoom', 'zoom', 'setX', 'x',
  'setY', 'y', 'setMapId', 'mapId', 'setVersion', 'version', '__eq__',
  '__ne__', '__lt__', 'isEqual', 'isLess', 'hash'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoTileSpec::QGeoTileSpec(QGeoTileSpec &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QGeoTileSpec::~QGeoTileSpec()': the destructor: Python removes its
    C++ QGeoTileSpec by it, and has no other use for it.
  - Qt's 'QGeoTileSpec &QGeoTileSpec::operator=(const QGeoTileSpec &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoTileSpec &QGeoTileSpec::operator=(QGeoTileSpec &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoTileSpec::swap(QGeoTileSpec &other)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoTileSpec is created at the first use, not by
    'QGeoTileSpec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoTileSpec back gives a copy the ritual made for
    Python, in a new cute QGeoTileSpec.
  - Each name of Qt's QGeoTileSpec that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTileSpec'

  #  Qt's '~QGeoTileSpec()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoTileSpec behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QGeoTileSpecD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def plugin(self) -> str:
    """
    Calls Qt's 'QString QGeoTileSpec::plugin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#plugin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoTileSpec::plugin() const
    return self.uglySide.call('ritual_ZNK12QGeoTileSpec6pluginEv')

  def zoom(self) -> int:
    """
    Calls Qt's 'int QGeoTileSpec::zoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#zoom
    """
    #  int QGeoTileSpec::zoom() const
    return self.uglySide.call('ritual_ZNK12QGeoTileSpec4zoomEv')

  def x(self) -> int:
    """
    Calls Qt's 'int QGeoTileSpec::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#x
    """
    #  int QGeoTileSpec::x() const
    return self.uglySide.call('ritual_ZNK12QGeoTileSpec1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QGeoTileSpec::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#y
    """
    #  int QGeoTileSpec::y() const
    return self.uglySide.call('ritual_ZNK12QGeoTileSpec1yEv')

  def mapId(self) -> int:
    """
    Calls Qt's 'int QGeoTileSpec::mapId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#mapId
    """
    #  int QGeoTileSpec::mapId() const
    return self.uglySide.call('ritual_ZNK12QGeoTileSpec5mapIdEv')

  def version(self) -> int:
    """
    Calls Qt's 'int QGeoTileSpec::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#version
    """
    #  int QGeoTileSpec::version() const
    return self.uglySide.call('ritual_ZNK12QGeoTileSpec7versionEv')

  @overload(THIS)
  def isEqual(self, rhs: QGeoTileSpec) -> bool:
    """
    Calls Qt's 'bool QGeoTileSpec::isEqual(const QGeoTileSpec &rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#isEqual

    Parameters
    ----------

    rhs : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  bool QGeoTileSpec::isEqual(const QGeoTileSpec &rhs) const
    return self.uglySide.call(
        'ritual_ZNK12QGeoTileSpec7isEqualERKS_', self._valueOf(rhs),
    )

  @overload(THIS)
  def isLess(self, rhs: QGeoTileSpec) -> bool:
    """
    Calls Qt's 'bool QGeoTileSpec::isLess(const QGeoTileSpec &rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#isLess

    Parameters
    ----------

    rhs : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  bool QGeoTileSpec::isLess(const QGeoTileSpec &rhs) const
    return self.uglySide.call(
        'ritual_ZNK12QGeoTileSpec6isLessERKS_', self._valueOf(rhs),
    )

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoTileSpec::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoTileSpec::hash(size_t seed) const
    return self.uglySide.call('ritual_ZNK12QGeoTileSpec4hashEm', seed)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setZoom(self, zoom: int) -> None:
    """
    Calls Qt's 'void QGeoTileSpec::setZoom(int zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#setZoom

    Parameters
    ----------

    zoom : int
      Passed on as it is.
    """
    #  void QGeoTileSpec::setZoom(int zoom)
    self.uglySide.call('ritual_ZN12QGeoTileSpec7setZoomEi', zoom)

  @overload(int)
  def setX(self, x: int) -> None:
    """
    Calls Qt's 'void QGeoTileSpec::setX(int x)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#setX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void QGeoTileSpec::setX(int x)
    self.uglySide.call('ritual_ZN12QGeoTileSpec4setXEi', x)

  @overload(int)
  def setY(self, y: int) -> None:
    """
    Calls Qt's 'void QGeoTileSpec::setY(int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#setY

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  void QGeoTileSpec::setY(int y)
    self.uglySide.call('ritual_ZN12QGeoTileSpec4setYEi', y)

  @overload(int)
  def setMapId(self, mapId: int) -> None:
    """
    Calls Qt's 'void QGeoTileSpec::setMapId(int mapId)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#setMapId

    Parameters
    ----------

    mapId : int
      Passed on as it is.
    """
    #  void QGeoTileSpec::setMapId(int mapId)
    self.uglySide.call('ritual_ZN12QGeoTileSpec8setMapIdEi', mapId)

  @overload(int)
  def setVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QGeoTileSpec::setVersion(int version)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#setVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QGeoTileSpec::setVersion(int version)
    self.uglySide.call('ritual_ZN12QGeoTileSpec10setVersionEi', version)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoTileSpec) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoTileSpec &lhs, const QGeoTileSpec
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#operator==

    Parameters
    ----------

    rhs : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  bool operator==(const QGeoTileSpec &lhs, const QGeoTileSpec &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QGeoTileSpecS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGeoTileSpec) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoTileSpec &lhs, const QGeoTileSpec
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#operator!=

    Parameters
    ----------

    rhs : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoTileSpec &lhs, const QGeoTileSpec &rhs)
    return Rituals.call(
        'ritual_ZneRK12QGeoTileSpecS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: QGeoTileSpec) -> bool:
    """
    Calls Qt's 'bool operator<(const QGeoTileSpec &lhs, const QGeoTileSpec
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#operator<

    Parameters
    ----------

    rhs : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  bool operator<(const QGeoTileSpec &lhs, const QGeoTileSpec &rhs)
    return Rituals.call(
        'ritual_ZltRK12QGeoTileSpecS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGeoTileSpec::QGeoTileSpec()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#QGeoTileSpec
    """
    #  QGeoTileSpec::QGeoTileSpec()
    self._noteCreation(QGeoTileSpec, lambda: Rituals.call(
        'ritual_ZN12QGeoTileSpecC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoTileSpec) -> None:
    """
    Notes what was given, for Qt's 'QGeoTileSpec::QGeoTileSpec(const
    QGeoTileSpec &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#QGeoTileSpec

    Parameters
    ----------

    other : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  QGeoTileSpec::QGeoTileSpec(const QGeoTileSpec &other)
    self._noteCreation(QGeoTileSpec, lambda: Rituals.call(
        'ritual_ZN12QGeoTileSpecC1ERKS_', self._valueOf(other),
    ))

  @overload(str, int, int, int, int)
  @overload(str, int, int, int, int, int)
  def __init__(
      self,
      plugin: str,
      mapId: int,
      zoom: int,
      x: int,
      y: int,
      version: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoTileSpec::QGeoTileSpec(const QString
    &plugin, int mapId, int zoom, int x, int y, int version)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilespec.html#QGeoTileSpec

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.

    mapId : int
      Passed on as it is.

    zoom : int
      Passed on as it is.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    version : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QGeoTileSpec::QGeoTileSpec(const QString &plugin, int mapId, int zoom,
    #      int x, int y, int version)
    self._noteCreation(QGeoTileSpec, lambda: Rituals.call(
        'ritual_ZN12QGeoTileSpecC1ERK7QStringiiiii',
        plugin, mapId, zoom, x, y, version,
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoTileSpec::swap(QGeoTileSpec &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTileSpec.swap' has no cute function yet. Qt's 'void "
        "QGeoTileSpec::swap(QGeoTileSpec &other)': takes a type Python has "
        "no way to hand over yet.")
