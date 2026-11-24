//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformscreen.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformscreen.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>

//  QPlatformPlaceholderScreen::QPlatformPlaceholderScreen(bool
//      virtualSibling)
extern "C" Q_DECL_EXPORT
QPlatformPlaceholderScreen *ritual_ZN26QPlatformPlaceholderScreenC1Eb(
    bool virtualSibling) {
  return new QPlatformPlaceholderScreen(virtualSibling);
}

//  bool QPlatformPlaceholderScreen::isPlaceholder() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPlatformPlaceholderScreen13isPlaceholderEv(
    const QPlatformPlaceholderScreen *self) {
  return self->isPlaceholder();
}

//  QRect QPlatformPlaceholderScreen::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK26QPlatformPlaceholderScreen8geometryEv(
    const QPlatformPlaceholderScreen *self) {
  return new QRect(self->geometry());
}

//  QRect QPlatformPlaceholderScreen::availableGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK26QPlatformPlaceholderScreen17availableGeometryEv(
    const QPlatformPlaceholderScreen *self) {
  return new QRect(self->availableGeometry());
}

//  int QPlatformPlaceholderScreen::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QPlatformPlaceholderScreen5depthEv(
    const QPlatformPlaceholderScreen *self) {
  return self->depth();
}

//  QImage::Format QPlatformPlaceholderScreen::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK26QPlatformPlaceholderScreen6formatEv(
    const QPlatformPlaceholderScreen *self) {
  return self->format();
}

//  QList<QPlatformScreen *> QPlatformPlaceholderScreen::virtualSiblings()
//      const
extern "C" Q_DECL_EXPORT
QList<QPlatformScreen *> *ritual_ZNK26QPlatformPlaceholderScreen15virtualSiblingsEv(
    const QPlatformPlaceholderScreen *self) {
  return new QList<QPlatformScreen *>(self->virtualSiblings());
}

//  bool QPlatformPlaceholderScreen::isPlaceholder() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QPlatformPlaceholderScreen13isPlaceholderEv(
    const QPlatformPlaceholderScreen *self) {
  return self->QPlatformPlaceholderScreen::isPlaceholder();
}

//  QRect QPlatformPlaceholderScreen::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK26QPlatformPlaceholderScreen8geometryEv(
    const QPlatformPlaceholderScreen *self) {
  return new QRect(self->QPlatformPlaceholderScreen::geometry());
}

//  QRect QPlatformPlaceholderScreen::availableGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK26QPlatformPlaceholderScreen17availableGeometryEv(
    const QPlatformPlaceholderScreen *self) {
  return new QRect(self->QPlatformPlaceholderScreen::availableGeometry());
}

//  int QPlatformPlaceholderScreen::depth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QPlatformPlaceholderScreen5depthEv(
    const QPlatformPlaceholderScreen *self) {
  return self->QPlatformPlaceholderScreen::depth();
}

//  QImage::Format QPlatformPlaceholderScreen::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_own_ZNK26QPlatformPlaceholderScreen6formatEv(
    const QPlatformPlaceholderScreen *self) {
  return self->QPlatformPlaceholderScreen::format();
}
