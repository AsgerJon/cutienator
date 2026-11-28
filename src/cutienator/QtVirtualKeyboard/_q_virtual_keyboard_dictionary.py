"""
QVirtualKeyboardDictionary binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/qvirtualkeyboarddictionary.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardDictionary(QObject):
  """
  The cute side of Qt's QVirtualKeyboardDictionary: a plain Python object
  standing in front of one C++ QVirtualKeyboardDictionary.

  It is built on the cute 'QObject', as Qt's QVirtualKeyboardDictionary is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardDictionary that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr', 'name',
  'contents', 'setContents', 'resetContents', 'contentsChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardDictionary::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QVirtualKeyboardDictionary::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVirtualKeyboardDictionary is created at the first use, not by
    'QVirtualKeyboardDictionary(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardDictionary.
  - Qt tells when it has removed the C++ QVirtualKeyboardDictionary. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QVirtualKeyboardDictionary::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html#tr

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
    #  QString QVirtualKeyboardDictionary::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QVirtualKeyboardDictionary2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardDictionary'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVirtualKeyboardDictionary::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardDictionary::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QVirtualKeyboardDictionary10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QVirtualKeyboardDictionary::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVirtualKeyboardDictionary::name() const
    return self.uglySide.call(
        'ritual_ZNK26QVirtualKeyboardDictionary4nameEv',
    )

  def contents(self) -> QStringList:
    """
    Calls Qt's 'QStringList QVirtualKeyboardDictionary::contents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html#contents

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QVirtualKeyboardDictionary::contents() const
    address = self.uglySide.call(
        'ritual_ZNK26QVirtualKeyboardDictionary8contentsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setContents(self, contents: QStringList) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardDictionary::setContents(const
    QStringList &contents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html#setContents

    Parameters
    ----------

    contents : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVirtualKeyboardDictionary::setContents(const QStringList
    #      &contents)
    self.uglySide.call(
        'ritual_ZN26QVirtualKeyboardDictionary11setContentsERK5QListI7QStri'
        'ngE',
        self._valueOf(contents),
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

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, name: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QVirtualKeyboardDictionary::QVirtualKeyboardDictionary(const QString
    &name, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVirtualKeyboardDictionary::QVirtualKeyboardDictionary(const QString
    #      &name, QObject *parent)
    self._noteCreation(QVirtualKeyboardDictionary, lambda: Rituals.call(
        'ritual_ZN26QVirtualKeyboardDictionaryC1ERK7QStringP7QObject',
        name, self._addressOf(parent, 'QObject'),
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

  def resetContents(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardDictionary::resetContents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html#resetContents
    """
    #  void QVirtualKeyboardDictionary::resetContents()
    self.uglySide.call(
        'ritual_ZN26QVirtualKeyboardDictionary13resetContentsEv',
    )

  def contentsChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardDictionary::contentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionary.html#contentsChanged
    """
    #  void QVirtualKeyboardDictionary::contentsChanged()
    self.uglySide.call(
        'ritual_ZN26QVirtualKeyboardDictionary15contentsChangedEv',
    )
