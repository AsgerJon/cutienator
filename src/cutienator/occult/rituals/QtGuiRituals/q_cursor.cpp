//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qcursor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_CURSOR)
#include <QtGui/qcursor.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>

//  QCursor::QCursor()
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZN7QCursorC1Ev() {
  return new QCursor();
}

//  QCursor::QCursor(Qt::CursorShape shape)
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZN7QCursorC1EN2Qt11CursorShapeE(Qt::CursorShape shape) {
  return new QCursor(shape);
}

//  QCursor::QCursor(const QBitmap &bitmap, const QBitmap &mask, int hotX,
//      int hotY)
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZN7QCursorC1ERK7QBitmapS2_ii(
    const QBitmap *bitmap,
    const QBitmap *mask,
    int hotX,
    int hotY) {
  return new QCursor(*bitmap, *mask, hotX, hotY);
}

//  QCursor::QCursor(const QPixmap &pixmap, int hotX, int hotY)
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZN7QCursorC1ERK7QPixmapii(
    const QPixmap *pixmap,
    int hotX,
    int hotY) {
  return new QCursor(*pixmap, hotX, hotY);
}

//  QCursor::QCursor(const QCursor &cursor)
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZN7QCursorC1ERKS_(const QCursor *cursor) {
  return new QCursor(*cursor);
}

//  QCursor::~QCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCursorD1Ev(QCursor *self) {
  delete self;
}

//  QVariant QCursor::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QCursorcv8QVariantEv(const QCursor *self) {
  return new QVariant(self->operator QVariant());
}

//  Qt::CursorShape QCursor::shape() const
extern "C" Q_DECL_EXPORT
Qt::CursorShape ritual_ZNK7QCursor5shapeEv(const QCursor *self) {
  return self->shape();
}

//  void QCursor::setShape(Qt::CursorShape newShape)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCursor8setShapeEN2Qt11CursorShapeE(
    QCursor *self,
    Qt::CursorShape newShape) {
  self->setShape(newShape);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QBitmap QCursor::bitmap(Qt::ReturnByValueConstant a0) const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QCursor6bitmapEN2Qt21ReturnByValueConstantE(
    const QCursor *self,
    Qt::ReturnByValueConstant a0) {
  return new QBitmap(self->bitmap(a0));
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QBitmap QCursor::mask(Qt::ReturnByValueConstant a0) const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QCursor4maskEN2Qt21ReturnByValueConstantE(
    const QCursor *self,
    Qt::ReturnByValueConstant a0) {
  return new QBitmap(self->mask(a0));
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  QBitmap QCursor::bitmap() const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QCursor6bitmapEv(const QCursor *self) {
  return new QBitmap(self->bitmap());
}

//  QBitmap QCursor::mask() const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QCursor4maskEv(const QCursor *self) {
  return new QBitmap(self->mask());
}

//  QPixmap QCursor::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QCursor6pixmapEv(const QCursor *self) {
  return new QPixmap(self->pixmap());
}

//  QPoint QCursor::hotSpot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QCursor7hotSpotEv(const QCursor *self) {
  return new QPoint(self->hotSpot());
}

//  QPoint QCursor::pos()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN7QCursor3posEv() {
  return new QPoint(QCursor::pos());
}

//  QPoint QCursor::pos(const QScreen *screen)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN7QCursor3posEPK7QScreen(const QScreen *screen) {
  return new QPoint(QCursor::pos(screen));
}

//  void QCursor::setPos(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCursor6setPosEii(int x, int y) {
  QCursor::setPos(x, y);
}

//  void QCursor::setPos(QScreen *screen, int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCursor6setPosEP7QScreenii(QScreen *screen, int x, int y) {
  QCursor::setPos(screen, x, y);
}

//  void QCursor::setPos(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCursor6setPosERK6QPoint(const QPoint *p) {
  QCursor::setPos(*p);
}

//  void QCursor::setPos(QScreen *screen, const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCursor6setPosEP7QScreenRK6QPoint(
    QScreen *screen,
    const QPoint *p) {
  QCursor::setPos(screen, *p);
}

//  bool operator==(const QCursor &lhs, const QCursor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QCursorS1_(const QCursor *lhs, const QCursor *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCursor &lhs, const QCursor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QCursorS1_(const QCursor *lhs, const QCursor *rhs) {
  return operator!=(*lhs, *rhs);
}

#endif  // !defined(QT_NO_CURSOR)
