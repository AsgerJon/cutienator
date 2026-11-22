//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtGui/qcursor.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qregion.h>
#include <QtGui/qpolygon.h>
#include <QtCore/qvariant.h>

//  QGraphicsItem::~QGraphicsItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItemD1Ev(QGraphicsItem *self) {
  delete self;
}

//  QGraphicsScene *QGraphicsItem::scene() const
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZNK13QGraphicsItem5sceneEv(
    const QGraphicsItem *self) {
  return self->scene();
}

//  QGraphicsItem *QGraphicsItem::parentItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsItem10parentItemEv(
    const QGraphicsItem *self) {
  return self->parentItem();
}

//  QGraphicsItem *QGraphicsItem::topLevelItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsItem12topLevelItemEv(
    const QGraphicsItem *self) {
  return self->topLevelItem();
}

//  QGraphicsObject *QGraphicsItem::parentObject() const
extern "C" Q_DECL_EXPORT
QGraphicsObject *ritual_ZNK13QGraphicsItem12parentObjectEv(
    const QGraphicsItem *self) {
  return self->parentObject();
}

//  QGraphicsWidget *QGraphicsItem::parentWidget() const
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZNK13QGraphicsItem12parentWidgetEv(
    const QGraphicsItem *self) {
  return self->parentWidget();
}

//  QGraphicsWidget *QGraphicsItem::topLevelWidget() const
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZNK13QGraphicsItem14topLevelWidgetEv(
    const QGraphicsItem *self) {
  return self->topLevelWidget();
}

//  QGraphicsWidget *QGraphicsItem::window() const
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZNK13QGraphicsItem6windowEv(
    const QGraphicsItem *self) {
  return self->window();
}

//  QGraphicsItem *QGraphicsItem::panel() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsItem5panelEv(const QGraphicsItem *self) {
  return self->panel();
}

//  void QGraphicsItem::setParentItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem13setParentItemEPS_(
    QGraphicsItem *self,
    QGraphicsItem *parent) {
  self->setParentItem(parent);
}

//  bool QGraphicsItem::isWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem8isWidgetEv(const QGraphicsItem *self) {
  return self->isWidget();
}

//  bool QGraphicsItem::isWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem8isWindowEv(const QGraphicsItem *self) {
  return self->isWindow();
}

//  bool QGraphicsItem::isPanel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem7isPanelEv(const QGraphicsItem *self) {
  return self->isPanel();
}

//  QGraphicsObject *QGraphicsItem::toGraphicsObject()
extern "C" Q_DECL_EXPORT
QGraphicsObject *ritual_ZN13QGraphicsItem16toGraphicsObjectEv(
    QGraphicsItem *self) {
  return self->toGraphicsObject();
}

//  const QGraphicsObject *QGraphicsItem::toGraphicsObject() const
extern "C" Q_DECL_EXPORT
const QGraphicsObject *ritual_ZNK13QGraphicsItem16toGraphicsObjectEv(
    const QGraphicsItem *self) {
  return self->toGraphicsObject();
}

//  QGraphicsItemGroup *QGraphicsItem::group() const
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZNK13QGraphicsItem5groupEv(
    const QGraphicsItem *self) {
  return self->group();
}

//  void QGraphicsItem::setGroup(QGraphicsItemGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem8setGroupEP18QGraphicsItemGroup(
    QGraphicsItem *self,
    QGraphicsItemGroup *group) {
  self->setGroup(group);
}

//  GraphicsItemFlags QGraphicsItem::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsItem5flagsEv(const QGraphicsItem *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QGraphicsItem::setFlag(GraphicsItemFlag flag, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem7setFlagENS_16GraphicsItemFlagEb(
    QGraphicsItem *self,
    QGraphicsItem::GraphicsItemFlag flag,
    bool enabled) {
  self->setFlag(flag, enabled);
}

//  void QGraphicsItem::setFlags(GraphicsItemFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem8setFlagsE6QFlagsINS_16GraphicsItemFlagEE(
    QGraphicsItem *self,
    int flags) {
  self->setFlags(QFlags<QGraphicsItem::GraphicsItemFlag>::fromInt(flags));
}

