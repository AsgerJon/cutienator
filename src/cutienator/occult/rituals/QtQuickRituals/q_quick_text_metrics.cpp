//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextmetrics_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextmetrics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QQuickTextMetrics::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickTextMetrics10metaObjectEv(
    const QQuickTextMetrics *self) {
  return self->metaObject();
}

//  QString QQuickTextMetrics::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickTextMetrics2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextMetrics::tr(s, c, n));
}

//  QQuickTextMetrics::QQuickTextMetrics(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTextMetrics *ritual_ZN17QQuickTextMetricsC1EP7QObject(
    QObject *parent) {
  return new QQuickTextMetrics(parent);
}

//  QFont QQuickTextMetrics::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QQuickTextMetrics4fontEv(const QQuickTextMetrics *self) {
  return new QFont(self->font());
}

//  void QQuickTextMetrics::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextMetrics7setFontERK5QFont(
    QQuickTextMetrics *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QString QQuickTextMetrics::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextMetrics4textEv(
    const QQuickTextMetrics *self) {
  return new QString(self->text());
}

//  void QQuickTextMetrics::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextMetrics7setTextERK7QString(
    QQuickTextMetrics *self,
    const QString *text) {
  self->setText(*text);
}

//  Qt::TextElideMode QQuickTextMetrics::elide() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK17QQuickTextMetrics5elideEv(
    const QQuickTextMetrics *self) {
  return self->elide();
}

//  void QQuickTextMetrics::setElide(Qt::TextElideMode elide)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextMetrics8setElideEN2Qt13TextElideModeE(
    QQuickTextMetrics *self,
    Qt::TextElideMode elide) {
  self->setElide(elide);
}

//  qreal QQuickTextMetrics::elideWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextMetrics10elideWidthEv(
    const QQuickTextMetrics *self) {
  return self->elideWidth();
}

//  void QQuickTextMetrics::setElideWidth(qreal elideWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextMetrics13setElideWidthEd(
    QQuickTextMetrics *self,
    qreal elideWidth) {
  self->setElideWidth(elideWidth);
}

//  qreal QQuickTextMetrics::advanceWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextMetrics12advanceWidthEv(
    const QQuickTextMetrics *self) {
  return self->advanceWidth();
}

//  QRectF QQuickTextMetrics::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickTextMetrics12boundingRectEv(
    const QQuickTextMetrics *self) {
  return new QRectF(self->boundingRect());
}

//  qreal QQuickTextMetrics::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextMetrics5widthEv(const QQuickTextMetrics *self) {
  return self->width();
}

//  qreal QQuickTextMetrics::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextMetrics6heightEv(const QQuickTextMetrics *self) {
  return self->height();
}

//  QRectF QQuickTextMetrics::tightBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickTextMetrics17tightBoundingRectEv(
    const QQuickTextMetrics *self) {
  return new QRectF(self->tightBoundingRect());
}

//  QString QQuickTextMetrics::elidedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextMetrics10elidedTextEv(
    const QQuickTextMetrics *self) {
  return new QString(self->elidedText());
}

//  QQuickText::RenderType QQuickTextMetrics::renderType() const
extern "C" Q_DECL_EXPORT
QQuickText::RenderType ritual_ZNK17QQuickTextMetrics10renderTypeEv(
    const QQuickTextMetrics *self) {
  return self->renderType();
}

//  void QQuickTextMetrics::setRenderType(QQuickText::RenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextMetrics13setRenderTypeEN10QQuickText10RenderTypeE(
    QQuickTextMetrics *self,
    QQuickText::RenderType renderType) {
  self->setRenderType(renderType);
}
