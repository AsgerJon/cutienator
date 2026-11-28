"""
QtProtobufPrivate::QProtobufPropertyOrderingBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufpropertyorderingbuilder_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtProtobufPrivate::QProtobufPropertyOrderingBuilder to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtProtobufPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QProtobufPropertyOrderingBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtProtobufPrivate::QProtobufPropertyOrderingBuilder:
  a plain Python object standing in front of one C++
  QtProtobufPrivate::QProtobufPropertyOrderingBuilder.

  What exists
  -----------

  Every function of Qt's QtProtobufPrivate::QProtobufPropertyOrderingBuilder
  that has a ritual and that Python can call so far, 2 names in all:
  'addV0Field', 'build'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtProtobufPrivate::QProtobufPropertyOrderingBuilder::
    ~QProtobufPropertyOrderingBuilder()': the destructor: Python never
    removes a C++ QtProtobufPrivate::QProtobufPropertyOrderingBuilder.

  What has no ritual
  ------------------

  6 of the 10 functions Qt declares: 4 forbidden; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtProtobufPrivate::QProtobufPropertyOrderingBuilder is created at
    the first use, not by
    'QtProtobufPrivate::QProtobufPropertyOrderingBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtProtobufPrivate::QProtobufPropertyOrderingBuilder.
  - Each name of Qt's QtProtobufPrivate::QProtobufPropertyOrderingBuilder
    that has no cute function yet, 'd_func', holds a function that raises
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
  __qt_class__ = 'QtProtobufPrivate::QProtobufPropertyOrderingBuilder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def build(
      self,
  ) -> Optional[QtProtobufPrivate.QProtobufPropertyOrdering.Data]:
    """
    Calls Qt's 'QProtobufPropertyOrdering::Data
    *QtProtobufPrivate::QProtobufPropertyOrderingBuilder::build() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyorderingbuilder.html

    Returns
    -------

    Optional[QtProtobufPrivate.QProtobufPropertyOrdering.Data]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProtobufPropertyOrdering::Data
    #      *QtProtobufPrivate::QProtobufPropertyOrderingBuilder::build()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate32QProtobufPropertyOrderingBuilder5bu'
        'ildEv',
    )
    return QtProtobufPrivate.QProtobufPropertyOrdering.Data._cuteAt(address)

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

  @overload(QByteArray)
  def __init__(self, packageName: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QtProtobufPrivate::QProtobufPropertyOrderingBuilder::
    QProtobufPropertyOrderingBuilder(QByteArray packageName)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyorderingbuilder.html

    Parameters
    ----------

    packageName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QtProtobufPrivate::QProtobufPropertyOrderingBuilder::
    #      QProtobufPropertyOrderingBuilder(QByteArray packageName)
    self._noteCreation(
        QProtobufPropertyOrderingBuilder, lambda: Rituals.call(
            'ritual_ZN17QtProtobufPrivate32QProtobufPropertyOrderingBuilder'
            'C1E10QByteArray',
            self._valueOf(packageName),
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

  @overload(QByteArray, int, int, QtProtobufPrivate.FieldFlags)
  def addV0Field(
      self,
      jsonName: QByteArray,
      fieldNumber: int,
      propertyIndex: int,
      flags: QtProtobufPrivate.FieldFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QtProtobufPrivate::QProtobufPropertyOrderingBuilder::addV0Field(
    QByteArray jsonName, uint fieldNumber, uint propertyIndex, FieldFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyorderingbuilder.html

    Parameters
    ----------

    jsonName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    fieldNumber : int
      Passed on as it is.

    propertyIndex : int
      Passed on as it is.

    flags : QtProtobufPrivate.FieldFlags
      Passed on as its number.
    """
    #  void QtProtobufPrivate::QProtobufPropertyOrderingBuilder::addV0Field(
    #      QByteArray jsonName, uint fieldNumber, uint propertyIndex,
    #      FieldFlags flags)
    self.uglySide.call(
        'ritual_ZN17QtProtobufPrivate32QProtobufPropertyOrderingBuilder10ad'
        'dV0FieldE10QByteArrayjj6QFlagsINS_9FieldFlagEE',
        self._valueOf(jsonName), fieldNumber, propertyIndex, flags.value,
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QProtobufPropertyOrderingBuilderPrivate
      *QtProtobufPrivate::QProtobufPropertyOrderingBuilder::d_func()': the
      compiler refuses its ritual as it would be written here: unknown type
      name 'QProtobufPropertyOrderingBuilderPrivate'; did you mean
      'QtProtobufPrivate::QProtobufPropertyOrderingBuilderPrivate'?.
    - Qt's 'const QProtobufPropertyOrderingBuilderPrivate
      *QtProtobufPrivate::QProtobufPropertyOrderingBuilder::d_func() const':
      the compiler refuses its ritual as it would be written here: unknown
      type name 'QProtobufPropertyOrderingBuilderPrivate'; did you mean
      'QtProtobufPrivate::QProtobufPropertyOrderingBuilderPrivate'?.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufPropertyOrderingBuilder.d_func' has no "
        "cute function yet. Qt's 'QProtobufPropertyOrderingBuilderPrivate "
        "*QtProtobufPrivate::QProtobufPropertyOrderingBuilder::d_func()': "
        "the compiler refuses its ritual as it would be written here: "
        "unknown type name 'QProtobufPropertyOrderingBuilderPrivate'; did "
        "you mean "
        "'QtProtobufPrivate::QProtobufPropertyOrderingBuilderPrivate'?. "
        "Qt's 'const QProtobufPropertyOrderingBuilderPrivate "
        "*QtProtobufPrivate::QProtobufPropertyOrderingBuilder::d_func() "
        "const': the compiler refuses its ritual as it would be written "
        "here: unknown type name 'QProtobufPropertyOrderingBuilderPrivate'; "
        "did you mean "
        "'QtProtobufPrivate::QProtobufPropertyOrderingBuilderPrivate'?.")
