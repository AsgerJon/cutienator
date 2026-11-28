"""
QQmlXmlListModelQueryRunnable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlXmlListModelQueryRunnable to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QRunnable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlXmlListModelQueryResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlXmlListModelQueryResult = WAIT['QQmlXmlListModelQueryResult']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlXmlListModelQueryRunnable(QRunnable):
  """
  The cute side of Qt's QQmlXmlListModelQueryRunnable: a plain Python object
  standing in front of one C++ QQmlXmlListModelQueryRunnable.

  It is built on the cute 'QRunnable', as Qt's QQmlXmlListModelQueryRunnable
  is built on Qt's QRunnable, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlXmlListModelQueryRunnable that has a ritual and
  that Python can call so far, 2 names in all: 'run', 'doQueryJob'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlXmlListModelQueryRunnable::QQmlXmlListModelQueryRunnable(
    QQmlXmlListModelQueryJob &&job)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QFuture<QQmlXmlListModelQueryResult>
    QQmlXmlListModelQueryRunnable::future() const': gives a type Python has
    no way to take yet.
  - Qt's 'void
    QQmlXmlListModelQueryRunnable::processElement(QQmlXmlListModelQueryResult
    *currentResult, const QString &element, QXmlStreamReader &reader)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlXmlListModelQueryRunnable is created at the first use, not by
    'QQmlXmlListModelQueryRunnable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlXmlListModelQueryRunnable.
  - Each name of Qt's QQmlXmlListModelQueryRunnable that has no cute function
    yet, '__init__', 'future', 'processElement', 'readSubTree', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlXmlListModelQueryRunnable'

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
    Qt's 'QQmlXmlListModelQueryRunnable::QQmlXmlListModelQueryRunnable(
    QQmlXmlListModelQueryJob &&job)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlXmlListModelQueryRunnable.__init__' has no cute function yet. "
        "Qt's "
        "'QQmlXmlListModelQueryRunnable::QQmlXmlListModelQueryRunnable(QQmlX"
        "mlListModelQueryJob &&job)': takes a type Python has no way to "
        "hand over yet.")

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

  def run(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModelQueryRunnable::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelqueryrunnable.html#run
    """
    #  void QQmlXmlListModelQueryRunnable::run()
    ritual = 'ritual_ZN29QQmlXmlListModelQueryRunnable3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QQmlXmlListModelQueryRunnable3runEv'
    self.uglySide.call(ritual)

  @overload(QQmlXmlListModelQueryResult)
  @overload(NoneType)
  def doQueryJob(
      self,
      currentResult: Optional[QQmlXmlListModelQueryResult],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlXmlListModelQueryRunnable::doQueryJob(QQmlXmlListModelQueryResult
    *currentResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodelqueryrunnable.html#doQueryJob

    Parameters
    ----------

    currentResult : Optional[QQmlXmlListModelQueryResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlXmlListModelQueryRunnable::doQueryJob(
    #      QQmlXmlListModelQueryResult *currentResult)
    self.uglySide.call(
        'ritual_ZN29QQmlXmlListModelQueryRunnable10doQueryJobEP27QQmlXmlLis'
        'tModelQueryResult',
        self._addressOf(currentResult),
    )

  @staticmethod
  def future(*__, **_) -> Never:
    """
    Qt's 'QFuture<QQmlXmlListModelQueryResult>
    QQmlXmlListModelQueryRunnable::future() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlXmlListModelQueryRunnable.future' has no cute function yet. "
        "Qt's 'QFuture<QQmlXmlListModelQueryResult> "
        "QQmlXmlListModelQueryRunnable::future() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def processElement(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlXmlListModelQueryRunnable::processElement(QQmlXmlListModelQueryResult
    *currentResult, const QString &element, QXmlStreamReader &reader)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlXmlListModelQueryRunnable.processElement' has no cute "
        "function yet. Qt's 'void "
        "QQmlXmlListModelQueryRunnable::processElement(QQmlXmlListModelQuery"
        "Result *currentResult, const QString &element, QXmlStreamReader "
        "&reader)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def readSubTree(*__, **_) -> Never:
    """
    Qt's 'void QQmlXmlListModelQueryRunnable::readSubTree(const QString
    &prefix, QXmlStreamReader &reader, QFlatMap<int, QString> &results,
    QList<std::pair<void *, QString>> *errors)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'findIndexOfName'.
    """
    raise NotImplementedError(
        "'QQmlXmlListModelQueryRunnable.readSubTree' has no cute function "
        "yet. Qt's 'void QQmlXmlListModelQueryRunnable::readSubTree(const "
        "QString &prefix, QXmlStreamReader &reader, QFlatMap<int, QString> "
        "&results, QList<std::pair<void *, QString>> *errors)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'findIndexOfName'.")
