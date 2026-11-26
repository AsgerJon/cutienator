//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickimageparticle_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 3. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickimageparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuickImageParticle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickImageParticle : QQuickImageParticle {
  using QQuickImageParticle::reset;
  using QQuickImageParticle::initialize;
  using QQuickImageParticle::commit;
  using QQuickImageParticle::updatePaintNode;
  using QQuickImageParticle::sceneGraphInvalidated;
};

//  A QQuickImageParticle that Python can take functions over in. Every QQuickImageParticle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickImageParticleCall0)(const void *, int *);
typedef void (*CuteQQuickImageParticleCall1)(const void *, int, int, int *);
typedef void (*CuteQQuickImageParticleCall2)(const void *, int, int, int *);
typedef void * (*CuteQQuickImageParticleCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickImageParticleCall4)(const void *, int *);
typedef void (*CuteQQuickImageParticleCall5)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickImageParticleCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickImageParticleCall7)(const void *, int *);
typedef const QRectF * (*CuteQQuickImageParticleCall8)(const void *, int *);
typedef bool (*CuteQQuickImageParticleCall9)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickImageParticleCall10)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickImageParticleCall11)(const void *, int *);
typedef void * (*CuteQQuickImageParticleCall12)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageParticleCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageParticleCall14)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickImageParticleCall15)(const void *, int *);
typedef void (*CuteQQuickImageParticleCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickImageParticleCall17)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickImageParticleCall18)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickImageParticleCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickImageParticleCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickImageParticleCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageParticleCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageParticleCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageParticleCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickImageParticleCall25)(const void *, int *);
typedef void (*CuteQQuickImageParticleCall26)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickImageParticleCall27)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickImageParticleCall28)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickImageParticleCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickImageParticleCall30)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickImageParticleCall31)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageParticleCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageParticleCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageParticleCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickImageParticleCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickImageParticleCall36)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickImageParticleCall37)(const void *, int *);
typedef void (*CuteQQuickImageParticleCall38)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageParticleCall39)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageParticleCall40)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageParticleCall41)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageParticleCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageParticleCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageParticleCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImageParticle : public QQuickImageParticle {
public:
  using QQuickImageParticle::QQuickImageParticle;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter5resetEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter10initializeEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter6commitEii")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
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

  //  void QQuickImageParticle::reset()
  void reset() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageParticleCall0 call = reinterpret_cast<CuteQQuickImageParticleCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageParticle::reset();
  }

  //  void QQuickImageParticle::initialize(int gIdx, int pIdx)
  void initialize(int gIdx, int pIdx) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageParticleCall1 call = reinterpret_cast<CuteQQuickImageParticleCall1>(taken[1]);
      call(this, gIdx, pIdx, &handled);
      if (handled) return;
    }
    QQuickImageParticle::initialize(gIdx, pIdx);
  }

  //  void QQuickImageParticle::commit(int gIdx, int pIdx)
  void commit(int gIdx, int pIdx) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageParticleCall2 call = reinterpret_cast<CuteQQuickImageParticleCall2>(taken[2]);
      call(this, gIdx, pIdx, &handled);
      if (handled) return;
    }
    QQuickImageParticle::commit(gIdx, pIdx);
  }

  //  QSGNode *QQuickImageParticle::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageParticleCall3 call = reinterpret_cast<CuteQQuickImageParticleCall3>(taken[3]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickImageParticle::updatePaintNode(a0, a1);
  }

  //  void QQuickImageParticle::sceneGraphInvalidated()
  void sceneGraphInvalidated() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImageParticleCall4 call = reinterpret_cast<CuteQQuickImageParticleCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickImageParticle::sceneGraphInvalidated();
  }

  //  void QQuickParticlePainter::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImageParticleCall5 call = reinterpret_cast<CuteQQuickImageParticleCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::itemChange(a0, a1);
  }

  //  void QQuickParticlePainter::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImageParticleCall6 call = reinterpret_cast<CuteQQuickImageParticleCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::componentComplete();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickImageParticleCall7 call = reinterpret_cast<CuteQQuickImageParticleCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickImageParticleCall8 call = reinterpret_cast<CuteQQuickImageParticleCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickImageParticleCall9 call = reinterpret_cast<CuteQQuickImageParticleCall9>(taken[9]);
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
      CuteQQuickImageParticleCall10 call = reinterpret_cast<CuteQQuickImageParticleCall10>(taken[10]);
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
      CuteQQuickImageParticleCall11 call = reinterpret_cast<CuteQQuickImageParticleCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickImageParticleCall12 call = reinterpret_cast<CuteQQuickImageParticleCall12>(taken[12]);
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
      CuteQQuickImageParticleCall13 call = reinterpret_cast<CuteQQuickImageParticleCall13>(taken[13]);
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
      CuteQQuickImageParticleCall14 call = reinterpret_cast<CuteQQuickImageParticleCall14>(taken[14]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickImageParticleCall15 call = reinterpret_cast<CuteQQuickImageParticleCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickImageParticleCall16 call = reinterpret_cast<CuteQQuickImageParticleCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickImageParticleCall17 call = reinterpret_cast<CuteQQuickImageParticleCall17>(taken[17]);
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
      CuteQQuickImageParticleCall18 call = reinterpret_cast<CuteQQuickImageParticleCall18>(taken[18]);
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
      CuteQQuickImageParticleCall19 call = reinterpret_cast<CuteQQuickImageParticleCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickImageParticleCall20 call = reinterpret_cast<CuteQQuickImageParticleCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickImageParticleCall21 call = reinterpret_cast<CuteQQuickImageParticleCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickImageParticleCall22 call = reinterpret_cast<CuteQQuickImageParticleCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickImageParticleCall23 call = reinterpret_cast<CuteQQuickImageParticleCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickImageParticleCall24 call = reinterpret_cast<CuteQQuickImageParticleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickImageParticleCall25 call = reinterpret_cast<CuteQQuickImageParticleCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickImageParticleCall26 call = reinterpret_cast<CuteQQuickImageParticleCall26>(taken[26]);
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
      CuteQQuickImageParticleCall27 call = reinterpret_cast<CuteQQuickImageParticleCall27>(taken[27]);
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
      CuteQQuickImageParticleCall28 call = reinterpret_cast<CuteQQuickImageParticleCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickImageParticleCall29 call = reinterpret_cast<CuteQQuickImageParticleCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickImageParticleCall30 call = reinterpret_cast<CuteQQuickImageParticleCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickImageParticleCall31 call = reinterpret_cast<CuteQQuickImageParticleCall31>(taken[31]);
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
      CuteQQuickImageParticleCall32 call = reinterpret_cast<CuteQQuickImageParticleCall32>(taken[32]);
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
      CuteQQuickImageParticleCall33 call = reinterpret_cast<CuteQQuickImageParticleCall33>(taken[33]);
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
      CuteQQuickImageParticleCall34 call = reinterpret_cast<CuteQQuickImageParticleCall34>(taken[34]);
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
      CuteQQuickImageParticleCall35 call = reinterpret_cast<CuteQQuickImageParticleCall35>(taken[35]);
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
      CuteQQuickImageParticleCall36 call = reinterpret_cast<CuteQQuickImageParticleCall36>(taken[36]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickImageParticleCall37 call = reinterpret_cast<CuteQQuickImageParticleCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickImageParticleCall38 call = reinterpret_cast<CuteQQuickImageParticleCall38>(taken[38]);
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
      CuteQQuickImageParticleCall39 call = reinterpret_cast<CuteQQuickImageParticleCall39>(taken[39]);
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
      CuteQQuickImageParticleCall40 call = reinterpret_cast<CuteQQuickImageParticleCall40>(taken[40]);
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
      CuteQQuickImageParticleCall41 call = reinterpret_cast<CuteQQuickImageParticleCall41>(taken[41]);
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
      CuteQQuickImageParticleCall42 call = reinterpret_cast<CuteQQuickImageParticleCall42>(taken[42]);
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
      CuteQQuickImageParticleCall43 call = reinterpret_cast<CuteQQuickImageParticleCall43>(taken[43]);
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
      CuteQQuickImageParticleCall44 call = reinterpret_cast<CuteQQuickImageParticleCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickImageParticle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickImageParticle10metaObjectEv(
    const QQuickImageParticle *self) {
  return self->metaObject();
}

//  void *QQuickImageParticle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickImageParticle11qt_metacastEPKc(
    QQuickImageParticle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickImageParticle::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickImageParticle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickImageParticle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickImageParticle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickImageParticle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImageParticle::tr(s, c, n));
}

