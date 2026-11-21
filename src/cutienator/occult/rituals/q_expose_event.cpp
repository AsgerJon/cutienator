//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qregion.h>

//  QExposeEvent *QExposeEvent::clone() const
extern "C" Q_DECL_EXPORT
QExposeEvent *ritual_ZNK12QExposeEvent5cloneEv(const QExposeEvent *self) {
  return self->clone();
}

//  QExposeEvent::~QExposeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QExposeEventD1Ev(QExposeEvent *self) {
  delete self;
}

//  QExposeEvent::QExposeEvent(const QRegion &m_region)
extern "C" Q_DECL_EXPORT
QExposeEvent *ritual_ZN12QExposeEventC1ERK7QRegion(const QRegion *m_region) {
  return new QExposeEvent(*m_region);
}

//  const QRegion &QExposeEvent::region() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK12QExposeEvent6regionEv(const QExposeEvent *self) {
  return new QRegion(self->region());
}
