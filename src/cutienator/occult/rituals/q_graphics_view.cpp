//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qvariant.h>
#include <QtGui/qbrush.h>

//  const QMetaObject *QGraphicsView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QGraphicsView10metaObjectEv(
    const QGraphicsView *self) {
  return self->metaObject();
}

//  QString QGraphicsView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QGraphicsView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsView::tr(s, c, n));
}

//  QGraphicsView::QGraphicsView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QGraphicsView *ritual_ZN13QGraphicsViewC1EP7QWidget(QWidget *parent) {
  return new QGraphicsView(parent);
}

//  QGraphicsView::QGraphicsView(QGraphicsScene *scene, QWidget *parent)
extern "C" Q_DECL_EXPORT
QGraphicsView *ritual_ZN13QGraphicsViewC1EP14QGraphicsSceneP7QWidget(
    QGraphicsScene *scene,
    QWidget *parent) {
  return new QGraphicsView(scene, parent);
}

//  QGraphicsView::~QGraphicsView()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsViewD1Ev(QGraphicsView *self) {
  delete self;
}

//  QSize QGraphicsView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QGraphicsView8sizeHintEv(const QGraphicsView *self) {
  return new QSize(self->sizeHint());
}

//  QPainter::RenderHints QGraphicsView::renderHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView11renderHintsEv(const QGraphicsView *self) {
  return static_cast<int>(self->renderHints().toInt());
}

//  void QGraphicsView::setRenderHint(QPainter::RenderHint hint, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13setRenderHintEN8QPainter10RenderHintEb(
    QGraphicsView *self,
    QPainter::RenderHint hint,
    bool enabled) {
  self->setRenderHint(hint, enabled);
}

//  void QGraphicsView::setRenderHints(QPainter::RenderHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView14setRenderHintsE6QFlagsIN8QPainter10RenderHintEE(
    QGraphicsView *self,
    int hints) {
  self->setRenderHints(QFlags<QPainter::RenderHint>::fromInt(hints));
}

//  Qt::Alignment QGraphicsView::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView9alignmentEv(const QGraphicsView *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QGraphicsView::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsView *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  ViewportAnchor QGraphicsView::transformationAnchor() const
extern "C" Q_DECL_EXPORT
QGraphicsView::ViewportAnchor ritual_ZNK13QGraphicsView20transformationAnchorEv(
    const QGraphicsView *self) {
  return self->transformationAnchor();
}

//  void QGraphicsView::setTransformationAnchor(ViewportAnchor anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView23setTransformationAnchorENS_14ViewportAnchorE(
    QGraphicsView *self,
    QGraphicsView::ViewportAnchor anchor) {
  self->setTransformationAnchor(anchor);
}

//  ViewportAnchor QGraphicsView::resizeAnchor() const
extern "C" Q_DECL_EXPORT
QGraphicsView::ViewportAnchor ritual_ZNK13QGraphicsView12resizeAnchorEv(
    const QGraphicsView *self) {
  return self->resizeAnchor();
}

//  void QGraphicsView::setResizeAnchor(ViewportAnchor anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView15setResizeAnchorENS_14ViewportAnchorE(
    QGraphicsView *self,
    QGraphicsView::ViewportAnchor anchor) {
  self->setResizeAnchor(anchor);
}

//  ViewportUpdateMode QGraphicsView::viewportUpdateMode() const
extern "C" Q_DECL_EXPORT
QGraphicsView::ViewportUpdateMode ritual_ZNK13QGraphicsView18viewportUpdateModeEv(
    const QGraphicsView *self) {
  return self->viewportUpdateMode();
}

//  void QGraphicsView::setViewportUpdateMode(ViewportUpdateMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView21setViewportUpdateModeENS_18ViewportUpdateModeE(
    QGraphicsView *self,
    QGraphicsView::ViewportUpdateMode mode) {
  self->setViewportUpdateMode(mode);
}

//  OptimizationFlags QGraphicsView::optimizationFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView17optimizationFlagsEv(
    const QGraphicsView *self) {
  return static_cast<int>(self->optimizationFlags().toInt());
}

