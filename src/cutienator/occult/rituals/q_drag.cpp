//  Written by dev_tooling.RitualGenerator from the records of QtGui/qdrag.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qdrag.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QDrag::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QDrag10metaObjectEv(const QDrag *self) {
  return self->metaObject();
}

//  QString QDrag::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QDrag2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QDrag::tr(s, c, n));
}

//  QDrag::QDrag(QObject *dragSource)
extern "C" Q_DECL_EXPORT
QDrag *ritual_ZN5QDragC1EP7QObject(QObject *dragSource) {
  return new QDrag(dragSource);
}

//  QDrag::~QDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDragD1Ev(QDrag *self) {
  delete self;
}

//  void QDrag::setMimeData(QMimeData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag11setMimeDataEP9QMimeData(QDrag *self, QMimeData *data) {
  self->setMimeData(data);
}

//  QMimeData *QDrag::mimeData() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK5QDrag8mimeDataEv(const QDrag *self) {
  return self->mimeData();
}

//  void QDrag::setPixmap(const QPixmap &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag9setPixmapERK7QPixmap(QDrag *self, const QPixmap *a0) {
  self->setPixmap(*a0);
}

//  QPixmap QDrag::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QDrag6pixmapEv(const QDrag *self) {
  return new QPixmap(self->pixmap());
}

//  void QDrag::setHotSpot(const QPoint &hotspot)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag10setHotSpotERK6QPoint(
    QDrag *self,
    const QPoint *hotspot) {
  self->setHotSpot(*hotspot);
}

//  QPoint QDrag::hotSpot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QDrag7hotSpotEv(const QDrag *self) {
  return new QPoint(self->hotSpot());
}

//  QObject *QDrag::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK5QDrag6sourceEv(const QDrag *self) {
  return self->source();
}

//  QObject *QDrag::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK5QDrag6targetEv(const QDrag *self) {
  return self->target();
}

//  Qt::DropAction QDrag::exec(Qt::DropActions supportedActions)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN5QDrag4execE6QFlagsIN2Qt10DropActionEE(
    QDrag *self,
    int supportedActions) {
  return self->exec(QFlags<Qt::DropAction>::fromInt(supportedActions));
}

//  Qt::DropAction QDrag::exec(Qt::DropActions supportedActions,
//      Qt::DropAction defaultAction)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN5QDrag4execE6QFlagsIN2Qt10DropActionEES2_(
    QDrag *self,
    int supportedActions,
    Qt::DropAction defaultAction) {
  return self->exec(
      QFlags<Qt::DropAction>::fromInt(supportedActions),
      defaultAction);
}

//  void QDrag::setDragCursor(const QPixmap &cursor, Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag13setDragCursorERK7QPixmapN2Qt10DropActionE(
    QDrag *self,
    const QPixmap *cursor,
    Qt::DropAction action) {
  self->setDragCursor(*cursor, action);
}

//  QPixmap QDrag::dragCursor(Qt::DropAction action) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QDrag10dragCursorEN2Qt10DropActionE(
    const QDrag *self,
    Qt::DropAction action) {
  return new QPixmap(self->dragCursor(action));
}

//  Qt::DropActions QDrag::supportedActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDrag16supportedActionsEv(const QDrag *self) {
  return static_cast<int>(self->supportedActions().toInt());
}

//  Qt::DropAction QDrag::defaultAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK5QDrag13defaultActionEv(const QDrag *self) {
  return self->defaultAction();
}

//  void QDrag::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDrag6cancelEv() {
  QDrag::cancel();
}
