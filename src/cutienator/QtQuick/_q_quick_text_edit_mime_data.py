"""
QQuickTextEditMimeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextEditMimeData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMimeData, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QMetaType, QVariant
  from ..QtGui import QTextDocumentFragment
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QTextDocumentFragment = WAIT['QTextDocumentFragment']


class QQuickTextEditMimeData(QMimeData):
  """
  The cute side of Qt's QQuickTextEditMimeData: a plain Python object
  standing in front of one C++ QQuickTextEditMimeData.

  It is built on the cute 'QMimeData', as Qt's QQuickTextEditMimeData is
  built on Qt's QMimeData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextEditMimeData that has a ritual and that
  Python can call so far, 3 names in all: 'formats', 'retrieveData', 'setup'.
  It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickTextEditMimeData is created at the first use, not by
    'QQuickTextEditMimeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextEditMimeData.
  - Qt tells when it has removed the C++ QQuickTextEditMimeData. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextEditMimeData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def formats(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickTextEditMimeData::formats() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditmimedata.html#formats

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickTextEditMimeData::formats() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTextEditMimeData7formatsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str, QMetaType)
  def retrieveData(self, mimeType: str, type: QMetaType) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickTextEditMimeData::retrieveData(const QString
    &mimeType, QMetaType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditmimedata.html#retrieveData

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTextEditMimeData::retrieveData(const QString &mimeType,
    #      QMetaType type) const
    ritual = (
        'ritual_ZNK22QQuickTextEditMimeData12retrieveDataERK7QString9QMetaT'
        'ype')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QQuickTextEditMimeData12retrieveDataERK7QString9'
          'QMetaType')
    address = self.uglySide.call(ritual, mimeType, self._valueOf(type))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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

  @overload(QTextDocumentFragment)
  def __init__(self, aFragment: QTextDocumentFragment) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTextEditMimeData::QQuickTextEditMimeData(const
    QTextDocumentFragment &aFragment)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexteditmimedata.html#QQuickTextEditMimeData

    Parameters
    ----------

    aFragment : QTextDocumentFragment
      Passed on as a value: Qt reads the C++ QTextDocumentFragment, which
      stays Python's own.
    """
    #  QQuickTextEditMimeData::QQuickTextEditMimeData(const
    #      QTextDocumentFragment &aFragment)
    self._noteCreation(QQuickTextEditMimeData, lambda: Rituals.call(
        'ritual_ZN22QQuickTextEditMimeDataC1ERK21QTextDocumentFragment',
        self._valueOf(aFragment),
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

  def setup(self) -> None:
    """
    Calls Qt's 'void QQuickTextEditMimeData::setup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktexteditmimedata.html#setup
    """
    #  void QQuickTextEditMimeData::setup() const
    self.uglySide.call('ritual_ZNK22QQuickTextEditMimeData5setupEv')
