//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmladaptormodel.cpp, line 13, as _ZN16QQmlAdaptorModel9AccessorsD1Ev
inline QQmlAdaptorModel::Accessors::~Accessors()
{
}
//  -----------------------------------------------------------------------

//  QQmlAdaptorModel::Accessors::Accessors()
extern "C" Q_DECL_EXPORT
QQmlAdaptorModel::Accessors *ritual_ZN16QQmlAdaptorModel9AccessorsC1Ev() {
  return new QQmlAdaptorModel::Accessors();
}

//  QQmlAdaptorModel::Accessors::~Accessors()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlAdaptorModel9AccessorsD1Ev(
    QQmlAdaptorModel::Accessors *self) {
  delete self;
}

//  int QQmlAdaptorModel::Accessors::rowCount(const QQmlAdaptorModel &a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel9Accessors8rowCountERKS_(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *a0) {
  return self->rowCount(*a0);
}

//  int QQmlAdaptorModel::Accessors::columnCount(const QQmlAdaptorModel &a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlAdaptorModel9Accessors11columnCountERKS_(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *a0) {
  return self->columnCount(*a0);
}

//  void QQmlAdaptorModel::Accessors::cleanup(QQmlAdaptorModel &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QQmlAdaptorModel9Accessors7cleanupERS_(
    const QQmlAdaptorModel::Accessors *self,
    QQmlAdaptorModel *a0) {
  self->cleanup(*a0);
}

//  QVariant QQmlAdaptorModel::Accessors::value(const QQmlAdaptorModel &a0,
//      int a1, const QString &a2) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlAdaptorModel9Accessors5valueERKS_iRK7QString(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *a0,
    int a1,
    const QString *a2) {
  return new QVariant(self->value(*a0, a1, *a2));
}

//  QQmlDelegateModelItem
//      *QQmlAdaptorModel::Accessors::createItem(QQmlAdaptorModel &a0, const
//      QQmlRefPointer<QQmlDelegateModelItemMetaType> &a1, int a2, int a3,
//      int a4)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_ZN16QQmlAdaptorModel9Accessors10createItemERS_RK14QQmlRefPointerI29QQmlDelegateModelItemMetaTypeEiii(
    QQmlAdaptorModel::Accessors *self,
    QQmlAdaptorModel *a0,
    const QQmlRefPointer<QQmlDelegateModelItemMetaType> *a1,
    int a2,
    int a3,
    int a4) {
  return self->createItem(*a0, *a1, a2, a3, a4);
}

//  bool QQmlAdaptorModel::Accessors::notify(const QQmlAdaptorModel &a0,
//      const QList<QQmlDelegateModelItem *> &a1, int a2, int a3, const
//      QList<int> &a4) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlAdaptorModel9Accessors6notifyERKS_RK5QListIP21QQmlDelegateModelItemEiiRKS3_IiE(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *a0,
    const QList<QQmlDelegateModelItem *> *a1,
    int a2,
    int a3,
    const QList<int> *a4) {
  return self->notify(*a0, *a1, a2, a3, *a4);
}

//  void QQmlAdaptorModel::Accessors::replaceWatchedRoles(QQmlAdaptorModel
//      &a0, const QList<QByteArray> &a1, const QList<QByteArray> &a2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QQmlAdaptorModel9Accessors19replaceWatchedRolesERS_RK5QListI10QByteArrayES6_(
    const QQmlAdaptorModel::Accessors *self,
    QQmlAdaptorModel *a0,
    const QList<QByteArray> *a1,
    const QList<QByteArray> *a2) {
  self->replaceWatchedRoles(*a0, *a1, *a2);
}

//  QVariant QQmlAdaptorModel::Accessors::parentModelIndex(const
//      QQmlAdaptorModel &a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlAdaptorModel9Accessors16parentModelIndexERKS_(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *a0) {
  return new QVariant(self->parentModelIndex(*a0));
}

//  QVariant QQmlAdaptorModel::Accessors::modelIndex(const QQmlAdaptorModel
//      &a0, int a1) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlAdaptorModel9Accessors10modelIndexERKS_i(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *a0,
    int a1) {
  return new QVariant(self->modelIndex(*a0, a1));
}

//  bool QQmlAdaptorModel::Accessors::canFetchMore(const QQmlAdaptorModel
//      &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlAdaptorModel9Accessors12canFetchMoreERKS_(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *a0) {
  return self->canFetchMore(*a0);
}

//  void QQmlAdaptorModel::Accessors::fetchMore(QQmlAdaptorModel &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QQmlAdaptorModel9Accessors9fetchMoreERS_(
    const QQmlAdaptorModel::Accessors *self,
    QQmlAdaptorModel *a0) {
  self->fetchMore(*a0);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
