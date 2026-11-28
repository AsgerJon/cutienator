"""
QSvgCssProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgcssproperties_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSvgCssProperties to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QXmlStreamAttributes
  from . import QSvgOffsetProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QXmlStreamAttributes = WAIT['QXmlStreamAttributes']


class QSvgCssProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgCssProperties: a plain Python object standing in
  front of one C++ QSvgCssProperties.

  C++ hands a QSvgCssProperties around as a copy, so every C++
  QSvgCssProperties behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgCssProperties that has a ritual and that Python
  can call so far, 1 name in all: 'offset'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgCssProperties::~QSvgCssProperties()': the destructor: Python
    removes its C++ QSvgCssProperties by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSvgCssProperties is created at the first use, not by
    'QSvgCssProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgCssProperties back gives a copy the ritual made
    for Python, in a new cute QSvgCssProperties.
  - Each name of Qt's QSvgCssProperties that has no cute function yet,
    'animations', 'shortHandtoLonghandForm', holds a function that raises
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
  __qt_class__ = 'QSvgCssProperties'

  #  Qt's '~QSvgCssProperties()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgCssProperties behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSvgCssPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def offset(self) -> QSvgOffsetProperty:
    """
    Calls Qt's 'QSvgOffsetProperty QSvgCssProperties::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcssproperties.html#offset

    Returns
    -------

    QSvgOffsetProperty
      A new cute QSvgOffsetProperty around the copy Qt gave back. Python owns
      it.
    """
    #  QSvgOffsetProperty QSvgCssProperties::offset() const
    address = self.uglySide.call('ritual_ZNK17QSvgCssProperties6offsetEv')
    from . import QSvgOffsetProperty
    return QSvgOffsetProperty._cuteOwning(address)

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

  @overload(QXmlStreamAttributes)
  def __init__(self, attributes: QXmlStreamAttributes) -> None:
    """
    Notes what was given, for Qt's
    'QSvgCssProperties::QSvgCssProperties(const QXmlStreamAttributes
    &attributes)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcssproperties.html#QSvgCssProperties

    Parameters
    ----------

    attributes : QXmlStreamAttributes
      Passed on as a value: Qt reads the C++ QXmlStreamAttributes, which
      stays Python's own.
    """
    #  QSvgCssProperties::QSvgCssProperties(const QXmlStreamAttributes
    #      &attributes)
    self._noteCreation(QSvgCssProperties, lambda: Rituals.call(
        'ritual_ZN17QSvgCssPropertiesC1ERK20QXmlStreamAttributes',
        self._valueOf(attributes),
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
  def animations(*__, **_) -> Never:
    """
    Qt's 'QList<QSvgAnimationProperty> QSvgCssProperties::animations()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'parseCssClockValue'.
    """
    raise NotImplementedError(
        "'QSvgCssProperties.animations' has no cute function yet. Qt's "
        "'QList<QSvgAnimationProperty> QSvgCssProperties::animations() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'parseCssClockValue'.")

  @staticmethod
  def shortHandtoLonghandForm(*__, **_) -> Never:
    """
    Qt's 'void QSvgCssProperties::shortHandtoLonghandForm(QStringView
    value)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isTimeValue'.
    """
    raise NotImplementedError(
        "'QSvgCssProperties.shortHandtoLonghandForm' has no cute function "
        "yet. Qt's 'void "
        "QSvgCssProperties::shortHandtoLonghandForm(QStringView value)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'isTimeValue'.")
