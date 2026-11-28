"""
QQuickSpriteEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickSpriteEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickPixmap, QQuickStochasticEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
  from . import QQuickSprite
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickSprite = WAIT['QQuickSprite']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSpriteEngine(QQuickStochasticEngine):
  """
  The cute side of Qt's QQuickSpriteEngine: a plain Python object standing in
  front of one C++ QQuickSpriteEngine.

  It is built on the cute 'QQuickStochasticEngine', as Qt's
  QQuickSpriteEngine is built on Qt's QQuickStochasticEngine, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSpriteEngine that has a ritual and that Python
  can call so far, 22 names in all: 'metaObject', 'tr', 'sprite',
  'spriteState', 'spriteStart', 'spriteFrames', 'spriteDuration', 'spriteX',
  'spriteY', 'spriteWidth', 'spriteHeight', 'spriteCount', 'maxFrames',
  'restart', 'advance', 'isNull', 'isReady', 'isLoading', 'isError',
  'status', 'startAssemblingImage', 'assembledImage'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSpriteEngine::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickSpriteEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSpriteEngine::~QQuickSpriteEngine()': the destructor: Python
    never removes a C++ QQuickSpriteEngine.
  - Qt's 'QQmlListProperty<QQuickSprite> QQuickSpriteEngine::sprites()':
    gives a type Python has no way to take yet.
  - Qt's 'int QQuickSpriteEngine::pseudospriteProgress(int a0, int a1, int
    *rd) const': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSpriteEngine is created at the first use, not by
    'QQuickSpriteEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSpriteEngine.
  - Qt tells when it has removed the C++ QQuickSpriteEngine. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickSpriteEngine that has no cute function yet,
    'pseudospriteProgress', 'sprites', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QQuickSpriteEngine::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#tr

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
    #  QString QQuickSpriteEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickSpriteEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSpriteEngine'

  #  A C++ QQuickSpriteEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSpriteEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSpriteEngine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSpriteEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(int)
  def sprite(self, sprite: int = 0) -> Optional[QQuickSprite]:
    """
    Calls Qt's 'QQuickSprite *QQuickSpriteEngine::sprite(int sprite) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#sprite

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QQuickSprite]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSprite *QQuickSpriteEngine::sprite(int sprite) const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine6spriteEi', sprite,
    )
    from . import QQuickSprite
    return QQuickSprite._cuteAt(address)

  @overload()
  @overload(int)
  def spriteState(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteState(int sprite) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#spriteState

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteState(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine11spriteStateEi', sprite,
    )

  @overload()
  @overload(int)
  def spriteStart(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteStart(int sprite) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#spriteStart

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteStart(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine11spriteStartEi', sprite,
    )

  @overload()
  @overload(int)
  def spriteFrames(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteFrames(int sprite) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#spriteFrames

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteFrames(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine12spriteFramesEi', sprite,
    )

  @overload()
  @overload(int)
  def spriteDuration(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteDuration(int sprite) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#spriteDuration

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteDuration(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine14spriteDurationEi', sprite,
    )

  @overload()
  @overload(int)
  def spriteX(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteX(int sprite) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#spriteX

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteX(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine7spriteXEi', sprite,
    )

  @overload()
  @overload(int)
  def spriteY(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteY(int sprite) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#spriteY

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteY(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine7spriteYEi', sprite,
    )

  @overload()
  @overload(int)
  def spriteWidth(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteWidth(int sprite) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#spriteWidth

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteWidth(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine11spriteWidthEi', sprite,
    )

  @overload()
  @overload(int)
  def spriteHeight(self, sprite: int = 0) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteHeight(int sprite) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#spriteHeight

    Parameters
    ----------

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickSpriteEngine::spriteHeight(int sprite) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine12spriteHeightEi', sprite,
    )

  def spriteCount(self) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::spriteCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#spriteCount
    """
    #  int QQuickSpriteEngine::spriteCount() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine11spriteCountEv',
    )

  def maxFrames(self) -> int:
    """
    Calls Qt's 'int QQuickSpriteEngine::maxFrames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#maxFrames
    """
    #  int QQuickSpriteEngine::maxFrames() const
    return self.uglySide.call('ritual_ZNK18QQuickSpriteEngine9maxFramesEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteEngine::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#isNull
    """
    #  bool QQuickSpriteEngine::isNull() const
    return self.uglySide.call('ritual_ZNK18QQuickSpriteEngine6isNullEv')

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteEngine::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#isReady
    """
    #  bool QQuickSpriteEngine::isReady() const
    return self.uglySide.call('ritual_ZNK18QQuickSpriteEngine7isReadyEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteEngine::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#isLoading
    """
    #  bool QQuickSpriteEngine::isLoading() const
    return self.uglySide.call('ritual_ZNK18QQuickSpriteEngine9isLoadingEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteEngine::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#isError
    """
    #  bool QQuickSpriteEngine::isError() const
    return self.uglySide.call('ritual_ZNK18QQuickSpriteEngine7isErrorEv')

  def status(self) -> QQuickPixmap.Status:
    """
    Calls Qt's 'QQuickPixmap::Status QQuickSpriteEngine::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#status

    Returns
    -------

    QQuickPixmap.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickPixmap.Status(number)' gives.
    """
    #  QQuickPixmap::Status QQuickSpriteEngine::status() const
    return QQuickPixmap.Status(self.uglySide.call(
        'ritual_ZNK18QQuickSpriteEngine6statusEv',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSpriteEngine::QQuickSpriteEngine(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#QQuickSpriteEngine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSpriteEngine::QQuickSpriteEngine(QObject *parent)
    self._noteCreation(QQuickSpriteEngine, lambda: Rituals.call(
        'ritual_ZN18QQuickSpriteEngineC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QList[QQuickSprite])
  @overload(QList[QQuickSprite], QObject)
  @overload(QList[QQuickSprite], NoneType)
  def __init__(
      self,
      sprites: QList[QQuickSprite],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSpriteEngine::QQuickSpriteEngine(const QList<QQuickSprite *>
    &sprites, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#QQuickSpriteEngine

    Parameters
    ----------

    sprites : QList[QQuickSprite]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSpriteEngine::QQuickSpriteEngine(const QList<QQuickSprite *>
    #      &sprites, QObject *parent)
    self._noteCreation(QQuickSpriteEngine, lambda: Rituals.call(
        'ritual_ZN18QQuickSpriteEngineC1ERK5QListIP12QQuickSpriteEP7QObject',
        self._valueOf(sprites), self._addressOf(parent, 'QObject'),
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

  @overload()
  @overload(int)
  def restart(self, index: int = 0) -> None:
    """
    Calls Qt's 'void QQuickSpriteEngine::restart(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#restart

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickSpriteEngine::restart(int index)
    ritual = 'ritual_ZN18QQuickSpriteEngine7restartEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickSpriteEngine7restartEi'
    self.uglySide.call(ritual, index)

  @overload()
  @overload(int)
  def advance(self, index: int = 0) -> None:
    """
    Calls Qt's 'void QQuickSpriteEngine::advance(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspriteengine.html#advance

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickSpriteEngine::advance(int index)
    ritual = 'ritual_ZN18QQuickSpriteEngine7advanceEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickSpriteEngine7advanceEi'
    self.uglySide.call(ritual, index)

  def startAssemblingImage(self) -> None:
    """
    Calls Qt's 'void QQuickSpriteEngine::startAssemblingImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#startAssemblingImage
    """
    #  void QQuickSpriteEngine::startAssemblingImage()
    self.uglySide.call(
        'ritual_ZN18QQuickSpriteEngine20startAssemblingImageEv',
    )

  @overload()
  @overload(int)
  def assembledImage(self, maxSize: int = 2048) -> QImage:
    """
    Calls Qt's 'QImage QQuickSpriteEngine::assembledImage(int maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspriteengine.html#assembledImage

    Parameters
    ----------

    maxSize : int
      Passed on as it is. May be left out, as in Qt: it is then 2048.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickSpriteEngine::assembledImage(int maxSize)
    address = self.uglySide.call(
        'ritual_ZN18QQuickSpriteEngine14assembledImageEi', maxSize,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @staticmethod
  def pseudospriteProgress(*__, **_) -> Never:
    """
    Qt's 'int QQuickSpriteEngine::pseudospriteProgress(int a0, int a1, int
    *rd) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickSpriteEngine.pseudospriteProgress' has no cute function "
        "yet. Qt's 'int QQuickSpriteEngine::pseudospriteProgress(int a0, "
        "int a1, int *rd) const': takes a number to change where it is.")

  @staticmethod
  def sprites(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickSprite> QQuickSpriteEngine::sprites()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickSpriteEngine.sprites' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickSprite> QQuickSpriteEngine::sprites()': "
        "gives a type Python has no way to take yet.")
