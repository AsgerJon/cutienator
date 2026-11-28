"""
qdesigner_internal::MetaDataBaseItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/metadatabase_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::MetaDataBaseItem to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QDesignerMetaDataBaseItemInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MetaDataBaseItem(QDesignerMetaDataBaseItemInterface):
  """
  The cute side of Qt's qdesigner_internal::MetaDataBaseItem: a plain Python
  object standing in front of one C++ qdesigner_internal::MetaDataBaseItem.

  It is built on the cute 'QDesignerMetaDataBaseItemInterface', as Qt's
  qdesigner_internal::MetaDataBaseItem is built on Qt's
  QDesignerMetaDataBaseItemInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::MetaDataBaseItem that has a
  ritual and that Python can call so far, 12 names in all: 'name', 'setName',
  'tabOrder', 'setTabOrder', 'enabled', 'setEnabled', 'customClassName',
  'setCustomClassName', 'fakeSlots', 'setFakeSlots', 'fakeSignals',
  'setFakeSignals'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::MetaDataBaseItem::~MetaDataBaseItem()': the
    destructor: Python never removes a C++
    qdesigner_internal::MetaDataBaseItem.

  What to expect
  --------------

  - The C++ qdesigner_internal::MetaDataBaseItem is created at the first use,
    not by 'qdesigner_internal::MetaDataBaseItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::MetaDataBaseItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::MetaDataBaseItem'

  #  A C++ qdesigner_internal::MetaDataBaseItem Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_MetaDataBaseItem'

  #  The functions Qt calls itself that qdesigner_internal::MetaDataBaseItem
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setTabOrder': (
          'void qdesigner_internal::MetaDataBaseItem::setTabOrder(const '
          'QWidgetList &)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::MetaDataBaseItem::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::MetaDataBaseItem::name() const
    ritual = 'ritual_ZNK18qdesigner_internal16MetaDataBaseItem4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal16MetaDataBaseItem4nameEv'
    return self.uglySide.call(ritual)

  def tabOrder(self) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList qdesigner_internal::MetaDataBaseItem::tabOrder()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html#tabOrder

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::MetaDataBaseItem::tabOrder() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16MetaDataBaseItem8tabOrderEv',
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::MetaDataBaseItem::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html#enabled
    """
    #  bool qdesigner_internal::MetaDataBaseItem::enabled() const
    ritual = 'ritual_ZNK18qdesigner_internal16MetaDataBaseItem7enabledEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal16MetaDataBaseItem7enabledEv')
    return self.uglySide.call(ritual)

  def customClassName(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::MetaDataBaseItem::customClassName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::MetaDataBaseItem::customClassName() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16MetaDataBaseItem15customClassNameE'
        'v',
    )

  def fakeSlots(self) -> QStringList:
    """
    Calls Qt's 'QStringList qdesigner_internal::MetaDataBaseItem::fakeSlots()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html#fakeSlots

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::MetaDataBaseItem::fakeSlots() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16MetaDataBaseItem9fakeSlotsEv',
    )
    return QStringList._cuteOwning(address)

  def fakeSignals(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::MetaDataBaseItem::fakeSignals() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::MetaDataBaseItem::fakeSignals() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16MetaDataBaseItem11fakeSignalsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MetaDataBaseItem::setName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::MetaDataBaseItem::setName(const QString
    #      &name)
    ritual = (
        'ritual_ZN18qdesigner_internal16MetaDataBaseItem7setNameERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal16MetaDataBaseItem7setNameERK7Q'
          'String')
    self.uglySide.call(ritual, name)

  @overload(QList[QWidget])
  def setTabOrder(self, tabOrder: QList[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MetaDataBaseItem::setTabOrder(const
    QWidgetList &tabOrder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Parameters
    ----------

    tabOrder : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::MetaDataBaseItem::setTabOrder(const
    #      QWidgetList &tabOrder)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16MetaDataBaseItem11setTabOrderERK5QL'
        'istIP7QWidgetE',
        self._valueOf(tabOrder),
    )

  @overload(bool)
  def setEnabled(self, b: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MetaDataBaseItem::setEnabled(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::MetaDataBaseItem::setEnabled(bool b)
    ritual = 'ritual_ZN18qdesigner_internal16MetaDataBaseItem10setEnabledEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal16MetaDataBaseItem10setEnabledE'
          'b')
    self.uglySide.call(ritual, b)

  @overload(str)
  def setCustomClassName(self, customClassName: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::MetaDataBaseItem::setCustomClassName(const QString
    &customClassName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Parameters
    ----------

    customClassName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::MetaDataBaseItem::setCustomClassName(const
    #      QString &customClassName)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16MetaDataBaseItem18setCustomClassNam'
        'eERK7QString',
        customClassName,
    )

  @overload(QStringList)
  def setFakeSlots(self, a0: QStringList) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MetaDataBaseItem::setFakeSlots(const
    QStringList &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::MetaDataBaseItem::setFakeSlots(const
    #      QStringList &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16MetaDataBaseItem12setFakeSlotsERK5Q'
        'ListI7QStringE',
        self._valueOf(a0),
    )

  @overload(QStringList)
  def setFakeSignals(self, a0: QStringList) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::MetaDataBaseItem::setFakeSignals(const QStringList
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::MetaDataBaseItem::setFakeSignals(const
    #      QStringList &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16MetaDataBaseItem14setFakeSignalsERK'
        '5QListI7QStringE',
        self._valueOf(a0),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, object: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::MetaDataBaseItem::MetaDataBaseItem(QObject
    *object)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabaseitem.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::MetaDataBaseItem::MetaDataBaseItem(QObject
    #      *object)
    self._noteCreation(MetaDataBaseItem, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal16MetaDataBaseItemC1EP7QObject',
        self._addressOf(object, 'QObject'),
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
