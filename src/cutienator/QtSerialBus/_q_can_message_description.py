"""
QCanMessageDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanmessagedescription.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
  from . import QCanSignalDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanSignalDescription = WAIT['QCanSignalDescription']
  QDebug = WAIT['QDebug']


class QCanMessageDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanMessageDescription: a plain Python object
  standing in front of one C++ QCanMessageDescription.

  C++ hands a QCanMessageDescription around as a copy, so every C++
  QCanMessageDescription behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanMessageDescription that has a ritual and that
  Python can call so far, 16 names in all: 'isValid', 'name', 'setName',
  'size', 'setSize', 'transmitter', 'setTransmitter', 'comment',
  'setComment', 'signalDescriptions', 'signalDescriptionForName',
  'clearSignalDescriptions', 'addSignalDescription', 'setSignalDescriptions',
  '__rlshift__', 'debugStreaming'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QCanMessageDescription::QCanMessageDescription(QCanMessageDescription
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanMessageDescription::~QCanMessageDescription()': the destructor:
    Python removes its C++ QCanMessageDescription by it, and has no other use
    for it.
  - Qt's 'QCanMessageDescription &QCanMessageDescription::operator=(const
    QCanMessageDescription &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QCanMessageDescription
    &QCanMessageDescription::operator=(QCanMessageDescription &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCanMessageDescription::swap(QCanMessageDescription &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QtCanBus::UniqueId QCanMessageDescription::uniqueId() const': gives
    the enum 'QtCanBus::UniqueId', whose class cannot be named here.
  - Qt's 'void QCanMessageDescription::setUniqueId(QtCanBus::UniqueId id)':
    names the enum 'QtCanBus::UniqueId', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QCanMessageDescription is created at the first use, not by
    'QCanMessageDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanMessageDescription back gives a copy the ritual
    made for Python, in a new cute QCanMessageDescription.
  - Each name of Qt's QCanMessageDescription that has no cute function yet,
    'setUniqueId', 'swap', 'uniqueId', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDebug, THIS)
  def debugStreaming(dbg: QDebug, msg: QCanMessageDescription) -> QDebug:
    """
    Calls Qt's 'QDebug QCanMessageDescription::debugStreaming(QDebug dbg,
    const QCanMessageDescription &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#debugStreaming

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    msg : QCanMessageDescription
      Passed on as a value: Qt reads the C++ QCanMessageDescription, which
      stays Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QCanMessageDescription::debugStreaming(QDebug dbg, const
    #      QCanMessageDescription &msg)
    address = Rituals.call(
        'ritual_ZN22QCanMessageDescription14debugStreamingE6QDebugRKS_',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(msg),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanMessageDescription'

  #  Qt's '~QCanMessageDescription()'. Naming it makes this a value class:
  #  Python owns every C++ QCanMessageDescription behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QCanMessageDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCanMessageDescription::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#isValid
    """
    #  bool QCanMessageDescription::isValid() const
    return self.uglySide.call('ritual_ZNK22QCanMessageDescription7isValidEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QCanMessageDescription::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanmessagedescription.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanMessageDescription::name() const
    return self.uglySide.call('ritual_ZNK22QCanMessageDescription4nameEv')

  def size(self) -> int:
    """
    Calls Qt's 'quint8 QCanMessageDescription::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanmessagedescription.html#size
    """
    #  quint8 QCanMessageDescription::size() const
    return self.uglySide.call('ritual_ZNK22QCanMessageDescription4sizeEv')

  def transmitter(self) -> str:
    """
    Calls Qt's 'QString QCanMessageDescription::transmitter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#transmitter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanMessageDescription::transmitter() const
    return self.uglySide.call(
        'ritual_ZNK22QCanMessageDescription11transmitterEv',
    )

  def comment(self) -> str:
    """
    Calls Qt's 'QString QCanMessageDescription::comment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#comment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanMessageDescription::comment() const
    return self.uglySide.call('ritual_ZNK22QCanMessageDescription7commentEv')

  def signalDescriptions(self) -> QList[QCanSignalDescription]:
    """
    Calls Qt's 'QList<QCanSignalDescription>
    QCanMessageDescription::signalDescriptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#signalDescriptions

    Returns
    -------

    QList[QCanSignalDescription]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanSignalDescription>
    #      QCanMessageDescription::signalDescriptions() const
    address = self.uglySide.call(
        'ritual_ZNK22QCanMessageDescription18signalDescriptionsEv',
    )
    from . import QCanSignalDescription
    return QList[QCanSignalDescription]._cuteOwning(address)

  @overload(str)
  def signalDescriptionForName(self, name: str) -> QCanSignalDescription:
    """
    Calls Qt's 'QCanSignalDescription
    QCanMessageDescription::signalDescriptionForName(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCanSignalDescription
      A new cute QCanSignalDescription around the copy Qt gave back. Python
      owns it.
    """
    #  QCanSignalDescription
    #      QCanMessageDescription::signalDescriptionForName(const QString
    #      &name) const
    address = self.uglySide.call(
        'ritual_ZNK22QCanMessageDescription24signalDescriptionForNameERK7QS'
        'tring',
        name,
    )
    from . import QCanSignalDescription
    return QCanSignalDescription._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QCanMessageDescription::setName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanMessageDescription::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN22QCanMessageDescription7setNameERK7QString', name,
    )

  @overload(int)
  def setSize(self, size: int) -> None:
    """
    Calls Qt's 'void QCanMessageDescription::setSize(quint8 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#setSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QCanMessageDescription::setSize(quint8 size)
    self.uglySide.call('ritual_ZN22QCanMessageDescription7setSizeEh', size)

  @overload(str)
  def setTransmitter(self, transmitter: str) -> None:
    """
    Calls Qt's 'void QCanMessageDescription::setTransmitter(const QString
    &transmitter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#setTransmitter

    Parameters
    ----------

    transmitter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanMessageDescription::setTransmitter(const QString
    #      &transmitter)
    self.uglySide.call(
        'ritual_ZN22QCanMessageDescription14setTransmitterERK7QString',
        transmitter,
    )

  @overload(str)
  def setComment(self, text: str) -> None:
    """
    Calls Qt's 'void QCanMessageDescription::setComment(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#setComment

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanMessageDescription::setComment(const QString &text)
    self.uglySide.call(
        'ritual_ZN22QCanMessageDescription10setCommentERK7QString', text,
    )

  @overload(QList[QCanSignalDescription])
  def setSignalDescriptions(
      self,
      descriptions: QList[QCanSignalDescription],
  ) -> None:
    """
    Calls Qt's 'void QCanMessageDescription::setSignalDescriptions(const
    QList<QCanSignalDescription> &descriptions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#setSignalDescriptions

    Parameters
    ----------

    descriptions : QList[QCanSignalDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCanMessageDescription::setSignalDescriptions(const
    #      QList<QCanSignalDescription> &descriptions)
    self.uglySide.call(
        'ritual_ZN22QCanMessageDescription21setSignalDescriptionsERK5QListI'
        '21QCanSignalDescriptionE',
        self._valueOf(descriptions),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QCanMessageDescription
    &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QCanMessageDescription &msg)
    address = Rituals.call(
        'ritual_Zls6QDebugRK22QCanMessageDescription',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanMessageDescription::QCanMessageDescription()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#QCanMessageDescription
    """
    #  QCanMessageDescription::QCanMessageDescription()
    self._noteCreation(QCanMessageDescription, lambda: Rituals.call(
        'ritual_ZN22QCanMessageDescriptionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCanMessageDescription) -> None:
    """
    Notes what was given, for Qt's
    'QCanMessageDescription::QCanMessageDescription(const
    QCanMessageDescription &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#QCanMessageDescription

    Parameters
    ----------

    other : QCanMessageDescription
      Passed on as a value: Qt reads the C++ QCanMessageDescription, which
      stays Python's own.
    """
    #  QCanMessageDescription::QCanMessageDescription(const
    #      QCanMessageDescription &other)
    self._noteCreation(QCanMessageDescription, lambda: Rituals.call(
        'ritual_ZN22QCanMessageDescriptionC1ERKS_', self._valueOf(other),
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

  def clearSignalDescriptions(self) -> None:
    """
    Calls Qt's 'void QCanMessageDescription::clearSignalDescriptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html
    """
    #  void QCanMessageDescription::clearSignalDescriptions()
    self.uglySide.call(
        'ritual_ZN22QCanMessageDescription23clearSignalDescriptionsEv',
    )

  @overload(QCanSignalDescription)
  def addSignalDescription(self, description: QCanSignalDescription) -> None:
    """
    Calls Qt's 'void QCanMessageDescription::addSignalDescription(const
    QCanSignalDescription &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanmessagedescription.html#addSignalDescription

    Parameters
    ----------

    description : QCanSignalDescription
      Passed on as a value: Qt reads the C++ QCanSignalDescription, which
      stays Python's own.
    """
    #  void QCanMessageDescription::addSignalDescription(const
    #      QCanSignalDescription &description)
    self.uglySide.call(
        'ritual_ZN22QCanMessageDescription20addSignalDescriptionERK21QCanSi'
        'gnalDescription',
        self._valueOf(description),
    )

  @staticmethod
  def setUniqueId(*__, **_) -> Never:
    """
    Qt's 'void QCanMessageDescription::setUniqueId(QtCanBus::UniqueId id)':
    names the enum 'QtCanBus::UniqueId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QCanMessageDescription.setUniqueId' has no cute function yet. "
        "Qt's 'void QCanMessageDescription::setUniqueId(QtCanBus::UniqueId "
        "id)': names the enum 'QtCanBus::UniqueId', whose class cannot be "
        "named here.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanMessageDescription::swap(QCanMessageDescription &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanMessageDescription.swap' has no cute function yet. Qt's 'void "
        "QCanMessageDescription::swap(QCanMessageDescription &other)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def uniqueId(*__, **_) -> Never:
    """
    Qt's 'QtCanBus::UniqueId QCanMessageDescription::uniqueId() const': gives
    the enum 'QtCanBus::UniqueId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QCanMessageDescription.uniqueId' has no cute function yet. Qt's "
        "'QtCanBus::UniqueId QCanMessageDescription::uniqueId() const': "
        "gives the enum 'QtCanBus::UniqueId', whose class cannot be named "
        "here.")


#  Qt's 'QList<QCanMessageDescription>': the list of QCanMessageDescription,
#  which 'QList[QCanMessageDescription]' gives. It is made here, so that
#  there is one as soon as there can be a QCanMessageDescription.
QList.createKind(
    QCanMessageDescription, 'value',
    make='ritual_list_make_QCanMessageDescription',
    add='ritual_list_add_QCanMessageDescription',
    size='ritual_list_size_QCanMessageDescription',
    at='ritual_list_at_QCanMessageDescription',
    drop='ritual_list_drop_QCanMessageDescription',
)
