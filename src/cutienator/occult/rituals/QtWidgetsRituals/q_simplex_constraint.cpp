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
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qsimplex_p.h>
#include <QtCore/qset.h>
#include <QtCore/qdebug.h>
#include <stdlib.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/graphicsview/qsimplex_p.cpp, line 621, as _ZN18QSimplexConstraint6invertEv
inline void QSimplexConstraint::invert()
{
    constant = -constant;
    ratio = Ratio(2 - ratio);

    for (auto iter = variables.begin(); iter != variables.end(); ++iter)
        iter.value() = -iter.value();
}
//  -----------------------------------------------------------------------

//  QSimplexConstraint::QSimplexConstraint()
extern "C" Q_DECL_EXPORT
QSimplexConstraint *ritual_ZN18QSimplexConstraintC1Ev() {
  return new QSimplexConstraint();
}

//  void QSimplexConstraint::invert()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSimplexConstraint6invertEv(QSimplexConstraint *self) {
  self->invert();
}

//  bool QSimplexConstraint::isSatisfied()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSimplexConstraint11isSatisfiedEv(QSimplexConstraint *self) {
  return self->isSatisfied();
}

#if defined(QT_DEBUG)
//  QString QSimplexConstraint::toString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QSimplexConstraint8toStringEv(QSimplexConstraint *self) {
  return new QString(self->toString());
}
#endif  // defined(QT_DEBUG)

//  QList<QSimplexConstraint *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSimplexConstraint *> *ritual_list_make_QSimplexConstraint_ptr() {
  return new QList<QSimplexConstraint *>();
}

//  void QList<QSimplexConstraint *>::append(const QSimplexConstraint *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSimplexConstraint_ptr(
    QList<QSimplexConstraint *> *self,
    QSimplexConstraint *element) {
  self->append(element);
}

//  qsizetype QList<QSimplexConstraint *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSimplexConstraint_ptr(
    const QList<QSimplexConstraint *> *self) {
  return self->size();
}

//  const QSimplexConstraint * &QList<QSimplexConstraint *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QSimplexConstraint *ritual_list_at_QSimplexConstraint_ptr(
    const QList<QSimplexConstraint *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSimplexConstraint *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSimplexConstraint_ptr(
    QList<QSimplexConstraint *> *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
