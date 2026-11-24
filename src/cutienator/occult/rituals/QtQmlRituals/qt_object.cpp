//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlocale.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QtObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QtObject10metaObjectEv(const QtObject *self) {
  return self->metaObject();
}

//  QString QtObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QtObject2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QtObject::tr(s, c, n));
}

//  void QtObject::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QtObject22qt_qmlMarker_singletonEv(QtObject *self) {
  self->qt_qmlMarker_singleton();
}

//  const QMetaObject *QtObject::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN8QtObject20qmlExtendedNamespaceEv() {
  return QtObject::qmlExtendedNamespace();
}

//  void QtObject::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QtObject30qt_qmlMarker_extendedNamespaceEv(QtObject *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QtObject *QtObject::create(QQmlEngine *a0, QJSEngine *jsEngine)
extern "C" Q_DECL_EXPORT
QtObject *ritual_ZN8QtObject6createEP10QQmlEngineP9QJSEngine(
    QQmlEngine *a0,
    QJSEngine *jsEngine) {
  return QtObject::create(a0, jsEngine);
}

//  QJSValue QtObject::include(const QString &url, const QJSValue &callback)
//      const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QtObject7includeERK7QStringRK8QJSValue(
    const QtObject *self,
    const QString *url,
    const QJSValue *callback) {
  return new QJSValue(self->include(*url, *callback));
}

//  bool QtObject::isQtObject(const QJSValue &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QtObject10isQtObjectERK8QJSValue(
    const QtObject *self,
    const QJSValue *value) {
  return self->isQtObject(*value);
}

//  QVariant QtObject::color(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject5colorERK7QString(
    const QtObject *self,
    const QString *name) {
  return new QVariant(self->color(*name));
}

//  QVariant QtObject::rgba(double r, double g, double b, double a) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject4rgbaEdddd(
    const QtObject *self,
    double r,
    double g,
    double b,
    double a) {
  return new QVariant(self->rgba(r, g, b, a));
}

//  QVariant QtObject::hsla(double h, double s, double l, double a) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject4hslaEdddd(
    const QtObject *self,
    double h,
    double s,
    double l,
    double a) {
  return new QVariant(self->hsla(h, s, l, a));
}

//  QVariant QtObject::hsva(double h, double s, double v, double a) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject4hsvaEdddd(
    const QtObject *self,
    double h,
    double s,
    double v,
    double a) {
  return new QVariant(self->hsva(h, s, v, a));
}

//  bool QtObject::colorEqual(const QVariant &lhs, const QVariant &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QtObject10colorEqualERK8QVariantS2_(
    const QtObject *self,
    const QVariant *lhs,
    const QVariant *rhs) {
  return self->colorEqual(*lhs, *rhs);
}

//  QRectF QtObject::rect(double x, double y, double width, double height)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QtObject4rectEdddd(
    const QtObject *self,
    double x,
    double y,
    double width,
    double height) {
  return new QRectF(self->rect(x, y, width, height));
}

//  QPointF QtObject::point(double x, double y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QtObject5pointEdd(
    const QtObject *self,
    double x,
    double y) {
  return new QPointF(self->point(x, y));
}

//  QSizeF QtObject::size(double width, double height) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK8QtObject4sizeEdd(
    const QtObject *self,
    double width,
    double height) {
  return new QSizeF(self->size(width, height));
}

//  QVariant QtObject::vector2d(double x, double y) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject8vector2dEdd(
    const QtObject *self,
    double x,
    double y) {
  return new QVariant(self->vector2d(x, y));
}

//  QVariant QtObject::vector3d(double x, double y, double z) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject8vector3dEddd(
    const QtObject *self,
    double x,
    double y,
    double z) {
  return new QVariant(self->vector3d(x, y, z));
}

//  QVariant QtObject::vector4d(double x, double y, double z, double w) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject8vector4dEdddd(
    const QtObject *self,
    double x,
    double y,
    double z,
    double w) {
  return new QVariant(self->vector4d(x, y, z, w));
}

