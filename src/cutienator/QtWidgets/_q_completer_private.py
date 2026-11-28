"""
QCompleterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCompleterPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QItemSelection, QModelIndex, QRect
  from . import QCompleter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCompleter = WAIT['QCompleter']
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCompleterPrivate(QObjectPrivate):
  """
  The cute side of Qt's QCompleterPrivate: a plain Python object standing in
  front of one C++ QCompleterPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QCompleterPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCompleterPrivate that has a ritual and that Python
  can call so far, 7 names in all: 'q_func', 'showPopup', '_q_complete',
  '_q_completionSelected', '_q_autoResizePopup', 'setCurrentIndex', 'get'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCompleter *QCompleterPrivate::q_func() const': takes in
    Python what 'QCompleter *QCompleterPrivate::q_func()' takes.
  - Qt's 'QCompleterPrivate::~QCompleterPrivate()': the destructor: Python
    never removes a C++ QCompleterPrivate.
  - Qt's 'const QCompleterPrivate *QCompleterPrivate::get(const QCompleter
    *o)': takes in Python what 'QCompleterPrivate
    *QCompleterPrivate::get(QCompleter *o)' takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 leans on 'vtable for
  QCompletionModel', which Qt's source does not mark for use from outside Qt
  and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QCompleterPrivate is created at the first use, not by
    'QCompleterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCompleterPrivate.
  - Each name of Qt's QCompleterPrivate that has no cute function yet,
    '_q_fileSystemModelDirectoryLoaded', 'init', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCompleter)
  @overload(NoneType)
  def get(o: Optional[QCompleter]) -> Optional[QCompleterPrivate]:
    """
    Calls Qt's 'QCompleterPrivate *QCompleterPrivate::get(QCompleter *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleterprivate.html#get

    Parameters
    ----------

    o : Optional[QCompleter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCompleterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCompleterPrivate *QCompleterPrivate::get(QCompleter *o)
    address = Rituals.call(
        'ritual_ZN17QCompleterPrivate3getEP10QCompleter',
        CuteMixin._addressOf(o),
    )
    return QCompleterPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCompleterPrivate'

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

  @overload(QModelIndex)
  @overload(QModelIndex, bool)
  def setCurrentIndex(self, a0: QModelIndex, a1: bool = True) -> None:
    """
    Calls Qt's 'void QCompleterPrivate::setCurrentIndex(QModelIndex a0, bool
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompleterprivate.html#setCurrentIndex

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QCompleterPrivate::setCurrentIndex(QModelIndex a0, bool a1)
    self.uglySide.call(
        'ritual_ZN17QCompleterPrivate15setCurrentIndexE11QModelIndexb',
        self._valueOf(a0), a1,
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
    Notes what was given, for Qt's 'QCompleterPrivate::QCompleterPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompleterprivate.html#QCompleterPrivate
    """
    #  QCompleterPrivate::QCompleterPrivate()
    self._noteCreation(QCompleterPrivate, lambda: Rituals.call(
        'ritual_ZN17QCompleterPrivateC1Ev',
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

  def q_func(self) -> Optional[QCompleter]:
    """
    Calls Qt's 'QCompleter *QCompleterPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleterprivate.html#q_func

    Returns
    -------

    Optional[QCompleter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCompleter *QCompleterPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QCompleterPrivate6q_funcEv')
    from . import QCompleter
    return QCompleter._cuteAt(address)

  @overload(QRect)
  def showPopup(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QCompleterPrivate::showPopup(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleterprivate.html#showPopup

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QCompleterPrivate::showPopup(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN17QCompleterPrivate9showPopupERK5QRect', self._valueOf(a0),
    )

  @overload(QModelIndex)
  @overload(QModelIndex, bool)
  def _q_complete(self, a0: QModelIndex, a1: bool = False) -> None:
    """
    Calls Qt's 'void QCompleterPrivate::_q_complete(QModelIndex a0, bool
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleterprivate.html#_q_complete

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QCompleterPrivate::_q_complete(QModelIndex a0, bool a1)
    self.uglySide.call(
        'ritual_ZN17QCompleterPrivate11_q_completeE11QModelIndexb',
        self._valueOf(a0), a1,
    )

  @overload(QItemSelection)
  def _q_completionSelected(self, a0: QItemSelection) -> None:
    """
    Calls Qt's 'void QCompleterPrivate::_q_completionSelected(const
    QItemSelection &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompleterprivate.html#_q_completionSelected

    Parameters
    ----------

    a0 : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void QCompleterPrivate::_q_completionSelected(const QItemSelection
    #      &a0)
    self.uglySide.call(
        'ritual_ZN17QCompleterPrivate21_q_completionSelectedERK14QItemSelec'
        'tion',
        self._valueOf(a0),
    )

  def _q_autoResizePopup(self) -> None:
    """
    Calls Qt's 'void QCompleterPrivate::_q_autoResizePopup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompleterprivate.html#_q_autoResizePopup
    """
    #  void QCompleterPrivate::_q_autoResizePopup()
    self.uglySide.call('ritual_ZN17QCompleterPrivate18_q_autoResizePopupEv')

  @staticmethod
  def _q_fileSystemModelDirectoryLoaded(*__, **_) -> Never:
    """
    Qt's 'void QCompleterPrivate::_q_fileSystemModelDirectoryLoaded(const
    QString &path)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QCompleterPrivate._q_fileSystemModelDirectoryLoaded' has no cute "
        "function yet. Qt's 'void "
        "QCompleterPrivate::_q_fileSystemModelDirectoryLoaded(const QString "
        "&path)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QCompleterPrivate::init(QAbstractItemModel *model)': leans on
    'vtable for QCompletionModel', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCompleterPrivate.init' has no cute function yet. Qt's 'void "
        "QCompleterPrivate::init(QAbstractItemModel *model)': leans on "
        "'vtable for QCompletionModel', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