//  void QGraphicsView::setOptimizationFlag(OptimizationFlag flag, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView19setOptimizationFlagENS_16OptimizationFlagEb(
    QGraphicsView *self,
    QGraphicsView::OptimizationFlag flag,
    bool enabled) {
  self->setOptimizationFlag(flag, enabled);
}

//  void QGraphicsView::setOptimizationFlags(OptimizationFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView20setOptimizationFlagsE6QFlagsINS_16OptimizationFlagEE(
    QGraphicsView *self,
    int flags) {
  self->setOptimizationFlags(
      QFlags<QGraphicsView::OptimizationFlag>::fromInt(flags));
}

//  DragMode QGraphicsView::dragMode() const
extern "C" Q_DECL_EXPORT
QGraphicsView::DragMode ritual_ZNK13QGraphicsView8dragModeEv(
    const QGraphicsView *self) {
  return self->dragMode();
}

//  void QGraphicsView::setDragMode(DragMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView11setDragModeENS_8DragModeE(
    QGraphicsView *self,
    QGraphicsView::DragMode mode) {
  self->setDragMode(mode);
}

//  Qt::ItemSelectionMode QGraphicsView::rubberBandSelectionMode() const
extern "C" Q_DECL_EXPORT
Qt::ItemSelectionMode ritual_ZNK13QGraphicsView23rubberBandSelectionModeEv(
    const QGraphicsView *self) {
  return self->rubberBandSelectionMode();
}

//  void QGraphicsView::setRubberBandSelectionMode(Qt::ItemSelectionMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView26setRubberBandSelectionModeEN2Qt17ItemSelectionModeE(
    QGraphicsView *self,
    Qt::ItemSelectionMode mode) {
  self->setRubberBandSelectionMode(mode);
}

//  QRect QGraphicsView::rubberBandRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QGraphicsView14rubberBandRectEv(
    const QGraphicsView *self) {
  return new QRect(self->rubberBandRect());
}

//  CacheMode QGraphicsView::cacheMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView9cacheModeEv(const QGraphicsView *self) {
  return static_cast<int>(self->cacheMode().toInt());
}

//  void QGraphicsView::setCacheMode(CacheMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setCacheModeE6QFlagsINS_13CacheModeFlagEE(
    QGraphicsView *self,
    int mode) {
  self->setCacheMode(QFlags<QGraphicsView::CacheModeFlag>::fromInt(mode));
}

//  void QGraphicsView::resetCachedContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView18resetCachedContentEv(QGraphicsView *self) {
  self->resetCachedContent();
}

//  bool QGraphicsView::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsView13isInteractiveEv(const QGraphicsView *self) {
  return self->isInteractive();
}

//  void QGraphicsView::setInteractive(bool allowed)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView14setInteractiveEb(
    QGraphicsView *self,
    bool allowed) {
  self->setInteractive(allowed);
}

//  QGraphicsScene *QGraphicsView::scene() const
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZNK13QGraphicsView5sceneEv(
    const QGraphicsView *self) {
  return self->scene();
}

//  void QGraphicsView::setScene(QGraphicsScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8setSceneEP14QGraphicsScene(
    QGraphicsView *self,
    QGraphicsScene *scene) {
  self->setScene(scene);
}

//  QRectF QGraphicsView::sceneRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsView9sceneRectEv(const QGraphicsView *self) {
  return new QRectF(self->sceneRect());
}

//  void QGraphicsView::setSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setSceneRectERK6QRectF(
    QGraphicsView *self,
    const QRectF *rect) {
  self->setSceneRect(*rect);
}

//  void QGraphicsView::setSceneRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setSceneRectEdddd(
    QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setSceneRect(x, y, w, h);
}

//  QTransform QGraphicsView::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsView9transformEv(
    const QGraphicsView *self) {
  return new QTransform(self->transform());
}

//  QTransform QGraphicsView::viewportTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsView17viewportTransformEv(
    const QGraphicsView *self) {
  return new QTransform(self->viewportTransform());
}

//  bool QGraphicsView::isTransformed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsView13isTransformedEv(const QGraphicsView *self) {
  return self->isTransformed();
}

