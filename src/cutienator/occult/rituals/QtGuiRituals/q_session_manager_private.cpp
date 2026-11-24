//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qsessionmanager_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_SESSIONMANAGER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qsessionmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSessionManagerPrivate::QSessionManagerPrivate(const QString &id, const
//      QString &key)
extern "C" Q_DECL_EXPORT
QSessionManagerPrivate *ritual_ZN22QSessionManagerPrivateC1ERK7QStringS2_(
    const QString *id,
    const QString *key) {
  return new QSessionManagerPrivate(*id, *key);
}

//  QSessionManagerPrivate::~QSessionManagerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSessionManagerPrivateD1Ev(QSessionManagerPrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_SESSIONMANAGER)
