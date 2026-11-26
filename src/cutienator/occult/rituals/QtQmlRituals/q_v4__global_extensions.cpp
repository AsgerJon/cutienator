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

#if QT_CONFIG(translation)
//  ReturnedValue QV4::GlobalExtensions::method_qsTranslate(const
//      FunctionObject *b, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions18method_qsTranslateEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_qsTranslate(
      b,
      thisObject,
      argv,
      argc);
}
#endif  // QT_CONFIG(translation)

#if QT_CONFIG(translation)
//  ReturnedValue QV4::GlobalExtensions::method_qsTranslateNoOp(const
//      FunctionObject *b, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions22method_qsTranslateNoOpEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_qsTranslateNoOp(
      b,
      thisObject,
      argv,
      argc);
}
#endif  // QT_CONFIG(translation)

#if QT_CONFIG(translation)
//  ReturnedValue QV4::GlobalExtensions::method_qsTr(const FunctionObject *b,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions11method_qsTrEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_qsTr(b, thisObject, argv, argc);
}
#endif  // QT_CONFIG(translation)

#if QT_CONFIG(translation)
//  ReturnedValue QV4::GlobalExtensions::method_qsTrNoOp(const FunctionObject
//      *b, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions15method_qsTrNoOpEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_qsTrNoOp(b, thisObject, argv, argc);
}
#endif  // QT_CONFIG(translation)

#if QT_CONFIG(translation)
//  ReturnedValue QV4::GlobalExtensions::method_qsTrId(const FunctionObject
//      *b, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions13method_qsTrIdEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_qsTrId(b, thisObject, argv, argc);
}
#endif  // QT_CONFIG(translation)

#if QT_CONFIG(translation)
//  ReturnedValue QV4::GlobalExtensions::method_qsTrIdNoOp(const
//      FunctionObject *b, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions17method_qsTrIdNoOpEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_qsTrIdNoOp(b, thisObject, argv, argc);
}
#endif  // QT_CONFIG(translation)

//  ReturnedValue QV4::GlobalExtensions::method_gc(const FunctionObject *b,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions9method_gcEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_gc(b, thisObject, argv, argc);
}

//  ReturnedValue QV4::GlobalExtensions::method_string_arg(const
//      FunctionObject *b, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416GlobalExtensions17method_string_argEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::GlobalExtensions::method_string_arg(b, thisObject, argv, argc);
}

//  QV4::GlobalExtensions::~GlobalExtensions()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416GlobalExtensionsD1Ev(QV4::GlobalExtensions *self) {
  delete self;
}
