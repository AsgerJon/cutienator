"""
QIOOperationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qiooperation_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QIOOperationPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QIOOperation, QObjectPrivate, QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIOOperationPrivate(QObjectPrivate):
  """
  The cute side of Qt's QIOOperationPrivate: a plain Python object standing
  in front of one C++ QIOOperationPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QIOOperationPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIOOperationPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'get',
  'appendBytesProcessed', 'operationComplete', 'setError'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QIOOperation *QIOOperationPrivate::q_func() const': takes in
    Python what 'QIOOperation *QIOOperationPrivate::q_func()' takes.
  - Qt's 'QIOOperationPrivate::~QIOOperationPrivate()': the destructor:
    Python never removes a C++ QIOOperationPrivate.

  What to expect
  --------------

  - The C++ QIOOperationPrivate is created at the first use, not by
    'QIOOperationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIOOperationPrivate.
  """

  #  The enums Qt writes inside QIOOperationPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum, scoped=True):
    """
    The enum 'QIOOperationPrivate::State' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Running = Kee[int](0)
    Finished = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QIOOperation)
  @overload(NoneType)
  def get(op: Optional[QIOOperation]) -> Optional[QIOOperationPrivate]:
    """
    Calls Qt's 'QIOOperationPrivate *QIOOperationPrivate::get(QIOOperation
    *op)'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperationprivate.html#get

    Parameters
    ----------

    op : Optional[QIOOperation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QIOOperationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperationPrivate *QIOOperationPrivate::get(QIOOperation *op)
    address = Rituals.call(
        'ritual_ZN19QIOOperationPrivate3getEP12QIOOperation',
        CuteMixin._addressOf(op),
    )
    return QIOOperationPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIOOperationPrivate'

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

  @overload(QIOOperation.Error)
  def setError(self, err: QIOOperation.Error) -> None:
    """
    Calls Qt's 'void QIOOperationPrivate::setError(QIOOperation::Error err)'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperationprivate.html#setError

    Parameters
    ----------

    err : QIOOperation.Error
      Passed on as its number.
    """
    #  void QIOOperationPrivate::setError(QIOOperation::Error err)
    self.uglySide.call(
        'ritual_ZN19QIOOperationPrivate8setErrorEN12QIOOperation5ErrorE',
        err.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QtPrivate.QIOOperationDataStorage'])
  @overload(NoneType)
  def __init__(
      self,
      storage: Optional[QtPrivate.QIOOperationDataStorage],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QIOOperationPrivate::QIOOperationPrivate(QtPrivate::
    QIOOperationDataStorage *storage)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qiooperationprivate.html#QIOOperationPrivate

    Parameters
    ----------

    storage : Optional[QtPrivate.QIOOperationDataStorage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QIOOperationPrivate::QIOOperationPrivate(QtPrivate::
    #      QIOOperationDataStorage *storage)
    self._noteCreation(QIOOperationPrivate, lambda: Rituals.call(
        'ritual_ZN19QIOOperationPrivateC1EPN9QtPrivate23QIOOperationDataSto'
        'rageE',
        self._addressOf(storage),
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

  def q_func(self) -> Optional[QIOOperation]:
    """
    Calls Qt's 'QIOOperation *QIOOperationPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperationprivate.html#q_func

    Returns
    -------

    Optional[QIOOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperation *QIOOperationPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QIOOperationPrivate6q_funcEv')
    return QIOOperation._cuteAt(address)

  @overload(int)
  def appendBytesProcessed(self, num: int) -> None:
    """
    Calls Qt's 'void QIOOperationPrivate::appendBytesProcessed(qint64 num)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiooperationprivate.html#appendBytesProcessed

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QIOOperationPrivate::appendBytesProcessed(qint64 num)
    self.uglySide.call(
        'ritual_ZN19QIOOperationPrivate20appendBytesProcessedEx', num,
    )

  @overload(QIOOperation.Error)
  def operationComplete(self, err: QIOOperation.Error) -> None:
    """
    Calls Qt's 'void
    QIOOperationPrivate::operationComplete(QIOOperation::Error err)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiooperationprivate.html#operationComplete

    Parameters
    ----------

    err : QIOOperation.Error
      Passed on as its number.
    """
    #  void QIOOperationPrivate::operationComplete(QIOOperation::Error err)
    self.uglySide.call(
        'ritual_ZN19QIOOperationPrivate17operationCompleteEN12QIOOperation5'
        'ErrorE',
        err.value,
    )
