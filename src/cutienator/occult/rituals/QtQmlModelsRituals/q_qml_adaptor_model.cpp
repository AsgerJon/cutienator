//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qtyperevision.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmllistaccessor_p.h"
#include <private/qqmlmetatype_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetasequence.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qurl.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 25, as _ZNK16QQmlListAccessor4listEv
inline QVariant QQmlListAccessor::list() const
{
    return d;
}
//  -----------------------------------------------------------------------

//  QQmlAdaptorModel::QQmlAdaptorModel()
extern "C" Q_DECL_EXPORT
QQmlAdaptorModel *ritual_ZN16QQmlAdaptorModelC1Ev() {
  return new QQmlAdaptorModel();
}

//  QQmlAdaptorModel::~QQmlAdaptorModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModelD1Ev(QQmlAdaptorModel *self) {
  delete self;
}

//  QVariant QQmlAdaptorModel::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlAdaptorModel5modelEv(
    const QQmlAdaptorModel *self) {
  return new QVariant(self->model());
}

//  void QQmlAdaptorModel::setModel(const QVariant &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModel8setModelERK8QVariant(
    QQmlAdaptorModel *self,
    const QVariant *variant) {
  self->setModel(*variant);
}

//  void QQmlAdaptorModel::invalidateModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModel15invalidateModelEv(QQmlAdaptorModel *self) {
  self->invalidateModel();
}

//  bool QQmlAdaptorModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlAdaptorModel7isValidEv(const QQmlAdaptorModel *self) {
  return self->isValid();
}

//  int QQmlAdaptorModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel5countEv(const QQmlAdaptorModel *self) {
  return self->count();
}

//  int QQmlAdaptorModel::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel8rowCountEv(const QQmlAdaptorModel *self) {
  return self->rowCount();
}

//  int QQmlAdaptorModel::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel11columnCountEv(
    const QQmlAdaptorModel *self) {
  return self->columnCount();
}

//  int QQmlAdaptorModel::rowAt(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel5rowAtEi(
    const QQmlAdaptorModel *self,
    int index) {
  return self->rowAt(index);
}

//  int QQmlAdaptorModel::columnAt(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel8columnAtEi(
    const QQmlAdaptorModel *self,
    int index) {
  return self->columnAt(index);
}

//  int QQmlAdaptorModel::indexAt(int row, int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel7indexAtEii(
    const QQmlAdaptorModel *self,
    int row,
    int column) {
  return self->indexAt(row, column);
}

//  void QQmlAdaptorModel::useImportVersion(QTypeRevision revision)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModel16useImportVersionE13QTypeRevision(
    QQmlAdaptorModel *self,
    const QTypeRevision *revision) {
  self->useImportVersion(*revision);
}

//  bool QQmlAdaptorModel::adaptsAim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlAdaptorModel9adaptsAimEv(const QQmlAdaptorModel *self) {
  return self->adaptsAim();
}

//  QAbstractItemModel *QQmlAdaptorModel::aim()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZN16QQmlAdaptorModel3aimEv(
    QQmlAdaptorModel *self) {
  return self->aim();
}

//  const QAbstractItemModel *QQmlAdaptorModel::aim() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK16QQmlAdaptorModel3aimEv(
    const QQmlAdaptorModel *self) {
  return self->aim();
}

//  QVariant QQmlAdaptorModel::value(int index, const QString &role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlAdaptorModel5valueEiRK7QString(
    const QQmlAdaptorModel *self,
    int index,
    const QString *role) {
  return new QVariant(self->value(index, *role));
}

//  bool QQmlAdaptorModel::hasProxyObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlAdaptorModel14hasProxyObjectEv(
    const QQmlAdaptorModel *self) {
  return self->hasProxyObject();
}

//  void QQmlAdaptorModel::replaceWatchedRoles(const QList<QByteArray>
//      &oldRoles, const QList<QByteArray> &newRoles)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModel19replaceWatchedRolesERK5QListI10QByteArrayES4_(
    QQmlAdaptorModel *self,
    const QList<QByteArray> *oldRoles,
    const QList<QByteArray> *newRoles) {
  self->replaceWatchedRoles(*oldRoles, *newRoles);
}

//  QVariant QQmlAdaptorModel::modelIndex(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlAdaptorModel10modelIndexEi(
    const QQmlAdaptorModel *self,
    int index) {
  return new QVariant(self->modelIndex(index));
}

//  QVariant QQmlAdaptorModel::parentModelIndex() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlAdaptorModel16parentModelIndexEv(
    const QQmlAdaptorModel *self) {
  return new QVariant(self->parentModelIndex());
}

//  bool QQmlAdaptorModel::canFetchMore() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlAdaptorModel12canFetchMoreEv(
    const QQmlAdaptorModel *self) {
  return self->canFetchMore();
}

//  void QQmlAdaptorModel::fetchMore()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModel9fetchMoreEv(QQmlAdaptorModel *self) {
  self->fetchMore();
}

//  void QQmlAdaptorModel::objectDestroyedImpl(QQmlGuardImpl *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModel19objectDestroyedImplEP13QQmlGuardImpl(
    QQmlGuardImpl *a0) {
  QQmlAdaptorModel::objectDestroyedImpl(a0);
}

#endif  // QT_CONFIG(qml_delegate_model)
