"""
QPanGesture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGesture

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


class QPanGesture(QGesture):
  """
  The cute side of Qt's QPanGesture: a plain Python object standing in front
  of one C++ QPanGesture.

  It is built on the cute 'QGesture', as Qt's QPanGesture is built on Qt's
  QGesture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPanGesture that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'lastOffset', 'offset',
  'delta', 'acceleration', 'setLastOffset', 'setOffset', 'setAcceleration'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPanGesturePrivate *QPanGesture::d_func()': gives
    'QPanGesturePrivate', which has no cute class yet.
  - Qt's 'const QPanGesturePrivate *QPanGesture::d_func() const': gives
    'QPanGesturePrivate', which has no cute class yet.
  - Qt's 'QPanGesture::~QPanGesture()': the destructor: Python never removes
    a C++ QPanGesture.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QPanGesture is created at the first use, not by
    'QPanGesture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPanGesture.
  - Qt tells when it has removed the C++ QPanGesture. Every call on the cute
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
    Calls Qt's 'QString QPanGesture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#tr

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
    #  QString QPanGesture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QPanGesture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPanGesture'

  #  A C++ QPanGesture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPanGesture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPanGesture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPanGesture::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QPanGesture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lastOffset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPanGesture::lastOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#lastOffset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPanGesture::lastOffset() const
    address = self.uglySide.call('ritual_ZNK11QPanGesture10lastOffsetEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPanGesture::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPanGesture::offset() const
    address = self.uglySide.call('ritual_ZNK11QPanGesture6offsetEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def delta(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPanGesture::delta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#delta

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPanGesture::delta() const
    address = self.uglySide.call('ritual_ZNK11QPanGesture5deltaEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def acceleration(self) -> float:
    """
    Calls Qt's 'qreal QPanGesture::acceleration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#acceleration
    """
    #  qreal QPanGesture::acceleration() const
    return self.uglySide.call('ritual_ZNK11QPanGesture12accelerationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setLastOffset(self, value: QPointF) -> None:
    """
    Calls Qt's 'void QPanGesture::setLastOffset(const QPointF &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#setLastOffset

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPanGesture::setLastOffset(const QPointF &value)
    self.uglySide.call(
        'ritual_ZN11QPanGesture13setLastOffsetERK7QPointF',
        self._valueOf(value),
    )

  @overload(QPointF)
  def setOffset(self, value: QPointF) -> None:
    """
    Calls Qt's 'void QPanGesture::setOffset(const QPointF &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#setOffset

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPanGesture::setOffset(const QPointF &value)
    self.uglySide.call(
        'ritual_ZN11QPanGesture9setOffsetERK7QPointF', self._valueOf(value),
    )

  @overload(float)
  def setAcceleration(self, value: float) -> None:
    """
    Calls Qt's 'void QPanGesture::setAcceleration(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#setAcceleration

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPanGesture::setAcceleration(qreal value)
    self.uglySide.call('ritual_ZN11QPanGesture15setAccelerationEd', value)

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
    Notes what was given, for Qt's 'QPanGesture::QPanGesture(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpangesture.html#QPanGesture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPanGesture::QPanGesture(QObject *parent)
    self._noteCreation(QPanGesture, lambda: Rituals.call(
        'ritual_ZN11QPanGestureC1EP7QObject', self._addressOf(parent),
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
