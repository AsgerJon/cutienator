//  Written by dev_tooling.RitualGenerator from the records of
//  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtXml/qtxmlglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(dom)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtXml/QtXml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtXml/6.12.0/QtXml/private/qdom_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#include <qdom.h>
#include "private/qxmlutils_p.h"
#if QT_CONFIG(dom)
#include "qdom_p.h"
#include "qdomhelpers_p.h"
#include <qatomic.h>
#include <qbuffer.h>
#include <qiodevice.h>
#if QT_CONFIG(regularexpression)
#include <qregularexpression.h>
#endif
#include <qtextstream.h>
#include <qvariant.h>
#include <qshareddata.h>
#include <qdebug.h>
#include <qxmlstream.h>
#include <private/qduplicatetracker_p.h>
#include <private/qstringiterator_p.h>
#include <qvarlengtharray.h>
#include <stdio.h>
#include <limits>
#include <memory>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/xml/dom/qdom.cpp, line 325, as _ZN25QDomImplementationPrivate5cloneEv
#if QT_CONFIG(dom)
inline QDomImplementationPrivate* QDomImplementationPrivate::clone()
{
    return new QDomImplementationPrivate;
}
#endif  // QT_CONFIG(dom)
//  -----------------------------------------------------------------------

//  QDomImplementationPrivate::QDomImplementationPrivate()
extern "C" Q_DECL_EXPORT
QDomImplementationPrivate *ritual_ZN25QDomImplementationPrivateC1Ev() {
  return new QDomImplementationPrivate();
}

#if QT_CONFIG(dom)
//  QDomImplementationPrivate *QDomImplementationPrivate::clone()
extern "C" Q_DECL_EXPORT
QDomImplementationPrivate *ritual_ZN25QDomImplementationPrivate5cloneEv(
    QDomImplementationPrivate *self) {
  return self->clone();
}
#endif  // QT_CONFIG(dom)

//  QDomImplementationPrivate::~QDomImplementationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDomImplementationPrivateD1Ev(
    QDomImplementationPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
