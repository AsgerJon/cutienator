"""
QProtobufSerializerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QProtobufSerializerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QProtobufSerializerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProtobufSerializerPrivate: a plain Python object
  standing in front of one C++ QProtobufSerializerPrivate.

  What exists
  -----------

  Every function of Qt's QProtobufSerializerPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'clearError'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  8 of the 9 functions Qt declares: 4 forbidden; 2 a template; 1 leans on
  'QProtobufDeserializerImpl; 1 leans on 'QtProtobufSerializerHelpers.

  What to expect
  --------------

  - The C++ QProtobufSerializerPrivate is created at the first use, not by
    'QProtobufSerializerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufSerializerPrivate.
  - Each name of Qt's QProtobufSerializerPrivate that has no cute function
    yet, '__init__', 'serializeNonPackedWrapper', 'serializeWrapper', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QProtobufSerializerPrivate, each a class in
  #  here as in C++.

  class ProtobufSerializationHandler(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QProtobufSerializerPrivate::ProtobufSerializationHandler: a plain Python
    object standing in front of one C++
    QProtobufSerializerPrivate::ProtobufSerializationHandler.

    C++ hands a QProtobufSerializerPrivate::ProtobufSerializationHandler
    around as a copy, so every C++
    QProtobufSerializerPrivate::ProtobufSerializationHandler behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QProtobufSerializerPrivate::ProtobufSerializationHandler yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QProtobufSerializerPrivate::ProtobufSerializationHandler::
      ~ProtobufSerializationHandler()': the destructor: Python removes its
      C++ QProtobufSerializerPrivate::ProtobufSerializationHandler by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QProtobufSerializerPrivate::ProtobufSerializationHandler is
      created at the first use, not by
      'QProtobufSerializerPrivate::ProtobufSerializationHandler(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QProtobufSerializerPrivate::ProtobufSerializationHandler back gives a
      copy the ritual made for Python, in a new cute
      QProtobufSerializerPrivate::ProtobufSerializationHandler.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QProtobufSerializerPrivate::ProtobufSerializationHandler'

    #  Qt's '~QProtobufSerializerPrivate::ProtobufSerializationHandler()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QProtobufSerializerPrivate::ProtobufSerializationHandler behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN26QProtobufSerializerPrivate28ProtobufSerializationHandlerD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufSerializerPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QProtobufSerializerPrivate::QProtobufSerializerPrivate()': leans on
    'QProtobufDeserializerImpl::nextFieldIndex(QProtobufMessage*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QProtobufSerializerPrivate.__init__' has no cute function yet. "
        "Qt's 'QProtobufSerializerPrivate::QProtobufSerializerPrivate()': "
        "leans on "
        "'QProtobufDeserializerImpl::nextFieldIndex(QProtobufMessage*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def clearError(self) -> None:
    """
    Calls Qt's 'void QProtobufSerializerPrivate::clearError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerprivate.html#clearError
    """
    #  void QProtobufSerializerPrivate::clearError()
    self.uglySide.call('ritual_ZN26QProtobufSerializerPrivate10clearErrorEv')

  @staticmethod
  def serializeNonPackedWrapper(*__, **_) -> Never:
    """
    Qt's 'QProtobufSerializerPrivate::serializeNonPackedWrapper': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'QProtobufSerializerPrivate.serializeNonPackedWrapper' has no cute "
        "function yet. Qt's "
        "'QProtobufSerializerPrivate::serializeNonPackedWrapper': a "
        "template: a pattern and no single function.")

  @staticmethod
  def serializeWrapper(*__, **_) -> Never:
    """
    Qt's 'QProtobufSerializerPrivate::serializeWrapper': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QProtobufSerializerPrivate.serializeWrapper' has no cute function "
        "yet. Qt's 'QProtobufSerializerPrivate::serializeWrapper': a "
        "template: a pattern and no single function.")
