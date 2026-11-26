//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxritem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxritem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxritem_p.h>
#include <QtQuick3DXr/private/qquick3dxrview_p.h>
#include <QtQuick3D/private/qquick3dnode_p_p.h>
#include <QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtGui/QColor>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxritem.cpp, line 16, as local:qquick3dxritem.cpp:QQuick3DXrItemPrivate
class QQuick3DXrItemPrivate : public QQuick3DNodePrivate
{
    Q_DECLARE_PUBLIC(QQuick3DXrItem)
public:
    QQuick3DXrItemPrivate() : QQuick3DNodePrivate(QQuick3DXrItemPrivate::Type::Node)
    {
    }

    void setContentItem(QQuickItem *newContentItem)
    {
        Q_Q(QQuick3DXrItem);
        m_contentItem = newContentItem;

        initParentItem();

        if (m_contentItemDestroyedConnection) {
            QObject::disconnect(m_contentItemDestroyedConnection);
            m_contentItemDestroyedConnection = {};
        }
        if (m_contentItem) {
            m_contentItem->setParentItem(m_containerItem);
            m_contentItem->setParent(m_containerItem);
            m_contentItemDestroyedConnection = QObject::connect(m_contentItem, &QObject::destroyed, q, [q]() {
                q->setContentItem(nullptr);
            });

            if (m_automaticHeight) {
                setAutomaticHeightConnection();
            }

            if (m_automaticWidth) {
                setAutomaticWidthConnection();
            }
        }

        updateContent();
    }

    void initParentItem()
    {
        Q_Q(QQuick3DXrItem);
        if (!m_containerItem) {
            m_containerItem = new QQuickRectangle;
            m_containerItem->setTransformOrigin(QQuickItem::TopLeft);
            m_containerItem->setParent(q);
            m_containerItem->setVisible(q->visible());
            QObject::connect(q, &QQuick3DNode::visibleChanged, m_containerItem, [this, q](){
                m_containerItem->setVisible(q->visible());
            });
            QQuickItemPrivate::get(m_containerItem)->requestCustomOverlay();
            auto dataProp = data();
            dataProp.append(&dataProp, m_containerItem);
        }
    }

    void updateContent();

void setAutomaticHeightConnection()
{
    Q_Q(QQuick3DXrItem);
    if (m_automaticHeightConnection && ((m_contentItem == nullptr) || !m_automaticHeight)) {
        QObject::disconnect(m_automaticHeightConnection);
        m_automaticHeightConnection = {};
    }
    if (m_contentItem) {
        m_automaticHeightConnection = QObject::connect(m_contentItem, &QQuickItem::heightChanged, q, [this, q](){
            qreal newHeight = m_contentItem->height()/m_pixelsPerUnit;
            if (m_height != newHeight) {
                m_height = newHeight;
                emit q->heightChanged();
                updateContent();
            }
        });
    }
}

void setAutomaticWidthConnection()
{
    Q_Q(QQuick3DXrItem);
    if (m_automaticWidthConnection && ((m_contentItem == nullptr) || !m_automaticHeight)) {
        QObject::disconnect(m_automaticWidthConnection);
        m_automaticWidthConnection = {};
    }

    if (m_contentItem) {
        m_automaticWidthConnection = QObject::connect(m_contentItem, &QQuickItem::widthChanged, q, [this, q](){
            qreal newWidth = m_contentItem->width()/m_pixelsPerUnit;
            if (m_width != newWidth) {
                m_width = newWidth;
                emit q->widthChanged();
                updateContent();
            }
        });
    }
}

