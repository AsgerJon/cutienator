//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtCore/qpoint.h>
#include <QtGui/qregion.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicseffect_p.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtWidgets/qgraphicsview.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/qgraphicsproxywidget.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstack.h>
#include <QtCore/qvariant.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qnumeric.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmapcache.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtGui/qinputmethod.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/qgraphicseffect.h>
#endif
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/private/qgraphicswidget_p.h>
#include <QtWidgets/private/qwidgettextcontrol_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtCore/private/qdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/effects/qgraphicseffect.cpp, line 355, as _ZNK28QGraphicsEffectSourcePrivate15invalidateCacheENS_16InvalidateReasonE
inline void QGraphicsEffectSourcePrivate::invalidateCache(InvalidateReason reason) const
{
    if (m_cachedMode != QGraphicsEffect::PadToEffectiveBoundingRect
        && (reason == EffectRectChanged
            || (reason == TransformChanged && m_cachedSystem == Qt::LogicalCoordinates))) {
        return;
    }

    QPixmapCache::remove(m_cacheKey);
}

//  from src/widgets/graphicsview/qgraphicsitem.cpp, line 4624, as _ZN20QGraphicsItemPrivate18sendScenePosChangeEv
inline void QGraphicsItemPrivate::sendScenePosChange()
{
    Q_Q(QGraphicsItem);
    if (scene) {
        if (flags & QGraphicsItem::ItemSendsScenePositionChanges)
            q->itemChange(QGraphicsItem::ItemScenePositionHasChanged, q->scenePos());
        if (scenePosDescendants) {
            for (QGraphicsItem *item : std::as_const(scene->d_func()->scenePosItems)) {
                if (q->isAncestorOf(item))
                    item->itemChange(QGraphicsItem::ItemScenePositionHasChanged, item->scenePos());
            }
        }
    }
}
//  -----------------------------------------------------------------------

