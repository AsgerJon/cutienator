"""
QTextEditMimeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QTextEditMimeData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QMimeData, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']


class QTextEditMimeData(QMimeData):
  """
  The cute side of Qt's QTextEditMimeData: a plain Python object standing in
  front of one C++ QTextEditMimeData.

  It is built on the cute 'QMimeData', as Qt's QTextEditMimeData is built on
  Qt's QMimeData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextEditMimeData that has a ritual and that Python
  can call so far, 2 names in all: 'formats', 'retrieveData'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  5 of the 7 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QTextEditMimeData; 1 leans on 'vtable for QTextEditMimeData', which Qt's
  library does not offer and Qt's source has no code for that could be taken.

  What to expect
  --------------

  - The C++ QTextEditMimeData is created at the first use, not by
    'QTextEditMimeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextEditMimeData.
  - Qt tells when it has removed the C++ QTextEditMimeData. Every call on the
    cute object, and every use of it as an argument, then raises
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
  __qt_class__ = 'QTextEditMimeData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def formats(self) -> QStringList:
    """
    Calls Qt's 'QStringList QTextEditMimeData::formats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexteditmimedata.html#formats

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTextEditMimeData::formats() const
    address = self.uglySide.call('ritual_ZNK17QTextEditMimeData7formatsEv')
    return QStringList._cuteOwning(address)

  @overload(str, QMetaType)
  def retrieveData(self, mimeType: str, type: QMetaType) -> QVariant:
    """
    Calls Qt's 'QVariant QTextEditMimeData::retrieveData(const QString
    &mimeType, QMetaType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexteditmimedata.html#retrieveData

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
    #  QVariant QTextEditMimeData::retrieveData(const QString &mimeType,
    #      QMetaType type) const
    address = self.uglySide.call(
        'ritual_ZNK17QTextEditMimeData12retrieveDataERK7QString9QMetaType',
        mimeType, self._valueOf(type),
    )
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
