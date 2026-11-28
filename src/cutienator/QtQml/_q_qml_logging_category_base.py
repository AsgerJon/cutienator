"""
QQmlLoggingCategoryBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlloggingcategorybase_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlLoggingCategoryBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLoggingCategory, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlLoggingCategoryBase(QObject):
  """
  The cute side of Qt's QQmlLoggingCategoryBase: a plain Python object
  standing in front of one C++ QQmlLoggingCategoryBase.

  It is built on the cute 'QObject', as Qt's QQmlLoggingCategoryBase is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlLoggingCategoryBase that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'category',
  'forceCompletion'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlLoggingCategoryBase::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlLoggingCategoryBase::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlLoggingCategoryBase::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.
  - Qt's 'void QQmlLoggingCategoryBase::setCategory(const char *name,
    QtMsgType type)': names the enum 'QtMsgType', whose class cannot be named
    here.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QQmlLoggingCategoryBase is created at the first use, not by
    'QQmlLoggingCategoryBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlLoggingCategoryBase.
  - Qt tells when it has removed the C++ QQmlLoggingCategoryBase. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlLoggingCategoryBase that has no cute function yet,
    '__init__', 'setCategory', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQmlLoggingCategoryBase::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlloggingcategorybase.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLoggingCategoryBase::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQmlLoggingCategoryBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlLoggingCategoryBase'

  #  The functions Qt calls itself that QQmlLoggingCategoryBase is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'forceCompletion': (
          ('_ZN23QQmlLoggingCategoryBase15forceCompletionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlLoggingCategoryBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategorybase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlLoggingCategoryBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlLoggingCategoryBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QQmlLoggingCategoryBase::QQmlLoggingCategoryBase(QObject *parent)':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlLoggingCategoryBase.__init__' has no cute function yet. Qt's "
        "'QQmlLoggingCategoryBase::QQmlLoggingCategoryBase(QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  def category(self) -> Optional[QLoggingCategory]:
    """
    Calls Qt's 'const QLoggingCategory *QQmlLoggingCategoryBase::category()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategorybase.html#category

    Returns
    -------

    Optional[QLoggingCategory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QLoggingCategory *QQmlLoggingCategoryBase::category()
    address = self.uglySide.call(
        'ritual_ZN23QQmlLoggingCategoryBase8categoryEv',
    )
    from ..QtCore import QLoggingCategory
    return QLoggingCategory._cuteAt(address)

  def forceCompletion(self) -> None:
    """
    Calls Qt's 'void QQmlLoggingCategoryBase::forceCompletion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategorybase.html#forceCompletion
    """
    #  void QQmlLoggingCategoryBase::forceCompletion()
    self.uglySide.call(
        'ritual_ZN23QQmlLoggingCategoryBase15forceCompletionEv',
    )

  @staticmethod
  def setCategory(*__, **_) -> Never:
    """
    Qt's 'void QQmlLoggingCategoryBase::setCategory(const char *name,
    QtMsgType type)': names the enum 'QtMsgType', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQmlLoggingCategoryBase.setCategory' has no cute function yet. "
        "Qt's 'void QQmlLoggingCategoryBase::setCategory(const char *name, "
        "QtMsgType type)': names the enum 'QtMsgType', whose class cannot "
        "be named here.")
