//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsscene.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsscene.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtCore/qline.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>
#include <QtGui/qpalette.h>

//  const QMetaObject *QGraphicsScene::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGraphicsScene10metaObjectEv(
    const QGraphicsScene *self) {
  return self->metaObject();
}

//  QString QGraphicsScene::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGraphicsScene2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsScene::tr(s, c, n));
}

//  QGraphicsScene::QGraphicsScene(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN14QGraphicsSceneC1EP7QObject(QObject *parent) {
  return new QGraphicsScene(parent);
}

//  QGraphicsScene::QGraphicsScene(const QRectF &sceneRect, QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN14QGraphicsSceneC1ERK6QRectFP7QObject(
    const QRectF *sceneRect,
    QObject *parent) {
  return new QGraphicsScene(*sceneRect, parent);
}

//  QGraphicsScene::QGraphicsScene(qreal x, qreal y, qreal width, qreal
//      height, QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN14QGraphicsSceneC1EddddP7QObject(
    qreal x,
    qreal y,
    qreal width,
    qreal height,
    QObject *parent) {
  return new QGraphicsScene(x, y, width, height, parent);
}

//  QGraphicsScene::~QGraphicsScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsSceneD1Ev(QGraphicsScene *self) {
  delete self;
}

//  QRectF QGraphicsScene::sceneRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QGraphicsScene9sceneRectEv(const QGraphicsScene *self) {
  return new QRectF(self->sceneRect());
}

//  qreal QGraphicsScene::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScene5widthEv(const QGraphicsScene *self) {
  return self->width();
}

//  qreal QGraphicsScene::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScene6heightEv(const QGraphicsScene *self) {
  return self->height();
}

//  void QGraphicsScene::setSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene12setSceneRectERK6QRectF(
    QGraphicsScene *self,
    const QRectF *rect) {
  self->setSceneRect(*rect);
}

//  void QGraphicsScene::setSceneRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene12setSceneRectEdddd(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setSceneRect(x, y, w, h);
}

//  void QGraphicsScene::render(QPainter *painter, const QRectF &target,
//      const QRectF &source, Qt::AspectRatioMode aspectRatioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene6renderEP8QPainterRK6QRectFS4_N2Qt15AspectRatioModeE(
    QGraphicsScene *self,
    QPainter *painter,
    const QRectF *target,
    const QRectF *source,
    Qt::AspectRatioMode aspectRatioMode) {
  self->render(painter, *target, *source, aspectRatioMode);
}

//  ItemIndexMethod QGraphicsScene::itemIndexMethod() const
extern "C" Q_DECL_EXPORT
QGraphicsScene::ItemIndexMethod ritual_ZNK14QGraphicsScene15itemIndexMethodEv(
    const QGraphicsScene *self) {
  return self->itemIndexMethod();
}

//  void QGraphicsScene::setItemIndexMethod(ItemIndexMethod method)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene18setItemIndexMethodENS_15ItemIndexMethodE(
    QGraphicsScene *self,
    QGraphicsScene::ItemIndexMethod method) {
  self->setItemIndexMethod(method);
}

//  int QGraphicsScene::bspTreeDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QGraphicsScene12bspTreeDepthEv(const QGraphicsScene *self) {
  return self->bspTreeDepth();
}

//  void QGraphicsScene::setBspTreeDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15setBspTreeDepthEi(
    QGraphicsScene *self,
    int depth) {
  self->setBspTreeDepth(depth);
}

//  QRectF QGraphicsScene::itemsBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QGraphicsScene17itemsBoundingRectEv(
    const QGraphicsScene *self) {
  return new QRectF(self->itemsBoundingRect());
}

//  QGraphicsItem *QGraphicsScene::itemAt(const QPointF &pos, const
//      QTransform &deviceTransform) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene6itemAtERK7QPointFRK10QTransform(
    const QGraphicsScene *self,
    const QPointF *pos,
    const QTransform *deviceTransform) {
  return self->itemAt(*pos, *deviceTransform);
}

//  QGraphicsItem *QGraphicsScene::itemAt(qreal x, qreal y, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene6itemAtEddRK10QTransform(
    const QGraphicsScene *self,
    qreal x,
    qreal y,
    const QTransform *deviceTransform) {
  return self->itemAt(x, y, *deviceTransform);
}

