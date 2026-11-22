"""
QGraphicsOpacityEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGraphicsEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsOpacityEffect(QGraphicsEffect):
  """
  The cute side of Qt's QGraphicsOpacityEffect: a plain Python object
  standing in front of one C++ QGraphicsOpacityEffect.

  It is built on the cute 'QGraphicsEffect', as Qt's QGraphicsOpacityEffect
  is built on Qt's QGraphicsEffect, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsOpacityEffect that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'opacity',
  'opacityMask', 'setOpacity', 'setOpacityMask', 'draw'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsOpacityEffect::~QGraphicsOpacityEffect()': the destructor:
    Python never removes a C++ QGraphicsOpacityEffect.

  What has no ritual
  ------------------

  10 of the 19 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QGraphicsOpacityEffect is created at the first use, not by
    'QGraphicsOpacityEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsOpacityEffect.
  - Qt tells when it has removed the C++ QGraphicsOpacityEffect. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGraphicsOpacityEffect::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#tr

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
    #  QString QGraphicsOpacityEffect::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QGraphicsOpacityEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsOpacityEffect'

  #  A C++ QGraphicsOpacityEffect Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsOpacityEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsOpacityEffect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsOpacityEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsOpacityEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsOpacityEffect::opacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacity
    """
    #  qreal QGraphicsOpacityEffect::opacity() const
    return self.uglySide.call('ritual_ZNK22QGraphicsOpacityEffect7opacityEv')

  def opacityMask(self) -> QBrush:
    """
    Calls Qt's 'QBrush QGraphicsOpacityEffect::opacityMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#opacityMask

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QGraphicsOpacityEffect::opacityMask() const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsOpacityEffect11opacityMaskEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QGraphicsOpacityEffect::setOpacity(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QGraphicsOpacityEffect::setOpacity(qreal opacity)
    self.uglySide.call(
        'ritual_ZN22QGraphicsOpacityEffect10setOpacityEd', opacity,
    )

  @overload(QBrush)
  def setOpacityMask(self, mask: QBrush) -> None:
    """
    Calls Qt's 'void QGraphicsOpacityEffect::setOpacityMask(const QBrush
    &mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#setOpacityMask

    Parameters
    ----------

    mask : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QGraphicsOpacityEffect::setOpacityMask(const QBrush &mask)
    self.uglySide.call(
        'ritual_ZN22QGraphicsOpacityEffect14setOpacityMaskERK6QBrush',
        self._valueOf(mask),
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
    'QGraphicsOpacityEffect::QGraphicsOpacityEffect(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#QGraphicsOpacityEffect

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsOpacityEffect::QGraphicsOpacityEffect(QObject *parent)
    self._noteCreation(QGraphicsOpacityEffect, lambda: Rituals.call(
        'ritual_ZN22QGraphicsOpacityEffectC1EP7QObject',
        self._addressOf(parent),
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

  @overload(QPainter)
  @overload(NoneType)
  def draw(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QGraphicsOpacityEffect::draw(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsopacityeffect.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsOpacityEffect::draw(QPainter *painter)
    self.uglySide.call(
        'ritual_own_ZN22QGraphicsOpacityEffect4drawEP8QPainter',
        self._addressOf(painter),
    )
