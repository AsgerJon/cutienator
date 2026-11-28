"""
DomLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomLayout to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomLayoutItem, DomProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomLayoutItem = WAIT['DomLayoutItem']
  DomProperty = WAIT['DomProperty']


class DomLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomLayout: a plain Python object standing in front of
  one C++ DomLayout.

  What exists
  -----------

  Every function of Qt's DomLayout that has a ritual and that Python can call
  so far, 34 names in all: 'hasAttributeClass', 'attributeClass',
  'setAttributeClass', 'clearAttributeClass', 'hasAttributeName',
  'attributeName', 'setAttributeName', 'clearAttributeName',
  'hasAttributeStretch', 'attributeStretch', 'setAttributeStretch',
  'clearAttributeStretch', 'hasAttributeRowStretch', 'attributeRowStretch',
  'setAttributeRowStretch', 'clearAttributeRowStretch',
  'hasAttributeColumnStretch', 'attributeColumnStretch',
  'setAttributeColumnStretch', 'clearAttributeColumnStretch',
  'hasAttributeRowMinimumHeight', 'attributeRowMinimumHeight',
  'setAttributeRowMinimumHeight', 'clearAttributeRowMinimumHeight',
  'hasAttributeColumnMinimumWidth', 'attributeColumnMinimumWidth',
  'setAttributeColumnMinimumWidth', 'clearAttributeColumnMinimumWidth',
  'elementProperty', 'setElementProperty', 'elementAttribute',
  'setElementAttribute', 'elementItem', 'setElementItem'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomLayout::~DomLayout()': the destructor: Python never removes a
    C++ DomLayout.
  - Qt's 'void DomLayout::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomLayout::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomLayout is created at the first use, not by 'DomLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomLayout.
  - Each name of Qt's DomLayout that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeClass(self) -> bool:
    """
    Calls Qt's 'bool DomLayout::hasAttributeClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#hasAttributeClass
    """
    #  bool DomLayout::hasAttributeClass() const
    return self.uglySide.call('ritual_ZNK9DomLayout17hasAttributeClassEv')

  def attributeClass(self) -> str:
    """
    Calls Qt's 'QString DomLayout::attributeClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#attributeClass

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayout::attributeClass() const
    return self.uglySide.call('ritual_ZNK9DomLayout14attributeClassEv')

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomLayout::hasAttributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#hasAttributeName
    """
    #  bool DomLayout::hasAttributeName() const
    return self.uglySide.call('ritual_ZNK9DomLayout16hasAttributeNameEv')

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomLayout::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayout::attributeName() const
    return self.uglySide.call('ritual_ZNK9DomLayout13attributeNameEv')

  def hasAttributeStretch(self) -> bool:
    """
    Calls Qt's 'bool DomLayout::hasAttributeStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#hasAttributeStretch
    """
    #  bool DomLayout::hasAttributeStretch() const
    return self.uglySide.call('ritual_ZNK9DomLayout19hasAttributeStretchEv')

  def attributeStretch(self) -> str:
    """
    Calls Qt's 'QString DomLayout::attributeStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#attributeStretch

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayout::attributeStretch() const
    return self.uglySide.call('ritual_ZNK9DomLayout16attributeStretchEv')

  def hasAttributeRowStretch(self) -> bool:
    """
    Calls Qt's 'bool DomLayout::hasAttributeRowStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#hasAttributeRowStretch
    """
    #  bool DomLayout::hasAttributeRowStretch() const
    return self.uglySide.call(
        'ritual_ZNK9DomLayout22hasAttributeRowStretchEv',
    )

  def attributeRowStretch(self) -> str:
    """
    Calls Qt's 'QString DomLayout::attributeRowStretch() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#attributeRowStretch

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayout::attributeRowStretch() const
    return self.uglySide.call('ritual_ZNK9DomLayout19attributeRowStretchEv')

  def hasAttributeColumnStretch(self) -> bool:
    """
    Calls Qt's 'bool DomLayout::hasAttributeColumnStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#hasAttributeColumnStretch
    """
    #  bool DomLayout::hasAttributeColumnStretch() const
    return self.uglySide.call(
        'ritual_ZNK9DomLayout25hasAttributeColumnStretchEv',
    )

  def attributeColumnStretch(self) -> str:
    """
    Calls Qt's 'QString DomLayout::attributeColumnStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#attributeColumnStretch

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayout::attributeColumnStretch() const
    return self.uglySide.call(
        'ritual_ZNK9DomLayout22attributeColumnStretchEv',
    )

  def hasAttributeRowMinimumHeight(self) -> bool:
    """
    Calls Qt's 'bool DomLayout::hasAttributeRowMinimumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#hasAttributeRowMinimumHeight
    """
    #  bool DomLayout::hasAttributeRowMinimumHeight() const
    return self.uglySide.call(
        'ritual_ZNK9DomLayout28hasAttributeRowMinimumHeightEv',
    )

  def attributeRowMinimumHeight(self) -> str:
    """
    Calls Qt's 'QString DomLayout::attributeRowMinimumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#attributeRowMinimumHeight

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayout::attributeRowMinimumHeight() const
    return self.uglySide.call(
        'ritual_ZNK9DomLayout25attributeRowMinimumHeightEv',
    )

  def hasAttributeColumnMinimumWidth(self) -> bool:
    """
    Calls Qt's 'bool DomLayout::hasAttributeColumnMinimumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#hasAttributeColumnMinimumWidth
    """
    #  bool DomLayout::hasAttributeColumnMinimumWidth() const
    return self.uglySide.call(
        'ritual_ZNK9DomLayout30hasAttributeColumnMinimumWidthEv',
    )

  def attributeColumnMinimumWidth(self) -> str:
    """
    Calls Qt's 'QString DomLayout::attributeColumnMinimumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#attributeColumnMinimumWidth

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayout::attributeColumnMinimumWidth() const
    return self.uglySide.call(
        'ritual_ZNK9DomLayout27attributeColumnMinimumWidthEv',
    )

  def elementProperty(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomLayout::elementProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#elementProperty

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomLayout::elementProperty() const
    address = self.uglySide.call('ritual_ZNK9DomLayout15elementPropertyEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementAttribute(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomLayout::elementAttribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#elementAttribute

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomLayout::elementAttribute() const
    address = self.uglySide.call('ritual_ZNK9DomLayout16elementAttributeEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementItem(self) -> QList[DomLayoutItem]:
    """
    Calls Qt's 'QList<DomLayoutItem *> DomLayout::elementItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#elementItem

    Returns
    -------

    QList[DomLayoutItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomLayoutItem *> DomLayout::elementItem() const
    address = self.uglySide.call('ritual_ZNK9DomLayout11elementItemEv')
    from . import DomLayoutItem
    return QList[DomLayoutItem]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeClass(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayout::setAttributeClass(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#setAttributeClass

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayout::setAttributeClass(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout17setAttributeClassERK7QString', a,
    )

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayout::setAttributeName(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayout::setAttributeName(const QString &a)
    self.uglySide.call('ritual_ZN9DomLayout16setAttributeNameERK7QString', a)

  @overload(str)
  def setAttributeStretch(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayout::setAttributeStretch(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#setAttributeStretch

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayout::setAttributeStretch(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout19setAttributeStretchERK7QString', a,
    )

  @overload(str)
  def setAttributeRowStretch(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayout::setAttributeRowStretch(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#setAttributeRowStretch

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayout::setAttributeRowStretch(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout22setAttributeRowStretchERK7QString', a,
    )

  @overload(str)
  def setAttributeColumnStretch(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayout::setAttributeColumnStretch(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#setAttributeColumnStretch

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayout::setAttributeColumnStretch(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout25setAttributeColumnStretchERK7QString', a,
    )

  @overload(str)
  def setAttributeRowMinimumHeight(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayout::setAttributeRowMinimumHeight(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#setAttributeRowMinimumHeight

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayout::setAttributeRowMinimumHeight(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout28setAttributeRowMinimumHeightERK7QString', a,
    )

  @overload(str)
  def setAttributeColumnMinimumWidth(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayout::setAttributeColumnMinimumWidth(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#setAttributeColumnMinimumWidth

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayout::setAttributeColumnMinimumWidth(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout30setAttributeColumnMinimumWidthERK7QString', a,
    )

  @overload(QList[DomProperty])
  def setElementProperty(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomLayout::setElementProperty(const QList<DomProperty *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#setElementProperty

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomLayout::setElementProperty(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout18setElementPropertyERK5QListIP11DomPropertyE',
        self._valueOf(a),
    )

  @overload(QList[DomProperty])
  def setElementAttribute(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomLayout::setElementAttribute(const QList<DomProperty
    *> &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#setElementAttribute

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomLayout::setElementAttribute(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout19setElementAttributeERK5QListIP11DomPropertyE',
        self._valueOf(a),
    )

  @overload(QList[DomLayoutItem])
  def setElementItem(self, a: QList[DomLayoutItem]) -> None:
    """
    Calls Qt's 'void DomLayout::setElementItem(const QList<DomLayoutItem *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#setElementItem

    Parameters
    ----------

    a : QList[DomLayoutItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomLayout::setElementItem(const QList<DomLayoutItem *> &a)
    self.uglySide.call(
        'ritual_ZN9DomLayout14setElementItemERK5QListIP13DomLayoutItemE',
        self._valueOf(a),
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
    Notes what was given, for Qt's 'DomLayout::DomLayout()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#DomLayout
    """
    #  DomLayout::DomLayout()
    self._noteCreation(DomLayout, lambda: Rituals.call(
        'ritual_ZN9DomLayoutC1Ev',
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

  def clearAttributeClass(self) -> None:
    """
    Calls Qt's 'void DomLayout::clearAttributeClass()'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#clearAttributeClass
    """
    #  void DomLayout::clearAttributeClass()
    self.uglySide.call('ritual_ZN9DomLayout19clearAttributeClassEv')

  def clearAttributeName(self) -> None:
    """
    Calls Qt's 'void DomLayout::clearAttributeName()'.

    Qt's own words: https://doc.qt.io/qt-6/domlayout.html#clearAttributeName
    """
    #  void DomLayout::clearAttributeName()
    self.uglySide.call('ritual_ZN9DomLayout18clearAttributeNameEv')

  def clearAttributeStretch(self) -> None:
    """
    Calls Qt's 'void DomLayout::clearAttributeStretch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#clearAttributeStretch
    """
    #  void DomLayout::clearAttributeStretch()
    self.uglySide.call('ritual_ZN9DomLayout21clearAttributeStretchEv')

  def clearAttributeRowStretch(self) -> None:
    """
    Calls Qt's 'void DomLayout::clearAttributeRowStretch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#clearAttributeRowStretch
    """
    #  void DomLayout::clearAttributeRowStretch()
    self.uglySide.call('ritual_ZN9DomLayout24clearAttributeRowStretchEv')

  def clearAttributeColumnStretch(self) -> None:
    """
    Calls Qt's 'void DomLayout::clearAttributeColumnStretch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#clearAttributeColumnStretch
    """
    #  void DomLayout::clearAttributeColumnStretch()
    self.uglySide.call('ritual_ZN9DomLayout27clearAttributeColumnStretchEv')

  def clearAttributeRowMinimumHeight(self) -> None:
    """
    Calls Qt's 'void DomLayout::clearAttributeRowMinimumHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#clearAttributeRowMinimumHeight
    """
    #  void DomLayout::clearAttributeRowMinimumHeight()
    self.uglySide.call(
        'ritual_ZN9DomLayout30clearAttributeRowMinimumHeightEv',
    )

  def clearAttributeColumnMinimumWidth(self) -> None:
    """
    Calls Qt's 'void DomLayout::clearAttributeColumnMinimumWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayout.html#clearAttributeColumnMinimumWidth
    """
    #  void DomLayout::clearAttributeColumnMinimumWidth()
    self.uglySide.call(
        'ritual_ZN9DomLayout32clearAttributeColumnMinimumWidthEv',
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomLayout::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLayout.read' has no cute function yet. Qt's 'void "
        "DomLayout::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomLayout::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLayout.write' has no cute function yet. Qt's 'void "
        "DomLayout::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomLayout *>': the list of DomLayout, which 'QList[DomLayout]'
#  gives. It is made here, so that there is one as soon as there can be a
#  DomLayout.
QList.createKind(
    DomLayout, 'address',
    make='ritual_list_make_DomLayout_ptr',
    add='ritual_list_add_DomLayout_ptr',
    size='ritual_list_size_DomLayout_ptr',
    at='ritual_list_at_DomLayout_ptr',
    drop='ritual_list_drop_DomLayout_ptr',
)
