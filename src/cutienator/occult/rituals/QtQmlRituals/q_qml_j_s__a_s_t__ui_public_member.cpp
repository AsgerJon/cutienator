//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJS::AST::UiPublicMember::UiPublicMember(UiQualifiedId *memberType,
//      QStringView name)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::UiPublicMember *ritual_ZN6QQmlJS3AST14UiPublicMemberC1EPNS0_13UiQualifiedIdE11QStringView(
    QQmlJS::MemoryPool *pool,
    QQmlJS::AST::UiQualifiedId *memberType,
    const QString *name) {
  return new (pool) QQmlJS::AST::UiPublicMember(
      memberType,
      QStringView(*name));
}

//  QQmlJS::AST::UiPublicMember::UiPublicMember(UiQualifiedId *memberType,
//      QStringView name, Statement *statement)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::UiPublicMember *ritual_ZN6QQmlJS3AST14UiPublicMemberC1EPNS0_13UiQualifiedIdE11QStringViewPNS0_9StatementE(
    QQmlJS::MemoryPool *pool,
    QQmlJS::AST::UiQualifiedId *memberType,
    const QString *name,
    QQmlJS::AST::Statement *statement) {
  return new (pool) QQmlJS::AST::UiPublicMember(
      memberType,
      QStringView(*name),
      statement);
}

//  void QQmlJS::AST::UiPublicMember::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST14UiPublicMember7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::UiPublicMember *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept0(visitor);
}

//  SourceLocation QQmlJS::AST::UiPublicMember::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember19firstSourceLocationEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::UiPublicMember::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember18lastSourceLocationEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  SourceLocation QQmlJS::AST::UiPublicMember::defaultToken() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember12defaultTokenEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->defaultToken());
}

//  bool QQmlJS::AST::UiPublicMember::isDefaultMember() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14UiPublicMember15isDefaultMemberEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return self->isDefaultMember();
}

//  SourceLocation QQmlJS::AST::UiPublicMember::requiredToken() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember13requiredTokenEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->requiredToken());
}

//  bool QQmlJS::AST::UiPublicMember::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14UiPublicMember10isRequiredEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return self->isRequired();
}

//  SourceLocation QQmlJS::AST::UiPublicMember::readonlyToken() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember13readonlyTokenEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->readonlyToken());
}

//  bool QQmlJS::AST::UiPublicMember::isReadonly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14UiPublicMember10isReadonlyEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return self->isReadonly();
}

//  SourceLocation QQmlJS::AST::UiPublicMember::finalToken() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember10finalTokenEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->finalToken());
}

//  bool QQmlJS::AST::UiPublicMember::isFinal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14UiPublicMember7isFinalEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return self->isFinal();
}

//  SourceLocation QQmlJS::AST::UiPublicMember::overrideToken() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember13overrideTokenEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->overrideToken());
}

//  bool QQmlJS::AST::UiPublicMember::isOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14UiPublicMember10isOverrideEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return self->isOverride();
}

//  SourceLocation QQmlJS::AST::UiPublicMember::virtualToken() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember12virtualTokenEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->virtualToken());
}

//  bool QQmlJS::AST::UiPublicMember::isVirtual() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14UiPublicMember9isVirtualEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return self->isVirtual();
}

//  void QQmlJS::AST::UiPublicMember::setAttributes(UiPropertyAttributes
//      *attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST14UiPublicMember13setAttributesEPNS0_20UiPropertyAttributesE(
    QQmlJS::AST::UiPublicMember *self,
    QQmlJS::AST::UiPropertyAttributes *attributes) {
  self->setAttributes(attributes);
}

//  SourceLocation QQmlJS::AST::UiPublicMember::propertyToken() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiPublicMember13propertyTokenEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(self->propertyToken());
}

//  void QQmlJS::AST::UiPublicMember::setPropertyToken(SourceLocation token)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST14UiPublicMember16setPropertyTokenENS_14SourceLocationE(
    QQmlJS::AST::UiPublicMember *self,
    const QQmlJS::SourceLocation *token) {
  self->setPropertyToken(*token);
}

//  void QQmlJS::AST::UiPublicMember::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST14UiPublicMember7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::UiPublicMember *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::UiPublicMember::accept0(visitor);
}

//  SourceLocation QQmlJS::AST::UiPublicMember::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST14UiPublicMember19firstSourceLocationEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::UiPublicMember::firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::UiPublicMember::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST14UiPublicMember18lastSourceLocationEv(
    const QQmlJS::AST::UiPublicMember *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::UiPublicMember::lastSourceLocation());
}