//  A QGraphicsItemPrivate that Python can take functions over in. Every QGraphicsItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall1)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall3)(const void *, uint, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall4)(const void *, uint, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsItemPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall7)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsItemPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall10)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsItemPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall13)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsItemPrivate : public QGraphicsItemPrivate {
public:
  using QGraphicsItemPrivate::QGraphicsItemPrivate;
  CuteQGraphicsItemPrivate(const QGraphicsItemPrivate &other) : QGraphicsItemPrivate(other) {}
  void *taken[15] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate30updateSceneTransformFromParentEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate16transformChangedEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate11resolveFontEj")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate14resolvePaletteEj")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate13isProxyWidgetEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate18subFocusItemChangeEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate20focusScopeItemChangeEb")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate18siblingOrderChangeEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate5widthEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate8setWidthEd")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate10resetWidthEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate6heightEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate9setHeightEd")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate11resetHeightEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::updateSceneTransformFromParent()
  void updateSceneTransformFromParent() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall0 call = reinterpret_cast<CuteQGraphicsItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::updateSceneTransformFromParent();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::setPosHelper(const QPointF &pos)
  void setPosHelper(const QPointF &pos) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall1 call = reinterpret_cast<CuteQGraphicsItemPrivateCall1>(taken[1]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::setPosHelper(pos);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::transformChanged()
  void transformChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall2 call = reinterpret_cast<CuteQGraphicsItemPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::transformChanged();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::resolveFont(uint inheritedMask)
  void resolveFont(uint inheritedMask) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall3 call = reinterpret_cast<CuteQGraphicsItemPrivateCall3>(taken[3]);
      call(this, inheritedMask, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::resolveFont(inheritedMask);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::resolvePalette(uint inheritedMask)
  void resolvePalette(uint inheritedMask) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall4 call = reinterpret_cast<CuteQGraphicsItemPrivateCall4>(taken[4]);
      call(this, inheritedMask, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::resolvePalette(inheritedMask);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItemPrivate::isProxyWidget() const
  bool isProxyWidget() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall5 call = reinterpret_cast<CuteQGraphicsItemPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItemPrivate::isProxyWidget();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::subFocusItemChange()
  void subFocusItemChange() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall6 call = reinterpret_cast<CuteQGraphicsItemPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::subFocusItemChange();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::focusScopeItemChange(bool isSubFocusItem)
  void focusScopeItemChange(bool isSubFocusItem) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall7 call = reinterpret_cast<CuteQGraphicsItemPrivateCall7>(taken[7]);
      call(this, isSubFocusItem, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::focusScopeItemChange(isSubFocusItem);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::siblingOrderChange()
  void siblingOrderChange() override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall8 call = reinterpret_cast<CuteQGraphicsItemPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::siblingOrderChange();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsItemPrivate::width() const
  qreal width() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall9 call = reinterpret_cast<CuteQGraphicsItemPrivateCall9>(taken[9]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItemPrivate::width();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::setWidth(qreal a0)
  void setWidth(qreal a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall10 call = reinterpret_cast<CuteQGraphicsItemPrivateCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::setWidth(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::resetWidth()
  void resetWidth() override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall11 call = reinterpret_cast<CuteQGraphicsItemPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::resetWidth();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsItemPrivate::height() const
  qreal height() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall12 call = reinterpret_cast<CuteQGraphicsItemPrivateCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItemPrivate::height();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::setHeight(qreal a0)
  void setHeight(qreal a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall13 call = reinterpret_cast<CuteQGraphicsItemPrivateCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::setHeight(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::resetHeight()
  void resetHeight() override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsItemPrivateCall14 call = reinterpret_cast<CuteQGraphicsItemPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::resetHeight();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QGraphicsItem *QGraphicsItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZN20QGraphicsItemPrivate6q_funcEv(
    QGraphicsItemPrivate *self) {
  return self->q_func();
}

//  const QGraphicsItem *QGraphicsItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsItem *ritual_ZNK20QGraphicsItemPrivate6q_funcEv(
    const QGraphicsItemPrivate *self) {
  return self->q_func();
}

//  QGraphicsItemPrivate::QGraphicsItemPrivate()
extern "C" Q_DECL_EXPORT
QGraphicsItemPrivate *ritual_ZN20QGraphicsItemPrivateC1Ev() {
  return new CuteQGraphicsItemPrivate();
}

//  QGraphicsItemPrivate::~QGraphicsItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivateD1Ev(QGraphicsItemPrivate *self) {
  delete self;
}

//  const QGraphicsItemPrivate *QGraphicsItemPrivate::get(const QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
const QGraphicsItemPrivate *ritual_ZN20QGraphicsItemPrivate3getEPK13QGraphicsItem(
    const QGraphicsItem *item) {
  return QGraphicsItemPrivate::get(item);
}

//  QGraphicsItemPrivate *QGraphicsItemPrivate::get(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
QGraphicsItemPrivate *ritual_ZN20QGraphicsItemPrivate3getEP13QGraphicsItem(
    QGraphicsItem *item) {
  return QGraphicsItemPrivate::get(item);
}

//  void QGraphicsItemPrivate::updateChildWithGraphicsEffectFlagRecursively()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate44updateChildWithGraphicsEffectFlagRecursivelyEv(
    QGraphicsItemPrivate *self) {
  self->updateChildWithGraphicsEffectFlagRecursively();
}

//  void
//      QGraphicsItemPrivate::updateAncestorFlag(QGraphicsItem::GraphicsItemF
//      lag childFlag, AncestorFlag flag, bool enabled, bool root)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate18updateAncestorFlagEN13QGraphicsItem16GraphicsItemFlagENS_12AncestorFlagEbb(
    QGraphicsItemPrivate *self,
    QGraphicsItem::GraphicsItemFlag childFlag,
    QGraphicsItemPrivate::AncestorFlag flag,
    bool enabled,
    bool root) {
  self->updateAncestorFlag(childFlag, flag, enabled, root);
}

//  void QGraphicsItemPrivate::updateAncestorFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate19updateAncestorFlagsEv(
    QGraphicsItemPrivate *self) {
  self->updateAncestorFlags();
}

//  void QGraphicsItemPrivate::setIsMemberOfGroup(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate18setIsMemberOfGroupEb(
    QGraphicsItemPrivate *self,
    bool enabled) {
  self->setIsMemberOfGroup(enabled);
}

//  void QGraphicsItemPrivate::remapItemPos(QEvent *event, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate12remapItemPosEP6QEventP13QGraphicsItem(
    QGraphicsItemPrivate *self,
    QEvent *event,
    QGraphicsItem *item) {
  self->remapItemPos(event, item);
}

//  QTransform QGraphicsItemPrivate::genericMapFromSceneTransform(const
//      QWidget *viewport) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK20QGraphicsItemPrivate28genericMapFromSceneTransformEPK7QWidget(
    const QGraphicsItemPrivate *self,
    const QWidget *viewport) {
  return new QTransform(self->genericMapFromSceneTransform(viewport));
}

//  QPointF QGraphicsItemPrivate::genericMapFromScene(const QPointF &pos,
//      const QWidget *viewport) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK20QGraphicsItemPrivate19genericMapFromSceneERK7QPointFPK7QWidget(
    const QGraphicsItemPrivate *self,
    const QPointF *pos,
    const QWidget *viewport) {
  return new QPointF(self->genericMapFromScene(*pos, viewport));
}

