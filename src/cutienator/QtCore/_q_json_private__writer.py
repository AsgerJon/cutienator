"""
QJsonPrivate::Writer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qjsonwriter_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QJsonPrivate::Writer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Writer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonPrivate::Writer: a plain Python object standing
  in front of one C++ QJsonPrivate::Writer.

  C++ hands a QJsonPrivate::Writer around as a copy, so every C++
  QJsonPrivate::Writer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QJsonPrivate::Writer yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonPrivate::Writer::~Writer()': the destructor: Python removes
    its C++ QJsonPrivate::Writer by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 4 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QJsonPrivate::Writer is created at the first use, not by
    'QJsonPrivate::Writer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonPrivate::Writer back gives a copy the ritual
    made for Python, in a new cute QJsonPrivate::Writer.
  - Each name of Qt's QJsonPrivate::Writer that has no cute function yet,
    'arrayToJson', 'objectToJson', 'valueToJson', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonPrivate::Writer'

  #  Qt's '~QJsonPrivate::Writer()'. Naming it makes this a value class:
  #  Python owns every C++ QJsonPrivate::Writer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QJsonPrivate6WriterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def arrayToJson(*__, **_) -> Never:
    """
    Qt's 'void QJsonPrivate::Writer::arrayToJson(const QCborContainerPrivate
    *a, QByteArray &json, int indent, bool compact)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'arrayContentToJson'.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Writer.arrayToJson' has no cute function yet. Qt's "
        "'void QJsonPrivate::Writer::arrayToJson(const "
        "QCborContainerPrivate *a, QByteArray &json, int indent, bool "
        "compact)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'arrayContentToJson'.")

  @staticmethod
  def objectToJson(*__, **_) -> Never:
    """
    Qt's 'void QJsonPrivate::Writer::objectToJson(const QCborContainerPrivate
    *o, QByteArray &json, int indent, bool compact)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'objectContentToJson'; did you mean
    'arrayContentToJson'?.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Writer.objectToJson' has no cute function yet. Qt's "
        "'void QJsonPrivate::Writer::objectToJson(const "
        "QCborContainerPrivate *o, QByteArray &json, int indent, bool "
        "compact)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'objectContentToJson'; did you mean "
        "'arrayContentToJson'?.")

  @staticmethod
  def valueToJson(*__, **_) -> Never:
    """
    Qt's 'void QJsonPrivate::Writer::valueToJson(const QCborValue &v,
    QByteArray &json, int indent, bool compact)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'valueContentToJson'; did you mean
    'arrayContentToJson'?.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Writer.valueToJson' has no cute function yet. Qt's "
        "'void QJsonPrivate::Writer::valueToJson(const QCborValue &v, "
        "QByteArray &json, int indent, bool compact)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'valueContentToJson'; "
        "did you mean 'arrayContentToJson'?.")
