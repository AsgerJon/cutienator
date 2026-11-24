//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>

//  QQmlSA::PropertyPassBuilder::PropertyPassBuilder(PassManager
//      *passManager)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPassBuilder *ritual_ZN6QQmlSA19PropertyPassBuilderC1EPNS_11PassManagerE(
    QQmlSA::PassManager *passManager) {
  return new QQmlSA::PropertyPassBuilder(passManager);
}

//  QQmlSA::PropertyPassBuilder::~PropertyPassBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19PropertyPassBuilderD1Ev(
    QQmlSA::PropertyPassBuilder *self) {
  delete self;
}

//  void QQmlSA::PropertyPassBuilder::registerOn(QAnyStringView module,
//      QAnyStringView type, QAnyStringView property)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19PropertyPassBuilder10registerOnE14QAnyStringViewS1_S1_(
    QQmlSA::PropertyPassBuilder *self,
    const QString *module,
    const QString *type,
    const QString *property) {
  self->registerOn(
      QAnyStringView(*module),
      QAnyStringView(*type),
      QAnyStringView(*property));
}

//  void QQmlSA::PropertyPassBuilder::registerOnBuiltin(QAnyStringView type,
//      QAnyStringView property)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19PropertyPassBuilder17registerOnBuiltinE14QAnyStringViewS1_(
    QQmlSA::PropertyPassBuilder *self,
    const QString *type,
    const QString *property) {
  self->registerOnBuiltin(QAnyStringView(*type), QAnyStringView(*property));
}
