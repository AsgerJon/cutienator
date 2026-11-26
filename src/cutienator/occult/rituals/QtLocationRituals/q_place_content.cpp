//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacecontent.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplacecontent.h>
#include <QtCore/qvariant.h>
#include <QtLocation/qplacesupplier.h>
#include <QtLocation/qplaceuser.h>
#include <QtCore/qstring.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QList>
#include <QtLocation/QPlaceContent>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacecontent.h>
#include <QtLocation/private/qplacecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacecontent.cpp, line 10, as _ZN13QPlaceContent6d_funcEv
inline QPlaceContentPrivate *QPlaceContent::d_func()
{
    return d_ptr.data();
}

//  from ../qtlocation/src/location/places/qplacecontent.cpp, line 15, as _ZNK13QPlaceContent6d_funcEv
inline const QPlaceContentPrivate *QPlaceContent::d_func() const
{
    return d_ptr.constData();
}
//  -----------------------------------------------------------------------

//  QPlaceContent::QPlaceContent(Type type)
extern "C" Q_DECL_EXPORT
QPlaceContent *ritual_ZN13QPlaceContentC1ENS_4TypeE(
    QPlaceContent::Type type) {
  return new QPlaceContent(type);
}

//  QPlaceContent::~QPlaceContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceContentD1Ev(QPlaceContent *self) {
  delete self;
}

//  QPlaceContent::QPlaceContent(const QPlaceContent &other)
extern "C" Q_DECL_EXPORT
QPlaceContent *ritual_ZN13QPlaceContentC1ERKS_(const QPlaceContent *other) {
  return new QPlaceContent(*other);
}

//  QPlaceContent &QPlaceContent::operator=(const QPlaceContent &other)
extern "C" Q_DECL_EXPORT
QPlaceContent *ritual_ZN13QPlaceContentaSERKS_(
    QPlaceContent *self,
    const QPlaceContent *other) {
  return &(self->operator=(*other));
}

//  QPlaceContent::QPlaceContent(QPlaceContent &&other)
extern "C" Q_DECL_EXPORT
QPlaceContent *ritual_ZN13QPlaceContentC1EOS_(QPlaceContent *other) {
  return new QPlaceContent(std::move(*other));
}

//  QPlaceContent &QPlaceContent::operator=(QPlaceContent &&other)
extern "C" Q_DECL_EXPORT
QPlaceContent *ritual_ZN13QPlaceContentaSEOS_(
    QPlaceContent *self,
    QPlaceContent *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPlaceContent::swap(QPlaceContent &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceContent4swapERS_(
    QPlaceContent *self,
    QPlaceContent *other) {
  self->swap(*other);
}

//  void QPlaceContent::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceContent6detachEv(QPlaceContent *self) {
  self->detach();
}

//  bool QPlaceContent::operator==(const QPlaceContent &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlaceContenteqERKS_(
    const QPlaceContent *self,
    const QPlaceContent *other) {
  return self->operator==(*other);
}

//  bool QPlaceContent::operator!=(const QPlaceContent &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlaceContentneERKS_(
    const QPlaceContent *self,
    const QPlaceContent *other) {
  return self->operator!=(*other);
}

//  QPlaceContent::Type QPlaceContent::type() const
extern "C" Q_DECL_EXPORT
QPlaceContent::Type ritual_ZNK13QPlaceContent4typeEv(
    const QPlaceContent *self) {
  return self->type();
}

//  QList<DataTag> QPlaceContent::dataTags() const
extern "C" Q_DECL_EXPORT
QList<QPlaceContent::DataTag> *ritual_ZNK13QPlaceContent8dataTagsEv(
    const QPlaceContent *self) {
  return new QList<QPlaceContent::DataTag>(self->dataTags());
}

//  QVariant QPlaceContent::value(DataTag tag) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QPlaceContent5valueENS_7DataTagE(
    const QPlaceContent *self,
    QPlaceContent::DataTag tag) {
  return new QVariant(self->value(tag));
}

