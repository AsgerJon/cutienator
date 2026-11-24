//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QQuickPen::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QQuickPen10metaObjectEv(
    const QQuickPen *self) {
  return self->metaObject();
}

//  QString QQuickPen::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QQuickPen2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPen::tr(s, c, n));
}

//  void QQuickPen::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickPen22qt_qmlMarker_anonymousEv(QQuickPen *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickPen::QQuickPen(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPen *ritual_ZN9QQuickPenC1EP7QObject(QObject *parent) {
  return new QQuickPen(parent);
}

//  qreal QQuickPen::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QQuickPen5widthEv(const QQuickPen *self) {
  return self->width();
}

//  void QQuickPen::setWidth(qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickPen8setWidthEd(QQuickPen *self, qreal w) {
  self->setWidth(w);
}

//  QColor QQuickPen::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QQuickPen5colorEv(const QQuickPen *self) {
  return new QColor(self->color());
}

//  void QQuickPen::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickPen8setColorERK6QColor(
    QQuickPen *self,
    const QColor *c) {
  self->setColor(*c);
}

//  bool QQuickPen::pixelAligned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuickPen12pixelAlignedEv(const QQuickPen *self) {
  return self->pixelAligned();
}

//  void QQuickPen::setPixelAligned(bool aligned)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickPen15setPixelAlignedEb(QQuickPen *self, bool aligned) {
  self->setPixelAligned(aligned);
}

//  bool QQuickPen::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuickPen7isValidEv(const QQuickPen *self) {
  return self->isValid();
}
