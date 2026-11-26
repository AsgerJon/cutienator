//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlobjectorgadget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlobjectorgadget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlobjectorgadget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlobjectorgadget.cpp, line 9, as _ZNK18QQmlObjectOrGadget8metacallEN11QMetaObject4CallEiPPv
inline void QQmlObjectOrGadget::metacall(QMetaObject::Call type, int index, void **argv) const
{
    if (ptr.isNull()) {
        _m->d.static_metacall(nullptr, type, index, argv);
    }
    else if (ptr.isT1()) {
        QMetaObject::metacall(ptr.asT1(), type, index, argv);
    }
    else {
        const QMetaObject *metaObject = _m;
        QQmlMetaObject::resolveGadgetMethodOrPropertyIndex(type, &metaObject, &index);
        metaObject->d.static_metacall(reinterpret_cast<QObject*>(ptr.asT2()), type, index, argv);
    }
}
//  -----------------------------------------------------------------------

//  QQmlObjectOrGadget::QQmlObjectOrGadget(QObject *obj)
extern "C" Q_DECL_EXPORT
QQmlObjectOrGadget *ritual_ZN18QQmlObjectOrGadgetC1EP7QObject(QObject *obj) {
  return new QQmlObjectOrGadget(obj);
}

//  QQmlObjectOrGadget::QQmlObjectOrGadget(const QMetaObject *metaObject,
//      void *gadget)
extern "C" Q_DECL_EXPORT
QQmlObjectOrGadget *ritual_ZN18QQmlObjectOrGadgetC1EPK11QMetaObjectPv(
    const QMetaObject *metaObject,
    void *gadget) {
  return new QQmlObjectOrGadget(metaObject, gadget);
}

//  QQmlObjectOrGadget::QQmlObjectOrGadget(const QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
QQmlObjectOrGadget *ritual_ZN18QQmlObjectOrGadgetC1EPK11QMetaObject(
    const QMetaObject *metaObject) {
  return new QQmlObjectOrGadget(metaObject);
}

//  void QQmlObjectOrGadget::metacall(QMetaObject::Call type, int index, void
//      **argv) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QQmlObjectOrGadget8metacallEN11QMetaObject4CallEiPPv(
    const QQmlObjectOrGadget *self,
    QMetaObject::Call type,
    int index,
    void **argv) {
  self->metacall(type, index, argv);
}

//  bool QQmlObjectOrGadget::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlObjectOrGadget6isNullEv(
    const QQmlObjectOrGadget *self) {
  return self->isNull();
}

//  QObject *QQmlObjectOrGadget::qObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQmlObjectOrGadget7qObjectEv(
    const QQmlObjectOrGadget *self) {
  return self->qObject();
}

//  QQmlObjectOrGadget::~QQmlObjectOrGadget()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlObjectOrGadgetD1Ev(QQmlObjectOrGadget *self) {
  delete self;
}