    QQuickItem *m_contentItem = nullptr;
    QQuickRectangle *m_containerItem = nullptr;
    QPointer<QQuick3DXrView> m_XrView;
    QMetaObject::Connection m_contentItemDestroyedConnection;
    QMetaObject::Connection m_automaticHeightConnection;
    QMetaObject::Connection m_automaticWidthConnection;
    QColor m_color = Qt::white;
    qreal m_pixelsPerUnit { 1.0 };
    qreal m_width = 1;
    qreal m_height = 1;
    bool m_manualPixelsPerUnit = false;
    bool m_automaticHeight = false;
    bool m_automaticWidth = false;
};

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxritem.cpp, line 127, as local:qquick3dxritem.cpp:calculatePPU
static inline qreal calculatePPU(qreal pxWidth, qreal pxHeight, qreal diagonal)
{
    return (diagonal > 0) ? std::sqrt((pxWidth * pxWidth) + (pxHeight * pxHeight)) / diagonal : 1.0;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxritem.cpp, line 132, as local:qquick3dxritem.cpp:QQuick3DXrItemPrivate::updateContent
inline void QQuick3DXrItemPrivate::updateContent()
{
    if (!componentComplete)
        return;
    Q_Q(QQuick3DXrItem);
    initParentItem();
    m_containerItem->setColor(m_color);
    if (m_contentItem) {
        if (Q_UNLIKELY(m_manualPixelsPerUnit && m_pixelsPerUnit < 0)) {
            qWarning() << "XrItem invalid pixelPerUnit" << m_pixelsPerUnit;
            return;
        }
        qreal newScale;
        if (m_manualPixelsPerUnit) {
            newScale = 1.0 / m_pixelsPerUnit;

        } else {
            qreal diagonal = std::sqrt((m_width * m_width) + (m_height * m_height));
            qreal ppu = calculatePPU(m_contentItem->width(), m_contentItem->height(), diagonal);
            if (ppu <= 0)
                ppu = 1.0;
            q->setPixelsPerUnit(ppu);
            newScale = 1.0 / ppu;
        }
        QSizeF newSize(m_width / newScale, m_height / newScale);
        m_containerItem->setSize(newSize);
        m_containerItem->setScale(newScale);
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxritem.cpp, line 204, as _ZN14QQuick3DXrItem17componentCompleteEv
inline void QQuick3DXrItem::componentComplete()
{
    Q_D(QQuick3DXrItem);
    QQuick3DNode::componentComplete(); // Sets d->componentComplete, so must be called first

    auto findView = [this]() -> QQuick3DXrView * {
        QQuick3DNode *parent = parentNode();
        while (parent) {
            if (auto *xrView = qobject_cast<QQuick3DXrView*>(parent))
                return xrView;
            parent = parent->parentNode();
        }
        return nullptr;
    };
    d->m_XrView = findView();
    if (d->m_XrView)
        d->m_XrView->registerXrItem(this);
    else
        qWarning("Could not find XrView for XrItem");
    d->updateContent();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxritem.cpp, line 267, as _ZN14QQuick3DXrItem16setPixelsPerUnitEd
inline void QQuick3DXrItem::setPixelsPerUnit(qreal newPixelsPerUnit)
{
    Q_D(QQuick3DXrItem);
    if (qFuzzyCompare(d->m_pixelsPerUnit, newPixelsPerUnit))
        return;

    d->m_pixelsPerUnit = newPixelsPerUnit;

    if (d->m_manualPixelsPerUnit)
        d->updateContent();

    emit pixelsPerUnitChanged();
}
//  -----------------------------------------------------------------------

//  A QQuick3DXrItem that Python can take functions over in. Every QQuick3DXrItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DXrItemCall0)(const void *, int *);
typedef void (*CuteQQuick3DXrItemCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrItemCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrItemCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuick3DXrItemCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DXrItemCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DXrItemCall6)(const void *, int *);
typedef void (*CuteQQuick3DXrItemCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrItemCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrItemCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrItemCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrItemCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrItemCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrItem : public QQuick3DXrItem {
public:
  using QQuick3DXrItem::QQuick3DXrItem;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DXrItem::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DXrItemCall0 call = reinterpret_cast<CuteQQuick3DXrItemCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DXrItem::componentComplete();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DXrItemCall1 call = reinterpret_cast<CuteQQuick3DXrItemCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DXrItemCall2 call = reinterpret_cast<CuteQQuick3DXrItemCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DXrItemCall3 call = reinterpret_cast<CuteQQuick3DXrItemCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DXrItemCall4 call = reinterpret_cast<CuteQQuick3DXrItemCall4>(taken[4]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DXrItemCall5 call = reinterpret_cast<CuteQQuick3DXrItemCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DXrItemCall6 call = reinterpret_cast<CuteQQuick3DXrItemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DXrItemCall7 call = reinterpret_cast<CuteQQuick3DXrItemCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DXrItemCall8 call = reinterpret_cast<CuteQQuick3DXrItemCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DXrItemCall9 call = reinterpret_cast<CuteQQuick3DXrItemCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DXrItemCall10 call = reinterpret_cast<CuteQQuick3DXrItemCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DXrItemCall11 call = reinterpret_cast<CuteQQuick3DXrItemCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DXrItemCall12 call = reinterpret_cast<CuteQQuick3DXrItemCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuick3DXrItem10metaObjectEv(
    const QQuick3DXrItem *self) {
  return self->metaObject();
}

//  void *QQuick3DXrItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuick3DXrItem11qt_metacastEPKc(
    QQuick3DXrItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrItem::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuick3DXrItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DXrItemPrivate *QQuick3DXrItem::d_func()
extern "C" Q_DECL_EXPORT
QQuick3DXrItemPrivate *ritual_ZN14QQuick3DXrItem6d_funcEv(
    QQuick3DXrItem *self) {
  return self->d_func();
}

//  const QQuick3DXrItemPrivate *QQuick3DXrItem::d_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DXrItemPrivate *ritual_ZNK14QQuick3DXrItem6d_funcEv(
    const QQuick3DXrItem *self) {
  return self->d_func();
}

//  QQuick3DXrItem::~QQuick3DXrItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItemD1Ev(QQuick3DXrItem *self) {
  delete self;
}

//  void QQuick3DXrItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem17componentCompleteEv(QQuick3DXrItem *self) {
  self->componentComplete();
}

//  void QQuick3DXrItem::contentItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem18contentItemChangedEv(QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "contentItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "contentItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::pixelsPerUnitChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem20pixelsPerUnitChangedEv(
    QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pixelsPerUnitChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pixelsPerUnitChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::flagsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem12flagsChangedEv(QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "flagsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "flagsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::manualPixelsPerUnitChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem26manualPixelsPerUnitChangedEv(
    QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "manualPixelsPerUnitChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "manualPixelsPerUnitChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::widthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem12widthChangedEv(QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "widthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "widthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::heightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem13heightChangedEv(QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "heightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "heightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem12colorChangedEv(QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "colorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "colorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::automaticHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem22automaticHeightChangedEv(
    QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "automaticHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "automaticHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrItem::automaticWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DXrItem21automaticWidthChangedEv(
    QQuick3DXrItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "automaticWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "automaticWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuick3DXrItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrItem(
    QQuick3DXrItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrItem *>(self)->take(key, call);
}
