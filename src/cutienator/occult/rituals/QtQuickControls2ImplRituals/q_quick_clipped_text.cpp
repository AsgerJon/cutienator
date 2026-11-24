//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickclippedtext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickclippedtext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QQuickClippedText::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickClippedText10metaObjectEv(
    const QQuickClippedText *self) {
  return self->metaObject();
}

//  QString QQuickClippedText::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickClippedText2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickClippedText::tr(s, c, n));
}

//  QQuickClippedText::QQuickClippedText(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickClippedText *ritual_ZN17QQuickClippedTextC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickClippedText(parent);
}

//  qreal QQuickClippedText::clipX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickClippedText5clipXEv(const QQuickClippedText *self) {
  return self->clipX();
}

//  void QQuickClippedText::setClipX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickClippedText8setClipXEd(
    QQuickClippedText *self,
    qreal x) {
  self->setClipX(x);
}

//  qreal QQuickClippedText::clipY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickClippedText5clipYEv(const QQuickClippedText *self) {
  return self->clipY();
}

//  void QQuickClippedText::setClipY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickClippedText8setClipYEd(
    QQuickClippedText *self,
    qreal y) {
  self->setClipY(y);
}

//  qreal QQuickClippedText::clipWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickClippedText9clipWidthEv(
    const QQuickClippedText *self) {
  return self->clipWidth();
}

//  void QQuickClippedText::setClipWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickClippedText12setClipWidthEd(
    QQuickClippedText *self,
    qreal width) {
  self->setClipWidth(width);
}

//  qreal QQuickClippedText::clipHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickClippedText10clipHeightEv(
    const QQuickClippedText *self) {
  return self->clipHeight();
}

//  void QQuickClippedText::setClipHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickClippedText13setClipHeightEd(
    QQuickClippedText *self,
    qreal height) {
  self->setClipHeight(height);
}

//  QRectF QQuickClippedText::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickClippedText8clipRectEv(
    const QQuickClippedText *self) {
  return new QRectF(self->clipRect());
}

//  void QQuickClippedText::markClipDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickClippedText13markClipDirtyEv(QQuickClippedText *self) {
  self->markClipDirty();
}

//  QRectF QQuickClippedText::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17QQuickClippedText8clipRectEv(
    const QQuickClippedText *self) {
  return new QRectF(self->QQuickClippedText::clipRect());
}