//  void QPlaceContent::setValue(DataTag tag, const QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceContent8setValueENS_7DataTagERK8QVariant(
    QPlaceContent *self,
    QPlaceContent::DataTag tag,
    const QVariant *a1) {
  self->setValue(tag, *a1);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QPlaceSupplier QPlaceContent::supplier() const
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_ZNK13QPlaceContent8supplierEv(
    const QPlaceContent *self) {
  return new QPlaceSupplier(self->supplier());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QPlaceContent::setSupplier(const QPlaceSupplier &supplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceContent11setSupplierERK14QPlaceSupplier(
    QPlaceContent *self,
    const QPlaceSupplier *supplier) {
  self->setSupplier(*supplier);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPlaceUser QPlaceContent::user() const
extern "C" Q_DECL_EXPORT
QPlaceUser *ritual_ZNK13QPlaceContent4userEv(const QPlaceContent *self) {
  return new QPlaceUser(self->user());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QPlaceContent::setUser(const QPlaceUser &user)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceContent7setUserERK10QPlaceUser(
    QPlaceContent *self,
    const QPlaceUser *user) {
  self->setUser(*user);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QString QPlaceContent::attribution() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPlaceContent11attributionEv(
    const QPlaceContent *self) {
  return new QString(self->attribution());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QPlaceContent::setAttribution(const QString &attribution)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceContent14setAttributionERK7QString(
    QPlaceContent *self,
    const QString *attribution) {
  self->setAttribution(*attribution);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  QPlaceContentPrivate *QPlaceContent::d_func()
extern "C" Q_DECL_EXPORT
QPlaceContentPrivate *ritual_ZN13QPlaceContent6d_funcEv(
    QPlaceContent *self) {
  return self->d_func();
}

//  const QPlaceContentPrivate *QPlaceContent::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceContentPrivate *ritual_ZNK13QPlaceContent6d_funcEv(
    const QPlaceContent *self) {
  return self->d_func();
}

//  QMap<int, QPlaceContent>: QMap<int, QPlaceContent>()
extern "C" Q_DECL_EXPORT
QMap<int, QPlaceContent> *ritual_map_make_QMap_int_QPlaceContent() {
  return new QMap<int, QPlaceContent>();
}

//  QMap<int, QPlaceContent>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QMap_int_QPlaceContent(
    QMap<int, QPlaceContent> *self,
    int key,
    const QPlaceContent *value) {
  self->insert(key, *value);
}

//  QMap<int, QPlaceContent>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QMap_int_QPlaceContent(
    const QMap<int, QPlaceContent> *self) {
  return self->size();
}

//  QMap<int, QPlaceContent>: the key at a place
extern "C" Q_DECL_EXPORT
int ritual_map_key_QMap_int_QPlaceContent(
    const QMap<int, QPlaceContent> *self,
    long long index) {
  return *std::next(self->keyBegin(), index);
}

//  QMap<int, QPlaceContent>: the value at a place
extern "C" Q_DECL_EXPORT
QPlaceContent *ritual_map_value_QMap_int_QPlaceContent(
    const QMap<int, QPlaceContent> *self,
    long long index) {
  return new QPlaceContent(*std::next(self->constBegin(), index));
}

//  QMap<int, QPlaceContent>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QMap_int_QPlaceContent(
    const QMap<int, QPlaceContent> *self,
    int key) {
  return self->contains(key);
}

//  QMap<int, QPlaceContent>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QPlaceContent *ritual_map_get_QMap_int_QPlaceContent(
    const QMap<int, QPlaceContent> *self,
    int key) {
  return new QPlaceContent(self->value(key));
}

//  QMap<int, QPlaceContent>: ~QMap()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QMap_int_QPlaceContent(QMap<int, QPlaceContent> *self) {
  delete self;
}

//  a QList<QPlaceContent::DataTag> a ritual of QPlaceContent gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlaceContent__QList_QPlaceContent_DataTag(
    QList<QPlaceContent::DataTag> *self) {
  delete self;
}
