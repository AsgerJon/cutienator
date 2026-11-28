"""
QDomCharacterData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDomNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomCharacterDataPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomCharacterDataPrivate = WAIT['QDomCharacterDataPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomCharacterData(QDomNode):
  """
  The cute side of Qt's QDomCharacterData: a plain Python object standing in
  front of one C++ QDomCharacterData.

  It is built on the cute 'QDomNode', as Qt's QDomCharacterData is built on
  Qt's QDomNode, and has everything that class has.

  C++ hands a QDomCharacterData around as a copy, so every C++
  QDomCharacterData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomCharacterData that has a ritual and that Python
  can call so far, 9 names in all: 'substringData', 'appendData',
  'insertData', 'deleteData', 'replaceData', 'length', 'data', 'setData',
  'nodeType'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomCharacterData &QDomCharacterData::operator=(const
    QDomCharacterData &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDomCharacterData::~QDomCharacterData()': the destructor: Python
    removes its C++ QDomCharacterData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomCharacterData is created at the first use, not by
    'QDomCharacterData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomCharacterData back gives a copy the ritual made
    for Python, in a new cute QDomCharacterData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomCharacterData'

  #  Qt's '~QDomCharacterData()'. Naming it makes this a value class: Python
  #  owns every C++ QDomCharacterData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QDomCharacterDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def length(self) -> int:
    """
    Calls Qt's 'int QDomCharacterData::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#length
    """
    #  int QDomCharacterData::length() const
    return self.uglySide.call('ritual_ZNK17QDomCharacterData6lengthEv')

  def data(self) -> str:
    """
    Calls Qt's 'QString QDomCharacterData::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#data

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomCharacterData::data() const
    return self.uglySide.call('ritual_ZNK17QDomCharacterData4dataEv')

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomCharacterData::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomCharacterData::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK17QDomCharacterData8nodeTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setData(self, data: str) -> None:
    """
    Calls Qt's 'void QDomCharacterData::setData(const QString &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#setData

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomCharacterData::setData(const QString &data)
    self.uglySide.call(
        'ritual_ZN17QDomCharacterData7setDataERK7QString', data,
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
    Notes what was given, for Qt's 'QDomCharacterData::QDomCharacterData()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdata.html#QDomCharacterData
    """
    #  QDomCharacterData::QDomCharacterData()
    self._noteCreation(QDomCharacterData, lambda: Rituals.call(
        'ritual_ZN17QDomCharacterDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, characterData: QDomCharacterData) -> None:
    """
    Notes what was given, for Qt's
    'QDomCharacterData::QDomCharacterData(const QDomCharacterData
    &characterData)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdata.html#QDomCharacterData

    Parameters
    ----------

    characterData : QDomCharacterData
      Passed on as a value: Qt reads the C++ QDomCharacterData, which stays
      Python's own.
    """
    #  QDomCharacterData::QDomCharacterData(const QDomCharacterData
    #      &characterData)
    self._noteCreation(QDomCharacterData, lambda: Rituals.call(
        'ritual_ZN17QDomCharacterDataC1ERKS_', self._valueOf(characterData),
    ))

  @overload(QDomCharacterDataPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomCharacterDataPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomCharacterData::QDomCharacterData(QDomCharacterDataPrivate *a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdata.html#QDomCharacterData

    Parameters
    ----------

    a0 : Optional[QDomCharacterDataPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomCharacterData::QDomCharacterData(QDomCharacterDataPrivate *a0)
    self._noteCreation(QDomCharacterData, lambda: Rituals.call(
        'ritual_ZN17QDomCharacterDataC1EP24QDomCharacterDataPrivate',
        self._addressOf(a0),
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

  @overload(int, int)
  def substringData(self, offset: int, count: int) -> str:
    """
    Calls Qt's 'QString QDomCharacterData::substringData(unsigned long
    offset, unsigned long count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdata.html#substringData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomCharacterData::substringData(unsigned long offset,
    #      unsigned long count)
    return self.uglySide.call(
        'ritual_ZN17QDomCharacterData13substringDataEmm', offset, count,
    )

  @overload(str)
  def appendData(self, arg: str) -> None:
    """
    Calls Qt's 'void QDomCharacterData::appendData(const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#appendData

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomCharacterData::appendData(const QString &arg)
    self.uglySide.call(
        'ritual_ZN17QDomCharacterData10appendDataERK7QString', arg,
    )

  @overload(int, str)
  def insertData(self, offset: int, arg: str) -> None:
    """
    Calls Qt's 'void QDomCharacterData::insertData(unsigned long offset,
    const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#insertData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomCharacterData::insertData(unsigned long offset, const QString
    #      &arg)
    self.uglySide.call(
        'ritual_ZN17QDomCharacterData10insertDataEmRK7QString', offset, arg,
    )

  @overload(int, int)
  def deleteData(self, offset: int, count: int) -> None:
    """
    Calls Qt's 'void QDomCharacterData::deleteData(unsigned long offset,
    unsigned long count)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#deleteData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QDomCharacterData::deleteData(unsigned long offset, unsigned long
    #      count)
    self.uglySide.call(
        'ritual_ZN17QDomCharacterData10deleteDataEmm', offset, count,
    )

  @overload(int, int, str)
  def replaceData(self, offset: int, count: int, arg: str) -> None:
    """
    Calls Qt's 'void QDomCharacterData::replaceData(unsigned long offset,
    unsigned long count, const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcharacterdata.html#replaceData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomCharacterData::replaceData(unsigned long offset, unsigned
    #      long count, const QString &arg)
    self.uglySide.call(
        'ritual_ZN17QDomCharacterData11replaceDataEmmRK7QString',
        offset, count, arg,
    )
