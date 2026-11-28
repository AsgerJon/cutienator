"""
QQuickShapeConicalGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShapeConicalGradient to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickShapeGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeConicalGradient(QQuickShapeGradient):
  """
  The cute side of Qt's QQuickShapeConicalGradient: a plain Python object
  standing in front of one C++ QQuickShapeConicalGradient.

  It is built on the cute 'QQuickShapeGradient', as Qt's
  QQuickShapeConicalGradient is built on Qt's QQuickShapeGradient, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShapeConicalGradient that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'centerX', 'setCenterX', 'centerY', 'setCenterY', 'angle', 'setAngle',
  'centerXChanged', 'centerYChanged', 'angleChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShapeConicalGradient::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickShapeConicalGradient::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickShapeConicalGradient is created at the first use, not by
    'QQuickShapeConicalGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeConicalGradient.
  - Qt tells when it has removed the C++ QQuickShapeConicalGradient. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickShapeConicalGradient::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#tr

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
    #  QString QQuickShapeConicalGradient::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuickShapeConicalGradient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeConicalGradient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShapeConicalGradient::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShapeConicalGradient::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickShapeConicalGradient10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def centerX(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeConicalGradient::centerX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#centerX
    """
    #  qreal QQuickShapeConicalGradient::centerX() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickShapeConicalGradient7centerXEv',
    )

  def centerY(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeConicalGradient::centerY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#centerY
    """
    #  qreal QQuickShapeConicalGradient::centerY() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickShapeConicalGradient7centerYEv',
    )

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeConicalGradient::angle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#angle
    """
    #  qreal QQuickShapeConicalGradient::angle() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickShapeConicalGradient5angleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setCenterX(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeConicalGradient::setCenterX(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#setCenterX

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeConicalGradient::setCenterX(qreal v)
    self.uglySide.call(
        'ritual_ZN26QQuickShapeConicalGradient10setCenterXEd', v,
    )

  @overload(float)
  def setCenterY(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeConicalGradient::setCenterY(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#setCenterY

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeConicalGradient::setCenterY(qreal v)
    self.uglySide.call(
        'ritual_ZN26QQuickShapeConicalGradient10setCenterYEd', v,
    )

  @overload(float)
  def setAngle(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeConicalGradient::setAngle(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#setAngle

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeConicalGradient::setAngle(qreal v)
    self.uglySide.call('ritual_ZN26QQuickShapeConicalGradient8setAngleEd', v)

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
    'QQuickShapeConicalGradient::QQuickShapeConicalGradient(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShapeConicalGradient::QQuickShapeConicalGradient(QObject
    #      *parent)
    self._noteCreation(QQuickShapeConicalGradient, lambda: Rituals.call(
        'ritual_ZN26QQuickShapeConicalGradientC1EP7QObject',
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
    Calls Qt's 'void QQuickShapeConicalGradient::centerXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#centerXChanged
    """
    #  void QQuickShapeConicalGradient::centerXChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickShapeConicalGradient14centerXChangedEv',
    )

  def centerYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapeConicalGradient::centerYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#centerYChanged
    """
    #  void QQuickShapeConicalGradient::centerYChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickShapeConicalGradient14centerYChangedEv',
    )

  def angleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapeConicalGradient::angleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeconicalgradient.html#angleChanged
    """
    #  void QQuickShapeConicalGradient::angleChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickShapeConicalGradient12angleChangedEv',
    )
