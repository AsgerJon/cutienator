"""
QQuickScale binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickScale to be private: it declares the class in a header it
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


class QQuickScale(QQuickTransform):
  """
  The cute side of Qt's QQuickScale: a plain Python object standing in front
  of one C++ QQuickScale.

  It is built on the cute 'QQuickTransform', as Qt's QQuickScale is built on
  Qt's QQuickTransform, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScale that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'origin', 'setOrigin',
  'xScale', 'setXScale', 'yScale', 'setYScale', 'zScale', 'setZScale',
  'applyTo', 'originChanged', 'xScaleChanged', 'yScaleChanged',
  'zScaleChanged', 'scaleChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScale::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickScale::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickScalePrivate *QQuickScale::d_func()': gives
    'QQuickScalePrivate', which has no cute class yet.
  - Qt's 'const QQuickScalePrivate *QQuickScale::d_func() const': gives
    'QQuickScalePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickScale is created at the first use, not by
    'QQuickScale(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScale.
  - Qt tells when it has removed the C++ QQuickScale. Every call on the cute
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
    Calls Qt's 'QString QQuickScale::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#tr

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
    #  QString QQuickScale::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickScale2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScale'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScale::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScale::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickScale10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickScale::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickScale::origin() const
    address = self.uglySide.call('ritual_ZNK11QQuickScale6originEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def xScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickScale::xScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#xScale
    """
    #  qreal QQuickScale::xScale() const
    return self.uglySide.call('ritual_ZNK11QQuickScale6xScaleEv')

  def yScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickScale::yScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#yScale
    """
    #  qreal QQuickScale::yScale() const
    return self.uglySide.call('ritual_ZNK11QQuickScale6yScaleEv')

  def zScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickScale::zScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#zScale
    """
    #  qreal QQuickScale::zScale() const
    return self.uglySide.call('ritual_ZNK11QQuickScale6zScaleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setOrigin(self, point: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickScale::setOrigin(const QVector3D &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#setOrigin

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickScale::setOrigin(const QVector3D &point)
    self.uglySide.call(
        'ritual_ZN11QQuickScale9setOriginERK9QVector3D',
        self._valueOf(point),
    )

  @overload(float)
  def setXScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickScale::setXScale(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#setXScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickScale::setXScale(qreal a0)
    self.uglySide.call('ritual_ZN11QQuickScale9setXScaleEd', a0)

  @overload(float)
  def setYScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickScale::setYScale(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#setYScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickScale::setYScale(qreal a0)
    self.uglySide.call('ritual_ZN11QQuickScale9setYScaleEd', a0)

  @overload(float)
  def setZScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickScale::setZScale(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#setZScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickScale::setZScale(qreal a0)
    self.uglySide.call('ritual_ZN11QQuickScale9setZScaleEd', a0)

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
    Notes what was given, for Qt's 'QQuickScale::QQuickScale(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#QQuickScale

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScale::QQuickScale(QObject *parent)
    self._noteCreation(QQuickScale, lambda: Rituals.call(
        'ritual_ZN11QQuickScaleC1EP7QObject',
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
    Calls Qt's 'void QQuickScale::applyTo(QMatrix4x4 *matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#applyTo

    Parameters
    ----------

    matrix : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScale::applyTo(QMatrix4x4 *matrix) const
    ritual = 'ritual_ZNK11QQuickScale7applyToEP10QMatrix4x4'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickScale7applyToEP10QMatrix4x4'
    self.uglySide.call(ritual, self._addressOf(matrix))

  def originChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScale::originChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#originChanged
    """
    #  void QQuickScale::originChanged()
    self.uglySide.call('ritual_ZN11QQuickScale13originChangedEv')

  def xScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScale::xScaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#xScaleChanged
    """
    #  void QQuickScale::xScaleChanged()
    self.uglySide.call('ritual_ZN11QQuickScale13xScaleChangedEv')

  def yScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScale::yScaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#yScaleChanged
    """
    #  void QQuickScale::yScaleChanged()
    self.uglySide.call('ritual_ZN11QQuickScale13yScaleChangedEv')

  def zScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScale::zScaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#zScaleChanged
    """
    #  void QQuickScale::zScaleChanged()
    self.uglySide.call('ritual_ZN11QQuickScale13zScaleChangedEv')

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScale::scaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscale.html#scaleChanged
    """
    #  void QQuickScale::scaleChanged()
    self.uglySide.call('ritual_ZN11QQuickScale12scaleChangedEv')
