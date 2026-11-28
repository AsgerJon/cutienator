"""
QSvgTransformStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgTransformStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTransform = WAIT['QTransform']


class QSvgTransformStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgTransformStyle: a plain Python object standing in
  front of one C++ QSvgTransformStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgTransformStyle is
  built on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgTransformStyle around as a copy, so every C++
  QSvgTransformStyle behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgTransformStyle that has a ritual and that Python
  can call so far, 3 names in all: 'type', 'qtransform', 'isDefault'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgTransformStyle::~QSvgTransformStyle()': the destructor: Python
    removes its C++ QSvgTransformStyle by it, and has no other use for it.
  - Qt's 'void QSvgTransformStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgTransformStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgTransformStyle is created at the first use, not by
    'QSvgTransformStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgTransformStyle back gives a copy the ritual made
    for Python, in a new cute QSvgTransformStyle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgTransformStyle'

  #  A C++ QSvgTransformStyle Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgTransformStyle'

  #  Qt's '~QSvgTransformStyle()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgTransformStyle behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSvgTransformStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgTransformStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtransformstyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgTransformStyle::type() const
    ritual = 'ritual_ZNK18QSvgTransformStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSvgTransformStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  def qtransform(self) -> QTransform:
    """
    Calls Qt's 'const QTransform &QSvgTransformStyle::qtransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtransformstyle.html#qtransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  const QTransform &QSvgTransformStyle::qtransform() const
    address = self.uglySide.call(
        'ritual_ZNK18QSvgTransformStyle10qtransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QSvgTransformStyle::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtransformstyle.html#isDefault
    """
    #  bool QSvgTransformStyle::isDefault() const
    ritual = 'ritual_ZNK18QSvgTransformStyle9isDefaultEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSvgTransformStyle9isDefaultEv'
    return self.uglySide.call(ritual)

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

  @overload(QTransform)
  def __init__(self, transform: QTransform) -> None:
    """
    Notes what was given, for Qt's
    'QSvgTransformStyle::QSvgTransformStyle(const QTransform &transform)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgtransformstyle.html#QSvgTransformStyle

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QSvgTransformStyle::QSvgTransformStyle(const QTransform &transform)
    self._noteCreation(QSvgTransformStyle, lambda: Rituals.call(
        'ritual_ZN18QSvgTransformStyleC1ERK10QTransform',
        self._valueOf(transform),
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
