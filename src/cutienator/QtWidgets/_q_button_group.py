"""
QButtonGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qbuttongroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAbstractButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractButton = WAIT['QAbstractButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QButtonGroup(QObject):
  """
  The cute side of Qt's QButtonGroup: a plain Python object standing in front
  of one C++ QButtonGroup.

  It is built on the cute 'QObject', as Qt's QButtonGroup is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QButtonGroup that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'setExclusive',
  'exclusive', 'addButton', 'removeButton', 'buttons', 'checkedButton',
  'button', 'setId', 'id', 'checkedId'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QButtonGroup::~QButtonGroup()': the destructor: Python never
    removes a C++ QButtonGroup.

  What has no ritual
  ------------------

  16 of the 30 functions Qt declares: 8 a signal; 4 takes or gives a type
  that cannot be passed yet; 2 forbidden; 1 a template; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QButtonGroup is created at the first use, not by
    'QButtonGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QButtonGroup.
  - Qt tells when it has removed the C++ QButtonGroup. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QButtonGroup::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#tr

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
    #  QString QButtonGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QButtonGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QButtonGroup'

  #  A C++ QButtonGroup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QButtonGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QButtonGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QButtonGroup::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QButtonGroup10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def exclusive(self) -> bool:
    """
    Calls Qt's 'bool QButtonGroup::exclusive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#exclusive
    """
    #  bool QButtonGroup::exclusive() const
    return self.uglySide.call('ritual_ZNK12QButtonGroup9exclusiveEv')

  def buttons(self) -> QList[QAbstractButton]:
    """
    Calls Qt's 'QList<QAbstractButton *> QButtonGroup::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#buttons

    Returns
    -------

    QList[QAbstractButton]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractButton *> QButtonGroup::buttons() const
    address = self.uglySide.call('ritual_ZNK12QButtonGroup7buttonsEv')
    from . import QAbstractButton
    return QList[QAbstractButton]._cuteOwning(address)

  def checkedButton(self) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QButtonGroup::checkedButton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#checkedButton

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QButtonGroup::checkedButton() const
    address = self.uglySide.call('ritual_ZNK12QButtonGroup13checkedButtonEv')
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  @overload(int)
  def button(self, id: int) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QButtonGroup::button(int id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#button

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QButtonGroup::button(int id) const
    address = self.uglySide.call('ritual_ZNK12QButtonGroup6buttonEi', id)
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  @overload(QAbstractButton)
  @overload(NoneType)
  def id(self, button: Optional[QAbstractButton]) -> int:
    """
    Calls Qt's 'int QButtonGroup::id(QAbstractButton *button) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#id

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QButtonGroup::id(QAbstractButton *button) const
    return self.uglySide.call(
        'ritual_ZNK12QButtonGroup2idEP15QAbstractButton',
        self._addressOf(button),
    )

  def checkedId(self) -> int:
    """
    Calls Qt's 'int QButtonGroup::checkedId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#checkedId
    """
    #  int QButtonGroup::checkedId() const
    return self.uglySide.call('ritual_ZNK12QButtonGroup9checkedIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setExclusive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QButtonGroup::setExclusive(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#setExclusive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QButtonGroup::setExclusive(bool a0)
    self.uglySide.call('ritual_ZN12QButtonGroup12setExclusiveEb', a0)

  @overload(QAbstractButton, int)
  @overload(NoneType, int)
  def setId(self, button: Optional[QAbstractButton], id: int) -> None:
    """
    Calls Qt's 'void QButtonGroup::setId(QAbstractButton *button, int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#setId

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.
    """
    #  void QButtonGroup::setId(QAbstractButton *button, int id)
    self.uglySide.call(
        'ritual_ZN12QButtonGroup5setIdEP15QAbstractButtoni',
        self._addressOf(button), id,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QButtonGroup::QButtonGroup(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#QButtonGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QButtonGroup::QButtonGroup(QObject *parent)
    self._noteCreation(QButtonGroup, lambda: Rituals.call(
        'ritual_ZN12QButtonGroupC1EP7QObject', self._addressOf(parent),
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

  @overload(QAbstractButton)
  @overload(NoneType)
  @overload(QAbstractButton, int)
  @overload(NoneType, int)
  def addButton(self, a0: Optional[QAbstractButton], id: int = -1) -> None:
    """
    Calls Qt's 'void QButtonGroup::addButton(QAbstractButton *a0, int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#addButton

    Parameters
    ----------

    a0 : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QButtonGroup::addButton(QAbstractButton *a0, int id)
    self.uglySide.call(
        'ritual_ZN12QButtonGroup9addButtonEP15QAbstractButtoni',
        self._addressOf(a0), id,
    )

  @overload(QAbstractButton)
  @overload(NoneType)
  def removeButton(self, a0: Optional[QAbstractButton]) -> None:
    """
    Calls Qt's 'void QButtonGroup::removeButton(QAbstractButton *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuttongroup.html#removeButton

    Parameters
    ----------

    a0 : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QButtonGroup::removeButton(QAbstractButton *a0)
    self.uglySide.call(
        'ritual_ZN12QButtonGroup12removeButtonEP15QAbstractButton',
        self._addressOf(a0),
    )
