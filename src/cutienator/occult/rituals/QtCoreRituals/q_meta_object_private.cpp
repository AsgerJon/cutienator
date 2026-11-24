//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qbytearrayview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/qmetatype.h>
#include <QtCore/private/qmetatype_p.h>
#include <QtCore/qobject.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qspan.h>
#include <QtCore/qvariant.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#if QT_CONFIG(thread)
#include <QtCore/private/qlatch_p.h>
#endif
#include <QtCore/private/qmetaobject_moc_p.h>
#include <ctype.h>
#include <memory>
#include <cstring>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qmetaobject.cpp, line 4633, as _ZN18QMetaObjectPrivate13originalCloneEPK11QMetaObjecti
inline int QMetaObjectPrivate::originalClone(const QMetaObject *mobj, int local_method_index)
{
    Q_ASSERT(local_method_index < get(mobj)->methodCount);
    while (QMetaMethod::fromRelativeMethodIndex(mobj, local_method_index).data.flags() & MethodCloned) {
        Q_ASSERT(local_method_index > 0);
        --local_method_index;
    }
    return local_method_index;
}
//  -----------------------------------------------------------------------

//  const QMetaObjectPrivate *QMetaObjectPrivate::get(const QMetaObject
//      *metaobject)
extern "C" Q_DECL_EXPORT
const QMetaObjectPrivate *ritual_ZN18QMetaObjectPrivate3getEPK11QMetaObject(
    const QMetaObject *metaobject) {
  return QMetaObjectPrivate::get(metaobject);
}

//  int QMetaObjectPrivate::originalClone(const QMetaObject *obj, int
//      local_method_index)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate13originalCloneEPK11QMetaObjecti(
    const QMetaObject *obj,
    int local_method_index) {
  return QMetaObjectPrivate::originalClone(obj, local_method_index);
}

//  QMetaMethod QMetaObjectPrivate::signal(const QMetaObject *m, int
//      signal_index)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN18QMetaObjectPrivate6signalEPK11QMetaObjecti(
    const QMetaObject *m,
    int signal_index) {
  return new QMetaMethod(QMetaObjectPrivate::signal(m, signal_index));
}

//  int QMetaObjectPrivate::signalOffset(const QMetaObject *m)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate12signalOffsetEPK11QMetaObject(
    const QMetaObject *m) {
  return QMetaObjectPrivate::signalOffset(m);
}

//  int QMetaObjectPrivate::absoluteSignalCount(const QMetaObject *m)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate19absoluteSignalCountEPK11QMetaObject(
    const QMetaObject *m) {
  return QMetaObjectPrivate::absoluteSignalCount(m);
}

//  int QMetaObjectPrivate::signalIndex(const QMetaMethod &m)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate11signalIndexERK11QMetaMethod(
    const QMetaMethod *m) {
  return QMetaObjectPrivate::signalIndex(*m);
}

//  QMetaMethod QMetaObjectPrivate::firstMethod(const QMetaObject
//      *baseObject, QByteArrayView name)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN18QMetaObjectPrivate11firstMethodEPK11QMetaObject14QByteArrayView(
    const QMetaObject *baseObject,
    const QByteArrayView *name) {
  return new QMetaMethod(QMetaObjectPrivate::firstMethod(baseObject, *name));
}

//  QMetaObjectPrivate::~QMetaObjectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectPrivateD1Ev(QMetaObjectPrivate *self) {
  delete self;
}
