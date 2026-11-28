"""
QQuickSpriteSequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickspritesequence_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickSpriteSequence to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickSpriteSequencePrivate, QSGNode, QSGSpriteNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGNode = WAIT['QSGNode']
  QSGSpriteNode = WAIT['QSGSpriteNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSpriteSequence(QQuickItem):
  """
  The cute side of Qt's QQuickSpriteSequence: a plain Python object standing
  in front of one C++ QQuickSpriteSequence.

  It is built on the cute 'QQuickItem', as Qt's QQuickSpriteSequence is built
  on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSpriteSequence that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'running',
  'interpolate', 'goalSprite', 'currentSprite', 'runningChanged',
  'interpolateChanged', 'goalSpriteChanged', 'currentSpriteChanged',
  'jumpTo', 'setGoalSprite', 'setRunning', 'setInterpolate', 'createEngine',
  'reset', 'updatePaintNode', 'prepareNextFrame', 'initNode', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSpriteSequence::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSpriteSequence::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QQuickSprite> QQuickSpriteSequence::sprites()':
    gives a type Python has no way to take yet.
  - Qt's 'const QQuickSpriteSequencePrivate *QQuickSpriteSequence::d_func()
    const': takes in Python what 'QQuickSpriteSequencePrivate
    *QQuickSpriteSequence::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSpriteSequence is created at the first use, not by
    'QQuickSpriteSequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSpriteSequence.
  - Qt tells when it has removed the C++ QQuickSpriteSequence. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickSpriteSequence that has no cute function yet,
    'sprites', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuickSpriteSequence::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritesequence.html#tr

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
    #  QString QQuickSpriteSequence::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickSpriteSequence2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSpriteSequence'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSpriteSequence::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSpriteSequence::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickSpriteSequence10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def running(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteSequence::running() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritesequence.html#running
    """
    #  bool QQuickSpriteSequence::running() const
    return self.uglySide.call('ritual_ZNK20QQuickSpriteSequence7runningEv')

  def interpolate(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteSequence::interpolate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#interpolate
    """
    #  bool QQuickSpriteSequence::interpolate() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickSpriteSequence11interpolateEv',
    )

  def goalSprite(self) -> str:
    """
    Calls Qt's 'QString QQuickSpriteSequence::goalSprite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#goalSprite

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSpriteSequence::goalSprite() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickSpriteSequence10goalSpriteEv',
    )

  def currentSprite(self) -> str:
    """
    Calls Qt's 'QString QQuickSpriteSequence::currentSprite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#currentSprite

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSpriteSequence::currentSprite() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickSpriteSequence13currentSpriteEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setGoalSprite(self, sprite: str) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::setGoalSprite(const QString
    &sprite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#setGoalSprite

    Parameters
    ----------

    sprite : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSpriteSequence::setGoalSprite(const QString &sprite)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence13setGoalSpriteERK7QString', sprite,
    )

  @overload(bool)
  def setRunning(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::setRunning(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#setRunning

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteSequence::setRunning(bool arg)
    self.uglySide.call('ritual_ZN20QQuickSpriteSequence10setRunningEb', arg)

  @overload(bool)
  def setInterpolate(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::setInterpolate(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#setInterpolate

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteSequence::setInterpolate(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence14setInterpolateEb', arg,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSpriteSequence::QQuickSpriteSequence(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#QQuickSpriteSequence

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSpriteSequence::QQuickSpriteSequence(QQuickItem *parent)
    self._noteCreation(QQuickSpriteSequence, lambda: Rituals.call(
        'ritual_ZN20QQuickSpriteSequenceC1EP10QQuickItem',
        self._addressOf(parent),
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
  def runningChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::runningChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#runningChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteSequence::runningChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence14runningChangedEb', arg,
    )

  @overload(bool)
  def interpolateChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::interpolateChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#interpolateChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteSequence::interpolateChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence18interpolateChangedEb', arg,
    )

  @overload(str)
  def goalSpriteChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::goalSpriteChanged(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#goalSpriteChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSpriteSequence::goalSpriteChanged(const QString &arg)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence17goalSpriteChangedERK7QString', arg,
    )

  @overload(str)
  def currentSpriteChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::currentSpriteChanged(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#currentSpriteChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSpriteSequence::currentSpriteChanged(const QString &arg)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence20currentSpriteChangedERK7QString',
        arg,
    )

  @overload(str)
  def jumpTo(self, sprite: str) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::jumpTo(const QString &sprite)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritesequence.html#jumpTo

    Parameters
    ----------

    sprite : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSpriteSequence::jumpTo(const QString &sprite)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence6jumpToERK7QString', sprite,
    )

  def createEngine(self) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::createEngine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#createEngine
    """
    #  void QQuickSpriteSequence::createEngine()
    self.uglySide.call('ritual_ZN20QQuickSpriteSequence12createEngineEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritesequence.html#reset
    """
    #  void QQuickSpriteSequence::reset()
    self.uglySide.call('ritual_ZN20QQuickSpriteSequence5resetEv')

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickSpriteSequence::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickSpriteSequence::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN20QQuickSpriteSequence15updatePaintNodeEP7QSGNodePN10QQui'
        'ckItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickSpriteSequence15updatePaintNodeEP7QSGNodePN'
          '10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QSGSpriteNode)
  @overload(NoneType)
  def prepareNextFrame(self, node: Optional[QSGSpriteNode]) -> None:
    """
    Calls Qt's 'void QQuickSpriteSequence::prepareNextFrame(QSGSpriteNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritesequence.html#prepareNextFrame

    Parameters
    ----------

    node : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpriteSequence::prepareNextFrame(QSGSpriteNode *node)
    self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence16prepareNextFrameEP13QSGSpriteNode',
        self._addressOf(node),
    )

  def initNode(self) -> Optional[QSGSpriteNode]:
    """
    Calls Qt's 'QSGSpriteNode *QQuickSpriteSequence::initNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritesequence.html#initNode

    Returns
    -------

    Optional[QSGSpriteNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGSpriteNode *QQuickSpriteSequence::initNode()
    address = self.uglySide.call(
        'ritual_ZN20QQuickSpriteSequence8initNodeEv',
    )
    from . import QSGSpriteNode
    return QSGSpriteNode._cuteAt(address)

  def d_func(self) -> Optional[QQuickSpriteSequencePrivate]:
    """
    Calls Qt's 'QQuickSpriteSequencePrivate *QQuickSpriteSequence::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritesequence.html#d_func

    Returns
    -------

    Optional[QQuickSpriteSequencePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSpriteSequencePrivate *QQuickSpriteSequence::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickSpriteSequence6d_funcEv')
    from . import QQuickSpriteSequencePrivate
    return QQuickSpriteSequencePrivate._cuteAt(address)

  @staticmethod
  def sprites(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickSprite> QQuickSpriteSequence::sprites()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickSpriteSequence.sprites' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickSprite> QQuickSpriteSequence::sprites()': "
        "gives a type Python has no way to take yet.")
