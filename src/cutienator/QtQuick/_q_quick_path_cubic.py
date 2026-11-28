"""
QQuickPathCubic binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathCubic to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickCurve

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathCubic(QQuickCurve):
  """
  The cute side of Qt's QQuickPathCubic: a plain Python object standing in
  front of one C++ QQuickPathCubic.

  It is built on the cute 'QQuickCurve', as Qt's QQuickPathCubic is built on
  Qt's QQuickCurve, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathCubic that has a ritual and that Python
  can call so far, 30 names in all: 'metaObject', 'tr', 'control1X',
  'setControl1X', 'control1Y', 'setControl1Y', 'control2X', 'setControl2X',
  'control2Y', 'setControl2Y', 'relativeControl1X', 'setRelativeControl1X',
  'hasRelativeControl1X', 'relativeControl1Y', 'setRelativeControl1Y',
  'hasRelativeControl1Y', 'relativeControl2X', 'setRelativeControl2X',
  'hasRelativeControl2X', 'relativeControl2Y', 'setRelativeControl2Y',
  'hasRelativeControl2Y', 'control1XChanged', 'control1YChanged',
  'control2XChanged', 'control2YChanged', 'relativeControl1XChanged',
  'relativeControl1YChanged', 'relativeControl2XChanged',
  'relativeControl2YChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathCubic::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPathCubic::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathCubic::addToPath(QPainterPath &path, const
    QQuickPathData &a1)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathCubic is created at the first use, not by
    'QQuickPathCubic(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathCubic.
  - Qt tells when it has removed the C++ QQuickPathCubic. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickPathCubic::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#tr

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
    #  QString QQuickPathCubic::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickPathCubic2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathCubic'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathCubic::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathCubic::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickPathCubic10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def control1X(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::control1X() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#control1X
    """
    #  qreal QQuickPathCubic::control1X() const
    return self.uglySide.call('ritual_ZNK15QQuickPathCubic9control1XEv')

  def control1Y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::control1Y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#control1Y
    """
    #  qreal QQuickPathCubic::control1Y() const
    return self.uglySide.call('ritual_ZNK15QQuickPathCubic9control1YEv')

  def control2X(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::control2X() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#control2X
    """
    #  qreal QQuickPathCubic::control2X() const
    return self.uglySide.call('ritual_ZNK15QQuickPathCubic9control2XEv')

  def control2Y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::control2Y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#control2Y
    """
    #  qreal QQuickPathCubic::control2Y() const
    return self.uglySide.call('ritual_ZNK15QQuickPathCubic9control2YEv')

  def relativeControl1X(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::relativeControl1X() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl1X
    """
    #  qreal QQuickPathCubic::relativeControl1X() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickPathCubic17relativeControl1XEv',
    )

  def relativeControl1Y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::relativeControl1Y() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl1Y
    """
    #  qreal QQuickPathCubic::relativeControl1Y() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickPathCubic17relativeControl1YEv',
    )

  def relativeControl2X(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::relativeControl2X() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl2X
    """
    #  qreal QQuickPathCubic::relativeControl2X() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickPathCubic17relativeControl2XEv',
    )

  def relativeControl2Y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathCubic::relativeControl2Y() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl2Y
    """
    #  qreal QQuickPathCubic::relativeControl2Y() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickPathCubic17relativeControl2YEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setControl1X(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setControl1X(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#setControl1X

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setControl1X(qreal x)
    self.uglySide.call('ritual_ZN15QQuickPathCubic12setControl1XEd', x)

  @overload(float)
  def setControl1Y(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setControl1Y(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#setControl1Y

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setControl1Y(qreal y)
    self.uglySide.call('ritual_ZN15QQuickPathCubic12setControl1YEd', y)

  @overload(float)
  def setControl2X(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setControl2X(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#setControl2X

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setControl2X(qreal x)
    self.uglySide.call('ritual_ZN15QQuickPathCubic12setControl2XEd', x)

  @overload(float)
  def setControl2Y(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setControl2Y(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathcubic.html#setControl2Y

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setControl2Y(qreal y)
    self.uglySide.call('ritual_ZN15QQuickPathCubic12setControl2YEd', y)

  @overload(float)
  def setRelativeControl1X(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setRelativeControl1X(qreal x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#setRelativeControl1X

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setRelativeControl1X(qreal x)
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20setRelativeControl1XEd', x,
    )

  @overload(float)
  def setRelativeControl1Y(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setRelativeControl1Y(qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#setRelativeControl1Y

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setRelativeControl1Y(qreal y)
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20setRelativeControl1YEd', y,
    )

  @overload(float)
  def setRelativeControl2X(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setRelativeControl2X(qreal x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#setRelativeControl2X

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setRelativeControl2X(qreal x)
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20setRelativeControl2XEd', x,
    )

  @overload(float)
  def setRelativeControl2Y(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::setRelativeControl2Y(qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#setRelativeControl2Y

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPathCubic::setRelativeControl2Y(qreal y)
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20setRelativeControl2YEd', y,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickPathCubic::QQuickPathCubic(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#QQuickPathCubic

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathCubic::QQuickPathCubic(QObject *parent)
    self._noteCreation(QQuickPathCubic, lambda: Rituals.call(
        'ritual_ZN15QQuickPathCubicC1EP7QObject',
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

  def hasRelativeControl1X(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathCubic::hasRelativeControl1X()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#hasRelativeControl1X
    """
    #  bool QQuickPathCubic::hasRelativeControl1X()
    return self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20hasRelativeControl1XEv',
    )

  def hasRelativeControl1Y(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathCubic::hasRelativeControl1Y()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#hasRelativeControl1Y
    """
    #  bool QQuickPathCubic::hasRelativeControl1Y()
    return self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20hasRelativeControl1YEv',
    )

  def hasRelativeControl2X(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathCubic::hasRelativeControl2X()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#hasRelativeControl2X
    """
    #  bool QQuickPathCubic::hasRelativeControl2X()
    return self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20hasRelativeControl2XEv',
    )

  def hasRelativeControl2Y(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathCubic::hasRelativeControl2Y()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#hasRelativeControl2Y
    """
    #  bool QQuickPathCubic::hasRelativeControl2Y()
    return self.uglySide.call(
        'ritual_ZN15QQuickPathCubic20hasRelativeControl2YEv',
    )

  def control1XChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::control1XChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#control1XChanged
    """
    #  void QQuickPathCubic::control1XChanged()
    self.uglySide.call('ritual_ZN15QQuickPathCubic16control1XChangedEv')

  def control1YChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::control1YChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#control1YChanged
    """
    #  void QQuickPathCubic::control1YChanged()
    self.uglySide.call('ritual_ZN15QQuickPathCubic16control1YChangedEv')

  def control2XChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::control2XChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#control2XChanged
    """
    #  void QQuickPathCubic::control2XChanged()
    self.uglySide.call('ritual_ZN15QQuickPathCubic16control2XChangedEv')

  def control2YChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::control2YChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#control2YChanged
    """
    #  void QQuickPathCubic::control2YChanged()
    self.uglySide.call('ritual_ZN15QQuickPathCubic16control2YChangedEv')

  def relativeControl1XChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::relativeControl1XChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl1XChanged
    """
    #  void QQuickPathCubic::relativeControl1XChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic24relativeControl1XChangedEv',
    )

  def relativeControl1YChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::relativeControl1YChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl1YChanged
    """
    #  void QQuickPathCubic::relativeControl1YChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic24relativeControl1YChangedEv',
    )

  def relativeControl2XChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::relativeControl2XChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl2XChanged
    """
    #  void QQuickPathCubic::relativeControl2XChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic24relativeControl2XChangedEv',
    )

  def relativeControl2YChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathCubic::relativeControl2YChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathcubic.html#relativeControl2YChanged
    """
    #  void QQuickPathCubic::relativeControl2YChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickPathCubic24relativeControl2YChangedEv',
    )
