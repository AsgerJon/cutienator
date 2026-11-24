//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QByteArray QQsbCollection::EntryDesc::generateSha() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QQsbCollection9EntryDesc11generateShaEv(
    const QQsbCollection::EntryDesc *self) {
  return new QByteArray(self->generateSha());
}

//  QQsbCollection::EntryDesc::~EntryDesc()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQsbCollection9EntryDescD1Ev(
    QQsbCollection::EntryDesc *self) {
  delete self;
}
