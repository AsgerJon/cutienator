//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickrendercontrol.h>
#include <QtQml/qjsengine.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <QtQuick/private/qquickscreen_p.h>
#include <QtQuick/private/qquicksafearea_p.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qpen.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qstylehints.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtGui/qinputmethod.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQuick/private/qquickstategroup_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickaccessibleattached_p.h>
#include <QtQuick/private/qquickattachedpropertypropagator_p.h>
#include <QtQuick/private/qquickhoverhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtCore/private/qdebug_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#if QT_CONFIG(cursor)
# include <QtGui/qcursor.h>
#endif
#if QT_CONFIG(accessibility)
# include <QtGui/private/qaccessiblecache_p.h>
#endif
#include <QtCore/qpointer.h>
#include <algorithm>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 160, as _ZN14QQuickContentsC1EP10QQuickItem
inline QQuickContents::QQuickContents(QQuickItem *item)
: m_item(item)
{
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 165, as _ZN14QQuickContentsD1Ev
inline QQuickContents::~QQuickContents()
{
    inDestructor = true;
    QList<QQuickItem *> children = m_item->childItems();
    for (int i = 0; i < children.size(); ++i) {
        QQuickItem *child = children.at(i);
        QQuickItemPrivate::get(child)->removeItemChangeListener(this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Destroyed);
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 245, as _ZN14QQuickContents8completeEv
inline void QQuickContents::complete()
{
    QQuickItemPrivate::get(m_item)->addItemChangeListener(this, QQuickItemPrivate::Children);

    QList<QQuickItem *> children = m_item->childItems();
    for (int i = 0; i < children.size(); ++i) {
        QQuickItem *child = children.at(i);
        QQuickItemPrivate::get(child)->addItemChangeListener(this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Destroyed);
        //###what about changes to visibility?
    }
    calcGeometry();
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 263, as _ZN14QQuickContents19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickContents::itemGeometryChanged(QQuickItem *changed, QQuickGeometryChange change, const QRectF &)
{
    Q_UNUSED(changed);
    bool wChanged = false;
    bool hChanged = false;
    //### we can only pass changed if the left edge has moved left, or the right edge has moved right
    if (change.horizontalChange())
        wChanged = calcWidth(/*changed*/);
    if (change.verticalChange())
        hChanged = calcHeight(/*changed*/);
    if (wChanged || hChanged)
        updateRect();
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 277, as _ZN14QQuickContents13itemDestroyedEP10QQuickItem
inline void QQuickContents::itemDestroyed(QQuickItem *item)
{
    if (item)
        QQuickItemPrivate::get(item)->removeItemChangeListener(this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Destroyed);
    calcGeometry();
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 291, as _ZN14QQuickContents14itemChildAddedEP10QQuickItemS1_
inline void QQuickContents::itemChildAdded(QQuickItem *, QQuickItem *item)
{
    if (item)
        QQuickItemPrivate::get(item)->addItemChangeListener(this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Destroyed);
    calcGeometry(item);
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 284, as _ZN14QQuickContents16itemChildRemovedEP10QQuickItemS1_
inline void QQuickContents::itemChildRemoved(QQuickItem *, QQuickItem *item)
{
    if (item)
        QQuickItemPrivate::get(item)->removeItemChangeListener(this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Destroyed);
    calcGeometry();
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 175, as _ZN14QQuickContents10calcHeightEP10QQuickItem
inline bool QQuickContents::calcHeight(QQuickItem *changed)
{
    qreal oldy = m_contents.y();
    qreal oldheight = m_contents.height();

    if (changed) {
        qreal top = oldy;
        qreal bottom = oldy + oldheight;
        qreal y = changed->y();
        if (y + changed->height() > bottom)
            bottom = y + changed->height();
        if (y < top)
            top = y;
        m_contents.setY(top);
        m_contents.setHeight(bottom - top);
    } else {
        qreal top = std::numeric_limits<qreal>::max();
        qreal bottom = -std::numeric_limits<qreal>::max();
        QList<QQuickItem *> children = m_item->childItems();
        for (int i = 0; i < children.size(); ++i) {
            QQuickItem *child = children.at(i);
            qreal y = child->y();
            if (y + child->height() > bottom)
                bottom = y + child->height();
            if (y < top)
                top = y;
        }
        if (!children.isEmpty())
            m_contents.setY(top);
        m_contents.setHeight(qMax(bottom - top, qreal(0.0)));
    }

    return (m_contents.height() != oldheight || m_contents.y() != oldy);
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 210, as _ZN14QQuickContents9calcWidthEP10QQuickItem
inline bool QQuickContents::calcWidth(QQuickItem *changed)
{
    qreal oldx = m_contents.x();
    qreal oldwidth = m_contents.width();

    if (changed) {
        qreal left = oldx;
        qreal right = oldx + oldwidth;
        qreal x = changed->x();
        if (x + changed->width() > right)
            right = x + changed->width();
        if (x < left)
            left = x;
        m_contents.setX(left);
        m_contents.setWidth(right - left);
    } else {
        qreal left = std::numeric_limits<qreal>::max();
        qreal right = -std::numeric_limits<qreal>::max();
        QList<QQuickItem *> children = m_item->childItems();
        for (int i = 0; i < children.size(); ++i) {
            QQuickItem *child = children.at(i);
            qreal x = child->x();
            if (x + child->width() > right)
                right = x + child->width();
            if (x < left)
                left = x;
        }
        if (!children.isEmpty())
            m_contents.setX(left);
        m_contents.setWidth(qMax(right - left, qreal(0.0)));
    }

    return (m_contents.width() != oldwidth || m_contents.x() != oldx);
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 258, as _ZN14QQuickContents10updateRectEv
inline void QQuickContents::updateRect()
{
    QQuickItemPrivate::get(m_item)->emitChildrenRectChanged(rectF());
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickContents may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickContents : QQuickContents {
  using QQuickContents::itemGeometryChanged;
  using QQuickContents::itemDestroyed;
  using QQuickContents::itemChildAdded;
  using QQuickContents::itemChildRemoved;
};

//  A QQuickContents that Python can take functions over in. Every QQuickContents
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickContentsCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickContentsCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickContentsCall2)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickContentsCall3)(const void *, QQuickItem *, QQuickItem *, int *);
class CuteQQuickContents : public QQuickContents {
public:
  using QQuickContents::QQuickContents;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuickContents19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuickContents13itemDestroyedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuickContents14itemChildAddedEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuickContents16itemChildRemovedEP10QQuickItemS1_")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QQuickContents::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContentsCall0 call = reinterpret_cast<CuteQQuickContentsCall0>(taken[0]);
      call(this, item, &change, &a2, &handled);
      if (handled) return;
    }
    QQuickContents::itemGeometryChanged(item, change, a2);
  }

  //  void QQuickContents::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContentsCall1 call = reinterpret_cast<CuteQQuickContentsCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickContents::itemDestroyed(item);
  }

  //  void QQuickContents::itemChildAdded(QQuickItem *a0, QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickContentsCall2 call = reinterpret_cast<CuteQQuickContentsCall2>(taken[2]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickContents::itemChildAdded(a0, a1);
  }

  //  void QQuickContents::itemChildRemoved(QQuickItem *a0, QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickContentsCall3 call = reinterpret_cast<CuteQQuickContentsCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickContents::itemChildRemoved(a0, a1);
  }
};

//  QQuickContents::QQuickContents(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickContents *ritual_ZN14QQuickContentsC1EP10QQuickItem(QQuickItem *item) {
  return new CuteQQuickContents(item);
}

//  QQuickContents::~QQuickContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContentsD1Ev(QQuickContents *self) {
  delete self;
}

//  QRectF QQuickContents::rectF() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QQuickContents5rectFEv(const QQuickContents *self) {
  return new QRectF(self->rectF());
}

//  void QQuickContents::calcGeometry(QQuickItem *changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContents12calcGeometryEP10QQuickItem(
    QQuickContents *self,
    QQuickItem *changed) {
  self->calcGeometry(changed);
}

