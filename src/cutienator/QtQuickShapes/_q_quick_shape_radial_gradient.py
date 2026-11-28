"""
QQuickShapeRadialGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShapeRadialGradient to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class QQuickShapeRadialGradient(QQuickShapeGradient):
  """
  The cute side of Qt's QQuickShapeRadialGradient: a plain Python object
  standing in front of one C++ QQuickShapeRadialGradient.

  It is built on the cute 'QQuickShapeGradient', as Qt's
  QQuickShapeRadialGradient is built on Qt's QQuickShapeGradient, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShapeRadialGradient that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'centerX',
  'setCenterX', 'centerY', 'setCenterY', 'centerRadius', 'setCenterRadius',
  'focalX', 'setFocalX', 'focalY', 'setFocalY', 'focalRadius',
  'setFocalRadius', 'centerXChanged', 'centerYChanged', 'focalXChanged',
  'focalYChanged', 'centerRadiusChanged', 'focalRadiusChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShapeRadialGradient::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickShapeRadialGradient::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickShapeRadialGradient is created at the first use, not by
    'QQuickShapeRadialGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeRadialGradient.
  - Qt tells when it has removed the C++ QQuickShapeRadialGradient. Every
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
    Calls Qt's 'QString QQuickShapeRadialGradient::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshaperadialgradient.html#tr

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
    #  QString QQuickShapeRadialGradient::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickShapeRadialGradient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeRadialGradient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShapeRadialGradient::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShapeRadialGradient::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickShapeRadialGradient10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def centerX(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeRadialGradient::centerX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#centerX
    """
    #  qreal QQuickShapeRadialGradient::centerX() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShapeRadialGradient7centerXEv',
    )

  def centerY(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeRadialGradient::centerY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#centerY
    """
    #  qreal QQuickShapeRadialGradient::centerY() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShapeRadialGradient7centerYEv',
    )

  def centerRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeRadialGradient::centerRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#centerRadius
    """
    #  qreal QQuickShapeRadialGradient::centerRadius() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShapeRadialGradient12centerRadiusEv',
    )

  def focalX(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeRadialGradient::focalX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#focalX
    """
    #  qreal QQuickShapeRadialGradient::focalX() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShapeRadialGradient6focalXEv',
    )

  def focalY(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeRadialGradient::focalY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#focalY
    """
    #  qreal QQuickShapeRadialGradient::focalY() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShapeRadialGradient6focalYEv',
    )

  def focalRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapeRadialGradient::focalRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#focalRadius
    """
    #  qreal QQuickShapeRadialGradient::focalRadius() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShapeRadialGradient11focalRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setCenterX(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::setCenterX(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#setCenterX

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeRadialGradient::setCenterX(qreal v)
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient10setCenterXEd', v,
    )

  @overload(float)
  def setCenterY(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::setCenterY(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#setCenterY

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeRadialGradient::setCenterY(qreal v)
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient10setCenterYEd', v,
    )

  @overload(float)
  def setCenterRadius(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::setCenterRadius(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#setCenterRadius

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeRadialGradient::setCenterRadius(qreal v)
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient15setCenterRadiusEd', v,
    )

  @overload(float)
  def setFocalX(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::setFocalX(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#setFocalX

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeRadialGradient::setFocalX(qreal v)
    self.uglySide.call('ritual_ZN25QQuickShapeRadialGradient9setFocalXEd', v)

  @overload(float)
  def setFocalY(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::setFocalY(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#setFocalY

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeRadialGradient::setFocalY(qreal v)
    self.uglySide.call('ritual_ZN25QQuickShapeRadialGradient9setFocalYEd', v)

  @overload(float)
  def setFocalRadius(self, v: float) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::setFocalRadius(qreal v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#setFocalRadius

    Parameters
    ----------

    v : float
      Passed on as it is.
    """
    #  void QQuickShapeRadialGradient::setFocalRadius(qreal v)
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient14setFocalRadiusEd', v,
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
    'QQuickShapeRadialGradient::QQuickShapeRadialGradient(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShapeRadialGradient::QQuickShapeRadialGradient(QObject *parent)
    self._noteCreation(QQuickShapeRadialGradient, lambda: Rituals.call(
        'ritual_ZN25QQuickShapeRadialGradientC1EP7QObject',
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
    Calls Qt's 'void QQuickShapeRadialGradient::centerXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#centerXChanged
    """
    #  void QQuickShapeRadialGradient::centerXChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient14centerXChangedEv',
    )

  def centerYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::centerYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#centerYChanged
    """
    #  void QQuickShapeRadialGradient::centerYChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient14centerYChangedEv',
    )

  def focalXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::focalXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#focalXChanged
    """
    #  void QQuickShapeRadialGradient::focalXChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient13focalXChangedEv',
    )

  def focalYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::focalYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#focalYChanged
    """
    #  void QQuickShapeRadialGradient::focalYChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient13focalYChangedEv',
    )

  def centerRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::centerRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#centerRadiusChanged
    """
    #  void QQuickShapeRadialGradient::centerRadiusChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient19centerRadiusChangedEv',
    )

  def focalRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapeRadialGradient::focalRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshaperadialgradient.html#focalRadiusChanged
    """
    #  void QQuickShapeRadialGradient::focalRadiusChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickShapeRadialGradient18focalRadiusChangedEv',
    )
