"""
Qt3DRender::QTextureWrapMode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qtexturewrapmode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextureWrapMode(QObject):
  """
  The cute side of Qt's Qt3DRender::QTextureWrapMode: a plain Python object
  standing in front of one C++ Qt3DRender::QTextureWrapMode.

  It is built on the cute 'QObject', as Qt's Qt3DRender::QTextureWrapMode is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureWrapMode that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr', 'x', 'y',
  'z', 'setX', 'setY', 'setZ', 'xChanged', 'yChanged', 'zChanged'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QTextureWrapMode::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QTextureWrapMode::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QTextureWrapMode::~QTextureWrapMode()': the destructor:
    Python never removes a C++ Qt3DRender::QTextureWrapMode.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureWrapMode is created at the first use, not by
    'Qt3DRender::QTextureWrapMode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QTextureWrapMode.
  - Qt tells when it has removed the C++ Qt3DRender::QTextureWrapMode. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QTextureWrapMode, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class WrapMode(CuteNum):
    """
    The enum 'Qt3DRender::QTextureWrapMode::WrapMode' of Qt, with the 4 names
    Qt gives in it.
    """

    Repeat = Kee[int](10497)
    MirroredRepeat = Kee[int](33648)
    ClampToEdge = Kee[int](33071)
    ClampToBorder = Kee[int](33069)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QTextureWrapMode::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QTextureWrapMode::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender16QTextureWrapMode2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QTextureWrapMode'

  #  A C++ Qt3DRender::QTextureWrapMode Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QTextureWrapMode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QTextureWrapMode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QTextureWrapMode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QTextureWrapMode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode Qt3DRender::QTextureWrapMode::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#x

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode Qt3DRender::QTextureWrapMode::x() const
    return QTextureWrapMode.WrapMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QTextureWrapMode1xEv',
    ))

  def y(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode Qt3DRender::QTextureWrapMode::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#y

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode Qt3DRender::QTextureWrapMode::y() const
    return QTextureWrapMode.WrapMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QTextureWrapMode1yEv',
    ))

  def z(self) -> WrapMode:
    """
    Calls Qt's 'WrapMode Qt3DRender::QTextureWrapMode::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#z

    Returns
    -------

    WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WrapMode(number)' gives.
    """
    #  WrapMode Qt3DRender::QTextureWrapMode::z() const
    return QTextureWrapMode.WrapMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QTextureWrapMode1zEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WrapMode)
  def setX(self, x: WrapMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureWrapMode::setX(WrapMode x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#setX

    Parameters
    ----------

    x : WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureWrapMode::setX(WrapMode x)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QTextureWrapMode4setXENS0_8WrapModeE',
        x.value,
    )

  @overload(WrapMode)
  def setY(self, y: WrapMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureWrapMode::setY(WrapMode y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#setY

    Parameters
    ----------

    y : WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureWrapMode::setY(WrapMode y)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QTextureWrapMode4setYENS0_8WrapModeE',
        y.value,
    )

  @overload(WrapMode)
  def setZ(self, z: WrapMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureWrapMode::setZ(WrapMode z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#setZ

    Parameters
    ----------

    z : WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureWrapMode::setZ(WrapMode z)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QTextureWrapMode4setZENS0_8WrapModeE',
        z.value,
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
  @overload(WrapMode)
  @overload(WrapMode, QObject)
  @overload(WrapMode, NoneType)
  def __init__(
      self,
      wrapMode: WrapMode = WrapMode.ClampToEdge,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QTextureWrapMode::QTextureWrapMode(WrapMode wrapMode,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#QTextureWrapMode

    Parameters
    ----------

    wrapMode : WrapMode
      Passed on as its number. May be left out, as in Qt: it is then
      WrapMode.ClampToEdge.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QTextureWrapMode::QTextureWrapMode(WrapMode wrapMode,
    #      QObject *parent)
    self._noteCreation(QTextureWrapMode, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QTextureWrapModeC1ENS0_8WrapModeEP7QObject',
        wrapMode.value, self._addressOf(parent, 'QObject'),
    ))

  @overload(WrapMode, WrapMode, WrapMode)
  @overload(WrapMode, WrapMode, WrapMode, QObject)
  @overload(WrapMode, WrapMode, WrapMode, NoneType)
  def __init__(
      self,
      x: WrapMode,
      y: WrapMode,
      z: WrapMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QTextureWrapMode::QTextureWrapMode(WrapMode x, WrapMode y,
    WrapMode z, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#QTextureWrapMode

    Parameters
    ----------

    x : WrapMode
      Passed on as its number.

    y : WrapMode
      Passed on as its number.

    z : WrapMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QTextureWrapMode::QTextureWrapMode(WrapMode x, WrapMode y,
    #      WrapMode z, QObject *parent)
    self._noteCreation(QTextureWrapMode, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QTextureWrapModeC1ENS0_8WrapModeES1_S1_P7QO'
        'bject',
        x.value, y.value, z.value, self._addressOf(parent, 'QObject'),
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

  @overload(WrapMode)
  def xChanged(self, x: WrapMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureWrapMode::xChanged(WrapMode x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#xChanged

    Parameters
    ----------

    x : WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureWrapMode::xChanged(WrapMode x)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QTextureWrapMode8xChangedENS0_8WrapModeE',
        x.value,
    )

  @overload(WrapMode)
  def yChanged(self, y: WrapMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureWrapMode::yChanged(WrapMode y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#yChanged

    Parameters
    ----------

    y : WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureWrapMode::yChanged(WrapMode y)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QTextureWrapMode8yChangedENS0_8WrapModeE',
        y.value,
    )

  @overload(WrapMode)
  def zChanged(self, z: WrapMode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureWrapMode::zChanged(WrapMode z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturewrapmode.html#zChanged

    Parameters
    ----------

    z : WrapMode
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureWrapMode::zChanged(WrapMode z)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QTextureWrapMode8zChangedENS0_8WrapModeE',
        z.value,
    )
