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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  void QQmlModelIndexValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlModelIndexValueType22qt_qmlMarker_anonymousEv(
    QQmlModelIndexValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQmlModelIndexValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlModelIndexValueType21qt_qmlMarker_extendedEv(
    QQmlModelIndexValueType *self) {
  self->qt_qmlMarker_extended();
}

//  void QQmlModelIndexValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlModelIndexValueType20qt_qmlMarker_foreignEv(
    QQmlModelIndexValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  QString QQmlModelIndexValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQmlModelIndexValueType8toStringEv(
    const QQmlModelIndexValueType *self) {
  return new QString(self->toString());
}

//  QVariant QQmlModelIndexValueType::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QQmlModelIndexValueType4dataEi(
    const QQmlModelIndexValueType *self,
    int role) {
  return new QVariant(self->data(role));
}

//  int QQmlModelIndexValueType::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQmlModelIndexValueType3rowEv(
    const QQmlModelIndexValueType *self) {
  return self->row();
}

//  int QQmlModelIndexValueType::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQmlModelIndexValueType6columnEv(
    const QQmlModelIndexValueType *self) {
  return self->column();
}

//  QModelIndex QQmlModelIndexValueType::parent() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK23QQmlModelIndexValueType6parentEv(
    const QQmlModelIndexValueType *self) {
  return new QModelIndex(self->parent());
}

//  bool QQmlModelIndexValueType::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlModelIndexValueType7isValidEv(
    const QQmlModelIndexValueType *self) {
  return self->isValid();
}

//  QAbstractItemModel *QQmlModelIndexValueType::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK23QQmlModelIndexValueType5modelEv(
    const QQmlModelIndexValueType *self) {
  return self->model();
}

//  quint64 QQmlModelIndexValueType::internalId() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK23QQmlModelIndexValueType10internalIdEv(
    const QQmlModelIndexValueType *self) {
  return self->internalId();
}

//  QString QQmlModelIndexValueType::propertiesString(const QModelIndex &idx)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQmlModelIndexValueType16propertiesStringERK11QModelIndex(
    const QModelIndex *idx) {
  return new QString(QQmlModelIndexValueType::propertiesString(*idx));
}

//  QPersistentModelIndex
//      QQmlModelIndexValueType::toPersistentModelIndex(const QModelIndex
//      &index)
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZN23QQmlModelIndexValueType22toPersistentModelIndexERK11QModelIndex(
    const QModelIndex *index) {
  return new QPersistentModelIndex(
      QQmlModelIndexValueType::toPersistentModelIndex(
          *index));
}

//  QModelIndex QQmlModelIndexValueType::operator QModelIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK23QQmlModelIndexValueTypecv11QModelIndexEv(
    const QQmlModelIndexValueType *self) {
  return new QModelIndex(self->operator QModelIndex());
}

//  QQmlModelIndexValueType::~QQmlModelIndexValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlModelIndexValueTypeD1Ev(QQmlModelIndexValueType *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_itemmodel)