//  CacheMode QGraphicsItem::cacheMode() const
extern "C" Q_DECL_EXPORT
QGraphicsItem::CacheMode ritual_ZNK13QGraphicsItem9cacheModeEv(
    const QGraphicsItem *self) {
  return self->cacheMode();
}

//  void QGraphicsItem::setCacheMode(CacheMode mode, const QSize &cacheSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem12setCacheModeENS_9CacheModeERK5QSize(
    QGraphicsItem *self,
    QGraphicsItem::CacheMode mode,
    const QSize *cacheSize) {
  self->setCacheMode(mode, *cacheSize);
}

//  PanelModality QGraphicsItem::panelModality() const
extern "C" Q_DECL_EXPORT
QGraphicsItem::PanelModality ritual_ZNK13QGraphicsItem13panelModalityEv(
    const QGraphicsItem *self) {
  return self->panelModality();
}

//  void QGraphicsItem::setPanelModality(PanelModality panelModality)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem16setPanelModalityENS_13PanelModalityE(
    QGraphicsItem *self,
    QGraphicsItem::PanelModality panelModality) {
  self->setPanelModality(panelModality);
}

//  QString QGraphicsItem::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QGraphicsItem7toolTipEv(const QGraphicsItem *self) {
  return new QString(self->toolTip());
}

//  void QGraphicsItem::setToolTip(const QString &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem10setToolTipERK7QString(
    QGraphicsItem *self,
    const QString *toolTip) {
  self->setToolTip(*toolTip);
}

//  QCursor QGraphicsItem::cursor() const
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZNK13QGraphicsItem6cursorEv(const QGraphicsItem *self) {
  return new QCursor(self->cursor());
}

//  void QGraphicsItem::setCursor(const QCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem9setCursorERK7QCursor(
    QGraphicsItem *self,
    const QCursor *cursor) {
  self->setCursor(*cursor);
}

//  bool QGraphicsItem::hasCursor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem9hasCursorEv(const QGraphicsItem *self) {
  return self->hasCursor();
}

//  void QGraphicsItem::unsetCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem11unsetCursorEv(QGraphicsItem *self) {
  self->unsetCursor();
}

//  bool QGraphicsItem::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem9isVisibleEv(const QGraphicsItem *self) {
  return self->isVisible();
}

//  bool QGraphicsItem::isVisibleTo(const QGraphicsItem *parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem11isVisibleToEPKS_(
    const QGraphicsItem *self,
    const QGraphicsItem *parent) {
  return self->isVisibleTo(parent);
}

//  void QGraphicsItem::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem10setVisibleEb(
    QGraphicsItem *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QGraphicsItem::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem4hideEv(QGraphicsItem *self) {
  self->hide();
}

//  void QGraphicsItem::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem4showEv(QGraphicsItem *self) {
  self->show();
}

//  bool QGraphicsItem::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem9isEnabledEv(const QGraphicsItem *self) {
  return self->isEnabled();
}

//  void QGraphicsItem::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem10setEnabledEb(
    QGraphicsItem *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QGraphicsItem::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem10isSelectedEv(const QGraphicsItem *self) {
  return self->isSelected();
}

//  void QGraphicsItem::setSelected(bool selected)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem11setSelectedEb(
    QGraphicsItem *self,
    bool selected) {
  self->setSelected(selected);
}

//  bool QGraphicsItem::acceptDrops() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem11acceptDropsEv(const QGraphicsItem *self) {
  return self->acceptDrops();
}

//  void QGraphicsItem::setAcceptDrops(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem14setAcceptDropsEb(
    QGraphicsItem *self,
    bool on) {
  self->setAcceptDrops(on);
}

//  qreal QGraphicsItem::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem7opacityEv(const QGraphicsItem *self) {
  return self->opacity();
}

//  qreal QGraphicsItem::effectiveOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem16effectiveOpacityEv(
    const QGraphicsItem *self) {
  return self->effectiveOpacity();
}

//  void QGraphicsItem::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem10setOpacityEd(
    QGraphicsItem *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  QGraphicsEffect *QGraphicsItem::graphicsEffect() const