//  QVariant QtObject::quaternion(double scalar, double x, double y, double
//      z) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject10quaternionEdddd(
    const QtObject *self,
    double scalar,
    double x,
    double y,
    double z) {
  return new QVariant(self->quaternion(scalar, x, y, z));
}

//  QVariant QtObject::matrix4x4() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject9matrix4x4Ev(const QtObject *self) {
  return new QVariant(self->matrix4x4());
}

//  QVariant QtObject::matrix4x4(double m11, double m12, double m13, double
//      m14, double m21, double m22, double m23, double m24, double m31,
//      double m32, double m33, double m34, double m41, double m42, double
//      m43, double m44) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject9matrix4x4Edddddddddddddddd(
    const QtObject *self,
    double m11,
    double m12,
    double m13,
    double m14,
    double m21,
    double m22,
    double m23,
    double m24,
    double m31,
    double m32,
    double m33,
    double m34,
    double m41,
    double m42,
    double m43,
    double m44) {
  return new QVariant(
      self->matrix4x4(
          m11,
          m12,
          m13,
          m14,
          m21,
          m22,
          m23,
          m24,
          m31,
          m32,
          m33,
          m34,
          m41,
          m42,
          m43,
          m44));
}

//  QVariant QtObject::matrix4x4(const QJSValue &value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject9matrix4x4ERK8QJSValue(
    const QtObject *self,
    const QJSValue *value) {
  return new QVariant(self->matrix4x4(*value));
}

//  QVariant QtObject::lighter(const QJSValue &color, double factor) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject7lighterERK8QJSValued(
    const QtObject *self,
    const QJSValue *color,
    double factor) {
  return new QVariant(self->lighter(*color, factor));
}

//  QVariant QtObject::darker(const QJSValue &color, double factor) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject6darkerERK8QJSValued(
    const QtObject *self,
    const QJSValue *color,
    double factor) {
  return new QVariant(self->darker(*color, factor));
}

//  QVariant QtObject::alpha(const QJSValue &baseColor, double value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject5alphaERK8QJSValued(
    const QtObject *self,
    const QJSValue *baseColor,
    double value) {
  return new QVariant(self->alpha(*baseColor, value));
}

//  QVariant QtObject::tint(const QJSValue &baseColor, const QJSValue
//      &tintColor) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject4tintERK8QJSValueS2_(
    const QtObject *self,
    const QJSValue *baseColor,
    const QJSValue *tintColor) {
  return new QVariant(self->tint(*baseColor, *tintColor));
}

//  QString QtObject::formatDate(QDate date, const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateE5QDateRK7QString(
    const QtObject *self,
    const QDate *date,
    const QString *format) {
  return new QString(self->formatDate(*date, *format));
}

//  QString QtObject::formatDate(const QDateTime &dateTime, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateERK9QDateTimeRK7QString(
    const QtObject *self,
    const QDateTime *dateTime,
    const QString *format) {
  return new QString(self->formatDate(*dateTime, *format));
}

//  QString QtObject::formatDate(const QString &string, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateERK7QStringS2_(
    const QtObject *self,
    const QString *string,
    const QString *format) {
  return new QString(self->formatDate(*string, *format));
}

//  QString QtObject::formatDate(QDate date, Qt::DateFormat format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateE5QDateN2Qt10DateFormatE(
    const QtObject *self,
    const QDate *date,
    Qt::DateFormat format) {
  return new QString(self->formatDate(*date, format));
}

//  QString QtObject::formatDate(const QDateTime &dateTime, Qt::DateFormat
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateERK9QDateTimeN2Qt10DateFormatE(
    const QtObject *self,
    const QDateTime *dateTime,
    Qt::DateFormat format) {
  return new QString(self->formatDate(*dateTime, format));
}

//  QString QtObject::formatDate(const QString &string, Qt::DateFormat
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateERK7QStringN2Qt10DateFormatE(
    const QtObject *self,
    const QString *string,
    Qt::DateFormat format) {
  return new QString(self->formatDate(*string, format));
}

//  QString QtObject::formatTime(QTime time, const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeE5QTimeRK7QString(
    const QtObject *self,
    const QTime *time,
    const QString *format) {
  return new QString(self->formatTime(*time, *format));
}

