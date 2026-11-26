//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitem_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator
//  runs again. The whole file stands under the condition Qt builds
//  the module under (macOS and Windows only, as
//  quickcontrols/CMakeLists.txt says).
//  Qt's library offers nothing of this class by name: only its
//  inline functions and its virtual functions are called, through
//  the object.
//  Not written: the constructor, since Qt does not export the
//  class, and what is not inline and not virtual (contentWidth,
//  markGeometryDirty and the like, the signals, controlSize,
//  initStyleOptionBase). Not written either: 'style', which calls
//  'QQC2::style' that Qt's library offers not, and the template
//  'control'. No include of QtWidgets, whose 'QStyle' would be
//  ambiguous with that of QQC2 under the header's 'using'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/qtquicknativestyleexports.h>
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitem_p.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickStyleItem10metaObjectEv(
    const QQuickStyleItem *self) {
  return self->metaObject();
}

//  QQuickStyleItem::~QQuickStyleItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStyleItemD1Ev(QQuickStyleItem *self) {
  delete self;
}

//  QSize QQuickStyleItem::contentSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QQuickStyleItem11contentSizeEv(
    const QQuickStyleItem *self) {
  return new QSize(self->contentSize());
}

//  QFont QQuickStyleItem::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QQuickStyleItem9styleFontEP10QQuickItem(
    const QQuickStyleItem *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStyleItem17componentCompleteEv(
    QQuickStyleItem *self) {
  self->componentComplete();
}

//  QSGNode *QQuickStyleItem::updatePaintNode(QSGNode *oldNode,
//      QQuickItem::UpdatePaintNodeData *updatePaintNodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN15QQuickStyleItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickStyleItem *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData) {
  return self->updatePaintNode(oldNode, updatePaintNodeData);
}

//  void QQuickStyleItem::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStyleItem14geometryChangeERK6QRectFS2_(
    QQuickStyleItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickStyleItem::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStyleItem10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickStyleItem *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickStyleItem::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickStyleItem12updatePolishEv(QQuickStyleItem *self) {
  self->updatePolish();
}

//  void QQuickStyleItem::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQuickStyleItem16connectToControlEv(
    const QQuickStyleItem *self) {
  self->connectToControl();
}

//  void QQuickStyleItem::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQuickStyleItem10paintEventEP8QPainter(
    const QQuickStyleItem *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItem::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN15QQuickStyleItem17calculateGeometryEv(
    QQuickStyleItem *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

//  bool QQuickStyleItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickStyleItem5eventEP6QEvent(
    QQuickStyleItem *self,
    QEvent *event) {
  return self->event(event);
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
