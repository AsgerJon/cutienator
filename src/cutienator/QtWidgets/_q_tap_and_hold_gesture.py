"""
QTapAndHoldGesture binding of the Qt C++
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


class QTapAndHoldGesture(QGesture):
  """
  The cute side of Qt's QTapAndHoldGesture: a plain Python object standing in
  front of one C++ QTapAndHoldGesture.

  It is built on the cute 'QGesture', as Qt's QTapAndHoldGesture is built on
  Qt's QGesture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTapAndHoldGesture that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'position',
  'setPosition', 'setTimeout', 'timeout'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTapAndHoldGesture::~QTapAndHoldGesture()': the destructor: Python
    never removes a C++ QTapAndHoldGesture.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QTapAndHoldGesture is created at the first use, not by
    'QTapAndHoldGesture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTapAndHoldGesture.
  - Qt tells when it has removed the C++ QTapAndHoldGesture. Every call on
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
    Calls Qt's 'QString QTapAndHoldGesture::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapandholdgesture.html#tr

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
    #  QString QTapAndHoldGesture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QTapAndHoldGesture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int)
  def setTimeout(msecs: int) -> None:
    """
    Calls Qt's 'void QTapAndHoldGesture::setTimeout(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapandholdgesture.html#setTimeout

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QTapAndHoldGesture::setTimeout(int msecs)
    Rituals.call('ritual_ZN18QTapAndHoldGesture10setTimeoutEi', msecs)

  @staticmethod
  def timeout() -> int:
    """
    Calls Qt's 'int QTapAndHoldGesture::timeout()'.

    Qt's own words: https://doc.qt.io/qt-6/qtapandholdgesture.html#timeout
    """
    #  int QTapAndHoldGesture::timeout()
    return Rituals.call('ritual_ZN18QTapAndHoldGesture7timeoutEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTapAndHoldGesture'

  #  A C++ QTapAndHoldGesture Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTapAndHoldGesture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTapAndHoldGesture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtapandholdgesture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTapAndHoldGesture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QTapAndHoldGesture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QTapAndHoldGesture::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtapandholdgesture.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QTapAndHoldGesture::position() const
    address = self.uglySide.call('ritual_ZNK18QTapAndHoldGesture8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPosition(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QTapAndHoldGesture::setPosition(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtapandholdgesture.html#setPosition

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QTapAndHoldGesture::setPosition(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN18QTapAndHoldGesture11setPositionERK7QPointF',
        self._valueOf(pos),
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
    'QTapAndHoldGesture::QTapAndHoldGesture(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtapandholdgesture.html#QTapAndHoldGesture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTapAndHoldGesture::QTapAndHoldGesture(QObject *parent)
    self._noteCreation(QTapAndHoldGesture, lambda: Rituals.call(
        'ritual_ZN18QTapAndHoldGestureC1EP7QObject', self._addressOf(parent),
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
