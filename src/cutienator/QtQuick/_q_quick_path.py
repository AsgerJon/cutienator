"""
QQuickPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPath to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QSizeF
  from ..QtGui import QPainterPath
  from . import QQuickPathPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPath(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickPath: a plain Python object standing in front
  of one C++ QQuickPath.

  It is built on the cute 'QObject', as Qt's QQuickPath is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickPath is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPath that has a ritual and that Python can
  call so far, 38 names in all: 'metaObject', 'tr', 'startX', 'setStartX',
  'hasStartX', 'startY', 'setStartY', 'hasStartY', 'isClosed', 'path',
  'setPath', 'attributes', 'attributeAt', 'pointAtPercent',
  'invalidateSequentialHistory', 'scale', 'setScale', 'simplify',
  'setSimplify', 'isAsynchronous', 'setAsynchronous', 'processPath',
  'changed', 'startXChanged', 'startYChanged', 'simplifyChanged',
  'scaleChanged', 'asynchronousChanged', 'componentComplete', 'classBegin',
  'disconnectPathElements', 'connectPathElements', 'gatherAttributes',
  'doProcessPath', 'interpolate', 'endpoint', 'createPointCache', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPath::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPath::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPath::~QQuickPath()': the destructor: Python never removes a
    C++ QQuickPath.
  - Qt's 'QQmlListProperty<QQuickPathElement> QQuickPath::pathElements()':
    gives a type Python has no way to take yet.
  - Qt's 'QPointF QQuickPath::sequentialPointAt(qreal p, qreal *angle)
    const': takes a number to change where it is.
  - Qt's 'QQuickPath::QQuickPath(QQuickPathPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQuickPathElement
    *QQuickPath::pathElements_at(QQmlListProperty<QQuickPathElement> *a0,
    qsizetype a1)': names 'QQmlListProperty<QQuickPathElement>', which has no
    cute class yet.
  - Qt's 'void
    QQuickPath::pathElements_append(QQmlListProperty<QQuickPathElement> *a0,
    QQuickPathElement *a1)': names 'QQmlListProperty<QQuickPathElement>',
    which has no cute class yet.
  - Qt's 'qsizetype
    QQuickPath::pathElements_count(QQmlListProperty<QQuickPathElement> *a0)':
    names 'QQmlListProperty<QQuickPathElement>', which has no cute class yet.
  - Qt's 'void
    QQuickPath::pathElements_clear(QQmlListProperty<QQuickPathElement> *a0)':
    names 'QQmlListProperty<QQuickPathElement>', which has no cute class yet.
  - Qt's 'void
    QQuickPath::pathElements_replace(QQmlListProperty<QQuickPathElement> *a0,
    qsizetype a1, QQuickPathElement *a2)': names
    'QQmlListProperty<QQuickPathElement>', which has no cute class yet.
  - Qt's 'void
    QQuickPath::pathElements_removeLast(QQmlListProperty<QQuickPathElement>
    *a0)': names 'QQmlListProperty<QQuickPathElement>', which has no cute
    class yet.
  - Qt's 'void QQuickPath::interpolate(QList<AttributePoint> &points, int
    idx, const QString &name, qreal value)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QQuickPath::endpoint(QList<AttributePoint> &attributePoints,
    const QString &name)': takes a type Python has no way to hand over yet.
  - Qt's 'QPointF QQuickPath::forwardsPointAt(const QPainterPath &path, const
    qreal &pathLength, const QList<AttributePoint> &attributePoints,
    QQuickCachedBezier &prevBez, qreal p, qreal *angle)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QPointF QQuickPath::backwardsPointAt(const QPainterPath &path,
    const qreal &pathLength, const QList<AttributePoint> &attributePoints,
    QQuickCachedBezier &prevBez, qreal p, qreal *angle)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QQuickPathPrivate *QQuickPath::d_func() const': takes in
    Python what 'QQuickPathPrivate *QQuickPath::d_func()' takes.
  - Qt's 'QPainterPath QQuickPath::createPath(const QPointF &startPoint,
    const QPointF &endPoint, const QStringList &attributes, qreal
    &pathLength, QList<AttributePoint> &attributePoints, bool *closed)':
    takes a number to change where it is.
  - Qt's 'QPainterPath QQuickPath::createShapePath(const QPointF &startPoint,
    const QPointF &endPoint, qreal &pathLength, bool *closed)': takes a
    number to change where it is.
  - Qt's 'QPointF QQuickPath::sequentialPointAt(const QPainterPath &path,
    const qreal &pathLength, const QList<AttributePoint> &attributePoints,
    QQuickCachedBezier &prevBez, qreal p, qreal *angle)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 63 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPath is created at the first use, not by 'QQuickPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPath.
  - Qt tells when it has removed the C++ QQuickPath. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickPath that has no cute function yet,
    'backwardsPointAt', 'createPath', 'createShapePath', 'forwardsPointAt',
    'pathElements', 'pathElements_append', 'pathElements_at',
    'pathElements_clear', 'pathElements_count', 'pathElements_removeLast',
    'pathElements_replace', 'sequentialPointAt', holds a function that raises
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
    Calls Qt's 'QString QQuickPath::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#tr

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
    #  QString QQuickPath::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickPath2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPath'

  #  Qt's QQuickPath is built on more than one class. The part of a C++
  #  QQuickPath that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickPath_QQmlParserStatus',
  }

  #  A C++ QQuickPath Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPath'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPath::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPath::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickPath10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def startX(self) -> float:
    """
    Calls Qt's 'qreal QQuickPath::startX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#startX
    """
    #  qreal QQuickPath::startX() const
    return self.uglySide.call('ritual_ZNK10QQuickPath6startXEv')

  def hasStartX(self) -> bool:
    """
    Calls Qt's 'bool QQuickPath::hasStartX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#hasStartX
    """
    #  bool QQuickPath::hasStartX() const
    return self.uglySide.call('ritual_ZNK10QQuickPath9hasStartXEv')

  def startY(self) -> float:
    """
    Calls Qt's 'qreal QQuickPath::startY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#startY
    """
    #  qreal QQuickPath::startY() const
    return self.uglySide.call('ritual_ZNK10QQuickPath6startYEv')

  def hasStartY(self) -> bool:
    """
    Calls Qt's 'bool QQuickPath::hasStartY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#hasStartY
    """
    #  bool QQuickPath::hasStartY() const
    return self.uglySide.call('ritual_ZNK10QQuickPath9hasStartYEv')

  def isClosed(self) -> bool:
    """
    Calls Qt's 'bool QQuickPath::isClosed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#isClosed
    """
    #  bool QQuickPath::isClosed() const
    return self.uglySide.call('ritual_ZNK10QQuickPath8isClosedEv')

  def path(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QQuickPath::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#path

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QQuickPath::path() const
    address = self.uglySide.call('ritual_ZNK10QQuickPath4pathEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def attributes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickPath::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#attributes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickPath::attributes() const
    address = self.uglySide.call('ritual_ZNK10QQuickPath10attributesEv')
    return QStringList._cuteOwning(address)

  @overload(str, float)
  def attributeAt(self, a0: str, a1: float) -> float:
    """
    Calls Qt's 'qreal QQuickPath::attributeAt(const QString &a0, qreal a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#attributeAt

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : float
      Passed on as it is.
    """
    #  qreal QQuickPath::attributeAt(const QString &a0, qreal a1) const
    return self.uglySide.call(
        'ritual_ZNK10QQuickPath11attributeAtERK7QStringd', a0, a1,
    )

  @overload(float)
  def pointAtPercent(self, t: float) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPath::pointAtPercent(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#pointAtPercent

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPath::pointAtPercent(qreal t) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickPath14pointAtPercentEd', t,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scale(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickPath::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#scale

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickPath::scale() const
    address = self.uglySide.call('ritual_ZNK10QQuickPath5scaleEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def simplify(self) -> bool:
    """
    Calls Qt's 'bool QQuickPath::simplify() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#simplify
    """
    #  bool QQuickPath::simplify() const
    return self.uglySide.call('ritual_ZNK10QQuickPath8simplifyEv')

  def isAsynchronous(self) -> bool:
    """
    Calls Qt's 'bool QQuickPath::isAsynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#isAsynchronous
    """
    #  bool QQuickPath::isAsynchronous() const
    return self.uglySide.call('ritual_ZNK10QQuickPath14isAsynchronousEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStartX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPath::setStartX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#setStartX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPath::setStartX(qreal x)
    self.uglySide.call('ritual_ZN10QQuickPath9setStartXEd', x)

  @overload(float)
  def setStartY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPath::setStartY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#setStartY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPath::setStartY(qreal y)
    self.uglySide.call('ritual_ZN10QQuickPath9setStartYEd', y)

  @overload(QPainterPath)
  def setPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QQuickPath::setPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#setPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QQuickPath::setPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN10QQuickPath7setPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(QSizeF)
  def setScale(self, scale: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickPath::setScale(const QSizeF &scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#setScale

    Parameters
    ----------

    scale : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickPath::setScale(const QSizeF &scale)
    self.uglySide.call(
        'ritual_ZN10QQuickPath8setScaleERK6QSizeF', self._valueOf(scale),
    )

  @overload(bool)
  def setSimplify(self, s: bool) -> None:
    """
    Calls Qt's 'void QQuickPath::setSimplify(bool s)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#setSimplify

    Parameters
    ----------

    s : bool
      Passed on as it is.
    """
    #  void QQuickPath::setSimplify(bool s)
    self.uglySide.call('ritual_ZN10QQuickPath11setSimplifyEb', s)

  @overload(bool)
  def setAsynchronous(self, a: bool) -> None:
    """
    Calls Qt's 'void QQuickPath::setAsynchronous(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#setAsynchronous

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QQuickPath::setAsynchronous(bool a)
    self.uglySide.call('ritual_ZN10QQuickPath15setAsynchronousEb', a)

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
    Notes what was given, for Qt's 'QQuickPath::QQuickPath(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#QQuickPath

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPath::QQuickPath(QObject *parent)
    self._noteCreation(QQuickPath, lambda: Rituals.call(
        'ritual_ZN10QQuickPathC1EP7QObject',
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

  def invalidateSequentialHistory(self) -> None:
    """
    Calls Qt's 'void QQuickPath::invalidateSequentialHistory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpath.html#invalidateSequentialHistory
    """
    #  void QQuickPath::invalidateSequentialHistory() const
    self.uglySide.call(
        'ritual_ZNK10QQuickPath27invalidateSequentialHistoryEv',
    )

  def processPath(self) -> None:
    """
    Calls Qt's 'void QQuickPath::processPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#processPath
    """
    #  void QQuickPath::processPath()
    self.uglySide.call('ritual_ZN10QQuickPath11processPathEv')

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuickPath::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#changed
    """
    #  void QQuickPath::changed()
    self.uglySide.call('ritual_ZN10QQuickPath7changedEv')

  def startXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPath::startXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#startXChanged
    """
    #  void QQuickPath::startXChanged()
    self.uglySide.call('ritual_ZN10QQuickPath13startXChangedEv')

  def startYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPath::startYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#startYChanged
    """
    #  void QQuickPath::startYChanged()
    self.uglySide.call('ritual_ZN10QQuickPath13startYChangedEv')

  def simplifyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPath::simplifyChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#simplifyChanged
    """
    #  void QQuickPath::simplifyChanged()
    self.uglySide.call('ritual_ZN10QQuickPath15simplifyChangedEv')

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPath::scaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#scaleChanged
    """
    #  void QQuickPath::scaleChanged()
    self.uglySide.call('ritual_ZN10QQuickPath12scaleChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPath::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpath.html#asynchronousChanged
    """
    #  void QQuickPath::asynchronousChanged()
    self.uglySide.call('ritual_ZN10QQuickPath19asynchronousChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickPath::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#componentComplete
    """
    #  void QQuickPath::componentComplete()
    ritual = 'ritual_ZN10QQuickPath17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickPath17componentCompleteEv'
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickPath::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#classBegin
    """
    #  void QQuickPath::classBegin()
    ritual = 'ritual_ZN10QQuickPath10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickPath10classBeginEv'
    self.uglySide.call(ritual)

  def disconnectPathElements(self) -> None:
    """
    Calls Qt's 'void QQuickPath::disconnectPathElements()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpath.html#disconnectPathElements
    """
    #  void QQuickPath::disconnectPathElements()
    self.uglySide.call('ritual_ZN10QQuickPath22disconnectPathElementsEv')

  def connectPathElements(self) -> None:
    """
    Calls Qt's 'void QQuickPath::connectPathElements()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpath.html#connectPathElements
    """
    #  void QQuickPath::connectPathElements()
    self.uglySide.call('ritual_ZN10QQuickPath19connectPathElementsEv')

  def gatherAttributes(self) -> None:
    """
    Calls Qt's 'void QQuickPath::gatherAttributes()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#gatherAttributes
    """
    #  void QQuickPath::gatherAttributes()
    self.uglySide.call('ritual_ZN10QQuickPath16gatherAttributesEv')

  def doProcessPath(self) -> None:
    """
    Calls Qt's 'void QQuickPath::doProcessPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#doProcessPath
    """
    #  void QQuickPath::doProcessPath()
    self.uglySide.call('ritual_ZN10QQuickPath13doProcessPathEv')

  @overload(int, str, float)
  def interpolate(self, idx: int, name: str, value: float) -> None:
    """
    Calls Qt's 'void QQuickPath::interpolate(int idx, const QString &name,
    qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#interpolate

    Parameters
    ----------

    idx : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : float
      Passed on as it is.
    """
    #  void QQuickPath::interpolate(int idx, const QString &name, qreal
    #      value)
    self.uglySide.call(
        'ritual_ZN10QQuickPath11interpolateEiRK7QStringd', idx, name, value,
    )

  @overload(str)
  def endpoint(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickPath::endpoint(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#endpoint

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPath::endpoint(const QString &name)
    self.uglySide.call('ritual_ZN10QQuickPath8endpointERK7QString', name)

  def createPointCache(self) -> None:
    """
    Calls Qt's 'void QQuickPath::createPointCache() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#createPointCache
    """
    #  void QQuickPath::createPointCache() const
    self.uglySide.call('ritual_ZNK10QQuickPath16createPointCacheEv')

  def d_func(self) -> Optional[QQuickPathPrivate]:
    """
    Calls Qt's 'QQuickPathPrivate *QQuickPath::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpath.html#d_func

    Returns
    -------

    Optional[QQuickPathPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathPrivate *QQuickPath::d_func()
    address = self.uglySide.call('ritual_ZN10QQuickPath6d_funcEv')
    from . import QQuickPathPrivate
    return QQuickPathPrivate._cuteAt(address)

  @staticmethod
  def backwardsPointAt(*__, **_) -> Never:
    """
    Qt's 'QPointF QQuickPath::backwardsPointAt(const QPainterPath &path,
    const qreal &pathLength, const QList<AttributePoint> &attributePoints,
    QQuickCachedBezier &prevBez, qreal p, qreal *angle)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPath.backwardsPointAt' has no cute function yet. Qt's "
        "'QPointF QQuickPath::backwardsPointAt(const QPainterPath &path, "
        "const qreal &pathLength, const QList<AttributePoint> "
        "&attributePoints, QQuickCachedBezier &prevBez, qreal p, qreal "
        "*angle)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createPath(*__, **_) -> Never:
    """
    Qt's 'QPainterPath QQuickPath::createPath(const QPointF &startPoint,
    const QPointF &endPoint, const QStringList &attributes, qreal
    &pathLength, QList<AttributePoint> &attributePoints, bool *closed)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickPath.createPath' has no cute function yet. Qt's "
        "'QPainterPath QQuickPath::createPath(const QPointF &startPoint, "
        "const QPointF &endPoint, const QStringList &attributes, qreal "
        "&pathLength, QList<AttributePoint> &attributePoints, bool "
        "*closed)': takes a number to change where it is.")

  @staticmethod
  def createShapePath(*__, **_) -> Never:
    """
    Qt's 'QPainterPath QQuickPath::createShapePath(const QPointF &startPoint,
    const QPointF &endPoint, qreal &pathLength, bool *closed)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickPath.createShapePath' has no cute function yet. Qt's "
        "'QPainterPath QQuickPath::createShapePath(const QPointF "
        "&startPoint, const QPointF &endPoint, qreal &pathLength, bool "
        "*closed)': takes a number to change where it is.")

  @staticmethod
  def forwardsPointAt(*__, **_) -> Never:
    """
    Qt's 'QPointF QQuickPath::forwardsPointAt(const QPainterPath &path, const
    qreal &pathLength, const QList<AttributePoint> &attributePoints,
    QQuickCachedBezier &prevBez, qreal p, qreal *angle)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPath.forwardsPointAt' has no cute function yet. Qt's "
        "'QPointF QQuickPath::forwardsPointAt(const QPainterPath &path, "
        "const qreal &pathLength, const QList<AttributePoint> "
        "&attributePoints, QQuickCachedBezier &prevBez, qreal p, qreal "
        "*angle)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def pathElements(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickPathElement> QQuickPath::pathElements()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPath.pathElements' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickPathElement> QQuickPath::pathElements()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def pathElements_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickPath::pathElements_append(QQmlListProperty<QQuickPathElement> *a0,
    QQuickPathElement *a1)': names 'QQmlListProperty<QQuickPathElement>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickPath.pathElements_append' has no cute function yet. Qt's "
        "'void "
        "QQuickPath::pathElements_append(QQmlListProperty<QQuickPathElement>"
        " *a0, QQuickPathElement *a1)': names "
        "'QQmlListProperty<QQuickPathElement>', which has no cute class yet."
    )

  @staticmethod
  def pathElements_at(*__, **_) -> Never:
    """
    Qt's 'QQuickPathElement
    *QQuickPath::pathElements_at(QQmlListProperty<QQuickPathElement> *a0,
    qsizetype a1)': names 'QQmlListProperty<QQuickPathElement>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickPath.pathElements_at' has no cute function yet. Qt's "
        "'QQuickPathElement "
        "*QQuickPath::pathElements_at(QQmlListProperty<QQuickPathElement> "
        "*a0, qsizetype a1)': names 'QQmlListProperty<QQuickPathElement>', "
        "which has no cute class yet.")

  @staticmethod
  def pathElements_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickPath::pathElements_clear(QQmlListProperty<QQuickPathElement> *a0)':
    names 'QQmlListProperty<QQuickPathElement>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickPath.pathElements_clear' has no cute function yet. Qt's "
        "'void "
        "QQuickPath::pathElements_clear(QQmlListProperty<QQuickPathElement> "
        "*a0)': names 'QQmlListProperty<QQuickPathElement>', which has no "
        "cute class yet.")

  @staticmethod
  def pathElements_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickPath::pathElements_count(QQmlListProperty<QQuickPathElement> *a0)':
    names 'QQmlListProperty<QQuickPathElement>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickPath.pathElements_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickPath::pathElements_count(QQmlListProperty<QQuickPathElement> "
        "*a0)': names 'QQmlListProperty<QQuickPathElement>', which has no "
        "cute class yet.")

  @staticmethod
  def pathElements_removeLast(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickPath::pathElements_removeLast(QQmlListProperty<QQuickPathElement>
    *a0)': names 'QQmlListProperty<QQuickPathElement>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickPath.pathElements_removeLast' has no cute function yet. "
        "Qt's 'void "
        "QQuickPath::pathElements_removeLast(QQmlListProperty<QQuickPathElem"
        "ent> *a0)': names 'QQmlListProperty<QQuickPathElement>', which has "
        "no cute class yet.")

  @staticmethod
  def pathElements_replace(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickPath::pathElements_replace(QQmlListProperty<QQuickPathElement> *a0,
    qsizetype a1, QQuickPathElement *a2)': names
    'QQmlListProperty<QQuickPathElement>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickPath.pathElements_replace' has no cute function yet. Qt's "
        "'void "
        "QQuickPath::pathElements_replace(QQmlListProperty<QQuickPathElement"
        "> *a0, qsizetype a1, QQuickPathElement *a2)': names "
        "'QQmlListProperty<QQuickPathElement>', which has no cute class yet."
    )

  @staticmethod
  def sequentialPointAt(*__, **_) -> Never:
    """
    - Qt's 'QPointF QQuickPath::sequentialPointAt(qreal p, qreal *angle)
      const': takes a number to change where it is.
    - Qt's 'QPointF QQuickPath::sequentialPointAt(const QPainterPath &path,
      const qreal &pathLength, const QList<AttributePoint> &attributePoints,
      QQuickCachedBezier &prevBez, qreal p, qreal *angle)': takes a type
      Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPath.sequentialPointAt' has no cute function yet. Qt's "
        "'QPointF QQuickPath::sequentialPointAt(qreal p, qreal *angle) "
        "const': takes a number to change where it is. Qt's 'QPointF "
        "QQuickPath::sequentialPointAt(const QPainterPath &path, const "
        "qreal &pathLength, const QList<AttributePoint> &attributePoints, "
        "QQuickCachedBezier &prevBez, qreal p, qreal *angle)': takes a type "
        "Python has no way to hand over yet.")
