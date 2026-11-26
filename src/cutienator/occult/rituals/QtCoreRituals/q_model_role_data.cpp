//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, instances of templates of the class: 5. Kept as it is when
//  the generator runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
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

//  QVariant &QModelRoleData::data()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QModelRoleData4dataEv(QModelRoleData *self) {
  return &(self->data());
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

//  void QModelRoleData::setData<int>(int &&value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModelRoleData7setDataIiEEvOT_(
    QModelRoleData *self,
    int value) {
  self->setData<int>(int(value));
}

//  void QModelRoleData::setData<double>(double &&value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModelRoleData7setDataIdEEvOT_(
    QModelRoleData *self,
    double value) {
  self->setData<double>(double(value));
}

//  void QModelRoleData::setData<bool>(bool &&value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModelRoleData7setDataIbEEvOT_(
    QModelRoleData *self,
    bool value) {
  self->setData<bool>(bool(value));
}

//  void QModelRoleData::setData<QString>(QString &&value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModelRoleData7setDataI7QStringEEvOT_(
    QModelRoleData *self,
    const QString *value) {
  self->setData<QString>(QString(*value));
}

//  void QModelRoleData::setData<QVariant>(QVariant &&value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModelRoleData7setDataI8QVariantEEvOT_(
    QModelRoleData *self,
    const QVariant *value) {
  self->setData<QVariant>(QVariant(*value));
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
