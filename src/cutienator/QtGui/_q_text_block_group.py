"""
QTextBlockGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QTextObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QTextBlock
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextBlock = WAIT['QTextBlock']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextBlockGroup(QTextObject):
  """
  The cute side of Qt's QTextBlockGroup: a plain Python object standing in
  front of one C++ QTextBlockGroup.

  It is built on the cute 'QTextObject', as Qt's QTextBlockGroup is built on
  Qt's QTextObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextBlockGroup that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'blockInserted',
  'blockRemoved', 'blockFormatChanged'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  12 of the 17 functions Qt declares: 4 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QTextBlockGroup is created at the first use, not by
    'QTextBlockGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextBlockGroup.
  - Qt tells when it has removed the C++ QTextBlockGroup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTextBlockGroup::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockgroup.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextBlockGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QTextBlockGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextBlockGroup'

  #  A C++ QTextBlockGroup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextBlockGroup'

  #  The functions Qt calls itself that QTextBlockGroup is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'blockInserted': (
          ('_ZN15QTextBlockGroup13blockInsertedERK10QTextBlock',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextBlock'),
           )),
      ),
      'blockRemoved': (
          ('_ZN15QTextBlockGroup12blockRemovedERK10QTextBlock',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextBlock'),
           )),
      ),
      'blockFormatChanged': (
          ('_ZN15QTextBlockGroup18blockFormatChangedERK10QTextBlock',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextBlock'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextBlockGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextBlockGroup::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QTextBlockGroup10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QTextBlock)
  def blockInserted(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QTextBlockGroup::blockInserted(const QTextBlock
    &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockgroup.html#blockInserted

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QTextBlockGroup::blockInserted(const QTextBlock &block)
    self.uglySide.call(
        'ritual_own_ZN15QTextBlockGroup13blockInsertedERK10QTextBlock',
        self._valueOf(block),
    )

  @overload(QTextBlock)
  def blockRemoved(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QTextBlockGroup::blockRemoved(const QTextBlock &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockgroup.html#blockRemoved

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QTextBlockGroup::blockRemoved(const QTextBlock &block)
    self.uglySide.call(
        'ritual_own_ZN15QTextBlockGroup12blockRemovedERK10QTextBlock',
        self._valueOf(block),
    )

  @overload(QTextBlock)
  def blockFormatChanged(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QTextBlockGroup::blockFormatChanged(const QTextBlock
    &block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockgroup.html#blockFormatChanged

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QTextBlockGroup::blockFormatChanged(const QTextBlock &block)
    self.uglySide.call(
        'ritual_own_ZN15QTextBlockGroup18blockFormatChangedERK10QTextBlock',
        self._valueOf(block),
    )
