"""
QQmlFileSelectorInterceptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlfileselector_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlFileSelectorInterceptor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlAbstractUrlInterceptor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
  from . import QQmlFileSelectorPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlFileSelectorPrivate = WAIT['QQmlFileSelectorPrivate']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlFileSelectorInterceptor(QQmlAbstractUrlInterceptor):
  """
  The cute side of Qt's QQmlFileSelectorInterceptor: a plain Python object
  standing in front of one C++ QQmlFileSelectorInterceptor.

  It is built on the cute 'QQmlAbstractUrlInterceptor', as Qt's
  QQmlFileSelectorInterceptor is built on Qt's QQmlAbstractUrlInterceptor,
  and has everything that class has.

  C++ hands a QQmlFileSelectorInterceptor around as a copy, so every C++
  QQmlFileSelectorInterceptor behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlFileSelectorInterceptor that has a ritual and
  that Python can call so far, 1 name in all: 'intercept'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlFileSelectorInterceptor::~QQmlFileSelectorInterceptor()': the
    destructor: Python removes its C++ QQmlFileSelectorInterceptor by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlFileSelectorInterceptor is created at the first use, not by
    'QQmlFileSelectorInterceptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlFileSelectorInterceptor back gives a copy the
    ritual made for Python, in a new cute QQmlFileSelectorInterceptor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFileSelectorInterceptor'

  #  A C++ QQmlFileSelectorInterceptor Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlFileSelectorInterceptor'

  #  Qt's '~QQmlFileSelectorInterceptor()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlFileSelectorInterceptor behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QQmlFileSelectorInterceptorD1Ev'

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

  @overload(QQmlFileSelectorPrivate)
  @overload(NoneType)
  def __init__(self, pd: Optional[QQmlFileSelectorPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlFileSelectorInterceptor::QQmlFileSelectorInterceptor(
    QQmlFileSelectorPrivate *pd)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfileselectorinterceptor.html

    Parameters
    ----------

    pd : Optional[QQmlFileSelectorPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlFileSelectorInterceptor::QQmlFileSelectorInterceptor(
    #      QQmlFileSelectorPrivate *pd)
    self._noteCreation(QQmlFileSelectorInterceptor, lambda: Rituals.call(
        'ritual_ZN27QQmlFileSelectorInterceptorC1EP23QQmlFileSelectorPrivat'
        'e',
        self._addressOf(pd),
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

  @overload(QUrl, QQmlAbstractUrlInterceptor.DataType)
  def intercept(
      self,
      path: QUrl,
      type: QQmlAbstractUrlInterceptor.DataType,
  ) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlFileSelectorInterceptor::intercept(const QUrl &path,
    DataType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfileselectorinterceptor.html#intercept

    Parameters
    ----------

    path : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : QQmlAbstractUrlInterceptor.DataType
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlFileSelectorInterceptor::intercept(const QUrl &path, DataType
    #      type)
    ritual = (
        'ritual_ZN27QQmlFileSelectorInterceptor9interceptERK4QUrlN26QQmlAbs'
        'tractUrlInterceptor8DataTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQmlFileSelectorInterceptor9interceptERK4QUrlN26Q'
          'QmlAbstractUrlInterceptor8DataTypeE')
    address = self.uglySide.call(ritual, self._valueOf(path), type.value)
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)