//  QQuickImageParticle::QQuickImageParticle(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickImageParticle *ritual_ZN19QQuickImageParticleC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickImageParticle(parent);
}

//  QQuickImageParticle::~QQuickImageParticle()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticleD1Ev(QQuickImageParticle *self) {
  delete self;
}

//  QQmlListProperty<QQuickSprite> QQuickImageParticle::sprites()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickSprite> *ritual_ZN19QQuickImageParticle7spritesEv(
    QQuickImageParticle *self) {
  return new QQmlListProperty<QQuickSprite>(self->sprites());
}

//  QQuickStochasticEngine *QQuickImageParticle::spriteEngine()
extern "C" Q_DECL_EXPORT
QQuickStochasticEngine *ritual_ZN19QQuickImageParticle12spriteEngineEv(
    QQuickImageParticle *self) {
  return self->spriteEngine();
}

//  QUrl QQuickImageParticle::image() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickImageParticle5imageEv(
    const QQuickImageParticle *self) {
  return new QUrl(self->image());
}

//  void QQuickImageParticle::setImage(const QUrl &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle8setImageERK4QUrl(
    QQuickImageParticle *self,
    const QUrl *image) {
  self->setImage(*image);
}

//  QUrl QQuickImageParticle::colortable() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickImageParticle10colortableEv(
    const QQuickImageParticle *self) {
  return new QUrl(self->colortable());
}

