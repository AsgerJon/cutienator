"""
QGraphicsBlurEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGraphicsEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsBlurEffect(QGraphicsEffect):
  """
  The cute side of Qt's QGraphicsBlurEffect: a plain Python object standing
  in front of one C++ QGraphicsBlurEffect.

  It is built on the cute 'QGraphicsEffect', as Qt's QGraphicsBlurEffect is
  built on Qt's QGraphicsEffect, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsBlurEffect that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr',
  'boundingRectFor', 'blurRadius', 'blurHints', 'setBlurRadius',
  'setBlurHints', 'draw'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsBlurEffect::~QGraphicsBlurEffect()': the destructor:
    Python never removes a C++ QGraphicsBlurEffect.
  - Qt's 'QGraphicsBlurEffectPrivate *QGraphicsBlurEffect::d_func()': gives
    'QGraphicsBlurEffectPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsBlurEffectPrivate *QGraphicsBlurEffect::d_func()
    const': gives 'QGraphicsBlurEffectPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  8 of the 20 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QGraphicsBlurEffect is created at the first use, not by
    'QGraphicsBlurEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsBlurEffect.
  - Qt tells when it has removed the C++ QGraphicsBlurEffect. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGraphicsBlurEffect, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BlurHint(CuteFlags):
    """
    The flags enum 'QGraphicsBlurEffect::BlurHint' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QGraphicsBlurEffect::BlurHints'.
    """

    PerformanceHint = 0x0
    QualityHint = 0x1
    AnimationHint = 0x2

  BlurHints = BlurHint

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
    Calls Qt's 'QString QGraphicsBlurEffect::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsblureffect.html#tr

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
    #  QString QGraphicsBlurEffect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QGraphicsBlurEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsBlurEffect'

  #  A C++ QGraphicsBlurEffect Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsBlurEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsBlurEffect::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsblureffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsBlurEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsBlurEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QRectF)
  def boundingRectFor(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsBlurEffect::boundingRectFor(const QRectF
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsblureffect.html#boundingRectFor

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsBlurEffect::boundingRectFor(const QRectF &rect) const
    ritual = 'ritual_ZNK19QGraphicsBlurEffect15boundingRectForERK6QRectF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QGraphicsBlurEffect15boundingRectForERK6QRectF')
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def blurRadius(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsBlurEffect::blurRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsblureffect.html#blurRadius
    """
    #  qreal QGraphicsBlurEffect::blurRadius() const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsBlurEffect10blurRadiusEv',
    )

  def blurHints(self) -> BlurHints:
    """
    Calls Qt's 'BlurHints QGraphicsBlurEffect::blurHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsblureffect.html#blurHints

    Returns
    -------

    BlurHints
      The value standing for the combination Qt gave back.
    """
    #  BlurHints QGraphicsBlurEffect::blurHints() const
    return QGraphicsBlurEffect.BlurHints(self.uglySide.call(
        'ritual_ZNK19QGraphicsBlurEffect9blurHintsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBlurRadius(self, blurRadius: float) -> None:
    """
    Calls Qt's 'void QGraphicsBlurEffect::setBlurRadius(qreal blurRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsblureffect.html#setBlurRadius

    Parameters
    ----------

    blurRadius : float
      Passed on as it is.
    """
    #  void QGraphicsBlurEffect::setBlurRadius(qreal blurRadius)
    self.uglySide.call(
        'ritual_ZN19QGraphicsBlurEffect13setBlurRadiusEd', blurRadius,
    )

  @overload(BlurHints)
  def setBlurHints(self, hints: BlurHints) -> None:
    """
    Calls Qt's 'void QGraphicsBlurEffect::setBlurHints(BlurHints hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsblureffect.html#setBlurHints

    Parameters
    ----------

    hints : BlurHints
      Passed on as its number.
    """
    #  void QGraphicsBlurEffect::setBlurHints(BlurHints hints)
    self.uglySide.call(
        'ritual_ZN19QGraphicsBlurEffect12setBlurHintsE6QFlagsINS_8BlurHintE'
        'E',
        hints.value,
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
    'QGraphicsBlurEffect::QGraphicsBlurEffect(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsblureffect.html#QGraphicsBlurEffect

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsBlurEffect::QGraphicsBlurEffect(QObject *parent)
    self._noteCreation(QGraphicsBlurEffect, lambda: Rituals.call(
        'ritual_ZN19QGraphicsBlurEffectC1EP7QObject',
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
    Calls Qt's 'void QGraphicsBlurEffect::draw(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsblureffect.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsBlurEffect::draw(QPainter *painter)
    ritual = 'ritual_ZN19QGraphicsBlurEffect4drawEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGraphicsBlurEffect4drawEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(painter))