//  bool QGraphicsItemPrivate::itemIsUntransformable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate21itemIsUntransformableEv(
    const QGraphicsItemPrivate *self) {
  return self->itemIsUntransformable();
}

//  void QGraphicsItemPrivate::combineTransformToParent(QTransform *x, const
//      QTransform *viewTransform) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QGraphicsItemPrivate24combineTransformToParentEP10QTransformPKS0_(
    const QGraphicsItemPrivate *self,
    QTransform *x,
    const QTransform *viewTransform) {
  self->combineTransformToParent(x, viewTransform);
}

//  void QGraphicsItemPrivate::combineTransformFromParent(QTransform *x,
//      const QTransform *viewTransform) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QGraphicsItemPrivate26combineTransformFromParentEP10QTransformPKS0_(
    const QGraphicsItemPrivate *self,
    QTransform *x,
    const QTransform *viewTransform) {
  self->combineTransformFromParent(x, viewTransform);
}

//  void QGraphicsItemPrivate::updateSceneTransformFromParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate30updateSceneTransformFromParentEv(
    QGraphicsItemPrivate *self) {
  self->updateSceneTransformFromParent();
}

//  bool QGraphicsItemPrivate::movableAncestorIsSelected(const QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsItemPrivate25movableAncestorIsSelectedEPK13QGraphicsItem(
    const QGraphicsItem *item) {
  return QGraphicsItemPrivate::movableAncestorIsSelected(item);
}

//  void QGraphicsItemPrivate::setPosHelper(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF(
    QGraphicsItemPrivate *self,
    const QPointF *pos) {
  self->setPosHelper(*pos);
}

//  void QGraphicsItemPrivate::setTransformHelper(const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate18setTransformHelperERK10QTransform(
    QGraphicsItemPrivate *self,
    const QTransform *transform) {
  self->setTransformHelper(*transform);
}

//  void QGraphicsItemPrivate::prependGraphicsTransform(QGraphicsTransform
//      *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate24prependGraphicsTransformEP18QGraphicsTransform(
    QGraphicsItemPrivate *self,
    QGraphicsTransform *t) {
  self->prependGraphicsTransform(t);
}

