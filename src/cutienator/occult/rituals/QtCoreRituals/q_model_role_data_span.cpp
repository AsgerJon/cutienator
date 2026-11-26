//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, instances of templates of the class: 1. Kept as it is when
//  the generator runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>

//  QModelRoleDataSpan::QModelRoleDataSpan()
extern "C" Q_DECL_EXPORT
QModelRoleDataSpan *ritual_ZN18QModelRoleDataSpanC1Ev() {
  return new QModelRoleDataSpan();
}

//  QModelRoleDataSpan::QModelRoleDataSpan(QModelRoleData &modelRoleData)
extern "C" Q_DECL_EXPORT
QModelRoleDataSpan *ritual_ZN18QModelRoleDataSpanC1ER14QModelRoleData(
    QModelRoleData *modelRoleData) {
  return new QModelRoleDataSpan(*modelRoleData);
}

//  QModelRoleDataSpan::QModelRoleDataSpan(QModelRoleData *modelRoleData,
//      qsizetype len)
extern "C" Q_DECL_EXPORT
QModelRoleDataSpan *ritual_ZN18QModelRoleDataSpanC1EP14QModelRoleDatax(
    QModelRoleData *modelRoleData,
    qsizetype len) {
  return new QModelRoleDataSpan(modelRoleData, len);
}

//  qsizetype QModelRoleDataSpan::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QModelRoleDataSpan4sizeEv(
    const QModelRoleDataSpan *self) {
  return self->size();
}

//  qsizetype QModelRoleDataSpan::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QModelRoleDataSpan6lengthEv(
    const QModelRoleDataSpan *self) {
  return self->length();
}

//  QModelRoleData *QModelRoleDataSpan::data() const
extern "C" Q_DECL_EXPORT
QModelRoleData *ritual_ZNK18QModelRoleDataSpan4dataEv(
    const QModelRoleDataSpan *self) {
  return self->data();
}

//  QModelRoleData *QModelRoleDataSpan::begin() const
extern "C" Q_DECL_EXPORT
QModelRoleData *ritual_ZNK18QModelRoleDataSpan5beginEv(
    const QModelRoleDataSpan *self) {
  return self->begin();
}

//  QModelRoleData *QModelRoleDataSpan::end() const
extern "C" Q_DECL_EXPORT
QModelRoleData *ritual_ZNK18QModelRoleDataSpan3endEv(
    const QModelRoleDataSpan *self) {
  return self->end();
}

//  QModelRoleData &QModelRoleDataSpan::operator[](qsizetype index) const
extern "C" Q_DECL_EXPORT
QModelRoleData *ritual_ZNK18QModelRoleDataSpanixEx(
    const QModelRoleDataSpan *self,
    qsizetype index) {
  return &(self->operator[](index));
}

//  QVariant *QModelRoleDataSpan::dataForRole(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QModelRoleDataSpan11dataForRoleEi(
    const QModelRoleDataSpan *self,
    int role) {
  return self->dataForRole(role);
}

//  QModelRoleDataSpan::~QModelRoleDataSpan()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QModelRoleDataSpanD1Ev(QModelRoleDataSpan *self) {
  delete self;
}

//  QModelRoleDataSpan::QModelRoleDataSpan<QList<QModelRoleData>>(QList<QModelRoleData>
//      &c)
extern "C" Q_DECL_EXPORT
QModelRoleDataSpan * ritual_ZN18QModelRoleDataSpanC1I5QListI14QModelRoleDataELb1EERT_(
    QList<QModelRoleData> *c) {
  return new QModelRoleDataSpan(*c);
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