extern "C" Q_DECL_EXPORT
QGraphicsEffect *ritual_ZNK13QGraphicsItem14graphicsEffectEv(
    const QGraphicsItem *self) {
  return self->graphicsEffect();
}

//  void QGraphicsItem::setGraphicsEffect(QGraphicsEffect *effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem17setGraphicsEffectEP15QGraphicsEffect(
    QGraphicsItem *self,
    QGraphicsEffect *effect) {
  self->setGraphicsEffect(effect);
}

//  Qt::MouseButtons QGraphicsItem::acceptedMouseButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsItem20acceptedMouseButtonsEv(
    const QGraphicsItem *self) {
  return static_cast<int>(self->acceptedMouseButtons().toInt());
}

//  void QGraphicsItem::setAcceptedMouseButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem23setAcceptedMouseButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QGraphicsItem *self,
    int buttons) {
  self->setAcceptedMouseButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  bool QGraphicsItem::acceptHoverEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem17acceptHoverEventsEv(
    const QGraphicsItem *self) {
  return self->acceptHoverEvents();
}

//  void QGraphicsItem::setAcceptHoverEvents(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem20setAcceptHoverEventsEb(
    QGraphicsItem *self,
    bool enabled) {
  self->setAcceptHoverEvents(enabled);
}

//  bool QGraphicsItem::acceptTouchEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem17acceptTouchEventsEv(
    const QGraphicsItem *self) {
  return self->acceptTouchEvents();
}

//  void QGraphicsItem::setAcceptTouchEvents(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem20setAcceptTouchEventsEb(
    QGraphicsItem *self,
    bool enabled) {
  self->setAcceptTouchEvents(enabled);
}

//  bool QGraphicsItem::filtersChildEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem18filtersChildEventsEv(
    const QGraphicsItem *self) {
  return self->filtersChildEvents();
}

//  void QGraphicsItem::setFiltersChildEvents(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem21setFiltersChildEventsEb(
    QGraphicsItem *self,
    bool enabled) {
  self->setFiltersChildEvents(enabled);
}

//  bool QGraphicsItem::handlesChildEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem18handlesChildEventsEv(
    const QGraphicsItem *self) {
  return self->handlesChildEvents();
}

//  void QGraphicsItem::setHandlesChildEvents(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem21setHandlesChildEventsEb(
    QGraphicsItem *self,
    bool enabled) {
  self->setHandlesChildEvents(enabled);
}

//  bool QGraphicsItem::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem8isActiveEv(const QGraphicsItem *self) {
  return self->isActive();
}

//  void QGraphicsItem::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem9setActiveEb(QGraphicsItem *self, bool active) {
  self->setActive(active);
}

//  bool QGraphicsItem::hasFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem8hasFocusEv(const QGraphicsItem *self) {
  return self->hasFocus();
}

//  void QGraphicsItem::setFocus(Qt::FocusReason focusReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem8setFocusEN2Qt11FocusReasonE(
    QGraphicsItem *self,
    Qt::FocusReason focusReason) {
  self->setFocus(focusReason);
}

//  void QGraphicsItem::clearFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem10clearFocusEv(QGraphicsItem *self) {
  self->clearFocus();
}

//  QGraphicsItem *QGraphicsItem::focusProxy() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsItem10focusProxyEv(
    const QGraphicsItem *self) {
  return self->focusProxy();
}

//  void QGraphicsItem::setFocusProxy(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem13setFocusProxyEPS_(
    QGraphicsItem *self,
    QGraphicsItem *item) {
  self->setFocusProxy(item);
}

//  QGraphicsItem *QGraphicsItem::focusItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsItem9focusItemEv(
    const QGraphicsItem *self) {
  return self->focusItem();
}

//  QGraphicsItem *QGraphicsItem::focusScopeItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsItem14focusScopeItemEv(
    const QGraphicsItem *self) {
  return self->focusScopeItem();
}

//  void QGraphicsItem::grabMouse()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem9grabMouseEv(QGraphicsItem *self) {
  self->grabMouse();
}

//  void QGraphicsItem::ungrabMouse()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem11ungrabMouseEv(QGraphicsItem *self) {
  self->ungrabMouse();
}

//  void QGraphicsItem::grabKeyboard()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem12grabKeyboardEv(QGraphicsItem *self) {
  self->grabKeyboard();
}

