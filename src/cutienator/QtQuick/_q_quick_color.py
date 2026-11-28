"""
QQuickColor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcolor_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickColor to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColor(QObject):
  """
  The cute side of Qt's QQuickColor: a plain Python object standing in front
  of one C++ QQuickColor.

  It is built on the cute 'QObject', as Qt's QQuickColor is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickColor that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'rgba', 'hsla', 'hsva',
  'fromString', 'equal', 'transparent', 'blend', 'darker', 'lighter', 'tint'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColor::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickColor::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickColor::qt_qmlMarker_singleton()': one of Qt's own inner
    workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickColor is created at the first use, not by
    'QQuickColor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColor.
  - Qt tells when it has removed the C++ QQuickColor. Every call on the cute
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
    Calls Qt's 'QString QQuickColor::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#tr

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
    #  QString QQuickColor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickColor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColor'

  #  A C++ QQuickColor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickColor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickColor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColor::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickColor10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(float, float, float, float)
  def rgba(self, r: float, g: float, b: float, a: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::rgba(double r, double g, double b, double
    a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#rgba

    Parameters
    ----------

    r : float
      Passed on as it is.

    g : float
      Passed on as it is.

    b : float
      Passed on as it is.

    a : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::rgba(double r, double g, double b, double a) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor4rgbaEdddd', r, g, b, a,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(float, float, float, float)
  def hsla(self, h: float, s: float, l: float, a: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::hsla(double h, double s, double l, double
    a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#hsla

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    l : float
      Passed on as it is.

    a : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::hsla(double h, double s, double l, double a) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor4hslaEdddd', h, s, l, a,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(float, float, float, float)
  def hsva(self, h: float, s: float, v: float, a: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::hsva(double h, double s, double v, double
    a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#hsva

    Parameters
    ----------

    h : float
      Passed on as it is.

    s : float
      Passed on as it is.

    v : float
      Passed on as it is.

    a : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::hsva(double h, double s, double v, double a) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor4hsvaEdddd', h, s, v, a,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(str)
  def fromString(self, name: str) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::fromString(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#fromString

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::fromString(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor10fromStringERK7QString', name,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QColor, QColor)
  def equal(self, lhs: QColor, rhs: QColor) -> bool:
    """
    Calls Qt's 'bool QQuickColor::equal(const QColor &lhs, const QColor &rhs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#equal

    Parameters
    ----------

    lhs : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    rhs : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  bool QQuickColor::equal(const QColor &lhs, const QColor &rhs) const
    return self.uglySide.call(
        'ritual_ZNK11QQuickColor5equalERK6QColorS2_',
        self._valueOf(lhs), self._valueOf(rhs),
    )

  @overload(QColor, float)
  def transparent(self, color: QColor, opacity: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::transparent(const QColor &color, qreal
    opacity) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#transparent

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    opacity : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::transparent(const QColor &color, qreal opacity)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor11transparentERK6QColord',
        self._valueOf(color), opacity,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QColor, QColor, float)
  def blend(self, a: QColor, b: QColor, factor: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::blend(const QColor &a, const QColor &b,
    qreal factor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#blend

    Parameters
    ----------

    a : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    b : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    factor : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::blend(const QColor &a, const QColor &b, qreal
    #      factor) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor5blendERK6QColorS2_d',
        self._valueOf(a), self._valueOf(b), factor,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QColor, float)
  def darker(self, baseColor: QColor, factor: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::darker(const QColor &baseColor, double
    factor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#darker

    Parameters
    ----------

    baseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    factor : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::darker(const QColor &baseColor, double factor)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor6darkerERK6QColord',
        self._valueOf(baseColor), factor,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QColor, float)
  def lighter(self, baseColor: QColor, factor: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::lighter(const QColor &baseColor, double
    factor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#lighter

    Parameters
    ----------

    baseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    factor : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::lighter(const QColor &baseColor, double factor)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor7lighterERK6QColord',
        self._valueOf(baseColor), factor,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QColor, QColor)
  def tint(self, baseColor: QColor, tintColor: QColor) -> QColor:
    """
    Calls Qt's 'QColor QQuickColor::tint(const QColor &baseColor, const
    QColor &tintColor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#tint

    Parameters
    ----------

    baseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    tintColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColor::tint(const QColor &baseColor, const QColor
    #      &tintColor) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuickColor4tintERK6QColorS2_',
        self._valueOf(baseColor), self._valueOf(tintColor),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QQuickColor::QQuickColor(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolor.html#QQuickColor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColor::QQuickColor(QObject *parent)
    self._noteCreation(QQuickColor, lambda: Rituals.call(
        'ritual_ZN11QQuickColorC1EP7QObject',
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
