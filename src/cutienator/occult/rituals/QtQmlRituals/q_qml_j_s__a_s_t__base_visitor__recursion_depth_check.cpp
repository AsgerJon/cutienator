//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJS::AST::BaseVisitor::RecursionDepthCheck::RecursionDepthCheck(BaseVi
//      sitor *visitor)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::BaseVisitor::RecursionDepthCheck *ritual_ZN6QQmlJS3AST11BaseVisitor19RecursionDepthCheckC1EPS1_(
    QQmlJS::AST::BaseVisitor *visitor) {
  return new QQmlJS::AST::BaseVisitor::RecursionDepthCheck(visitor);
}

//  QQmlJS::AST::BaseVisitor::RecursionDepthCheck::~RecursionDepthCheck()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor19RecursionDepthCheckD1Ev(
    QQmlJS::AST::BaseVisitor::RecursionDepthCheck *self) {
  delete self;
}

//  bool QQmlJS::AST::BaseVisitor::RecursionDepthCheck::operator()() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST11BaseVisitor19RecursionDepthCheckclEv(
    const QQmlJS::AST::BaseVisitor::RecursionDepthCheck *self) {
  return self->operator()();
}
