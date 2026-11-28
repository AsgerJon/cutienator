"""
QKeySequencePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qkeysequence_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QKeySequencePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt
from . import QKeySequence

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QKeySequencePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QKeySequencePrivate: a plain Python object standing
  in front of one C++ QKeySequencePrivate.

  C++ hands a QKeySequencePrivate around as a copy, so every C++
  QKeySequencePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QKeySequencePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'keyName'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKeySequencePrivate::~QKeySequencePrivate()': the destructor:
    Python removes its C++ QKeySequencePrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QKeySequencePrivate is created at the first use, not by
    'QKeySequencePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QKeySequencePrivate back gives a copy the ritual made
    for Python, in a new cute QKeySequencePrivate.
  - Each name of Qt's QKeySequencePrivate that has no cute function yet,
    'decodeString', 'encodeString', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Qt.Key, QKeySequence.SequenceFormat)
  def keyName(key: Qt.Key, format: QKeySequence.SequenceFormat) -> str:
    """
    Calls Qt's 'QString QKeySequencePrivate::keyName(Qt::Key key,
    QKeySequence::SequenceFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceprivate.html#keyName

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    format : QKeySequence.SequenceFormat
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QKeySequencePrivate::keyName(Qt::Key key,
    #      QKeySequence::SequenceFormat format)
    return Rituals.call(
        'ritual_ZN19QKeySequencePrivate7keyNameEN2Qt3KeyEN12QKeySequence14S'
        'equenceFormatE',
        key.value, format.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeySequencePrivate'

  #  Qt's '~QKeySequencePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QKeySequencePrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QKeySequencePrivateD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QKeySequencePrivate::QKeySequencePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceprivate.html#QKeySequencePrivate
    """
    #  QKeySequencePrivate::QKeySequencePrivate()
    self._noteCreation(QKeySequencePrivate, lambda: Rituals.call(
        'ritual_ZN19QKeySequencePrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, copy: QKeySequencePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QKeySequencePrivate::QKeySequencePrivate(const QKeySequencePrivate
    &copy)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceprivate.html#QKeySequencePrivate

    Parameters
    ----------

    copy : QKeySequencePrivate
      Passed on as a value: Qt reads the C++ QKeySequencePrivate, which stays
      Python's own.
    """
    #  QKeySequencePrivate::QKeySequencePrivate(const QKeySequencePrivate
    #      &copy)
    self._noteCreation(QKeySequencePrivate, lambda: Rituals.call(
        'ritual_ZN19QKeySequencePrivateC1ERKS_', self._valueOf(copy),
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

  @staticmethod
  def decodeString(*__, **_) -> Never:
    """
    Qt's 'QKeyCombination QKeySequencePrivate::decodeString(QString accel,
    QKeySequence::SequenceFormat format)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'globalModifs'.
    """
    raise NotImplementedError(
        "'QKeySequencePrivate.decodeString' has no cute function yet. Qt's "
        "'QKeyCombination QKeySequencePrivate::decodeString(QString accel, "
        "QKeySequence::SequenceFormat format)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'globalModifs'.")

  @staticmethod
  def encodeString(*__, **_) -> Never:
    """
    Qt's 'QString QKeySequencePrivate::encodeString(QKeyCombination
    keyCombination, QKeySequence::SequenceFormat format)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'addKey'.
    """
    raise NotImplementedError(
        "'QKeySequencePrivate.encodeString' has no cute function yet. Qt's "
        "'QString QKeySequencePrivate::encodeString(QKeyCombination "
        "keyCombination, QKeySequence::SequenceFormat format)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'addKey'."
    )
