"""
QSvgStaticStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgStaticStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QSvgStaticStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgStaticStyle: a plain Python object standing in
  front of one C++ QSvgStaticStyle.

  What exists
  -----------

  Every function of Qt's QSvgStaticStyle that has a ritual and that Python
  can call so far, 2 names in all: 'property', 'isDefaultProperty'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgStaticStyle::~QSvgStaticStyle()': the destructor: Python never
    removes a C++ QSvgStaticStyle.
  - Qt's 'void QSvgStaticStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgStaticStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QSvgStaticStyle is created at the first use, not by
    'QSvgStaticStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgStaticStyle.
  - Each name of Qt's QSvgStaticStyle that has no cute function yet,
    'appendProperty', 'apply', 'revert', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgStaticStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSvgStyleProperty.Type)
  def property(
      self,
      type: QSvgStyleProperty.Type,
  ) -> Optional[QSvgStyleProperty]:
    """
    Calls Qt's 'QSvgStyleProperty
    *QSvgStaticStyle::property(QSvgStyleProperty::Type type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstaticstyle.html#property

    Parameters
    ----------

    type : QSvgStyleProperty.Type
      Passed on as its number.

    Returns
    -------

    Optional[QSvgStyleProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgStyleProperty *QSvgStaticStyle::property(QSvgStyleProperty::Type
    #      type) const
    address = self.uglySide.call(
        'ritual_ZNK15QSvgStaticStyle8propertyEN17QSvgStyleProperty4TypeE',
        type.value,
    )
    return QSvgStyleProperty._cuteAt(address)

  @overload(QSvgStyleProperty.Type)
  def isDefaultProperty(self, type: QSvgStyleProperty.Type) -> bool:
    """
    Calls Qt's 'bool
    QSvgStaticStyle::isDefaultProperty(QSvgStyleProperty::Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstaticstyle.html#isDefaultProperty

    Parameters
    ----------

    type : QSvgStyleProperty.Type
      Passed on as its number.
    """
    #  bool QSvgStaticStyle::isDefaultProperty(QSvgStyleProperty::Type type)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QSvgStaticStyle17isDefaultPropertyEN17QSvgStylePropert'
        'y4TypeE',
        type.value,
    )

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
    Notes what was given, for Qt's 'QSvgStaticStyle::QSvgStaticStyle()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstaticstyle.html#QSvgStaticStyle
    """
    #  QSvgStaticStyle::QSvgStaticStyle()
    self._noteCreation(QSvgStaticStyle, lambda: Rituals.call(
        'ritual_ZN15QSvgStaticStyleC1Ev',
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

  @staticmethod
  def appendProperty(*__, **_) -> Never:
    """
    Qt's 'void QSvgStaticStyle::appendProperty(QSvgStylePropertyPtr prop)':
    the compiler refuses its ritual as it would be written here: call to
    deleted constructor of 'QSvgStylePropertyPtr' (aka
    'std::unique_ptr<QSvgStyleProperty>').
    """
    raise NotImplementedError(
        "'QSvgStaticStyle.appendProperty' has no cute function yet. Qt's "
        "'void QSvgStaticStyle::appendProperty(QSvgStylePropertyPtr prop)': "
        "the compiler refuses its ritual as it would be written here: call "
        "to deleted constructor of 'QSvgStylePropertyPtr' (aka "
        "'std::unique_ptr<QSvgStyleProperty>').")

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QSvgStaticStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSvgStaticStyle.apply' has no cute function yet. Qt's 'void "
        "QSvgStaticStyle::apply(QPainter *p, const QSvgNode *node, "
        "QSvgExtraStates &states)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def revert(*__, **_) -> Never:
    """
    Qt's 'void QSvgStaticStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgStaticStyle.revert' has no cute function yet. Qt's 'void "
        "QSvgStaticStyle::revert(QPainter *p, QSvgExtraStates &states)': "
        "takes a type Python has no way to hand over yet.")
