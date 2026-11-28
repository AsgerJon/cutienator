"""
QNdefNfcUriRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qndefnfcurirecord.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QNdefRecord

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QNdefNfcUriRecord(QNdefRecord):
  """
  The cute side of Qt's QNdefNfcUriRecord: a plain Python object standing in
  front of one C++ QNdefNfcUriRecord.

  It is built on the cute 'QNdefRecord', as Qt's QNdefNfcUriRecord is built
  on Qt's QNdefRecord, and has everything that class has.

  C++ hands a QNdefNfcUriRecord around as a copy, so every C++
  QNdefNfcUriRecord behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcUriRecord that has a ritual and that Python
  can call so far, 2 names in all: 'uri', 'setUri'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefNfcUriRecord::~QNdefNfcUriRecord()': the destructor: Python
    removes its C++ QNdefNfcUriRecord by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcUriRecord is created at the first use, not by
    'QNdefNfcUriRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcUriRecord back gives a copy the ritual made
    for Python, in a new cute QNdefNfcUriRecord.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcUriRecord'

  #  Qt's '~QNdefNfcUriRecord()'. Naming it makes this a value class: Python
  #  owns every C++ QNdefNfcUriRecord behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QNdefNfcUriRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def uri(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNdefNfcUriRecord::uri() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfcurirecord.html#uri

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNdefNfcUriRecord::uri() const
    address = self.uglySide.call('ritual_ZNK17QNdefNfcUriRecord3uriEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUri(self, uri: QUrl) -> None:
    """
    Calls Qt's 'void QNdefNfcUriRecord::setUri(const QUrl &uri)'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfcurirecord.html#setUri

    Parameters
    ----------

    uri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNdefNfcUriRecord::setUri(const QUrl &uri)
    self.uglySide.call(
        'ritual_ZN17QNdefNfcUriRecord6setUriERK4QUrl', self._valueOf(uri),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QNdefNfcUriRecord::QNdefNfcUriRecord()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcurirecord.html#QNdefNfcUriRecord
    """
    #  QNdefNfcUriRecord::QNdefNfcUriRecord()
    self._noteCreation(QNdefNfcUriRecord, lambda: Rituals.call(
        'ritual_ZN17QNdefNfcUriRecordC1Ev',
    ))

  @overload(QNdefRecord)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcUriRecord::QNdefNfcUriRecord(const QNdefRecord &other)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcurirecord.html#QNdefNfcUriRecord

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefNfcUriRecord::QNdefNfcUriRecord(const QNdefRecord &other)
    self._noteCreation(QNdefNfcUriRecord, lambda: Rituals.call(
        'ritual_ZN17QNdefNfcUriRecordC1ERK11QNdefRecord',
        self._valueOf(other),
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
