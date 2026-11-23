//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtransform.h>
#include <QtCore/qrect.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include "qdebug.h"
#include "qgraphicsscene.h"
#include "qgraphicsitem_p.h"
#include "qgraphicsscene_p.h"
#include "qgraphicswidget.h"
#include "qgraphicssceneindex_p.h"
#include "qgraphicsscenebsptreeindex_p.h"
#include <QtGui/qpainterpath.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 521, as _ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF
inline void QGraphicsSceneIndex::updateSceneRect(const QRectF &rect)
{
    Q_UNUSED(rect);
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 529, as _ZN19QGraphicsSceneIndex5clearEv
inline void QGraphicsSceneIndex::clear()
{
    const QList<QGraphicsItem *> allItems = items();
    for (int i = 0 ; i < allItems.size(); ++i)
        removeItem(allItems.at(i));
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 561, as _ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem
inline void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)
{
    removeItem(item);
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 591, as _ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK13QGraphicsItem
inline void QGraphicsSceneIndex::prepareBoundingRectChange(const QGraphicsItem *item)
{
    Q_UNUSED(item);
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 344, as _ZNK19QGraphicsSceneIndex5sceneEv
inline QGraphicsScene* QGraphicsSceneIndex::scene() const
{
    Q_D(const QGraphicsSceneIndex);
    return d->scene;
}
//  -----------------------------------------------------------------------

//  Only a class built on QGraphicsSceneIndex may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsSceneIndex : QGraphicsSceneIndex {
  using QGraphicsSceneIndex::updateSceneRect;
  using QGraphicsSceneIndex::clear;
  using QGraphicsSceneIndex::deleteItem;
  using QGraphicsSceneIndex::prepareBoundingRectChange;
};

//  A QGraphicsSceneIndex that Python can take functions over in. Every QGraphicsSceneIndex
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneIndexCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQGraphicsSceneIndexCall1)(const void *, int *);
typedef void (*CuteQGraphicsSceneIndexCall2)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQGraphicsSceneIndexCall3)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQGraphicsSceneIndexCall4)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQGraphicsSceneIndexCall5)(const void *, const QGraphicsItem *, int *);
typedef bool (*CuteQGraphicsSceneIndexCall6)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsSceneIndexCall7)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsSceneIndexCall8)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsSceneIndexCall9)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsSceneIndexCall10)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsSceneIndexCall11)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsSceneIndexCall12)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsSceneIndex : public QGraphicsSceneIndex {
public:
  using QGraphicsSceneIndex::QGraphicsSceneIndex;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex5clearEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex7addItemEP13QGraphicsItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex10removeItemEP13QGraphicsItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK13QGraphicsItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsSceneIndex::updateSceneRect(const QRectF &rect)
  void updateSceneRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall0 call = reinterpret_cast<CuteQGraphicsSceneIndexCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsSceneIndex::updateSceneRect(rect);
  }

  //  void QGraphicsSceneIndex::clear()
  void clear() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall1 call = reinterpret_cast<CuteQGraphicsSceneIndexCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsSceneIndex::clear();
  }

  //  void QGraphicsSceneIndex::addItem(QGraphicsItem *item)
  void addItem(QGraphicsItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall2 call = reinterpret_cast<CuteQGraphicsSceneIndexCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
  }

  //  void QGraphicsSceneIndex::removeItem(QGraphicsItem *item)
  void removeItem(QGraphicsItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall3 call = reinterpret_cast<CuteQGraphicsSceneIndexCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
  }

  //  void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)
  void deleteItem(QGraphicsItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall4 call = reinterpret_cast<CuteQGraphicsSceneIndexCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGraphicsSceneIndex::deleteItem(item);
  }

  //  void QGraphicsSceneIndex::prepareBoundingRectChange(const
  //      QGraphicsItem *item)
  void prepareBoundingRectChange(const QGraphicsItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall5 call = reinterpret_cast<CuteQGraphicsSceneIndexCall5>(taken[5]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGraphicsSceneIndex::prepareBoundingRectChange(item);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall6 call = reinterpret_cast<CuteQGraphicsSceneIndexCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall7 call = reinterpret_cast<CuteQGraphicsSceneIndexCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall8 call = reinterpret_cast<CuteQGraphicsSceneIndexCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall9 call = reinterpret_cast<CuteQGraphicsSceneIndexCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall10 call = reinterpret_cast<CuteQGraphicsSceneIndexCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall11 call = reinterpret_cast<CuteQGraphicsSceneIndexCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsSceneIndexCall12 call = reinterpret_cast<CuteQGraphicsSceneIndexCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsSceneIndex::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QGraphicsSceneIndex10metaObjectEv(
    const QGraphicsSceneIndex *self) {
  return self->metaObject();
}

//  QGraphicsSceneIndex::~QGraphicsSceneIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneIndexD1Ev(QGraphicsSceneIndex *self) {
  delete self;
}

//  QGraphicsScene *QGraphicsSceneIndex::scene() const
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZNK19QGraphicsSceneIndex5sceneEv(
    const QGraphicsSceneIndex *self) {
  return self->scene();
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::items(Qt::SortOrder order)
//      const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex5itemsEN2Qt9SortOrderE(
    const QGraphicsSceneIndex *self,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->items(order));
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QPointF &pos,
//      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex5itemsERK7QPointFN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsSceneIndex *self,
    const QPointF *pos,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *pos,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QRectF &rect,
//      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex5itemsERK6QRectFN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsSceneIndex *self,
    const QRectF *rect,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *rect,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QPolygonF
//      &polygon, Qt::ItemSelectionMode mode, Qt::SortOrder order, const
//      QTransform &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex5itemsERK9QPolygonFN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsSceneIndex *self,
    const QPolygonF *polygon,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *polygon,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::items(const QPainterPath
//      &path, Qt::ItemSelectionMode mode, Qt::SortOrder order, const
//      QTransform &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex5itemsERK12QPainterPathN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsSceneIndex *self,
    const QPainterPath *path,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *path,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::estimateItems(const QPointF
//      &point, Qt::SortOrder order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex13estimateItemsERK7QPointFN2Qt9SortOrderE(
    const QGraphicsSceneIndex *self,
    const QPointF *point,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->estimateItems(*point, order));
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::estimateItems(const QRectF
//      &rect, Qt::SortOrder order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex13estimateItemsERK6QRectFN2Qt9SortOrderE(
    const QGraphicsSceneIndex *self,
    const QRectF *rect,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->estimateItems(*rect, order));
}

//  QList<QGraphicsItem *> QGraphicsSceneIndex::estimateTopLevelItems(const
//      QRectF &a0, Qt::SortOrder order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK19QGraphicsSceneIndex21estimateTopLevelItemsERK6QRectFN2Qt9SortOrderE(
    const QGraphicsSceneIndex *self,
    const QRectF *a0,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->estimateTopLevelItems(*a0, order));
}

