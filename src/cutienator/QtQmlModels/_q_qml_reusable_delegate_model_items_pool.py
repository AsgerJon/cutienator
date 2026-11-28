"""
QQmlReusableDelegateModelItemsPool binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlReusableDelegateModelItemsPool to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQml import QQmlComponent
  from . import QQmlDelegateModelItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQmlDelegateModelItem = WAIT['QQmlDelegateModelItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlReusableDelegateModelItemsPool(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlReusableDelegateModelItemsPool: a plain Python
  object standing in front of one C++ QQmlReusableDelegateModelItemsPool.

  C++ hands a QQmlReusableDelegateModelItemsPool around as a copy, so every
  C++ QQmlReusableDelegateModelItemsPool behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QQmlReusableDelegateModelItemsPool that has a ritual
  and that Python can call so far, 3 names in all: 'insertItem', 'takeItem',
  'size'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlReusableDelegateModelItemsPool::drain(int maxPoolTime,
    std::function<void (QQmlDelegateModelItem *)> releaseItem)': takes a type
    Python has no way to hand over yet.
  - Qt's
    'QQmlReusableDelegateModelItemsPool::~QQmlReusableDelegateModelItemsPool(
    )': the destructor: Python removes its C++
    QQmlReusableDelegateModelItemsPool by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlReusableDelegateModelItemsPool is created at the first use,
    not by 'QQmlReusableDelegateModelItemsPool(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlReusableDelegateModelItemsPool back gives a copy
    the ritual made for Python, in a new cute
    QQmlReusableDelegateModelItemsPool.
  - Each name of Qt's QQmlReusableDelegateModelItemsPool that has no cute
    function yet, 'drain', 'reuseItem', holds a function that raises
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
  __qt_class__ = 'QQmlReusableDelegateModelItemsPool'

  #  Qt's '~QQmlReusableDelegateModelItemsPool()'. Naming it makes this a
  #  value class: Python owns every C++ QQmlReusableDelegateModelItemsPool
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN34QQmlReusableDelegateModelItemsPoolD1Ev'

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

  @overload(QQmlDelegateModelItem)
  @overload(NoneType)
  def insertItem(self, modelItem: Optional[QQmlDelegateModelItem]) -> bool:
    """
    Calls Qt's 'bool
    QQmlReusableDelegateModelItemsPool::insertItem(QQmlDelegateModelItem
    *modelItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlreusabledelegatemodelitemspool.html#insertItem

    Parameters
    ----------

    modelItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlReusableDelegateModelItemsPool::insertItem(
    #      QQmlDelegateModelItem *modelItem)
    return self.uglySide.call(
        'ritual_ZN34QQmlReusableDelegateModelItemsPool10insertItemEP21QQmlD'
        'elegateModelItem',
        self._addressOf(modelItem),
    )

  @overload(QQmlComponent, int)
  @overload(NoneType, int)
  def takeItem(
      self,
      delegate: Optional[QQmlComponent],
      newIndexHint: int,
  ) -> Optional[QQmlDelegateModelItem]:
    """
    Calls Qt's 'QQmlDelegateModelItem
    *QQmlReusableDelegateModelItemsPool::takeItem(const QQmlComponent
    *delegate, int newIndexHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlreusabledelegatemodelitemspool.html#takeItem

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newIndexHint : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlDelegateModelItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelItem
    #      *QQmlReusableDelegateModelItemsPool::takeItem(const QQmlComponent
    #      *delegate, int newIndexHint)
    address = self.uglySide.call(
        'ritual_ZN34QQmlReusableDelegateModelItemsPool8takeItemEPK13QQmlCom'
        'ponenti',
        self._addressOf(delegate), newIndexHint,
    )
    from . import QQmlDelegateModelItem
    return QQmlDelegateModelItem._cuteAt(address)

  def size(self) -> int:
    """
    Calls Qt's 'int QQmlReusableDelegateModelItemsPool::size()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlreusabledelegatemodelitemspool.html#size
    """
    #  int QQmlReusableDelegateModelItemsPool::size()
    return self.uglySide.call(
        'ritual_ZN34QQmlReusableDelegateModelItemsPool4sizeEv',
    )

  @staticmethod
  def drain(*__, **_) -> Never:
    """
    Qt's 'void QQmlReusableDelegateModelItemsPool::drain(int maxPoolTime,
    std::function<void (QQmlDelegateModelItem *)> releaseItem)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlReusableDelegateModelItemsPool.drain' has no cute function "
        "yet. Qt's 'void QQmlReusableDelegateModelItemsPool::drain(int "
        "maxPoolTime, std::function<void (QQmlDelegateModelItem *)> "
        "releaseItem)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def reuseItem(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlReusableDelegateModelItemsPool::reuseItem(QQmlDelegateModelItem
    *item, int newModelIndex)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlReusableDelegateModelItemsPool.reuseItem' has no cute "
        "function yet. Qt's 'void "
        "QQmlReusableDelegateModelItemsPool::reuseItem(QQmlDelegateModelItem"
        " *item, int newModelIndex)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
