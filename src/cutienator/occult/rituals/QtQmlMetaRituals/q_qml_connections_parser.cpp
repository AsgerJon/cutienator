//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlconnections_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlMeta/QtQmlMeta>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlconnections_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlConnectionsParser::verifyBindings(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &props)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlConnectionsParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE(
    QQmlConnectionsParser *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *props) {
  self->verifyBindings(*compilationUnit, *props);
}

//  void QQmlConnectionsParser::applyBindings(QObject *object, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlConnectionsParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE(
    QQmlConnectionsParser *self,
    QObject *object,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *bindings) {
  self->applyBindings(object, *compilationUnit, *bindings);
}

//  QQmlConnectionsParser::~QQmlConnectionsParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlConnectionsParserD1Ev(QQmlConnectionsParser *self) {
  delete self;
}
