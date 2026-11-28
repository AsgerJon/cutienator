"""
QQmlListReferencePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllist_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlListReferencePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQmlListReference
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlListReference = WAIT['QQmlListReference']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlListReferencePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlListReferencePrivate: a plain Python object
  standing in front of one C++ QQmlListReferencePrivate.

  C++ hands a QQmlListReferencePrivate around as a copy, so every C++
  QQmlListReferencePrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlListReferencePrivate that has a ritual and that
  Python can call so far, 4 names in all: 'addref', 'release', 'get',
  'elementType'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlListReference QQmlListReferencePrivate::init(const
    QQmlListProperty<QObject> &a0, QMetaType a1)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlListReferencePrivate::~QQmlListReferencePrivate()': the
    destructor: Python removes its C++ QQmlListReferencePrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlListReferencePrivate is created at the first use, not by
    'QQmlListReferencePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlListReferencePrivate back gives a copy the ritual
    made for Python, in a new cute QQmlListReferencePrivate.
  - Each name of Qt's QQmlListReferencePrivate that has no cute function yet,
    'init', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlListReference)
  @overload(NoneType)
  def get(
      ref: Optional[QQmlListReference],
  ) -> Optional[QQmlListReferencePrivate]:
    """
    Calls Qt's 'QQmlListReferencePrivate
    *QQmlListReferencePrivate::get(QQmlListReference *ref)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreferenceprivate.html#get

    Parameters
    ----------

    ref : Optional[QQmlListReference]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlListReferencePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlListReferencePrivate
    #      *QQmlListReferencePrivate::get(QQmlListReference *ref)
    address = Rituals.call(
        'ritual_ZN24QQmlListReferencePrivate3getEP17QQmlListReference',
        CuteMixin._addressOf(ref),
    )
    return QQmlListReferencePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlListReferencePrivate'

  #  Qt's '~QQmlListReferencePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlListReferencePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQmlListReferencePrivateD1Ev'

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
    'QQmlListReferencePrivate::QQmlListReferencePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreferenceprivate.html
    """
    #  QQmlListReferencePrivate::QQmlListReferencePrivate()
    self._noteCreation(QQmlListReferencePrivate, lambda: Rituals.call(
        'ritual_ZN24QQmlListReferencePrivateC1Ev',
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

  def addref(self) -> None:
    """
    Calls Qt's 'void QQmlListReferencePrivate::addref()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreferenceprivate.html#addref
    """
    #  void QQmlListReferencePrivate::addref()
    self.uglySide.call('ritual_ZN24QQmlListReferencePrivate6addrefEv')

  def release(self) -> None:
    """
    Calls Qt's 'void QQmlListReferencePrivate::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreferenceprivate.html#release
    """
    #  void QQmlListReferencePrivate::release()
    self.uglySide.call('ritual_ZN24QQmlListReferencePrivate7releaseEv')

  def elementType(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlListReferencePrivate::elementType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreferenceprivate.html#elementType

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlListReferencePrivate::elementType()
    address = self.uglySide.call(
        'ritual_ZN24QQmlListReferencePrivate11elementTypeEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'QQmlListReference QQmlListReferencePrivate::init(const
    QQmlListProperty<QObject> &a0, QMetaType a1)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlListReferencePrivate.init' has no cute function yet. Qt's "
        "'QQmlListReference QQmlListReferencePrivate::init(const "
        "QQmlListProperty<QObject> &a0, QMetaType a1)': takes a type Python "
        "has no way to hand over yet.")
