"""
QQuickCurve binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickCurve to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickPathElement

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickCurve(QQuickPathElement):
  """
  The cute side of Qt's QQuickCurve: a plain Python object standing in front
  of one C++ QQuickCurve.

  It is built on the cute 'QQuickPathElement', as Qt's QQuickCurve is built
  on Qt's QQuickPathElement, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickCurve that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'x', 'setX', 'hasX', 'y',
  'setY', 'hasY', 'relativeX', 'setRelativeX', 'hasRelativeX', 'relativeY',
  'setRelativeY', 'hasRelativeY', 'xChanged', 'yChanged', 'relativeXChanged',
  'relativeYChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickCurve::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickCurve::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickCurve::qt_qmlMarker_anonymous()': one of Qt's own inner
    workings.
  - Qt's 'void QQuickCurve::addToPath(QPainterPath &a0, const QQuickPathData
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDebug operator<<(QDebug debug, const QQuickCurve *curve)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickCurve is created at the first use, not by
    'QQuickCurve(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCurve.
  - Qt tells when it has removed the C++ QQuickCurve. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickCurve that has no cute function yet, 'addToPath',
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
    Calls Qt's 'QString QQuickCurve::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#tr

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
    #  QString QQuickCurve::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickCurve2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCurve'

  #  The functions Qt calls itself that QQuickCurve is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'addToPath': (
          'void QQuickCurve::addToPath(QPainterPath &, const '
          'QQuickPathData &)',
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
    Calls Qt's 'const QMetaObject *QQuickCurve::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickCurve::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickCurve10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickCurve::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#x
    """
    #  qreal QQuickCurve::x() const
    return self.uglySide.call('ritual_ZNK11QQuickCurve1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickCurve::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#y
    """
    #  qreal QQuickCurve::y() const
    return self.uglySide.call('ritual_ZNK11QQuickCurve1yEv')

  def relativeX(self) -> float:
    """
    Calls Qt's 'qreal QQuickCurve::relativeX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#relativeX
    """
    #  qreal QQuickCurve::relativeX() const
    return self.uglySide.call('ritual_ZNK11QQuickCurve9relativeXEv')

  def relativeY(self) -> float:
    """
    Calls Qt's 'qreal QQuickCurve::relativeY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#relativeY
    """
    #  qreal QQuickCurve::relativeY() const
    return self.uglySide.call('ritual_ZNK11QQuickCurve9relativeYEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickCurve::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickCurve::setX(qreal x)
    self.uglySide.call('ritual_ZN11QQuickCurve4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickCurve::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickCurve::setY(qreal y)
    self.uglySide.call('ritual_ZN11QQuickCurve4setYEd', y)

  @overload(float)
  def setRelativeX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickCurve::setRelativeX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#setRelativeX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickCurve::setRelativeX(qreal x)
    self.uglySide.call('ritual_ZN11QQuickCurve12setRelativeXEd', x)

  @overload(float)
  def setRelativeY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickCurve::setRelativeY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#setRelativeY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickCurve::setRelativeY(qreal y)
    self.uglySide.call('ritual_ZN11QQuickCurve12setRelativeYEd', y)

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
    Notes what was given, for Qt's 'QQuickCurve::QQuickCurve(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#QQuickCurve

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickCurve::QQuickCurve(QObject *parent)
    self._noteCreation(QQuickCurve, lambda: Rituals.call(
        'ritual_ZN11QQuickCurveC1EP7QObject',
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

  def hasX(self) -> bool:
    """
    Calls Qt's 'bool QQuickCurve::hasX()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#hasX
    """
    #  bool QQuickCurve::hasX()
    return self.uglySide.call('ritual_ZN11QQuickCurve4hasXEv')

  def hasY(self) -> bool:
    """
    Calls Qt's 'bool QQuickCurve::hasY()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#hasY
    """
    #  bool QQuickCurve::hasY()
    return self.uglySide.call('ritual_ZN11QQuickCurve4hasYEv')

  def hasRelativeX(self) -> bool:
    """
    Calls Qt's 'bool QQuickCurve::hasRelativeX()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#hasRelativeX
    """
    #  bool QQuickCurve::hasRelativeX()
    return self.uglySide.call('ritual_ZN11QQuickCurve12hasRelativeXEv')

  def hasRelativeY(self) -> bool:
    """
    Calls Qt's 'bool QQuickCurve::hasRelativeY()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#hasRelativeY
    """
    #  bool QQuickCurve::hasRelativeY()
    return self.uglySide.call('ritual_ZN11QQuickCurve12hasRelativeYEv')

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCurve::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#xChanged
    """
    #  void QQuickCurve::xChanged()
    self.uglySide.call('ritual_ZN11QQuickCurve8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCurve::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#yChanged
    """
    #  void QQuickCurve::yChanged()
    self.uglySide.call('ritual_ZN11QQuickCurve8yChangedEv')

  def relativeXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCurve::relativeXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#relativeXChanged
    """
    #  void QQuickCurve::relativeXChanged()
    self.uglySide.call('ritual_ZN11QQuickCurve16relativeXChangedEv')

  def relativeYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCurve::relativeYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcurve.html#relativeYChanged
    """
    #  void QQuickCurve::relativeYChanged()
    self.uglySide.call('ritual_ZN11QQuickCurve16relativeYChangedEv')

  @staticmethod
  def addToPath(*__, **_) -> Never:
    """
    Qt's 'void QQuickCurve::addToPath(QPainterPath &a0, const QQuickPathData
    &a1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickCurve.addToPath' has no cute function yet. Qt's 'void "
        "QQuickCurve::addToPath(QPainterPath &a0, const QQuickPathData "
        "&a1)': takes a type Python has no way to hand over yet.")
