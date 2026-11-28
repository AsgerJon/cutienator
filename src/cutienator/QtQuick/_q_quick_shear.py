"""
QQuickShear binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickShear to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickTransform

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShear(QQuickTransform):
  """
  The cute side of Qt's QQuickShear: a plain Python object standing in front
  of one C++ QQuickShear.

  It is built on the cute 'QQuickTransform', as Qt's QQuickShear is built on
  Qt's QQuickTransform, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShear that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'origin', 'setOrigin',
  'xFactor', 'setXFactor', 'yFactor', 'setYFactor', 'xAngle', 'setXAngle',
  'yAngle', 'setYAngle', 'applyTo', 'originChanged', 'xFactorChanged',
  'yFactorChanged', 'xAngleChanged', 'yAngleChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShear::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickShear::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickShearPrivate *QQuickShear::d_func()': gives
    'QQuickShearPrivate', which has no cute class yet.
  - Qt's 'const QQuickShearPrivate *QQuickShear::d_func() const': gives
    'QQuickShearPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickShear is created at the first use, not by
    'QQuickShear(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShear.
  - Qt tells when it has removed the C++ QQuickShear. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QQuickShear::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#tr

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
    #  QString QQuickShear::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickShear2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShear'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShear::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShear::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickShear10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickShear::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickShear::origin() const
    address = self.uglySide.call('ritual_ZNK11QQuickShear6originEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def xFactor(self) -> float:
    """
    Calls Qt's 'qreal QQuickShear::xFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#xFactor
    """
    #  qreal QQuickShear::xFactor() const
    return self.uglySide.call('ritual_ZNK11QQuickShear7xFactorEv')

  def yFactor(self) -> float:
    """
    Calls Qt's 'qreal QQuickShear::yFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#yFactor
    """
    #  qreal QQuickShear::yFactor() const
    return self.uglySide.call('ritual_ZNK11QQuickShear7yFactorEv')

  def xAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickShear::xAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#xAngle
    """
    #  qreal QQuickShear::xAngle() const
    return self.uglySide.call('ritual_ZNK11QQuickShear6xAngleEv')

  def yAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickShear::yAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#yAngle
    """
    #  qreal QQuickShear::yAngle() const
    return self.uglySide.call('ritual_ZNK11QQuickShear6yAngleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setOrigin(self, point: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickShear::setOrigin(const QVector3D &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#setOrigin

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickShear::setOrigin(const QVector3D &point)
    self.uglySide.call(
        'ritual_ZN11QQuickShear9setOriginERK9QVector3D',
        self._valueOf(point),
    )

  @overload(float)
  def setXFactor(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickShear::setXFactor(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#setXFactor

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickShear::setXFactor(qreal a0)
    self.uglySide.call('ritual_ZN11QQuickShear10setXFactorEd', a0)

  @overload(float)
  def setYFactor(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickShear::setYFactor(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#setYFactor

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickShear::setYFactor(qreal a0)
    self.uglySide.call('ritual_ZN11QQuickShear10setYFactorEd', a0)

  @overload(float)
  def setXAngle(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickShear::setXAngle(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#setXAngle

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickShear::setXAngle(qreal a0)
    self.uglySide.call('ritual_ZN11QQuickShear9setXAngleEd', a0)

  @overload(float)
  def setYAngle(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickShear::setYAngle(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#setYAngle

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickShear::setYAngle(qreal a0)
    self.uglySide.call('ritual_ZN11QQuickShear9setYAngleEd', a0)

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
    Notes what was given, for Qt's 'QQuickShear::QQuickShear(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#QQuickShear

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShear::QQuickShear(QObject *parent)
    self._noteCreation(QQuickShear, lambda: Rituals.call(
        'ritual_ZN11QQuickShearC1EP7QObject',
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

  @overload(QMatrix4x4)
  @overload(NoneType)
  def applyTo(self, matrix: Optional[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QQuickShear::applyTo(QMatrix4x4 *matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#applyTo

    Parameters
    ----------

    matrix : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShear::applyTo(QMatrix4x4 *matrix) const
    ritual = 'ritual_ZNK11QQuickShear7applyToEP10QMatrix4x4'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickShear7applyToEP10QMatrix4x4'
    self.uglySide.call(ritual, self._addressOf(matrix))

  def originChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShear::originChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#originChanged
    """
    #  void QQuickShear::originChanged()
    self.uglySide.call('ritual_ZN11QQuickShear13originChangedEv')

  def xFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShear::xFactorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#xFactorChanged
    """
    #  void QQuickShear::xFactorChanged()
    self.uglySide.call('ritual_ZN11QQuickShear14xFactorChangedEv')

  def yFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShear::yFactorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#yFactorChanged
    """
    #  void QQuickShear::yFactorChanged()
    self.uglySide.call('ritual_ZN11QQuickShear14yFactorChangedEv')

  def xAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShear::xAngleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#xAngleChanged
    """
    #  void QQuickShear::xAngleChanged()
    self.uglySide.call('ritual_ZN11QQuickShear13xAngleChangedEv')

  def yAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShear::yAngleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshear.html#yAngleChanged
    """
    #  void QQuickShear::yAngleChanged()
    self.uglySide.call('ritual_ZN11QQuickShear13yAngleChangedEv')
