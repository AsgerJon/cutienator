//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qremoteobjectabstractitemmodeladapter_p.h"
#include <QtCore/qitemselectionmodel.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 85, as _ZNK31QAbstractItemModelSourceAdapter14selectionModelEv
inline QItemSelectionModel* QAbstractItemModelSourceAdapter::selectionModel() const
{
    return m_selectionModel;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QAbstractItemModelSourceAdapter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QAbstractItemModelSourceAdapter10metaObjectEv(
    const QAbstractItemModelSourceAdapter *self) {
  return self->metaObject();
}

//  QItemSelectionModel *QAbstractItemModelSourceAdapter::selectionModel()
//      const
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZNK31QAbstractItemModelSourceAdapter14selectionModelEv(
    const QAbstractItemModelSourceAdapter *self) {
  return self->selectionModel();
}

//  QIntHash QAbstractItemModelSourceAdapter::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK31QAbstractItemModelSourceAdapter9roleNamesEv(
    const QAbstractItemModelSourceAdapter *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}
