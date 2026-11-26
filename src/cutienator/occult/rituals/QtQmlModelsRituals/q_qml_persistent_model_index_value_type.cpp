//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlmodelindexvaluetype_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_itemmodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlmodelindexvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmlmodelindexvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmlmodelindexvaluetype.cpp, line 12, as _ZN23QQmlModelIndexValueType16propertiesStringERK11QModelIndex
inline QString QQmlModelIndexValueType::propertiesString(const QModelIndex &idx)
{
    if (!idx.isValid())
        return QLatin1String("()");
    return QString(QLatin1String("(%1,%2,0x%3,%4(0x%5))"))
            .arg(idx.row()).arg(idx.column()).arg(idx.internalId(), 0, 16)
            .arg(QLatin1String(idx.model()->metaObject()->className())).arg(quintptr(idx.model()), 0, 16);
}
//  -----------------------------------------------------------------------

//  void QQmlPersistentModelIndexValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQmlPersistentModelIndexValueType22qt_qmlMarker_anonymousEv(
    QQmlPersistentModelIndexValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQmlPersistentModelIndexValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQmlPersistentModelIndexValueType21qt_qmlMarker_extendedEv(
    QQmlPersistentModelIndexValueType *self) {
  self->qt_qmlMarker_extended();
}

//  void QQmlPersistentModelIndexValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQmlPersistentModelIndexValueType20qt_qmlMarker_foreignEv(
    QQmlPersistentModelIndexValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  QString QQmlPersistentModelIndexValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QQmlPersistentModelIndexValueType8toStringEv(
    const QQmlPersistentModelIndexValueType *self) {
  return new QString(self->toString());
}

//  QVariant QQmlPersistentModelIndexValueType::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QQmlPersistentModelIndexValueType4dataEi(
    const QQmlPersistentModelIndexValueType *self,
    int role) {
  return new QVariant(self->data(role));
}

//  int QQmlPersistentModelIndexValueType::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QQmlPersistentModelIndexValueType3rowEv(
    const QQmlPersistentModelIndexValueType *self) {
  return self->row();
}

//  int QQmlPersistentModelIndexValueType::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QQmlPersistentModelIndexValueType6columnEv(
    const QQmlPersistentModelIndexValueType *self) {
  return self->column();
}

//  QModelIndex QQmlPersistentModelIndexValueType::parent() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK33QQmlPersistentModelIndexValueType6parentEv(
    const QQmlPersistentModelIndexValueType *self) {
  return new QModelIndex(self->parent());
}

//  bool QQmlPersistentModelIndexValueType::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QQmlPersistentModelIndexValueType7isValidEv(
    const QQmlPersistentModelIndexValueType *self) {
  return self->isValid();
}

//  QAbstractItemModel *QQmlPersistentModelIndexValueType::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK33QQmlPersistentModelIndexValueType5modelEv(
    const QQmlPersistentModelIndexValueType *self) {
  return self->model();
}

//  quint64 QQmlPersistentModelIndexValueType::internalId() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK33QQmlPersistentModelIndexValueType10internalIdEv(
    const QQmlPersistentModelIndexValueType *self) {
  return self->internalId();
}

//  QPersistentModelIndex QQmlPersistentModelIndexValueType::operator
//      QPersistentModelIndex() const
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZNK33QQmlPersistentModelIndexValueTypecv21QPersistentModelIndexEv(
    const QQmlPersistentModelIndexValueType *self) {
  return new QPersistentModelIndex(self->operator QPersistentModelIndex());
}

//  QQmlPersistentModelIndexValueType::~QQmlPersistentModelIndexValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQmlPersistentModelIndexValueTypeD1Ev(
    QQmlPersistentModelIndexValueType *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_itemmodel)
