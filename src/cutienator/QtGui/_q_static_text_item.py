"""
QStaticTextItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstatictext_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QStaticTextItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QFontEngine, QStaticTextUserData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFontEngine = WAIT['QFontEngine']
  QStaticTextUserData = WAIT['QStaticTextUserData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStaticTextItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStaticTextItem: a plain Python object standing in
  front of one C++ QStaticTextItem.

  C++ hands a QStaticTextItem around as a copy, so every C++ QStaticTextItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStaticTextItem that has a ritual and that Python
  can call so far, 4 names in all: 'setUserData', 'userData',
  'setFontEngine', 'fontEngine'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStaticTextItem::~QStaticTextItem()': the destructor: Python
    removes its C++ QStaticTextItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QStaticTextItem is created at the first use, not by
    'QStaticTextItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStaticTextItem back gives a copy the ritual made for
    Python, in a new cute QStaticTextItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStaticTextItem'

  #  Qt's '~QStaticTextItem()'. Naming it makes this a value class: Python
  #  owns every C++ QStaticTextItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QStaticTextItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def userData(self) -> Optional[QStaticTextUserData]:
    """
    Calls Qt's 'QStaticTextUserData *QStaticTextItem::userData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictextitem.html#userData

    Returns
    -------

    Optional[QStaticTextUserData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStaticTextUserData *QStaticTextItem::userData() const
    address = self.uglySide.call('ritual_ZNK15QStaticTextItem8userDataEv')
    from . import QStaticTextUserData
    return QStaticTextUserData._cuteAt(address)

  def fontEngine(self) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QStaticTextItem::fontEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictextitem.html#fontEngine

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QStaticTextItem::fontEngine() const
    address = self.uglySide.call('ritual_ZNK15QStaticTextItem10fontEngineEv')
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStaticTextUserData)
  @overload(NoneType)
  def setUserData(self, newUserData: Optional[QStaticTextUserData]) -> None:
    """
    Calls Qt's 'void QStaticTextItem::setUserData(QStaticTextUserData
    *newUserData)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictextitem.html#setUserData

    Parameters
    ----------

    newUserData : Optional[QStaticTextUserData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStaticTextItem::setUserData(QStaticTextUserData *newUserData)
    self.uglySide.call(
        'ritual_ZN15QStaticTextItem11setUserDataEP19QStaticTextUserData',
        self._addressOf(newUserData),
    )

  @overload(QFontEngine)
  @overload(NoneType)
  def setFontEngine(self, fe: Optional[QFontEngine]) -> None:
    """
    Calls Qt's 'void QStaticTextItem::setFontEngine(QFontEngine *fe)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictextitem.html#setFontEngine

    Parameters
    ----------

    fe : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStaticTextItem::setFontEngine(QFontEngine *fe)
    self.uglySide.call(
        'ritual_ZN15QStaticTextItem13setFontEngineEP11QFontEngine',
        self._addressOf(fe),
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
    Notes what was given, for Qt's 'QStaticTextItem::QStaticTextItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatictextitem.html#QStaticTextItem
    """
    #  QStaticTextItem::QStaticTextItem()
    self._noteCreation(QStaticTextItem, lambda: Rituals.call(
        'ritual_ZN15QStaticTextItemC1Ev',
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
