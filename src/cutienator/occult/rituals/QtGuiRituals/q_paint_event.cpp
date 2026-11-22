//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qregion.h>
#include <QtCore/qrect.h>

//  QPaintEvent *QPaintEvent::clone() const
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZNK11QPaintEvent5cloneEv(const QPaintEvent *self) {
  return self->clone();
}

//  QPaintEvent::~QPaintEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPaintEventD1Ev(QPaintEvent *self) {
  delete self;
}

//  QPaintEvent::QPaintEvent(const QRegion &paintRegion)
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZN11QPaintEventC1ERK7QRegion(
    const QRegion *paintRegion) {
  return new QPaintEvent(*paintRegion);
}

//  QPaintEvent::QPaintEvent(const QRect &paintRect)
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZN11QPaintEventC1ERK5QRect(const QRect *paintRect) {
  return new QPaintEvent(*paintRect);
}

//  const QRect &QPaintEvent::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QPaintEvent4rectEv(const QPaintEvent *self) {
  return new QRect(self->rect());
}

//  const QRegion &QPaintEvent::region() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK11QPaintEvent6regionEv(const QPaintEvent *self) {
  return new QRegion(self->region());
}
