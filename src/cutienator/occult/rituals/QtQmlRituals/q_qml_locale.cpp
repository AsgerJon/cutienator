//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmllocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_locale)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmllocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QQmlLocale::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlLocale22qt_qmlMarker_anonymousEv(QQmlLocale *self) {
  self->qt_qmlMarker_anonymous();
}

//  QV4::ReturnedValue QQmlLocale::locale(QV4::ExecutionEngine *engine, const
//      QString &localeName)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN10QQmlLocale6localeEPN3QV415ExecutionEngineERK7QString(
    QV4::ExecutionEngine *engine,
    const QString *localeName) {
  return QQmlLocale::locale(engine, *localeName);
}

//  void QQmlLocale::registerStringLocaleCompare(QV4::ExecutionEngine
//      *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlLocale27registerStringLocaleCompareEPN3QV415ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  QQmlLocale::registerStringLocaleCompare(engine);
}

//  QV4::ReturnedValue QQmlLocale::method_localeCompare(const
//      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
//      QV4::Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN10QQmlLocale20method_localeCompareEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QQmlLocale::method_localeCompare(a0, thisObject, argv, argc);
}

//  QQmlLocale::~QQmlLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlLocaleD1Ev(QQmlLocale *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_locale)
