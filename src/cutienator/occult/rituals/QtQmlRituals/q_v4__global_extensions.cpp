//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QV4::GlobalExtensions::init(Object *globalObject,
//      QJSEngine::Extensions extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416GlobalExtensions4initEPNS_6ObjectE6QFlagsIN9QJSEngine9ExtensionEE(
    QV4::Object *globalObject,
    int extensions) {
  QV4::GlobalExtensions::init(
      globalObject,
      QFlags<QJSEngine::Extension>::fromInt(extensions));
}

#if QT_CONFIG(translation)
//  QString QV4::GlobalExtensions::currentTranslationContext(ExecutionEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV416GlobalExtensions25currentTranslationContextEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QString(
      QV4::GlobalExtensions::currentTranslationContext(
          engine));
}
#endif  // QT_CONFIG(translation)

//  QV4::GlobalExtensions::~GlobalExtensions()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416GlobalExtensionsD1Ev(QV4::GlobalExtensions *self) {
  delete self;
}
