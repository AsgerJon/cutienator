"""
QWebChannelPropertyChangeNotifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebChannel/6.12.0/QtWebChannel/private/qmetaobjectpublisher_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWebChannelPropertyChangeNotifier to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QPropertyObserver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QUntypedPropertyData
  from . import QMetaObjectPublisher
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObjectPublisher = WAIT['QMetaObjectPublisher']
  QObject = WAIT['QObject']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebChannelPropertyChangeNotifier(QPropertyObserver):
  """
  The cute side of Qt's QWebChannelPropertyChangeNotifier: a plain Python
  object standing in front of one C++ QWebChannelPropertyChangeNotifier.

  It is built on the cute 'QPropertyObserver', as Qt's
  QWebChannelPropertyChangeNotifier is built on Qt's QPropertyObserver, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebChannelPropertyChangeNotifier that has a ritual
  and that Python can call so far, 1 name in all: 'notify'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QWebChannelPropertyChangeNotifier is created at the first use,
    not by 'QWebChannelPropertyChangeNotifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebChannelPropertyChangeNotifier.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPropertyObserver, QUntypedPropertyData)
  @overload(QPropertyObserver, NoneType)
  @overload(NoneType, QUntypedPropertyData)
  @overload(NoneType, NoneType)
  def notify(
      a0: Optional[QPropertyObserver],
      a1: Optional[QUntypedPropertyData],
  ) -> None:
    """
    Calls Qt's 'void
    QWebChannelPropertyChangeNotifier::notify(QPropertyObserver *a0,
    QUntypedPropertyData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannelpropertychangenotifier.html#notify

    Parameters
    ----------

    a0 : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebChannelPropertyChangeNotifier::notify(QPropertyObserver *a0,
    #      QUntypedPropertyData *a1)
    Rituals.call(
        'ritual_ZN33QWebChannelPropertyChangeNotifier6notifyEP17QPropertyOb'
        'serverP20QUntypedPropertyData',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebChannelPropertyChangeNotifier'

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

  @overload(QMetaObjectPublisher, QObject, int)
  @overload(QMetaObjectPublisher, NoneType, int)
  @overload(NoneType, QObject, int)
  @overload(NoneType, NoneType, int)
  def __init__(
      self,
      publisher: Optional[QMetaObjectPublisher],
      object: Optional[QObject],
      propertyIndex: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebChannelPropertyChangeNotifier::QWebChannelPropertyChangeNotifier(
    QMetaObjectPublisher *publisher, const QObject *object, int
    propertyIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannelpropertychangenotifier.html

    Parameters
    ----------

    publisher : Optional[QMetaObjectPublisher]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.
    """
    #  QWebChannelPropertyChangeNotifier::
    #      QWebChannelPropertyChangeNotifier(QMetaObjectPublisher *publisher,
    #      const QObject *object, int propertyIndex)
    self._noteCreation(
        QWebChannelPropertyChangeNotifier, lambda: Rituals.call(
            'ritual_ZN33QWebChannelPropertyChangeNotifierC1EP20QMetaObjectP'
            'ublisherPK7QObjecti',
            self._addressOf(publisher), self._addressOf(object, 'QObject'),
            propertyIndex,
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
