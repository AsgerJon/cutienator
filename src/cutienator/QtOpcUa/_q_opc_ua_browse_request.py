"""
QOpcUaBrowseRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuabrowserequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpcUaBrowseRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaBrowseRequest: a plain Python object standing
  in front of one C++ QOpcUaBrowseRequest.

  C++ hands a QOpcUaBrowseRequest around as a copy, so every C++
  QOpcUaBrowseRequest behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaBrowseRequest that has a ritual and that
  Python can call so far, 6 names in all: 'browseDirection',
  'referenceTypeId', 'setReferenceTypeId', 'includeSubtypes',
  'setIncludeSubtypes', 'nodeClassMask'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaBrowseRequest &QOpcUaBrowseRequest::operator=(const
    QOpcUaBrowseRequest &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaBrowseRequest::~QOpcUaBrowseRequest()': the destructor:
    Python removes its C++ QOpcUaBrowseRequest by it, and has no other use
    for it.
  - Qt's 'void QOpcUaBrowseRequest::setBrowseDirection(const
    QOpcUaBrowseRequest::BrowseDirection &browseDirection)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QOpcUaBrowseRequest::setNodeClassMask(const
    QOpcUa::NodeClasses &nodeClassMask)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaBrowseRequest is created at the first use, not by
    'QOpcUaBrowseRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaBrowseRequest back gives a copy the ritual made
    for Python, in a new cute QOpcUaBrowseRequest.
  - Each name of Qt's QOpcUaBrowseRequest that has no cute function yet,
    'setBrowseDirection', 'setNodeClassMask', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaBrowseRequest, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BrowseDirection(CuteNum, scoped=True):
    """
    The enum 'QOpcUaBrowseRequest::BrowseDirection' of Qt, with the 3 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Forward = Kee[int](0)
    Inverse = Kee[int](1)
    Both = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaBrowseRequest'

  #  Qt's '~QOpcUaBrowseRequest()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaBrowseRequest behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QOpcUaBrowseRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def browseDirection(self) -> BrowseDirection:
    """
    Calls Qt's 'QOpcUaBrowseRequest::BrowseDirection
    QOpcUaBrowseRequest::browseDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#browseDirection

    Returns
    -------

    BrowseDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BrowseDirection(number)'
      gives.
    """
    #  QOpcUaBrowseRequest::BrowseDirection
    #      QOpcUaBrowseRequest::browseDirection() const
    return QOpcUaBrowseRequest.BrowseDirection(self.uglySide.call(
        'ritual_ZNK19QOpcUaBrowseRequest15browseDirectionEv',
    ))

  def referenceTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaBrowseRequest::referenceTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#referenceTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaBrowseRequest::referenceTypeId() const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaBrowseRequest15referenceTypeIdEv',
    )

  def includeSubtypes(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaBrowseRequest::includeSubtypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#includeSubtypes
    """
    #  bool QOpcUaBrowseRequest::includeSubtypes() const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaBrowseRequest15includeSubtypesEv',
    )

  def nodeClassMask(self) -> QOpcUa.NodeClasses:
    """
    Calls Qt's 'QOpcUa::NodeClasses QOpcUaBrowseRequest::nodeClassMask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#nodeClassMask

    Returns
    -------

    QOpcUa.NodeClasses
      The value standing for the combination Qt gave back.
    """
    #  QOpcUa::NodeClasses QOpcUaBrowseRequest::nodeClassMask() const
    return QOpcUa.NodeClasses(self.uglySide.call(
        'ritual_ZNK19QOpcUaBrowseRequest13nodeClassMaskEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setReferenceTypeId(self, referenceTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaBrowseRequest::setReferenceTypeId(const QString
    &referenceTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#setReferenceTypeId

    Parameters
    ----------

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaBrowseRequest::setReferenceTypeId(const QString
    #      &referenceTypeId)
    self.uglySide.call(
        'ritual_ZN19QOpcUaBrowseRequest18setReferenceTypeIdERK7QString',
        referenceTypeId,
    )

  @overload(QOpcUa.ReferenceTypeId)
  def setReferenceTypeId(
      self,
      referenceTypeId: QOpcUa.ReferenceTypeId,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBrowseRequest::setReferenceTypeId(QOpcUa::ReferenceTypeId
    referenceTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#setReferenceTypeId

    Parameters
    ----------

    referenceTypeId : QOpcUa.ReferenceTypeId
      Passed on as its number.
    """
    #  void QOpcUaBrowseRequest::setReferenceTypeId(QOpcUa::ReferenceTypeId
    #      referenceTypeId)
    self.uglySide.call(
        'ritual_ZN19QOpcUaBrowseRequest18setReferenceTypeIdEN6QOpcUa15Refer'
        'enceTypeIdE',
        referenceTypeId.value,
    )

  @overload(bool)
  def setIncludeSubtypes(self, includeSubtypes: bool) -> None:
    """
    Calls Qt's 'void QOpcUaBrowseRequest::setIncludeSubtypes(bool
    includeSubtypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#setIncludeSubtypes

    Parameters
    ----------

    includeSubtypes : bool
      Passed on as it is.
    """
    #  void QOpcUaBrowseRequest::setIncludeSubtypes(bool includeSubtypes)
    self.uglySide.call(
        'ritual_ZN19QOpcUaBrowseRequest18setIncludeSubtypesEb',
        includeSubtypes,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaBrowseRequest::QOpcUaBrowseRequest()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#QOpcUaBrowseRequest
    """
    #  QOpcUaBrowseRequest::QOpcUaBrowseRequest()
    self._noteCreation(QOpcUaBrowseRequest, lambda: Rituals.call(
        'ritual_ZN19QOpcUaBrowseRequestC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaBrowseRequest) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaBrowseRequest::QOpcUaBrowseRequest(const QOpcUaBrowseRequest
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabrowserequest.html#QOpcUaBrowseRequest

    Parameters
    ----------

    other : QOpcUaBrowseRequest
      Passed on as a value: Qt reads the C++ QOpcUaBrowseRequest, which stays
      Python's own.
    """
    #  QOpcUaBrowseRequest::QOpcUaBrowseRequest(const QOpcUaBrowseRequest
    #      &other)
    self._noteCreation(QOpcUaBrowseRequest, lambda: Rituals.call(
        'ritual_ZN19QOpcUaBrowseRequestC1ERKS_', self._valueOf(other),
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
  def setBrowseDirection(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaBrowseRequest::setBrowseDirection(const
    QOpcUaBrowseRequest::BrowseDirection &browseDirection)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaBrowseRequest.setBrowseDirection' has no cute function yet. "
        "Qt's 'void QOpcUaBrowseRequest::setBrowseDirection(const "
        "QOpcUaBrowseRequest::BrowseDirection &browseDirection)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setNodeClassMask(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaBrowseRequest::setNodeClassMask(const
    QOpcUa::NodeClasses &nodeClassMask)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaBrowseRequest.setNodeClassMask' has no cute function yet. "
        "Qt's 'void QOpcUaBrowseRequest::setNodeClassMask(const "
        "QOpcUa::NodeClasses &nodeClassMask)': takes a type Python has no "
        "way to hand over yet.")