//  QString QtObject::formatTime(const QDateTime &dateTime, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeERK9QDateTimeRK7QString(
    const QtObject *self,
    const QDateTime *dateTime,
    const QString *format) {
  return new QString(self->formatTime(*dateTime, *format));
}

//  QString QtObject::formatTime(const QString &time, const QString &format)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeERK7QStringS2_(
    const QtObject *self,
    const QString *time,
    const QString *format) {
  return new QString(self->formatTime(*time, *format));
}

//  QString QtObject::formatTime(QTime time, Qt::DateFormat format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeE5QTimeN2Qt10DateFormatE(
    const QtObject *self,
    const QTime *time,
    Qt::DateFormat format) {
  return new QString(self->formatTime(*time, format));
}

//  QString QtObject::formatTime(const QDateTime &dateTime, Qt::DateFormat
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeERK9QDateTimeN2Qt10DateFormatE(
    const QtObject *self,
    const QDateTime *dateTime,
    Qt::DateFormat format) {
  return new QString(self->formatTime(*dateTime, format));
}

//  QString QtObject::formatTime(const QString &time, Qt::DateFormat format)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeERK7QStringN2Qt10DateFormatE(
    const QtObject *self,
    const QString *time,
    Qt::DateFormat format) {
  return new QString(self->formatTime(*time, format));
}

//  QString QtObject::formatDateTime(const QDateTime &date, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject14formatDateTimeERK9QDateTimeRK7QString(
    const QtObject *self,
    const QDateTime *date,
    const QString *format) {
  return new QString(self->formatDateTime(*date, *format));
}

//  QString QtObject::formatDateTime(const QString &string, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject14formatDateTimeERK7QStringS2_(
    const QtObject *self,
    const QString *string,
    const QString *format) {
  return new QString(self->formatDateTime(*string, *format));
}

//  QString QtObject::formatDateTime(const QDateTime &date, Qt::DateFormat
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject14formatDateTimeERK9QDateTimeN2Qt10DateFormatE(
    const QtObject *self,
    const QDateTime *date,
    Qt::DateFormat format) {
  return new QString(self->formatDateTime(*date, format));
}

