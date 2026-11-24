//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>

//  QModelRoleData::QModelRoleData(int role)
extern "C" Q_DECL_EXPORT
QModelRoleData *ritual_ZN14QModelRoleDataC1Ei(int role) {
  return new QModelRoleData(role);
}

//  int QModelRoleData::role() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QModelRoleData4roleEv(const QModelRoleData *self) {
  return self->role();
}

//  const QVariant &QModelRoleData::data() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QModelRoleData4dataEv(const QModelRoleData *self) {
  return new QVariant(self->data());
}

//  void QModelRoleData::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModelRoleData9clearDataEv(QModelRoleData *self) {
  self->clearData();
}

//  QModelRoleData::~QModelRoleData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModelRoleDataD1Ev(QModelRoleData *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
