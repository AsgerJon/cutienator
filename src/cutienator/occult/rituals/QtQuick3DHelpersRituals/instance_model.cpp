//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/instancerepeater_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/instancerepeater_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *InstanceModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13InstanceModel10metaObjectEv(
    const InstanceModel *self) {
  return self->metaObject();
}

//  QString InstanceModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13InstanceModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(InstanceModel::tr(s, c, n));
}

//  InstanceModel::InstanceModel(QObject *parent)
extern "C" Q_DECL_EXPORT
InstanceModel *ritual_ZN13InstanceModelC1EP7QObject(QObject *parent) {
  return new InstanceModel(parent);
}

//  QVariant InstanceModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13InstanceModel4dataERK11QModelIndexi(
    const InstanceModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int InstanceModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13InstanceModel8rowCountERK11QModelIndex(
    const InstanceModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QQuick3DInstancing *InstanceModel::instancing() const
extern "C" Q_DECL_EXPORT
QQuick3DInstancing *ritual_ZNK13InstanceModel10instancingEv(
    const InstanceModel *self) {
  return self->instancing();
}

//  void InstanceModel::setInstancing(QQuick3DInstancing *instancing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13InstanceModel13setInstancingEP18QQuick3DInstancing(
    InstanceModel *self,
    QQuick3DInstancing *instancing) {
  self->setInstancing(instancing);
}

//  const QQuick3DInstancing::InstanceTableEntry
//      *InstanceModel::instanceData(int index) const
extern "C" Q_DECL_EXPORT
const QQuick3DInstancing::InstanceTableEntry *ritual_ZNK13InstanceModel12instanceDataEi(
    const InstanceModel *self,
    int index) {
  return self->instanceData(index);
}

//  QHash<int, QByteArray> InstanceModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK13InstanceModel9roleNamesEv(
    const InstanceModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void InstanceModel::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13InstanceModel5resetEv(InstanceModel *self) {
  self->reset();
}

//  void InstanceModel::ensureTable() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13InstanceModel11ensureTableEv(const InstanceModel *self) {
  self->ensureTable();
}

//  QVariant InstanceModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK13InstanceModel4dataERK11QModelIndexi(
    const InstanceModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->InstanceModel::data(*index, role));
}

//  int InstanceModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13InstanceModel8rowCountERK11QModelIndex(
    const InstanceModel *self,
    const QModelIndex *parent) {
  return self->InstanceModel::rowCount(*parent);
}
