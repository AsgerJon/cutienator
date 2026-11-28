"""
QDBusAbstractAdaptorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDBusAbstractAdaptorPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDBusAbstractAdaptor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusAbstractAdaptor = WAIT['QDBusAbstractAdaptor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusAbstractAdaptorPrivate(QObjectPrivate):
  """
  The cute side of Qt's QDBusAbstractAdaptorPrivate: a plain Python object
  standing in front of one C++ QDBusAbstractAdaptorPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QDBusAbstractAdaptorPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusAbstractAdaptorPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'q_func',
  'retrieveIntrospectionXml', 'saveIntrospectionXml'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDBusAbstractAdaptor *QDBusAbstractAdaptorPrivate::q_func()
    const': takes in Python what 'QDBusAbstractAdaptor
    *QDBusAbstractAdaptorPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QDBusAbstractAdaptorPrivate is created at the first use, not by
    'QDBusAbstractAdaptorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusAbstractAdaptorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDBusAbstractAdaptor)
  @overload(NoneType)
  def retrieveIntrospectionXml(
      adaptor: Optional[QDBusAbstractAdaptor],
  ) -> str:
    """
    Calls Qt's 'QString
    QDBusAbstractAdaptorPrivate::retrieveIntrospectionXml(
    QDBusAbstractAdaptor *adaptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptorprivate.html

    Parameters
    ----------

    adaptor : Optional[QDBusAbstractAdaptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusAbstractAdaptorPrivate::retrieveIntrospectionXml(
    #      QDBusAbstractAdaptor *adaptor)
    return Rituals.call(
        'ritual_ZN27QDBusAbstractAdaptorPrivate24retrieveIntrospectionXmlEP'
        '20QDBusAbstractAdaptor',
        CuteMixin._addressOf(adaptor),
    )

  @staticmethod
  @overload(QDBusAbstractAdaptor, str)
  @overload(NoneType, str)
  def saveIntrospectionXml(
      adaptor: Optional[QDBusAbstractAdaptor],
      xml: str,
  ) -> None:
    """
    Calls Qt's 'void
    QDBusAbstractAdaptorPrivate::saveIntrospectionXml(QDBusAbstractAdaptor
    *adaptor, const QString &xml)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptorprivate.html

    Parameters
    ----------

    adaptor : Optional[QDBusAbstractAdaptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xml : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusAbstractAdaptorPrivate::saveIntrospectionXml(
    #      QDBusAbstractAdaptor *adaptor, const QString &xml)
    Rituals.call(
        'ritual_ZN27QDBusAbstractAdaptorPrivate20saveIntrospectionXmlEP20QD'
        'BusAbstractAdaptorRK7QString',
        CuteMixin._addressOf(adaptor), xml,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusAbstractAdaptorPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDBusAbstractAdaptorPrivate::QDBusAbstractAdaptorPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptorprivate.html
    """
    #  QDBusAbstractAdaptorPrivate::QDBusAbstractAdaptorPrivate()
    self._noteCreation(QDBusAbstractAdaptorPrivate, lambda: Rituals.call(
        'ritual_ZN27QDBusAbstractAdaptorPrivateC1Ev',
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

  def q_func(self) -> Optional[QDBusAbstractAdaptor]:
    """
    Calls Qt's 'QDBusAbstractAdaptor *QDBusAbstractAdaptorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractadaptorprivate.html#q_func

    Returns
    -------

    Optional[QDBusAbstractAdaptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusAbstractAdaptor *QDBusAbstractAdaptorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QDBusAbstractAdaptorPrivate6q_funcEv',
    )
    from . import QDBusAbstractAdaptor
    return QDBusAbstractAdaptor._cuteAt(address)
