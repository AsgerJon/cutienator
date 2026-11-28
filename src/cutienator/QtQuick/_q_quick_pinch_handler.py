"""
QQuickPinchHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpinchhandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPinchHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickMultiPointHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QPointerEvent, QVector2D
  from . import QQuickDragAxis, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPinchHandler(QQuickMultiPointHandler):
  """
  The cute side of Qt's QQuickPinchHandler: a plain Python object standing in
  front of one C++ QQuickPinchHandler.

  It is built on the cute 'QQuickMultiPointHandler', as Qt's
  QQuickPinchHandler is built on Qt's QQuickMultiPointHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPinchHandler that has a ritual and that Python
  can call so far, 39 names in all: 'metaObject', 'tr', 'xAxis', 'yAxis',
  'translation', 'activeTranslation', 'persistentTranslation',
  'setPersistentTranslation', 'scaleAxis', 'minimumScale', 'setMinimumScale',
  'maximumScale', 'setMaximumScale', 'scale', 'activeScale',
  'setActiveScale', 'persistentScale', 'setPersistentScale', 'rotationAxis',
  'minimumRotation', 'setMinimumRotation', 'maximumRotation',
  'setMaximumRotation', 'rotation', 'activeRotation', 'setActiveRotation',
  'persistentRotation', 'setPersistentRotation', 'minimumScaleChanged',
  'maximumScaleChanged', 'minimumRotationChanged', 'maximumRotationChanged',
  'updated', 'scaleChanged', 'rotationChanged', 'translationChanged',
  'wantsPointerEvent', 'onActiveChanged', 'handlePointerEventImpl'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPinchHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPinchHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 44 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPinchHandler is created at the first use, not by
    'QQuickPinchHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPinchHandler.
  - Qt tells when it has removed the C++ QQuickPinchHandler. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickPinchHandler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#tr

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
    #  QString QQuickPinchHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickPinchHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPinchHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPinchHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPinchHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def translation(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickPinchHandler::translation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#translation

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickPinchHandler::translation() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler11translationEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def activeTranslation(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchHandler::activeTranslation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#activeTranslation

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchHandler::activeTranslation() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler17activeTranslationEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def persistentTranslation(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPinchHandler::persistentTranslation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#persistentTranslation

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPinchHandler::persistentTranslation() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler21persistentTranslationEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def minimumScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::minimumScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#minimumScale
    """
    #  qreal QQuickPinchHandler::minimumScale() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler12minimumScaleEv',
    )

  def maximumScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::maximumScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#maximumScale
    """
    #  qreal QQuickPinchHandler::maximumScale() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler12maximumScaleEv',
    )

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#scale
    """
    #  qreal QQuickPinchHandler::scale() const
    return self.uglySide.call('ritual_ZNK18QQuickPinchHandler5scaleEv')

  def activeScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::activeScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#activeScale
    """
    #  qreal QQuickPinchHandler::activeScale() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler11activeScaleEv',
    )

  def persistentScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::persistentScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#persistentScale
    """
    #  qreal QQuickPinchHandler::persistentScale() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler15persistentScaleEv',
    )

  def minimumRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::minimumRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#minimumRotation
    """
    #  qreal QQuickPinchHandler::minimumRotation() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler15minimumRotationEv',
    )

  def maximumRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::maximumRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#maximumRotation
    """
    #  qreal QQuickPinchHandler::maximumRotation() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler15maximumRotationEv',
    )

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#rotation
    """
    #  qreal QQuickPinchHandler::rotation() const
    return self.uglySide.call('ritual_ZNK18QQuickPinchHandler8rotationEv')

  def activeRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::activeRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#activeRotation
    """
    #  qreal QQuickPinchHandler::activeRotation() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler14activeRotationEv',
    )

  def persistentRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPinchHandler::persistentRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#persistentRotation
    """
    #  qreal QQuickPinchHandler::persistentRotation() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPinchHandler18persistentRotationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPersistentTranslation(self, trans: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setPersistentTranslation(const
    QPointF &trans)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setPersistentTranslation

    Parameters
    ----------

    trans : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPinchHandler::setPersistentTranslation(const QPointF
    #      &trans)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler24setPersistentTranslationERK7QPointF',
        self._valueOf(trans, 'QPointF'),
    )

  @overload(float)
  def setMinimumScale(self, minimumScale: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setMinimumScale(qreal
    minimumScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setMinimumScale

    Parameters
    ----------

    minimumScale : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setMinimumScale(qreal minimumScale)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler15setMinimumScaleEd', minimumScale,
    )

  @overload(float)
  def setMaximumScale(self, maximumScale: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setMaximumScale(qreal
    maximumScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setMaximumScale

    Parameters
    ----------

    maximumScale : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setMaximumScale(qreal maximumScale)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler15setMaximumScaleEd', maximumScale,
    )

  @overload(float)
  def setActiveScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setActiveScale(qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setActiveScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setActiveScale(qreal scale)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler14setActiveScaleEd', scale,
    )

  @overload(float)
  def setPersistentScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setPersistentScale(qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setPersistentScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setPersistentScale(qreal scale)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler18setPersistentScaleEd', scale,
    )

  @overload(float)
  def setMinimumRotation(self, minimumRotation: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setMinimumRotation(qreal
    minimumRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setMinimumRotation

    Parameters
    ----------

    minimumRotation : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setMinimumRotation(qreal minimumRotation)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler18setMinimumRotationEd',
        minimumRotation,
    )

  @overload(float)
  def setMaximumRotation(self, maximumRotation: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setMaximumRotation(qreal
    maximumRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setMaximumRotation

    Parameters
    ----------

    maximumRotation : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setMaximumRotation(qreal maximumRotation)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler18setMaximumRotationEd',
        maximumRotation,
    )

  @overload(float)
  def setActiveRotation(self, rot: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setActiveRotation(qreal rot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setActiveRotation

    Parameters
    ----------

    rot : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setActiveRotation(qreal rot)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler17setActiveRotationEd', rot,
    )

  @overload(float)
  def setPersistentRotation(self, rot: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::setPersistentRotation(qreal rot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#setPersistentRotation

    Parameters
    ----------

    rot : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::setPersistentRotation(qreal rot)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler21setPersistentRotationEd', rot,
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
    'QQuickPinchHandler::QQuickPinchHandler(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#QQuickPinchHandler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPinchHandler::QQuickPinchHandler(QQuickItem *parent)
    self._noteCreation(QQuickPinchHandler, lambda: Rituals.call(
        'ritual_ZN18QQuickPinchHandlerC1EP10QQuickItem',
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

  def xAxis(self) -> Optional[QQuickDragAxis]:
    """
    Calls Qt's 'QQuickDragAxis *QQuickPinchHandler::xAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#xAxis

    Returns
    -------

    Optional[QQuickDragAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAxis *QQuickPinchHandler::xAxis()
    address = self.uglySide.call('ritual_ZN18QQuickPinchHandler5xAxisEv')
    from . import QQuickDragAxis
    return QQuickDragAxis._cuteAt(address)

  def yAxis(self) -> Optional[QQuickDragAxis]:
    """
    Calls Qt's 'QQuickDragAxis *QQuickPinchHandler::yAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#yAxis

    Returns
    -------

    Optional[QQuickDragAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAxis *QQuickPinchHandler::yAxis()
    address = self.uglySide.call('ritual_ZN18QQuickPinchHandler5yAxisEv')
    from . import QQuickDragAxis
    return QQuickDragAxis._cuteAt(address)

  def scaleAxis(self) -> Optional[QQuickDragAxis]:
    """
    Calls Qt's 'QQuickDragAxis *QQuickPinchHandler::scaleAxis()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#scaleAxis

    Returns
    -------

    Optional[QQuickDragAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAxis *QQuickPinchHandler::scaleAxis()
    address = self.uglySide.call('ritual_ZN18QQuickPinchHandler9scaleAxisEv')
    from . import QQuickDragAxis
    return QQuickDragAxis._cuteAt(address)

  def rotationAxis(self) -> Optional[QQuickDragAxis]:
    """
    Calls Qt's 'QQuickDragAxis *QQuickPinchHandler::rotationAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#rotationAxis

    Returns
    -------

    Optional[QQuickDragAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAxis *QQuickPinchHandler::rotationAxis()
    address = self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler12rotationAxisEv',
    )
    from . import QQuickDragAxis
    return QQuickDragAxis._cuteAt(address)

  def minimumScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::minimumScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#minimumScaleChanged
    """
    #  void QQuickPinchHandler::minimumScaleChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler19minimumScaleChangedEv',
    )

  def maximumScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::maximumScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#maximumScaleChanged
    """
    #  void QQuickPinchHandler::maximumScaleChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler19maximumScaleChangedEv',
    )

  def minimumRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::minimumRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#minimumRotationChanged
    """
    #  void QQuickPinchHandler::minimumRotationChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler22minimumRotationChangedEv',
    )

  def maximumRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::maximumRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#maximumRotationChanged
    """
    #  void QQuickPinchHandler::maximumRotationChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler22maximumRotationChangedEv',
    )

  def updated(self) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::updated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchhandler.html#updated
    """
    #  void QQuickPinchHandler::updated()
    self.uglySide.call('ritual_ZN18QQuickPinchHandler7updatedEv')

  @overload(float)
  def scaleChanged(self, delta: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::scaleChanged(qreal delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#scaleChanged

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::scaleChanged(qreal delta)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler12scaleChangedEd', delta,
    )

  @overload(float)
  def rotationChanged(self, delta: float) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::rotationChanged(qreal delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#rotationChanged

    Parameters
    ----------

    delta : float
      Passed on as it is.
    """
    #  void QQuickPinchHandler::rotationChanged(qreal delta)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler15rotationChangedEd', delta,
    )

  @overload(QVector2D)
  def translationChanged(self, delta: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::translationChanged(QVector2D
    delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#translationChanged

    Parameters
    ----------

    delta : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickPinchHandler::translationChanged(QVector2D delta)
    self.uglySide.call(
        'ritual_ZN18QQuickPinchHandler18translationChangedE9QVector2D',
        self._valueOf(delta),
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickPinchHandler::wantsPointerEvent(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPinchHandler::wantsPointerEvent(QPointerEvent *event)
    ritual = (
        'ritual_ZN18QQuickPinchHandler17wantsPointerEventEP13QPointerEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPinchHandler17wantsPointerEventEP13QPointer'
          'Event')
    return self.uglySide.call(ritual, self._addressOf(event))

  def onActiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::onActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#onActiveChanged
    """
    #  void QQuickPinchHandler::onActiveChanged()
    ritual = 'ritual_ZN18QQuickPinchHandler15onActiveChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPinchHandler15onActiveChangedEv'
    self.uglySide.call(ritual)

  @overload(QPointerEvent)
  @overload(NoneType)
  def handlePointerEventImpl(self, event: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void QQuickPinchHandler::handlePointerEventImpl(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchhandler.html#handlePointerEventImpl

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPinchHandler::handlePointerEventImpl(QPointerEvent *event)
    ritual = (
        'ritual_ZN18QQuickPinchHandler22handlePointerEventImplEP13QPointerE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPinchHandler22handlePointerEventImplEP13QPo'
          'interEvent')
    self.uglySide.call(ritual, self._addressOf(event))
