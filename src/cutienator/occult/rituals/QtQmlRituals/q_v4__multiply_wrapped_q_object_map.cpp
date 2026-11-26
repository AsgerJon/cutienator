//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  8. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qjsmanagedvalue_p.h>
#include <QtQml/private/qqmlbinding_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlobjectorgadget_p.h>
#include <QtQml/private/qqmlpropertybinding_p.h>
#include <QtQml/private/qqmlscriptstring_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4jsonobject_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4regexpobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qqueue.h>
#include <QtCore/qtimer.h>
#include <QtCore/qtypes.h>
#include <QtCore/qvarlengtharray.h>
#include <vector>
#if QT_CONFIG(qml_itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4qobjectwrapper.cpp, line 2913, as _ZN3QV425MultiplyWrappedQObjectMap21removeDestroyedObjectEP7QObject
namespace QV4 {
using namespace Qt::StringLiterals;
inline void MultiplyWrappedQObjectMap::removeDestroyedObject(QObject *object)
{
    QHash<QObjectBiPointer, WeakValue>::remove(object);
    QHash<QObjectBiPointer, WeakValue>::remove(static_cast<const QObject *>(object));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4qobjectwrapper.cpp, line 2904, as _ZN3QV425MultiplyWrappedQObjectMap5eraseEN5QHashI10QBiPointerI7QObjectKS3_ENS_9WeakValueEE8iteratorE
namespace QV4 {
using namespace Qt::StringLiterals;
inline MultiplyWrappedQObjectMap::Iterator MultiplyWrappedQObjectMap::erase(
        MultiplyWrappedQObjectMap::Iterator it)
{
    const QObjectBiPointer key = it.key();
    const QObject *obj = key.isT1() ? key.asT1() : key.asT2();
    disconnect(obj, &QObject::destroyed, this, &MultiplyWrappedQObjectMap::removeDestroyedObject);
    return QHash<QObjectBiPointer, WeakValue>::erase(it);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const QMetaObject *QV4::MultiplyWrappedQObjectMap::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV425MultiplyWrappedQObjectMap10metaObjectEv(
    const QV4::MultiplyWrappedQObjectMap *self) {
  return self->metaObject();
}

//  void *QV4::MultiplyWrappedQObjectMap::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN3QV425MultiplyWrappedQObjectMap11qt_metacastEPKc(
    QV4::MultiplyWrappedQObjectMap *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QV4::MultiplyWrappedQObjectMap::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV425MultiplyWrappedQObjectMap11qt_metacallEN11QMetaObject4CallEiPPv(
    QV4::MultiplyWrappedQObjectMap *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  ConstIterator QV4::MultiplyWrappedQObjectMap::begin() const
extern "C" Q_DECL_EXPORT
QV4::MultiplyWrappedQObjectMap::ConstIterator *ritual_ZNK3QV425MultiplyWrappedQObjectMap5beginEv(
    const QV4::MultiplyWrappedQObjectMap *self) {
  return new QV4::MultiplyWrappedQObjectMap::ConstIterator(self->begin());
}

//  Iterator QV4::MultiplyWrappedQObjectMap::begin()
extern "C" Q_DECL_EXPORT
QV4::MultiplyWrappedQObjectMap::Iterator *ritual_ZN3QV425MultiplyWrappedQObjectMap5beginEv(
    QV4::MultiplyWrappedQObjectMap *self) {
  return new QV4::MultiplyWrappedQObjectMap::Iterator(self->begin());
}

//  ConstIterator QV4::MultiplyWrappedQObjectMap::end() const
extern "C" Q_DECL_EXPORT
QV4::MultiplyWrappedQObjectMap::ConstIterator *ritual_ZNK3QV425MultiplyWrappedQObjectMap3endEv(
    const QV4::MultiplyWrappedQObjectMap *self) {
  return new QV4::MultiplyWrappedQObjectMap::ConstIterator(self->end());
}

//  Iterator QV4::MultiplyWrappedQObjectMap::end()
extern "C" Q_DECL_EXPORT
QV4::MultiplyWrappedQObjectMap::Iterator *ritual_ZN3QV425MultiplyWrappedQObjectMap3endEv(
    QV4::MultiplyWrappedQObjectMap *self) {
  return new QV4::MultiplyWrappedQObjectMap::Iterator(self->end());
}

//  Iterator QV4::MultiplyWrappedQObjectMap::erase(Iterator it)
extern "C" Q_DECL_EXPORT
QV4::MultiplyWrappedQObjectMap::Iterator *ritual_ZN3QV425MultiplyWrappedQObjectMap5eraseEN5QHashI10QBiPointerI7QObjectKS3_ENS_9WeakValueEE8iteratorE(
    QV4::MultiplyWrappedQObjectMap *self,
    const QV4::MultiplyWrappedQObjectMap::Iterator *it) {
  return new QV4::MultiplyWrappedQObjectMap::Iterator(self->erase(*it));
}

//  void QV4::MultiplyWrappedQObjectMap::removeDestroyedObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425MultiplyWrappedQObjectMap21removeDestroyedObjectEP7QObject(
    QV4::MultiplyWrappedQObjectMap *self,
    QObject *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QV4::MultiplyWrappedQObjectMap")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeDestroyedObject(QObject *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeDestroyedObject(QObject *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a QV4::MultiplyWrappedQObjectMap::ConstIterator a ritual of
//      QV4::MultiplyWrappedQObjectMap gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_MultiplyWrappedQObjectMap__QV4_MultiplyWrappedQObjectMap_ConstIterator(
    QV4::MultiplyWrappedQObjectMap::ConstIterator *self) {
  delete self;
}

//  a QV4::MultiplyWrappedQObjectMap::Iterator a ritual of
//      QV4::MultiplyWrappedQObjectMap gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_MultiplyWrappedQObjectMap__QV4_MultiplyWrappedQObjectMap_Iterator(
    QV4::MultiplyWrappedQObjectMap::Iterator *self) {
  delete self;
}


//  void QV4::MultiplyWrappedQObjectMap::insert<QObject *>(QObject * key,
//      Heap::Object *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425MultiplyWrappedQObjectMap6insertIP7QObjectEEvT_PNS_4Heap6ObjectE(
    QV4::MultiplyWrappedQObjectMap *self, QObject *key,
    QV4::Heap::Object *value) {
  self->insert<QObject *>(key, value);
}

//  ReturnedValue QV4::MultiplyWrappedQObjectMap::value<QObject *>(QObject *
//      key) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV425MultiplyWrappedQObjectMap5valueIP7QObjectEEyT_(
    const QV4::MultiplyWrappedQObjectMap *self, QObject *key) {
  return self->value<QObject *>(key);
}

//  void QV4::MultiplyWrappedQObjectMap::remove<QObject *>(QObject * key)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425MultiplyWrappedQObjectMap6removeIP7QObjectEEvT_(
    QV4::MultiplyWrappedQObjectMap *self, QObject *key) {
  self->remove<QObject *>(key);
}