//  void QGraphicsItem::ungrabKeyboard()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem14ungrabKeyboardEv(QGraphicsItem *self) {
  self->ungrabKeyboard();
}

//  QPointF QGraphicsItem::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem3posEv(const QGraphicsItem *self) {
  return new QPointF(self->pos());
}

//  qreal QGraphicsItem::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem1xEv(const QGraphicsItem *self) {
  return self->x();
}

//  void QGraphicsItem::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem4setXEd(QGraphicsItem *self, qreal x) {
  self->setX(x);
}

//  qreal QGraphicsItem::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem1yEv(const QGraphicsItem *self) {
  return self->y();
}

//  void QGraphicsItem::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem4setYEd(QGraphicsItem *self, qreal y) {
  self->setY(y);
}

//  QPointF QGraphicsItem::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem8scenePosEv(const QGraphicsItem *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsItem::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem6setPosERK7QPointF(
    QGraphicsItem *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  void QGraphicsItem::setPos(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem6setPosEdd(
    QGraphicsItem *self,
    qreal x,
    qreal y) {
  self->setPos(x, y);
}

//  void QGraphicsItem::moveBy(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem6moveByEdd(
    QGraphicsItem *self,
    qreal dx,
    qreal dy) {
  self->moveBy(dx, dy);
}

//  void QGraphicsItem::ensureVisible(const QRectF &rect, int xmargin, int
//      ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem13ensureVisibleERK6QRectFii(
    QGraphicsItem *self,
    const QRectF *rect,
    int xmargin,
    int ymargin) {
  self->ensureVisible(*rect, xmargin, ymargin);
}

//  void QGraphicsItem::ensureVisible(qreal x, qreal y, qreal w, qreal h, int
//      xmargin, int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem13ensureVisibleEddddii(
    QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    int xmargin,
    int ymargin) {
  self->ensureVisible(x, y, w, h, xmargin, ymargin);
}

//  QTransform QGraphicsItem::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsItem9transformEv(
    const QGraphicsItem *self) {
  return new QTransform(self->transform());
}

//  QTransform QGraphicsItem::sceneTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsItem14sceneTransformEv(
    const QGraphicsItem *self) {
  return new QTransform(self->sceneTransform());
}

//  QTransform QGraphicsItem::deviceTransform(const QTransform
//      &viewportTransform) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsItem15deviceTransformERK10QTransform(
    const QGraphicsItem *self,
    const QTransform *viewportTransform) {
  return new QTransform(self->deviceTransform(*viewportTransform));
}

//  QTransform QGraphicsItem::itemTransform(const QGraphicsItem *other, bool
//      *ok) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsItem13itemTransformEPKS_Pb(
    const QGraphicsItem *self,
    const QGraphicsItem *other,
    bool *ok) {
  return new QTransform(self->itemTransform(other, ok));
}

//  void QGraphicsItem::setTransform(const QTransform &matrix, bool combine)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem12setTransformERK10QTransformb(
    QGraphicsItem *self,
    const QTransform *matrix,
    bool combine) {
  self->setTransform(*matrix, combine);
}

//  void QGraphicsItem::resetTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem14resetTransformEv(QGraphicsItem *self) {
  self->resetTransform();
}

//  void QGraphicsItem::setRotation(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem11setRotationEd(
    QGraphicsItem *self,
    qreal angle) {
  self->setRotation(angle);
}

//  qreal QGraphicsItem::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem8rotationEv(const QGraphicsItem *self) {
  return self->rotation();
}

//  void QGraphicsItem::setScale(qreal scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem8setScaleEd(QGraphicsItem *self, qreal scale) {
  self->setScale(scale);
}

//  qreal QGraphicsItem::scale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem5scaleEv(const QGraphicsItem *self) {
  return self->scale();
}

//  QPointF QGraphicsItem::transformOriginPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem20transformOriginPointEv(
    const QGraphicsItem *self) {
  return new QPointF(self->transformOriginPoint());
}

//  void QGraphicsItem::setTransformOriginPoint(const QPointF &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem23setTransformOriginPointERK7QPointF(
    QGraphicsItem *self,
    const QPointF *origin) {
  self->setTransformOriginPoint(*origin);
}

