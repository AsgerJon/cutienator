"""
QDoubleValidator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QValidator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDoubleValidator(QValidator):
  """
  The cute side of Qt's QDoubleValidator: a plain Python object standing in
  front of one C++ QDoubleValidator.

  It is built on the cute 'QValidator', as Qt's QDoubleValidator is built on
  Qt's QValidator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDoubleValidator that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'setRange',
  'setBottom', 'setTop', 'setDecimals', 'setNotation', 'bottom', 'top',
  'decimals', 'notation'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDoubleValidator::~QDoubleValidator()': the destructor: Python
    never removes a C++ QDoubleValidator.

  What has no ritual
  ------------------

  14 of the 29 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 4 a signal; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QDoubleValidator is created at the first use, not by
    'QDoubleValidator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDoubleValidator.
  - Qt tells when it has removed the C++ QDoubleValidator. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDoubleValidator, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Notation(CuteNum):
    """
    The enum 'QDoubleValidator::Notation' of Qt, with the 2 names Qt gives in
    it.
    """

    StandardNotation = Kee[int](0)
    ScientificNotation = Kee[int](1)

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
    Calls Qt's 'QString QDoubleValidator::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#tr

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
    #  QString QDoubleValidator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QDoubleValidator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDoubleValidator'

  #  A C++ QDoubleValidator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDoubleValidator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDoubleValidator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDoubleValidator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleValidator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bottom(self) -> float:
    """
    Calls Qt's 'double QDoubleValidator::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#bottom
    """
    #  double QDoubleValidator::bottom() const
    return self.uglySide.call('ritual_ZNK16QDoubleValidator6bottomEv')

  def top(self) -> float:
    """
    Calls Qt's 'double QDoubleValidator::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#top
    """
    #  double QDoubleValidator::top() const
    return self.uglySide.call('ritual_ZNK16QDoubleValidator3topEv')

  def decimals(self) -> int:
    """
    Calls Qt's 'int QDoubleValidator::decimals() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#decimals
    """
    #  int QDoubleValidator::decimals() const
    return self.uglySide.call('ritual_ZNK16QDoubleValidator8decimalsEv')

  def notation(self) -> Notation:
    """
    Calls Qt's 'Notation QDoubleValidator::notation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#notation

    Returns
    -------

    Notation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Notation(number)' gives.
    """
    #  Notation QDoubleValidator::notation() const
    return QDoubleValidator.Notation(self.uglySide.call(
        'ritual_ZNK16QDoubleValidator8notationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, int)
  def setRange(self, bottom: float, top: float, decimals: int) -> None:
    """
    Calls Qt's 'void QDoubleValidator::setRange(double bottom, double top,
    int decimals)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#setRange

    Parameters
    ----------

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    decimals : int
      Passed on as it is.
    """
    #  void QDoubleValidator::setRange(double bottom, double top, int
    #      decimals)
    self.uglySide.call(
        'ritual_ZN16QDoubleValidator8setRangeEddi', bottom, top, decimals,
    )

  @overload(float, float)
  def setRange(self, bottom: float, top: float) -> None:
    """
    Calls Qt's 'void QDoubleValidator::setRange(double bottom, double top)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#setRange

    Parameters
    ----------

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.
    """
    #  void QDoubleValidator::setRange(double bottom, double top)
    self.uglySide.call(
        'ritual_ZN16QDoubleValidator8setRangeEdd', bottom, top,
    )

  @overload(float)
  def setBottom(self, a0: float) -> None:
    """
    Calls Qt's 'void QDoubleValidator::setBottom(double a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#setBottom

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QDoubleValidator::setBottom(double a0)
    self.uglySide.call('ritual_ZN16QDoubleValidator9setBottomEd', a0)

  @overload(float)
  def setTop(self, a0: float) -> None:
    """
    Calls Qt's 'void QDoubleValidator::setTop(double a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#setTop

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QDoubleValidator::setTop(double a0)
    self.uglySide.call('ritual_ZN16QDoubleValidator6setTopEd', a0)

  @overload(int)
  def setDecimals(self, a0: int) -> None:
    """
    Calls Qt's 'void QDoubleValidator::setDecimals(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#setDecimals

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QDoubleValidator::setDecimals(int a0)
    self.uglySide.call('ritual_ZN16QDoubleValidator11setDecimalsEi', a0)

  @overload(Notation)
  def setNotation(self, a0: Notation) -> None:
    """
    Calls Qt's 'void QDoubleValidator::setNotation(Notation a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevalidator.html#setNotation

    Parameters
    ----------

    a0 : Notation
      Passed on as its number.
    """
    #  void QDoubleValidator::setNotation(Notation a0)
    self.uglySide.call(
        'ritual_ZN16QDoubleValidator11setNotationENS_8NotationE', a0.value,
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
    'QDoubleValidator::QDoubleValidator(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevalidator.html#QDoubleValidator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDoubleValidator::QDoubleValidator(QObject *parent)
    self._noteCreation(QDoubleValidator, lambda: Rituals.call(
        'ritual_ZN16QDoubleValidatorC1EP7QObject', self._addressOf(parent),
    ))

  @overload(float, float, int)
  @overload(float, float, int, QObject)
  @overload(float, float, int, NoneType)
  def __init__(
      self,
      bottom: float,
      top: float,
      decimals: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDoubleValidator::QDoubleValidator(double
    bottom, double top, int decimals, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevalidator.html#QDoubleValidator

    Parameters
    ----------

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    decimals : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDoubleValidator::QDoubleValidator(double bottom, double top, int
    #      decimals, QObject *parent)
    self._noteCreation(QDoubleValidator, lambda: Rituals.call(
        'ritual_ZN16QDoubleValidatorC1EddiP7QObject',
        bottom, top, decimals, self._addressOf(parent),
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