//  void QV4::MultiplyWrappedQObjectMap::mark<QObject *>(QObject * key,
//      MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425MultiplyWrappedQObjectMap4markIP7QObjectEEvT_PNS_9MarkStackE(
    QV4::MultiplyWrappedQObjectMap *self, QObject *key,
    QV4::MarkStack *markStack) {
  self->mark<QObject *>(key, markStack);
}

//  void QV4::MultiplyWrappedQObjectMap::insert<const QObject *>(const
//      QObject * key, Heap::Object *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425MultiplyWrappedQObjectMap6insertIPK7QObjectEEvT_PNS_4Heap6ObjectE(
    QV4::MultiplyWrappedQObjectMap *self, const QObject *key,
    QV4::Heap::Object *value) {
  self->insert<const QObject *>(key, value);
}

//  ReturnedValue QV4::MultiplyWrappedQObjectMap::value<const QObject
//      *>(const QObject * key) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV425MultiplyWrappedQObjectMap5valueIPK7QObjectEEyT_(
    const QV4::MultiplyWrappedQObjectMap *self, const QObject *key) {
  return self->value<const QObject *>(key);
}

//  void QV4::MultiplyWrappedQObjectMap::remove<const QObject *>(const
//      QObject * key)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425MultiplyWrappedQObjectMap6removeIPK7QObjectEEvT_(
    QV4::MultiplyWrappedQObjectMap *self, const QObject *key) {
  self->remove<const QObject *>(key);
}

//  void QV4::MultiplyWrappedQObjectMap::mark<const QObject *>(const QObject
//      * key, MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425MultiplyWrappedQObjectMap4markIPK7QObjectEEvT_PNS_9MarkStackE(
    QV4::MultiplyWrappedQObjectMap *self, const QObject *key,
    QV4::MarkStack *markStack) {
  self->mark<const QObject *>(key, markStack);
}