//  void QGraphicsItem::setTransformOriginPoint(qreal ax, qreal ay)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem23setTransformOriginPointEdd(
    QGraphicsItem *self,
    qreal ax,
    qreal ay) {
  self->setTransformOriginPoint(ax, ay);
}

//  void QGraphicsItem::advance(int phase)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem7advanceEi(QGraphicsItem *self, int phase) {
  self->advance(phase);
}

//  qreal QGraphicsItem::zValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem6zValueEv(const QGraphicsItem *self) {
  return self->zValue();
}

//  void QGraphicsItem::setZValue(qreal z)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem9setZValueEd(QGraphicsItem *self, qreal z) {
  self->setZValue(z);
}

//  void QGraphicsItem::stackBefore(const QGraphicsItem *sibling)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem11stackBeforeEPKS_(
    QGraphicsItem *self,
    const QGraphicsItem *sibling) {
  self->stackBefore(sibling);
}

//  QRectF QGraphicsItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem12boundingRectEv(
    const QGraphicsItem *self) {
  return new QRectF(self->boundingRect());
}

//  QRectF QGraphicsItem::childrenBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem20childrenBoundingRectEv(
    const QGraphicsItem *self) {
  return new QRectF(self->childrenBoundingRect());
}

//  QRectF QGraphicsItem::sceneBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem17sceneBoundingRectEv(
    const QGraphicsItem *self) {
  return new QRectF(self->sceneBoundingRect());
}

//  QPainterPath QGraphicsItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem5shapeEv(const QGraphicsItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsItem::isClipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem9isClippedEv(const QGraphicsItem *self) {
  return self->isClipped();
}

//  QPainterPath QGraphicsItem::clipPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem8clipPathEv(
    const QGraphicsItem *self) {
  return new QPainterPath(self->clipPath());
}

//  bool QGraphicsItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem8containsERK7QPointF(
    const QGraphicsItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  bool QGraphicsItem::collidesWithItem(const QGraphicsItem *other,
//      Qt::ItemSelectionMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE(
    const QGraphicsItem *self,
    const QGraphicsItem *other,
    Qt::ItemSelectionMode mode) {
  return self->collidesWithItem(other, mode);
}

//  bool QGraphicsItem::collidesWithPath(const QPainterPath &path,
//      Qt::ItemSelectionMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE(
    const QGraphicsItem *self,
    const QPainterPath *path,
    Qt::ItemSelectionMode mode) {
  return self->collidesWithPath(*path, mode);
}

//  bool QGraphicsItem::isObscured(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem10isObscuredERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return self->isObscured(*rect);
}

//  bool QGraphicsItem::isObscured(qreal x, qreal y, qreal w, qreal h) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem10isObscuredEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return self->isObscured(x, y, w, h);
}

//  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem12isObscuredByEPKS_(
    const QGraphicsItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem10opaqueAreaEv(
    const QGraphicsItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  QRegion QGraphicsItem::boundingRegion(const QTransform
//      &itemToDeviceTransform) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK13QGraphicsItem14boundingRegionERK10QTransform(
    const QGraphicsItem *self,
    const QTransform *itemToDeviceTransform) {
  return new QRegion(self->boundingRegion(*itemToDeviceTransform));
}

//  qreal QGraphicsItem::boundingRegionGranularity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QGraphicsItem25boundingRegionGranularityEv(
    const QGraphicsItem *self) {
  return self->boundingRegionGranularity();
}

//  void QGraphicsItem::setBoundingRegionGranularity(qreal granularity)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem28setBoundingRegionGranularityEd(
    QGraphicsItem *self,
    qreal granularity) {
  self->setBoundingRegionGranularity(granularity);
}

//  void QGraphicsItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void QGraphicsItem::update(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem6updateERK6QRectF(
    QGraphicsItem *self,
    const QRectF *rect) {
  self->update(*rect);
}

//  void QGraphicsItem::update(qreal x, qreal y, qreal width, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem6updateEdddd(
    QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->update(x, y, width, height);
}

