"""
QQmlJSAnnotation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsannotation_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSAnnotation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QQQmlJSDeprecation


class QQmlJSAnnotation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSAnnotation: a plain Python object standing in
  front of one C++ QQmlJSAnnotation.

  C++ hands a QQmlJSAnnotation around as a copy, so every C++
  QQmlJSAnnotation behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSAnnotation that has a ritual and that Python
  can call so far, 2 names in all: 'isDeprecation', 'deprecation'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSAnnotation::~QQmlJSAnnotation()': the destructor: Python
    removes its C++ QQmlJSAnnotation by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 leans on 'operator==(QQmlJSAnnotation
  const&, QQmlJSAnnotation const&)', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQmlJSAnnotation is created at the first use, not by
    'QQmlJSAnnotation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSAnnotation back gives a copy the ritual made
    for Python, in a new cute QQmlJSAnnotation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSAnnotation'

  #  Qt's '~QQmlJSAnnotation()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSAnnotation behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlJSAnnotationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isDeprecation(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSAnnotation::isDeprecation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsannotation.html#isDeprecation
    """
    #  bool QQmlJSAnnotation::isDeprecation() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSAnnotation13isDeprecationEv',
    )

  def deprecation(self) -> QQQmlJSDeprecation:
    """
    Calls Qt's 'QQQmlJSDeprecation QQmlJSAnnotation::deprecation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsannotation.html#deprecation

    Returns
    -------

    QQQmlJSDeprecation
      A new cute QQQmlJSDeprecation around the copy Qt gave back. Python owns
      it.
    """
    #  QQQmlJSDeprecation QQmlJSAnnotation::deprecation() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlJSAnnotation11deprecationEv',
    )
    from . import QQQmlJSDeprecation
    return QQQmlJSDeprecation._cuteOwning(address)

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


#  Qt's 'QList<QQmlJSAnnotation>': the list of QQmlJSAnnotation, which
#  'QList[QQmlJSAnnotation]' gives. It is made here, so that there is one as
#  soon as there can be a QQmlJSAnnotation.
QList.createKind(
    QQmlJSAnnotation, 'value',
    make='ritual_list_make_QQmlJSAnnotation',
    add='ritual_list_add_QQmlJSAnnotation',
    size='ritual_list_size_QQmlJSAnnotation',
    at='ritual_list_at_QQmlJSAnnotation',
    drop='ritual_list_drop_QQmlJSAnnotation',
)
