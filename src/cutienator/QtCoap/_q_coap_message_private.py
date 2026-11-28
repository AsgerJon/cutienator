"""
QCoapMessagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapmessage_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoapMessagePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData
from . import QCoapMessage, QCoapOption

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QCoapMessagePrivate(QSharedData):
  """
  The cute side of Qt's QCoapMessagePrivate: a plain Python object standing
  in front of one C++ QCoapMessagePrivate.

  It is built on the cute 'QSharedData', as Qt's QCoapMessagePrivate is built
  on Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapMessagePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'clone'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapMessagePrivate::~QCoapMessagePrivate()': the destructor:
    Python never removes a C++ QCoapMessagePrivate.
  - Qt's 'QList<QCoapOption>::const_iterator
    QCoapMessagePrivate::findOption(QCoapOption::OptionName name) const':
    gives a type Python has no way to take yet.
  - Qt's 'QCoapMessagePrivate::QCoapMessagePrivate(const QCoapMessagePrivate
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCoapMessagePrivate is created at the first use, not by
    'QCoapMessagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapMessagePrivate.
  - Each name of Qt's QCoapMessagePrivate that has no cute function yet,
    'findOption', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QCoapMessagePrivate'

  #  A C++ QCoapMessagePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapMessagePrivate'

  #  The functions Qt calls itself that QCoapMessagePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clone': (
          ('_ZNK19QCoapMessagePrivate5cloneEv',
           ('address', 'address', 'QtCoap:QCoapMessagePrivate'),
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

  def clone(self) -> Optional[QCoapMessagePrivate]:
    """
    Calls Qt's 'QCoapMessagePrivate *QCoapMessagePrivate::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessageprivate.html#clone

    Returns
    -------

    Optional[QCoapMessagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapMessagePrivate *QCoapMessagePrivate::clone() const
    ritual = 'ritual_ZNK19QCoapMessagePrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QCoapMessagePrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QCoapMessagePrivate._cuteAt(address)

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
  @overload(QCoapMessage.Type)
  def __init__(
      self,
      type: QCoapMessage.Type = QCoapMessage.Type.NonConfirmable,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCoapMessagePrivate::QCoapMessagePrivate(QCoapMessage::Type type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapmessageprivate.html#QCoapMessagePrivate

    Parameters
    ----------

    type : QCoapMessage.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QCoapMessage.Type.NonConfirmable.
    """
    #  QCoapMessagePrivate::QCoapMessagePrivate(QCoapMessage::Type type)
    self._noteCreation(QCoapMessagePrivate, lambda: Rituals.call(
        'ritual_ZN19QCoapMessagePrivateC1EN12QCoapMessage4TypeE', type.value,
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
  def findOption(*__, **_) -> Never:
    """
    Qt's 'QList<QCoapOption>::const_iterator
    QCoapMessagePrivate::findOption(QCoapOption::OptionName name) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCoapMessagePrivate.findOption' has no cute function yet. Qt's "
        "'QList<QCoapOption>::const_iterator "
        "QCoapMessagePrivate::findOption(QCoapOption::OptionName name) "
        "const': gives a type Python has no way to take yet.")