//  QPainterPath QGraphicsScene::selectionArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK14QGraphicsScene13selectionAreaEv(
    const QGraphicsScene *self) {
  return new QPainterPath(self->selectionArea());
}

//  void QGraphicsScene::setSelectionArea(const QPainterPath &path, const
//      QTransform &deviceTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16setSelectionAreaERK12QPainterPathRK10QTransform(
    QGraphicsScene *self,
    const QPainterPath *path,
    const QTransform *deviceTransform) {
  self->setSelectionArea(*path, *deviceTransform);
}

//  void QGraphicsScene::setSelectionArea(const QPainterPath &path,
//      Qt::ItemSelectionOperation selectionOperation, Qt::ItemSelectionMode
//      mode, const QTransform &deviceTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16setSelectionAreaERK12QPainterPathN2Qt22ItemSelectionOperationENS3_17ItemSelectionModeERK10QTransform(
    QGraphicsScene *self,
    const QPainterPath *path,
    Qt::ItemSelectionOperation selectionOperation,
    Qt::ItemSelectionMode mode,
    const QTransform *deviceTransform) {
  self->setSelectionArea(*path, selectionOperation, mode, *deviceTransform);
}

//  void QGraphicsScene::destroyItemGroup(QGraphicsItemGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16destroyItemGroupEP18QGraphicsItemGroup(
    QGraphicsScene *self,
    QGraphicsItemGroup *group) {
  self->destroyItemGroup(group);
}

//  void QGraphicsScene::addItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene7addItemEP13QGraphicsItem(
    QGraphicsScene *self,
    QGraphicsItem *item) {
  self->addItem(item);
}

//  QGraphicsEllipseItem *QGraphicsScene::addEllipse(const QRectF &rect,
//      const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsEllipseItem *ritual_ZN14QGraphicsScene10addEllipseERK6QRectFRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QRectF *rect,
    const QPen *pen,
    const QBrush *brush) {
  return self->addEllipse(*rect, *pen, *brush);
}

//  QGraphicsLineItem *QGraphicsScene::addLine(const QLineF &line, const QPen
//      &pen)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN14QGraphicsScene7addLineERK6QLineFRK4QPen(
    QGraphicsScene *self,
    const QLineF *line,
    const QPen *pen) {
  return self->addLine(*line, *pen);
}

//  QGraphicsPathItem *QGraphicsScene::addPath(const QPainterPath &path,
//      const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsPathItem *ritual_ZN14QGraphicsScene7addPathERK12QPainterPathRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QPainterPath *path,
    const QPen *pen,
    const QBrush *brush) {
  return self->addPath(*path, *pen, *brush);
}

//  QGraphicsPixmapItem *QGraphicsScene::addPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem *ritual_ZN14QGraphicsScene9addPixmapERK7QPixmap(
    QGraphicsScene *self,
    const QPixmap *pixmap) {
  return self->addPixmap(*pixmap);
}

//  QGraphicsPolygonItem *QGraphicsScene::addPolygon(const QPolygonF
//      &polygon, const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsPolygonItem *ritual_ZN14QGraphicsScene10addPolygonERK9QPolygonFRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QPolygonF *polygon,
    const QPen *pen,
    const QBrush *brush) {
  return self->addPolygon(*polygon, *pen, *brush);
}

//  QGraphicsRectItem *QGraphicsScene::addRect(const QRectF &rect, const QPen
//      &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN14QGraphicsScene7addRectERK6QRectFRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QRectF *rect,
    const QPen *pen,
    const QBrush *brush) {
  return self->addRect(*rect, *pen, *brush);
}

//  QGraphicsTextItem *QGraphicsScene::addText(const QString &text, const
//      QFont &font)
extern "C" Q_DECL_EXPORT
QGraphicsTextItem *ritual_ZN14QGraphicsScene7addTextERK7QStringRK5QFont(
    QGraphicsScene *self,
    const QString *text,
    const QFont *font) {
  return self->addText(*text, *font);
}

