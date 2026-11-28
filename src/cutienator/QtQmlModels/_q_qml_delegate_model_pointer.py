"""
QQmlDelegateModelPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelPointer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlDelegateModel, QQmlInstanceModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlDelegateModel = WAIT['QQmlDelegateModel']
  QQmlInstanceModel = WAIT['QQmlInstanceModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelPointer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDelegateModelPointer: a plain Python object
  standing in front of one C++ QQmlDelegateModelPointer.

  C++ hands a QQmlDelegateModelPointer around as a copy, so every C++
  QQmlDelegateModelPointer behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelPointer that has a ritual and that
  Python can call so far, 3 names in all: 'delegateModel', 'instanceModel',
  '__bool__'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDelegateModelPointer::QQmlDelegateModelPointer(
    QQmlDelegateModelPointer &&a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlDelegateModelPointer &QQmlDelegateModelPointer::operator=(const
    QQmlDelegateModelPointer &a0)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QQmlDelegateModelPointer
    &QQmlDelegateModelPointer::operator=(QQmlDelegateModelPointer &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlDelegateModelPointer
    &QQmlDelegateModelPointer::operator=(QQmlInstanceModel *instanceModel)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlDelegateModelPointer
    &QQmlDelegateModelPointer::operator=(QQmlDelegateModel *delegateModel)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlDelegateModelPointer::~QQmlDelegateModelPointer()': the
    destructor: Python removes its C++ QQmlDelegateModelPointer by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlDelegateModelPointer is created at the first use, not by
    'QQmlDelegateModelPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDelegateModelPointer back gives a copy the ritual
    made for Python, in a new cute QQmlDelegateModelPointer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelPointer'

  #  Qt's '~QQmlDelegateModelPointer()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlDelegateModelPointer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQmlDelegateModelPointerD1Ev'

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

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelPointer::operator bool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpointer.html#operator bool
    """
    #  bool QQmlDelegateModelPointer::operator bool() const
    return self.uglySide.call('ritual_ZNK24QQmlDelegateModelPointercvbEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModelPointer::QQmlDelegateModelPointer()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpointer.html
    """
    #  QQmlDelegateModelPointer::QQmlDelegateModelPointer()
    self._noteCreation(QQmlDelegateModelPointer, lambda: Rituals.call(
        'ritual_ZN24QQmlDelegateModelPointerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlDelegateModelPointer) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModelPointer::QQmlDelegateModelPointer(const
    QQmlDelegateModelPointer &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpointer.html

    Parameters
    ----------

    a0 : QQmlDelegateModelPointer
      Passed on as a value: Qt reads the C++ QQmlDelegateModelPointer, which
      stays Python's own.
    """
    #  QQmlDelegateModelPointer::QQmlDelegateModelPointer(const
    #      QQmlDelegateModelPointer &a0)
    self._noteCreation(QQmlDelegateModelPointer, lambda: Rituals.call(
        'ritual_ZN24QQmlDelegateModelPointerC1ERKS_', self._valueOf(a0),
    ))

  @overload(QQmlDelegateModel)
  def __init__(self, model: Optional[QQmlDelegateModel]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModelPointer::QQmlDelegateModelPointer(QQmlDelegateModel
    *model)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpointer.html

    Parameters
    ----------

    model : Optional[QQmlDelegateModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlDelegateModelPointer::QQmlDelegateModelPointer(QQmlDelegateModel
    #      *model)
    self._noteCreation(QQmlDelegateModelPointer, lambda: Rituals.call(
        'ritual_ZN24QQmlDelegateModelPointerC1EP17QQmlDelegateModel',
        self._addressOf(model),
    ))

  @overload(QQmlInstanceModel)
  @overload(NoneType)
  def __init__(self, model: Optional[QQmlInstanceModel]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModelPointer::QQmlDelegateModelPointer(QQmlInstanceModel
    *model)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpointer.html

    Parameters
    ----------

    model : Optional[QQmlInstanceModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlDelegateModelPointer::QQmlDelegateModelPointer(QQmlInstanceModel
    #      *model)
    self._noteCreation(QQmlDelegateModelPointer, lambda: Rituals.call(
        'ritual_ZN24QQmlDelegateModelPointerC1EP17QQmlInstanceModel',
        self._addressOf(model),
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

  def delegateModel(self) -> Optional[QQmlDelegateModel]:
    """
    Calls Qt's 'QQmlDelegateModel
    *QQmlDelegateModelPointer::delegateModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpointer.html#delegateModel

    Returns
    -------

    Optional[QQmlDelegateModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModel *QQmlDelegateModelPointer::delegateModel()
    address = self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPointer13delegateModelEv',
    )
    from . import QQmlDelegateModel
    return QQmlDelegateModel._cuteAt(address)

  def instanceModel(self) -> Optional[QQmlInstanceModel]:
    """
    Calls Qt's 'QQmlInstanceModel
    *QQmlDelegateModelPointer::instanceModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpointer.html#instanceModel

    Returns
    -------

    Optional[QQmlInstanceModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlInstanceModel *QQmlDelegateModelPointer::instanceModel()
    address = self.uglySide.call(
        'ritual_ZN24QQmlDelegateModelPointer13instanceModelEv',
    )
    from . import QQmlInstanceModel
    return QQmlInstanceModel._cuteAt(address)