//  void QGraphicsView::setTransform(const QTransform &matrix, bool combine)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setTransformERK10QTransformb(
    QGraphicsView *self,
    const QTransform *matrix,
    bool combine) {
  self->setTransform(*matrix, combine);
}

//  void QGraphicsView::resetTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView14resetTransformEv(QGraphicsView *self) {
  self->resetTransform();
}

//  void QGraphicsView::rotate(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView6rotateEd(QGraphicsView *self, qreal angle) {
  self->rotate(angle);
}

//  void QGraphicsView::scale(qreal sx, qreal sy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView5scaleEdd(
    QGraphicsView *self,
    qreal sx,
    qreal sy) {
  self->scale(sx, sy);
}

//  void QGraphicsView::shear(qreal sh, qreal sv)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView5shearEdd(
    QGraphicsView *self,
    qreal sh,
    qreal sv) {
  self->shear(sh, sv);
}

//  void QGraphicsView::translate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9translateEdd(
    QGraphicsView *self,
    qreal dx,
    qreal dy) {
  self->translate(dx, dy);
}

//  void QGraphicsView::centerOn(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8centerOnERK7QPointF(
    QGraphicsView *self,
    const QPointF *pos) {
  self->centerOn(*pos);
}

//  void QGraphicsView::centerOn(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8centerOnEdd(
    QGraphicsView *self,
    qreal x,
    qreal y) {
  self->centerOn(x, y);
}

//  void QGraphicsView::centerOn(const QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8centerOnEPK13QGraphicsItem(
    QGraphicsView *self,
    const QGraphicsItem *item) {
  self->centerOn(item);
}

//  void QGraphicsView::ensureVisible(const QRectF &rect, int xmargin, int
//      ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13ensureVisibleERK6QRectFii(
    QGraphicsView *self,
    const QRectF *rect,
    int xmargin,
    int ymargin) {
  self->ensureVisible(*rect, xmargin, ymargin);
}

//  void QGraphicsView::ensureVisible(qreal x, qreal y, qreal w, qreal h, int
//      xmargin, int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13ensureVisibleEddddii(
    QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    int xmargin,
    int ymargin) {
  self->ensureVisible(x, y, w, h, xmargin, ymargin);
}

//  void QGraphicsView::ensureVisible(const QGraphicsItem *item, int xmargin,
//      int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13ensureVisibleEPK13QGraphicsItemii(
    QGraphicsView *self,
    const QGraphicsItem *item,
    int xmargin,
    int ymargin) {
  self->ensureVisible(item, xmargin, ymargin);
}

//  void QGraphicsView::fitInView(const QRectF &rect, Qt::AspectRatioMode
//      aspectRadioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9fitInViewERK6QRectFN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    const QRectF *rect,
    Qt::AspectRatioMode aspectRadioMode) {
  self->fitInView(*rect, aspectRadioMode);
}

//  void QGraphicsView::fitInView(qreal x, qreal y, qreal w, qreal h,
//      Qt::AspectRatioMode aspectRadioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9fitInViewEddddN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    Qt::AspectRatioMode aspectRadioMode) {
  self->fitInView(x, y, w, h, aspectRadioMode);
}

//  void QGraphicsView::fitInView(const QGraphicsItem *item,
//      Qt::AspectRatioMode aspectRadioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9fitInViewEPK13QGraphicsItemN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    const QGraphicsItem *item,
    Qt::AspectRatioMode aspectRadioMode) {
  self->fitInView(item, aspectRadioMode);
}

//  void QGraphicsView::render(QPainter *painter, const QRectF &target, const
//      QRect &source, Qt::AspectRatioMode aspectRatioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView6renderEP8QPainterRK6QRectFRK5QRectN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    QPainter *painter,
    const QRectF *target,
    const QRect *source,
    Qt::AspectRatioMode aspectRatioMode) {
  self->render(painter, *target, *source, aspectRatioMode);
}

//  QGraphicsItem *QGraphicsView::itemAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsView6itemAtERK6QPoint(
    const QGraphicsView *self,
    const QPoint *pos) {
  return self->itemAt(*pos);
}

