//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickfontmetrics_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickfontmetrics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QQuickFontMetrics::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickFontMetrics10metaObjectEv(
    const QQuickFontMetrics *self) {
  return self->metaObject();
}

//  void *QQuickFontMetrics::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickFontMetrics11qt_metacastEPKc(
    QQuickFontMetrics *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFontMetrics::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickFontMetrics11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFontMetrics *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFontMetrics::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickFontMetrics2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFontMetrics::tr(s, c, n));
}

//  QQuickFontMetrics::QQuickFontMetrics(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFontMetrics *ritual_ZN17QQuickFontMetricsC1EP7QObject(
    QObject *parent) {
  return new QQuickFontMetrics(parent);
}

//  QFont QQuickFontMetrics::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QQuickFontMetrics4fontEv(const QQuickFontMetrics *self) {
  return new QFont(self->font());
}

//  void QQuickFontMetrics::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickFontMetrics7setFontERK5QFont(
    QQuickFontMetrics *self,
    const QFont *font) {
  self->setFont(*font);
}

//  qreal QQuickFontMetrics::ascent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics6ascentEv(const QQuickFontMetrics *self) {
  return self->ascent();
}

//  qreal QQuickFontMetrics::descent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics7descentEv(
    const QQuickFontMetrics *self) {
  return self->descent();
}

//  qreal QQuickFontMetrics::capitalHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics13capitalHeightEv(
    const QQuickFontMetrics *self) {
  return self->capitalHeight();
}

//  qreal QQuickFontMetrics::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics6heightEv(const QQuickFontMetrics *self) {
  return self->height();
}

//  qreal QQuickFontMetrics::leading() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics7leadingEv(
    const QQuickFontMetrics *self) {
  return self->leading();
}

//  qreal QQuickFontMetrics::lineSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics11lineSpacingEv(
    const QQuickFontMetrics *self) {
  return self->lineSpacing();
}

//  qreal QQuickFontMetrics::minimumLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics18minimumLeftBearingEv(
    const QQuickFontMetrics *self) {
  return self->minimumLeftBearing();
}

//  qreal QQuickFontMetrics::minimumRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics19minimumRightBearingEv(
    const QQuickFontMetrics *self) {
  return self->minimumRightBearing();
}

//  qreal QQuickFontMetrics::maximumCharacterWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics21maximumCharacterWidthEv(
    const QQuickFontMetrics *self) {
  return self->maximumCharacterWidth();
}

//  qreal QQuickFontMetrics::xHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics7xHeightEv(
    const QQuickFontMetrics *self) {
  return self->xHeight();
}

//  qreal QQuickFontMetrics::averageCharacterWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics21averageCharacterWidthEv(
    const QQuickFontMetrics *self) {
  return self->averageCharacterWidth();
}

//  qreal QQuickFontMetrics::underlinePosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics17underlinePositionEv(
    const QQuickFontMetrics *self) {
  return self->underlinePosition();
}

//  qreal QQuickFontMetrics::overlinePosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics16overlinePositionEv(
    const QQuickFontMetrics *self) {
  return self->overlinePosition();
}

//  qreal QQuickFontMetrics::strikeOutPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics17strikeOutPositionEv(
    const QQuickFontMetrics *self) {
  return self->strikeOutPosition();
}

//  qreal QQuickFontMetrics::lineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics9lineWidthEv(
    const QQuickFontMetrics *self) {
  return self->lineWidth();
}

//  qreal QQuickFontMetrics::advanceWidth(const QString &text) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickFontMetrics12advanceWidthERK7QString(
    const QQuickFontMetrics *self,
    const QString *text) {
  return self->advanceWidth(*text);
}

//  QRectF QQuickFontMetrics::boundingRect(const QString &text) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickFontMetrics12boundingRectERK7QString(
    const QQuickFontMetrics *self,
    const QString *text) {
  return new QRectF(self->boundingRect(*text));
}

//  QRectF QQuickFontMetrics::tightBoundingRect(const QString &text) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickFontMetrics17tightBoundingRectERK7QString(
    const QQuickFontMetrics *self,
    const QString *text) {
  return new QRectF(self->tightBoundingRect(*text));
}

//  QString QQuickFontMetrics::elidedText(const QString &text,
//      Qt::TextElideMode mode, qreal width, int flags) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickFontMetrics10elidedTextERK7QStringN2Qt13TextElideModeEdi(
    const QQuickFontMetrics *self,
    const QString *text,
    Qt::TextElideMode mode,
    qreal width,
    int flags) {
  return new QString(self->elidedText(*text, mode, width, flags));
}

//  void QQuickFontMetrics::fontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickFontMetrics11fontChangedERK5QFont(
    QQuickFontMetrics *self,
    const QFont *font) {
  self->fontChanged(*font);
}
