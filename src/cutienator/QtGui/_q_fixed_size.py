"""
QFixedSize binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfixed_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QFixedSize to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSizeF
  from . import QFixed
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFixed = WAIT['QFixed']
  QSizeF = WAIT['QSizeF']


class QFixedSize(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFixedSize: a plain Python object standing in front
  of one C++ QFixedSize.

  C++ hands a QFixedSize around as a copy, so every C++ QFixedSize behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFixedSize that has a ritual and that Python can
  call so far, 2 names in all: 'toSizeF', 'fromSizeF'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFixedSize::~QFixedSize()': the destructor: Python removes its C++
    QFixedSize by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QFixedSize is created at the first use, not by 'QFixedSize(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFixedSize back gives a copy the ritual made for
    Python, in a new cute QFixedSize.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSizeF)
  def fromSizeF(s: QSizeF) -> QFixedSize:
    """
    Calls Qt's 'QFixedSize QFixedSize::fromSizeF(const QSizeF &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixedsize.html#fromSizeF

    Parameters
    ----------

    s : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QFixedSize
      A new cute QFixedSize around the copy Qt gave back. Python owns it.
    """
    #  QFixedSize QFixedSize::fromSizeF(const QSizeF &s)
    address = Rituals.call(
        'ritual_ZN10QFixedSize9fromSizeFERK6QSizeF', CuteMixin._valueOf(s),
    )
    return QFixedSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFixedSize'

  #  Qt's '~QFixedSize()'. Naming it makes this a value class: Python owns
  #  every C++ QFixedSize behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QFixedSizeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toSizeF(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QFixedSize::toSizeF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixedsize.html#toSizeF

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QFixedSize::toSizeF() const
    address = self.uglySide.call('ritual_ZNK10QFixedSize7toSizeFEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFixedSize::QFixedSize()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixedsize.html#QFixedSize
    """
    #  QFixedSize::QFixedSize()
    self._noteCreation(QFixedSize, lambda: Rituals.call(
        'ritual_ZN10QFixedSizeC1Ev',
    ))

  @overload(QFixed, QFixed)
  def __init__(self, _width: QFixed, _height: QFixed) -> None:
    """
    Notes what was given, for Qt's 'QFixedSize::QFixedSize(QFixed _width,
    QFixed _height)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixedsize.html#QFixedSize

    Parameters
    ----------

    _width : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    _height : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  QFixedSize::QFixedSize(QFixed _width, QFixed _height)
    self._noteCreation(QFixedSize, lambda: Rituals.call(
        'ritual_ZN10QFixedSizeC1E6QFixedS0_',
        self._valueOf(_width), self._valueOf(_height),
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