//  QString QtObject::formatDateTime(const QString &string, Qt::DateFormat
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject14formatDateTimeERK7QStringN2Qt10DateFormatE(
    const QtObject *self,
    const QString *string,
    Qt::DateFormat format) {
  return new QString(self->formatDateTime(*string, format));
}

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatDate(QDate date, const QLocale &locale,
//      QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateE5QDateRK7QLocaleNS1_10FormatTypeE(
    const QtObject *self,
    const QDate *date,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatDate(*date, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatDate(const QDateTime &dateTime, const QLocale
//      &locale, QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateERK9QDateTimeRK7QLocaleNS3_10FormatTypeE(
    const QtObject *self,
    const QDateTime *dateTime,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatDate(*dateTime, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatDate(const QString &string, const QLocale
//      &locale, QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatDateERK7QStringRK7QLocaleNS3_10FormatTypeE(
    const QtObject *self,
    const QString *string,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatDate(*string, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatTime(QTime time, const QLocale &locale,
//      QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeE5QTimeRK7QLocaleNS1_10FormatTypeE(
    const QtObject *self,
    const QTime *time,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatTime(*time, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatTime(const QDateTime &dateTime, const QLocale
//      &locale, QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeERK9QDateTimeRK7QLocaleNS3_10FormatTypeE(
    const QtObject *self,
    const QDateTime *dateTime,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatTime(*dateTime, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatTime(const QString &time, const QLocale &locale,
//      QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10formatTimeERK7QStringRK7QLocaleNS3_10FormatTypeE(
    const QtObject *self,
    const QString *time,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatTime(*time, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatDateTime(const QDateTime &date, const QLocale
//      &locale, QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject14formatDateTimeERK9QDateTimeRK7QLocaleNS3_10FormatTypeE(
    const QtObject *self,
    const QDateTime *date,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatDateTime(*date, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QString QtObject::formatDateTime(const QString &string, const QLocale
//      &locale, QLocale::FormatType formatType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject14formatDateTimeERK7QStringRK7QLocaleNS3_10FormatTypeE(
    const QtObject *self,
    const QString *string,
    const QLocale *locale,
    QLocale::FormatType formatType) {
  return new QString(self->formatDateTime(*string, *locale, formatType));
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QLocale QtObject::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK8QtObject6localeEv(const QtObject *self) {
  return new QLocale(self->locale());
}
#endif  // QT_CONFIG(qml_locale)

#if QT_CONFIG(qml_locale)
//  QLocale QtObject::locale(const QString &name) const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK8QtObject6localeERK7QString(
    const QtObject *self,
    const QString *name) {
  return new QLocale(self->locale(*name));
}
#endif  // QT_CONFIG(qml_locale)

//  QUrl QtObject::url(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QtObject3urlERK4QUrl(
    const QtObject *self,
    const QUrl *url) {
  return new QUrl(self->url(*url));
}

//  QUrl QtObject::resolvedUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QtObject11resolvedUrlERK4QUrl(
    const QtObject *self,
    const QUrl *url) {
  return new QUrl(self->resolvedUrl(*url));
}

//  QUrl QtObject::resolvedUrl(const QUrl &url, QObject *context) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QtObject11resolvedUrlERK4QUrlP7QObject(
    const QtObject *self,
    const QUrl *url,
    QObject *context) {
  return new QUrl(self->resolvedUrl(*url, context));
}

//  bool QtObject::openUrlExternally(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QtObject17openUrlExternallyERK4QUrl(
    const QtObject *self,
    const QUrl *url) {
  return self->openUrlExternally(*url);
}

//  QVariant QtObject::font(const QJSValue &fontSpecifier) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QtObject4fontERK8QJSValue(
    const QtObject *self,
    const QJSValue *fontSpecifier) {
  return new QVariant(self->font(*fontSpecifier));
}

//  QStringList QtObject::fontFamilies() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QtObject12fontFamiliesEv(const QtObject *self) {
  return new QList<QString>(self->fontFamilies());
}

//  QString QtObject::md5(const QString &data) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject3md5ERK7QString(
    const QtObject *self,
    const QString *data) {
  return new QString(self->md5(*data));
}

//  QString QtObject::btoa(const QString &data) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject4btoaERK7QString(
    const QtObject *self,
    const QString *data) {
  return new QString(self->btoa(*data));
}

//  QString QtObject::atob(const QString &data) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject4atobERK7QString(
    const QtObject *self,
    const QString *data) {
  return new QString(self->atob(*data));
}

//  QString QtObject::escapeHtml(const QString &data) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10escapeHtmlERK7QString(
    const QtObject *self,
    const QString *data) {
  return new QString(self->escapeHtml(*data));
}

//  QByteArray QtObject::btoa(const QByteArray &data) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QtObject4btoaERK10QByteArray(
    const QtObject *self,
    const QByteArray *data) {
  return new QByteArray(self->btoa(*data));
}

//  QByteArray QtObject::atob(const QByteArray &data) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QtObject4atobERK10QByteArray(
    const QtObject *self,
    const QByteArray *data) {
  return new QByteArray(self->atob(*data));
}

//  QByteArray QtObject::btoa(const QVariantList &data) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QtObject4btoaERK5QListI8QVariantE(
    const QtObject *self,
    const QList<QVariant> *data) {
  return new QByteArray(self->btoa(*data));
}

//  QByteArray QtObject::atob(const QVariantList &data) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QtObject4atobERK5QListI8QVariantE(
    const QtObject *self,
    const QList<QVariant> *data) {
  return new QByteArray(self->atob(*data));
}

//  void QtObject::quit() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QtObject4quitEv(const QtObject *self) {
  self->quit();
}

//  void QtObject::exit(int retCode) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QtObject4exitEi(const QtObject *self, int retCode) {
  self->exit(retCode);
}

