//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickTextLine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTextLine10metaObjectEv(
    const QQuickTextLine *self) {
  return self->metaObject();
}

//  void *QQuickTextLine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickTextLine11qt_metacastEPKc(
    QQuickTextLine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextLine::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTextLine11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextLine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTextLine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickTextLine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextLine::tr(s, c, n));
}

//  void QQuickTextLine::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine22qt_qmlMarker_anonymousEv(
    QQuickTextLine *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickTextLine::QQuickTextLine()
extern "C" Q_DECL_EXPORT
QQuickTextLine *ritual_ZN14QQuickTextLineC1Ev() {
  return new QQuickTextLine();
}

//  void QQuickTextLine::setLine(QTextLine *line)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine7setLineEP9QTextLine(
    QQuickTextLine *self,
    QTextLine *line) {
  self->setLine(line);
}

//  void QQuickTextLine::setLineOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine13setLineOffsetEi(
    QQuickTextLine *self,
    int offset) {
  self->setLineOffset(offset);
}

//  void QQuickTextLine::setFullLayoutTextLength(int length)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine23setFullLayoutTextLengthEi(
    QQuickTextLine *self,
    int length) {
  self->setFullLayoutTextLength(length);
}

//  int QQuickTextLine::number() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextLine6numberEv(const QQuickTextLine *self) {
  return self->number();
}

//  qreal QQuickTextLine::implicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextLine13implicitWidthEv(
    const QQuickTextLine *self) {
  return self->implicitWidth();
}

//  bool QQuickTextLine::isLast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextLine6isLastEv(const QQuickTextLine *self) {
  return self->isLast();
}

//  qreal QQuickTextLine::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextLine5widthEv(const QQuickTextLine *self) {
  return self->width();
}

//  void QQuickTextLine::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine8setWidthEd(
    QQuickTextLine *self,
    qreal width) {
  self->setWidth(width);
}

//  qreal QQuickTextLine::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextLine6heightEv(const QQuickTextLine *self) {
  return self->height();
}

//  void QQuickTextLine::setHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine9setHeightEd(
    QQuickTextLine *self,
    qreal height) {
  self->setHeight(height);
}

//  qreal QQuickTextLine::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextLine1xEv(const QQuickTextLine *self) {
  return self->x();
}

//  void QQuickTextLine::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine4setXEd(QQuickTextLine *self, qreal x) {
  self->setX(x);
}

//  qreal QQuickTextLine::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextLine1yEv(const QQuickTextLine *self) {
  return self->y();
}

//  void QQuickTextLine::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextLine4setYEd(QQuickTextLine *self, qreal y) {
  self->setY(y);
}
