"""
QInternalMimeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qinternalmimedata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QInternalMimeData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMimeData, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInternalMimeData(QMimeData):
  """
  The cute side of Qt's QInternalMimeData: a plain Python object standing in
  front of one C++ QInternalMimeData.

  It is built on the cute 'QMimeData', as Qt's QInternalMimeData is built on
  Qt's QMimeData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInternalMimeData that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'hasFormat',
  'formats', 'canReadData', 'formatsHelper', 'hasFormatHelper',
  'renderDataHelper', 'retrieveData', 'hasFormat_sys', 'formats_sys',
  'retrieveData_sys'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInternalMimeData::~QInternalMimeData()': the destructor: Python
    never removes a C++ QInternalMimeData.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found; 1 the class
  is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QInternalMimeData is created at the first use, not by
    'QInternalMimeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInternalMimeData.
  - Qt tells when it has removed the C++ QInternalMimeData. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QInternalMimeData::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qinternalmimedata.html#tr

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
    #  QString QInternalMimeData::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QInternalMimeData2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def canReadData(mimeType: str) -> bool:
    """
    Calls Qt's 'bool QInternalMimeData::canReadData(const QString
    &mimeType)'.

    Qt's own words: https://doc.qt.io/qt-6/qinternalmimedata.html#canReadData

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QInternalMimeData::canReadData(const QString &mimeType)
    return Rituals.call(
        'ritual_ZN17QInternalMimeData11canReadDataERK7QString', mimeType,
    )

  @staticmethod
  @overload(QMimeData)
  @overload(NoneType)
  def formatsHelper(data: Optional[QMimeData]) -> QStringList:
    """
    Calls Qt's 'QStringList QInternalMimeData::formatsHelper(const QMimeData
    *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinternalmimedata.html#formatsHelper

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QInternalMimeData::formatsHelper(const QMimeData *data)
    address = Rituals.call(
        'ritual_ZN17QInternalMimeData13formatsHelperEPK9QMimeData',
        CuteMixin._addressOf(data),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str, QMimeData)
  @overload(str, NoneType)
  def hasFormatHelper(mimeType: str, data: Optional[QMimeData]) -> bool:
    """
    Calls Qt's 'bool QInternalMimeData::hasFormatHelper(const QString
    &mimeType, const QMimeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinternalmimedata.html#hasFormatHelper

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QInternalMimeData::hasFormatHelper(const QString &mimeType, const
    #      QMimeData *data)
    return Rituals.call(
        'ritual_ZN17QInternalMimeData15hasFormatHelperERK7QStringPK9QMimeDa'
        'ta',
        mimeType, CuteMixin._addressOf(data),
    )

  @staticmethod
  @overload(str, QMimeData)
  @overload(str, NoneType)
  def renderDataHelper(
      mimeType: str,
      data: Optional[QMimeData],
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QInternalMimeData::renderDataHelper(const QString
    &mimeType, const QMimeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinternalmimedata.html#renderDataHelper

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QInternalMimeData::renderDataHelper(const QString
    #      &mimeType, const QMimeData *data)
    address = Rituals.call(
        'ritual_ZN17QInternalMimeData16renderDataHelperERK7QStringPK9QMimeD'
        'ata',
        mimeType, CuteMixin._addressOf(data),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInternalMimeData'

  #  A C++ QInternalMimeData Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInternalMimeData'

  #  The functions Qt calls itself that QInternalMimeData is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'formats_sys': (
          'QStringList QInternalMimeData::formats_sys() const',
      ),
  }

  #  The functions Qt calls itself that QInternalMimeData is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'hasFormat_sys': (
          ('_ZNK17QInternalMimeData13hasFormat_sysERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'retrieveData_sys': (
          ('_ZNK17QInternalMimeData16retrieveData_sysERK7QString9QMetaType',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QMetaType'),
           )),
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
    Calls Qt's 'const QMetaObject *QInternalMimeData::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinternalmimedata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QInternalMimeData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QInternalMimeData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def hasFormat(self, mimeType: str) -> bool:
    """
    Calls Qt's 'bool QInternalMimeData::hasFormat(const QString &mimeType)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qinternalmimedata.html#hasFormat

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QInternalMimeData::hasFormat(const QString &mimeType) const
    ritual = 'ritual_ZNK17QInternalMimeData9hasFormatERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QInternalMimeData9hasFormatERK7QString'
    return self.uglySide.call(ritual, mimeType)

  def formats(self) -> QStringList:
    """
    Calls Qt's 'QStringList QInternalMimeData::formats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinternalmimedata.html#formats

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QInternalMimeData::formats() const
    address = self.uglySide.call('ritual_ZNK17QInternalMimeData7formatsEv')
    return QStringList._cuteOwning(address)

  @overload(str, QMetaType)
  def retrieveData(self, mimeType: str, type: QMetaType) -> QVariant:
    """
    Calls Qt's 'QVariant QInternalMimeData::retrieveData(const QString
    &mimeType, QMetaType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinternalmimedata.html#retrieveData

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QInternalMimeData::retrieveData(const QString &mimeType,
    #      QMetaType type) const
    ritual = (
        'ritual_ZNK17QInternalMimeData12retrieveDataERK7QString9QMetaType')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QInternalMimeData12retrieveDataERK7QString9QMeta'
          'Type')
    address = self.uglySide.call(ritual, mimeType, self._valueOf(type))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def hasFormat_sys(self, mimeType: str) -> bool:
    """
    Calls Qt's 'bool QInternalMimeData::hasFormat_sys(const QString
    &mimeType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinternalmimedata.html#hasFormat_sys

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QInternalMimeData::hasFormat_sys(const QString &mimeType) const
    return self.uglySide.call(
        'ritual_ZNK17QInternalMimeData13hasFormat_sysERK7QString', mimeType,
    )

  def formats_sys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QInternalMimeData::formats_sys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinternalmimedata.html#formats_sys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QInternalMimeData::formats_sys() const
    address = self.uglySide.call(
        'ritual_ZNK17QInternalMimeData11formats_sysEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str, QMetaType)
  def retrieveData_sys(self, mimeType: str, type: QMetaType) -> QVariant:
    """
    Calls Qt's 'QVariant QInternalMimeData::retrieveData_sys(const QString
    &mimeType, QMetaType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinternalmimedata.html#retrieveData_sys

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QInternalMimeData::retrieveData_sys(const QString &mimeType,
    #      QMetaType type) const
    address = self.uglySide.call(
        'ritual_ZNK17QInternalMimeData16retrieveData_sysERK7QString9QMetaTy'
        'pe',
        mimeType, self._valueOf(type),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