//  void QGraphicsItemPrivate::appendGraphicsTransform(QGraphicsTransform *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate23appendGraphicsTransformEP18QGraphicsTransform(
    QGraphicsItemPrivate *self,
    QGraphicsTransform *t) {
  self->appendGraphicsTransform(t);
}

//  void QGraphicsItemPrivate::setVisibleHelper(bool newVisible, bool
//      explicitly, bool update, bool hiddenByPanel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate16setVisibleHelperEbbbb(
    QGraphicsItemPrivate *self,
    bool newVisible,
    bool explicitly,
    bool update,
    bool hiddenByPanel) {
  self->setVisibleHelper(newVisible, explicitly, update, hiddenByPanel);
}

//  void QGraphicsItemPrivate::setEnabledHelper(bool newEnabled, bool
//      explicitly, bool update)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate16setEnabledHelperEbbb(
    QGraphicsItemPrivate *self,
    bool newEnabled,
    bool explicitly,
    bool update) {
  self->setEnabledHelper(newEnabled, explicitly, update);
}

//  bool QGraphicsItemPrivate::discardUpdateRequest(bool ignoreVisibleBit,
//      bool ignoreDirtyBit, bool ignoreOpacity) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate20discardUpdateRequestEbbb(
    const QGraphicsItemPrivate *self,
    bool ignoreVisibleBit,
    bool ignoreDirtyBit,
    bool ignoreOpacity) {
  return self->discardUpdateRequest(
      ignoreVisibleBit,
      ignoreDirtyBit,
      ignoreOpacity);
}

//  void QGraphicsItemPrivate::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate16transformChangedEv(
    QGraphicsItemPrivate *self) {
  self->transformChanged();
}

//  int QGraphicsItemPrivate::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QGraphicsItemPrivate5depthEv(
    const QGraphicsItemPrivate *self) {
  return self->depth();
}

#if QT_CONFIG(graphicseffect)
//  void QGraphicsItemPrivate::invalidateParentGraphicsEffectsRecursively()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate42invalidateParentGraphicsEffectsRecursivelyEv(
    QGraphicsItemPrivate *self) {
  self->invalidateParentGraphicsEffectsRecursively();
}
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
//  void QGraphicsItemPrivate::invalidateChildGraphicsEffectsRecursively(Inva
//      lidateReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate41invalidateChildGraphicsEffectsRecursivelyENS_16InvalidateReasonE(
    QGraphicsItemPrivate *self,
    QGraphicsItemPrivate::InvalidateReason reason) {
  self->invalidateChildGraphicsEffectsRecursively(reason);
}
#endif  // QT_CONFIG(graphicseffect)

//  void QGraphicsItemPrivate::invalidateDepthRecursively()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate26invalidateDepthRecursivelyEv(
    QGraphicsItemPrivate *self) {
  self->invalidateDepthRecursively();
}

//  void QGraphicsItemPrivate::resolveDepth()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate12resolveDepthEv(
    QGraphicsItemPrivate *self) {
  self->resolveDepth();
}

//  void QGraphicsItemPrivate::addChild(QGraphicsItem *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate8addChildEP13QGraphicsItem(
    QGraphicsItemPrivate *self,
    QGraphicsItem *child) {
  self->addChild(child);
}

//  void QGraphicsItemPrivate::removeChild(QGraphicsItem *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate11removeChildEP13QGraphicsItem(
    QGraphicsItemPrivate *self,
    QGraphicsItem *child) {
  self->removeChild(child);
}

//  void QGraphicsItemPrivate::setParentItemHelper(QGraphicsItem *parent,
//      const QVariant *newParentVariant, const QVariant *thisPointerVariant)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate19setParentItemHelperEP13QGraphicsItemPK8QVariantS4_(
    QGraphicsItemPrivate *self,
    QGraphicsItem *parent,
    const QVariant *newParentVariant,
    const QVariant *thisPointerVariant) {
  self->setParentItemHelper(parent, newParentVariant, thisPointerVariant);
}

