"""
QJsonPrivate::Value binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qjson_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QJsonPrivate::Value to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtCbor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCborContainerPrivate, QCborValue, QJsonValue
  from . import QJsonValueConstRef, QJsonValueRef
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCborValue = WAIT['QCborValue']
  QJsonValueConstRef = WAIT['QJsonValueConstRef']
  QJsonValueRef = WAIT['QJsonValueRef']


class Value(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonPrivate::Value: a plain Python object standing
  in front of one C++ QJsonPrivate::Value.

  C++ hands a QJsonPrivate::Value around as a copy, so every C++
  QJsonPrivate::Value behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonPrivate::Value that has a ritual and that
  Python can call so far, 5 names in all: 'valueHelper', 'container',
  'indexHelper', 'elementHelper', 'fromTrustedCbor'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonPrivate::Value::~Value()': the destructor: Python removes its
    C++ QJsonPrivate::Value by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QJsonPrivate::Value is created at the first use, not by
    'QJsonPrivate::Value(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonPrivate::Value back gives a copy the ritual made
    for Python, in a new cute QJsonPrivate::Value.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCborValue)
  def valueHelper(v: QCborValue) -> int:
    """
    Calls Qt's 'qint64 QJsonPrivate::Value::valueHelper(const QCborValue
    &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonprivate-value.html#valueHelper

    Parameters
    ----------

    v : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  qint64 QJsonPrivate::Value::valueHelper(const QCborValue &v)
    return Rituals.call(
        'ritual_ZN12QJsonPrivate5Value11valueHelperERK10QCborValue',
        CuteMixin._valueOf(v),
    )

  @staticmethod
  @overload(QCborValue)
  def container(v: QCborValue) -> Optional[QCborContainerPrivate]:
    """
    Calls Qt's 'QCborContainerPrivate *QJsonPrivate::Value::container(const
    QCborValue &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonprivate-value.html#container

    Parameters
    ----------

    v : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    Optional[QCborContainerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCborContainerPrivate *QJsonPrivate::Value::container(const QCborValue
    #      &v)
    address = Rituals.call(
        'ritual_ZN12QJsonPrivate5Value9containerERK10QCborValue',
        CuteMixin._valueOf(v),
    )
    from . import QCborContainerPrivate
    return QCborContainerPrivate._cuteAt(address)

  @staticmethod
  @overload(QJsonValueRef)
  def container(r: QJsonValueRef) -> Optional[QCborContainerPrivate]:
    """
    Calls Qt's 'QCborContainerPrivate
    *QJsonPrivate::Value::container(QJsonValueRef r)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonprivate-value.html#container

    Parameters
    ----------

    r : QJsonValueRef
      Passed on as a value: Qt reads the C++ QJsonValueRef, which stays
      Python's own.

    Returns
    -------

    Optional[QCborContainerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCborContainerPrivate *QJsonPrivate::Value::container(QJsonValueRef r)
    address = Rituals.call(
        'ritual_ZN12QJsonPrivate5Value9containerE13QJsonValueRef',
        CuteMixin._valueOf(r),
    )
    from . import QCborContainerPrivate
    return QCborContainerPrivate._cuteAt(address)

  @staticmethod
  @overload(QJsonValueConstRef)
  def container(r: QJsonValueConstRef) -> Optional[QCborContainerPrivate]:
    """
    Calls Qt's 'const QCborContainerPrivate
    *QJsonPrivate::Value::container(QJsonValueConstRef r)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonprivate-value.html#container

    Parameters
    ----------

    r : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    Returns
    -------

    Optional[QCborContainerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCborContainerPrivate
    #      *QJsonPrivate::Value::container(QJsonValueConstRef r)
    address = Rituals.call(
        'ritual_ZN12QJsonPrivate5Value9containerE18QJsonValueConstRef',
        CuteMixin._valueOf(r),
    )
    from . import QCborContainerPrivate
    return QCborContainerPrivate._cuteAt(address)

  @staticmethod
  @overload(QJsonValueConstRef)
  def indexHelper(r: QJsonValueConstRef) -> int:
    """
    Calls Qt's 'qsizetype QJsonPrivate::Value::indexHelper(QJsonValueConstRef
    r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonprivate-value.html#indexHelper

    Parameters
    ----------

    r : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  qsizetype QJsonPrivate::Value::indexHelper(QJsonValueConstRef r)
    return Rituals.call(
        'ritual_ZN12QJsonPrivate5Value11indexHelperE18QJsonValueConstRef',
        CuteMixin._valueOf(r),
    )

  @staticmethod
  @overload(QJsonValueConstRef)
  def elementHelper(r: QJsonValueConstRef) -> QtCbor.Element:
    """
    Calls Qt's 'const QtCbor::Element
    &QJsonPrivate::Value::elementHelper(QJsonValueConstRef r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonprivate-value.html#elementHelper

    Parameters
    ----------

    r : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.

    Returns
    -------

    QtCbor.Element
      A new cute QtCbor::Element around the copy Qt gave back. Python owns
      it.
    """
    #  const QtCbor::Element
    #      &QJsonPrivate::Value::elementHelper(QJsonValueConstRef r)
    address = Rituals.call(
        'ritual_ZN12QJsonPrivate5Value13elementHelperE18QJsonValueConstRef',
        CuteMixin._valueOf(r),
    )
    return QtCbor.Element._cuteOwning(address)

  @staticmethod
  @overload(QCborValue)
  def fromTrustedCbor(v: QCborValue) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonPrivate::Value::fromTrustedCbor(const
    QCborValue &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonprivate-value.html#fromTrustedCbor

    Parameters
    ----------

    v : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonPrivate::Value::fromTrustedCbor(const QCborValue &v)
    address = Rituals.call(
        'ritual_ZN12QJsonPrivate5Value15fromTrustedCborERK10QCborValue',
        CuteMixin._valueOf(v),
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonPrivate::Value'

  #  Qt's '~QJsonPrivate::Value()'. Naming it makes this a value class:
  #  Python owns every C++ QJsonPrivate::Value behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QJsonPrivate5ValueD1Ev'

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