//  void QGraphicsItem::scroll(qreal dx, qreal dy, const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem6scrollEddRK6QRectF(
    QGraphicsItem *self,
    qreal dx,
    qreal dy,
    const QRectF *rect) {
  self->scroll(dx, dy, *rect);
}

//  QPointF QGraphicsItem::mapToItem(const QGraphicsItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK7QPointF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QPointF *point) {
  return new QPointF(self->mapToItem(item, *point));
}

//  QPointF QGraphicsItem::mapToParent(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem11mapToParentERK7QPointF(
    const QGraphicsItem *self,
    const QPointF *point) {
  return new QPointF(self->mapToParent(*point));
}

//  QPointF QGraphicsItem::mapToScene(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem10mapToSceneERK7QPointF(
    const QGraphicsItem *self,
    const QPointF *point) {
  return new QPointF(self->mapToScene(*point));
}

//  QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item, const
//      QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK6QRectF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QRectF *rect) {
  return new QPolygonF(self->mapToItem(item, *rect));
}

//  QPolygonF QGraphicsItem::mapToParent(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem11mapToParentERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QPolygonF(self->mapToParent(*rect));
}

//  QPolygonF QGraphicsItem::mapToScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem10mapToSceneERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QPolygonF(self->mapToScene(*rect));
}

//  QRectF QGraphicsItem::mapRectToItem(const QGraphicsItem *item, const
//      QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem13mapRectToItemEPKS_RK6QRectF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QRectF *rect) {
  return new QRectF(self->mapRectToItem(item, *rect));
}

//  QRectF QGraphicsItem::mapRectToParent(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem15mapRectToParentERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QRectF(self->mapRectToParent(*rect));
}

//  QRectF QGraphicsItem::mapRectToScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem14mapRectToSceneERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QRectF(self->mapRectToScene(*rect));
}

//  QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item, const
//      QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK9QPolygonF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QPolygonF *polygon) {
  return new QPolygonF(self->mapToItem(item, *polygon));
}

//  QPolygonF QGraphicsItem::mapToParent(const QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem11mapToParentERK9QPolygonF(
    const QGraphicsItem *self,
    const QPolygonF *polygon) {
  return new QPolygonF(self->mapToParent(*polygon));
}

//  QPolygonF QGraphicsItem::mapToScene(const QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem10mapToSceneERK9QPolygonF(
    const QGraphicsItem *self,
    const QPolygonF *polygon) {
  return new QPolygonF(self->mapToScene(*polygon));
}

//  QPainterPath QGraphicsItem::mapToItem(const QGraphicsItem *item, const
//      QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem9mapToItemEPKS_RK12QPainterPath(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QPainterPath *path) {
  return new QPainterPath(self->mapToItem(item, *path));
}

//  QPainterPath QGraphicsItem::mapToParent(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem11mapToParentERK12QPainterPath(
    const QGraphicsItem *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapToParent(*path));
}

//  QPainterPath QGraphicsItem::mapToScene(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem10mapToSceneERK12QPainterPath(
    const QGraphicsItem *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapToScene(*path));
}

//  QPointF QGraphicsItem::mapFromItem(const QGraphicsItem *item, const
//      QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK7QPointF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QPointF *point) {
  return new QPointF(self->mapFromItem(item, *point));
}

//  QPointF QGraphicsItem::mapFromParent(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem13mapFromParentERK7QPointF(
    const QGraphicsItem *self,
    const QPointF *point) {
  return new QPointF(self->mapFromParent(*point));
}

//  QPointF QGraphicsItem::mapFromScene(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem12mapFromSceneERK7QPointF(
    const QGraphicsItem *self,
    const QPointF *point) {
  return new QPointF(self->mapFromScene(*point));
}

//  QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem *item, const
//      QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK6QRectF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QRectF *rect) {
  return new QPolygonF(self->mapFromItem(item, *rect));
}

//  QPolygonF QGraphicsItem::mapFromParent(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem13mapFromParentERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QPolygonF(self->mapFromParent(*rect));
}

//  QPolygonF QGraphicsItem::mapFromScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem12mapFromSceneERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QPolygonF(self->mapFromScene(*rect));
}