//  QObject *QtObject::createQmlObject(const QString &qml, QObject *parent,
//      const QUrl &url) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8QtObject15createQmlObjectERK7QStringP7QObjectRK4QUrl(
    const QtObject *self,
    const QString *qml,
    QObject *parent,
    const QUrl *url) {
  return self->createQmlObject(*qml, parent, *url);
}

//  QQmlComponent *QtObject::createComponent(const QUrl &url, QObject
//      *parent) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK8QtObject15createComponentERK4QUrlP7QObject(
    const QtObject *self,
    const QUrl *url,
    QObject *parent) {
  return self->createComponent(*url, parent);
}

//  QQmlComponent *QtObject::createComponent(const QUrl &url,
//      QQmlComponent::CompilationMode mode, QObject *parent) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK8QtObject15createComponentERK4QUrlN13QQmlComponent15CompilationModeEP7QObject(
    const QtObject *self,
    const QUrl *url,
    QQmlComponent::CompilationMode mode,
    QObject *parent) {
  return self->createComponent(*url, mode, parent);
}

//  QQmlComponent *QtObject::createComponent(const QString &moduleUri, const
//      QString &typeName, QObject *parent) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK8QtObject15createComponentERK7QStringS2_P7QObject(
    const QtObject *self,
    const QString *moduleUri,
    const QString *typeName,
    QObject *parent) {
  return self->createComponent(*moduleUri, *typeName, parent);
}

//  QQmlComponent *QtObject::createComponent(const QString &moduleUri, const
//      QString &typeName, QQmlComponent::CompilationMode mode, QObject
//      *parent) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK8QtObject15createComponentERK7QStringS2_N13QQmlComponent15CompilationModeEP7QObject(
    const QtObject *self,
    const QString *moduleUri,
    const QString *typeName,
    QQmlComponent::CompilationMode mode,
    QObject *parent) {
  return self->createComponent(*moduleUri, *typeName, mode, parent);
}

//  QJSValue QtObject::binding(const QJSValue &function) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QtObject7bindingERK8QJSValue(
    const QtObject *self,
    const QJSValue *function) {
  return new QJSValue(self->binding(*function));
}

//  void QtObject::callLater(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QtObject9callLaterEP14QQmlV4Function(
    QtObject *self,
    QQmlV4FunctionPtr args) {
  self->callLater(args);
}

#if QT_CONFIG(translation)
//  QString QtObject::uiLanguage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QtObject10uiLanguageEv(const QtObject *self) {
  return new QString(self->uiLanguage());
}
#endif  // QT_CONFIG(translation)

#if QT_CONFIG(translation)
//  void QtObject::setUiLanguage(const QString &uiLanguage)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QtObject13setUiLanguageERK7QString(
    QtObject *self,
    const QString *uiLanguage) {
  self->setUiLanguage(*uiLanguage);
}
#endif  // QT_CONFIG(translation)

//  QQmlPlatform *QtObject::platform()
extern "C" Q_DECL_EXPORT
QQmlPlatform *ritual_ZN8QtObject8platformEv(QtObject *self) {
  return self->platform();
}

//  QQmlApplication *QtObject::application()
extern "C" Q_DECL_EXPORT
QQmlApplication *ritual_ZN8QtObject11applicationEv(QtObject *self) {
  return self->application();
}

//  QObject *QtObject::inputMethod() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8QtObject11inputMethodEv(const QtObject *self) {
  return self->inputMethod();
}

//  QObject *QtObject::styleHints() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8QtObject10styleHintsEv(const QtObject *self) {
  return self->styleHints();
}

//  QtObject::QtObject(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QtObject *ritual_ZN8QtObjectC1EPN3QV415ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QtObject(engine);
}

//  QQmlEngine *QtObject::qmlEngine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK8QtObject9qmlEngineEv(const QtObject *self) {
  return self->qmlEngine();
}

//  QJSEngine *QtObject::jsEngine() const
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZNK8QtObject8jsEngineEv(const QtObject *self) {
  return self->jsEngine();
}

//  QV4::ExecutionEngine *QtObject::v4Engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK8QtObject8v4EngineEv(const QtObject *self) {
  return self->v4Engine();
}
