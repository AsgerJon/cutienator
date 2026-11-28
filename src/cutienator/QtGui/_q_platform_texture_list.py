"""
QPlatformTextureList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect
  from . import QRhiTexture

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformTextureList(QObject):
  """
  The cute side of Qt's QPlatformTextureList: a plain Python object standing
  in front of one C++ QPlatformTextureList.

  It is built on the cute 'QObject', as Qt's QPlatformTextureList is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformTextureList that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'count',
  'isEmpty', 'texture', 'textureExtra', 'geometry', 'clipRect', 'flags',
  'lock', 'isLocked', 'clear', 'locked'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformTextureList::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformTextureList::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformTextureListPrivate *QPlatformTextureList::d_func()': gives
    'QPlatformTextureListPrivate', which has no cute class yet.
  - Qt's 'const QPlatformTextureListPrivate *QPlatformTextureList::d_func()
    const': gives 'QPlatformTextureListPrivate', which has no cute class yet.
  - Qt's 'QPlatformTextureList::~QPlatformTextureList()': the destructor:
    Python never removes a C++ QPlatformTextureList.
  - Qt's 'void *QPlatformTextureList::source(int index)': gives 'void', which
    has no cute class yet.
  - Qt's 'void QPlatformTextureList::appendTexture(void *source, QRhiTexture
    *texture, const QRect &geometry, const QRect &clipRect, Flags flags)':
    names 'void', which has no cute class yet.
  - Qt's 'void QPlatformTextureList::appendTexture(void *source, QRhiTexture
    *textureLeft, QRhiTexture *textureRight, const QRect &geometry, const
    QRect &clipRect, Flags flags)': names 'void', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformTextureList is created at the first use, not by
    'QPlatformTextureList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformTextureList.
  - Qt tells when it has removed the C++ QPlatformTextureList. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformTextureList that has no cute function yet,
    'appendTexture', 'source', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformTextureList, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QPlatformTextureList::Flag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QPlatformTextureList::Flags'.
    """

    StacksOnTop = 0x1
    TextureIsSrgb = 0x2
    NeedsPremultipliedAlphaBlending = 0x4
    MirrorVertically = 0x8

  Flags = Flag

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
    Calls Qt's 'QString QPlatformTextureList::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#tr

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
    #  QString QPlatformTextureList::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QPlatformTextureList2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformTextureList'

  #  A C++ QPlatformTextureList Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformTextureList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlatformTextureList::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtexturelist.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformTextureList::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformTextureList10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QPlatformTextureList::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#count
    """
    #  int QPlatformTextureList::count() const
    return self.uglySide.call('ritual_ZNK20QPlatformTextureList5countEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlatformTextureList::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#isEmpty
    """
    #  bool QPlatformTextureList::isEmpty() const
    return self.uglySide.call('ritual_ZNK20QPlatformTextureList7isEmptyEv')

  @overload(int)
  def texture(self, index: int) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QPlatformTextureList::texture(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#texture

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QPlatformTextureList::texture(int index) const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformTextureList7textureEi', index,
    )
    from . import QRhiTexture
    return QRhiTexture._cuteAt(address)

  @overload(int)
  def textureExtra(self, index: int) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QPlatformTextureList::textureExtra(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtexturelist.html#textureExtra

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QPlatformTextureList::textureExtra(int index) const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformTextureList12textureExtraEi', index,
    )
    from . import QRhiTexture
    return QRhiTexture._cuteAt(address)

  @overload(int)
  def geometry(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect QPlatformTextureList::geometry(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#geometry

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformTextureList::geometry(int index) const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformTextureList8geometryEi', index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def clipRect(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect QPlatformTextureList::clipRect(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#clipRect

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformTextureList::clipRect(int index) const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformTextureList8clipRectEi', index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def flags(self, index: int) -> Flags:
    """
    Calls Qt's 'Flags QPlatformTextureList::flags(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#flags

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QPlatformTextureList::flags(int index) const
    return QPlatformTextureList.Flags(self.uglySide.call(
        'ritual_ZNK20QPlatformTextureList5flagsEi', index,
    ))

  def isLocked(self) -> bool:
    """
    Calls Qt's 'bool QPlatformTextureList::isLocked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#isLocked
    """
    #  bool QPlatformTextureList::isLocked() const
    return self.uglySide.call('ritual_ZNK20QPlatformTextureList8isLockedEv')

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformTextureList::QPlatformTextureList(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformtexturelist.html#QPlatformTextureList

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlatformTextureList::QPlatformTextureList(QObject *parent)
    self._noteCreation(QPlatformTextureList, lambda: Rituals.call(
        'ritual_ZN20QPlatformTextureListC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(bool)
  def lock(self, on: bool) -> None:
    """
    Calls Qt's 'void QPlatformTextureList::lock(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#lock

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QPlatformTextureList::lock(bool on)
    self.uglySide.call('ritual_ZN20QPlatformTextureList4lockEb', on)

  def clear(self) -> None:
    """
    Calls Qt's 'void QPlatformTextureList::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#clear
    """
    #  void QPlatformTextureList::clear()
    self.uglySide.call('ritual_ZN20QPlatformTextureList5clearEv')

  @overload(bool)
  def locked(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlatformTextureList::locked(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformtexturelist.html#locked

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlatformTextureList::locked(bool a0)
    self.uglySide.call('ritual_ZN20QPlatformTextureList6lockedEb', a0)

  @staticmethod
  def appendTexture(*__, **_) -> Never:
    """
    - Qt's 'void QPlatformTextureList::appendTexture(void *source,
      QRhiTexture *texture, const QRect &geometry, const QRect &clipRect,
      Flags flags)': names 'void', which has no cute class yet.
    - Qt's 'void QPlatformTextureList::appendTexture(void *source,
      QRhiTexture *textureLeft, QRhiTexture *textureRight, const QRect
      &geometry, const QRect &clipRect, Flags flags)': names 'void', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformTextureList.appendTexture' has no cute function yet. "
        "Qt's 'void QPlatformTextureList::appendTexture(void *source, "
        "QRhiTexture *texture, const QRect &geometry, const QRect "
        "&clipRect, Flags flags)': names 'void', which has no cute class "
        "yet. Qt's 'void QPlatformTextureList::appendTexture(void *source, "
        "QRhiTexture *textureLeft, QRhiTexture *textureRight, const QRect "
        "&geometry, const QRect &clipRect, Flags flags)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def source(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformTextureList::source(int index)': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformTextureList.source' has no cute function yet. Qt's 'void "
        "*QPlatformTextureList::source(int index)': gives 'void', which has "
        "no cute class yet.")