//  void QQuickImageParticle::setColortable(const QUrl &table)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13setColortableERK4QUrl(
    QQuickImageParticle *self,
    const QUrl *table) {
  self->setColortable(*table);
}

//  QUrl QQuickImageParticle::sizetable() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickImageParticle9sizetableEv(
    const QQuickImageParticle *self) {
  return new QUrl(self->sizetable());
}

//  void QQuickImageParticle::setSizetable(const QUrl &table)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle12setSizetableERK4QUrl(
    QQuickImageParticle *self,
    const QUrl *table) {
  self->setSizetable(*table);
}

//  QUrl QQuickImageParticle::opacitytable() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickImageParticle12opacitytableEv(
    const QQuickImageParticle *self) {
  return new QUrl(self->opacitytable());
}

//  void QQuickImageParticle::setOpacitytable(const QUrl &table)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle15setOpacitytableERK4QUrl(
    QQuickImageParticle *self,
    const QUrl *table) {
  self->setOpacitytable(*table);
}

//  QColor QQuickImageParticle::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickImageParticle5colorEv(
    const QQuickImageParticle *self) {
  return new QColor(self->color());
}

//  void QQuickImageParticle::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle8setColorERK6QColor(
    QQuickImageParticle *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QQuickImageParticle::colorVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle14colorVariationEv(
    const QQuickImageParticle *self) {
  return self->colorVariation();
}

//  void QQuickImageParticle::setColorVariation(qreal var)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle17setColorVariationEd(
    QQuickImageParticle *self,
    qreal var) {
  self->setColorVariation(var);
}

