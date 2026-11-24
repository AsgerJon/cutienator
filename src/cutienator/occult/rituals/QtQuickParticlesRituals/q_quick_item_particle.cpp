//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickitemparticle_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickitemparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickItemParticle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickItemParticle : QQuickItemParticle {
  using QQuickItemParticle::reset;
  using QQuickItemParticle::commit;
  using QQuickItemParticle::initialize;
};

//  A QQuickItemParticle that Python can take functions over in. Every QQuickItemParticle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickItemParticleCall0)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickItemParticleCall1)(const void *, int *);
typedef void (*CuteQQuickItemParticleCall2)(const void *, int, int, int *);
typedef void (*CuteQQuickItemParticleCall3)(const void *, int, int, int *);
typedef void (*CuteQQuickItemParticleCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickItemParticleCall5)(const void *, int *);
typedef void (*CuteQQuickItemParticleCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickItemParticleCall7)(const void *, int *);
typedef const QRectF * (*CuteQQuickItemParticleCall8)(const void *, int *);
typedef bool (*CuteQQuickItemParticleCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickItemParticleCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickItemParticleCall11)(const void *, int *);
typedef void * (*CuteQQuickItemParticleCall12)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemParticleCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemParticleCall14)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickItemParticleCall15)(const void *, int *);
typedef void (*CuteQQuickItemParticleCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickItemParticleCall17)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickItemParticleCall18)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickItemParticleCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemParticleCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickItemParticleCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemParticleCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemParticleCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemParticleCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickItemParticleCall25)(const void *, int *);
typedef void (*CuteQQuickItemParticleCall26)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickItemParticleCall27)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickItemParticleCall28)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickItemParticleCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemParticleCall30)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickItemParticleCall31)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemParticleCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemParticleCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemParticleCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickItemParticleCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickItemParticleCall36)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickItemParticleCall37)(const void *, int *);
typedef void (*CuteQQuickItemParticleCall38)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemParticleCall39)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemParticleCall40)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemParticleCall41)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemParticleCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemParticleCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemParticleCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickItemParticle : public QQuickItemParticle {
public:
  using QQuickItemParticle::QQuickItemParticle;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter5resetEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter6commitEii")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter10initializeEii")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[31] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[38] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSGNode *QQuickItemParticle::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemParticleCall0 call = reinterpret_cast<CuteQQuickItemParticleCall0>(taken[0]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItemParticle::updatePaintNode(a0, a1);
  }

  //  void QQuickItemParticle::reset()
  void reset() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemParticleCall1 call = reinterpret_cast<CuteQQuickItemParticleCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemParticle::reset();
  }

  //  void QQuickItemParticle::commit(int gIdx, int pIdx)
  void commit(int gIdx, int pIdx) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemParticleCall2 call = reinterpret_cast<CuteQQuickItemParticleCall2>(taken[2]);
      call(this, gIdx, pIdx, &handled);
      if (handled) return;
    }
    QQuickItemParticle::commit(gIdx, pIdx);
  }

  //  void QQuickItemParticle::initialize(int gIdx, int pIdx)
  void initialize(int gIdx, int pIdx) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemParticleCall3 call = reinterpret_cast<CuteQQuickItemParticleCall3>(taken[3]);
      call(this, gIdx, pIdx, &handled);
      if (handled) return;
    }
    QQuickItemParticle::initialize(gIdx, pIdx);
  }

  //  void QQuickParticlePainter::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemParticleCall4 call = reinterpret_cast<CuteQQuickItemParticleCall4>(taken[4]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::itemChange(a0, a1);
  }

  //  void QQuickParticlePainter::sceneGraphInvalidated()
  void sceneGraphInvalidated() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemParticleCall5 call = reinterpret_cast<CuteQQuickItemParticleCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::sceneGraphInvalidated();
  }

  //  void QQuickParticlePainter::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemParticleCall6 call = reinterpret_cast<CuteQQuickItemParticleCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::componentComplete();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemParticleCall7 call = reinterpret_cast<CuteQQuickItemParticleCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemParticleCall8 call = reinterpret_cast<CuteQQuickItemParticleCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemParticleCall9 call = reinterpret_cast<CuteQQuickItemParticleCall9>(taken[9]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemParticleCall10 call = reinterpret_cast<CuteQQuickItemParticleCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemParticleCall11 call = reinterpret_cast<CuteQQuickItemParticleCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickItemParticleCall12 call = reinterpret_cast<CuteQQuickItemParticleCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickItemParticleCall13 call = reinterpret_cast<CuteQQuickItemParticleCall13>(taken[13]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickItemParticleCall14 call = reinterpret_cast<CuteQQuickItemParticleCall14>(taken[14]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemParticleCall15 call = reinterpret_cast<CuteQQuickItemParticleCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickItemParticleCall16 call = reinterpret_cast<CuteQQuickItemParticleCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickItemParticleCall17 call = reinterpret_cast<CuteQQuickItemParticleCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickItemParticleCall18 call = reinterpret_cast<CuteQQuickItemParticleCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickItemParticleCall19 call = reinterpret_cast<CuteQQuickItemParticleCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickItemParticleCall20 call = reinterpret_cast<CuteQQuickItemParticleCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickItemParticleCall21 call = reinterpret_cast<CuteQQuickItemParticleCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickItemParticleCall22 call = reinterpret_cast<CuteQQuickItemParticleCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickItemParticleCall23 call = reinterpret_cast<CuteQQuickItemParticleCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickItemParticleCall24 call = reinterpret_cast<CuteQQuickItemParticleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickItemParticleCall25 call = reinterpret_cast<CuteQQuickItemParticleCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickItemParticleCall26 call = reinterpret_cast<CuteQQuickItemParticleCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickItemParticleCall27 call = reinterpret_cast<CuteQQuickItemParticleCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickItemParticleCall28 call = reinterpret_cast<CuteQQuickItemParticleCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickItemParticleCall29 call = reinterpret_cast<CuteQQuickItemParticleCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickItemParticleCall30 call = reinterpret_cast<CuteQQuickItemParticleCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickItemParticleCall31 call = reinterpret_cast<CuteQQuickItemParticleCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickItemParticleCall32 call = reinterpret_cast<CuteQQuickItemParticleCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickItemParticleCall33 call = reinterpret_cast<CuteQQuickItemParticleCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickItemParticleCall34 call = reinterpret_cast<CuteQQuickItemParticleCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickItemParticleCall35 call = reinterpret_cast<CuteQQuickItemParticleCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickItemParticleCall36 call = reinterpret_cast<CuteQQuickItemParticleCall36>(taken[36]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickItemParticleCall37 call = reinterpret_cast<CuteQQuickItemParticleCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickItemParticleCall38 call = reinterpret_cast<CuteQQuickItemParticleCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickItemParticleCall39 call = reinterpret_cast<CuteQQuickItemParticleCall39>(taken[39]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickItemParticleCall40 call = reinterpret_cast<CuteQQuickItemParticleCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickItemParticleCall41 call = reinterpret_cast<CuteQQuickItemParticleCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickItemParticleCall42 call = reinterpret_cast<CuteQQuickItemParticleCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickItemParticleCall43 call = reinterpret_cast<CuteQQuickItemParticleCall43>(taken[43]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickItemParticleCall44 call = reinterpret_cast<CuteQQuickItemParticleCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickItemParticle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickItemParticle10metaObjectEv(
    const QQuickItemParticle *self) {
  return self->metaObject();
}