//  void QGraphicsItemPrivate::childrenBoundingRectHelper(QTransform *x,
//      QRectF *rect, QGraphicsItem *topMostEffectItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate26childrenBoundingRectHelperEP10QTransformP6QRectFP13QGraphicsItem(
    QGraphicsItemPrivate *self,
    QTransform *x,
    QRectF *rect,
    QGraphicsItem *topMostEffectItem) {
  self->childrenBoundingRectHelper(x, rect, topMostEffectItem);
}

//  void QGraphicsItemPrivate::initStyleOption(QStyleOptionGraphicsItem
//      *option, const QTransform &worldTransform, const QRegion
//      &exposedRegion, bool allItems) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QGraphicsItemPrivate15initStyleOptionEP24QStyleOptionGraphicsItemRK10QTransformRK7QRegionb(
    const QGraphicsItemPrivate *self,
    QStyleOptionGraphicsItem *option,
    const QTransform *worldTransform,
    const QRegion *exposedRegion,
    bool allItems) {
  self->initStyleOption(option, *worldTransform, *exposedRegion, allItems);
}

//  QRectF QGraphicsItemPrivate::effectiveBoundingRect(QGraphicsItem
//      *topMostEffectItem) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsItemPrivate21effectiveBoundingRectEP13QGraphicsItem(
    const QGraphicsItemPrivate *self,
    QGraphicsItem *topMostEffectItem) {
  return new QRectF(self->effectiveBoundingRect(topMostEffectItem));
}

//  QRectF QGraphicsItemPrivate::sceneEffectiveBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsItemPrivate26sceneEffectiveBoundingRectEv(
    const QGraphicsItemPrivate *self) {
  return new QRectF(self->sceneEffectiveBoundingRect());
}

//  QRectF QGraphicsItemPrivate::effectiveBoundingRect(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsItemPrivate21effectiveBoundingRectERK6QRectF(
    const QGraphicsItemPrivate *self,
    const QRectF *rect) {
  return new QRectF(self->effectiveBoundingRect(*rect));
}

//  void QGraphicsItemPrivate::resolveFont(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate11resolveFontEj(
    QGraphicsItemPrivate *self,
    uint inheritedMask) {
  self->resolveFont(inheritedMask);
}

//  void QGraphicsItemPrivate::resolvePalette(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate14resolvePaletteEj(
    QGraphicsItemPrivate *self,
    uint inheritedMask) {
  self->resolvePalette(inheritedMask);
}

//  bool QGraphicsItemPrivate::isProxyWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate13isProxyWidgetEv(
    const QGraphicsItemPrivate *self) {
  return self->isProxyWidget();
}

//  QVariant QGraphicsItemPrivate::extra(Extra type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QGraphicsItemPrivate5extraENS_5ExtraE(
    const QGraphicsItemPrivate *self,
    QGraphicsItemPrivate::Extra type) {
  return new QVariant(self->extra(type));
}

//  void QGraphicsItemPrivate::setExtra(Extra type, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate8setExtraENS_5ExtraERK8QVariant(
    QGraphicsItemPrivate *self,
    QGraphicsItemPrivate::Extra type,
    const QVariant *value) {
  self->setExtra(type, *value);
}

//  void QGraphicsItemPrivate::unsetExtra(Extra type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate10unsetExtraENS_5ExtraE(
    QGraphicsItemPrivate *self,
    QGraphicsItemPrivate::Extra type) {
  self->unsetExtra(type);
}

//  QGraphicsItemCache *QGraphicsItemPrivate::maybeExtraItemCache() const
extern "C" Q_DECL_EXPORT
QGraphicsItemCache *ritual_ZNK20QGraphicsItemPrivate19maybeExtraItemCacheEv(
    const QGraphicsItemPrivate *self) {
  return self->maybeExtraItemCache();
}

