"""
QSSGIblBaker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DIblBaker/6.12.0/QtQuick3DIblBaker/private/qssgiblbaker_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSSGIblBaker to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGIblBaker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGIblBaker: a plain Python object standing in front
  of one C++ QSSGIblBaker.

  C++ hands a QSSGIblBaker around as a copy, so every C++ QSSGIblBaker behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGIblBaker that has a ritual and that Python can
  call so far, 2 names in all: 'inputExtensions', 'outputExtension'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QString QSSGIblBaker::import(const QString &sourceFile, const
    QDir &savePath, QStringList *generatedFiles)': names 'QStringList', which
    has no cute class yet.
  - Qt's 'QSSGIblBaker::~QSSGIblBaker()': the destructor: Python removes its
    C++ QSSGIblBaker by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QSSGIblBaker is created at the first use, not by
    'QSSGIblBaker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGIblBaker back gives a copy the ritual made for
    Python, in a new cute QSSGIblBaker.
  - Each name of Qt's QSSGIblBaker that has no cute function yet, 'import_',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGIblBaker'

  #  Qt's '~QSSGIblBaker()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGIblBaker behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QSSGIblBakerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def inputExtensions(self) -> QStringList:
    """
    Calls Qt's 'const QStringList QSSGIblBaker::inputExtensions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgiblbaker.html#inputExtensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList QSSGIblBaker::inputExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK12QSSGIblBaker15inputExtensionsEv',
    )
    return QStringList._cuteOwning(address)

  def outputExtension(self) -> str:
    """
    Calls Qt's 'const QString QSSGIblBaker::outputExtension() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgiblbaker.html#outputExtension

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSSGIblBaker::outputExtension() const
    return self.uglySide.call('ritual_ZNK12QSSGIblBaker15outputExtensionEv')

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

  @staticmethod
  def import_(*__, **_) -> Never:
    """
    Qt's 'const QString QSSGIblBaker::import(const QString &sourceFile, const
    QDir &savePath, QStringList *generatedFiles)': names 'QStringList', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGIblBaker.import_' has no cute function yet. Qt's 'const "
        "QString QSSGIblBaker::import(const QString &sourceFile, const QDir "
        "&savePath, QStringList *generatedFiles)': names 'QStringList', "
        "which has no cute class yet.")