//  qreal QQuickImageParticle::alphaVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle14alphaVariationEv(
    const QQuickImageParticle *self) {
  return self->alphaVariation();
}

//  qreal QQuickImageParticle::alpha() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle5alphaEv(
    const QQuickImageParticle *self) {
  return self->alpha();
}

//  qreal QQuickImageParticle::redVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle12redVariationEv(
    const QQuickImageParticle *self) {
  return self->redVariation();
}

//  qreal QQuickImageParticle::greenVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle14greenVariationEv(
    const QQuickImageParticle *self) {
  return self->greenVariation();
}

//  qreal QQuickImageParticle::blueVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle13blueVariationEv(
    const QQuickImageParticle *self) {
  return self->blueVariation();
}

//  qreal QQuickImageParticle::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle8rotationEv(
    const QQuickImageParticle *self) {
  return self->rotation();
}

//  qreal QQuickImageParticle::rotationVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle17rotationVariationEv(
    const QQuickImageParticle *self) {
  return self->rotationVariation();
}

//  qreal QQuickImageParticle::rotationVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle16rotationVelocityEv(
    const QQuickImageParticle *self) {
  return self->rotationVelocity();
}

//  qreal QQuickImageParticle::rotationVelocityVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickImageParticle25rotationVelocityVariationEv(
    const QQuickImageParticle *self) {
  return self->rotationVelocityVariation();
}

//  bool QQuickImageParticle::autoRotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickImageParticle12autoRotationEv(
    const QQuickImageParticle *self) {
  return self->autoRotation();
}

//  QQuickDirection *QQuickImageParticle::xVector() const
extern "C" Q_DECL_EXPORT
QQuickDirection *ritual_ZNK19QQuickImageParticle7xVectorEv(
    const QQuickImageParticle *self) {
  return self->xVector();
}

//  QQuickDirection *QQuickImageParticle::yVector() const
extern "C" Q_DECL_EXPORT
QQuickDirection *ritual_ZNK19QQuickImageParticle7yVectorEv(
    const QQuickImageParticle *self) {
  return self->yVector();
}

//  bool QQuickImageParticle::spritesInterpolate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickImageParticle18spritesInterpolateEv(
    const QQuickImageParticle *self) {
  return self->spritesInterpolate();
}

//  bool QQuickImageParticle::bypassOptimizations() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickImageParticle19bypassOptimizationsEv(
    const QQuickImageParticle *self) {
  return self->bypassOptimizations();
}

//  EntryEffect QQuickImageParticle::entryEffect() const
extern "C" Q_DECL_EXPORT
QQuickImageParticle::EntryEffect ritual_ZNK19QQuickImageParticle11entryEffectEv(
    const QQuickImageParticle *self) {
  return self->entryEffect();
}

//  Status QQuickImageParticle::status() const
extern "C" Q_DECL_EXPORT
QQuickImageParticle::Status ritual_ZNK19QQuickImageParticle6statusEv(
    const QQuickImageParticle *self) {
  return self->status();
}

//  void QQuickImageParticle::resetColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle10resetColorEv(
    QQuickImageParticle *self) {
  self->resetColor();
}

//  void QQuickImageParticle::resetRotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13resetRotationEv(
    QQuickImageParticle *self) {
  self->resetRotation();
}

//  void QQuickImageParticle::resetDeformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle16resetDeformationEv(
    QQuickImageParticle *self) {
  self->resetDeformation();
}

//  void QQuickImageParticle::imageChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle12imageChangedEv(
    QQuickImageParticle *self) {
  self->imageChanged();
}

//  void QQuickImageParticle::colortableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle17colortableChangedEv(
    QQuickImageParticle *self) {
  self->colortableChanged();
}

//  void QQuickImageParticle::sizetableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle16sizetableChangedEv(
    QQuickImageParticle *self) {
  self->sizetableChanged();
}

