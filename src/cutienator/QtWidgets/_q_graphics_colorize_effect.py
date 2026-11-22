"""
QGraphicsColorizeEffect binding of the Qt C++
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
  from ..QtGui import QColor, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsColorizeEffect(QGraphicsEffect):
  """
  The cute side of Qt's QGraphicsColorizeEffect: a plain Python object
  standing in front of one C++ QGraphicsColorizeEffect.

  It is built on the cute 'QGraphicsEffect', as Qt's QGraphicsColorizeEffect
  is built on Qt's QGraphicsEffect, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsColorizeEffect that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'color',
  'strength', 'setColor', 'setStrength', 'draw'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsColorizeEffect::~QGraphicsColorizeEffect()': the
    destructor: Python never removes a C++ QGraphicsColorizeEffect.

  What has no ritual
  ------------------

  10 of the 19 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QGraphicsColorizeEffect is created at the first use, not by
    'QGraphicsColorizeEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsColorizeEffect.
  - Qt tells when it has removed the C++ QGraphicsColorizeEffect. Every call
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
    Calls Qt's 'QString QGraphicsColorizeEffect::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#tr

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
    #  QString QGraphicsColorizeEffect::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QGraphicsColorizeEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsColorizeEffect'

  #  A C++ QGraphicsColorizeEffect Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsColorizeEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsColorizeEffect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsColorizeEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QGraphicsColorizeEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphicsColorizeEffect::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphicsColorizeEffect::color() const
    address = self.uglySide.call(
        'ritual_ZNK23QGraphicsColorizeEffect5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def strength(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsColorizeEffect::strength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#strength
    """
    #  qreal QGraphicsColorizeEffect::strength() const
    return self.uglySide.call(
        'ritual_ZNK23QGraphicsColorizeEffect8strengthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QGraphicsColorizeEffect::setColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphicsColorizeEffect::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN23QGraphicsColorizeEffect8setColorERK6QColor',
        self._valueOf(c),
    )

  @overload(float)
  def setStrength(self, strength: float) -> None:
    """
    Calls Qt's 'void QGraphicsColorizeEffect::setStrength(qreal strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#setStrength

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void QGraphicsColorizeEffect::setStrength(qreal strength)
    self.uglySide.call(
        'ritual_ZN23QGraphicsColorizeEffect11setStrengthEd', strength,
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
    'QGraphicsColorizeEffect::QGraphicsColorizeEffect(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsColorizeEffect::QGraphicsColorizeEffect(QObject *parent)
    self._noteCreation(QGraphicsColorizeEffect, lambda: Rituals.call(
        'ritual_ZN23QGraphicsColorizeEffectC1EP7QObject',
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
    Calls Qt's 'void QGraphicsColorizeEffect::draw(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicscolorizeeffect.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsColorizeEffect::draw(QPainter *painter)
    self.uglySide.call(
        'ritual_own_ZN23QGraphicsColorizeEffect4drawEP8QPainter',
        self._addressOf(painter),
    )
