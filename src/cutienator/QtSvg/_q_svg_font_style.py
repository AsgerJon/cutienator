"""
QSvgFontStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgFontStyle to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QFont
from . import QSvgStyleProperty


class QSvgFontStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgFontStyle: a plain Python object standing in
  front of one C++ QSvgFontStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgFontStyle is built
  on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgFontStyle around as a copy, so every C++ QSvgFontStyle
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgFontStyle that has a ritual and that Python can
  call so far, 8 names in all: 'type', 'setSize', 'setTextAnchor',
  'setFamily', 'setStyle', 'setVariant', 'setWeight', 'qfont'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFontStyle::~QSvgFontStyle()': the destructor: Python removes
    its C++ QSvgFontStyle by it, and has no other use for it.
  - Qt's 'void QSvgFontStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgFontStyle::revert(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgFontStyle is created at the first use, not by
    'QSvgFontStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgFontStyle back gives a copy the ritual made for
    Python, in a new cute QSvgFontStyle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgFontStyle'

  #  A C++ QSvgFontStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFontStyle'

  #  Qt's '~QSvgFontStyle()'. Naming it makes this a value class: Python owns
  #  every C++ QSvgFontStyle behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QSvgFontStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgFontStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgFontStyle::type() const
    ritual = 'ritual_ZNK13QSvgFontStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSvgFontStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  def qfont(self) -> QFont:
    """
    Calls Qt's 'const QFont &QSvgFontStyle::qfont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#qfont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  const QFont &QSvgFontStyle::qfont() const
    address = self.uglySide.call('ritual_ZNK13QSvgFontStyle5qfontEv')
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSize(self, size: float) -> None:
    """
    Calls Qt's 'void QSvgFontStyle::setSize(qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#setSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QSvgFontStyle::setSize(qreal size)
    self.uglySide.call('ritual_ZN13QSvgFontStyle7setSizeEd', size)

  @overload(Qt.Alignment)
  def setTextAnchor(self, anchor: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QSvgFontStyle::setTextAnchor(Qt::Alignment anchor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#setTextAnchor

    Parameters
    ----------

    anchor : Qt.Alignment
      Passed on as its number.
    """
    #  void QSvgFontStyle::setTextAnchor(Qt::Alignment anchor)
    self.uglySide.call(
        'ritual_ZN13QSvgFontStyle13setTextAnchorE6QFlagsIN2Qt13AlignmentFla'
        'gEE',
        anchor.value,
    )

  @overload(str)
  def setFamily(self, family: str) -> None:
    """
    Calls Qt's 'void QSvgFontStyle::setFamily(const QString &family)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#setFamily

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgFontStyle::setFamily(const QString &family)
    self.uglySide.call(
        'ritual_ZN13QSvgFontStyle9setFamilyERK7QString', family,
    )

  @overload(QFont.Style)
  def setStyle(self, fontStyle: QFont.Style) -> None:
    """
    Calls Qt's 'void QSvgFontStyle::setStyle(QFont::Style fontStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#setStyle

    Parameters
    ----------

    fontStyle : QFont.Style
      Passed on as its number.
    """
    #  void QSvgFontStyle::setStyle(QFont::Style fontStyle)
    self.uglySide.call(
        'ritual_ZN13QSvgFontStyle8setStyleEN5QFont5StyleE', fontStyle.value,
    )

  @overload(QFont.Capitalization)
  def setVariant(self, fontVariant: QFont.Capitalization) -> None:
    """
    Calls Qt's 'void QSvgFontStyle::setVariant(QFont::Capitalization
    fontVariant)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#setVariant

    Parameters
    ----------

    fontVariant : QFont.Capitalization
      Passed on as its number.
    """
    #  void QSvgFontStyle::setVariant(QFont::Capitalization fontVariant)
    self.uglySide.call(
        'ritual_ZN13QSvgFontStyle10setVariantEN5QFont14CapitalizationE',
        fontVariant.value,
    )

  @overload(int)
  def setWeight(self, weight: int) -> None:
    """
    Calls Qt's 'void QSvgFontStyle::setWeight(int weight)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#setWeight

    Parameters
    ----------

    weight : int
      Passed on as it is.
    """
    #  void QSvgFontStyle::setWeight(int weight)
    self.uglySide.call('ritual_ZN13QSvgFontStyle9setWeightEi', weight)

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
    Notes what was given, for Qt's 'QSvgFontStyle::QSvgFontStyle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfontstyle.html#QSvgFontStyle
    """
    #  QSvgFontStyle::QSvgFontStyle()
    self._noteCreation(QSvgFontStyle, lambda: Rituals.call(
        'ritual_ZN13QSvgFontStyleC1Ev',
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
