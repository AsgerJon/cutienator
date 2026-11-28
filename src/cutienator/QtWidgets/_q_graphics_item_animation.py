"""
QGraphicsItemAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitemanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QTimeLine
  from ..QtGui import QTransform
  from . import QGraphicsItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QPointF = WAIT['QPointF']
  QTimeLine = WAIT['QTimeLine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsItemAnimation(QObject):
  """
  The cute side of Qt's QGraphicsItemAnimation: a plain Python object
  standing in front of one C++ QGraphicsItemAnimation.

  It is built on the cute 'QObject', as Qt's QGraphicsItemAnimation is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsItemAnimation that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr', 'item',
  'setItem', 'timeLine', 'setTimeLine', 'posAt', 'setPosAt', 'transformAt',
  'rotationAt', 'setRotationAt', 'xTranslationAt', 'yTranslationAt',
  'setTranslationAt', 'verticalScaleAt', 'horizontalScaleAt', 'setScaleAt',
  'verticalShearAt', 'horizontalShearAt', 'setShearAt', 'clear', 'setStep',
  'beforeAnimationStep', 'afterAnimationStep'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphicsItemAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGraphicsItemAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsItemAnimation::~QGraphicsItemAnimation()': the destructor:
    Python never removes a C++ QGraphicsItemAnimation.
  - Qt's 'QList<std::pair<qreal, QPointF>> QGraphicsItemAnimation::posList()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<std::pair<qreal, qreal>>
    QGraphicsItemAnimation::rotationList() const': gives a type Python has no
    way to take yet.
  - Qt's 'QList<std::pair<qreal, QPointF>>
    QGraphicsItemAnimation::translationList() const': gives a type Python has
    no way to take yet.
  - Qt's 'QList<std::pair<qreal, QPointF>>
    QGraphicsItemAnimation::scaleList() const': gives a type Python has no
    way to take yet.
  - Qt's 'QList<std::pair<qreal, QPointF>>
    QGraphicsItemAnimation::shearList() const': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsItemAnimation is created at the first use, not by
    'QGraphicsItemAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsItemAnimation.
  - Qt tells when it has removed the C++ QGraphicsItemAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGraphicsItemAnimation that has no cute function yet,
    'posList', 'rotationList', 'scaleList', 'shearList', 'translationList',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QGraphicsItemAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemanimation.html#tr

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
    #  QString QGraphicsItemAnimation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QGraphicsItemAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsItemAnimation'

  #  A C++ QGraphicsItemAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsItemAnimation'

  #  The functions Qt calls itself that QGraphicsItemAnimation is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'beforeAnimationStep': (
          ('_ZN22QGraphicsItemAnimation19beforeAnimationStepEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'afterAnimationStep': (
          ('_ZN22QGraphicsItemAnimation18afterAnimationStepEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsItemAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsItemAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def item(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItemAnimation::item() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemanimation.html#item

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItemAnimation::item() const
    address = self.uglySide.call('ritual_ZNK22QGraphicsItemAnimation4itemEv')
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def timeLine(self) -> Optional[QTimeLine]:
    """
    Calls Qt's 'QTimeLine *QGraphicsItemAnimation::timeLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#timeLine

    Returns
    -------

    Optional[QTimeLine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTimeLine *QGraphicsItemAnimation::timeLine() const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation8timeLineEv',
    )
    from ..QtCore import QTimeLine
    return QTimeLine._cuteAt(address)

  @overload(float)
  def posAt(self, step: float) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItemAnimation::posAt(qreal step) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemanimation.html#posAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItemAnimation::posAt(qreal step) const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation5posAtEd', step,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def transformAt(self, step: float) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsItemAnimation::transformAt(qreal step)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#transformAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsItemAnimation::transformAt(qreal step) const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation11transformAtEd', step,
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @overload(float)
  def rotationAt(self, step: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemAnimation::rotationAt(qreal step) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#rotationAt

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemAnimation::rotationAt(qreal step) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation10rotationAtEd', step,
    )

  @overload(float)
  def xTranslationAt(self, step: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemAnimation::xTranslationAt(qreal step)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#xTranslationAt

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemAnimation::xTranslationAt(qreal step) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation14xTranslationAtEd', step,
    )

  @overload(float)
  def yTranslationAt(self, step: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemAnimation::yTranslationAt(qreal step)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#yTranslationAt

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemAnimation::yTranslationAt(qreal step) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation14yTranslationAtEd', step,
    )

  @overload(float)
  def verticalScaleAt(self, step: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemAnimation::verticalScaleAt(qreal step)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#verticalScaleAt

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemAnimation::verticalScaleAt(qreal step) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation15verticalScaleAtEd', step,
    )

  @overload(float)
  def horizontalScaleAt(self, step: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemAnimation::horizontalScaleAt(qreal step)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#horizontalScaleAt

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemAnimation::horizontalScaleAt(qreal step) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation17horizontalScaleAtEd', step,
    )

  @overload(float)
  def verticalShearAt(self, step: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemAnimation::verticalShearAt(qreal step)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#verticalShearAt

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemAnimation::verticalShearAt(qreal step) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation15verticalShearAtEd', step,
    )

  @overload(float)
  def horizontalShearAt(self, step: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemAnimation::horizontalShearAt(qreal step)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#horizontalShearAt

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemAnimation::horizontalShearAt(qreal step) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsItemAnimation17horizontalShearAtEd', step,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphicsItem)
  @overload(NoneType)
  def setItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setItem(QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemAnimation::setItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN22QGraphicsItemAnimation7setItemEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QTimeLine)
  @overload(NoneType)
  def setTimeLine(self, timeLine: Optional[QTimeLine]) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setTimeLine(QTimeLine
    *timeLine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setTimeLine

    Parameters
    ----------

    timeLine : Optional[QTimeLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemAnimation::setTimeLine(QTimeLine *timeLine)
    self.uglySide.call(
        'ritual_ZN22QGraphicsItemAnimation11setTimeLineEP9QTimeLine',
        self._addressOf(timeLine),
    )

  @overload(float, QPointF)
  def setPosAt(self, step: float, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setPosAt(qreal step, const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setPosAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsItemAnimation::setPosAt(qreal step, const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN22QGraphicsItemAnimation8setPosAtEdRK7QPointF',
        step, self._valueOf(pos, 'QPointF'),
    )

  @overload(float, float)
  def setRotationAt(self, step: float, angle: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setRotationAt(qreal step, qreal
    angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setRotationAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    angle : float
      Passed on as it is.
    """
    #  void QGraphicsItemAnimation::setRotationAt(qreal step, qreal angle)
    self.uglySide.call(
        'ritual_ZN22QGraphicsItemAnimation13setRotationAtEdd', step, angle,
    )

  @overload(float, float, float)
  def setTranslationAt(self, step: float, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setTranslationAt(qreal step,
    qreal dx, qreal dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setTranslationAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QGraphicsItemAnimation::setTranslationAt(qreal step, qreal dx,
    #      qreal dy)
    self.uglySide.call(
        'ritual_ZN22QGraphicsItemAnimation16setTranslationAtEddd',
        step, dx, dy,
    )

  @overload(float, float, float)
  def setScaleAt(self, step: float, sx: float, sy: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setScaleAt(qreal step, qreal sx,
    qreal sy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setScaleAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    sx : float
      Passed on as it is.

    sy : float
      Passed on as it is.
    """
    #  void QGraphicsItemAnimation::setScaleAt(qreal step, qreal sx, qreal
    #      sy)
    self.uglySide.call(
        'ritual_ZN22QGraphicsItemAnimation10setScaleAtEddd', step, sx, sy,
    )

  @overload(float, float, float)
  def setShearAt(self, step: float, sh: float, sv: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setShearAt(qreal step, qreal sh,
    qreal sv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setShearAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    sh : float
      Passed on as it is.

    sv : float
      Passed on as it is.
    """
    #  void QGraphicsItemAnimation::setShearAt(qreal step, qreal sh, qreal
    #      sv)
    self.uglySide.call(
        'ritual_ZN22QGraphicsItemAnimation10setShearAtEddd', step, sh, sv,
    )

  @overload(float)
  def setStep(self, x: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::setStep(qreal x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#setStep

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QGraphicsItemAnimation::setStep(qreal x)
    self.uglySide.call('ritual_ZN22QGraphicsItemAnimation7setStepEd', x)

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
    'QGraphicsItemAnimation::QGraphicsItemAnimation(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#QGraphicsItemAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsItemAnimation::QGraphicsItemAnimation(QObject *parent)
    self._noteCreation(QGraphicsItemAnimation, lambda: Rituals.call(
        'ritual_ZN22QGraphicsItemAnimationC1EP7QObject',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemanimation.html#clear
    """
    #  void QGraphicsItemAnimation::clear()
    self.uglySide.call('ritual_ZN22QGraphicsItemAnimation5clearEv')

  @overload(float)
  def beforeAnimationStep(self, step: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::beforeAnimationStep(qreal
    step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#beforeAnimationStep

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QGraphicsItemAnimation::beforeAnimationStep(qreal step)
    ritual = 'ritual_ZN22QGraphicsItemAnimation19beforeAnimationStepEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsItemAnimation19beforeAnimationStepEd'
    self.uglySide.call(ritual, step)

  @overload(float)
  def afterAnimationStep(self, step: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemAnimation::afterAnimationStep(qreal step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemanimation.html#afterAnimationStep

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QGraphicsItemAnimation::afterAnimationStep(qreal step)
    ritual = 'ritual_ZN22QGraphicsItemAnimation18afterAnimationStepEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsItemAnimation18afterAnimationStepEd'
    self.uglySide.call(ritual, step)

  @staticmethod
  def posList(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<qreal, QPointF>> QGraphicsItemAnimation::posList()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGraphicsItemAnimation.posList' has no cute function yet. Qt's "
        "'QList<std::pair<qreal, QPointF>> "
        "QGraphicsItemAnimation::posList() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def rotationList(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<qreal, qreal>>
    QGraphicsItemAnimation::rotationList() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGraphicsItemAnimation.rotationList' has no cute function yet. "
        "Qt's 'QList<std::pair<qreal, qreal>> "
        "QGraphicsItemAnimation::rotationList() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def scaleList(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<qreal, QPointF>>
    QGraphicsItemAnimation::scaleList() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGraphicsItemAnimation.scaleList' has no cute function yet. Qt's "
        "'QList<std::pair<qreal, QPointF>> "
        "QGraphicsItemAnimation::scaleList() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def shearList(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<qreal, QPointF>>
    QGraphicsItemAnimation::shearList() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGraphicsItemAnimation.shearList' has no cute function yet. Qt's "
        "'QList<std::pair<qreal, QPointF>> "
        "QGraphicsItemAnimation::shearList() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def translationList(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<qreal, QPointF>>
    QGraphicsItemAnimation::translationList() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QGraphicsItemAnimation.translationList' has no cute function yet. "
        "Qt's 'QList<std::pair<qreal, QPointF>> "
        "QGraphicsItemAnimation::translationList() const': gives a type "
        "Python has no way to take yet.")