//  QString QQuickItemParticle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickItemParticle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItemParticle::tr(s, c, n));
}

//  void QQuickItemParticle::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle21qt_qmlMarker_attachedEv(
    QQuickItemParticle *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickItemParticle::QQuickItemParticle(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickItemParticle *ritual_ZN18QQuickItemParticleC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickItemParticle(parent);
}

//  QQuickItemParticle::~QQuickItemParticle()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticleD1Ev(QQuickItemParticle *self) {
  delete self;
}

//  bool QQuickItemParticle::fade() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickItemParticle4fadeEv(const QQuickItemParticle *self) {
  return self->fade();
}

//  QSGNode *QQuickItemParticle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN18QQuickItemParticle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickItemParticle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  QQuickItemParticleAttached
//      *QQuickItemParticle::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickItemParticleAttached *ritual_ZN18QQuickItemParticle21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickItemParticle::qmlAttachedProperties(object);
}

//  QQmlComponent *QQuickItemParticle::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK18QQuickItemParticle8delegateEv(
    const QQuickItemParticle *self) {
  return self->delegate();
}

//  void QQuickItemParticle::freeze(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle6freezeEP10QQuickItem(
    QQuickItemParticle *self,
    QQuickItem *item) {
  self->freeze(item);
}

