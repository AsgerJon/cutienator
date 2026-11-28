"""
QQmlColorProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlColorProvider to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QQmlColorProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlColorProvider: a plain Python object standing in
  front of one C++ QQmlColorProvider.

  C++ hands a QQmlColorProvider around as a copy, so every C++
  QQmlColorProvider behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlColorProvider that has a ritual and that Python
  can call so far, 7 names in all: 'fromRgbF', 'fromHslF', 'fromHsvF',
  'lighter', 'darker', 'alpha', 'tint'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlColorProvider::~QQmlColorProvider()': the destructor: Python
    removes its C++ QQmlColorProvider by it, and has no other use for it.
  - Qt's 'QVariant QQmlColorProvider::colorFromString(const QString &a0, bool
    *a1)': takes a number to change where it is.
  - Qt's 'unsigned int QQmlColorProvider::rgbaFromString(const QString &a0,
    bool *a1)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QQmlColorProvider is created at the first use, not by
    'QQmlColorProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlColorProvider back gives a copy the ritual made
    for Python, in a new cute QQmlColorProvider.
  - Each name of Qt's QQmlColorProvider that has no cute function yet,
    'colorFromString', 'rgbaFromString', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlColorProvider'

  #  A C++ QQmlColorProvider Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlColorProvider'

  #  The functions Qt calls itself that QQmlColorProvider is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'colorFromString': (
          'QVariant QQmlColorProvider::colorFromString(const QString &, '
          'bool *)',
      ),
      'rgbaFromString': (
          'unsigned int QQmlColorProvider::rgbaFromString(const QString &, '
          'bool *)',
      ),
  }

  #  The functions Qt calls itself that QQmlColorProvider is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'fromRgbF': (
          ('_ZN17QQmlColorProvider8fromRgbFEdddd',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'fromHslF': (
          ('_ZN17QQmlColorProvider8fromHslFEdddd',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'fromHsvF': (
          ('_ZN17QQmlColorProvider8fromHsvFEdddd',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'lighter': (
          ('_ZN17QQmlColorProvider7lighterERK8QVariantd',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('double', 'number', ''),
           )),
      ),
      'darker': (
          ('_ZN17QQmlColorProvider6darkerERK8QVariantd',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('double', 'number', ''),
           )),
      ),
      'alpha': (
          ('_ZN17QQmlColorProvider5alphaERK8QVariantd',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('double', 'number', ''),
           )),
      ),
      'tint': (
          ('_ZN17QQmlColorProvider4tintERK8QVariantS2_',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Qt's '~QQmlColorProvider()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlColorProvider behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQmlColorProviderD1Ev'

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

  @overload(float, float, float, float)
  def fromRgbF(self, a0: float, a1: float, a2: float, a3: float) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlColorProvider::fromRgbF(double a0, double a1,
    double a2, double a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcolorprovider.html#fromRgbF

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    a2 : float
      Passed on as it is.

    a3 : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlColorProvider::fromRgbF(double a0, double a1, double a2,
    #      double a3)
    ritual = 'ritual_ZN17QQmlColorProvider8fromRgbFEdddd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlColorProvider8fromRgbFEdddd'
    address = self.uglySide.call(ritual, a0, a1, a2, a3)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float, float)
  def fromHslF(self, a0: float, a1: float, a2: float, a3: float) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlColorProvider::fromHslF(double a0, double a1,
    double a2, double a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcolorprovider.html#fromHslF

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    a2 : float
      Passed on as it is.

    a3 : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlColorProvider::fromHslF(double a0, double a1, double a2,
    #      double a3)
    ritual = 'ritual_ZN17QQmlColorProvider8fromHslFEdddd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlColorProvider8fromHslFEdddd'
    address = self.uglySide.call(ritual, a0, a1, a2, a3)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(float, float, float, float)
  def fromHsvF(self, a0: float, a1: float, a2: float, a3: float) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlColorProvider::fromHsvF(double a0, double a1,
    double a2, double a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcolorprovider.html#fromHsvF

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    a2 : float
      Passed on as it is.

    a3 : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlColorProvider::fromHsvF(double a0, double a1, double a2,
    #      double a3)
    ritual = 'ritual_ZN17QQmlColorProvider8fromHsvFEdddd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlColorProvider8fromHsvFEdddd'
    address = self.uglySide.call(ritual, a0, a1, a2, a3)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant, float)
  def lighter(self, a0: QVariant, a1: float) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlColorProvider::lighter(const QVariant &a0, qreal
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcolorprovider.html#lighter

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a1 : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlColorProvider::lighter(const QVariant &a0, qreal a1)
    ritual = 'ritual_ZN17QQmlColorProvider7lighterERK8QVariantd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlColorProvider7lighterERK8QVariantd'
    address = self.uglySide.call(ritual, self._valueOf(a0), a1)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant, float)
  def darker(self, a0: QVariant, a1: float) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlColorProvider::darker(const QVariant &a0, qreal
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcolorprovider.html#darker

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a1 : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlColorProvider::darker(const QVariant &a0, qreal a1)
    ritual = 'ritual_ZN17QQmlColorProvider6darkerERK8QVariantd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlColorProvider6darkerERK8QVariantd'
    address = self.uglySide.call(ritual, self._valueOf(a0), a1)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant, float)
  def alpha(self, a0: QVariant, a1: float) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlColorProvider::alpha(const QVariant &a0, qreal
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcolorprovider.html#alpha

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a1 : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlColorProvider::alpha(const QVariant &a0, qreal a1)
    ritual = 'ritual_ZN17QQmlColorProvider5alphaERK8QVariantd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlColorProvider5alphaERK8QVariantd'
    address = self.uglySide.call(ritual, self._valueOf(a0), a1)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant, QVariant)
  def tint(self, a0: QVariant, a1: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlColorProvider::tint(const QVariant &a0, const
    QVariant &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcolorprovider.html#tint

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlColorProvider::tint(const QVariant &a0, const QVariant
    #      &a1)
    ritual = 'ritual_ZN17QQmlColorProvider4tintERK8QVariantS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlColorProvider4tintERK8QVariantS2_'
    address = self.uglySide.call(
        ritual, self._valueOf(a0), self._valueOf(a1),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  def colorFromString(*__, **_) -> Never:
    """
    Qt's 'QVariant QQmlColorProvider::colorFromString(const QString &a0, bool
    *a1)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlColorProvider.colorFromString' has no cute function yet. Qt's "
        "'QVariant QQmlColorProvider::colorFromString(const QString &a0, "
        "bool *a1)': takes a number to change where it is.")

  @staticmethod
  def rgbaFromString(*__, **_) -> Never:
    """
    Qt's 'unsigned int QQmlColorProvider::rgbaFromString(const QString &a0,
    bool *a1)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlColorProvider.rgbaFromString' has no cute function yet. Qt's "
        "'unsigned int QQmlColorProvider::rgbaFromString(const QString &a0, "
        "bool *a1)': takes a number to change where it is.")
