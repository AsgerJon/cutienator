"""
QAccessibilityHints binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessibilityhints.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QAccessibilityHintsPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibilityHints(QObject):
  """
  The cute side of Qt's QAccessibilityHints: a plain Python object standing
  in front of one C++ QAccessibilityHints.

  It is built on the cute 'QObject', as Qt's QAccessibilityHints is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibilityHints that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'contrastPreference', 'motionPreference', 'contrastPreferenceChanged',
  'motionPreferenceChanged', 'event'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAccessibilityHints::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAccessibilityHints::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QAccessibilityHintsPrivate *QAccessibilityHints::d_func()
    const': takes in Python what 'QAccessibilityHintsPrivate
    *QAccessibilityHints::d_func()' takes.
  - Qt's 'QAccessibilityHints::~QAccessibilityHints()': the destructor:
    Python never removes a C++ QAccessibilityHints.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAccessibilityHints is created at the first use, not by
    'QAccessibilityHints(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibilityHints.
  - Qt tells when it has removed the C++ QAccessibilityHints. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QAccessibilityHints::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibilityhints.html#tr

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
    #  QString QAccessibilityHints::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QAccessibilityHints2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibilityHints'

  #  A C++ QAccessibilityHints Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibilityHints'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAccessibilityHints::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhints.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAccessibilityHints::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QAccessibilityHints10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def contrastPreference(self) -> Qt.ContrastPreference:
    """
    Calls Qt's 'Qt::ContrastPreference
    QAccessibilityHints::contrastPreference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhints.html#contrastPreference

    Returns
    -------

    Qt.ContrastPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ContrastPreference(number)' gives.
    """
    #  Qt::ContrastPreference QAccessibilityHints::contrastPreference() const
    return Qt.ContrastPreference(self.uglySide.call(
        'ritual_ZNK19QAccessibilityHints18contrastPreferenceEv',
    ))

  def motionPreference(self) -> Qt.MotionPreference:
    """
    Calls Qt's 'Qt::MotionPreference QAccessibilityHints::motionPreference()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhints.html#motionPreference

    Returns
    -------

    Qt.MotionPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MotionPreference(number)' gives.
    """
    #  Qt::MotionPreference QAccessibilityHints::motionPreference() const
    return Qt.MotionPreference(self.uglySide.call(
        'ritual_ZNK19QAccessibilityHints16motionPreferenceEv',
    ))

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibilityHints::QAccessibilityHints(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhints.html#QAccessibilityHints

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAccessibilityHints::QAccessibilityHints(QObject *parent)
    self._noteCreation(QAccessibilityHints, lambda: Rituals.call(
        'ritual_ZN19QAccessibilityHintsC1EP7QObject',
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

  def d_func(self) -> Optional[QAccessibilityHintsPrivate]:
    """
    Calls Qt's 'QAccessibilityHintsPrivate *QAccessibilityHints::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibilityhints.html#d_func

    Returns
    -------

    Optional[QAccessibilityHintsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibilityHintsPrivate *QAccessibilityHints::d_func()
    address = self.uglySide.call('ritual_ZN19QAccessibilityHints6d_funcEv')
    from . import QAccessibilityHintsPrivate
    return QAccessibilityHintsPrivate._cuteAt(address)

  @overload(Qt.ContrastPreference)
  def contrastPreferenceChanged(
      self,
      contrastPreference: Qt.ContrastPreference,
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibilityHints::contrastPreferenceChanged(Qt::ContrastPreference
    contrastPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhints.html#contrastPreferenceChanged

    Parameters
    ----------

    contrastPreference : Qt.ContrastPreference
      Passed on as its number.
    """
    #  void QAccessibilityHints::contrastPreferenceChanged(Qt::
    #      ContrastPreference contrastPreference)
    self.uglySide.call(
        'ritual_ZN19QAccessibilityHints25contrastPreferenceChangedEN2Qt18Co'
        'ntrastPreferenceE',
        contrastPreference.value,
    )

  @overload(Qt.MotionPreference)
  def motionPreferenceChanged(
      self,
      motionPreference: Qt.MotionPreference,
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibilityHints::motionPreferenceChanged(Qt::MotionPreference
    motionPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhints.html#motionPreferenceChanged

    Parameters
    ----------

    motionPreference : Qt.MotionPreference
      Passed on as its number.
    """
    #  void QAccessibilityHints::motionPreferenceChanged(Qt::MotionPreference
    #      motionPreference)
    self.uglySide.call(
        'ritual_ZN19QAccessibilityHints23motionPreferenceChangedEN2Qt16Moti'
        'onPreferenceE',
        motionPreference.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAccessibilityHints::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibilityhints.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibilityHints::event(QEvent *event)
    ritual = 'ritual_ZN19QAccessibilityHints5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAccessibilityHints5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))