//  QRectF QGraphicsItem::mapRectFromItem(const QGraphicsItem *item, const
//      QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem15mapRectFromItemEPKS_RK6QRectF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QRectF *rect) {
  return new QRectF(self->mapRectFromItem(item, *rect));
}

//  QRectF QGraphicsItem::mapRectFromParent(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem17mapRectFromParentERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QRectF(self->mapRectFromParent(*rect));
}

//  QRectF QGraphicsItem::mapRectFromScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem16mapRectFromSceneERK6QRectF(
    const QGraphicsItem *self,
    const QRectF *rect) {
  return new QRectF(self->mapRectFromScene(*rect));
}

//  QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem *item, const
//      QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK9QPolygonF(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QPolygonF *polygon) {
  return new QPolygonF(self->mapFromItem(item, *polygon));
}

//  QPolygonF QGraphicsItem::mapFromParent(const QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem13mapFromParentERK9QPolygonF(
    const QGraphicsItem *self,
    const QPolygonF *polygon) {
  return new QPolygonF(self->mapFromParent(*polygon));
}

//  QPolygonF QGraphicsItem::mapFromScene(const QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem12mapFromSceneERK9QPolygonF(
    const QGraphicsItem *self,
    const QPolygonF *polygon) {
  return new QPolygonF(self->mapFromScene(*polygon));
}

//  QPainterPath QGraphicsItem::mapFromItem(const QGraphicsItem *item, const
//      QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem11mapFromItemEPKS_RK12QPainterPath(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    const QPainterPath *path) {
  return new QPainterPath(self->mapFromItem(item, *path));
}

//  QPainterPath QGraphicsItem::mapFromParent(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem13mapFromParentERK12QPainterPath(
    const QGraphicsItem *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapFromParent(*path));
}

//  QPainterPath QGraphicsItem::mapFromScene(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsItem12mapFromSceneERK12QPainterPath(
    const QGraphicsItem *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapFromScene(*path));
}

//  QPointF QGraphicsItem::mapToItem(const QGraphicsItem *item, qreal x,
//      qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem9mapToItemEPKS_dd(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    qreal x,
    qreal y) {
  return new QPointF(self->mapToItem(item, x, y));
}

//  QPointF QGraphicsItem::mapToParent(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem11mapToParentEdd(
    const QGraphicsItem *self,
    qreal x,
    qreal y) {
  return new QPointF(self->mapToParent(x, y));
}

//  QPointF QGraphicsItem::mapToScene(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem10mapToSceneEdd(
    const QGraphicsItem *self,
    qreal x,
    qreal y) {
  return new QPointF(self->mapToScene(x, y));
}

//  QPolygonF QGraphicsItem::mapToItem(const QGraphicsItem *item, qreal x,
//      qreal y, qreal w, qreal h) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem9mapToItemEPKS_dddd(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(self->mapToItem(item, x, y, w, h));
}

//  QPolygonF QGraphicsItem::mapToParent(qreal x, qreal y, qreal w, qreal h)
//      const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem11mapToParentEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(self->mapToParent(x, y, w, h));
}

//  QPolygonF QGraphicsItem::mapToScene(qreal x, qreal y, qreal w, qreal h)
//      const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem10mapToSceneEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(self->mapToScene(x, y, w, h));
}

//  QRectF QGraphicsItem::mapRectToItem(const QGraphicsItem *item, qreal x,
//      qreal y, qreal w, qreal h) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem13mapRectToItemEPKS_dddd(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QRectF(self->mapRectToItem(item, x, y, w, h));
}

//  QRectF QGraphicsItem::mapRectToParent(qreal x, qreal y, qreal w, qreal h)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem15mapRectToParentEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QRectF(self->mapRectToParent(x, y, w, h));
}

//  QRectF QGraphicsItem::mapRectToScene(qreal x, qreal y, qreal w, qreal h)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem14mapRectToSceneEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QRectF(self->mapRectToScene(x, y, w, h));
}

//  QPointF QGraphicsItem::mapFromItem(const QGraphicsItem *item, qreal x,
//      qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem11mapFromItemEPKS_dd(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    qreal x,
    qreal y) {
  return new QPointF(self->mapFromItem(item, x, y));
}