//  QGraphicsItem *QGraphicsView::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsView6itemAtEii(
    const QGraphicsView *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QPointF QGraphicsView::mapToScene(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsView10mapToSceneERK6QPoint(
    const QGraphicsView *self,
    const QPoint *point) {
  return new QPointF(self->mapToScene(*point));
}

//  QPolygonF QGraphicsView::mapToScene(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsView10mapToSceneERK5QRect(
    const QGraphicsView *self,
    const QRect *rect) {
  return new QPolygonF(self->mapToScene(*rect));
}

//  QPolygonF QGraphicsView::mapToScene(const QPolygon &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsView10mapToSceneERK8QPolygon(
    const QGraphicsView *self,
    const QPolygon *polygon) {
  return new QPolygonF(self->mapToScene(*polygon));
}

//  QPainterPath QGraphicsView::mapToScene(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsView10mapToSceneERK12QPainterPath(
    const QGraphicsView *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapToScene(*path));
}

//  QPoint QGraphicsView::mapFromScene(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK13QGraphicsView12mapFromSceneERK7QPointF(
    const QGraphicsView *self,
    const QPointF *point) {
  return new QPoint(self->mapFromScene(*point));
}

//  QPolygon QGraphicsView::mapFromScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK13QGraphicsView12mapFromSceneERK6QRectF(
    const QGraphicsView *self,
    const QRectF *rect) {
  return new QPolygon(self->mapFromScene(*rect));
}

//  QPolygon QGraphicsView::mapFromScene(const QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK13QGraphicsView12mapFromSceneERK9QPolygonF(
    const QGraphicsView *self,
    const QPolygonF *polygon) {
  return new QPolygon(self->mapFromScene(*polygon));
}

//  QPainterPath QGraphicsView::mapFromScene(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsView12mapFromSceneERK12QPainterPath(
    const QGraphicsView *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapFromScene(*path));
}

//  QPointF QGraphicsView::mapToScene(int x, int y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsView10mapToSceneEii(
    const QGraphicsView *self,
    int x,
    int y) {
  return new QPointF(self->mapToScene(x, y));
}

//  QPolygonF QGraphicsView::mapToScene(int x, int y, int w, int h) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsView10mapToSceneEiiii(
    const QGraphicsView *self,
    int x,
    int y,
    int w,
    int h) {
  return new QPolygonF(self->mapToScene(x, y, w, h));
}

//  QPoint QGraphicsView::mapFromScene(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK13QGraphicsView12mapFromSceneEdd(
    const QGraphicsView *self,
    qreal x,
    qreal y) {
  return new QPoint(self->mapFromScene(x, y));
}

//  QPolygon QGraphicsView::mapFromScene(qreal x, qreal y, qreal w, qreal h)
//      const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK13QGraphicsView12mapFromSceneEdddd(
    const QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygon(self->mapFromScene(x, y, w, h));
}

//  QVariant QGraphicsView::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QGraphicsView16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsView *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  QBrush QGraphicsView::backgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QGraphicsView15backgroundBrushEv(
    const QGraphicsView *self) {
  return new QBrush(self->backgroundBrush());
}

//  void QGraphicsView::setBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView18setBackgroundBrushERK6QBrush(
    QGraphicsView *self,
    const QBrush *brush) {
  self->setBackgroundBrush(*brush);
}

//  QBrush QGraphicsView::foregroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QGraphicsView15foregroundBrushEv(
    const QGraphicsView *self) {
  return new QBrush(self->foregroundBrush());
}

//  void QGraphicsView::setForegroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView18setForegroundBrushERK6QBrush(
    QGraphicsView *self,
    const QBrush *brush) {
  self->setForegroundBrush(*brush);
}

//  void QGraphicsView::invalidateScene(const QRectF &rect,
//      QGraphicsScene::SceneLayers layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView15invalidateSceneERK6QRectF6QFlagsIN14QGraphicsScene10SceneLayerEE(
    QGraphicsView *self,
    const QRectF *rect,
    int layers) {
  self->invalidateScene(
      *rect,
      QFlags<QGraphicsScene::SceneLayer>::fromInt(layers));
}

//  void QGraphicsView::updateSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView15updateSceneRectERK6QRectF(
    QGraphicsView *self,
    const QRectF *rect) {
  self->updateSceneRect(*rect);
}