//  QGraphicsItemCache *QGraphicsItemPrivate::extraItemCache() const
extern "C" Q_DECL_EXPORT
QGraphicsItemCache *ritual_ZNK20QGraphicsItemPrivate14extraItemCacheEv(
    const QGraphicsItemPrivate *self) {
  return self->extraItemCache();
}

//  void QGraphicsItemPrivate::removeExtraItemCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate20removeExtraItemCacheEv(
    QGraphicsItemPrivate *self) {
  self->removeExtraItemCache();
}

//  void QGraphicsItemPrivate::updatePaintedViewBoundingRects(bool
//      updateChildren)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate30updatePaintedViewBoundingRectsEb(
    QGraphicsItemPrivate *self,
    bool updateChildren) {
  self->updatePaintedViewBoundingRects(updateChildren);
}

//  void QGraphicsItemPrivate::ensureSceneTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate20ensureSceneTransformEv(
    QGraphicsItemPrivate *self) {
  self->ensureSceneTransform();
}

//  bool QGraphicsItemPrivate::hasTranslateOnlySceneTransform()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsItemPrivate30hasTranslateOnlySceneTransformEv(
    QGraphicsItemPrivate *self) {
  return self->hasTranslateOnlySceneTransform();
}

//  void QGraphicsItemPrivate::invalidateChildrenSceneTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate32invalidateChildrenSceneTransformEv(
    QGraphicsItemPrivate *self) {
  self->invalidateChildrenSceneTransform();
}

//  qreal QGraphicsItemPrivate::calcEffectiveOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QGraphicsItemPrivate20calcEffectiveOpacityEv(
    const QGraphicsItemPrivate *self) {
  return self->calcEffectiveOpacity();
}

//  bool QGraphicsItemPrivate::isOpacityNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate13isOpacityNullEv(
    const QGraphicsItemPrivate *self) {
  return self->isOpacityNull();
}

//  bool QGraphicsItemPrivate::isOpacityNull(qreal opacity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsItemPrivate13isOpacityNullEd(qreal opacity) {
  return QGraphicsItemPrivate::isOpacityNull(opacity);
}

//  bool QGraphicsItemPrivate::isFullyTransparent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate18isFullyTransparentEv(
    const QGraphicsItemPrivate *self) {
  return self->isFullyTransparent();
}

//  qreal QGraphicsItemPrivate::effectiveOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QGraphicsItemPrivate16effectiveOpacityEv(
    const QGraphicsItemPrivate *self) {
  return self->effectiveOpacity();
}

//  qreal QGraphicsItemPrivate::combineOpacityFromParent(qreal parentOpacity)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QGraphicsItemPrivate24combineOpacityFromParentEd(
    const QGraphicsItemPrivate *self,
    qreal parentOpacity) {
  return self->combineOpacityFromParent(parentOpacity);
}

//  bool QGraphicsItemPrivate::childrenCombineOpacity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate22childrenCombineOpacityEv(
    const QGraphicsItemPrivate *self) {
  return self->childrenCombineOpacity();
}

//  bool QGraphicsItemPrivate::childrenClippedToShape() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate22childrenClippedToShapeEv(
    const QGraphicsItemPrivate *self) {
  return self->childrenClippedToShape();
}

//  bool QGraphicsItemPrivate::isInvisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsItemPrivate11isInvisibleEv(
    const QGraphicsItemPrivate *self) {
  return self->isInvisible();
}

//  void QGraphicsItemPrivate::markParentDirty(bool updateBoundingRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate15markParentDirtyEb(
    QGraphicsItemPrivate *self,
    bool updateBoundingRect) {
  self->markParentDirty(updateBoundingRect);
}

//  void QGraphicsItemPrivate::setFocusHelper(Qt::FocusReason focusReason,
//      bool climb, bool focusFromHide)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate14setFocusHelperEN2Qt11FocusReasonEbb(
    QGraphicsItemPrivate *self,
    Qt::FocusReason focusReason,
    bool climb,
    bool focusFromHide) {
  self->setFocusHelper(focusReason, climb, focusFromHide);
}

