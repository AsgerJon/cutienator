"""
QVoicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTextToSpeech/6.12.0/QtTextToSpeech/private/qvoice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QVoicePrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QVoice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QLocale, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QVariant = WAIT['QVariant']


class QVoicePrivate(QSharedData):
  """
  The cute side of Qt's QVoicePrivate: a plain Python object standing in
  front of one C++ QVoicePrivate.

  It is built on the cute 'QSharedData', as Qt's QVoicePrivate is built on
  Qt's QSharedData, and has everything that class has.

  C++ hands a QVoicePrivate around as a copy, so every C++ QVoicePrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QVoicePrivate yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVoicePrivate::~QVoicePrivate()': the destructor: Python removes
    its C++ QVoicePrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QVoicePrivate is created at the first use, not by
    'QVoicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVoicePrivate back gives a copy the ritual made for
    Python, in a new cute QVoicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVoicePrivate'

  #  Qt's '~QVoicePrivate()'. Naming it makes this a value class: Python owns
  #  every C++ QVoicePrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QVoicePrivateD1Ev'

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
    Notes what was given, for Qt's 'QVoicePrivate::QVoicePrivate()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvoiceprivate.html#QVoicePrivate
    """
    #  QVoicePrivate::QVoicePrivate()
    self._noteCreation(QVoicePrivate, lambda: Rituals.call(
        'ritual_ZN13QVoicePrivateC1Ev',
    ))

  @overload(str, QLocale, QVoice.Gender, QVoice.Age, QVariant)
  def __init__(
      self,
      n: str,
      l: QLocale,
      g: QVoice.Gender,
      a: QVoice.Age,
      d: QVariant,
  ) -> None:
    """
    Notes what was given, for Qt's 'QVoicePrivate::QVoicePrivate(const
    QString &n, const QLocale &l, QVoice::Gender g, QVoice::Age a, const
    QVariant &d)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvoiceprivate.html#QVoicePrivate

    Parameters
    ----------

    n : str
      Passed on as it is: a QString is made of it for the call.

    l : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    g : QVoice.Gender
      Passed on as its number.

    a : QVoice.Age
      Passed on as its number.

    d : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QVoicePrivate::QVoicePrivate(const QString &n, const QLocale &l,
    #      QVoice::Gender g, QVoice::Age a, const QVariant &d)
    self._noteCreation(QVoicePrivate, lambda: Rituals.call(
        'ritual_ZN13QVoicePrivateC1ERK7QStringRK7QLocaleN6QVoice6GenderENS6'
        '_3AgeERK8QVariant',
        n, self._valueOf(l), g.value, a.value, self._valueOf(d),
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
