"""
QQuickFileDialogImplPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialogImplPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QDir, QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo
  from . import QQuickFileDialogImpl, QQuickFileDialogImplAttached
  from ..QtQuickTemplates2 import QQuickAbstractButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickFileDialogImpl = WAIT['QQuickFileDialogImpl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileDialogImplPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFileDialogImplPrivate: a plain Python object
  standing in front of one C++ QQuickFileDialogImplPrivate.

  What exists
  -----------

  Every function of Qt's QQuickFileDialogImplPrivate that has a ritual and
  that Python can call so far, 15 names in all: 'q_func', 'get',
  'attachedOrWarn', 'setNameFilters', 'updateEnabled', 'updateSelectedFile',
  'updateFileNameTextEdit', 'fileListSortFlags', 'fileList',
  'setFileDialogListViewCurrentIndex',
  'tryUpdateFileDialogListViewCurrentIndex',
  'fileDialogListViewCountChanged', 'handleAccept', 'handleClick',
  'selectFile'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFileDialogImpl *QQuickFileDialogImplPrivate::q_func()
    const': takes in Python what 'QQuickFileDialogImpl
    *QQuickFileDialogImplPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickFileDialogImplPrivate is created at the first use, not by
    'QQuickFileDialogImplPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialogImplPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickFileDialogImpl)
  @overload(NoneType)
  def get(
      dialog: Optional[QQuickFileDialogImpl],
  ) -> Optional[QQuickFileDialogImplPrivate]:
    """
    Calls Qt's 'QQuickFileDialogImplPrivate
    *QQuickFileDialogImplPrivate::get(QQuickFileDialogImpl *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#get

    Parameters
    ----------

    dialog : Optional[QQuickFileDialogImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFileDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImplPrivate
    #      *QQuickFileDialogImplPrivate::get(QQuickFileDialogImpl *dialog)
    address = Rituals.call(
        'ritual_ZN27QQuickFileDialogImplPrivate3getEP20QQuickFileDialogImpl',
        CuteMixin._addressOf(dialog),
    )
    return QQuickFileDialogImplPrivate._cuteAt(address)

  @staticmethod
  def fileListSortFlags() -> QDir.SortFlags:
    """
    Calls Qt's 'QDir::SortFlags
    QQuickFileDialogImplPrivate::fileListSortFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#fileListSortFlags

    Returns
    -------

    QDir.SortFlags
      The value standing for the combination Qt gave back.
    """
    #  QDir::SortFlags QQuickFileDialogImplPrivate::fileListSortFlags()
    return QDir.SortFlags(Rituals.call(
        'ritual_ZN27QQuickFileDialogImplPrivate17fileListSortFlagsEv',
    ))

  @staticmethod
  @overload(QDir)
  def fileList(dir: QDir) -> QList[QFileInfo]:
    """
    Calls Qt's 'QFileInfoList QQuickFileDialogImplPrivate::fileList(const
    QDir &dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#fileList

    Parameters
    ----------

    dir : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    Returns
    -------

    QList[QFileInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QFileInfoList QQuickFileDialogImplPrivate::fileList(const QDir &dir)
    address = Rituals.call(
        'ritual_ZN27QQuickFileDialogImplPrivate8fileListERK4QDir',
        CuteMixin._valueOf(dir),
    )
    from ..QtCore import QFileInfo
    return QList[QFileInfo]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialogImplPrivate'

  #  A C++ QQuickFileDialogImplPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFileDialogImplPrivate'

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

  @overload(QStringList)
  def setNameFilters(self, filters: QStringList) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplPrivate::setNameFilters(const
    QStringList &filters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#setNameFilters

    Parameters
    ----------

    filters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickFileDialogImplPrivate::setNameFilters(const QStringList
    #      &filters)
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate14setNameFiltersERK5QListI7Q'
        'StringE',
        self._valueOf(filters),
    )

  @overload(int)
  def setFileDialogListViewCurrentIndex(self, newCurrentIndex: int) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplPrivate::setFileDialogListViewCurrentIndex(int
    newCurrentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html

    Parameters
    ----------

    newCurrentIndex : int
      Passed on as it is.
    """
    #  void
    #      QQuickFileDialogImplPrivate::setFileDialogListViewCurrentIndex(int
    #      newCurrentIndex)
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate33setFileDialogListViewCurre'
        'ntIndexEi',
        newCurrentIndex,
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
    Notes what was given, for Qt's
    'QQuickFileDialogImplPrivate::QQuickFileDialogImplPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html
    """
    #  QQuickFileDialogImplPrivate::QQuickFileDialogImplPrivate()
    self._noteCreation(QQuickFileDialogImplPrivate, lambda: Rituals.call(
        'ritual_ZN27QQuickFileDialogImplPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickFileDialogImpl]:
    """
    Calls Qt's 'QQuickFileDialogImpl *QQuickFileDialogImplPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#q_func

    Returns
    -------

    Optional[QQuickFileDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImpl *QQuickFileDialogImplPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate6q_funcEv',
    )
    from . import QQuickFileDialogImpl
    return QQuickFileDialogImpl._cuteAt(address)

  def attachedOrWarn(self) -> Optional[QQuickFileDialogImplAttached]:
    """
    Calls Qt's 'QQuickFileDialogImplAttached
    *QQuickFileDialogImplPrivate::attachedOrWarn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#attachedOrWarn

    Returns
    -------

    Optional[QQuickFileDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImplAttached
    #      *QQuickFileDialogImplPrivate::attachedOrWarn()
    address = self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate14attachedOrWarnEv',
    )
    from . import QQuickFileDialogImplAttached
    return QQuickFileDialogImplAttached._cuteAt(address)

  def updateEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplPrivate::updateEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#updateEnabled
    """
    #  void QQuickFileDialogImplPrivate::updateEnabled()
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate13updateEnabledEv',
    )

  @overload(str)
  def updateSelectedFile(self, oldFolderPath: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplPrivate::updateSelectedFile(const
    QString &oldFolderPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html

    Parameters
    ----------

    oldFolderPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialogImplPrivate::updateSelectedFile(const QString
    #      &oldFolderPath)
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate18updateSelectedFileERK7QStr'
        'ing',
        oldFolderPath,
    )

  def updateFileNameTextEdit(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplPrivate::updateFileNameTextEdit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html
    """
    #  void QQuickFileDialogImplPrivate::updateFileNameTextEdit()
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate22updateFileNameTextEditEv',
    )

  @overload(int)
  def tryUpdateFileDialogListViewCurrentIndex(
      self,
      newCurrentIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplPrivate::tryUpdateFileDialogListViewCurrentIndex(int
    newCurrentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html

    Parameters
    ----------

    newCurrentIndex : int
      Passed on as it is.
    """
    #  void QQuickFileDialogImplPrivate::
    #      tryUpdateFileDialogListViewCurrentIndex(int newCurrentIndex)
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate39tryUpdateFileDialogListVie'
        'wCurrentIndexEi',
        newCurrentIndex,
    )

  def fileDialogListViewCountChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplPrivate::fileDialogListViewCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html
    """
    #  void QQuickFileDialogImplPrivate::fileDialogListViewCountChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate30fileDialogListViewCountCha'
        'ngedEv',
    )

  def handleAccept(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplPrivate::handleAccept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#handleAccept
    """
    #  void QQuickFileDialogImplPrivate::handleAccept()
    ritual = 'ritual_ZN27QQuickFileDialogImplPrivate12handleAcceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickFileDialogImplPrivate12handleAcceptEv'
    self.uglySide.call(ritual)

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def handleClick(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplPrivate::handleClick(QQuickAbstractButton *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#handleClick

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplPrivate::handleClick(QQuickAbstractButton
    #      *button)
    ritual = (
        'ritual_ZN27QQuickFileDialogImplPrivate11handleClickEP20QQuickAbstr'
        'actButton')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickFileDialogImplPrivate11handleClickEP20QQuic'
          'kAbstractButton')
    self.uglySide.call(ritual, self._addressOf(button))

  def selectFile(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplPrivate::selectFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplprivate.html#selectFile
    """
    #  void QQuickFileDialogImplPrivate::selectFile()
    self.uglySide.call(
        'ritual_ZN27QQuickFileDialogImplPrivate10selectFileEv',
    )
