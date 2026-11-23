"""
QModelRoleDataSpan binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QModelRoleData, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelRoleData = WAIT['QModelRoleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModelRoleDataSpan(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModelRoleDataSpan: a plain Python object standing in
  front of one C++ QModelRoleDataSpan.

  C++ hands a QModelRoleDataSpan around as a copy, so every C++
  QModelRoleDataSpan behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModelRoleDataSpan that has a ritual and that Python
  can call so far, 6 names in all: 'size', 'length', 'data', 'begin', 'end',
  'dataForRole'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModelRoleDataSpan::~QModelRoleDataSpan()': the destructor: Python
    removes its C++ QModelRoleDataSpan by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QModelRoleDataSpan is created at the first use, not by
    'QModelRoleDataSpan(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModelRoleDataSpan back gives a copy the ritual made
    for Python, in a new cute QModelRoleDataSpan.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModelRoleDataSpan'

  #  Qt's '~QModelRoleDataSpan()'. Naming it makes this a value class: Python
  #  owns every C++ QModelRoleDataSpan behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QModelRoleDataSpanD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QModelRoleDataSpan::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledataspan.html#size
    """
    #  qsizetype QModelRoleDataSpan::size() const
    return self.uglySide.call('ritual_ZNK18QModelRoleDataSpan4sizeEv')

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QModelRoleDataSpan::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledataspan.html#length
    """
    #  qsizetype QModelRoleDataSpan::length() const
    return self.uglySide.call('ritual_ZNK18QModelRoleDataSpan6lengthEv')

  def data(self) -> Optional[QModelRoleData]:
    """
    Calls Qt's 'QModelRoleData *QModelRoleDataSpan::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledataspan.html#data

    Returns
    -------

    Optional[QModelRoleData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModelRoleData *QModelRoleDataSpan::data() const
    address = self.uglySide.call('ritual_ZNK18QModelRoleDataSpan4dataEv')
    from . import QModelRoleData
    return QModelRoleData._cuteAt(address)

  def begin(self) -> Optional[QModelRoleData]:
    """
    Calls Qt's 'QModelRoleData *QModelRoleDataSpan::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledataspan.html#begin

    Returns
    -------

    Optional[QModelRoleData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModelRoleData *QModelRoleDataSpan::begin() const
    address = self.uglySide.call('ritual_ZNK18QModelRoleDataSpan5beginEv')
    from . import QModelRoleData
    return QModelRoleData._cuteAt(address)

  def end(self) -> Optional[QModelRoleData]:
    """
    Calls Qt's 'QModelRoleData *QModelRoleDataSpan::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodelroledataspan.html#end

    Returns
    -------

    Optional[QModelRoleData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModelRoleData *QModelRoleDataSpan::end() const
    address = self.uglySide.call('ritual_ZNK18QModelRoleDataSpan3endEv')
    from . import QModelRoleData
    return QModelRoleData._cuteAt(address)

  @overload(int)
  def dataForRole(self, role: int) -> Optional[QVariant]:
    """
    Calls Qt's 'QVariant *QModelRoleDataSpan::dataForRole(int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodelroledataspan.html#dataForRole

    Parameters
    ----------

    role : int
      Passed on as it is.

    Returns
    -------

    Optional[QVariant]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVariant *QModelRoleDataSpan::dataForRole(int role) const
    address = self.uglySide.call(
        'ritual_ZNK18QModelRoleDataSpan11dataForRoleEi', role,
    )
    from . import QVariant
    return QVariant._cuteAt(address)

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
    'QModelRoleDataSpan::QModelRoleDataSpan()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodelroledataspan.html#QModelRoleDataSpan
    """
    #  QModelRoleDataSpan::QModelRoleDataSpan()
    self._noteCreation(QModelRoleDataSpan, lambda: Rituals.call(
        'ritual_ZN18QModelRoleDataSpanC1Ev',
    ))

  @overload(QModelRoleData, int)
  @overload(NoneType, int)
  def __init__(
      self,
      modelRoleData: Optional[QModelRoleData],
      len: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QModelRoleDataSpan::QModelRoleDataSpan(QModelRoleData *modelRoleData,
    qsizetype len)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodelroledataspan.html#QModelRoleDataSpan

    Parameters
    ----------

    modelRoleData : Optional[QModelRoleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len : int
      Passed on as it is.
    """
    #  QModelRoleDataSpan::QModelRoleDataSpan(QModelRoleData *modelRoleData,
    #      qsizetype len)
    self._noteCreation(QModelRoleDataSpan, lambda: Rituals.call(
        'ritual_ZN18QModelRoleDataSpanC1EP14QModelRoleDatax',
        self._addressOf(modelRoleData), len,
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
