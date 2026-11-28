"""
QQmlBindingInstantiationContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlBindingInstantiationContext to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlPropertyCache, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlBindingInstantiationContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlBindingInstantiationContext: a plain Python
  object standing in front of one C++ QQmlBindingInstantiationContext.

  C++ hands a QQmlBindingInstantiationContext around as a copy, so every C++
  QQmlBindingInstantiationContext behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlBindingInstantiationContext that has a ritual
  and that Python can call so far, 2 names in all:
  'resolveInstantiatingProperty', 'instantiatingPropertyCache'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQmlBindingInstantiationContext::~QQmlBindingInstantiationContext()':
    the destructor: Python removes its C++ QQmlBindingInstantiationContext by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlBindingInstantiationContext is created at the first use, not
    by 'QQmlBindingInstantiationContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlBindingInstantiationContext back gives a copy the
    ritual made for Python, in a new cute QQmlBindingInstantiationContext.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlBindingInstantiationContext'

  #  Qt's '~QQmlBindingInstantiationContext()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlBindingInstantiationContext behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QQmlBindingInstantiationContextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def instantiatingPropertyCache(self) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlBindingInstantiationContext::instantiatingPropertyCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbindinginstantiationcontext.html

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlBindingInstantiationContext::instantiatingPropertyCache()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QQmlBindingInstantiationContext26instantiatingProperty'
        'CacheEv',
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

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
    'QQmlBindingInstantiationContext::QQmlBindingInstantiationContext()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbindinginstantiationcontext.html
    """
    #  QQmlBindingInstantiationContext::QQmlBindingInstantiationContext()
    self._noteCreation(QQmlBindingInstantiationContext, lambda: Rituals.call(
        'ritual_ZN31QQmlBindingInstantiationContextC1Ev',
    ))

  @overload(
      int, WAIT['QV4.CompiledData.Binding'], str, QQmlPropertyCache.ConstPtr,
  )
  @overload(int, NoneType, str, QQmlPropertyCache.ConstPtr)
  def __init__(
      self,
      referencingObjectIndex: int,
      instantiatingBinding: Optional[QV4.CompiledData.Binding],
      instantiatingPropertyName: str,
      referencingObjectPropertyCache: QQmlPropertyCache.ConstPtr,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlBindingInstantiationContext::QQmlBindingInstantiationContext(int
    referencingObjectIndex, const QV4::CompiledData::Binding
    *instantiatingBinding, const QString &instantiatingPropertyName, const
    QQmlPropertyCache::ConstPtr &referencingObjectPropertyCache)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbindinginstantiationcontext.html

    Parameters
    ----------

    referencingObjectIndex : int
      Passed on as it is.

    instantiatingBinding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instantiatingPropertyName : str
      Passed on as it is: a QString is made of it for the call.

    referencingObjectPropertyCache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  QQmlBindingInstantiationContext::QQmlBindingInstantiationContext(int
    #      referencingObjectIndex, const QV4::CompiledData::Binding
    #      *instantiatingBinding, const QString &instantiatingPropertyName,
    #      const QQmlPropertyCache::ConstPtr &referencingObjectPropertyCache)
    self._noteCreation(QQmlBindingInstantiationContext, lambda: Rituals.call(
        'ritual_ZN31QQmlBindingInstantiationContextC1EiPKN3QV412CompiledDat'
        'a7BindingERK7QStringRKN17QQmlPropertyCache8ConstPtrE',
        referencingObjectIndex, self._addressOf(instantiatingBinding),
        instantiatingPropertyName,
        self._valueOf(referencingObjectPropertyCache),
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

  def resolveInstantiatingProperty(self) -> bool:
    """
    Calls Qt's 'bool
    QQmlBindingInstantiationContext::resolveInstantiatingProperty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbindinginstantiationcontext.html
    """
    #  bool QQmlBindingInstantiationContext::resolveInstantiatingProperty()
    return self.uglySide.call(
        'ritual_ZN31QQmlBindingInstantiationContext28resolveInstantiatingPr'
        'opertyEv',
    )
