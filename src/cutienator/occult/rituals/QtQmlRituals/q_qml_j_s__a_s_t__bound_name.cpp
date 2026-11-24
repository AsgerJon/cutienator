//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJS::AST::BoundName::BoundName(const QString &id, const
//      QQmlJS::SourceLocation &location, TypeAnnotation *typeAnnotation,
//      Type type)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::BoundName *ritual_ZN6QQmlJS3AST9BoundNameC1ERK7QStringRKNS_14SourceLocationEPNS0_14TypeAnnotationENS1_4TypeE(
    const QString *id,
    const QQmlJS::SourceLocation *location,
    QQmlJS::AST::TypeAnnotation *typeAnnotation,
    QQmlJS::AST::BoundName::Type type) {
  return new QQmlJS::AST::BoundName(*id, *location, typeAnnotation, type);
}

//  QQmlJS::AST::BoundName::BoundName()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::BoundName *ritual_ZN6QQmlJS3AST9BoundNameC1Ev() {
  return new QQmlJS::AST::BoundName();
}

//  bool QQmlJS::AST::BoundName::isInjected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST9BoundName10isInjectedEv(
    const QQmlJS::AST::BoundName *self) {
  return self->isInjected();
}

//  QQmlJS::AST::BoundName::~BoundName()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9BoundNameD1Ev(QQmlJS::AST::BoundName *self) {
  delete self;
}
