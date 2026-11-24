//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbackingstore.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbackingstore.h>
#include <QtGui/qregion.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>

//  QBackingStore::QBackingStore(QWindow *window)
extern "C" Q_DECL_EXPORT
QBackingStore *ritual_ZN13QBackingStoreC1EP7QWindow(QWindow *window) {
  return new QBackingStore(window);
}

//  QBackingStore::~QBackingStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBackingStoreD1Ev(QBackingStore *self) {
  delete self;
}

//  QWindow *QBackingStore::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK13QBackingStore6windowEv(const QBackingStore *self) {
  return self->window();
}

//  QPaintDevice *QBackingStore::paintDevice()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZN13QBackingStore11paintDeviceEv(QBackingStore *self) {
  return self->paintDevice();
}

//  void QBackingStore::flush(const QRegion &region, QWindow *window, const
//      QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBackingStore5flushERK7QRegionP7QWindowRK6QPoint(
    QBackingStore *self,
    const QRegion *region,
    QWindow *window,
    const QPoint *offset) {
  self->flush(*region, window, *offset);
}

//  void QBackingStore::resize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBackingStore6resizeERK5QSize(
    QBackingStore *self,
    const QSize *size) {
  self->resize(*size);
}

//  QSize QBackingStore::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QBackingStore4sizeEv(const QBackingStore *self) {
  return new QSize(self->size());
}

//  bool QBackingStore::scroll(const QRegion &area, int dx, int dy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QBackingStore6scrollERK7QRegionii(
    QBackingStore *self,
    const QRegion *area,
    int dx,
    int dy) {
  return self->scroll(*area, dx, dy);
}

//  void QBackingStore::beginPaint(const QRegion &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBackingStore10beginPaintERK7QRegion(
    QBackingStore *self,
    const QRegion *a0) {
  self->beginPaint(*a0);
}

//  void QBackingStore::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBackingStore8endPaintEv(QBackingStore *self) {
  self->endPaint();
}

//  void QBackingStore::setStaticContents(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBackingStore17setStaticContentsERK7QRegion(
    QBackingStore *self,
    const QRegion *region) {
  self->setStaticContents(*region);
}

//  QRegion QBackingStore::staticContents() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK13QBackingStore14staticContentsEv(
    const QBackingStore *self) {
  return new QRegion(self->staticContents());
}

//  bool QBackingStore::hasStaticContents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QBackingStore17hasStaticContentsEv(
    const QBackingStore *self) {
  return self->hasStaticContents();
}

//  QPlatformBackingStore *QBackingStore::handle() const
extern "C" Q_DECL_EXPORT
QPlatformBackingStore *ritual_ZNK13QBackingStore6handleEv(
    const QBackingStore *self) {
  return self->handle();
}
