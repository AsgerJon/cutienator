"""
QPieSlicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qpieslice_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPieSlicePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QFont, QPen
  from . import QPieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QFont = WAIT['QFont']
  QPen = WAIT['QPen']
  QPieSlice = WAIT['QtCharts:QPieSlice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieSlicePrivate(QObject):
  """
  The cute side of Qt's QPieSlicePrivate: a plain Python object standing in
  front of one C++ QPieSlicePrivate.

  It is built on the cute 'QObject', as Qt's QPieSlicePrivate is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieSlicePrivate that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'fromSlice',
  'setPen', 'setBrush', 'setLabelBrush', 'setLabelFont', 'setPercentage',
  'setStartAngle', 'setAngleSpan', 'labelPositionChanged', 'explodedChanged',
  'labelArmLengthFactorChanged', 'explodeDistanceFactorChanged', 'q_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieSlicePrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPieSlicePrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPieSlicePrivate::~QPieSlicePrivate()': the destructor: Python
    never removes a C++ QPieSlicePrivate.
  - Qt's 'const QPieSlice *QPieSlicePrivate::q_func() const': takes in Python
    what 'QPieSlice *QPieSlicePrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPieSlicePrivate is created at the first use, not by
    'QPieSlicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieSlicePrivate.
  - Qt tells when it has removed the C++ QPieSlicePrivate. Every call on the
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
    Calls Qt's 'QString QPieSlicePrivate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#tr

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
    #  QString QPieSlicePrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPieSlicePrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QPieSlice)
  @overload(NoneType)
  def fromSlice(slice: Optional[QPieSlice]) -> Optional[QPieSlicePrivate]:
    """
    Calls Qt's 'QPieSlicePrivate *QPieSlicePrivate::fromSlice(QPieSlice
    *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#fromSlice

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPieSlicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlicePrivate *QPieSlicePrivate::fromSlice(QPieSlice *slice)
    address = Rituals.call(
        'ritual_ZN16QPieSlicePrivate9fromSliceEP9QPieSlice',
        CuteMixin._addressOf(slice),
    )
    return QPieSlicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieSlicePrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QPieSlicePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPieSlicePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPieSlicePrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieSlicePrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPieSlicePrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPen, bool)
  def setPen(self, pen: QPen, themed: bool) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setPen(const QPen &pen, bool themed)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.

    themed : bool
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setPen(const QPen &pen, bool themed)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate6setPenERK4QPenb',
        self._valueOf(pen), themed,
    )

  @overload(QBrush, bool)
  def setBrush(self, brush: QBrush, themed: bool) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setBrush(const QBrush &brush, bool
    themed)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    themed : bool
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setBrush(const QBrush &brush, bool themed)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate8setBrushERK6QBrushb',
        self._valueOf(brush), themed,
    )

  @overload(QBrush, bool)
  def setLabelBrush(self, brush: QBrush, themed: bool) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setLabelBrush(const QBrush &brush,
    bool themed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#setLabelBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    themed : bool
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setLabelBrush(const QBrush &brush, bool themed)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate13setLabelBrushERK6QBrushb',
        self._valueOf(brush), themed,
    )

  @overload(QFont, bool)
  def setLabelFont(self, font: QFont, themed: bool) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setLabelFont(const QFont &font, bool
    themed)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#setLabelFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    themed : bool
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setLabelFont(const QFont &font, bool themed)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate12setLabelFontERK5QFontb',
        self._valueOf(font), themed,
    )

  @overload(float)
  def setPercentage(self, percentage: float) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setPercentage(qreal percentage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#setPercentage

    Parameters
    ----------

    percentage : float
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setPercentage(qreal percentage)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate13setPercentageEd', percentage,
    )

  @overload(float)
  def setStartAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setStartAngle(qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#setStartAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setStartAngle(qreal angle)
    self.uglySide.call('ritual_ZN16QPieSlicePrivate13setStartAngleEd', angle)

  @overload(float)
  def setAngleSpan(self, span: float) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setAngleSpan(qreal span)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#setAngleSpan

    Parameters
    ----------

    span : float
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setAngleSpan(qreal span)
    self.uglySide.call('ritual_ZN16QPieSlicePrivate12setAngleSpanEd', span)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPieSlice)
  @overload(NoneType)
  def __init__(self, parent: Optional[QPieSlice]) -> None:
    """
    Notes what was given, for Qt's
    'QPieSlicePrivate::QPieSlicePrivate(QPieSlice *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#QPieSlicePrivate

    Parameters
    ----------

    parent : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPieSlicePrivate::QPieSlicePrivate(QPieSlice *parent)
    self._noteCreation(QPieSlicePrivate, lambda: Rituals.call(
        'ritual_ZN16QPieSlicePrivateC1EP9QPieSlice', self._addressOf(parent),
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

  def labelPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::labelPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#labelPositionChanged
    """
    #  void QPieSlicePrivate::labelPositionChanged()
    self.uglySide.call('ritual_ZN16QPieSlicePrivate20labelPositionChangedEv')

  def explodedChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::explodedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#explodedChanged
    """
    #  void QPieSlicePrivate::explodedChanged()
    self.uglySide.call('ritual_ZN16QPieSlicePrivate15explodedChangedEv')

  def labelArmLengthFactorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::labelArmLengthFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#labelArmLengthFactorChanged
    """
    #  void QPieSlicePrivate::labelArmLengthFactorChanged()
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate27labelArmLengthFactorChangedEv',
    )

  def explodeDistanceFactorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::explodeDistanceFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#explodeDistanceFactorChanged
    """
    #  void QPieSlicePrivate::explodeDistanceFactorChanged()
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate28explodeDistanceFactorChangedEv',
    )

  def q_func(self) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSlicePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#q_func

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSlicePrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QPieSlicePrivate6q_funcEv')
    from . import QPieSlice
    return QPieSlice._cuteAt(address)
