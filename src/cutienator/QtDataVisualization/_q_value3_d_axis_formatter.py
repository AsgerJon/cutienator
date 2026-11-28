"""
QValue3DAxisFormatter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qvalue3daxisformatter.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLocale, QMetaObject
  from . import QValue3DAxis, QValue3DAxisFormatterPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QValue3DAxisFormatterPrivate = WAIT['QValue3DAxisFormatterPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QValue3DAxisFormatter(QObject):
  """
  The cute side of Qt's QValue3DAxisFormatter: a plain Python object standing
  in front of one C++ QValue3DAxisFormatter.

  It is built on the cute 'QObject', as Qt's QValue3DAxisFormatter is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QValue3DAxisFormatter that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr',
  'setAllowNegatives', 'allowNegatives', 'setAllowZero', 'allowZero',
  'createNewInstance', 'recalculate', 'stringForValue', 'positionAt',
  'valueAt', 'markDirty', 'axis', 'setLocale', 'locale'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QValue3DAxisFormatter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QValue3DAxisFormatter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QValue3DAxisFormatter::~QValue3DAxisFormatter()': the destructor:
    Python never removes a C++ QValue3DAxisFormatter.
  - Qt's 'void QValue3DAxisFormatter::populateCopy(QValue3DAxisFormatter
    &copy) const': takes a type Python has no way to hand over yet.
  - Qt's 'QList<float> &QValue3DAxisFormatter::gridPositions() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<float> &QValue3DAxisFormatter::subGridPositions() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<float> &QValue3DAxisFormatter::labelPositions() const': gives
    a type Python has no way to take yet.
  - Qt's 'QStringList &QValue3DAxisFormatter::labelStrings() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QValue3DAxisFormatter is created at the first use, not by
    'QValue3DAxisFormatter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QValue3DAxisFormatter.
  - Qt tells when it has removed the C++ QValue3DAxisFormatter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QValue3DAxisFormatter that has no cute function yet,
    'gridPositions', 'labelPositions', 'labelStrings', 'populateCopy',
    'subGridPositions', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QValue3DAxisFormatter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisformatter.html#tr

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
    #  QString QValue3DAxisFormatter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QValue3DAxisFormatter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QValue3DAxisFormatter'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QValue3DAxisFormatter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QValue3DAxisFormatter'

  #  The functions Qt calls itself that QValue3DAxisFormatter is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'populateCopy': (
          'void QValue3DAxisFormatter::populateCopy(QValue3DAxisFormatter '
          '&) const',
      ),
  }

  #  The functions Qt calls itself that QValue3DAxisFormatter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createNewInstance': (
          ('_ZNK21QValue3DAxisFormatter17createNewInstanceEv',
           ('address', 'address',
            'QtDataVisualization:QValue3DAxisFormatter'),
           ()),
      ),
      'recalculate': (
          ('_ZN21QValue3DAxisFormatter11recalculateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stringForValue': (
          ('_ZNK21QValue3DAxisFormatter14stringForValueEdRK7QString',
           ('address', 'text', ''),
           (
               ('double', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'positionAt': (
          ('_ZNK21QValue3DAxisFormatter10positionAtEf',
           ('float', 'number', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'valueAt': (
          ('_ZNK21QValue3DAxisFormatter7valueAtEf',
           ('float', 'number', ''),
           (
               ('float', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QValue3DAxisFormatter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QValue3DAxisFormatter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QValue3DAxisFormatter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def allowNegatives(self) -> bool:
    """
    Calls Qt's 'bool QValue3DAxisFormatter::allowNegatives() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#allowNegatives
    """
    #  bool QValue3DAxisFormatter::allowNegatives() const
    return self.uglySide.call(
        'ritual_ZNK21QValue3DAxisFormatter14allowNegativesEv',
    )

  def allowZero(self) -> bool:
    """
    Calls Qt's 'bool QValue3DAxisFormatter::allowZero() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#allowZero
    """
    #  bool QValue3DAxisFormatter::allowZero() const
    return self.uglySide.call(
        'ritual_ZNK21QValue3DAxisFormatter9allowZeroEv',
    )

  def createNewInstance(self) -> Optional[QValue3DAxisFormatter]:
    """
    Calls Qt's 'QValue3DAxisFormatter
    *QValue3DAxisFormatter::createNewInstance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#createNewInstance

    Returns
    -------

    Optional[QValue3DAxisFormatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxisFormatter *QValue3DAxisFormatter::createNewInstance()
    #      const
    ritual = 'ritual_ZNK21QValue3DAxisFormatter17createNewInstanceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QValue3DAxisFormatter17createNewInstanceEv'
    address = self.uglySide.call(ritual)
    return QValue3DAxisFormatter._cuteAt(address)

  @overload(float, str)
  def stringForValue(self, value: float, format: str) -> str:
    """
    Calls Qt's 'QString QValue3DAxisFormatter::stringForValue(qreal value,
    const QString &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#stringForValue

    Parameters
    ----------

    value : float
      Passed on as it is.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QValue3DAxisFormatter::stringForValue(qreal value, const
    #      QString &format) const
    ritual = 'ritual_ZNK21QValue3DAxisFormatter14stringForValueEdRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QValue3DAxisFormatter14stringForValueEdRK7QStrin'
          'g')
    return self.uglySide.call(ritual, value, format)

  @overload(float)
  def positionAt(self, value: float) -> float:
    """
    Calls Qt's 'float QValue3DAxisFormatter::positionAt(float value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#positionAt

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  float QValue3DAxisFormatter::positionAt(float value) const
    ritual = 'ritual_ZNK21QValue3DAxisFormatter10positionAtEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QValue3DAxisFormatter10positionAtEf'
    return self.uglySide.call(ritual, value)

  @overload(float)
  def valueAt(self, position: float) -> float:
    """
    Calls Qt's 'float QValue3DAxisFormatter::valueAt(float position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisformatter.html#valueAt

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  float QValue3DAxisFormatter::valueAt(float position) const
    ritual = 'ritual_ZNK21QValue3DAxisFormatter7valueAtEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QValue3DAxisFormatter7valueAtEf'
    return self.uglySide.call(ritual, position)

  def axis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QValue3DAxisFormatter::axis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisformatter.html#axis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QValue3DAxisFormatter::axis() const
    address = self.uglySide.call('ritual_ZNK21QValue3DAxisFormatter4axisEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QValue3DAxisFormatter::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalue3daxisformatter.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QValue3DAxisFormatter::locale() const
    address = self.uglySide.call(
        'ritual_ZNK21QValue3DAxisFormatter6localeEv',
    )
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAllowNegatives(self, allow: bool) -> None:
    """
    Calls Qt's 'void QValue3DAxisFormatter::setAllowNegatives(bool allow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#setAllowNegatives

    Parameters
    ----------

    allow : bool
      Passed on as it is.
    """
    #  void QValue3DAxisFormatter::setAllowNegatives(bool allow)
    self.uglySide.call(
        'ritual_ZN21QValue3DAxisFormatter17setAllowNegativesEb', allow,
    )

  @overload(bool)
  def setAllowZero(self, allow: bool) -> None:
    """
    Calls Qt's 'void QValue3DAxisFormatter::setAllowZero(bool allow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#setAllowZero

    Parameters
    ----------

    allow : bool
      Passed on as it is.
    """
    #  void QValue3DAxisFormatter::setAllowZero(bool allow)
    self.uglySide.call(
        'ritual_ZN21QValue3DAxisFormatter12setAllowZeroEb', allow,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QValue3DAxisFormatter::setLocale(const QLocale
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QValue3DAxisFormatter::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN21QValue3DAxisFormatter9setLocaleERK7QLocale',
        self._valueOf(locale),
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

  @overload(QValue3DAxisFormatterPrivate)
  @overload(NoneType)
  @overload(QValue3DAxisFormatterPrivate, QObject)
  @overload(QValue3DAxisFormatterPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QValue3DAxisFormatterPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QValue3DAxisFormatter::QValue3DAxisFormatter(
    QValue3DAxisFormatterPrivate *d, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#QValue3DAxisFormatter

    Parameters
    ----------

    d : Optional[QValue3DAxisFormatterPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QValue3DAxisFormatter::QValue3DAxisFormatter(
    #      QValue3DAxisFormatterPrivate *d, QObject *parent)
    self._noteCreation(QValue3DAxisFormatter, lambda: Rituals.call(
        'ritual_ZN21QValue3DAxisFormatterC1EP28QValue3DAxisFormatterPrivate'
        'P7QObject',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QValue3DAxisFormatter::QValue3DAxisFormatter(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#QValue3DAxisFormatter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QValue3DAxisFormatter::QValue3DAxisFormatter(QObject *parent)
    self._noteCreation(QValue3DAxisFormatter, lambda: Rituals.call(
        'ritual_ZN21QValue3DAxisFormatterC1EP7QObject',
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

  def recalculate(self) -> None:
    """
    Calls Qt's 'void QValue3DAxisFormatter::recalculate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#recalculate
    """
    #  void QValue3DAxisFormatter::recalculate()
    ritual = 'ritual_ZN21QValue3DAxisFormatter11recalculateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QValue3DAxisFormatter11recalculateEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(bool)
  def markDirty(self, labelsChange: bool = False) -> None:
    """
    Calls Qt's 'void QValue3DAxisFormatter::markDirty(bool labelsChange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalue3daxisformatter.html#markDirty

    Parameters
    ----------

    labelsChange : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QValue3DAxisFormatter::markDirty(bool labelsChange)
    self.uglySide.call(
        'ritual_ZN21QValue3DAxisFormatter9markDirtyEb', labelsChange,
    )

  @staticmethod
  def gridPositions(*__, **_) -> Never:
    """
    Qt's 'QList<float> &QValue3DAxisFormatter::gridPositions() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QValue3DAxisFormatter.gridPositions' has no cute function yet. "
        "Qt's 'QList<float> &QValue3DAxisFormatter::gridPositions() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def labelPositions(*__, **_) -> Never:
    """
    Qt's 'QList<float> &QValue3DAxisFormatter::labelPositions() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QValue3DAxisFormatter.labelPositions' has no cute function yet. "
        "Qt's 'QList<float> &QValue3DAxisFormatter::labelPositions() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def labelStrings(*__, **_) -> Never:
    """
    Qt's 'QStringList &QValue3DAxisFormatter::labelStrings() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QValue3DAxisFormatter.labelStrings' has no cute function yet. "
        "Qt's 'QStringList &QValue3DAxisFormatter::labelStrings() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def populateCopy(*__, **_) -> Never:
    """
    Qt's 'void QValue3DAxisFormatter::populateCopy(QValue3DAxisFormatter
    &copy) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QValue3DAxisFormatter.populateCopy' has no cute function yet. "
        "Qt's 'void "
        "QValue3DAxisFormatter::populateCopy(QValue3DAxisFormatter &copy) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def subGridPositions(*__, **_) -> Never:
    """
    Qt's 'QList<float> &QValue3DAxisFormatter::subGridPositions() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QValue3DAxisFormatter.subGridPositions' has no cute function yet. "
        "Qt's 'QList<float> &QValue3DAxisFormatter::subGridPositions() "
        "const': gives a type Python has no way to take yet.")
