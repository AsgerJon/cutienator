"""
QDial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qdial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QAbstractSlider, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDial(QAbstractSlider):
  """
  The cute side of Qt's QDial: a plain Python object standing in front of one
  C++ QDial.

  It is built on the cute 'QAbstractSlider', as Qt's QDial is built on Qt's
  QAbstractSlider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDial that has a ritual and that Python can call so
  far, 11 names in all: 'metaObject', 'tr', 'wrapping', 'notchSize',
  'setNotchTarget', 'notchTarget', 'notchesVisible', 'sizeHint',
  'minimumSizeHint', 'setNotchesVisible', 'setWrapping'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDial::~QDial()': the destructor: Python never removes a C++ QDial.

  What has no ritual
  ------------------

  16 of the 29 functions Qt declares: 8 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QDial is created at the first use, not by 'QDial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDial.
  - Qt tells when it has removed the C++ QDial. Every call on the cute
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
    Calls Qt's 'QString QDial::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#tr

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
    #  QString QDial::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN5QDial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDial::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDial::metaObject() const
    address = self.uglySide.call('ritual_ZNK5QDial10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def wrapping(self) -> bool:
    """
    Calls Qt's 'bool QDial::wrapping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#wrapping
    """
    #  bool QDial::wrapping() const
    return self.uglySide.call('ritual_ZNK5QDial8wrappingEv')

  def notchSize(self) -> int:
    """
    Calls Qt's 'int QDial::notchSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#notchSize
    """
    #  int QDial::notchSize() const
    return self.uglySide.call('ritual_ZNK5QDial9notchSizeEv')

  def notchTarget(self) -> float:
    """
    Calls Qt's 'qreal QDial::notchTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#notchTarget
    """
    #  qreal QDial::notchTarget() const
    return self.uglySide.call('ritual_ZNK5QDial11notchTargetEv')

  def notchesVisible(self) -> bool:
    """
    Calls Qt's 'bool QDial::notchesVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#notchesVisible
    """
    #  bool QDial::notchesVisible() const
    return self.uglySide.call('ritual_ZNK5QDial14notchesVisibleEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDial::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDial::sizeHint() const
    address = self.uglySide.call('ritual_ZNK5QDial8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDial::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDial::minimumSizeHint() const
    address = self.uglySide.call('ritual_ZNK5QDial15minimumSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setNotchTarget(self, target: float) -> None:
    """
    Calls Qt's 'void QDial::setNotchTarget(double target)'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#setNotchTarget

    Parameters
    ----------

    target : float
      Passed on as it is.
    """
    #  void QDial::setNotchTarget(double target)
    self.uglySide.call('ritual_ZN5QDial14setNotchTargetEd', target)

  @overload(bool)
  def setNotchesVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QDial::setNotchesVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#setNotchesVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDial::setNotchesVisible(bool visible)
    self.uglySide.call('ritual_ZN5QDial17setNotchesVisibleEb', visible)

  @overload(bool)
  def setWrapping(self, on: bool) -> None:
    """
    Calls Qt's 'void QDial::setWrapping(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#setWrapping

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QDial::setWrapping(bool on)
    self.uglySide.call('ritual_ZN5QDial11setWrappingEb', on)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QDial::QDial(QWidget *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdial.html#QDial

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDial::QDial(QWidget *parent)
    self._noteCreation(QDial, lambda: Rituals.call(
        'ritual_ZN5QDialC1EP7QWidget', self._addressOf(parent),
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