//  void QGraphicsItemPrivate::clearFocusHelper(bool giveFocusToParent, bool
//      hiddenByParentPanel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate16clearFocusHelperEbb(
    QGraphicsItemPrivate *self,
    bool giveFocusToParent,
    bool hiddenByParentPanel) {
  self->clearFocusHelper(giveFocusToParent, hiddenByParentPanel);
}

//  void QGraphicsItemPrivate::setSubFocus(QGraphicsItem *rootItem,
//      QGraphicsItem *stopItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate11setSubFocusEP13QGraphicsItemS1_(
    QGraphicsItemPrivate *self,
    QGraphicsItem *rootItem,
    QGraphicsItem *stopItem) {
  self->setSubFocus(rootItem, stopItem);
}

//  void QGraphicsItemPrivate::clearSubFocus(QGraphicsItem *rootItem,
//      QGraphicsItem *stopItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate13clearSubFocusEP13QGraphicsItemS1_(
    QGraphicsItemPrivate *self,
    QGraphicsItem *rootItem,
    QGraphicsItem *stopItem) {
  self->clearSubFocus(rootItem, stopItem);
}

//  void QGraphicsItemPrivate::resetFocusProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate15resetFocusProxyEv(
    QGraphicsItemPrivate *self) {
  self->resetFocusProxy();
}

//  void QGraphicsItemPrivate::subFocusItemChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate18subFocusItemChangeEv(
    QGraphicsItemPrivate *self) {
  self->subFocusItemChange();
}

//  void QGraphicsItemPrivate::focusScopeItemChange(bool isSubFocusItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate20focusScopeItemChangeEb(
    QGraphicsItemPrivate *self,
    bool isSubFocusItem) {
  self->focusScopeItemChange(isSubFocusItem);
}

//  QTransform QGraphicsItemPrivate::transformToParent() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK20QGraphicsItemPrivate17transformToParentEv(
    const QGraphicsItemPrivate *self) {
  return new QTransform(self->transformToParent());
}

//  void QGraphicsItemPrivate::ensureSortedChildren()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate20ensureSortedChildrenEv(
    QGraphicsItemPrivate *self) {
  self->ensureSortedChildren();
}

//  bool QGraphicsItemPrivate::insertionOrder(QGraphicsItem *a, QGraphicsItem
//      *b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QGraphicsItemPrivate14insertionOrderEP13QGraphicsItemS1_(
    QGraphicsItem *a,
    QGraphicsItem *b) {
  return QGraphicsItemPrivate::insertionOrder(a, b);
}

//  void QGraphicsItemPrivate::ensureSequentialSiblingIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate28ensureSequentialSiblingIndexEv(
    QGraphicsItemPrivate *self) {
  self->ensureSequentialSiblingIndex();
}

//  void QGraphicsItemPrivate::sendScenePosChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate18sendScenePosChangeEv(
    QGraphicsItemPrivate *self) {
  self->sendScenePosChange();
}

//  void QGraphicsItemPrivate::siblingOrderChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate18siblingOrderChangeEv(
    QGraphicsItemPrivate *self) {
  self->siblingOrderChange();
}

//  qreal QGraphicsItemPrivate::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QGraphicsItemPrivate5widthEv(
    const QGraphicsItemPrivate *self) {
  return self->width();
}

//  void QGraphicsItemPrivate::setWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate8setWidthEd(
    QGraphicsItemPrivate *self,
    qreal a0) {
  self->setWidth(a0);
}

//  void QGraphicsItemPrivate::resetWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate10resetWidthEv(
    QGraphicsItemPrivate *self) {
  self->resetWidth();
}

//  qreal QGraphicsItemPrivate::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QGraphicsItemPrivate6heightEv(
    const QGraphicsItemPrivate *self) {
  return self->height();
}

