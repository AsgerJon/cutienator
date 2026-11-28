"""
QtSharedPointer::ExternalRefCountData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsharedpointer_impl.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExternalRefCountData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtSharedPointer::ExternalRefCountData: a plain Python
  object standing in front of one C++ QtSharedPointer::ExternalRefCountData.

  What exists
  -----------

  Every function of Qt's QtSharedPointer::ExternalRefCountData that has a
  ritual and that Python can call so far, 4 names in all: 'destroy',
  'getAndRef', 'setQObjectShared', 'checkQObjectShared'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtSharedPointer::ExternalRefCountData::~ExternalRefCountData()':
    the destructor: Python never removes a C++
    QtSharedPointer::ExternalRefCountData.
  - Qt's 'void *QtSharedPointer::ExternalRefCountData::operator
    new(std::size_t a0, void *ptr)': an operator Python has no name for.
  - Qt's 'void QtSharedPointer::ExternalRefCountData::operator delete(void
    *ptr)': an operator Python has no name for.
  - Qt's 'void QtSharedPointer::ExternalRefCountData::operator delete(void
    *a0, void *a1)': an operator Python has no name for.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 2 the class keeps 'new' to itself, so no
  ritual can make one; 2 takes any number of arguments; 1 forbidden.

  What to expect
  --------------

  - The C++ QtSharedPointer::ExternalRefCountData is created at the first
    use, not by 'QtSharedPointer::ExternalRefCountData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtSharedPointer::ExternalRefCountData.
  - Each name of Qt's QtSharedPointer::ExternalRefCountData that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def getAndRef(a0: Optional[QObject]) -> Optional[ExternalRefCountData]:
    """
    Calls Qt's 'ExternalRefCountData
    *QtSharedPointer::ExternalRefCountData::getAndRef(const QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtsharedpointer-externalrefcountdata.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ExternalRefCountData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExternalRefCountData
    #      *QtSharedPointer::ExternalRefCountData::getAndRef(const QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN15QtSharedPointer20ExternalRefCountData9getAndRefEPK7QObj'
        'ect',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    return ExternalRefCountData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtSharedPointer::ExternalRefCountData'

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

  @overload(QObject, bool)
  @overload(NoneType, bool)
  def setQObjectShared(self, a0: Optional[QObject], enable: bool) -> None:
    """
    Calls Qt's 'void
    QtSharedPointer::ExternalRefCountData::setQObjectShared(const QObject
    *a0, bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtsharedpointer-externalrefcountdata.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enable : bool
      Passed on as it is.
    """
    #  void QtSharedPointer::ExternalRefCountData::setQObjectShared(const
    #      QObject *a0, bool enable)
    self.uglySide.call(
        'ritual_ZN15QtSharedPointer20ExternalRefCountData16setQObjectShared'
        'EPK7QObjectb',
        self._addressOf(a0, 'QObject'), enable,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QtSharedPointer::ExternalRefCountData::ExternalRefCountData(
      DestroyerFn d)': the class keeps 'new' to itself, so no ritual can make
      one.
    - Qt's 'QtSharedPointer::ExternalRefCountData::ExternalRefCountData(Qt::
      Initialization a0)': the class keeps 'new' to itself, so no ritual can
      make one.
    """
    raise NotImplementedError(
        "'QtSharedPointer.ExternalRefCountData.__init__' has no cute "
        "function yet. Qt's "
        "'QtSharedPointer::ExternalRefCountData::ExternalRefCountData(Destro"
        "yerFn d)': the class keeps 'new' to itself, so no ritual can make "
        "one. Qt's "
        "'QtSharedPointer::ExternalRefCountData::ExternalRefCountData(Qt::In"
        "itialization a0)': the class keeps 'new' to itself, so no ritual "
        "can make one.")

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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QtSharedPointer::ExternalRefCountData::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtsharedpointer-externalrefcountdata.html#destroy
    """
    #  void QtSharedPointer::ExternalRefCountData::destroy()
    self.uglySide.call(
        'ritual_ZN15QtSharedPointer20ExternalRefCountData7destroyEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def checkQObjectShared(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QtSharedPointer::ExternalRefCountData::checkQObjectShared(const QObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtsharedpointer-externalrefcountdata.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtSharedPointer::ExternalRefCountData::checkQObjectShared(const
    #      QObject *a0)
    self.uglySide.call(
        'ritual_ZN15QtSharedPointer20ExternalRefCountData18checkQObjectShar'
        'edEPK7QObject',
        self._addressOf(a0, 'QObject'),
    )
