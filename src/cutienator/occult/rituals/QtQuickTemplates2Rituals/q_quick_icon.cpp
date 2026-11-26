//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qcolor.h>

//  void QQuickIcon::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon22qt_qmlMarker_anonymousEv(QQuickIcon *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickIcon::QQuickIcon()
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZN10QQuickIconC1Ev() {
  return new QQuickIcon();
}

//  QQuickIcon::QQuickIcon(const QQuickIcon &other)
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZN10QQuickIconC1ERKS_(const QQuickIcon *other) {
  return new QQuickIcon(*other);
}

//  QQuickIcon::~QQuickIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIconD1Ev(QQuickIcon *self) {
  delete self;
}

//  QQuickIcon &QQuickIcon::operator=(const QQuickIcon &other)
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZN10QQuickIconaSERKS_(
    QQuickIcon *self,
    const QQuickIcon *other) {
  return &(self->operator=(*other));
}

//  bool QQuickIcon::operator==(const QQuickIcon &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickIconeqERKS_(
    const QQuickIcon *self,
    const QQuickIcon *other) {
  return self->operator==(*other);
}

//  bool QQuickIcon::operator!=(const QQuickIcon &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickIconneERKS_(
    const QQuickIcon *self,
    const QQuickIcon *other) {
  return self->operator!=(*other);
}

//  bool QQuickIcon::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickIcon7isEmptyEv(const QQuickIcon *self) {
  return self->isEmpty();
}

//  QString QQuickIcon::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQuickIcon4nameEv(const QQuickIcon *self) {
  return new QString(self->name());
}

//  void QQuickIcon::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon7setNameERK7QString(
    QQuickIcon *self,
    const QString *name) {
  self->setName(*name);
}

//  void QQuickIcon::resetName()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon9resetNameEv(QQuickIcon *self) {
  self->resetName();
}

//  QUrl QQuickIcon::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QQuickIcon6sourceEv(const QQuickIcon *self) {
  return new QUrl(self->source());
}

//  void QQuickIcon::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon9setSourceERK4QUrl(
    QQuickIcon *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void QQuickIcon::resetSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon11resetSourceEv(QQuickIcon *self) {
  self->resetSource();
}

//  QUrl QQuickIcon::resolvedSource() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QQuickIcon14resolvedSourceEv(const QQuickIcon *self) {
  return new QUrl(self->resolvedSource());
}

//  void QQuickIcon::ensureRelativeSourceResolved(const QObject *owner)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon28ensureRelativeSourceResolvedEPK7QObject(
    QQuickIcon *self,
    const QObject *owner) {
  self->ensureRelativeSourceResolved(owner);
}

//  int QQuickIcon::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickIcon5widthEv(const QQuickIcon *self) {
  return self->width();
}

//  void QQuickIcon::setWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon8setWidthEi(QQuickIcon *self, int width) {
  self->setWidth(width);
}

//  void QQuickIcon::resetWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon10resetWidthEv(QQuickIcon *self) {
  self->resetWidth();
}

//  int QQuickIcon::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QQuickIcon6heightEv(const QQuickIcon *self) {
  return self->height();
}

//  void QQuickIcon::setHeight(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon9setHeightEi(QQuickIcon *self, int height) {
  self->setHeight(height);
}

//  void QQuickIcon::resetHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon11resetHeightEv(QQuickIcon *self) {
  self->resetHeight();
}

//  QColor QQuickIcon::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10QQuickIcon5colorEv(const QQuickIcon *self) {
  return new QColor(self->color());
}

//  void QQuickIcon::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon8setColorERK6QColor(
    QQuickIcon *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickIcon::resetColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon10resetColorEv(QQuickIcon *self) {
  self->resetColor();
}

//  void QQuickIcon::resolveColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon12resolveColorEv(QQuickIcon *self) {
  self->resolveColor();
}

//  bool QQuickIcon::cache() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickIcon5cacheEv(const QQuickIcon *self) {
  return self->cache();
}

//  void QQuickIcon::setCache(bool cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon8setCacheEb(QQuickIcon *self, bool cache) {
  self->setCache(cache);
}

//  void QQuickIcon::resetCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickIcon10resetCacheEv(QQuickIcon *self) {
  self->resetCache();
}

//  QQuickIcon QQuickIcon::resolve(const QQuickIcon &other) const
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZNK10QQuickIcon7resolveERKS_(
    const QQuickIcon *self,
    const QQuickIcon *other) {
  return new QQuickIcon(self->resolve(*other));
}
