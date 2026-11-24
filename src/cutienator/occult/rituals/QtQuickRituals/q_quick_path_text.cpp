//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickPathText::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickPathText10metaObjectEv(
    const QQuickPathText *self) {
  return self->metaObject();
}

//  QString QQuickPathText::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickPathText2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathText::tr(s, c, n));
}

//  QQuickPathText::QQuickPathText(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathText *ritual_ZN14QQuickPathTextC1EP7QObject(QObject *parent) {
  return new QQuickPathText(parent);
}

//  qreal QQuickPathText::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathText1xEv(const QQuickPathText *self) {
  return self->x();
}

//  qreal QQuickPathText::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathText1yEv(const QQuickPathText *self) {
  return self->y();
}

//  QString QQuickPathText::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickPathText4textEv(const QQuickPathText *self) {
  return new QString(self->text());
}

//  QFont QQuickPathText::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickPathText4fontEv(const QQuickPathText *self) {
  return new QFont(self->font());
}

//  void QQuickPathText::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathText4setXEd(QQuickPathText *self, qreal x) {
  self->setX(x);
}

//  void QQuickPathText::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathText4setYEd(QQuickPathText *self, qreal y) {
  self->setY(y);
}

//  void QQuickPathText::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathText7setTextERK7QString(
    QQuickPathText *self,
    const QString *text) {
  self->setText(*text);
}

//  void QQuickPathText::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathText7setFontERK5QFont(
    QQuickPathText *self,
    const QFont *font) {
  self->setFont(*font);
}

//  qreal QQuickPathText::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathText5widthEv(const QQuickPathText *self) {
  return self->width();
}

//  qreal QQuickPathText::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathText6heightEv(const QQuickPathText *self) {
  return self->height();
}

//  void QQuickPathText::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathText10invalidateEv(QQuickPathText *self) {
  self->invalidate();
}

//  void QQuickPathText::updatePath() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QQuickPathText10updatePathEv(const QQuickPathText *self) {
  self->updatePath();
}

#endif  // QT_CONFIG(quick_path)
#endif  // QT_CONFIG(quick_path)
