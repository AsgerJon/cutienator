"""
QDomProcessingInstruction binding of the Qt C++
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

  from . import QDomProcessingInstructionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomProcessingInstructionPrivate = WAIT['QDomProcessingInstructionPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomProcessingInstruction(QDomNode):
  """
  The cute side of Qt's QDomProcessingInstruction: a plain Python object
  standing in front of one C++ QDomProcessingInstruction.

  It is built on the cute 'QDomNode', as Qt's QDomProcessingInstruction is
  built on Qt's QDomNode, and has everything that class has.

  C++ hands a QDomProcessingInstruction around as a copy, so every C++
  QDomProcessingInstruction behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomProcessingInstruction that has a ritual and that
  Python can call so far, 4 names in all: 'target', 'data', 'setData',
  'nodeType'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomProcessingInstruction
    &QDomProcessingInstruction::operator=(const QDomProcessingInstruction
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDomProcessingInstruction::~QDomProcessingInstruction()': the
    destructor: Python removes its C++ QDomProcessingInstruction by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QDomProcessingInstruction is created at the first use, not by
    'QDomProcessingInstruction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomProcessingInstruction back gives a copy the
    ritual made for Python, in a new cute QDomProcessingInstruction.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomProcessingInstruction'

  #  Qt's '~QDomProcessingInstruction()'. Naming it makes this a value class:
  #  Python owns every C++ QDomProcessingInstruction behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QDomProcessingInstructionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def target(self) -> str:
    """
    Calls Qt's 'QString QDomProcessingInstruction::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html#target

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomProcessingInstruction::target() const
    return self.uglySide.call(
        'ritual_ZNK25QDomProcessingInstruction6targetEv',
    )

  def data(self) -> str:
    """
    Calls Qt's 'QString QDomProcessingInstruction::data() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html#data

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomProcessingInstruction::data() const
    return self.uglySide.call('ritual_ZNK25QDomProcessingInstruction4dataEv')

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomProcessingInstruction::nodeType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomProcessingInstruction::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK25QDomProcessingInstruction8nodeTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setData(self, data: str) -> None:
    """
    Calls Qt's 'void QDomProcessingInstruction::setData(const QString
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html#setData

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomProcessingInstruction::setData(const QString &data)
    self.uglySide.call(
        'ritual_ZN25QDomProcessingInstruction7setDataERK7QString', data,
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
    'QDomProcessingInstruction::QDomProcessingInstruction()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html
    """
    #  QDomProcessingInstruction::QDomProcessingInstruction()
    self._noteCreation(QDomProcessingInstruction, lambda: Rituals.call(
        'ritual_ZN25QDomProcessingInstructionC1Ev',
    ))

  @overload(THIS)
  def __init__(
      self,
      processingInstruction: QDomProcessingInstruction,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDomProcessingInstruction::QDomProcessingInstruction(const
    QDomProcessingInstruction &processingInstruction)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html

    Parameters
    ----------

    processingInstruction : QDomProcessingInstruction
      Passed on as a value: Qt reads the C++ QDomProcessingInstruction, which
      stays Python's own.
    """
    #  QDomProcessingInstruction::QDomProcessingInstruction(const
    #      QDomProcessingInstruction &processingInstruction)
    self._noteCreation(QDomProcessingInstruction, lambda: Rituals.call(
        'ritual_ZN25QDomProcessingInstructionC1ERKS_',
        self._valueOf(processingInstruction),
    ))

  @overload(QDomProcessingInstructionPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomProcessingInstructionPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomProcessingInstruction::QDomProcessingInstruction(
    QDomProcessingInstructionPrivate *a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomprocessinginstruction.html

    Parameters
    ----------

    a0 : Optional[QDomProcessingInstructionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomProcessingInstruction::QDomProcessingInstruction(
    #      QDomProcessingInstructionPrivate *a0)
    self._noteCreation(QDomProcessingInstruction, lambda: Rituals.call(
        'ritual_ZN25QDomProcessingInstructionC1EP32QDomProcessingInstructio'
        'nPrivate',
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
