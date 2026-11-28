"""
QIntValidator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QValidator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIntValidator(QValidator):
  """
  The cute side of Qt's QIntValidator: a plain Python object standing in
  front of one C++ QIntValidator.

  It is built on the cute 'QValidator', as Qt's QIntValidator is built on
  Qt's QValidator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIntValidator that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'setBottom', 'setTop',
  'setRange', 'bottom', 'top', 'bottomChanged', 'topChanged'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QIntValidator::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QIntValidator::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QIntValidator::~QIntValidator()': the destructor: Python never
    removes a C++ QIntValidator.
  - Qt's 'QValidator::State QIntValidator::validate(QString &a0, int &a1)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QIntValidator::fixup(QString &input) const': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QIntValidator is created at the first use, not by
    'QIntValidator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIntValidator.
  - Qt tells when it has removed the C++ QIntValidator. Every call on the
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
    Calls Qt's 'QString QIntValidator::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#tr

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
    #  QString QIntValidator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QIntValidator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIntValidator'

  #  A C++ QIntValidator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIntValidator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QIntValidator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QIntValidator::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QIntValidator10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bottom(self) -> int:
    """
    Calls Qt's 'int QIntValidator::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#bottom
    """
    #  int QIntValidator::bottom() const
    return self.uglySide.call('ritual_ZNK13QIntValidator6bottomEv')

  def top(self) -> int:
    """
    Calls Qt's 'int QIntValidator::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#top
    """
    #  int QIntValidator::top() const
    return self.uglySide.call('ritual_ZNK13QIntValidator3topEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBottom(self, a0: int) -> None:
    """
    Calls Qt's 'void QIntValidator::setBottom(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#setBottom

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QIntValidator::setBottom(int a0)
    self.uglySide.call('ritual_ZN13QIntValidator9setBottomEi', a0)

  @overload(int)
  def setTop(self, a0: int) -> None:
    """
    Calls Qt's 'void QIntValidator::setTop(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#setTop

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QIntValidator::setTop(int a0)
    self.uglySide.call('ritual_ZN13QIntValidator6setTopEi', a0)

  @overload(int, int)
  def setRange(self, bottom: int, top: int) -> None:
    """
    Calls Qt's 'void QIntValidator::setRange(int bottom, int top)'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#setRange

    Parameters
    ----------

    bottom : int
      Passed on as it is.

    top : int
      Passed on as it is.
    """
    #  void QIntValidator::setRange(int bottom, int top)
    self.uglySide.call('ritual_ZN13QIntValidator8setRangeEii', bottom, top)

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
    Notes what was given, for Qt's 'QIntValidator::QIntValidator(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#QIntValidator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QIntValidator::QIntValidator(QObject *parent)
    self._noteCreation(QIntValidator, lambda: Rituals.call(
        'ritual_ZN13QIntValidatorC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(int, int)
  @overload(int, int, QObject)
  @overload(int, int, NoneType)
  def __init__(
      self,
      bottom: int,
      top: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QIntValidator::QIntValidator(int bottom,
    int top, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#QIntValidator

    Parameters
    ----------

    bottom : int
      Passed on as it is.

    top : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QIntValidator::QIntValidator(int bottom, int top, QObject *parent)
    self._noteCreation(QIntValidator, lambda: Rituals.call(
        'ritual_ZN13QIntValidatorC1EiiP7QObject',
        bottom, top, self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def bottomChanged(self, bottom: int) -> None:
    """
    Calls Qt's 'void QIntValidator::bottomChanged(int bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#bottomChanged

    Parameters
    ----------

    bottom : int
      Passed on as it is.
    """
    #  void QIntValidator::bottomChanged(int bottom)
    self.uglySide.call('ritual_ZN13QIntValidator13bottomChangedEi', bottom)

  @overload(int)
  def topChanged(self, top: int) -> None:
    """
    Calls Qt's 'void QIntValidator::topChanged(int top)'.

    Qt's own words: https://doc.qt.io/qt-6/qintvalidator.html#topChanged

    Parameters
    ----------

    top : int
      Passed on as it is.
    """
    #  void QIntValidator::topChanged(int top)
    self.uglySide.call('ritual_ZN13QIntValidator10topChangedEi', top)