//  void QQuickImageParticle::opacitytableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle19opacitytableChangedEv(
    QQuickImageParticle *self) {
  self->opacitytableChanged();
}

//  void QQuickImageParticle::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle12colorChangedEv(
    QQuickImageParticle *self) {
  self->colorChanged();
}

//  void QQuickImageParticle::colorVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle21colorVariationChangedEv(
    QQuickImageParticle *self) {
  self->colorVariationChanged();
}

//  void QQuickImageParticle::alphaVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle21alphaVariationChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->alphaVariationChanged(arg);
}

//  void QQuickImageParticle::alphaChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle12alphaChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->alphaChanged(arg);
}

//  void QQuickImageParticle::redVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle19redVariationChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->redVariationChanged(arg);
}

//  void QQuickImageParticle::greenVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle21greenVariationChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->greenVariationChanged(arg);
}

//  void QQuickImageParticle::blueVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle20blueVariationChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->blueVariationChanged(arg);
}

//  void QQuickImageParticle::rotationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle15rotationChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->rotationChanged(arg);
}

//  void QQuickImageParticle::rotationVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle24rotationVariationChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->rotationVariationChanged(arg);
}

//  void QQuickImageParticle::rotationVelocityChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle23rotationVelocityChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->rotationVelocityChanged(arg);
}

//  void QQuickImageParticle::rotationVelocityVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle32rotationVelocityVariationChangedEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->rotationVelocityVariationChanged(arg);
}

//  void QQuickImageParticle::autoRotationChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle19autoRotationChangedEb(
    QQuickImageParticle *self,
    bool arg) {
  self->autoRotationChanged(arg);
}

//  void QQuickImageParticle::xVectorChanged(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle14xVectorChangedEP15QQuickDirection(
    QQuickImageParticle *self,
    QQuickDirection *arg) {
  self->xVectorChanged(arg);
}

//  void QQuickImageParticle::yVectorChanged(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle14yVectorChangedEP15QQuickDirection(
    QQuickImageParticle *self,
    QQuickDirection *arg) {
  self->yVectorChanged(arg);
}

//  void QQuickImageParticle::spritesInterpolateChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle25spritesInterpolateChangedEb(
    QQuickImageParticle *self,
    bool arg) {
  self->spritesInterpolateChanged(arg);
}

//  void QQuickImageParticle::bypassOptimizationsChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle26bypassOptimizationsChangedEb(
    QQuickImageParticle *self,
    bool arg) {
  self->bypassOptimizationsChanged(arg);
}

//  void QQuickImageParticle::entryEffectChanged(EntryEffect arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle18entryEffectChangedENS_11EntryEffectE(
    QQuickImageParticle *self,
    QQuickImageParticle::EntryEffect arg) {
  self->entryEffectChanged(arg);
}

//  void QQuickImageParticle::statusChanged(Status arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13statusChangedENS_6StatusE(
    QQuickImageParticle *self,
    QQuickImageParticle::Status arg) {
  self->statusChanged(arg);
}

//  void QQuickImageParticle::setAlphaVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle17setAlphaVariationEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setAlphaVariation(arg);
}

//  void QQuickImageParticle::setAlpha(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle8setAlphaEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setAlpha(arg);
}

//  void QQuickImageParticle::setRedVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle15setRedVariationEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setRedVariation(arg);
}

//  void QQuickImageParticle::setGreenVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle17setGreenVariationEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setGreenVariation(arg);
}

//  void QQuickImageParticle::setBlueVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle16setBlueVariationEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setBlueVariation(arg);
}

//  void QQuickImageParticle::setRotation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle11setRotationEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setRotation(arg);
}

//  void QQuickImageParticle::setRotationVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle20setRotationVariationEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setRotationVariation(arg);
}

//  void QQuickImageParticle::setRotationVelocity(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle19setRotationVelocityEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setRotationVelocity(arg);
}

