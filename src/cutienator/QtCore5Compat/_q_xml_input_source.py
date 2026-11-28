"""
QXmlInputSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QChar, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlInputSource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlInputSource: a plain Python object standing in
  front of one C++ QXmlInputSource.

  C++ hands a QXmlInputSource around as a copy, so every C++ QXmlInputSource
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QXmlInputSource that has a ritual and that Python
  can call so far, 7 names in all: 'setData', 'fetchData', 'data', 'next',
  'reset', 'fromRawData', 'init'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlInputSource::~QXmlInputSource()': the destructor: Python
    removes its C++ QXmlInputSource by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QXmlInputSource is created at the first use, not by
    'QXmlInputSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlInputSource back gives a copy the ritual made for
    Python, in a new cute QXmlInputSource.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlInputSource'

  #  A C++ QXmlInputSource Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlInputSource'

  #  The functions Qt calls itself that QXmlInputSource is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setData': (
          ('_ZN15QXmlInputSource7setDataERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
          ('_ZN15QXmlInputSource7setDataERK10QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'fetchData': (
          ('_ZN15QXmlInputSource9fetchDataEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'data': (
          ('_ZNK15QXmlInputSource4dataEv',
           ('address', 'text', ''),
           ()),
      ),
      'next': (
          ('_ZN15QXmlInputSource4nextEv',
           ('address', 'value', 'QtCore:QChar'),
           ()),
      ),
      'reset': (
          ('_ZN15QXmlInputSource5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'fromRawData': (
          ('_ZN15QXmlInputSource11fromRawDataERK10QByteArrayb',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('bool', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QXmlInputSource()'. Naming it makes this a value class: Python
  #  owns every C++ QXmlInputSource behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QXmlInputSourceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def data(self) -> str:
    """
    Calls Qt's 'QString QXmlInputSource::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#data

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlInputSource::data() const
    ritual = 'ritual_ZNK15QXmlInputSource4dataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QXmlInputSource4dataEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setData(self, dat: str) -> None:
    """
    Calls Qt's 'void QXmlInputSource::setData(const QString &dat)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#setData

    Parameters
    ----------

    dat : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlInputSource::setData(const QString &dat)
    ritual = 'ritual_ZN15QXmlInputSource7setDataERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QXmlInputSource7setDataERK7QString'
    self.uglySide.call(ritual, dat)

  @overload(QByteArray)
  def setData(self, dat: QByteArray) -> None:
    """
    Calls Qt's 'void QXmlInputSource::setData(const QByteArray &dat)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#setData

    Parameters
    ----------

    dat : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QXmlInputSource::setData(const QByteArray &dat)
    ritual = 'ritual_ZN15QXmlInputSource7setDataERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QXmlInputSource7setDataERK10QByteArray'
    self.uglySide.call(ritual, self._valueOf(dat))

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
    Notes what was given, for Qt's 'QXmlInputSource::QXmlInputSource()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlinputsource.html#QXmlInputSource
    """
    #  QXmlInputSource::QXmlInputSource()
    self._noteCreation(QXmlInputSource, lambda: Rituals.call(
        'ritual_ZN15QXmlInputSourceC1Ev',
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, dev: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's
    'QXmlInputSource::QXmlInputSource(QIODevice *dev)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlinputsource.html#QXmlInputSource

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXmlInputSource::QXmlInputSource(QIODevice *dev)
    self._noteCreation(QXmlInputSource, lambda: Rituals.call(
        'ritual_ZN15QXmlInputSourceC1EP9QIODevice', self._addressOf(dev),
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

  def fetchData(self) -> None:
    """
    Calls Qt's 'void QXmlInputSource::fetchData()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#fetchData
    """
    #  void QXmlInputSource::fetchData()
    ritual = 'ritual_ZN15QXmlInputSource9fetchDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QXmlInputSource9fetchDataEv'
    self.uglySide.call(ritual)

  def next(self) -> QChar:
    """
    Calls Qt's 'QChar QXmlInputSource::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#next

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QXmlInputSource::next()
    ritual = 'ritual_ZN15QXmlInputSource4nextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QXmlInputSource4nextEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QXmlInputSource::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#reset
    """
    #  void QXmlInputSource::reset()
    ritual = 'ritual_ZN15QXmlInputSource5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QXmlInputSource5resetEv'
    self.uglySide.call(ritual)

  @overload(QByteArray)
  @overload(QByteArray, bool)
  def fromRawData(self, data: QByteArray, beginning: bool = False) -> str:
    """
    Calls Qt's 'QString QXmlInputSource::fromRawData(const QByteArray &data,
    bool beginning)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#fromRawData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    beginning : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlInputSource::fromRawData(const QByteArray &data, bool
    #      beginning)
    ritual = 'ritual_ZN15QXmlInputSource11fromRawDataERK10QByteArrayb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QXmlInputSource11fromRawDataERK10QByteArrayb'
    return self.uglySide.call(ritual, self._valueOf(data), beginning)

  def init(self) -> None:
    """
    Calls Qt's 'void QXmlInputSource::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlinputsource.html#init
    """
    #  void QXmlInputSource::init()
    self.uglySide.call('ritual_ZN15QXmlInputSource4initEv')
