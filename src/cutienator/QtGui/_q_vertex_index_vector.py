"""
QVertexIndexVector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtriangulator_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVertexIndexVector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QVertexIndexVector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVertexIndexVector: a plain Python object standing in
  front of one C++ QVertexIndexVector.

  C++ hands a QVertexIndexVector around as a copy, so every C++
  QVertexIndexVector behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVertexIndexVector that has a ritual and that Python
  can call so far, 2 names in all: 'type', 'size'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QVertexIndexVector::setDataUint(const QList<quint32> &data)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QVertexIndexVector::setDataUshort(const QList<quint16>
    &data)': takes a type Python has no way to hand over yet.
  - Qt's 'const void *QVertexIndexVector::data() const': gives 'void', which
    has no cute class yet.
  - Qt's 'QVertexIndexVector::~QVertexIndexVector()': the destructor: Python
    removes its C++ QVertexIndexVector by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QVertexIndexVector is created at the first use, not by
    'QVertexIndexVector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVertexIndexVector back gives a copy the ritual made
    for Python, in a new cute QVertexIndexVector.
  - Each name of Qt's QVertexIndexVector that has no cute function yet,
    'data', 'setDataUint', 'setDataUshort', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QVertexIndexVector, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QVertexIndexVector::Type' of Qt, with the 2 names Qt gives in
    it.
    """

    UnsignedInt = Kee[int](0)
    UnsignedShort = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVertexIndexVector'

  #  Qt's '~QVertexIndexVector()'. Naming it makes this a value class: Python
  #  owns every C++ QVertexIndexVector behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QVertexIndexVectorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QVertexIndexVector::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvertexindexvector.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QVertexIndexVector::type() const
    return QVertexIndexVector.Type(self.uglySide.call(
        'ritual_ZNK18QVertexIndexVector4typeEv',
    ))

  def size(self) -> int:
    """
    Calls Qt's 'int QVertexIndexVector::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvertexindexvector.html#size
    """
    #  int QVertexIndexVector::size() const
    return self.uglySide.call('ritual_ZNK18QVertexIndexVector4sizeEv')

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

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'const void *QVertexIndexVector::data() const': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QVertexIndexVector.data' has no cute function yet. Qt's 'const "
        "void *QVertexIndexVector::data() const': gives 'void', which has "
        "no cute class yet.")

  @staticmethod
  def setDataUint(*__, **_) -> Never:
    """
    Qt's 'void QVertexIndexVector::setDataUint(const QList<quint32> &data)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVertexIndexVector.setDataUint' has no cute function yet. Qt's "
        "'void QVertexIndexVector::setDataUint(const QList<quint32> "
        "&data)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setDataUshort(*__, **_) -> Never:
    """
    Qt's 'void QVertexIndexVector::setDataUshort(const QList<quint16>
    &data)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVertexIndexVector.setDataUshort' has no cute function yet. Qt's "
        "'void QVertexIndexVector::setDataUshort(const QList<quint16> "
        "&data)': takes a type Python has no way to hand over yet.")
