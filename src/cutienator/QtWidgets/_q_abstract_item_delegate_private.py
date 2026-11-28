"""
QAbstractItemDelegatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qabstractitemdelegate_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractItemDelegatePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QLocale, QObject, QVariant
  from . import QAbstractItemDelegate, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QLocale = WAIT['QLocale']
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemDelegatePrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractItemDelegatePrivate: a plain Python object
  standing in front of one C++ QAbstractItemDelegatePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QAbstractItemDelegatePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemDelegatePrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'handleEditorEvent',
  'tryFixup', 'textForRole', '_q_commitDataAndCloseEditor'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractItemDelegate *QAbstractItemDelegatePrivate::q_func()
    const': takes in Python what 'QAbstractItemDelegate
    *QAbstractItemDelegatePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QAbstractItemDelegatePrivate is created at the first use, not by
    'QAbstractItemDelegatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemDelegatePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemDelegatePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.ItemDataRole, QVariant, QLocale)
  @overload(Qt.ItemDataRole, QVariant, QLocale, int)
  def textForRole(
      self,
      role: Qt.ItemDataRole,
      value: QVariant,
      locale: QLocale,
      precision: int = 6,
  ) -> str:
    """
    Calls Qt's 'QString
    QAbstractItemDelegatePrivate::textForRole(Qt::ItemDataRole role, const
    QVariant &value, const QLocale &locale, int precision) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegateprivate.html#textForRole

    Parameters
    ----------

    role : Qt.ItemDataRole
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    precision : int
      Passed on as it is. May be left out, as in Qt: it is then 6.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractItemDelegatePrivate::textForRole(Qt::ItemDataRole
    #      role, const QVariant &value, const QLocale &locale, int precision)
    #      const
    return self.uglySide.call(
        'ritual_ZNK28QAbstractItemDelegatePrivate11textForRoleEN2Qt12ItemDa'
        'taRoleERK8QVariantRK7QLocalei',
        role.value, self._valueOf(value), self._valueOf(locale), precision,
    )

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
    Notes what was given, for Qt's
    'QAbstractItemDelegatePrivate::QAbstractItemDelegatePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegateprivate.html
    """
    #  QAbstractItemDelegatePrivate::QAbstractItemDelegatePrivate()
    self._noteCreation(QAbstractItemDelegatePrivate, lambda: Rituals.call(
        'ritual_ZN28QAbstractItemDelegatePrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate
    *QAbstractItemDelegatePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegateprivate.html#q_func

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QAbstractItemDelegatePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QAbstractItemDelegatePrivate6q_funcEv',
    )
    from . import QAbstractItemDelegate
    return QAbstractItemDelegate._cuteAt(address)

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def handleEditorEvent(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemDelegatePrivate::handleEditorEvent(QObject
    *object, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegateprivate.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemDelegatePrivate::handleEditorEvent(QObject *object,
    #      QEvent *event)
    return self.uglySide.call(
        'ritual_ZN28QAbstractItemDelegatePrivate17handleEditorEventEP7QObje'
        'ctP6QEvent',
        self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QWidget)
  @overload(NoneType)
  def tryFixup(self, editor: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QAbstractItemDelegatePrivate::tryFixup(QWidget
    *editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegateprivate.html#tryFixup

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemDelegatePrivate::tryFixup(QWidget *editor)
    return self.uglySide.call(
        'ritual_ZN28QAbstractItemDelegatePrivate8tryFixupEP7QWidget',
        self._addressOf(editor),
    )

  @overload(QWidget)
  @overload(NoneType)
  def _q_commitDataAndCloseEditor(self, editor: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    QAbstractItemDelegatePrivate::_q_commitDataAndCloseEditor(QWidget
    *editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegateprivate.html

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemDelegatePrivate::_q_commitDataAndCloseEditor(QWidget
    #      *editor)
    self.uglySide.call(
        'ritual_ZN28QAbstractItemDelegatePrivate27_q_commitDataAndCloseEdit'
        'orEP7QWidget',
        self._addressOf(editor),
    )
