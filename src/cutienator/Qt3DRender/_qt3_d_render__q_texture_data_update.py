"""
Qt3DRender::QTextureDataUpdate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qtexturedataupdate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QTextureDataUpdate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QTextureDataUpdate: a plain Python object
  standing in front of one C++ Qt3DRender::QTextureDataUpdate.

  C++ hands a Qt3DRender::QTextureDataUpdate around as a copy, so every C++
  Qt3DRender::QTextureDataUpdate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureDataUpdate that has a ritual and
  that Python can call so far, 14 names in all: 'x', 'y', 'z', 'layer',
  'mipLevel', 'face', 'setX', 'setY', 'setZ', 'setLayer', 'setMipLevel',
  'setFace', '__eq__', 'd_func'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextureDataUpdate &Qt3DRender::QTextureDataUpdate::operator=(const
    QTextureDataUpdate &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QTextureDataUpdate
    &Qt3DRender::QTextureDataUpdate::operator=(QTextureDataUpdate &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'Qt3DRender::QTextureDataUpdate::~QTextureDataUpdate()': the
    destructor: Python removes its C++ Qt3DRender::QTextureDataUpdate by it,
    and has no other use for it.
  - Qt's 'void Qt3DRender::QTextureDataUpdate::swap(QTextureDataUpdate
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QTextureImageDataPtr Qt3DRender::QTextureDataUpdate::data() const':
    gives a type Python has no way to take yet.
  - Qt's 'void Qt3DRender::QTextureDataUpdate::setData(const
    QTextureImageDataPtr &data)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QTextureDataUpdatePrivate
    *Qt3DRender::QTextureDataUpdate::d_func() const': takes in Python what
    'QTextureDataUpdatePrivate *Qt3DRender::QTextureDataUpdate::d_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureDataUpdate is created at the first use, not
    by 'Qt3DRender::QTextureDataUpdate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QTextureDataUpdate back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::QTextureDataUpdate.
  - Each name of Qt's Qt3DRender::QTextureDataUpdate that has no cute
    function yet, 'data', 'setData', 'swap', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::QTextureDataUpdate'

  #  Qt's '~Qt3DRender::QTextureDataUpdate()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::QTextureDataUpdate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender18QTextureDataUpdateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def x(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureDataUpdate::x() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#x
    """
    #  int Qt3DRender::QTextureDataUpdate::x() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QTextureDataUpdate1xEv',
    )

  def y(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureDataUpdate::y() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#y
    """
    #  int Qt3DRender::QTextureDataUpdate::y() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QTextureDataUpdate1yEv',
    )

  def z(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureDataUpdate::z() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#z
    """
    #  int Qt3DRender::QTextureDataUpdate::z() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QTextureDataUpdate1zEv',
    )

  def layer(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureDataUpdate::layer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#layer
    """
    #  int Qt3DRender::QTextureDataUpdate::layer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QTextureDataUpdate5layerEv',
    )

  def mipLevel(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureDataUpdate::mipLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#mipLevel
    """
    #  int Qt3DRender::QTextureDataUpdate::mipLevel() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QTextureDataUpdate8mipLevelEv',
    )

  def face(self) -> Qt3DRender.QAbstractTexture.CubeMapFace:
    """
    Calls Qt's 'QAbstractTexture::CubeMapFace
    Qt3DRender::QTextureDataUpdate::face() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#face

    Returns
    -------

    Qt3DRender.QAbstractTexture.CubeMapFace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.CubeMapFace(number)' gives.
    """
    #  QAbstractTexture::CubeMapFace Qt3DRender::QTextureDataUpdate::face()
    #      const
    return Qt3DRender.QAbstractTexture.CubeMapFace(self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QTextureDataUpdate4faceEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setX(self, x: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureDataUpdate::setX(int x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#setX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureDataUpdate::setX(int x)
    self.uglySide.call('ritual_ZN10Qt3DRender18QTextureDataUpdate4setXEi', x)

  @overload(int)
  def setY(self, y: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureDataUpdate::setY(int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#setY

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureDataUpdate::setY(int y)
    self.uglySide.call('ritual_ZN10Qt3DRender18QTextureDataUpdate4setYEi', y)

  @overload(int)
  def setZ(self, z: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureDataUpdate::setZ(int z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#setZ

    Parameters
    ----------

    z : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureDataUpdate::setZ(int z)
    self.uglySide.call('ritual_ZN10Qt3DRender18QTextureDataUpdate4setZEi', z)

  @overload(int)
  def setLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureDataUpdate::setLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#setLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureDataUpdate::setLayer(int layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QTextureDataUpdate8setLayerEi', layer,
    )

  @overload(int)
  def setMipLevel(self, mipLevel: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureDataUpdate::setMipLevel(int
    mipLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#setMipLevel

    Parameters
    ----------

    mipLevel : int
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureDataUpdate::setMipLevel(int mipLevel)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QTextureDataUpdate11setMipLevelEi', mipLevel,
    )

  @overload(Qt3DRender.QAbstractTexture.CubeMapFace)
  def setFace(self, face: Qt3DRender.QAbstractTexture.CubeMapFace) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QTextureDataUpdate::setFace(QAbstractTexture::CubeMapFace
    face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#setFace

    Parameters
    ----------

    face : Qt3DRender.QAbstractTexture.CubeMapFace
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureDataUpdate::setFace(QAbstractTexture::
    #      CubeMapFace face)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QTextureDataUpdate7setFaceENS_16QAbstractTe'
        'xture11CubeMapFaceE',
        face.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QTextureDataUpdate) -> bool:
    """
    Calls Qt's 'bool operator==(const QTextureDataUpdate &lhs, const
    QTextureDataUpdate &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#operator==

    Parameters
    ----------

    rhs : QTextureDataUpdate
      Passed on as a value: Qt reads the C++ Qt3DRender::QTextureDataUpdate,
      which stays Python's own.
    """
    #  bool operator==(const QTextureDataUpdate &lhs, const
    #      QTextureDataUpdate &rhs)
    return Rituals.call(
        'ritual_ZN10Qt3DRendereqERKNS_18QTextureDataUpdateES2_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QTextureDataUpdate::QTextureDataUpdate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html
    """
    #  Qt3DRender::QTextureDataUpdate::QTextureDataUpdate()
    self._noteCreation(QTextureDataUpdate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QTextureDataUpdateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QTextureDataUpdate) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QTextureDataUpdate::QTextureDataUpdate(const
    QTextureDataUpdate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html

    Parameters
    ----------

    other : QTextureDataUpdate
      Passed on as a value: Qt reads the C++ Qt3DRender::QTextureDataUpdate,
      which stays Python's own.
    """
    #  Qt3DRender::QTextureDataUpdate::QTextureDataUpdate(const
    #      QTextureDataUpdate &other)
    self._noteCreation(QTextureDataUpdate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QTextureDataUpdateC1ERKS0_',
        self._valueOf(other),
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

  def d_func(self) -> Optional[Qt3DRender.QTextureDataUpdatePrivate]:
    """
    Calls Qt's 'QTextureDataUpdatePrivate
    *Qt3DRender::QTextureDataUpdate::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturedataupdate.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QTextureDataUpdatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureDataUpdatePrivate *Qt3DRender::QTextureDataUpdate::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender18QTextureDataUpdate6d_funcEv',
    )
    return Qt3DRender.QTextureDataUpdatePrivate._cuteAt(address)

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QTextureImageDataPtr Qt3DRender::QTextureDataUpdate::data() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureDataUpdate.data' has no cute function yet. "
        "Qt's 'QTextureImageDataPtr Qt3DRender::QTextureDataUpdate::data() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setData(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QTextureDataUpdate::setData(const
    QTextureImageDataPtr &data)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureDataUpdate.setData' has no cute function yet. "
        "Qt's 'void Qt3DRender::QTextureDataUpdate::setData(const "
        "QTextureImageDataPtr &data)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QTextureDataUpdate::swap(QTextureDataUpdate
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureDataUpdate.swap' has no cute function yet. "
        "Qt's 'void Qt3DRender::QTextureDataUpdate::swap(QTextureDataUpdate "
        "&other)': takes a type Python has no way to hand over yet.")
