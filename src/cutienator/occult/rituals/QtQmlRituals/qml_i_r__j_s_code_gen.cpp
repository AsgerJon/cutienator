//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>

//  QmlIR::JSCodeGen::JSCodeGen(Document *document,
//      QV4::Compiler::CodegenWarningInterface *iface, bool
//      storeSourceLocations)
extern "C" Q_DECL_EXPORT
QmlIR::JSCodeGen *ritual_ZN5QmlIR9JSCodeGenC1EPNS_8DocumentEPN3QV48Compiler23CodegenWarningInterfaceEb(
    QmlIR::Document *document,
    QV4::Compiler::CodegenWarningInterface *iface,
    bool storeSourceLocations) {
  return new QmlIR::JSCodeGen(document, iface, storeSourceLocations);
}

//  QList<int> QmlIR::JSCodeGen::generateJSCodeForFunctionsAndBindings(const
//      QList<CompiledFunctionOrExpression> &functions)
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZN5QmlIR9JSCodeGen37generateJSCodeForFunctionsAndBindingsERK5QListINS_28CompiledFunctionOrExpressionEE(
    QmlIR::JSCodeGen *self,
    const QList<QmlIR::CompiledFunctionOrExpression> *functions) {
  return new QList<int>(
      self->generateJSCodeForFunctionsAndBindings(
          *functions));
}

//  bool QmlIR::JSCodeGen::generateRuntimeFunctions(QmlIR::Object *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QmlIR9JSCodeGen24generateRuntimeFunctionsEPNS_6ObjectE(
    QmlIR::JSCodeGen *self,
    QmlIR::Object *object) {
  return self->generateRuntimeFunctions(object);
}

//  a QList<int> a ritual of QmlIR::JSCodeGen gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QmlIR_JSCodeGen__QList_int(QList<int> *self) {
  delete self;
}
