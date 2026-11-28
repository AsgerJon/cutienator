"""
QWebEngineDesktopMediaRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginedesktopmediarequest.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractListModel, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QWebEngineDesktopMediaRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineDesktopMediaRequest: a plain Python object
  standing in front of one C++ QWebEngineDesktopMediaRequest.

  C++ hands a QWebEngineDesktopMediaRequest around as a copy, so every C++
  QWebEngineDesktopMediaRequest behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineDesktopMediaRequest that has a ritual and
  that Python can call so far, 5 names in all: 'screensModel',
  'windowsModel', 'selectScreen', 'selectWindow', 'cancel'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineDesktopMediaRequest::~QWebEngineDesktopMediaRequest()':
    the destructor: Python removes its C++ QWebEngineDesktopMediaRequest by
    it, and has no other use for it.
  - Qt's 'QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest(
    QWebEngineDesktopMediaRequest &&other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QWebEngineDesktopMediaRequest
    &QWebEngineDesktopMediaRequest::operator=(const
    QWebEngineDesktopMediaRequest &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'QWebEngineDesktopMediaRequest
    &QWebEngineDesktopMediaRequest::operator=(QWebEngineDesktopMediaRequest
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void
    QWebEngineDesktopMediaRequest::swap(QWebEngineDesktopMediaRequest
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest(
    QtWebEngineCore::DesktopMediaController *controller)': names
    'QtWebEngineCore::DesktopMediaController', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineDesktopMediaRequest is created at the first use, not by
    'QWebEngineDesktopMediaRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineDesktopMediaRequest back gives a copy the
    ritual made for Python, in a new cute QWebEngineDesktopMediaRequest.
  - Each name of Qt's QWebEngineDesktopMediaRequest that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QWebEngineDesktopMediaRequest'

  #  Qt's '~QWebEngineDesktopMediaRequest()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineDesktopMediaRequest behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QWebEngineDesktopMediaRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def screensModel(self) -> Optional[QAbstractListModel]:
    """
    Calls Qt's 'QAbstractListModel
    *QWebEngineDesktopMediaRequest::screensModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedesktopmediarequest.html#screensModel

    Returns
    -------

    Optional[QAbstractListModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractListModel *QWebEngineDesktopMediaRequest::screensModel()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QWebEngineDesktopMediaRequest12screensModelEv',
    )
    from ..QtCore import QAbstractListModel
    return QAbstractListModel._cuteAt(address)

  def windowsModel(self) -> Optional[QAbstractListModel]:
    """
    Calls Qt's 'QAbstractListModel
    *QWebEngineDesktopMediaRequest::windowsModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedesktopmediarequest.html#windowsModel

    Returns
    -------

    Optional[QAbstractListModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractListModel *QWebEngineDesktopMediaRequest::windowsModel()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QWebEngineDesktopMediaRequest12windowsModelEv',
    )
    from ..QtCore import QAbstractListModel
    return QAbstractListModel._cuteAt(address)

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
    'QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedesktopmediarequest.html
    """
    #  QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest()
    self._noteCreation(QWebEngineDesktopMediaRequest, lambda: Rituals.call(
        'ritual_ZN29QWebEngineDesktopMediaRequestC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineDesktopMediaRequest) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest(const
    QWebEngineDesktopMediaRequest &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedesktopmediarequest.html

    Parameters
    ----------

    other : QWebEngineDesktopMediaRequest
      Passed on as a value: Qt reads the C++ QWebEngineDesktopMediaRequest,
      which stays Python's own.
    """
    #  QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest(const
    #      QWebEngineDesktopMediaRequest &other)
    self._noteCreation(QWebEngineDesktopMediaRequest, lambda: Rituals.call(
        'ritual_ZN29QWebEngineDesktopMediaRequestC1ERKS_',
        self._valueOf(other),
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

  @overload(QModelIndex)
  def selectScreen(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QWebEngineDesktopMediaRequest::selectScreen(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedesktopmediarequest.html#selectScreen

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QWebEngineDesktopMediaRequest::selectScreen(const QModelIndex
    #      &index) const
    self.uglySide.call(
        'ritual_ZNK29QWebEngineDesktopMediaRequest12selectScreenERK11QModel'
        'Index',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def selectWindow(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QWebEngineDesktopMediaRequest::selectWindow(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedesktopmediarequest.html#selectWindow

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QWebEngineDesktopMediaRequest::selectWindow(const QModelIndex
    #      &index) const
    self.uglySide.call(
        'ritual_ZNK29QWebEngineDesktopMediaRequest12selectWindowERK11QModel'
        'Index',
        self._valueOf(index),
    )

  def cancel(self) -> None:
    """
    Calls Qt's 'void QWebEngineDesktopMediaRequest::cancel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedesktopmediarequest.html#cancel
    """
    #  void QWebEngineDesktopMediaRequest::cancel() const
    self.uglySide.call('ritual_ZNK29QWebEngineDesktopMediaRequest6cancelEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void
    QWebEngineDesktopMediaRequest::swap(QWebEngineDesktopMediaRequest
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineDesktopMediaRequest.swap' has no cute function yet. "
        "Qt's 'void "
        "QWebEngineDesktopMediaRequest::swap(QWebEngineDesktopMediaRequest "
        "&other)': takes a type Python has no way to hand over yet.")
