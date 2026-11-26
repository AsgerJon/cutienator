//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplaceicon_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplaceicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplaceicon.h>
#include <QtLocation/private/qplaceicon_p.h>
#include <QtLocation/qplacemanager.h>
#include <QtLocation/qplacemanagerengine.h>
#include <QtCore/QVariant>
#include <QtQml/QJSValue>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplaceicon.cpp, line 17, as _ZNK17QPlaceIconPrivateeqERKS_
inline bool QPlaceIconPrivate::operator == (const QPlaceIconPrivate &other) const
{
    return manager == other.manager
            && parameters == other.parameters;
}
//  -----------------------------------------------------------------------

//  bool QPlaceIconPrivate::operator==(const QPlaceIconPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPlaceIconPrivateeqERKS_(
    const QPlaceIconPrivate *self,
    const QPlaceIconPrivate *other) {
  return self->operator==(*other);
}

//  QPlaceIconPrivate::~QPlaceIconPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlaceIconPrivateD1Ev(QPlaceIconPrivate *self) {
  delete self;
}
