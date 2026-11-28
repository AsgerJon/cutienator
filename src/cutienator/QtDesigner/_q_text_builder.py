"""
QTextBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/textbuilder_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTextBuilder to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import DomProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomProperty = WAIT['DomProperty']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextBuilder: a plain Python object standing in front
  of one C++ QTextBuilder.

  C++ hands a QTextBuilder around as a copy, so every C++ QTextBuilder behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextBuilder that has a ritual and that Python can
  call so far, 3 names in all: 'loadText', 'toNativeValue', 'saveText'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextBuilder::~QTextBuilder()': the destructor: Python removes its
    C++ QTextBuilder by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextBuilder is created at the first use, not by
    'QTextBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextBuilder back gives a copy the ritual made for
    Python, in a new cute QTextBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextBuilder'

  #  A C++ QTextBuilder Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextBuilder'

  #  The functions Qt calls itself that QTextBuilder is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'loadText': (
          ('_ZNK12QTextBuilder8loadTextEPK11DomProperty',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'address', 'QtDesigner:DomProperty'),
           )),
      ),
      'toNativeValue': (
          ('_ZNK12QTextBuilder13toNativeValueERK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'saveText': (
          ('_ZNK12QTextBuilder8saveTextERK8QVariant',
           ('address', 'address', 'QtDesigner:DomProperty'),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Qt's '~QTextBuilder()'. Naming it makes this a value class: Python owns
  #  every C++ QTextBuilder behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QTextBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DomProperty)
  @overload(NoneType)
  def loadText(self, property: Optional[DomProperty]) -> QVariant:
    """
    Calls Qt's 'QVariant QTextBuilder::loadText(const DomProperty *property)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbuilder.html#loadText

    Parameters
    ----------

    property : Optional[DomProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextBuilder::loadText(const DomProperty *property) const
    ritual = 'ritual_ZNK12QTextBuilder8loadTextEPK11DomProperty'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QTextBuilder8loadTextEPK11DomProperty'
    address = self.uglySide.call(ritual, self._addressOf(property))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def toNativeValue(self, value: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QTextBuilder::toNativeValue(const QVariant &value)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbuilder.html#toNativeValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextBuilder::toNativeValue(const QVariant &value) const
    ritual = 'ritual_ZNK12QTextBuilder13toNativeValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QTextBuilder13toNativeValueERK8QVariant'
    address = self.uglySide.call(ritual, self._valueOf(value))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def saveText(self, value: QVariant) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *QTextBuilder::saveText(const QVariant &value)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbuilder.html#saveText

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *QTextBuilder::saveText(const QVariant &value) const
    ritual = 'ritual_ZNK12QTextBuilder8saveTextERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QTextBuilder8saveTextERK8QVariant'
    address = self.uglySide.call(ritual, self._valueOf(value))
    from . import DomProperty
    return DomProperty._cuteAt(address)

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
    Notes what was given, for Qt's 'QTextBuilder::QTextBuilder()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextbuilder.html#QTextBuilder
    """
    #  QTextBuilder::QTextBuilder()
    self._noteCreation(QTextBuilder, lambda: Rituals.call(
        'ritual_ZN12QTextBuilderC1Ev',
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