//  void QQuickContents::complete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContents8completeEv(QQuickContents *self) {
  self->complete();
}

//  void QQuickContents::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContents19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickContents *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->itemGeometryChanged(item, *change, *a2);
}

//  void QQuickContents::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContents13itemDestroyedEP10QQuickItem(
    QQuickContents *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickContents::itemChildAdded(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContents14itemChildAddedEP10QQuickItemS1_(
    QQuickContents *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemChildAdded(a0, a1);
}

//  void QQuickContents::itemChildRemoved(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContents16itemChildRemovedEP10QQuickItemS1_(
    QQuickContents *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemChildRemoved(a0, a1);
}

//  bool QQuickContents::calcHeight(QQuickItem *changed)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickContents10calcHeightEP10QQuickItem(
    QQuickContents *self,
    QQuickItem *changed) {
  return self->calcHeight(changed);
}

//  bool QQuickContents::calcWidth(QQuickItem *changed)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickContents9calcWidthEP10QQuickItem(
    QQuickContents *self,
    QQuickItem *changed) {
  return self->calcWidth(changed);
}

//  void QQuickContents::updateRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickContents10updateRectEv(QQuickContents *self) {
  self->updateRect();
}

//  a Python function taken by a CuteQQuickContents, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContents(
    QQuickContents *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContents *>(self)->take(key, call);
}

//  void QQuickContents::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickContents19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickContents *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  static_cast<OwnQQuickContents *>(self)->OwnQQuickContents::itemGeometryChanged(
      item,
      *change,
      *a2);
}

//  void QQuickContents::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickContents13itemDestroyedEP10QQuickItem(
    QQuickContents *self,
    QQuickItem *item) {
  static_cast<OwnQQuickContents *>(self)->OwnQQuickContents::itemDestroyed(
      item);
}

//  void QQuickContents::itemChildAdded(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickContents14itemChildAddedEP10QQuickItemS1_(
    QQuickContents *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  static_cast<OwnQQuickContents *>(self)->OwnQQuickContents::itemChildAdded(
      a0,
      a1);
}

//  void QQuickContents::itemChildRemoved(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickContents16itemChildRemovedEP10QQuickItemS1_(
    QQuickContents *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  static_cast<OwnQQuickContents *>(self)->OwnQQuickContents::itemChildRemoved(
      a0,
      a1);
}
