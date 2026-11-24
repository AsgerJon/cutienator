//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickcolorimage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickcolorimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuickColorImage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickColorImage : QQuickColorImage {
  using QQuickColorImage::pixmapChange;
};

//  const QMetaObject *QQuickColorImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickColorImage10metaObjectEv(
    const QQuickColorImage *self) {
  return self->metaObject();
}

//  QString QQuickColorImage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickColorImage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickColorImage::tr(s, c, n));
}

//  QQuickColorImage::QQuickColorImage(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickColorImage *ritual_ZN16QQuickColorImageC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickColorImage(parent);
}

//  QColor QQuickColorImage::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorImage5colorEv(const QQuickColorImage *self) {
  return new QColor(self->color());
}

//  void QQuickColorImage::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorImage8setColorERK6QColor(
    QQuickColorImage *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickColorImage::resetColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorImage10resetColorEv(QQuickColorImage *self) {
  self->resetColor();
}

//  QColor QQuickColorImage::defaultColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorImage12defaultColorEv(
    const QQuickColorImage *self) {
  return new QColor(self->defaultColor());
}

//  void QQuickColorImage::setDefaultColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorImage15setDefaultColorERK6QColor(
    QQuickColorImage *self,
    const QColor *color) {
  self->setDefaultColor(*color);
}

//  void QQuickColorImage::resetDefaultColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorImage17resetDefaultColorEv(
    QQuickColorImage *self) {
  self->resetDefaultColor();
}

//  void QQuickColorImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorImage12pixmapChangeEv(QQuickColorImage *self) {
  self->pixmapChange();
}

//  void QQuickColorImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickColorImage12pixmapChangeEv(
    QQuickColorImage *self) {
  static_cast<OwnQQuickColorImage *>(self)->OwnQQuickColorImage::pixmapChange();
}
