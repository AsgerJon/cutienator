"""
QUtiMimeConverter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qutimimeconverter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMimeData, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMimeData = WAIT['QMimeData']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUtiMimeConverter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUtiMimeConverter: a plain Python object standing in
  front of one C++ QUtiMimeConverter.

  What exists
  -----------

  Every function of Qt's QUtiMimeConverter that has a ritual and that Python
  can call so far, 7 names in all: 'scope', 'canConvert', 'convertFromMime',
  'utiForMime', 'mimeForUti', 'convertToMime', 'count'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUtiMimeConverter::~QUtiMimeConverter()': the destructor: Python
    never removes a C++ QUtiMimeConverter.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 forbidden; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QUtiMimeConverter is created at the first use, not by
    'QUtiMimeConverter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUtiMimeConverter.
  - Each name of Qt's QUtiMimeConverter that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QUtiMimeConverter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HandlerScopeFlag(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QUtiMimeConverter::HandlerScopeFlag' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QUtiMimeConverter::HandlerScope'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    DnD = 0x1
    Clipboard = 0x2
    Qt_compatible = 0x4
    Qt3_compatible = 0x8
    All = 0x3
    AllCompatible = 0x7

  HandlerScope = HandlerScopeFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUtiMimeConverter'

  #  A C++ QUtiMimeConverter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUtiMimeConverter'

  #  The functions Qt calls itself that QUtiMimeConverter is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'convertFromMime': (
          'QList<QByteArray> QUtiMimeConverter::convertFromMime(const '
          'QString &, const QVariant &, const QString &) const',
      ),
      'convertToMime': (
          'QVariant QUtiMimeConverter::convertToMime(const QString &, '
          'const QList<QByteArray> &, const QString &) const',
      ),
  }

  #  The functions Qt calls itself that QUtiMimeConverter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'utiForMime': (
          ('_ZNK17QUtiMimeConverter10utiForMimeERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'mimeForUti': (
          ('_ZNK17QUtiMimeConverter10mimeForUtiERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'count': (
          ('_ZNK17QUtiMimeConverter5countEPK9QMimeData',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
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

  def scope(self) -> HandlerScope:
    """
    Calls Qt's 'HandlerScope QUtiMimeConverter::scope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qutimimeconverter.html#scope

    Returns
    -------

    HandlerScope
      The value standing for the combination Qt gave back.
    """
    #  HandlerScope QUtiMimeConverter::scope() const
    return QUtiMimeConverter.HandlerScope(self.uglySide.call(
        'ritual_ZNK17QUtiMimeConverter5scopeEv',
    ))

  @overload(str, str)
  def canConvert(self, mime: str, uti: str) -> bool:
    """
    Calls Qt's 'bool QUtiMimeConverter::canConvert(const QString &mime, const
    QString &uti) const'.

    Qt's own words: https://doc.qt.io/qt-6/qutimimeconverter.html#canConvert

    Parameters
    ----------

    mime : str
      Passed on as it is: a QString is made of it for the call.

    uti : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QUtiMimeConverter::canConvert(const QString &mime, const QString
    #      &uti) const
    return self.uglySide.call(
        'ritual_ZNK17QUtiMimeConverter10canConvertERK7QStringS2_', mime, uti,
    )

  @overload(str, QVariant, str)
  def convertFromMime(
      self,
      mime: str,
      data: QVariant,
      uti: str,
  ) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QUtiMimeConverter::convertFromMime(const
    QString &mime, const QVariant &data, const QString &uti) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qutimimeconverter.html#convertFromMime

    Parameters
    ----------

    mime : str
      Passed on as it is: a QString is made of it for the call.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    uti : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QUtiMimeConverter::convertFromMime(const QString
    #      &mime, const QVariant &data, const QString &uti) const
    address = self.uglySide.call(
        'ritual_ZNK17QUtiMimeConverter15convertFromMimeERK7QStringRK8QVaria'
        'ntS2_',
        mime, self._valueOf(data), uti,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(str)
  def utiForMime(self, mime: str) -> str:
    """
    Calls Qt's 'QString QUtiMimeConverter::utiForMime(const QString &mime)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qutimimeconverter.html#utiForMime

    Parameters
    ----------

    mime : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUtiMimeConverter::utiForMime(const QString &mime) const
    return self.uglySide.call(
        'ritual_ZNK17QUtiMimeConverter10utiForMimeERK7QString', mime,
    )

  @overload(str)
  def mimeForUti(self, uti: str) -> str:
    """
    Calls Qt's 'QString QUtiMimeConverter::mimeForUti(const QString &uti)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qutimimeconverter.html#mimeForUti

    Parameters
    ----------

    uti : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUtiMimeConverter::mimeForUti(const QString &uti) const
    return self.uglySide.call(
        'ritual_ZNK17QUtiMimeConverter10mimeForUtiERK7QString', uti,
    )

  @overload(str, QList[QByteArray], str)
  def convertToMime(
      self,
      mime: str,
      data: QList[QByteArray],
      uti: str,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QUtiMimeConverter::convertToMime(const QString
    &mime, const QList<QByteArray> &data, const QString &uti) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qutimimeconverter.html#convertToMime

    Parameters
    ----------

    mime : str
      Passed on as it is: a QString is made of it for the call.

    data : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    uti : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QUtiMimeConverter::convertToMime(const QString &mime, const
    #      QList<QByteArray> &data, const QString &uti) const
    address = self.uglySide.call(
        'ritual_ZNK17QUtiMimeConverter13convertToMimeERK7QStringRK5QListI10'
        'QByteArrayES2_',
        mime, self._valueOf(data), uti,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QMimeData)
  @overload(NoneType)
  def count(self, mimeData: Optional[QMimeData]) -> int:
    """
    Calls Qt's 'int QUtiMimeConverter::count(const QMimeData *mimeData)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qutimimeconverter.html#count

    Parameters
    ----------

    mimeData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QUtiMimeConverter::count(const QMimeData *mimeData) const
    ritual = 'ritual_ZNK17QUtiMimeConverter5countEPK9QMimeData'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QUtiMimeConverter5countEPK9QMimeData'
    return self.uglySide.call(ritual, self._addressOf(mimeData))

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QUtiMimeConverter::QUtiMimeConverter()': the class is abstract,
      so C++ cannot make one, and the C++ class of ours does not fill in
      every function it leaves open.
    - Qt's 'QUtiMimeConverter::QUtiMimeConverter(HandlerScope scope)': the
      class is abstract, so C++ cannot make one, and the C++ class of ours
      does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QUtiMimeConverter.__init__' has no cute function yet. Qt's "
        "'QUtiMimeConverter::QUtiMimeConverter()': the class is abstract, "
        "so C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open. Qt's "
        "'QUtiMimeConverter::QUtiMimeConverter(HandlerScope scope)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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
