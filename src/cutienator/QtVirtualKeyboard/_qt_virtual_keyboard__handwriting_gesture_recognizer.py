"""
QtVirtualKeyboard::HandwritingGestureRecognizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/handwritinggesturerecognizer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::HandwritingGestureRecognizer to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject
from . import QtVirtualKeyboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QVirtualKeyboardTrace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVirtualKeyboardTrace = WAIT['QVirtualKeyboardTrace']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class HandwritingGestureRecognizer(QtVirtualKeyboard.GestureRecognizer):
  """
  The cute side of Qt's QtVirtualKeyboard::HandwritingGestureRecognizer: a
  plain Python object standing in front of one C++
  QtVirtualKeyboard::HandwritingGestureRecognizer.

  It is built on the cute 'QtVirtualKeyboard::GestureRecognizer', as Qt's
  QtVirtualKeyboard::HandwritingGestureRecognizer is built on Qt's
  QtVirtualKeyboard::GestureRecognizer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::HandwritingGestureRecognizer that
  has a ritual and that Python can call so far, 5 names in all: 'metaObject',
  'tr', 'setDpi', 'dpi', 'recognize'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtVirtualKeyboard::HandwritingGestureRecognizer::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::HandwritingGestureRecognizer::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::HandwritingGestureRecognizer is created at the
    first use, not by 'QtVirtualKeyboard::HandwritingGestureRecognizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtVirtualKeyboard::HandwritingGestureRecognizer.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::HandwritingGestureRecognizer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString
    QtVirtualKeyboard::HandwritingGestureRecognizer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-handwritinggesturerecognizer.html

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
    #  QString QtVirtualKeyboard::HandwritingGestureRecognizer::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer2trEPKcS'
        '2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::HandwritingGestureRecognizer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtVirtualKeyboard::HandwritingGestureRecognizer::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-handwritinggesturerecognizer.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtVirtualKeyboard::HandwritingGestureRecognizer::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard28HandwritingGestureRecognizer10metaO'
        'bjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dpi(self) -> int:
    """
    Calls Qt's 'int QtVirtualKeyboard::HandwritingGestureRecognizer::dpi()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-handwritinggesturerecognizer.html
    """
    #  int QtVirtualKeyboard::HandwritingGestureRecognizer::dpi() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard28HandwritingGestureRecognizer3dpiEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDpi(self, dpi: int) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::HandwritingGestureRecognizer::setDpi(int dpi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-handwritinggesturerecognizer.html

    Parameters
    ----------

    dpi : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::HandwritingGestureRecognizer::setDpi(int dpi)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer6setDpiE'
        'i',
        dpi,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::HandwritingGestureRecognizer::
    HandwritingGestureRecognizer(QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-handwritinggesturerecognizer.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::HandwritingGestureRecognizer::
    #      HandwritingGestureRecognizer(QObject *parent)
    self._noteCreation(HandwritingGestureRecognizer, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizerC1EP7QOb'
        'ject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QList[QVirtualKeyboardTrace])
  def recognize(
      self,
      traceList: QList[QVirtualKeyboardTrace],
  ) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap
    QtVirtualKeyboard::HandwritingGestureRecognizer::recognize(const
    QList<QVirtualKeyboardTrace *> traceList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-handwritinggesturerecognizer.html

    Parameters
    ----------

    traceList : QList[QVirtualKeyboardTrace]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap
    #      QtVirtualKeyboard::HandwritingGestureRecognizer::recognize(const
    #      QList<QVirtualKeyboardTrace *> traceList)
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer9recogni'
        'zeE5QListIP21QVirtualKeyboardTraceE',
        self._valueOf(traceList),
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)
