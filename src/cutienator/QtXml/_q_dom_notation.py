"""
QDomNotation binding of the Qt C++
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

  from . import QDomNotationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomNotationPrivate = WAIT['QDomNotationPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomNotation(QDomNode):
  """
  The cute side of Qt's QDomNotation: a plain Python object standing in front
  of one C++ QDomNotation.

  It is built on the cute 'QDomNode', as Qt's QDomNotation is built on Qt's
  QDomNode, and has everything that class has.

  C++ hands a QDomNotation around as a copy, so every C++ QDomNotation behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomNotation that has a ritual and that Python can
  call so far, 3 names in all: 'publicId', 'systemId', 'nodeType'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomNotation &QDomNotation::operator=(const QDomNotation &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDomNotation::~QDomNotation()': the destructor: Python removes its
    C++ QDomNotation by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomNotation is created at the first use, not by
    'QDomNotation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomNotation back gives a copy the ritual made for
    Python, in a new cute QDomNotation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomNotation'

  #  Qt's '~QDomNotation()'. Naming it makes this a value class: Python owns
  #  every C++ QDomNotation behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QDomNotationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def publicId(self) -> str:
    """
    Calls Qt's 'QString QDomNotation::publicId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnotation.html#publicId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNotation::publicId() const
    return self.uglySide.call('ritual_ZNK12QDomNotation8publicIdEv')

  def systemId(self) -> str:
    """
    Calls Qt's 'QString QDomNotation::systemId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnotation.html#systemId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNotation::systemId() const
    return self.uglySide.call('ritual_ZNK12QDomNotation8systemIdEv')

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomNotation::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnotation.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomNotation::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK12QDomNotation8nodeTypeEv',
    ))

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
    Notes what was given, for Qt's 'QDomNotation::QDomNotation()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnotation.html#QDomNotation
    """
    #  QDomNotation::QDomNotation()
    self._noteCreation(QDomNotation, lambda: Rituals.call(
        'ritual_ZN12QDomNotationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, notation: QDomNotation) -> None:
    """
    Notes what was given, for Qt's 'QDomNotation::QDomNotation(const
    QDomNotation &notation)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnotation.html#QDomNotation

    Parameters
    ----------

    notation : QDomNotation
      Passed on as a value: Qt reads the C++ QDomNotation, which stays
      Python's own.
    """
    #  QDomNotation::QDomNotation(const QDomNotation &notation)
    self._noteCreation(QDomNotation, lambda: Rituals.call(
        'ritual_ZN12QDomNotationC1ERKS_', self._valueOf(notation),
    ))

  @overload(QDomNotationPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomNotationPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomNotation::QDomNotation(QDomNotationPrivate *a0)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnotation.html#QDomNotation

    Parameters
    ----------

    a0 : Optional[QDomNotationPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomNotation::QDomNotation(QDomNotationPrivate *a0)
    self._noteCreation(QDomNotation, lambda: Rituals.call(
        'ritual_ZN12QDomNotationC1EP19QDomNotationPrivate',
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
