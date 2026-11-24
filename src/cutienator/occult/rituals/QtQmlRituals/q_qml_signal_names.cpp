//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlsignalnames_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlsignalnames_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>

//  QString QQmlSignalNames::propertyNameToChangedSignalName(QStringView
//      property)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlSignalNames31propertyNameToChangedSignalNameE11QStringView(
    const QString *property) {
  return new QString(
      QQmlSignalNames::propertyNameToChangedSignalName(
          QStringView(*property)));
}

//  QString QQmlSignalNames::propertyNameToChangedHandlerName(QStringView
//      property)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlSignalNames32propertyNameToChangedHandlerNameE11QStringView(
    const QString *property) {
  return new QString(
      QQmlSignalNames::propertyNameToChangedHandlerName(
          QStringView(*property)));
}

//  QString QQmlSignalNames::signalNameToHandlerName(QAnyStringView signal)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlSignalNames23signalNameToHandlerNameE14QAnyStringView(
    const QString *signal) {
  return new QString(
      QQmlSignalNames::signalNameToHandlerName(
          QAnyStringView(*signal)));
}

//  bool QQmlSignalNames::isChangedHandlerName(QStringView signalName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQmlSignalNames20isChangedHandlerNameE11QStringView(
    const QString *signalName) {
  return QQmlSignalNames::isChangedHandlerName(QStringView(*signalName));
}

//  bool QQmlSignalNames::isChangedSignalName(QStringView signalName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQmlSignalNames19isChangedSignalNameE11QStringView(
    const QString *signalName) {
  return QQmlSignalNames::isChangedSignalName(QStringView(*signalName));
}

//  bool QQmlSignalNames::isHandlerName(QStringView signalName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQmlSignalNames13isHandlerNameE11QStringView(
    const QString *signalName) {
  return QQmlSignalNames::isHandlerName(QStringView(*signalName));
}

//  QString QQmlSignalNames::addPrefixToPropertyName(QStringView prefix,
//      QStringView propertyName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlSignalNames23addPrefixToPropertyNameE11QStringViewS0_(
    const QString *prefix,
    const QString *propertyName) {
  return new QString(
      QQmlSignalNames::addPrefixToPropertyName(
          QStringView(*prefix),
          QStringView(*propertyName)));
}

//  QQmlSignalNames::~QQmlSignalNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlSignalNamesD1Ev(QQmlSignalNames *self) {
  delete self;
}
