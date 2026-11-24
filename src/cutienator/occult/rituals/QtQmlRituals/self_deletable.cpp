//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qanimationjobutil_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qanimationjobutil_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  SelfDeletable::~SelfDeletable()
extern "C" Q_DECL_EXPORT
void ritual_ZN13SelfDeletableD1Ev(SelfDeletable *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_animation)
