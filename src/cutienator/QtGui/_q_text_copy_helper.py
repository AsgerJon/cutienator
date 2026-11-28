"""
QTextCopyHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTextCopyHelper to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QTextFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextFormat = WAIT['QTextFormat']


class QTextCopyHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextCopyHelper: a plain Python object standing in
  front of one C++ QTextCopyHelper.

  C++ hands a QTextCopyHelper around as a copy, so every C++ QTextCopyHelper
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextCopyHelper that has a ritual and that Python
  can call so far, 5 names in all: 'copy', 'appendFragments',
  'appendFragment', 'convertFormatIndex', 'convertFormat'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextCopyHelper::~QTextCopyHelper()': the destructor: Python
    removes its C++ QTextCopyHelper by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QTextCopyHelper is created at the first use, not by
    'QTextCopyHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextCopyHelper back gives a copy the ritual made for
    Python, in a new cute QTextCopyHelper.
  - Each name of Qt's QTextCopyHelper that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QTextCopyHelper'

  #  Qt's '~QTextCopyHelper()'. Naming it makes this a value class: Python
  #  owns every C++ QTextCopyHelper behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QTextCopyHelperD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QTextCopyHelper::QTextCopyHelper(const QTextCursor &_source, const
    QTextCursor &_destination, bool forceCharFormat, const QTextCharFormat
    &fmt)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QTextCopyHelper.__init__' has no cute function yet. Qt's "
        "'QTextCopyHelper::QTextCopyHelper(const QTextCursor &_source, "
        "const QTextCursor &_destination, bool forceCharFormat, const "
        "QTextCharFormat &fmt)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

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

  def copy(self) -> None:
    """
    Calls Qt's 'void QTextCopyHelper::copy()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcopyhelper.html#copy
    """
    #  void QTextCopyHelper::copy()
    self.uglySide.call('ritual_ZN15QTextCopyHelper4copyEv')

  @overload(int, int)
  def appendFragments(self, pos: int, endPos: int) -> None:
    """
    Calls Qt's 'void QTextCopyHelper::appendFragments(int pos, int endPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcopyhelper.html#appendFragments

    Parameters
    ----------

    pos : int
      Passed on as it is.

    endPos : int
      Passed on as it is.
    """
    #  void QTextCopyHelper::appendFragments(int pos, int endPos)
    self.uglySide.call(
        'ritual_ZN15QTextCopyHelper15appendFragmentsEii', pos, endPos,
    )

  @overload(int, int)
  @overload(int, int, int)
  def appendFragment(
      self,
      pos: int,
      endPos: int,
      objectIndex: int = -1,
  ) -> int:
    """
    Calls Qt's 'int QTextCopyHelper::appendFragment(int pos, int endPos, int
    objectIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcopyhelper.html#appendFragment

    Parameters
    ----------

    pos : int
      Passed on as it is.

    endPos : int
      Passed on as it is.

    objectIndex : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QTextCopyHelper::appendFragment(int pos, int endPos, int
    #      objectIndex)
    return self.uglySide.call(
        'ritual_ZN15QTextCopyHelper14appendFragmentEiii',
        pos, endPos, objectIndex,
    )

  @overload(QTextFormat)
  @overload(QTextFormat, int)
  def convertFormatIndex(
      self,
      oldFormat: QTextFormat,
      objectIndexToSet: int = -1,
  ) -> int:
    """
    Calls Qt's 'int QTextCopyHelper::convertFormatIndex(const QTextFormat
    &oldFormat, int objectIndexToSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcopyhelper.html#convertFormatIndex

    Parameters
    ----------

    oldFormat : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.

    objectIndexToSet : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QTextCopyHelper::convertFormatIndex(const QTextFormat &oldFormat,
    #      int objectIndexToSet)
    return self.uglySide.call(
        'ritual_ZN15QTextCopyHelper18convertFormatIndexERK11QTextFormati',
        self._valueOf(oldFormat), objectIndexToSet,
    )

  @overload(int)
  @overload(int, int)
  def convertFormatIndex(
      self,
      oldFormatIndex: int,
      objectIndexToSet: int = -1,
  ) -> int:
    """
    Calls Qt's 'int QTextCopyHelper::convertFormatIndex(int oldFormatIndex,
    int objectIndexToSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextcopyhelper.html#convertFormatIndex

    Parameters
    ----------

    oldFormatIndex : int
      Passed on as it is.

    objectIndexToSet : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QTextCopyHelper::convertFormatIndex(int oldFormatIndex, int
    #      objectIndexToSet)
    return self.uglySide.call(
        'ritual_ZN15QTextCopyHelper18convertFormatIndexEii',
        oldFormatIndex, objectIndexToSet,
    )

  @overload(QTextFormat)
  def convertFormat(self, fmt: QTextFormat) -> QTextFormat:
    """
    Calls Qt's 'QTextFormat QTextCopyHelper::convertFormat(const QTextFormat
    &fmt)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextcopyhelper.html#convertFormat

    Parameters
    ----------

    fmt : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.

    Returns
    -------

    QTextFormat
      A new cute QTextFormat around the copy Qt gave back. Python owns it.
    """
    #  QTextFormat QTextCopyHelper::convertFormat(const QTextFormat &fmt)
    address = self.uglySide.call(
        'ritual_ZN15QTextCopyHelper13convertFormatERK11QTextFormat',
        self._valueOf(fmt),
    )
    from . import QTextFormat
    return QTextFormat._cuteOwning(address)
