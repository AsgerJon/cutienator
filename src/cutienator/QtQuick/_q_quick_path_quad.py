"""
QQuickPathQuad binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathQuad to be private: it declares the class in a header
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


class QQuickPathQuad(QQuickCurve):
  """
  The cute side of Qt's QQuickPathQuad: a plain Python object standing in
  front of one C++ QQuickPathQuad.

  It is built on the cute 'QQuickCurve', as Qt's QQuickPathQuad is built on
  Qt's QQuickCurve, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathQuad that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'controlX',
  'setControlX', 'controlY', 'setControlY', 'relativeControlX',
  'setRelativeControlX', 'hasRelativeControlX', 'relativeControlY',
  'setRelativeControlY', 'hasRelativeControlY', 'controlXChanged',
  'controlYChanged', 'relativeControlXChanged', 'relativeControlYChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathQuad::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPathQuad::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathQuad::addToPath(QPainterPath &path, const
    QQuickPathData &a1)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathQuad is created at the first use, not by
    'QQuickPathQuad(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathQuad.
  - Qt tells when it has removed the C++ QQuickPathQuad. Every call on the
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
    Calls Qt's 'QString QQuickPathQuad::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathquad.html#tr

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
    #  QString QQuickPathQuad::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickPathQuad2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathQuad'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathQuad::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathquad.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathQuad::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathQuad10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def controlX(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathQuad::controlX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathquad.html#controlX
    """
    #  qreal QQuickPathQuad::controlX() const
    return self.uglySide.call('ritual_ZNK14QQuickPathQuad8controlXEv')

  def controlY(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathQuad::controlY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathquad.html#controlY
    """
    #  qreal QQuickPathQuad::controlY() const
    return self.uglySide.call('ritual_ZNK14QQuickPathQuad8controlYEv')

  def relativeControlX(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathQuad::relativeControlX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#relativeControlX
    """
    #  qreal QQuickPathQuad::relativeControlX() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickPathQuad16relativeControlXEv',
    )

  def relativeControlY(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathQuad::relativeControlY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#relativeControlY
    """
    #  qreal QQuickPathQuad::relativeControlY() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickPathQuad16relativeControlYEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setControlX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::setControlX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathquad.html#setControlX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPathQuad::setControlX(qreal x)
    self.uglySide.call('ritual_ZN14QQuickPathQuad11setControlXEd', x)

  @overload(float)
  def setControlY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::setControlY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathquad.html#setControlY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPathQuad::setControlY(qreal y)
    self.uglySide.call('ritual_ZN14QQuickPathQuad11setControlYEd', y)

  @overload(float)
  def setRelativeControlX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::setRelativeControlX(qreal x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#setRelativeControlX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPathQuad::setRelativeControlX(qreal x)
    self.uglySide.call('ritual_ZN14QQuickPathQuad19setRelativeControlXEd', x)

  @overload(float)
  def setRelativeControlY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::setRelativeControlY(qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#setRelativeControlY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPathQuad::setRelativeControlY(qreal y)
    self.uglySide.call('ritual_ZN14QQuickPathQuad19setRelativeControlYEd', y)

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
    Notes what was given, for Qt's 'QQuickPathQuad::QQuickPathQuad(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathquad.html#QQuickPathQuad

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathQuad::QQuickPathQuad(QObject *parent)
    self._noteCreation(QQuickPathQuad, lambda: Rituals.call(
        'ritual_ZN14QQuickPathQuadC1EP7QObject',
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

  def hasRelativeControlX(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathQuad::hasRelativeControlX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#hasRelativeControlX
    """
    #  bool QQuickPathQuad::hasRelativeControlX()
    return self.uglySide.call(
        'ritual_ZN14QQuickPathQuad19hasRelativeControlXEv',
    )

  def hasRelativeControlY(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathQuad::hasRelativeControlY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#hasRelativeControlY
    """
    #  bool QQuickPathQuad::hasRelativeControlY()
    return self.uglySide.call(
        'ritual_ZN14QQuickPathQuad19hasRelativeControlYEv',
    )

  def controlXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::controlXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#controlXChanged
    """
    #  void QQuickPathQuad::controlXChanged()
    self.uglySide.call('ritual_ZN14QQuickPathQuad15controlXChangedEv')

  def controlYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::controlYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#controlYChanged
    """
    #  void QQuickPathQuad::controlYChanged()
    self.uglySide.call('ritual_ZN14QQuickPathQuad15controlYChangedEv')

  def relativeControlXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::relativeControlXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#relativeControlXChanged
    """
    #  void QQuickPathQuad::relativeControlXChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathQuad23relativeControlXChangedEv',
    )

  def relativeControlYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathQuad::relativeControlYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathquad.html#relativeControlYChanged
    """
    #  void QQuickPathQuad::relativeControlYChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathQuad23relativeControlYChangedEv',
    )
