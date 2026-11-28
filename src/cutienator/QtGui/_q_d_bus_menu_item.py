"""
QDBusMenuItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusMenuItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDBusPlatformMenuItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusPlatformMenuItem = WAIT['QDBusPlatformMenuItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusMenuItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusMenuItem: a plain Python object standing in
  front of one C++ QDBusMenuItem.

  C++ hands a QDBusMenuItem around as a copy, so every C++ QDBusMenuItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusMenuItem that has a ritual and that Python can
  call so far, 1 name in all: 'convertMnemonic'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusMenuShortcut QDBusMenuItem::convertKeySequence(const
    QKeySequence &sequence)': gives a type Python has no way to take yet.
  - Qt's 'QDBusMenuItem::~QDBusMenuItem()': the destructor: Python removes
    its C++ QDBusMenuItem by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 1 leans on 'operator<<(QDebug,
  QDBusMenuItem const&)', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'QDBusPlatformMenuItem.

  What to expect
  --------------

  - The C++ QDBusMenuItem is created at the first use, not by
    'QDBusMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusMenuItem back gives a copy the ritual made for
    Python, in a new cute QDBusMenuItem.
  - Each name of Qt's QDBusMenuItem that has no cute function yet,
    'convertKeySequence', 'items', 'registerDBusTypes', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def convertMnemonic(label: str) -> str:
    """
    Calls Qt's 'QString QDBusMenuItem::convertMnemonic(const QString
    &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuitem.html#convertMnemonic

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMenuItem::convertMnemonic(const QString &label)
    return Rituals.call(
        'ritual_ZN13QDBusMenuItem15convertMnemonicERK7QString', label,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMenuItem'

  #  Qt's '~QDBusMenuItem()'. Naming it makes this a value class: Python owns
  #  every C++ QDBusMenuItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QDBusMenuItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QDBusMenuItem::QDBusMenuItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuitem.html#QDBusMenuItem
    """
    #  QDBusMenuItem::QDBusMenuItem()
    self._noteCreation(QDBusMenuItem, lambda: Rituals.call(
        'ritual_ZN13QDBusMenuItemC1Ev',
    ))

  @overload(QDBusPlatformMenuItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QDBusPlatformMenuItem]) -> None:
    """
    Notes what was given, for Qt's 'QDBusMenuItem::QDBusMenuItem(const
    QDBusPlatformMenuItem *item)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuitem.html#QDBusMenuItem

    Parameters
    ----------

    item : Optional[QDBusPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusMenuItem::QDBusMenuItem(const QDBusPlatformMenuItem *item)
    self._noteCreation(QDBusMenuItem, lambda: Rituals.call(
        'ritual_ZN13QDBusMenuItemC1EPK21QDBusPlatformMenuItem',
        self._addressOf(item),
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

  @staticmethod
  def convertKeySequence(*__, **_) -> Never:
    """
    Qt's 'QDBusMenuShortcut QDBusMenuItem::convertKeySequence(const
    QKeySequence &sequence)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusMenuItem.convertKeySequence' has no cute function yet. Qt's "
        "'QDBusMenuShortcut QDBusMenuItem::convertKeySequence(const "
        "QKeySequence &sequence)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def items(*__, **_) -> Never:
    """
    Qt's 'QDBusMenuItemList QDBusMenuItem::items(const QList<int> &ids, const
    QStringList &propertyNames)': leans on
    'QDBusPlatformMenuItem::byIds(QList<int> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuItem.items' has no cute function yet. Qt's "
        "'QDBusMenuItemList QDBusMenuItem::items(const QList<int> &ids, "
        "const QStringList &propertyNames)': leans on "
        "'QDBusPlatformMenuItem::byIds(QList<int> const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def registerDBusTypes(*__, **_) -> Never:
    """
    Qt's 'void QDBusMenuItem::registerDBusTypes()': leans on
    'operator<<(QDebug, QDBusMenuItem const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuItem.registerDBusTypes' has no cute function yet. Qt's "
        "'void QDBusMenuItem::registerDBusTypes()': leans on "
        "'operator<<(QDebug, QDBusMenuItem const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")


#  Qt's 'QList<QDBusMenuItem>': the list of QDBusMenuItem, which
#  'QList[QDBusMenuItem]' gives. It is made here, so that there is one as
#  soon as there can be a QDBusMenuItem. Qt has a name of its own for it.
QDBusMenuItemList = QList.createKind(
    QDBusMenuItem, 'value',
    name='QDBusMenuItemList',
    make='ritual_list_make_QDBusMenuItem',
    add='ritual_list_add_QDBusMenuItem',
    size='ritual_list_size_QDBusMenuItem',
    at='ritual_list_at_QDBusMenuItem',
    drop='ritual_list_drop_QDBusMenuItem',
)
