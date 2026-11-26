//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickpaddedrectangle_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickpaddedrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickPaddedRectangle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPaddedRectangle : QQuickPaddedRectangle {
  using QQuickPaddedRectangle::updatePaintNode;
};

//  const QMetaObject *QQuickPaddedRectangle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickPaddedRectangle10metaObjectEv(
    const QQuickPaddedRectangle *self) {
  return self->metaObject();
}

//  void *QQuickPaddedRectangle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickPaddedRectangle11qt_metacastEPKc(
    QQuickPaddedRectangle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPaddedRectangle::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickPaddedRectangle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPaddedRectangle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPaddedRectangle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickPaddedRectangle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPaddedRectangle::tr(s, c, n));
}

//  QQuickPaddedRectangle::QQuickPaddedRectangle(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPaddedRectangle *ritual_ZN21QQuickPaddedRectangleC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickPaddedRectangle(parent);
}

//  qreal QQuickPaddedRectangle::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickPaddedRectangle7paddingEv(
    const QQuickPaddedRectangle *self) {
  return self->padding();
}

//  void QQuickPaddedRectangle::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle10setPaddingEd(
    QQuickPaddedRectangle *self,
    qreal padding) {
  self->setPadding(padding);
}

//  void QQuickPaddedRectangle::resetPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle12resetPaddingEv(
    QQuickPaddedRectangle *self) {
  self->resetPadding();
}

//  qreal QQuickPaddedRectangle::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickPaddedRectangle10topPaddingEv(
    const QQuickPaddedRectangle *self) {
  return self->topPadding();
}

//  void QQuickPaddedRectangle::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle13setTopPaddingEd(
    QQuickPaddedRectangle *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickPaddedRectangle::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle15resetTopPaddingEv(
    QQuickPaddedRectangle *self) {
  self->resetTopPadding();
}

//  qreal QQuickPaddedRectangle::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickPaddedRectangle11leftPaddingEv(
    const QQuickPaddedRectangle *self) {
  return self->leftPadding();
}

//  void QQuickPaddedRectangle::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle14setLeftPaddingEd(
    QQuickPaddedRectangle *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickPaddedRectangle::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle16resetLeftPaddingEv(
    QQuickPaddedRectangle *self) {
  self->resetLeftPadding();
}

//  qreal QQuickPaddedRectangle::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickPaddedRectangle12rightPaddingEv(
    const QQuickPaddedRectangle *self) {
  return self->rightPadding();
}

//  void QQuickPaddedRectangle::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle15setRightPaddingEd(
    QQuickPaddedRectangle *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickPaddedRectangle::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle17resetRightPaddingEv(
    QQuickPaddedRectangle *self) {
  self->resetRightPadding();
}

//  qreal QQuickPaddedRectangle::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickPaddedRectangle13bottomPaddingEv(
    const QQuickPaddedRectangle *self) {
  return self->bottomPadding();
}

//  void QQuickPaddedRectangle::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle16setBottomPaddingEd(
    QQuickPaddedRectangle *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickPaddedRectangle::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle18resetBottomPaddingEv(
    QQuickPaddedRectangle *self) {
  self->resetBottomPadding();
}

//  void QQuickPaddedRectangle::paddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle14paddingChangedEv(
    QQuickPaddedRectangle *self) {
  self->paddingChanged();
}

//  void QQuickPaddedRectangle::topPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle17topPaddingChangedEv(
    QQuickPaddedRectangle *self) {
  self->topPaddingChanged();
}

//  void QQuickPaddedRectangle::leftPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle18leftPaddingChangedEv(
    QQuickPaddedRectangle *self) {
  self->leftPaddingChanged();
}

//  void QQuickPaddedRectangle::rightPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle19rightPaddingChangedEv(
    QQuickPaddedRectangle *self) {
  self->rightPaddingChanged();
}

//  void QQuickPaddedRectangle::bottomPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle20bottomPaddingChangedEv(
    QQuickPaddedRectangle *self) {
  self->bottomPaddingChanged();
}

//  QSGNode *QQuickPaddedRectangle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN21QQuickPaddedRectangle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickPaddedRectangle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickPaddedRectangle::setTopPadding(qreal padding, bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle13setTopPaddingEdb(
    QQuickPaddedRectangle *self,
    qreal padding,
    bool has) {
  self->setTopPadding(padding, has);
}

//  void QQuickPaddedRectangle::setLeftPadding(qreal padding, bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle14setLeftPaddingEdb(
    QQuickPaddedRectangle *self,
    qreal padding,
    bool has) {
  self->setLeftPadding(padding, has);
}

//  void QQuickPaddedRectangle::setRightPadding(qreal padding, bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle15setRightPaddingEdb(
    QQuickPaddedRectangle *self,
    qreal padding,
    bool has) {
  self->setRightPadding(padding, has);
}

//  void QQuickPaddedRectangle::setBottomPadding(qreal padding, bool has)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPaddedRectangle16setBottomPaddingEdb(
    QQuickPaddedRectangle *self,
    qreal padding,
    bool has) {
  self->setBottomPadding(padding, has);
}

//  QSGNode *QQuickPaddedRectangle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN21QQuickPaddedRectangle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickPaddedRectangle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickPaddedRectangle *>(self)->OwnQQuickPaddedRectangle::updatePaintNode(
      a0,
      a1);
}
