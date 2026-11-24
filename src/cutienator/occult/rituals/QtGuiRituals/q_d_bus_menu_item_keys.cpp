//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QDBusMenuItemKeys::~QDBusMenuItemKeys()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusMenuItemKeysD1Ev(QDBusMenuItemKeys *self) {
  delete self;
}

//  QList<QDBusMenuItemKeys>::QList()
extern "C" Q_DECL_EXPORT
QList<QDBusMenuItemKeys> *ritual_list_make_QDBusMenuItemKeys() {
  return new QList<QDBusMenuItemKeys>();
}

//  void QList<QDBusMenuItemKeys>::append(const QDBusMenuItemKeys &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDBusMenuItemKeys(
    QList<QDBusMenuItemKeys> *self,
    const QDBusMenuItemKeys *element) {
  self->append(*element);
}

//  qsizetype QList<QDBusMenuItemKeys>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDBusMenuItemKeys(
    const QList<QDBusMenuItemKeys> *self) {
  return self->size();
}

//  const QDBusMenuItemKeys &QList<QDBusMenuItemKeys>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDBusMenuItemKeys *ritual_list_at_QDBusMenuItemKeys(
    const QList<QDBusMenuItemKeys> *self,
    long long index) {
  return new QDBusMenuItemKeys(self->at(index));
}

//  QList<QDBusMenuItemKeys>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDBusMenuItemKeys(QList<QDBusMenuItemKeys> *self) {
  delete self;
}