//  void QGraphicsSceneIndex::updateSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF(
    QGraphicsSceneIndex *self,
    const QRectF *rect) {
  self->updateSceneRect(*rect);
}

//  void QGraphicsSceneIndex::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneIndex5clearEv(QGraphicsSceneIndex *self) {
  self->clear();
}

//  void QGraphicsSceneIndex::addItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneIndex7addItemEP13QGraphicsItem(
    QGraphicsSceneIndex *self,
    QGraphicsItem *item) {
  self->addItem(item);
}

//  void QGraphicsSceneIndex::removeItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneIndex10removeItemEP13QGraphicsItem(
    QGraphicsSceneIndex *self,
    QGraphicsItem *item) {
  self->removeItem(item);
}

//  void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem(
    QGraphicsSceneIndex *self,
    QGraphicsItem *item) {
  self->deleteItem(item);
}

//  void QGraphicsSceneIndex::prepareBoundingRectChange(const QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK13QGraphicsItem(
    QGraphicsSceneIndex *self,
    const QGraphicsItem *item) {
  self->prepareBoundingRectChange(item);
}

//  a Python function taken by a CuteQGraphicsSceneIndex, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneIndex(
    QGraphicsSceneIndex *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneIndex *>(self)->take(key, call);
}

//  void QGraphicsSceneIndex::updateSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF(
    QGraphicsSceneIndex *self,
    const QRectF *rect) {
  static_cast<OwnQGraphicsSceneIndex *>(self)->OwnQGraphicsSceneIndex::updateSceneRect(
      *rect);
}

//  void QGraphicsSceneIndex::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsSceneIndex5clearEv(QGraphicsSceneIndex *self) {
  static_cast<OwnQGraphicsSceneIndex *>(self)->OwnQGraphicsSceneIndex::clear();
}

//  void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem(
    QGraphicsSceneIndex *self,
    QGraphicsItem *item) {
  static_cast<OwnQGraphicsSceneIndex *>(self)->OwnQGraphicsSceneIndex::deleteItem(
      item);
}

//  void QGraphicsSceneIndex::prepareBoundingRectChange(const QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK13QGraphicsItem(
    QGraphicsSceneIndex *self,
    const QGraphicsItem *item) {
  static_cast<OwnQGraphicsSceneIndex *>(self)->OwnQGraphicsSceneIndex::prepareBoundingRectChange(
      item);
}
