"""
QDomText binding of the Qt C++
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
from . import QDomCharacterData, QDomNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomTextPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomTextPrivate = WAIT['QDomTextPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomText(QDomCharacterData):
  """
  The cute side of Qt's QDomText: a plain Python object standing in front of
  one C++ QDomText.

  It is built on the cute 'QDomCharacterData', as Qt's QDomText is built on
  Qt's QDomCharacterData, and has everything that class has.

  C++ hands a QDomText around as a copy, so every C++ QDomText behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomText that has a ritual and that Python can call
  so far, 2 names in all: 'splitText', 'nodeType'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomText &QDomText::operator=(const QDomText &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QDomText::~QDomText()': the destructor: Python removes its C++
    QDomText by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomText is created at the first use, not by 'QDomText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomText back gives a copy the ritual made for
    Python, in a new cute QDomText.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomText'

  #  Qt's '~QDomText()'. Naming it makes this a value class: Python owns
  #  every C++ QDomText behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QDomTextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomText::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomtext.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomText::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK8QDomText8nodeTypeEv',
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
    Notes what was given, for Qt's 'QDomText::QDomText()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomtext.html#QDomText
    """
    #  QDomText::QDomText()
    self._noteCreation(QDomText, lambda: Rituals.call(
        'ritual_ZN8QDomTextC1Ev',
    ))

  @overload(THIS)
  def __init__(self, text: QDomText) -> None:
    """
    Notes what was given, for Qt's 'QDomText::QDomText(const QDomText
    &text)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomtext.html#QDomText

    Parameters
    ----------

    text : QDomText
      Passed on as a value: Qt reads the C++ QDomText, which stays Python's
      own.
    """
    #  QDomText::QDomText(const QDomText &text)
    self._noteCreation(QDomText, lambda: Rituals.call(
        'ritual_ZN8QDomTextC1ERKS_', self._valueOf(text),
    ))

  @overload(QDomTextPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomTextPrivate]) -> None:
    """
    Notes what was given, for Qt's 'QDomText::QDomText(QDomTextPrivate *a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomtext.html#QDomText

    Parameters
    ----------

    a0 : Optional[QDomTextPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomText::QDomText(QDomTextPrivate *a0)
    self._noteCreation(QDomText, lambda: Rituals.call(
        'ritual_ZN8QDomTextC1EP15QDomTextPrivate', self._addressOf(a0),
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

  @overload(int)
  def splitText(self, offset: int) -> QDomText:
    """
    Calls Qt's 'QDomText QDomText::splitText(int offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomtext.html#splitText

    Parameters
    ----------

    offset : int
      Passed on as it is.

    Returns
    -------

    QDomText
      A new cute QDomText around the copy Qt gave back. Python owns it.
    """
    #  QDomText QDomText::splitText(int offset)
    address = self.uglySide.call('ritual_ZN8QDomText9splitTextEi', offset)
    return QDomText._cuteOwning(address)
