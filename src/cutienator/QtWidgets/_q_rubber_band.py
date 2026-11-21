"""
QRubberBand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qrubberband.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QRubberBandShape, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRubberBand(QWidget):
  """
  The cute side of Qt's QRubberBand: a plain Python object standing in front
  of one C++ QRubberBand.

  It is built on the cute 'QWidget', as Qt's QRubberBand is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRubberBand that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'shape', 'setGeometry',
  'move', 'resize'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRubberBand::~QRubberBand()': the destructor: Python never removes
    a C++ QRubberBand.

  What has no ritual
  ------------------

  13 of the 24 functions Qt declares: 7 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QRubberBand is created at the first use, not by
    'QRubberBand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRubberBand.
  - Qt tells when it has removed the C++ QRubberBand. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QRubberBand, and the names Qt has for the
  #  combinations of its flags enums.
  Shape = QRubberBandShape

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
    Calls Qt's 'QString QRubberBand::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#tr

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
    #  QString QRubberBand::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QRubberBand2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRubberBand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRubberBand::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRubberBand::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QRubberBand10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shape(self) -> Shape:
    """
    Calls Qt's 'Shape QRubberBand::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#shape

    Returns
    -------

    Shape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Shape(number)' gives.
    """
    #  Shape QRubberBand::shape() const
    return QRubberBand.Shape(self.uglySide.call(
        'ritual_ZNK11QRubberBand5shapeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setGeometry(self, r: QRect) -> None:
    """
    Calls Qt's 'void QRubberBand::setGeometry(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#setGeometry

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QRubberBand::setGeometry(const QRect &r)
    self.uglySide.call(
        'ritual_ZN11QRubberBand11setGeometryERK5QRect', self._valueOf(r),
    )

  @overload(int, int, int, int)
  def setGeometry(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QRubberBand::setGeometry(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#setGeometry

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QRubberBand::setGeometry(int x, int y, int w, int h)
    self.uglySide.call(
        'ritual_ZN11QRubberBand11setGeometryEiiii', x, y, w, h,
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

  @overload(Shape)
  @overload(Shape, QWidget)
  @overload(Shape, NoneType)
  def __init__(self, a0: Shape, a1: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QRubberBand::QRubberBand(Shape a0,
    QWidget *a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#QRubberBand

    Parameters
    ----------

    a0 : Shape
      Passed on as its number.

    a1 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRubberBand::QRubberBand(Shape a0, QWidget *a1)
    self._noteCreation(QRubberBand, lambda: Rituals.call(
        'ritual_ZN11QRubberBandC1ENS_5ShapeEP7QWidget',
        a0.value, self._addressOf(a1),
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

  @overload(int, int)
  def move(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QRubberBand::move(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#move

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QRubberBand::move(int x, int y)
    self.uglySide.call('ritual_ZN11QRubberBand4moveEii', x, y)

  @overload(QPoint)
  def move(self, p: QPoint) -> None:
    """
    Calls Qt's 'void QRubberBand::move(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#move

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QRubberBand::move(const QPoint &p)
    self.uglySide.call(
        'ritual_ZN11QRubberBand4moveERK6QPoint', self._valueOf(p),
    )

  @overload(int, int)
  def resize(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QRubberBand::resize(int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#resize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QRubberBand::resize(int w, int h)
    self.uglySide.call('ritual_ZN11QRubberBand6resizeEii', w, h)

  @overload(QSize)
  def resize(self, s: QSize) -> None:
    """
    Calls Qt's 'void QRubberBand::resize(const QSize &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qrubberband.html#resize

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRubberBand::resize(const QSize &s)
    self.uglySide.call(
        'ritual_ZN11QRubberBand6resizeERK5QSize', self._valueOf(s),
    )
