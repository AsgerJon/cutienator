"""
Qt3DCore::QAbstractServiceProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qservicelocator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QAbstractServiceProvider to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractServiceProvider(QObject):
  """
  The cute side of Qt's Qt3DCore::QAbstractServiceProvider: a plain Python
  object standing in front of one C++ Qt3DCore::QAbstractServiceProvider.

  It is built on the cute 'QObject', as Qt's
  Qt3DCore::QAbstractServiceProvider is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractServiceProvider that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'type', 'description', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAbstractServiceProvider::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::QAbstractServiceProvider::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QAbstractServiceProvider::~QAbstractServiceProvider()':
    the destructor: Python never removes a C++
    Qt3DCore::QAbstractServiceProvider.
  - Qt's 'Qt3DCore::QAbstractServiceProvider::QAbstractServiceProvider(
    QAbstractServiceProviderPrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QAbstractServiceProviderPrivate
    *Qt3DCore::QAbstractServiceProvider::d_func() const': takes in Python
    what 'QAbstractServiceProviderPrivate
    *Qt3DCore::QAbstractServiceProvider::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractServiceProvider is created at the first use,
    not by 'Qt3DCore::QAbstractServiceProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractServiceProvider.
  - Qt tells when it has removed the C++ Qt3DCore::QAbstractServiceProvider.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QAbstractServiceProvider::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractserviceprovider.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAbstractServiceProvider::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore24QAbstractServiceProvider2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractServiceProvider'

  #  A C++ Qt3DCore::QAbstractServiceProvider Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAbstractServiceProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::QAbstractServiceProvider::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractserviceprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QAbstractServiceProvider::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore24QAbstractServiceProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QAbstractServiceProvider::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractserviceprovider.html#type
    """
    #  int Qt3DCore::QAbstractServiceProvider::type() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore24QAbstractServiceProvider4typeEv',
    )

  def description(self) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QAbstractServiceProvider::description()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractserviceprovider.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QAbstractServiceProvider::description() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore24QAbstractServiceProvider11descriptionEv',
    )

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

  @overload(int, str)
  @overload(int, str, QObject)
  @overload(int, str, NoneType)
  def __init__(
      self,
      type: int,
      description: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QAbstractServiceProvider::QAbstractServiceProvider(int type,
    const QString &description, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractserviceprovider.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    description : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAbstractServiceProvider::QAbstractServiceProvider(int type,
    #      const QString &description, QObject *parent)
    self._noteCreation(QAbstractServiceProvider, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore24QAbstractServiceProviderC1EiRK7QStringP7QObjec'
        't',
        type, description, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[Qt3DCore.QAbstractServiceProviderPrivate]:
    """
    Calls Qt's 'QAbstractServiceProviderPrivate
    *Qt3DCore::QAbstractServiceProvider::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractserviceprovider.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QAbstractServiceProviderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractServiceProviderPrivate
    #      *Qt3DCore::QAbstractServiceProvider::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore24QAbstractServiceProvider6d_funcEv',
    )
    return Qt3DCore.QAbstractServiceProviderPrivate._cuteAt(address)
