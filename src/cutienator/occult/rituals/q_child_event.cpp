//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>

//  QChildEvent *QChildEvent::clone() const
extern "C" Q_DECL_EXPORT
QChildEvent *ritual_ZNK11QChildEvent5cloneEv(const QChildEvent *self) {
  return self->clone();
}

//  QChildEvent::~QChildEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QChildEventD1Ev(QChildEvent *self) {
  delete self;
}

//  QChildEvent::QChildEvent(Type type, QObject *child)
extern "C" Q_DECL_EXPORT
QChildEvent *ritual_ZN11QChildEventC1EN6QEvent4TypeEP7QObject(
    QEvent::Type type,
    QObject *child) {
  return new QChildEvent(type, child);
}

//  QObject *QChildEvent::child() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QChildEvent5childEv(const QChildEvent *self) {
  return self->child();
}

//  bool QChildEvent::added() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QChildEvent5addedEv(const QChildEvent *self) {
  return self->added();
}

//  bool QChildEvent::polished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QChildEvent8polishedEv(const QChildEvent *self) {
  return self->polished();
}

//  bool QChildEvent::removed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QChildEvent7removedEv(const QChildEvent *self) {
  return self->removed();
}
