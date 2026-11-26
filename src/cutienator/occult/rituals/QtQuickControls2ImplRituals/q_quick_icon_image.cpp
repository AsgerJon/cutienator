//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconimage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qurl.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

//  Only a class built on QQuickIconImage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickIconImage : QQuickIconImage {
  using QQuickIconImage::componentComplete;
  using QQuickIconImage::load;
  using QQuickIconImage::geometryChange;
  using QQuickIconImage::pixmapChange;
};

//  const QMetaObject *QQuickIconImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickIconImage10metaObjectEv(
    const QQuickIconImage *self) {
  return self->metaObject();
}

//  void *QQuickIconImage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickIconImage11qt_metacastEPKc(
    QQuickIconImage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickIconImage::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickIconImage11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickIconImage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickIconImage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickIconImage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickIconImage::tr(s, c, n));
}

//  QQuickIconImage::QQuickIconImage(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickIconImage *ritual_ZN15QQuickIconImageC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickIconImage(parent);
}

//  QString QQuickIconImage::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickIconImage4nameEv(const QQuickIconImage *self) {
  return new QString(self->name());
}

//  void QQuickIconImage::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage7setNameERK7QString(
    QQuickIconImage *self,
    const QString *name) {
  self->setName(*name);
}

//  QColor QQuickIconImage::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickIconImage5colorEv(const QQuickIconImage *self) {
  return new QColor(self->color());
}

//  void QQuickIconImage::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage8setColorERK6QColor(
    QQuickIconImage *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickIconImage::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage9setSourceERK4QUrl(
    QQuickIconImage *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  void QQuickIconImage::snapPositionTo(QPointF pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage14snapPositionToE7QPointF(
    QQuickIconImage *self,
    const QPointF *pos) {
  self->snapPositionTo(*pos);
}

//  void QQuickIconImage::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage11nameChangedEv(QQuickIconImage *self) {
  self->nameChanged();
}

//  void QQuickIconImage::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage12colorChangedEv(QQuickIconImage *self) {
  self->colorChanged();
}

//  void QQuickIconImage::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage17componentCompleteEv(QQuickIconImage *self) {
  self->componentComplete();
}

//  void QQuickIconImage::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage4loadEv(QQuickIconImage *self) {
  self->load();
}

//  void QQuickIconImage::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage14geometryChangeERK6QRectFS2_(
    QQuickIconImage *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickIconImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconImage12pixmapChangeEv(QQuickIconImage *self) {
  self->pixmapChange();
}

//  QQuickIconImagePrivate *QQuickIconImage::d_func()
extern "C" Q_DECL_EXPORT
QQuickIconImagePrivate *ritual_ZN15QQuickIconImage6d_funcEv(
    QQuickIconImage *self) {
  return self->d_func();
}

//  const QQuickIconImagePrivate *QQuickIconImage::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickIconImagePrivate *ritual_ZNK15QQuickIconImage6d_funcEv(
    const QQuickIconImage *self) {
  return self->d_func();
}

//  void QQuickIconImage::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickIconImage9setSourceERK4QUrl(
    QQuickIconImage *self,
    const QUrl *url) {
  self->QQuickIconImage::setSource(*url);
}

//  void QQuickIconImage::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickIconImage17componentCompleteEv(
    QQuickIconImage *self) {
  static_cast<OwnQQuickIconImage *>(self)->OwnQQuickIconImage::componentComplete();
}

//  void QQuickIconImage::load()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickIconImage4loadEv(QQuickIconImage *self) {
  static_cast<OwnQQuickIconImage *>(self)->OwnQQuickIconImage::load();
}

//  void QQuickIconImage::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickIconImage14geometryChangeERK6QRectFS2_(
    QQuickIconImage *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickIconImage *>(self)->OwnQQuickIconImage::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickIconImage::pixmapChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickIconImage12pixmapChangeEv(QQuickIconImage *self) {
  static_cast<OwnQQuickIconImage *>(self)->OwnQQuickIconImage::pixmapChange();
}
