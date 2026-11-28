"""
QDomCDATASection binding of the Qt C++
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
from . import QDomNode, QDomText

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomCDATASectionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomCDATASectionPrivate = WAIT['QDomCDATASectionPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomCDATASection(QDomText):
  """
  The cute side of Qt's QDomCDATASection: a plain Python object standing in
  front of one C++ QDomCDATASection.

  It is built on the cute 'QDomText', as Qt's QDomCDATASection is built on
  Qt's QDomText, and has everything that class has.

  C++ hands a QDomCDATASection around as a copy, so every C++
  QDomCDATASection behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomCDATASection that has a ritual and that Python
  can call so far, 1 name in all: 'nodeType'. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomCDATASection &QDomCDATASection::operator=(const
    QDomCDATASection &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDomCDATASection::~QDomCDATASection()': the destructor: Python
    removes its C++ QDomCDATASection by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomCDATASection is created at the first use, not by
    'QDomCDATASection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomCDATASection back gives a copy the ritual made
    for Python, in a new cute QDomCDATASection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomCDATASection'

  #  Qt's '~QDomCDATASection()'. Naming it makes this a value class: Python
  #  owns every C++ QDomCDATASection behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDomCDATASectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomCDATASection::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcdatasection.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomCDATASection::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK16QDomCDATASection8nodeTypeEv',
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
    Notes what was given, for Qt's 'QDomCDATASection::QDomCDATASection()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcdatasection.html#QDomCDATASection
    """
    #  QDomCDATASection::QDomCDATASection()
    self._noteCreation(QDomCDATASection, lambda: Rituals.call(
        'ritual_ZN16QDomCDATASectionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, cdataSection: QDomCDATASection) -> None:
    """
    Notes what was given, for Qt's 'QDomCDATASection::QDomCDATASection(const
    QDomCDATASection &cdataSection)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcdatasection.html#QDomCDATASection

    Parameters
    ----------

    cdataSection : QDomCDATASection
      Passed on as a value: Qt reads the C++ QDomCDATASection, which stays
      Python's own.
    """
    #  QDomCDATASection::QDomCDATASection(const QDomCDATASection
    #      &cdataSection)
    self._noteCreation(QDomCDATASection, lambda: Rituals.call(
        'ritual_ZN16QDomCDATASectionC1ERKS_', self._valueOf(cdataSection),
    ))

  @overload(QDomCDATASectionPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomCDATASectionPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomCDATASection::QDomCDATASection(QDomCDATASectionPrivate *a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcdatasection.html#QDomCDATASection

    Parameters
    ----------

    a0 : Optional[QDomCDATASectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomCDATASection::QDomCDATASection(QDomCDATASectionPrivate *a0)
    self._noteCreation(QDomCDATASection, lambda: Rituals.call(
        'ritual_ZN16QDomCDATASectionC1EP23QDomCDATASectionPrivate',
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
