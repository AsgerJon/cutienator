//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsimplex_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qsimplex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSimplexVariable::QSimplexVariable()
extern "C" Q_DECL_EXPORT
QSimplexVariable *ritual_ZN16QSimplexVariableC1Ev() {
  return new QSimplexVariable();
}

//  QSimplexVariable::~QSimplexVariable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSimplexVariableD1Ev(QSimplexVariable *self) {
  delete self;
}

//  QSimplexVariable::QSimplexVariable(const QSimplexVariable &a0)
extern "C" Q_DECL_EXPORT
QSimplexVariable *ritual_ZN16QSimplexVariableC1ERKS_(
    const QSimplexVariable *a0) {
  return new QSimplexVariable(*a0);
}

//  QSimplexVariable::QSimplexVariable(QSimplexVariable &&a0)
extern "C" Q_DECL_EXPORT
QSimplexVariable *ritual_ZN16QSimplexVariableC1EOS_(QSimplexVariable *a0) {
  return new QSimplexVariable(std::move(*a0));
}

//  QSimplexVariable &QSimplexVariable::operator=(const QSimplexVariable &a0)
extern "C" Q_DECL_EXPORT
QSimplexVariable *ritual_ZN16QSimplexVariableaSERKS_(
    QSimplexVariable *self,
    const QSimplexVariable *a0) {
  return &(self->operator=(*a0));
}

//  QSimplexVariable &QSimplexVariable::operator=(QSimplexVariable &&a0)
extern "C" Q_DECL_EXPORT
QSimplexVariable *ritual_ZN16QSimplexVariableaSEOS_(
    QSimplexVariable *self,
    QSimplexVariable *a0) {
  return &(self->operator=(std::move(*a0)));
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