//  void QQuickItemParticle::unfreeze(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle8unfreezeEP10QQuickItem(
    QQuickItemParticle *self,
    QQuickItem *item) {
  self->unfreeze(item);
}

//  void QQuickItemParticle::take(QQuickItem *item, bool prioritize)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle4takeEP10QQuickItemb(
    QQuickItemParticle *self,
    QQuickItem *item,
    bool prioritize) {
  self->take(item, prioritize);
}

//  void QQuickItemParticle::give(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle4giveEP10QQuickItem(
    QQuickItemParticle *self,
    QQuickItem *item) {
  self->give(item);
}

//  void QQuickItemParticle::setFade(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle7setFadeEb(
    QQuickItemParticle *self,
    bool arg) {
  self->setFade(arg);
}

//  void QQuickItemParticle::setDelegate(QQmlComponent *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle11setDelegateEP13QQmlComponent(
    QQuickItemParticle *self,
    QQmlComponent *arg) {
  self->setDelegate(arg);
}

//  void QQuickItemParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle5resetEv(QQuickItemParticle *self) {
  self->reset();
}

//  void QQuickItemParticle::commit(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle6commitEii(
    QQuickItemParticle *self,
    int gIdx,
    int pIdx) {
  self->commit(gIdx, pIdx);
}

//  void QQuickItemParticle::initialize(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle10initializeEii(
    QQuickItemParticle *self,
    int gIdx,
    int pIdx) {
  self->initialize(gIdx, pIdx);
}

//  void QQuickItemParticle::prepareNextFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle16prepareNextFrameEv(
    QQuickItemParticle *self) {
  self->prepareNextFrame();
}

//  bool QQuickItemParticle::clockShouldUpdate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickItemParticle17clockShouldUpdateEv(
    const QQuickItemParticle *self) {
  return self->clockShouldUpdate();
}

//  void QQuickItemParticle::updateClock()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle11updateClockEv(QQuickItemParticle *self) {
  self->updateClock();
}

//  void QQuickItemParticle::reconnectSystem(QQuickParticleSystem *system)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle15reconnectSystemEP20QQuickParticleSystem(
    QQuickItemParticle *self,
    QQuickParticleSystem *system) {
  self->reconnectSystem(system);
}

//  void QQuickItemParticle::reconnectParent(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle15reconnectParentEP10QQuickItem(
    QQuickItemParticle *self,
    QQuickItem *parent) {
  self->reconnectParent(parent);
}

//  void QQuickItemParticle::processDeletables()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle17processDeletablesEv(
    QQuickItemParticle *self) {
  self->processDeletables();
}

//  void QQuickItemParticle::tick(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemParticle4tickEi(
    QQuickItemParticle *self,
    int time) {
  self->tick(time);
}

//  a Python function taken by a CuteQQuickItemParticle, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemParticle(
    QQuickItemParticle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemParticle *>(self)->take(key, call);
}

//  QSGNode *QQuickItemParticle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN18QQuickItemParticle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickItemParticle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->QQuickItemParticle::updatePaintNode(a0, a1);
}

//  void QQuickItemParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickItemParticle5resetEv(QQuickItemParticle *self) {
  static_cast<OwnQQuickItemParticle *>(self)->OwnQQuickItemParticle::reset();
}

//  void QQuickItemParticle::commit(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickItemParticle6commitEii(
    QQuickItemParticle *self,
    int gIdx,
    int pIdx) {
  static_cast<OwnQQuickItemParticle *>(self)->OwnQQuickItemParticle::commit(
      gIdx,
      pIdx);
}

//  void QQuickItemParticle::initialize(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickItemParticle10initializeEii(
    QQuickItemParticle *self,
    int gIdx,
    int pIdx) {
  static_cast<OwnQQuickItemParticle *>(self)->OwnQQuickItemParticle::initialize(
      gIdx,
      pIdx);
}
