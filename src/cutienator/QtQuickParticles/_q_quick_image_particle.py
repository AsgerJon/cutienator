"""
QQuickImageParticle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickimageparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickImageParticle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickParticlePainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QColor
  from ..QtQuick import QQuickStochasticEngine, QSGNode
  from . import QQuickDirection, QQuickParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuickDirection = WAIT['QQuickDirection']
  QQuickParticleData = WAIT['QQuickParticleData']
  QSGNode = WAIT['QSGNode']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImageParticle(QQuickParticlePainter):
  """
  The cute side of Qt's QQuickImageParticle: a plain Python object standing
  in front of one C++ QQuickImageParticle.

  It is built on the cute 'QQuickParticlePainter', as Qt's
  QQuickImageParticle is built on Qt's QQuickParticlePainter, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImageParticle that has a ritual and that
  Python can call so far, 85 names in all: 'metaObject', 'tr',
  'spriteEngine', 'image', 'setImage', 'colortable', 'setColortable',
  'sizetable', 'setSizetable', 'opacitytable', 'setOpacitytable', 'color',
  'setColor', 'colorVariation', 'setColorVariation', 'alphaVariation',
  'alpha', 'redVariation', 'greenVariation', 'blueVariation', 'rotation',
  'rotationVariation', 'rotationVelocity', 'rotationVelocityVariation',
  'autoRotation', 'xVector', 'yVector', 'spritesInterpolate',
  'bypassOptimizations', 'entryEffect', 'status', 'resetColor',
  'resetRotation', 'resetDeformation', 'imageChanged', 'colortableChanged',
  'sizetableChanged', 'opacitytableChanged', 'colorChanged',
  'colorVariationChanged', 'alphaVariationChanged', 'alphaChanged',
  'redVariationChanged', 'greenVariationChanged', 'blueVariationChanged',
  'rotationChanged', 'rotationVariationChanged', 'rotationVelocityChanged',
  'rotationVelocityVariationChanged', 'autoRotationChanged',
  'xVectorChanged', 'yVectorChanged', 'spritesInterpolateChanged',
  'bypassOptimizationsChanged', 'entryEffectChanged', 'statusChanged',
  'setAlphaVariation', 'setAlpha', 'setRedVariation', 'setGreenVariation',
  'setBlueVariation', 'setRotation', 'setRotationVariation',
  'setRotationVelocity', 'setRotationVelocityVariation', 'setAutoRotation',
  'setXVector', 'setYVector', 'setSpritesInterpolate',
  'setBypassOptimizations', 'setEntryEffect', 'reset', 'initialize',
  'commit', 'updatePaintNode', 'sceneGraphInvalidated', 'createEngine',
  'spriteAdvance', 'spritesUpdate', 'mainThreadFetchImageData',
  'invalidateSceneGraph', 'loadingSomething', 'clearShadows',
  'getShadowDatum', 'checkPerfLevel'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImageParticle::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickImageParticle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickImageParticle::~QQuickImageParticle()': the destructor:
    Python never removes a C++ QQuickImageParticle.
  - Qt's 'QQmlListProperty<QQuickSprite> QQuickImageParticle::sprites()':
    gives a type Python has no way to take yet.
  - Qt's 'bool QQuickImageParticle::prepareNextFrame(QSGNode **a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQuickImageParticle::buildParticleNodes(QSGNode **a0)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQuickImageParticle::finishBuildParticleNodes(QSGNode **n)':
    takes a type Python has no way to hand over yet.
  - Qt's 'ImageMaterialData *QQuickImageParticle::getState(QSGMaterial *m)':
    gives 'ImageMaterialData', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 97 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QQuickImageParticle is created at the first use, not by
    'QQuickImageParticle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageParticle.
  - Qt tells when it has removed the C++ QQuickImageParticle. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickImageParticle that has no cute function yet,
    'buildParticleNodes', 'finishBuildParticleNodes', 'getState',
    'initTexCoords', 'prepareNextFrame', 'sprites', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickImageParticle, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class EntryEffect(CuteNum):
    """
    The enum 'QQuickImageParticle::EntryEffect' of Qt, with the 3 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Fade = Kee[int](1)
    Scale = Kee[int](2)

  class PerformanceLevel(CuteNum):
    """
    The enum 'QQuickImageParticle::PerformanceLevel' of Qt, with the 7 names
    Qt gives in it.
    """

    Unknown = Kee[int](0)
    SimplePoint = Kee[int](1)
    ColoredPoint = Kee[int](2)
    Colored = Kee[int](3)
    Deformable = Kee[int](4)
    Tabled = Kee[int](5)
    Sprites = Kee[int](6)

  class Status(CuteNum):
    """
    The enum 'QQuickImageParticle::Status' of Qt, with the 4 names Qt gives
    in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QQuickImageParticle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#tr

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
    #  QString QQuickImageParticle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickImageParticle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImageParticle'

  #  A C++ QQuickImageParticle Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImageParticle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickImageParticle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImageParticle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def image(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickImageParticle::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#image

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickImageParticle::image() const
    address = self.uglySide.call('ritual_ZNK19QQuickImageParticle5imageEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def colortable(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickImageParticle::colortable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#colortable

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickImageParticle::colortable() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle10colortableEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sizetable(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickImageParticle::sizetable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#sizetable

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickImageParticle::sizetable() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle9sizetableEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def opacitytable(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickImageParticle::opacitytable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#opacitytable

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickImageParticle::opacitytable() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle12opacitytableEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickImageParticle::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickImageParticle::color() const
    address = self.uglySide.call('ritual_ZNK19QQuickImageParticle5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def colorVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::colorVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#colorVariation
    """
    #  qreal QQuickImageParticle::colorVariation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle14colorVariationEv',
    )

  def alphaVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::alphaVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#alphaVariation
    """
    #  qreal QQuickImageParticle::alphaVariation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle14alphaVariationEv',
    )

  def alpha(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::alpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#alpha
    """
    #  qreal QQuickImageParticle::alpha() const
    return self.uglySide.call('ritual_ZNK19QQuickImageParticle5alphaEv')

  def redVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::redVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#redVariation
    """
    #  qreal QQuickImageParticle::redVariation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle12redVariationEv',
    )

  def greenVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::greenVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#greenVariation
    """
    #  qreal QQuickImageParticle::greenVariation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle14greenVariationEv',
    )

  def blueVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::blueVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#blueVariation
    """
    #  qreal QQuickImageParticle::blueVariation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle13blueVariationEv',
    )

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#rotation
    """
    #  qreal QQuickImageParticle::rotation() const
    return self.uglySide.call('ritual_ZNK19QQuickImageParticle8rotationEv')

  def rotationVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::rotationVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#rotationVariation
    """
    #  qreal QQuickImageParticle::rotationVariation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle17rotationVariationEv',
    )

  def rotationVelocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::rotationVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#rotationVelocity
    """
    #  qreal QQuickImageParticle::rotationVelocity() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle16rotationVelocityEv',
    )

  def rotationVelocityVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickImageParticle::rotationVelocityVariation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#rotationVelocityVariation
    """
    #  qreal QQuickImageParticle::rotationVelocityVariation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle25rotationVelocityVariationEv',
    )

  def autoRotation(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageParticle::autoRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#autoRotation
    """
    #  bool QQuickImageParticle::autoRotation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle12autoRotationEv',
    )

  def xVector(self) -> Optional[QQuickDirection]:
    """
    Calls Qt's 'QQuickDirection *QQuickImageParticle::xVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#xVector

    Returns
    -------

    Optional[QQuickDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDirection *QQuickImageParticle::xVector() const
    address = self.uglySide.call('ritual_ZNK19QQuickImageParticle7xVectorEv')
    from . import QQuickDirection
    return QQuickDirection._cuteAt(address)

  def yVector(self) -> Optional[QQuickDirection]:
    """
    Calls Qt's 'QQuickDirection *QQuickImageParticle::yVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#yVector

    Returns
    -------

    Optional[QQuickDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDirection *QQuickImageParticle::yVector() const
    address = self.uglySide.call('ritual_ZNK19QQuickImageParticle7yVectorEv')
    from . import QQuickDirection
    return QQuickDirection._cuteAt(address)

  def spritesInterpolate(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageParticle::spritesInterpolate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#spritesInterpolate
    """
    #  bool QQuickImageParticle::spritesInterpolate() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle18spritesInterpolateEv',
    )

  def bypassOptimizations(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageParticle::bypassOptimizations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#bypassOptimizations
    """
    #  bool QQuickImageParticle::bypassOptimizations() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle19bypassOptimizationsEv',
    )

  def entryEffect(self) -> EntryEffect:
    """
    Calls Qt's 'EntryEffect QQuickImageParticle::entryEffect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#entryEffect

    Returns
    -------

    EntryEffect
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EntryEffect(number)'
      gives.
    """
    #  EntryEffect QQuickImageParticle::entryEffect() const
    return QQuickImageParticle.EntryEffect(self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle11entryEffectEv',
    ))

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickImageParticle::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickImageParticle::status() const
    return QQuickImageParticle.Status(self.uglySide.call(
        'ritual_ZNK19QQuickImageParticle6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setImage(self, image: QUrl) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setImage(const QUrl &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#setImage

    Parameters
    ----------

    image : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickImageParticle::setImage(const QUrl &image)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle8setImageERK4QUrl',
        self._valueOf(image),
    )

  @overload(QUrl)
  def setColortable(self, table: QUrl) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setColortable(const QUrl &table)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setColortable

    Parameters
    ----------

    table : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickImageParticle::setColortable(const QUrl &table)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle13setColortableERK4QUrl',
        self._valueOf(table),
    )

  @overload(QUrl)
  def setSizetable(self, table: QUrl) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setSizetable(const QUrl &table)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setSizetable

    Parameters
    ----------

    table : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickImageParticle::setSizetable(const QUrl &table)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle12setSizetableERK4QUrl',
        self._valueOf(table),
    )

  @overload(QUrl)
  def setOpacitytable(self, table: QUrl) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setOpacitytable(const QUrl
    &table)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setOpacitytable

    Parameters
    ----------

    table : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickImageParticle::setOpacitytable(const QUrl &table)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle15setOpacitytableERK4QUrl',
        self._valueOf(table),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickImageParticle::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setColorVariation(self, var: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setColorVariation(qreal var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setColorVariation

    Parameters
    ----------

    var : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setColorVariation(qreal var)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle17setColorVariationEd', var,
    )

  @overload(float)
  def setAlphaVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setAlphaVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setAlphaVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setAlphaVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle17setAlphaVariationEd', arg,
    )

  @overload(float)
  def setAlpha(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setAlpha(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#setAlpha

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setAlpha(qreal arg)
    self.uglySide.call('ritual_ZN19QQuickImageParticle8setAlphaEd', arg)

  @overload(float)
  def setRedVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setRedVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setRedVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setRedVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle15setRedVariationEd', arg,
    )

  @overload(float)
  def setGreenVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setGreenVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setGreenVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setGreenVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle17setGreenVariationEd', arg,
    )

  @overload(float)
  def setBlueVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setBlueVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setBlueVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setBlueVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle16setBlueVariationEd', arg,
    )

  @overload(float)
  def setRotation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setRotation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setRotation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setRotation(qreal arg)
    self.uglySide.call('ritual_ZN19QQuickImageParticle11setRotationEd', arg)

  @overload(float)
  def setRotationVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setRotationVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setRotationVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setRotationVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle20setRotationVariationEd', arg,
    )

  @overload(float)
  def setRotationVelocity(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setRotationVelocity(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setRotationVelocity

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setRotationVelocity(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle19setRotationVelocityEd', arg,
    )

  @overload(float)
  def setRotationVelocityVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setRotationVelocityVariation(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::setRotationVelocityVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle28setRotationVelocityVariationEd',
        arg,
    )

  @overload(bool)
  def setAutoRotation(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setAutoRotation(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setAutoRotation

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickImageParticle::setAutoRotation(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle15setAutoRotationEb', arg,
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def setXVector(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setXVector(QQuickDirection *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setXVector

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickImageParticle::setXVector(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle10setXVectorEP15QQuickDirection',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def setYVector(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setYVector(QQuickDirection *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setYVector

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickImageParticle::setYVector(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle10setYVectorEP15QQuickDirection',
        self._addressOf(arg),
    )

  @overload(bool)
  def setSpritesInterpolate(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setSpritesInterpolate(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setSpritesInterpolate

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickImageParticle::setSpritesInterpolate(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle21setSpritesInterpolateEb', arg,
    )

  @overload(bool)
  def setBypassOptimizations(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setBypassOptimizations(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setBypassOptimizations

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickImageParticle::setBypassOptimizations(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle22setBypassOptimizationsEb', arg,
    )

  @overload(EntryEffect)
  def setEntryEffect(self, arg: EntryEffect) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::setEntryEffect(EntryEffect arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#setEntryEffect

    Parameters
    ----------

    arg : EntryEffect
      Passed on as its number.
    """
    #  void QQuickImageParticle::setEntryEffect(EntryEffect arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle14setEntryEffectENS_11EntryEffectE',
        arg.value,
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
    'QQuickImageParticle::QQuickImageParticle(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#QQuickImageParticle

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickImageParticle::QQuickImageParticle(QQuickItem *parent)
    self._noteCreation(QQuickImageParticle, lambda: Rituals.call(
        'ritual_ZN19QQuickImageParticleC1EP10QQuickItem',
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

  def spriteEngine(self) -> Optional[QQuickStochasticEngine]:
    """
    Calls Qt's 'QQuickStochasticEngine *QQuickImageParticle::spriteEngine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#spriteEngine

    Returns
    -------

    Optional[QQuickStochasticEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStochasticEngine *QQuickImageParticle::spriteEngine()
    address = self.uglySide.call(
        'ritual_ZN19QQuickImageParticle12spriteEngineEv',
    )
    from ..QtQuick import QQuickStochasticEngine
    return QQuickStochasticEngine._cuteAt(address)

  def resetColor(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::resetColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#resetColor
    """
    #  void QQuickImageParticle::resetColor()
    self.uglySide.call('ritual_ZN19QQuickImageParticle10resetColorEv')

  def resetRotation(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::resetRotation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#resetRotation
    """
    #  void QQuickImageParticle::resetRotation()
    self.uglySide.call('ritual_ZN19QQuickImageParticle13resetRotationEv')

  def resetDeformation(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::resetDeformation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#resetDeformation
    """
    #  void QQuickImageParticle::resetDeformation()
    self.uglySide.call('ritual_ZN19QQuickImageParticle16resetDeformationEv')

  def imageChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::imageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#imageChanged
    """
    #  void QQuickImageParticle::imageChanged()
    self.uglySide.call('ritual_ZN19QQuickImageParticle12imageChangedEv')

  def colortableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::colortableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#colortableChanged
    """
    #  void QQuickImageParticle::colortableChanged()
    self.uglySide.call('ritual_ZN19QQuickImageParticle17colortableChangedEv')

  def sizetableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::sizetableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#sizetableChanged
    """
    #  void QQuickImageParticle::sizetableChanged()
    self.uglySide.call('ritual_ZN19QQuickImageParticle16sizetableChangedEv')

  def opacitytableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::opacitytableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#opacitytableChanged
    """
    #  void QQuickImageParticle::opacitytableChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle19opacitytableChangedEv',
    )

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#colorChanged
    """
    #  void QQuickImageParticle::colorChanged()
    self.uglySide.call('ritual_ZN19QQuickImageParticle12colorChangedEv')

  def colorVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::colorVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#colorVariationChanged
    """
    #  void QQuickImageParticle::colorVariationChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle21colorVariationChangedEv',
    )

  @overload(float)
  def alphaVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::alphaVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#alphaVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::alphaVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle21alphaVariationChangedEd', arg,
    )

  @overload(float)
  def alphaChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::alphaChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#alphaChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::alphaChanged(qreal arg)
    self.uglySide.call('ritual_ZN19QQuickImageParticle12alphaChangedEd', arg)

  @overload(float)
  def redVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::redVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#redVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::redVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle19redVariationChangedEd', arg,
    )

  @overload(float)
  def greenVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::greenVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#greenVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::greenVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle21greenVariationChangedEd', arg,
    )

  @overload(float)
  def blueVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::blueVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#blueVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::blueVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle20blueVariationChangedEd', arg,
    )

  @overload(float)
  def rotationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::rotationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#rotationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::rotationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle15rotationChangedEd', arg,
    )

  @overload(float)
  def rotationVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::rotationVariationChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#rotationVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::rotationVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle24rotationVariationChangedEd', arg,
    )

  @overload(float)
  def rotationVelocityChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::rotationVelocityChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#rotationVelocityChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::rotationVelocityChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle23rotationVelocityChangedEd', arg,
    )

  @overload(float)
  def rotationVelocityVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void
    QQuickImageParticle::rotationVelocityVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickImageParticle::rotationVelocityVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle32rotationVelocityVariationChangedEd',
        arg,
    )

  @overload(bool)
  def autoRotationChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::autoRotationChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#autoRotationChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickImageParticle::autoRotationChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle19autoRotationChangedEb', arg,
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def xVectorChanged(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::xVectorChanged(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#xVectorChanged

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickImageParticle::xVectorChanged(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle14xVectorChangedEP15QQuickDirection',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def yVectorChanged(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::yVectorChanged(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#yVectorChanged

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickImageParticle::yVectorChanged(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle14yVectorChangedEP15QQuickDirection',
        self._addressOf(arg),
    )

  @overload(bool)
  def spritesInterpolateChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::spritesInterpolateChanged(bool
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#spritesInterpolateChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickImageParticle::spritesInterpolateChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle25spritesInterpolateChangedEb', arg,
    )

  @overload(bool)
  def bypassOptimizationsChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::bypassOptimizationsChanged(bool
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickImageParticle::bypassOptimizationsChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle26bypassOptimizationsChangedEb', arg,
    )

  @overload(EntryEffect)
  def entryEffectChanged(self, arg: EntryEffect) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::entryEffectChanged(EntryEffect
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#entryEffectChanged

    Parameters
    ----------

    arg : EntryEffect
      Passed on as its number.
    """
    #  void QQuickImageParticle::entryEffectChanged(EntryEffect arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle18entryEffectChangedENS_11EntryEffec'
        'tE',
        arg.value,
    )

  @overload(Status)
  def statusChanged(self, arg: Status) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::statusChanged(Status arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#statusChanged

    Parameters
    ----------

    arg : Status
      Passed on as its number.
    """
    #  void QQuickImageParticle::statusChanged(Status arg)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle13statusChangedENS_6StatusE',
        arg.value,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#reset
    """
    #  void QQuickImageParticle::reset()
    ritual = 'ritual_ZN19QQuickImageParticle5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickImageParticle5resetEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def initialize(self, gIdx: int, pIdx: int) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::initialize(int gIdx, int pIdx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#initialize

    Parameters
    ----------

    gIdx : int
      Passed on as it is.

    pIdx : int
      Passed on as it is.
    """
    #  void QQuickImageParticle::initialize(int gIdx, int pIdx)
    ritual = 'ritual_ZN19QQuickImageParticle10initializeEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickImageParticle10initializeEii'
    self.uglySide.call(ritual, gIdx, pIdx)

  @overload(int, int)
  def commit(self, gIdx: int, pIdx: int) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::commit(int gIdx, int pIdx)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageparticle.html#commit

    Parameters
    ----------

    gIdx : int
      Passed on as it is.

    pIdx : int
      Passed on as it is.
    """
    #  void QQuickImageParticle::commit(int gIdx, int pIdx)
    ritual = 'ritual_ZN19QQuickImageParticle6commitEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickImageParticle6commitEii'
    self.uglySide.call(ritual, gIdx, pIdx)

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
    Calls Qt's 'QSGNode *QQuickImageParticle::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#updatePaintNode

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
    #  QSGNode *QQuickImageParticle::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN19QQuickImageParticle15updatePaintNodeEP7QSGNodePN10QQuic'
        'kItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickImageParticle15updatePaintNodeEP7QSGNodePN1'
          '0QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def sceneGraphInvalidated(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::sceneGraphInvalidated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#sceneGraphInvalidated
    """
    #  void QQuickImageParticle::sceneGraphInvalidated()
    ritual = 'ritual_ZN19QQuickImageParticle21sceneGraphInvalidatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickImageParticle21sceneGraphInvalidatedEv'
    self.uglySide.call(ritual)

  def createEngine(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::createEngine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#createEngine
    """
    #  void QQuickImageParticle::createEngine()
    self.uglySide.call('ritual_ZN19QQuickImageParticle12createEngineEv')

  @overload(int)
  def spriteAdvance(self, spriteIndex: int) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::spriteAdvance(int spriteIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#spriteAdvance

    Parameters
    ----------

    spriteIndex : int
      Passed on as it is.
    """
    #  void QQuickImageParticle::spriteAdvance(int spriteIndex)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle13spriteAdvanceEi', spriteIndex,
    )

  @overload()
  @overload(float)
  def spritesUpdate(self, time: float = 0.0) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::spritesUpdate(qreal time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#spritesUpdate

    Parameters
    ----------

    time : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QQuickImageParticle::spritesUpdate(qreal time)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle13spritesUpdateEd', time,
    )

  def mainThreadFetchImageData(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::mainThreadFetchImageData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#mainThreadFetchImageData
    """
    #  void QQuickImageParticle::mainThreadFetchImageData()
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle24mainThreadFetchImageDataEv',
    )

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#invalidateSceneGraph
    """
    #  void QQuickImageParticle::invalidateSceneGraph()
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle20invalidateSceneGraphEv',
    )

  def loadingSomething(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageParticle::loadingSomething()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#loadingSomething
    """
    #  bool QQuickImageParticle::loadingSomething()
    return self.uglySide.call(
        'ritual_ZN19QQuickImageParticle16loadingSomethingEv',
    )

  def clearShadows(self) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::clearShadows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#clearShadows
    """
    #  void QQuickImageParticle::clearShadows()
    self.uglySide.call('ritual_ZN19QQuickImageParticle12clearShadowsEv')

  @overload(QQuickParticleData)
  @overload(NoneType)
  def getShadowDatum(
      self,
      datum: Optional[QQuickParticleData],
  ) -> Optional[QQuickParticleData]:
    """
    Calls Qt's 'QQuickParticleData
    *QQuickImageParticle::getShadowDatum(QQuickParticleData *datum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#getShadowDatum

    Parameters
    ----------

    datum : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickParticleData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleData
    #      *QQuickImageParticle::getShadowDatum(QQuickParticleData *datum)
    address = self.uglySide.call(
        'ritual_ZN19QQuickImageParticle14getShadowDatumEP18QQuickParticleDa'
        'ta',
        self._addressOf(datum),
    )
    from . import QQuickParticleData
    return QQuickParticleData._cuteAt(address)

  @overload(PerformanceLevel)
  def checkPerfLevel(self, level: PerformanceLevel) -> None:
    """
    Calls Qt's 'void QQuickImageParticle::checkPerfLevel(PerformanceLevel
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageparticle.html#checkPerfLevel

    Parameters
    ----------

    level : PerformanceLevel
      Passed on as its number.
    """
    #  void QQuickImageParticle::checkPerfLevel(PerformanceLevel level)
    self.uglySide.call(
        'ritual_ZN19QQuickImageParticle14checkPerfLevelENS_16PerformanceLev'
        'elE',
        level.value,
    )

  @staticmethod
  def buildParticleNodes(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageParticle::buildParticleNodes(QSGNode **a0)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickImageParticle.buildParticleNodes' has no cute function yet. "
        "Qt's 'void QQuickImageParticle::buildParticleNodes(QSGNode **a0)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def finishBuildParticleNodes(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageParticle::finishBuildParticleNodes(QSGNode **n)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickImageParticle.finishBuildParticleNodes' has no cute "
        "function yet. Qt's 'void "
        "QQuickImageParticle::finishBuildParticleNodes(QSGNode **n)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def getState(*__, **_) -> Never:
    """
    Qt's 'ImageMaterialData *QQuickImageParticle::getState(QSGMaterial *m)':
    gives 'ImageMaterialData', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickImageParticle.getState' has no cute function yet. Qt's "
        "'ImageMaterialData *QQuickImageParticle::getState(QSGMaterial "
        "*m)': gives 'ImageMaterialData', which has no cute class yet.")

  @staticmethod
  def initTexCoords(*__, **_) -> Never:
    """
    Qt's 'QQuickImageParticle::initTexCoords': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuickImageParticle.initTexCoords' has no cute function yet. Qt's "
        "'QQuickImageParticle::initTexCoords': a template: a pattern and no "
        "single function.")

  @staticmethod
  def prepareNextFrame(*__, **_) -> Never:
    """
    Qt's 'bool QQuickImageParticle::prepareNextFrame(QSGNode **a0)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickImageParticle.prepareNextFrame' has no cute function yet. "
        "Qt's 'bool QQuickImageParticle::prepareNextFrame(QSGNode **a0)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def sprites(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickSprite> QQuickImageParticle::sprites()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickImageParticle.sprites' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickSprite> QQuickImageParticle::sprites()': "
        "gives a type Python has no way to take yet.")