//  QPointF QGraphicsItem::mapFromParent(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem13mapFromParentEdd(
    const QGraphicsItem *self,
    qreal x,
    qreal y) {
  return new QPointF(self->mapFromParent(x, y));
}

//  QPointF QGraphicsItem::mapFromScene(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsItem12mapFromSceneEdd(
    const QGraphicsItem *self,
    qreal x,
    qreal y) {
  return new QPointF(self->mapFromScene(x, y));
}

//  QPolygonF QGraphicsItem::mapFromItem(const QGraphicsItem *item, qreal x,
//      qreal y, qreal w, qreal h) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem11mapFromItemEPKS_dddd(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(self->mapFromItem(item, x, y, w, h));
}

//  QPolygonF QGraphicsItem::mapFromParent(qreal x, qreal y, qreal w, qreal
//      h) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem13mapFromParentEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(self->mapFromParent(x, y, w, h));
}

//  QPolygonF QGraphicsItem::mapFromScene(qreal x, qreal y, qreal w, qreal h)
//      const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsItem12mapFromSceneEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(self->mapFromScene(x, y, w, h));
}

//  QRectF QGraphicsItem::mapRectFromItem(const QGraphicsItem *item, qreal x,
//      qreal y, qreal w, qreal h) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem15mapRectFromItemEPKS_dddd(
    const QGraphicsItem *self,
    const QGraphicsItem *item,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QRectF(self->mapRectFromItem(item, x, y, w, h));
}

//  QRectF QGraphicsItem::mapRectFromParent(qreal x, qreal y, qreal w, qreal
//      h) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem17mapRectFromParentEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QRectF(self->mapRectFromParent(x, y, w, h));
}

//  QRectF QGraphicsItem::mapRectFromScene(qreal x, qreal y, qreal w, qreal
//      h) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsItem16mapRectFromSceneEdddd(
    const QGraphicsItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QRectF(self->mapRectFromScene(x, y, w, h));
}

//  bool QGraphicsItem::isAncestorOf(const QGraphicsItem *child) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem12isAncestorOfEPKS_(
    const QGraphicsItem *self,
    const QGraphicsItem *child) {
  return self->isAncestorOf(child);
}

//  QGraphicsItem *QGraphicsItem::commonAncestorItem(const QGraphicsItem
//      *other) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsItem18commonAncestorItemEPKS_(
    const QGraphicsItem *self,
    const QGraphicsItem *other) {
  return self->commonAncestorItem(other);
}

//  bool QGraphicsItem::isUnderMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsItem12isUnderMouseEv(const QGraphicsItem *self) {
  return self->isUnderMouse();
}

//  QVariant QGraphicsItem::data(int key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QGraphicsItem4dataEi(
    const QGraphicsItem *self,
    int key) {
  return new QVariant(self->data(key));
}

//  void QGraphicsItem::setData(int key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem7setDataEiRK8QVariant(
    QGraphicsItem *self,
    int key,
    const QVariant *value) {
  self->setData(key, *value);
}

//  Qt::InputMethodHints QGraphicsItem::inputMethodHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsItem16inputMethodHintsEv(
    const QGraphicsItem *self) {
  return static_cast<int>(self->inputMethodHints().toInt());
}

//  void QGraphicsItem::setInputMethodHints(Qt::InputMethodHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem19setInputMethodHintsE6QFlagsIN2Qt15InputMethodHintEE(
    QGraphicsItem *self,
    int hints) {
  self->setInputMethodHints(QFlags<Qt::InputMethodHint>::fromInt(hints));
}

//  int QGraphicsItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsItem4typeEv(const QGraphicsItem *self) {
  return self->type();
}

//  void QGraphicsItem::installSceneEventFilter(QGraphicsItem *filterItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem23installSceneEventFilterEPS_(
    QGraphicsItem *self,
    QGraphicsItem *filterItem) {
  self->installSceneEventFilter(filterItem);
}

//  void QGraphicsItem::removeSceneEventFilter(QGraphicsItem *filterItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsItem22removeSceneEventFilterEPS_(
    QGraphicsItem *self,
    QGraphicsItem *filterItem) {
  self->removeSceneEventFilter(filterItem);
}
