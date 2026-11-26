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

//  PropertyPassBuilder &QQmlSA::PropertyPassBuilder::withOnBinding(GenericPr
//      opertyPass::OnBinding onBinding)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPassBuilder *ritual_ZN6QQmlSA19PropertyPassBuilder13withOnBindingEPFvPNS_12PropertyPassERKNS_7ElementERK7QStringRKNS_7BindingES5_S5_E(
    QQmlSA::PropertyPassBuilder *self,
    void *onBinding) {
  return &(
      self->withOnBinding(
          reinterpret_cast<QQmlSA::GenericPropertyPass::OnBinding>(onBinding)));
}

//  PropertyPassBuilder
//      &QQmlSA::PropertyPassBuilder::withOnRead(GenericPropertyPass::OnRead
//      onRead)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPassBuilder *ritual_ZN6QQmlSA19PropertyPassBuilder10withOnReadEPFvPNS_12PropertyPassERKNS_7ElementERK7QStringS5_NS_14SourceLocationEE(
    QQmlSA::PropertyPassBuilder *self,
    void *onRead) {
  return &(
      self->withOnRead(
          reinterpret_cast<QQmlSA::GenericPropertyPass::OnRead>(onRead)));
}

//  PropertyPassBuilder
//      &QQmlSA::PropertyPassBuilder::withOnCall(GenericPropertyPass::OnCall
//      onCall)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPassBuilder *ritual_ZN6QQmlSA19PropertyPassBuilder10withOnCallEPFvPNS_12PropertyPassERKNS_7ElementERK7QStringS5_NS_14SourceLocationEE(
    QQmlSA::PropertyPassBuilder *self,
    void *onCall) {
  return &(
      self->withOnCall(
          reinterpret_cast<QQmlSA::GenericPropertyPass::OnCall>(onCall)));
}

//  PropertyPassBuilder
//      &QQmlSA::PropertyPassBuilder::withOnWrite(GenericPropertyPass::OnWrit
//      e onWrite)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPassBuilder *ritual_ZN6QQmlSA19PropertyPassBuilder11withOnWriteEPFvPNS_12PropertyPassERKNS_7ElementERK7QStringS5_S5_NS_14SourceLocationEE(
    QQmlSA::PropertyPassBuilder *self,
    void *onWrite) {
  return &(
      self->withOnWrite(
          reinterpret_cast<QQmlSA::GenericPropertyPass::OnWrite>(onWrite)));
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
