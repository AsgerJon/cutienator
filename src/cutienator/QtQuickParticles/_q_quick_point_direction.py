"""
QQuickPointDirection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickpointdirection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPointDirection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickDirection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPointDirection(QQuickDirection):
  """
  The cute side of Qt's QQuickPointDirection: a plain Python object standing
  in front of one C++ QQuickPointDirection.

  It is built on the cute 'QQuickDirection', as Qt's QQuickPointDirection is
  built on Qt's QQuickDirection, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPointDirection that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'sample', 'x',
  'y', 'xVariation', 'yVariation', 'xChanged', 'yChanged',
  'xVariationChanged', 'yVariationChanged', 'setX', 'setY', 'setXVariation',
  'setYVariation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPointDirection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPointDirection::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPointDirection is created at the first use, not by
    'QQuickPointDirection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPointDirection.
  - Qt tells when it has removed the C++ QQuickPointDirection. Every call on
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
    Calls Qt's 'QString QQuickPointDirection::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#tr

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
    #  QString QQuickPointDirection::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickPointDirection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPointDirection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPointDirection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPointDirection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickPointDirection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickPointDirection::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#x
    """
    #  qreal QQuickPointDirection::x() const
    return self.uglySide.call('ritual_ZNK20QQuickPointDirection1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPointDirection::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#y
    """
    #  qreal QQuickPointDirection::y() const
    return self.uglySide.call('ritual_ZNK20QQuickPointDirection1yEv')

  def xVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPointDirection::xVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#xVariation
    """
    #  qreal QQuickPointDirection::xVariation() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickPointDirection10xVariationEv',
    )

  def yVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPointDirection::yVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#yVariation
    """
    #  qreal QQuickPointDirection::yVariation() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickPointDirection10yVariationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::setX(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#setX

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::setX(qreal arg)
    self.uglySide.call('ritual_ZN20QQuickPointDirection4setXEd', arg)

  @overload(float)
  def setY(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::setY(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#setY

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::setY(qreal arg)
    self.uglySide.call('ritual_ZN20QQuickPointDirection4setYEd', arg)

  @overload(float)
  def setXVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::setXVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#setXVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::setXVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickPointDirection13setXVariationEd', arg,
    )

  @overload(float)
  def setYVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::setYVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#setYVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::setYVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickPointDirection13setYVariationEd', arg,
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
    Notes what was given, for Qt's
    'QQuickPointDirection::QQuickPointDirection(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#QQuickPointDirection

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPointDirection::QQuickPointDirection(QObject *parent)
    self._noteCreation(QQuickPointDirection, lambda: Rituals.call(
        'ritual_ZN20QQuickPointDirectionC1EP7QObject',
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

  @overload(QPointF)
  def sample(self, from_: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPointDirection::sample(const QPointF &from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#sample

    Parameters
    ----------

    from_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPointDirection::sample(const QPointF &from)
    ritual = 'ritual_ZN20QQuickPointDirection6sampleERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickPointDirection6sampleERK7QPointF'
    address = self.uglySide.call(ritual, self._valueOf(from_, 'QPointF'))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def xChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::xChanged(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#xChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::xChanged(qreal arg)
    self.uglySide.call('ritual_ZN20QQuickPointDirection8xChangedEd', arg)

  @overload(float)
  def yChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::yChanged(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointdirection.html#yChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::yChanged(qreal arg)
    self.uglySide.call('ritual_ZN20QQuickPointDirection8yChangedEd', arg)

  @overload(float)
  def xVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::xVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#xVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::xVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickPointDirection17xVariationChangedEd', arg,
    )

  @overload(float)
  def yVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickPointDirection::yVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointdirection.html#yVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickPointDirection::yVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickPointDirection17yVariationChangedEd', arg,
    )
