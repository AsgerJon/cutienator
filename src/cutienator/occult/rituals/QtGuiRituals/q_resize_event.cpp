//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qsize.h>

//  QResizeEvent *QResizeEvent::clone() const
extern "C" Q_DECL_EXPORT
QResizeEvent *ritual_ZNK12QResizeEvent5cloneEv(const QResizeEvent *self) {
  return self->clone();
}

//  QResizeEvent::~QResizeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QResizeEventD1Ev(QResizeEvent *self) {
  delete self;
}

//  QResizeEvent::QResizeEvent(const QSize &size, const QSize &oldSize)
extern "C" Q_DECL_EXPORT
QResizeEvent *ritual_ZN12QResizeEventC1ERK5QSizeS2_(
    const QSize *size,
    const QSize *oldSize) {
  return new QResizeEvent(*size, *oldSize);
}

//  const QSize &QResizeEvent::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QResizeEvent4sizeEv(const QResizeEvent *self) {
  return new QSize(self->size());
}

//  const QSize &QResizeEvent::oldSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QResizeEvent7oldSizeEv(const QResizeEvent *self) {
  return new QSize(self->oldSize());
}