//  QGraphicsSimpleTextItem *QGraphicsScene::addSimpleText(const QString
//      &text, const QFont &font)
extern "C" Q_DECL_EXPORT
QGraphicsSimpleTextItem *ritual_ZN14QGraphicsScene13addSimpleTextERK7QStringRK5QFont(
    QGraphicsScene *self,
    const QString *text,
    const QFont *font) {
  return self->addSimpleText(*text, *font);
}

//  QGraphicsProxyWidget *QGraphicsScene::addWidget(QWidget *widget,
//      Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN14QGraphicsScene9addWidgetEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsScene *self,
    QWidget *widget,
    int wFlags) {
  return self->addWidget(widget, QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QGraphicsEllipseItem *QGraphicsScene::addEllipse(qreal x, qreal y, qreal
//      w, qreal h, const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsEllipseItem *ritual_ZN14QGraphicsScene10addEllipseEddddRK4QPenRK6QBrush(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    const QPen *pen,
    const QBrush *brush) {
  return self->addEllipse(x, y, w, h, *pen, *brush);
}

//  QGraphicsLineItem *QGraphicsScene::addLine(qreal x1, qreal y1, qreal x2,
//      qreal y2, const QPen &pen)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN14QGraphicsScene7addLineEddddRK4QPen(
    QGraphicsScene *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2,
    const QPen *pen) {
  return self->addLine(x1, y1, x2, y2, *pen);
}

//  QGraphicsRectItem *QGraphicsScene::addRect(qreal x, qreal y, qreal w,
//      qreal h, const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN14QGraphicsScene7addRectEddddRK4QPenRK6QBrush(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    const QPen *pen,
    const QBrush *brush) {
  return self->addRect(x, y, w, h, *pen, *brush);
}

//  void QGraphicsScene::removeItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10removeItemEP13QGraphicsItem(
    QGraphicsScene *self,
    QGraphicsItem *item) {
  self->removeItem(item);
}

//  QGraphicsItem *QGraphicsScene::focusItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene9focusItemEv(
    const QGraphicsScene *self) {
  return self->focusItem();
}

//  void QGraphicsScene::setFocusItem(QGraphicsItem *item, Qt::FocusReason
//      focusReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene12setFocusItemEP13QGraphicsItemN2Qt11FocusReasonE(
    QGraphicsScene *self,
    QGraphicsItem *item,
    Qt::FocusReason focusReason) {
  self->setFocusItem(item, focusReason);
}

//  bool QGraphicsScene::hasFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene8hasFocusEv(const QGraphicsScene *self) {
  return self->hasFocus();
}

//  void QGraphicsScene::setFocus(Qt::FocusReason focusReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene8setFocusEN2Qt11FocusReasonE(
    QGraphicsScene *self,
    Qt::FocusReason focusReason) {
  self->setFocus(focusReason);
}

//  void QGraphicsScene::clearFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10clearFocusEv(QGraphicsScene *self) {
  self->clearFocus();
}

//  void QGraphicsScene::setStickyFocus(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14setStickyFocusEb(
    QGraphicsScene *self,
    bool enabled) {
  self->setStickyFocus(enabled);
}

//  bool QGraphicsScene::stickyFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene11stickyFocusEv(const QGraphicsScene *self) {
  return self->stickyFocus();
}

//  QGraphicsItem *QGraphicsScene::mouseGrabberItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene16mouseGrabberItemEv(
    const QGraphicsScene *self) {
  return self->mouseGrabberItem();
}

//  QBrush QGraphicsScene::backgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14QGraphicsScene15backgroundBrushEv(
    const QGraphicsScene *self) {
  return new QBrush(self->backgroundBrush());
}

//  void QGraphicsScene::setBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene18setBackgroundBrushERK6QBrush(
    QGraphicsScene *self,
    const QBrush *brush) {
  self->setBackgroundBrush(*brush);
}

//  QBrush QGraphicsScene::foregroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14QGraphicsScene15foregroundBrushEv(
    const QGraphicsScene *self) {
  return new QBrush(self->foregroundBrush());
}

//  void QGraphicsScene::setForegroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene18setForegroundBrushERK6QBrush(
    QGraphicsScene *self,
    const QBrush *brush) {
  self->setForegroundBrush(*brush);
}

