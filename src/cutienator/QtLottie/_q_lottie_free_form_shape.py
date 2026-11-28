"""
QLottieFreeFormShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiefreeformshape_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottieFreeFormShape to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonArray, QJsonObject, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieFreeFormShape(QLottieShape):
  """
  The cute side of Qt's QLottieFreeFormShape: a plain Python object standing
  in front of one C++ QLottieFreeFormShape.

  It is built on the cute 'QLottieShape', as Qt's QLottieFreeFormShape is
  built on Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieFreeFormShape around as a copy, so every C++
  QLottieFreeFormShape behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieFreeFormShape that has a ritual and that
  Python can call so far, 10 names in all: 'clone', 'parse',
  'updateProperties', 'acceptsTrim', 'isAnimated', 'buildShape',
  'parseEasedVertices', 'finalizeVertices', 'createKeyframe', 'addCurve'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieFreeFormShape::render(QLottieRenderer &renderer)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QLottieProperty2D<QPointF>
    QLottieFreeFormShape::startPointProperty() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QLottieFreeFormShape::parseShapeKeyframes(QJsonObject
    &keyframes)': takes a type Python has no way to hand over yet.
  - Qt's 'QLottieFreeFormShape::~QLottieFreeFormShape()': the destructor:
    Python removes its C++ QLottieFreeFormShape by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QLottieFreeFormShape is created at the first use, not by
    'QLottieFreeFormShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieFreeFormShape back gives a copy the ritual
    made for Python, in a new cute QLottieFreeFormShape.
  - Each name of Qt's QLottieFreeFormShape that has no cute function yet,
    'parseShapeKeyframes', 'startPointProperty', holds a function that raises
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
  __qt_class__ = 'QLottieFreeFormShape'

  #  Qt's '~QLottieFreeFormShape()'. Naming it makes this a value class:
  #  Python owns every C++ QLottieFreeFormShape behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QLottieFreeFormShapeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieFreeFormShape::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefreeformshape.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieFreeFormShape::clone() const
    ritual = 'ritual_ZNK20QLottieFreeFormShape5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QLottieFreeFormShape5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottieFreeFormShape::acceptsTrim() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#acceptsTrim
    """
    #  bool QLottieFreeFormShape::acceptsTrim() const
    ritual = 'ritual_ZNK20QLottieFreeFormShape11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QLottieFreeFormShape11acceptsTrimEv'
    return self.uglySide.call(ritual)

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QLottieFreeFormShape::isAnimated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#isAnimated
    """
    #  bool QLottieFreeFormShape::isAnimated() const
    ritual = 'ritual_ZNK20QLottieFreeFormShape10isAnimatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QLottieFreeFormShape10isAnimatedEv'
    return self.uglySide.call(ritual)

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

  @overload(THIS)
  def __init__(self, other: QLottieFreeFormShape) -> None:
    """
    Notes what was given, for Qt's
    'QLottieFreeFormShape::QLottieFreeFormShape(const QLottieFreeFormShape
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#QLottieFreeFormShape

    Parameters
    ----------

    other : QLottieFreeFormShape
      Passed on as a value: Qt reads the C++ QLottieFreeFormShape, which
      stays Python's own.
    """
    #  QLottieFreeFormShape::QLottieFreeFormShape(const QLottieFreeFormShape
    #      &other)
    self._noteCreation(QLottieFreeFormShape, lambda: Rituals.call(
        'ritual_ZN20QLottieFreeFormShapeC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottieFreeFormShape::QLottieFreeFormShape(QLottieBase *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#QLottieFreeFormShape

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieFreeFormShape::QLottieFreeFormShape(QLottieBase *parent)
    self._noteCreation(QLottieFreeFormShape, lambda: Rituals.call(
        'ritual_ZN20QLottieFreeFormShapeC1EP11QLottieBase',
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

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieFreeFormShape::parse(const QJsonObject
    &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefreeformshape.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieFreeFormShape::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN20QLottieFreeFormShape5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLottieFreeFormShape5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieFreeFormShape::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieFreeFormShape::updateProperties(int frame)
    ritual = 'ritual_ZN20QLottieFreeFormShape16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QLottieFreeFormShape16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def buildShape(self, keyframe: QJsonObject) -> None:
    """
    Calls Qt's 'void QLottieFreeFormShape::buildShape(const QJsonObject
    &keyframe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#buildShape

    Parameters
    ----------

    keyframe : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QLottieFreeFormShape::buildShape(const QJsonObject &keyframe)
    self.uglySide.call(
        'ritual_ZN20QLottieFreeFormShape10buildShapeERK11QJsonObject',
        self._valueOf(keyframe),
    )

  @overload(int)
  def buildShape(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieFreeFormShape::buildShape(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#buildShape

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieFreeFormShape::buildShape(int frame)
    self.uglySide.call(
        'ritual_ZN20QLottieFreeFormShape10buildShapeEi', frame,
    )

  @overload(QJsonObject, int)
  def parseEasedVertices(
      self,
      keyframe: QJsonObject,
      startFrame: int,
  ) -> None:
    """
    Calls Qt's 'void QLottieFreeFormShape::parseEasedVertices(const
    QJsonObject &keyframe, int startFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#parseEasedVertices

    Parameters
    ----------

    keyframe : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    startFrame : int
      Passed on as it is.
    """
    #  void QLottieFreeFormShape::parseEasedVertices(const QJsonObject
    #      &keyframe, int startFrame)
    self.uglySide.call(
        'ritual_ZN20QLottieFreeFormShape18parseEasedVerticesERK11QJsonObjec'
        'ti',
        self._valueOf(keyframe), startFrame,
    )

  def finalizeVertices(self) -> None:
    """
    Calls Qt's 'void QLottieFreeFormShape::finalizeVertices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#finalizeVertices
    """
    #  void QLottieFreeFormShape::finalizeVertices()
    self.uglySide.call('ritual_ZN20QLottieFreeFormShape16finalizeVerticesEv')

  @overload(QJsonArray, QJsonArray, int, QJsonObject, QJsonObject)
  def createKeyframe(
      self,
      startValue: QJsonArray,
      endValue: QJsonArray,
      startFrame: int,
      easingIn: QJsonObject,
      easingOut: QJsonObject,
  ) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QLottieFreeFormShape::createKeyframe(QJsonArray
    startValue, QJsonArray endValue, int startFrame, QJsonObject easingIn,
    QJsonObject easingOut)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiefreeformshape.html#createKeyframe

    Parameters
    ----------

    startValue : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.

    endValue : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.

    startFrame : int
      Passed on as it is.

    easingIn : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    easingOut : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QLottieFreeFormShape::createKeyframe(QJsonArray
    #      startValue, QJsonArray endValue, int startFrame, QJsonObject
    #      easingIn, QJsonObject easingOut)
    address = self.uglySide.call(
        'ritual_ZN20QLottieFreeFormShape14createKeyframeE10QJsonArrayS0_i11'
        'QJsonObjectS1_',
        self._valueOf(startValue), self._valueOf(endValue), startFrame,
        self._valueOf(easingIn), self._valueOf(easingOut),
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  @overload(QPointF, QPointF, QPointF, QPointF)
  def addCurve(
      self,
      start: QPointF,
      ctlOffset1: QPointF,
      ctlOffset2: QPointF,
      end: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QLottieFreeFormShape::addCurve(QPointF start, QPointF
    ctlOffset1, QPointF ctlOffset2, QPointF end)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiefreeformshape.html#addCurve

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ctlOffset1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ctlOffset2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    end : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLottieFreeFormShape::addCurve(QPointF start, QPointF ctlOffset1,
    #      QPointF ctlOffset2, QPointF end)
    self.uglySide.call(
        'ritual_ZN20QLottieFreeFormShape8addCurveE7QPointFS0_S0_S0_',
        self._valueOf(start, 'QPointF'), self._valueOf(ctlOffset1,
        'QPointF'), self._valueOf(ctlOffset2, 'QPointF'), self._valueOf(end,
        'QPointF'),
    )

  @staticmethod
  def parseShapeKeyframes(*__, **_) -> Never:
    """
    Qt's 'void QLottieFreeFormShape::parseShapeKeyframes(QJsonObject
    &keyframes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieFreeFormShape.parseShapeKeyframes' has no cute function "
        "yet. Qt's 'void "
        "QLottieFreeFormShape::parseShapeKeyframes(QJsonObject "
        "&keyframes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def startPointProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty2D<QPointF>
    QLottieFreeFormShape::startPointProperty() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieFreeFormShape.startPointProperty' has no cute function "
        "yet. Qt's 'QLottieProperty2D<QPointF> "
        "QLottieFreeFormShape::startPointProperty() const': gives a type "
        "Python has no way to take yet.")
