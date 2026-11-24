//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  int QQmlJS::AST::BoundNames::indexOf(const QString &name, int from) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QQmlJS3AST10BoundNames7indexOfERK7QStringi(
    const QQmlJS::AST::BoundNames *self,
    const QString *name,
    int from) {
  return self->indexOf(*name, from);
}

//  bool QQmlJS::AST::BoundNames::contains(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST10BoundNames8containsERK7QString(
    const QQmlJS::AST::BoundNames *self,
    const QString *name) {
  return self->contains(*name);
}

//  QQmlJS::AST::BoundNames::~BoundNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST10BoundNamesD1Ev(QQmlJS::AST::BoundNames *self) {
  delete self;
}
