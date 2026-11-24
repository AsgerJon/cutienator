//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscontextualtypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscontextualtypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  CompileContext QQmlJS::ContextualTypes::context() const
extern "C" Q_DECL_EXPORT
QQmlJS::ContextualTypes::CompileContext ritual_ZNK6QQmlJS15ContextualTypes7contextEv(
    const QQmlJS::ContextualTypes *self) {
  return self->context();
}

//  bool QQmlJS::ContextualTypes::hasType(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS15ContextualTypes7hasTypeERK7QString(
    const QQmlJS::ContextualTypes *self,
    const QString *name) {
  return self->hasType(*name);
}

//  ContextualType QQmlJS::ContextualTypes::type(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJS::ContextualType *ritual_ZNK6QQmlJS15ContextualTypes4typeERK7QString(
    const QQmlJS::ContextualTypes *self,
    const QString *name) {
  return new QQmlJS::ContextualType(self->type(*name));
}

//  void QQmlJS::ContextualTypes::clearType(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes9clearTypeERK7QString(
    QQmlJS::ContextualTypes *self,
    const QString *name) {
  self->clearType(*name);
}

//  bool QQmlJS::ContextualTypes::isNullType(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS15ContextualTypes10isNullTypeERK7QString(
    const QQmlJS::ContextualTypes *self,
    const QString *name) {
  return self->isNullType(*name);
}

//  bool QQmlJS::ContextualTypes::hasFileSelectors() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS15ContextualTypes16hasFileSelectorsEv(
    const QQmlJS::ContextualTypes *self) {
  return self->hasFileSelectors();
}

//  QString QQmlJS::ContextualTypes::currentFileSelector() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS15ContextualTypes19currentFileSelectorEv(
    const QQmlJS::ContextualTypes *self) {
  return new QString(self->currentFileSelector());
}

//  void QQmlJS::ContextualTypes::setCurrentFileSelector(const QString
//      &selector)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes22setCurrentFileSelectorERK7QString(
    QQmlJS::ContextualTypes *self,
    const QString *selector) {
  self->setCurrentFileSelector(*selector);
}

//  void QQmlJS::ContextualTypes::clearTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes10clearTypesEv(
    QQmlJS::ContextualTypes *self) {
  self->clearTypes();
}

//  QQmlJS::ContextualTypes::~ContextualTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypesD1Ev(QQmlJS::ContextualTypes *self) {
  delete self;
}
