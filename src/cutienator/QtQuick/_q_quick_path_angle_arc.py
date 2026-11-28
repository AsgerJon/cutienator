"""
QQuickPathAngleArc binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathAngleArc to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QQuickPathAngleArc(QQuickCurve):
  """
  The cute side of Qt's QQuickPathAngleArc: a plain Python object standing in
  front of one C++ QQuickPathAngleArc.

  It is built on the cute 'QQuickCurve', as Qt's QQuickPathAngleArc is built
  on Qt's QQuickCurve, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathAngleArc that has a ritual and that Python
  can call so far, 23 names in all: 'metaObject', 'tr', 'centerX',
  'setCenterX', 'centerY', 'setCenterY', 'radiusX', 'setRadiusX', 'radiusY',
  'setRadiusY', 'startAngle', 'setStartAngle', 'sweepAngle', 'setSweepAngle',
  'moveToStart', 'setMoveToStart', 'centerXChanged', 'centerYChanged',
  'radiusXChanged', 'radiusYChanged', 'startAngleChanged',
  'sweepAngleChanged', 'moveToStartChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathAngleArc::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPathAngleArc::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathAngleArc::addToPath(QPainterPath &path, const
    QQuickPathData &a1)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathAngleArc is created at the first use, not by
    'QQuickPathAngleArc(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathAngleArc.
  - Qt tells when it has removed the C++ QQuickPathAngleArc. Every call on
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
    Calls Qt's 'QString QQuickPathAngleArc::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#tr

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
    #  QString QQuickPathAngleArc::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickPathAngleArc2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathAngleArc'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathAngleArc::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathAngleArc::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPathAngleArc10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def centerX(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathAngleArc::centerX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#centerX
    """
    #  qreal QQuickPathAngleArc::centerX() const
    return self.uglySide.call('ritual_ZNK18QQuickPathAngleArc7centerXEv')

  def centerY(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathAngleArc::centerY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#centerY
    """
    #  qreal QQuickPathAngleArc::centerY() const
    return self.uglySide.call('ritual_ZNK18QQuickPathAngleArc7centerYEv')

  def radiusX(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathAngleArc::radiusX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#radiusX
    """
    #  qreal QQuickPathAngleArc::radiusX() const
    return self.uglySide.call('ritual_ZNK18QQuickPathAngleArc7radiusXEv')

  def radiusY(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathAngleArc::radiusY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#radiusY
    """
    #  qreal QQuickPathAngleArc::radiusY() const
    return self.uglySide.call('ritual_ZNK18QQuickPathAngleArc7radiusYEv')

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathAngleArc::startAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#startAngle
    """
    #  qreal QQuickPathAngleArc::startAngle() const
    return self.uglySide.call('ritual_ZNK18QQuickPathAngleArc10startAngleEv')

  def sweepAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathAngleArc::sweepAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#sweepAngle
    """
    #  qreal QQuickPathAngleArc::sweepAngle() const
    return self.uglySide.call('ritual_ZNK18QQuickPathAngleArc10sweepAngleEv')

  def moveToStart(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathAngleArc::moveToStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#moveToStart
    """
    #  bool QQuickPathAngleArc::moveToStart() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPathAngleArc11moveToStartEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setCenterX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::setCenterX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#setCenterX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAngleArc::setCenterX(qreal a0)
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc10setCenterXEd', a0)

  @overload(float)
  def setCenterY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::setCenterY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#setCenterY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAngleArc::setCenterY(qreal a0)
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc10setCenterYEd', a0)

  @overload(float)
  def setRadiusX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::setRadiusX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#setRadiusX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAngleArc::setRadiusX(qreal a0)
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc10setRadiusXEd', a0)

  @overload(float)
  def setRadiusY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::setRadiusY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanglearc.html#setRadiusY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAngleArc::setRadiusY(qreal a0)
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc10setRadiusYEd', a0)

  @overload(float)
  def setStartAngle(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::setStartAngle(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#setStartAngle

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAngleArc::setStartAngle(qreal a0)
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc13setStartAngleEd', a0)

  @overload(float)
  def setSweepAngle(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::setSweepAngle(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#setSweepAngle

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAngleArc::setSweepAngle(qreal a0)
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc13setSweepAngleEd', a0)

  @overload(bool)
  def setMoveToStart(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::setMoveToStart(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#setMoveToStart

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickPathAngleArc::setMoveToStart(bool a0)
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc14setMoveToStartEb', a0)

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
    'QQuickPathAngleArc::QQuickPathAngleArc(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#QQuickPathAngleArc

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathAngleArc::QQuickPathAngleArc(QObject *parent)
    self._noteCreation(QQuickPathAngleArc, lambda: Rituals.call(
        'ritual_ZN18QQuickPathAngleArcC1EP7QObject',
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

  def centerXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::centerXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#centerXChanged
    """
    #  void QQuickPathAngleArc::centerXChanged()
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc14centerXChangedEv')

  def centerYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::centerYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#centerYChanged
    """
    #  void QQuickPathAngleArc::centerYChanged()
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc14centerYChangedEv')

  def radiusXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::radiusXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#radiusXChanged
    """
    #  void QQuickPathAngleArc::radiusXChanged()
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc14radiusXChangedEv')

  def radiusYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::radiusYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#radiusYChanged
    """
    #  void QQuickPathAngleArc::radiusYChanged()
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc14radiusYChangedEv')

  def startAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::startAngleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#startAngleChanged
    """
    #  void QQuickPathAngleArc::startAngleChanged()
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc17startAngleChangedEv')

  def sweepAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::sweepAngleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#sweepAngleChanged
    """
    #  void QQuickPathAngleArc::sweepAngleChanged()
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc17sweepAngleChangedEv')

  def moveToStartChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAngleArc::moveToStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanglearc.html#moveToStartChanged
    """
    #  void QQuickPathAngleArc::moveToStartChanged()
    self.uglySide.call('ritual_ZN18QQuickPathAngleArc18moveToStartChangedEv')