//  void QGraphicsItemPrivate::setHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate9setHeightEd(
    QGraphicsItemPrivate *self,
    qreal a0) {
  self->setHeight(a0);
}

//  void QGraphicsItemPrivate::resetHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsItemPrivate11resetHeightEv(
    QGraphicsItemPrivate *self) {
  self->resetHeight();
}

//  a Python function taken by a CuteQGraphicsItemPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsItemPrivate(
    QGraphicsItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsItemPrivate *>(self)->take(key, call);
}

//  void QGraphicsItemPrivate::updateSceneTransformFromParent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate30updateSceneTransformFromParentEv(
    QGraphicsItemPrivate *self) {
  self->QGraphicsItemPrivate::updateSceneTransformFromParent();
}

//  void QGraphicsItemPrivate::setPosHelper(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF(
    QGraphicsItemPrivate *self,
    const QPointF *pos) {
  self->QGraphicsItemPrivate::setPosHelper(*pos);
}

//  void QGraphicsItemPrivate::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate16transformChangedEv(
    QGraphicsItemPrivate *self) {
  self->QGraphicsItemPrivate::transformChanged();
}

//  void QGraphicsItemPrivate::resolveFont(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate11resolveFontEj(
    QGraphicsItemPrivate *self,
    uint inheritedMask) {
  self->QGraphicsItemPrivate::resolveFont(inheritedMask);
}

//  void QGraphicsItemPrivate::resolvePalette(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate14resolvePaletteEj(
    QGraphicsItemPrivate *self,
    uint inheritedMask) {
  self->QGraphicsItemPrivate::resolvePalette(inheritedMask);
}

//  bool QGraphicsItemPrivate::isProxyWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QGraphicsItemPrivate13isProxyWidgetEv(
    const QGraphicsItemPrivate *self) {
  return self->QGraphicsItemPrivate::isProxyWidget();
}

//  void QGraphicsItemPrivate::subFocusItemChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate18subFocusItemChangeEv(
    QGraphicsItemPrivate *self) {
  self->QGraphicsItemPrivate::subFocusItemChange();
}

//  void QGraphicsItemPrivate::focusScopeItemChange(bool isSubFocusItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate20focusScopeItemChangeEb(
    QGraphicsItemPrivate *self,
    bool isSubFocusItem) {
  self->QGraphicsItemPrivate::focusScopeItemChange(isSubFocusItem);
}

//  void QGraphicsItemPrivate::siblingOrderChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate18siblingOrderChangeEv(
    QGraphicsItemPrivate *self) {
  self->QGraphicsItemPrivate::siblingOrderChange();
}

//  qreal QGraphicsItemPrivate::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QGraphicsItemPrivate5widthEv(
    const QGraphicsItemPrivate *self) {
  return self->QGraphicsItemPrivate::width();
}

//  void QGraphicsItemPrivate::setWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate8setWidthEd(
    QGraphicsItemPrivate *self,
    qreal a0) {
  self->QGraphicsItemPrivate::setWidth(a0);
}

//  void QGraphicsItemPrivate::resetWidth()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate10resetWidthEv(
    QGraphicsItemPrivate *self) {
  self->QGraphicsItemPrivate::resetWidth();
}

//  qreal QGraphicsItemPrivate::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QGraphicsItemPrivate6heightEv(
    const QGraphicsItemPrivate *self) {
  return self->QGraphicsItemPrivate::height();
}

//  void QGraphicsItemPrivate::setHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate9setHeightEd(
    QGraphicsItemPrivate *self,
    qreal a0) {
  self->QGraphicsItemPrivate::setHeight(a0);
}

//  void QGraphicsItemPrivate::resetHeight()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QGraphicsItemPrivate11resetHeightEv(
    QGraphicsItemPrivate *self) {
  self->QGraphicsItemPrivate::resetHeight();
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
