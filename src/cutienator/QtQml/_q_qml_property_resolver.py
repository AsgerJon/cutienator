"""
QQmlPropertyResolver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertyresolver_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlPropertyResolver to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlPropertyData


class QQmlPropertyResolver(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyResolver: a plain Python object standing
  in front of one C++ QQmlPropertyResolver.

  C++ hands a QQmlPropertyResolver around as a copy, so every C++
  QQmlPropertyResolver behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPropertyResolver that has a ritual and that
  Python can call so far, 1 name in all: 'property'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlPropertyData *QQmlPropertyResolver::property(const
    QString &name, bool *notInRevision, RevisionCheck check) const': takes a
    number to change where it is.
  - Qt's 'const QQmlPropertyData *QQmlPropertyResolver::signal(const QString
    &name, bool *notInRevision, RevisionCheck check) const': takes a number
    to change where it is.
  - Qt's 'QQmlPropertyResolver::~QQmlPropertyResolver()': the destructor:
    Python removes its C++ QQmlPropertyResolver by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlPropertyResolver is created at the first use, not by
    'QQmlPropertyResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPropertyResolver back gives a copy the ritual
    made for Python, in a new cute QQmlPropertyResolver.
  - Each name of Qt's QQmlPropertyResolver that has no cute function yet,
    'signal', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQmlPropertyResolver, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class RevisionCheck(CuteNum):
    """
    The enum 'QQmlPropertyResolver::RevisionCheck' of Qt, with the 2 names Qt
    gives in it.
    """

    CheckRevision = Kee[int](0)
    IgnoreRevision = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyResolver'

  #  Qt's '~QQmlPropertyResolver()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlPropertyResolver behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlPropertyResolverD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def property(self, index: int) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData *QQmlPropertyResolver::property(int
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyresolver.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QQmlPropertyResolver::property(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlPropertyResolver8propertyEi', index,
    )
    from . import QQmlPropertyData
    return QQmlPropertyData._cuteAt(address)

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

  @overload(QQmlPropertyCache.ConstPtr)
  def __init__(self, cache: QQmlPropertyCache.ConstPtr) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPropertyResolver::QQmlPropertyResolver(const
    QQmlPropertyCache::ConstPtr &cache)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyresolver.html#QQmlPropertyResolver

    Parameters
    ----------

    cache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  QQmlPropertyResolver::QQmlPropertyResolver(const
    #      QQmlPropertyCache::ConstPtr &cache)
    self._noteCreation(QQmlPropertyResolver, lambda: Rituals.call(
        'ritual_ZN20QQmlPropertyResolverC1ERKN17QQmlPropertyCache8ConstPtrE',
        self._valueOf(cache),
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

  @staticmethod
  def signal(*__, **_) -> Never:
    """
    Qt's 'const QQmlPropertyData *QQmlPropertyResolver::signal(const QString
    &name, bool *notInRevision, RevisionCheck check) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QQmlPropertyResolver.signal' has no cute function yet. Qt's "
        "'const QQmlPropertyData *QQmlPropertyResolver::signal(const "
        "QString &name, bool *notInRevision, RevisionCheck check) const': "
        "takes a number to change where it is.")
