//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QDBusMenuEvent::~QDBusMenuEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusMenuEventD1Ev(QDBusMenuEvent *self) {
  delete self;
}

//  QList<QDBusMenuEvent>::QList()
extern "C" Q_DECL_EXPORT
QList<QDBusMenuEvent> *ritual_list_make_QDBusMenuEvent() {
  return new QList<QDBusMenuEvent>();
}

//  void QList<QDBusMenuEvent>::append(const QDBusMenuEvent &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDBusMenuEvent(
    QList<QDBusMenuEvent> *self,
    const QDBusMenuEvent *element) {
  self->append(*element);
}

//  qsizetype QList<QDBusMenuEvent>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDBusMenuEvent(
    const QList<QDBusMenuEvent> *self) {
  return self->size();
}

//  const QDBusMenuEvent &QList<QDBusMenuEvent>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDBusMenuEvent *ritual_list_at_QDBusMenuEvent(
    const QList<QDBusMenuEvent> *self,
    long long index) {
  return new QDBusMenuEvent(self->at(index));
}

//  QList<QDBusMenuEvent>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDBusMenuEvent(QList<QDBusMenuEvent> *self) {
  delete self;
}
