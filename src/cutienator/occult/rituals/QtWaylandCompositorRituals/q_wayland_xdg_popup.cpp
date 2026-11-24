//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandxdgshell.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QWaylandXdgPopup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QWaylandXdgPopup10metaObjectEv(
    const QWaylandXdgPopup *self) {
  return self->metaObject();
}

//  QString QWaylandXdgPopup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QWaylandXdgPopup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgPopup::tr(s, c, n));
}

//  QWaylandXdgSurface *QWaylandXdgPopup::xdgSurface() const
extern "C" Q_DECL_EXPORT
QWaylandXdgSurface *ritual_ZNK16QWaylandXdgPopup10xdgSurfaceEv(
    const QWaylandXdgPopup *self) {
  return self->xdgSurface();
}

//  QWaylandXdgSurface *QWaylandXdgPopup::parentXdgSurface() const
extern "C" Q_DECL_EXPORT
QWaylandXdgSurface *ritual_ZNK16QWaylandXdgPopup16parentXdgSurfaceEv(
    const QWaylandXdgPopup *self) {
  return self->parentXdgSurface();
}

//  QRect QWaylandXdgPopup::configuredGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QWaylandXdgPopup18configuredGeometryEv(
    const QWaylandXdgPopup *self) {
  return new QRect(self->configuredGeometry());
}

//  QRect QWaylandXdgPopup::anchorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QWaylandXdgPopup10anchorRectEv(
    const QWaylandXdgPopup *self) {
  return new QRect(self->anchorRect());
}

//  Qt::Edges QWaylandXdgPopup::anchorEdges() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QWaylandXdgPopup11anchorEdgesEv(
    const QWaylandXdgPopup *self) {
  return static_cast<int>(self->anchorEdges().toInt());
}

//  Qt::Edges QWaylandXdgPopup::gravityEdges() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QWaylandXdgPopup12gravityEdgesEv(
    const QWaylandXdgPopup *self) {
  return static_cast<int>(self->gravityEdges().toInt());
}

//  Qt::Orientations QWaylandXdgPopup::slideConstraints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QWaylandXdgPopup16slideConstraintsEv(
    const QWaylandXdgPopup *self) {
  return static_cast<int>(self->slideConstraints().toInt());
}

//  Qt::Orientations QWaylandXdgPopup::flipConstraints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QWaylandXdgPopup15flipConstraintsEv(
    const QWaylandXdgPopup *self) {
  return static_cast<int>(self->flipConstraints().toInt());
}

//  Qt::Orientations QWaylandXdgPopup::resizeConstraints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QWaylandXdgPopup17resizeConstraintsEv(
    const QWaylandXdgPopup *self) {
  return static_cast<int>(self->resizeConstraints().toInt());
}

//  QPoint QWaylandXdgPopup::offset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QWaylandXdgPopup6offsetEv(const QWaylandXdgPopup *self) {
  return new QPoint(self->offset());
}

//  QSize QWaylandXdgPopup::positionerSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QWaylandXdgPopup14positionerSizeEv(
    const QWaylandXdgPopup *self) {
  return new QSize(self->positionerSize());
}

//  QPoint QWaylandXdgPopup::unconstrainedPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QWaylandXdgPopup21unconstrainedPositionEv(
    const QWaylandXdgPopup *self) {
  return new QPoint(self->unconstrainedPosition());
}

//  uint QWaylandXdgPopup::sendConfigure(const QRect &geometry)
extern "C" Q_DECL_EXPORT
uint ritual_ZN16QWaylandXdgPopup13sendConfigureERK5QRect(
    QWaylandXdgPopup *self,
    const QRect *geometry) {
  return self->sendConfigure(*geometry);
}

//  void QWaylandXdgPopup::sendPopupDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgPopup13sendPopupDoneEv(QWaylandXdgPopup *self) {
  self->sendPopupDone();
}

//  QWaylandSurfaceRole *QWaylandXdgPopup::role()
extern "C" Q_DECL_EXPORT
QWaylandSurfaceRole *ritual_ZN16QWaylandXdgPopup4roleEv() {
  return QWaylandXdgPopup::role();
}
