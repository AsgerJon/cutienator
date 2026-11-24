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
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
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

//  from ../qtdeclarative/src/qmlmodels/qqmlmodelindexvaluetype.cpp, line 24, as _ZNK31QQmlItemSelectionRangeValueType8toStringEv
inline QString QQmlItemSelectionRangeValueType::toString() const
{
    return QString(QLatin1String("QItemSelectionRange(%1,%2)"))
            .arg(reinterpret_cast<const QQmlPersistentModelIndexValueType *>(&v.topLeft())->toString())
            .arg(reinterpret_cast<const QQmlPersistentModelIndexValueType *>(&v.bottomRight())->toString());
}
//  -----------------------------------------------------------------------

//  void QQmlItemSelectionRangeValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlItemSelectionRangeValueType22qt_qmlMarker_anonymousEv(
    QQmlItemSelectionRangeValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQmlItemSelectionRangeValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlItemSelectionRangeValueType21qt_qmlMarker_extendedEv(
    QQmlItemSelectionRangeValueType *self) {
  self->qt_qmlMarker_extended();
}

//  void QQmlItemSelectionRangeValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlItemSelectionRangeValueType20qt_qmlMarker_foreignEv(
    QQmlItemSelectionRangeValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  QString QQmlItemSelectionRangeValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQmlItemSelectionRangeValueType8toStringEv(
    const QQmlItemSelectionRangeValueType *self) {
  return new QString(self->toString());
}

//  bool QQmlItemSelectionRangeValueType::contains(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlItemSelectionRangeValueType8containsERK11QModelIndex(
    const QQmlItemSelectionRangeValueType *self,
    const QModelIndex *index) {
  return self->contains(*index);
}

//  bool QQmlItemSelectionRangeValueType::contains(int row, int column, const
//      QModelIndex &parentIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlItemSelectionRangeValueType8containsEiiRK11QModelIndex(
    const QQmlItemSelectionRangeValueType *self,
    int row,
    int column,
    const QModelIndex *parentIndex) {
  return self->contains(row, column, *parentIndex);
}

//  bool QQmlItemSelectionRangeValueType::intersects(const
//      QItemSelectionRange &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlItemSelectionRangeValueType10intersectsERK19QItemSelectionRange(
    const QQmlItemSelectionRangeValueType *self,
    const QItemSelectionRange *other) {
  return self->intersects(*other);
}

//  QItemSelectionRange QQmlItemSelectionRangeValueType::intersected(const
//      QItemSelectionRange &other) const
extern "C" Q_DECL_EXPORT
QItemSelectionRange *ritual_ZNK31QQmlItemSelectionRangeValueType11intersectedERK19QItemSelectionRange(
    const QQmlItemSelectionRangeValueType *self,
    const QItemSelectionRange *other) {
  return new QItemSelectionRange(self->intersected(*other));
}

//  int QQmlItemSelectionRangeValueType::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQmlItemSelectionRangeValueType3topEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->top();
}

//  int QQmlItemSelectionRangeValueType::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQmlItemSelectionRangeValueType4leftEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->left();
}

//  int QQmlItemSelectionRangeValueType::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQmlItemSelectionRangeValueType6bottomEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->bottom();
}

//  int QQmlItemSelectionRangeValueType::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQmlItemSelectionRangeValueType5rightEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->right();
}

//  int QQmlItemSelectionRangeValueType::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQmlItemSelectionRangeValueType5widthEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->width();
}

//  int QQmlItemSelectionRangeValueType::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQmlItemSelectionRangeValueType6heightEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->height();
}

//  QModelIndex QQmlItemSelectionRangeValueType::parent() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK31QQmlItemSelectionRangeValueType6parentEv(
    const QQmlItemSelectionRangeValueType *self) {
  return new QModelIndex(self->parent());
}

//  QAbstractItemModel *QQmlItemSelectionRangeValueType::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK31QQmlItemSelectionRangeValueType5modelEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->model();
}

//  bool QQmlItemSelectionRangeValueType::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlItemSelectionRangeValueType7isValidEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->isValid();
}

//  bool QQmlItemSelectionRangeValueType::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQmlItemSelectionRangeValueType7isEmptyEv(
    const QQmlItemSelectionRangeValueType *self) {
  return self->isEmpty();
}

//  QItemSelectionRange QQmlItemSelectionRangeValueType::operator
//      QItemSelectionRange() const
extern "C" Q_DECL_EXPORT
QItemSelectionRange *ritual_ZNK31QQmlItemSelectionRangeValueTypecv19QItemSelectionRangeEv(
    const QQmlItemSelectionRangeValueType *self) {
  return new QItemSelectionRange(self->operator QItemSelectionRange());
}

//  QQmlItemSelectionRangeValueType::~QQmlItemSelectionRangeValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlItemSelectionRangeValueTypeD1Ev(
    QQmlItemSelectionRangeValueType *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_itemmodel)