//  void QQuickImageParticle::setRotationVelocityVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle28setRotationVelocityVariationEd(
    QQuickImageParticle *self,
    qreal arg) {
  self->setRotationVelocityVariation(arg);
}

//  void QQuickImageParticle::setAutoRotation(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle15setAutoRotationEb(
    QQuickImageParticle *self,
    bool arg) {
  self->setAutoRotation(arg);
}

//  void QQuickImageParticle::setXVector(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle10setXVectorEP15QQuickDirection(
    QQuickImageParticle *self,
    QQuickDirection *arg) {
  self->setXVector(arg);
}

//  void QQuickImageParticle::setYVector(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle10setYVectorEP15QQuickDirection(
    QQuickImageParticle *self,
    QQuickDirection *arg) {
  self->setYVector(arg);
}

//  void QQuickImageParticle::setSpritesInterpolate(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle21setSpritesInterpolateEb(
    QQuickImageParticle *self,
    bool arg) {
  self->setSpritesInterpolate(arg);
}

//  void QQuickImageParticle::setBypassOptimizations(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle22setBypassOptimizationsEb(
    QQuickImageParticle *self,
    bool arg) {
  self->setBypassOptimizations(arg);
}

//  void QQuickImageParticle::setEntryEffect(EntryEffect arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle14setEntryEffectENS_11EntryEffectE(
    QQuickImageParticle *self,
    QQuickImageParticle::EntryEffect arg) {
  self->setEntryEffect(arg);
}

//  void QQuickImageParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle5resetEv(QQuickImageParticle *self) {
  self->reset();
}

//  void QQuickImageParticle::initialize(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle10initializeEii(
    QQuickImageParticle *self,
    int gIdx,
    int pIdx) {
  self->initialize(gIdx, pIdx);
}

//  void QQuickImageParticle::commit(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle6commitEii(
    QQuickImageParticle *self,
    int gIdx,
    int pIdx) {
  self->commit(gIdx, pIdx);
}

//  QSGNode *QQuickImageParticle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN19QQuickImageParticle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickImageParticle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  bool QQuickImageParticle::prepareNextFrame(QSGNode **a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickImageParticle16prepareNextFrameEPP7QSGNode(
    QQuickImageParticle *self,
    QSGNode **a0) {
  return self->prepareNextFrame(a0);
}

//  void QQuickImageParticle::buildParticleNodes(QSGNode **a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle18buildParticleNodesEPP7QSGNode(
    QQuickImageParticle *self,
    QSGNode **a0) {
  self->buildParticleNodes(a0);
}

//  void QQuickImageParticle::sceneGraphInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle21sceneGraphInvalidatedEv(
    QQuickImageParticle *self) {
  self->sceneGraphInvalidated();
}

//  void QQuickImageParticle::createEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle12createEngineEv(
    QQuickImageParticle *self) {
  self->createEngine();
}

//  void QQuickImageParticle::spriteAdvance(int spriteIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13spriteAdvanceEi(
    QQuickImageParticle *self,
    int spriteIndex) {
  self->spriteAdvance(spriteIndex);
}

//  void QQuickImageParticle::spritesUpdate(qreal time)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13spritesUpdateEd(
    QQuickImageParticle *self,
    qreal time) {
  self->spritesUpdate(time);
}

//  void QQuickImageParticle::mainThreadFetchImageData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle24mainThreadFetchImageDataEv(
    QQuickImageParticle *self) {
  self->mainThreadFetchImageData();
}

//  void QQuickImageParticle::invalidateSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle20invalidateSceneGraphEv(
    QQuickImageParticle *self) {
  self->invalidateSceneGraph();
}

//  bool QQuickImageParticle::loadingSomething()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickImageParticle16loadingSomethingEv(
    QQuickImageParticle *self) {
  return self->loadingSomething();
}

//  void QQuickImageParticle::finishBuildParticleNodes(QSGNode **n)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle24finishBuildParticleNodesEPP7QSGNode(
    QQuickImageParticle *self,
    QSGNode **n) {
  self->finishBuildParticleNodes(n);
}