//  QVariant QGraphicsScene::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QGraphicsScene16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsScene *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  void QGraphicsScene::update(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene6updateEdddd(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->update(x, y, w, h);
}

//  void QGraphicsScene::invalidate(qreal x, qreal y, qreal w, qreal h,
//      SceneLayers layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10invalidateEdddd6QFlagsINS_10SceneLayerEE(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    int layers) {
  self->invalidate(
      x,
      y,
      w,
      h,
      QFlags<QGraphicsScene::SceneLayer>::fromInt(layers));
}

//  QStyle *QGraphicsScene::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK14QGraphicsScene5styleEv(const QGraphicsScene *self) {
  return self->style();
}

//  void QGraphicsScene::setStyle(QStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene8setStyleEP6QStyle(
    QGraphicsScene *self,
    QStyle *style) {
  self->setStyle(style);
}

//  QFont QGraphicsScene::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QGraphicsScene4fontEv(const QGraphicsScene *self) {
  return new QFont(self->font());
}

//  void QGraphicsScene::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene7setFontERK5QFont(
    QGraphicsScene *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QPalette QGraphicsScene::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK14QGraphicsScene7paletteEv(const QGraphicsScene *self) {
  return new QPalette(self->palette());
}

//  void QGraphicsScene::setPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10setPaletteERK8QPalette(
    QGraphicsScene *self,
    const QPalette *palette) {
  self->setPalette(*palette);
}

//  bool QGraphicsScene::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene8isActiveEv(const QGraphicsScene *self) {
  return self->isActive();
}

//  QGraphicsItem *QGraphicsScene::activePanel() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene11activePanelEv(
    const QGraphicsScene *self) {
  return self->activePanel();
}

//  void QGraphicsScene::setActivePanel(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14setActivePanelEP13QGraphicsItem(
    QGraphicsScene *self,
    QGraphicsItem *item) {
  self->setActivePanel(item);
}

//  QGraphicsWidget *QGraphicsScene::activeWindow() const
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZNK14QGraphicsScene12activeWindowEv(
    const QGraphicsScene *self) {
  return self->activeWindow();
}

//  void QGraphicsScene::setActiveWindow(QGraphicsWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15setActiveWindowEP15QGraphicsWidget(
    QGraphicsScene *self,
    QGraphicsWidget *widget) {
  self->setActiveWindow(widget);
}

//  bool QGraphicsScene::sendEvent(QGraphicsItem *item, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGraphicsScene9sendEventEP13QGraphicsItemP6QEvent(
    QGraphicsScene *self,
    QGraphicsItem *item,
    QEvent *event) {
  return self->sendEvent(item, event);
}

//  qreal QGraphicsScene::minimumRenderSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScene17minimumRenderSizeEv(
    const QGraphicsScene *self) {
  return self->minimumRenderSize();
}

//  void QGraphicsScene::setMinimumRenderSize(qreal minSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene20setMinimumRenderSizeEd(
    QGraphicsScene *self,
    qreal minSize) {
  self->setMinimumRenderSize(minSize);
}

//  bool QGraphicsScene::focusOnTouch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene12focusOnTouchEv(const QGraphicsScene *self) {
  return self->focusOnTouch();
}

//  void QGraphicsScene::setFocusOnTouch(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15setFocusOnTouchEb(
    QGraphicsScene *self,
    bool enabled) {
  self->setFocusOnTouch(enabled);
}

//  void QGraphicsScene::update(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene6updateERK6QRectF(
    QGraphicsScene *self,
    const QRectF *rect) {
  self->update(*rect);
}

//  void QGraphicsScene::invalidate(const QRectF &rect, SceneLayers layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10invalidateERK6QRectF6QFlagsINS_10SceneLayerEE(
    QGraphicsScene *self,
    const QRectF *rect,
    int layers) {
  self->invalidate(
      *rect,
      QFlags<QGraphicsScene::SceneLayer>::fromInt(layers));
}

//  void QGraphicsScene::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene7advanceEv(QGraphicsScene *self) {
  self->advance();
}

//  void QGraphicsScene::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14clearSelectionEv(QGraphicsScene *self) {
  self->clearSelection();
}

//  void QGraphicsScene::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene5clearEv(QGraphicsScene *self) {
  self->clear();
}
