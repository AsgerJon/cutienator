//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qoffscreensurface.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qoffscreensurface.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QOffscreenSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QOffscreenSurface10metaObjectEv(
    const QOffscreenSurface *self) {
  return self->metaObject();
}

//  QString QOffscreenSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QOffscreenSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOffscreenSurface::tr(s, c, n));
}

//  QOffscreenSurface::QOffscreenSurface(QScreen *screen, QObject *parent)
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZN17QOffscreenSurfaceC1EP7QScreenP7QObject(
    QScreen *screen,
    QObject *parent) {
  return new QOffscreenSurface(screen, parent);
}

//  QOffscreenSurface::~QOffscreenSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurfaceD1Ev(QOffscreenSurface *self) {
  delete self;
}

//  SurfaceType QOffscreenSurface::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK17QOffscreenSurface11surfaceTypeEv(
    const QOffscreenSurface *self) {
  return self->surfaceType();
}

//  void QOffscreenSurface::create()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface6createEv(QOffscreenSurface *self) {
  self->create();
}

//  void QOffscreenSurface::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface7destroyEv(QOffscreenSurface *self) {
  self->destroy();
}

//  bool QOffscreenSurface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QOffscreenSurface7isValidEv(const QOffscreenSurface *self) {
  return self->isValid();
}

//  void QOffscreenSurface::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface9setFormatERK14QSurfaceFormat(
    QOffscreenSurface *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  QSurfaceFormat QOffscreenSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK17QOffscreenSurface6formatEv(
    const QOffscreenSurface *self) {
  return new QSurfaceFormat(self->format());
}

//  QSurfaceFormat QOffscreenSurface::requestedFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK17QOffscreenSurface15requestedFormatEv(
    const QOffscreenSurface *self) {
  return new QSurfaceFormat(self->requestedFormat());
}

//  QSize QOffscreenSurface::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QOffscreenSurface4sizeEv(const QOffscreenSurface *self) {
  return new QSize(self->size());
}

//  QScreen *QOffscreenSurface::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK17QOffscreenSurface6screenEv(
    const QOffscreenSurface *self) {
  return self->screen();
}

//  void QOffscreenSurface::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface9setScreenEP7QScreen(
    QOffscreenSurface *self,
    QScreen *screen) {
  self->setScreen(screen);
}