//  void QQuickImageParticle::clearShadows()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle12clearShadowsEv(
    QQuickImageParticle *self) {
  self->clearShadows();
}

//  QQuickParticleData
//      *QQuickImageParticle::getShadowDatum(QQuickParticleData *datum)
extern "C" Q_DECL_EXPORT
QQuickParticleData *ritual_ZN19QQuickImageParticle14getShadowDatumEP18QQuickParticleData(
    QQuickImageParticle *self,
    QQuickParticleData *datum) {
  return self->getShadowDatum(datum);
}

//  void QQuickImageParticle::checkPerfLevel(PerformanceLevel level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle14checkPerfLevelENS_16PerformanceLevelE(
    QQuickImageParticle *self,
    QQuickImageParticle::PerformanceLevel level) {
  self->checkPerfLevel(level);
}

//  ImageMaterialData *QQuickImageParticle::getState(QSGMaterial *m)
extern "C" Q_DECL_EXPORT
ImageMaterialData *ritual_ZN19QQuickImageParticle8getStateEP11QSGMaterial(
    QQuickImageParticle *self,
    QSGMaterial *m) {
  return self->getState(m);
}

//  a Python function taken by a CuteQQuickImageParticle, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageParticle(
    QQuickImageParticle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageParticle *>(self)->take(key, call);
}

//  void QQuickImageParticle::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickImageParticle5resetEv(QQuickImageParticle *self) {
  static_cast<OwnQQuickImageParticle *>(self)->OwnQQuickImageParticle::reset();
}

//  void QQuickImageParticle::initialize(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickImageParticle10initializeEii(
    QQuickImageParticle *self,
    int gIdx,
    int pIdx) {
  static_cast<OwnQQuickImageParticle *>(self)->OwnQQuickImageParticle::initialize(
      gIdx,
      pIdx);
}

//  void QQuickImageParticle::commit(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickImageParticle6commitEii(
    QQuickImageParticle *self,
    int gIdx,
    int pIdx) {
  static_cast<OwnQQuickImageParticle *>(self)->OwnQQuickImageParticle::commit(
      gIdx,
      pIdx);
}

//  QSGNode *QQuickImageParticle::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN19QQuickImageParticle15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickImageParticle *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickImageParticle *>(self)->OwnQQuickImageParticle::updatePaintNode(
      a0,
      a1);
}

//  void QQuickImageParticle::sceneGraphInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickImageParticle21sceneGraphInvalidatedEv(
    QQuickImageParticle *self) {
  static_cast<OwnQQuickImageParticle *>(self)->OwnQQuickImageParticle::sceneGraphInvalidated();
}

//  a QQmlListProperty<QQuickSprite> a ritual of QQuickImageParticle gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickImageParticle__QQmlListProperty_QQuickSprite(
    QQmlListProperty<QQuickSprite> *self) {
  delete self;
}

//  void QQuickImageParticle::initTexCoords<SpriteVertex>(SpriteVertex *v,
//      int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13initTexCoordsI12SpriteVertexEEvPT_i(QQuickImageParticle *self, SpriteVertex *v, int count) {
  self->initTexCoords<SpriteVertex>(v, count);
}

//  void
//      QQuickImageParticle::initTexCoords<DeformableVertex>(DeformableVertex
//      *v, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13initTexCoordsI16DeformableVertexEEvPT_i(QQuickImageParticle *self, DeformableVertex *v, int count) {
  self->initTexCoords<DeformableVertex>(v, count);
}

//  void QQuickImageParticle::initTexCoords<ColoredVertex>(ColoredVertex *v,
//      int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageParticle13initTexCoordsI13ColoredVertexEEvPT_i(QQuickImageParticle *self, ColoredVertex *v, int count) {
  self->initTexCoords<ColoredVertex>(v, count);
}
