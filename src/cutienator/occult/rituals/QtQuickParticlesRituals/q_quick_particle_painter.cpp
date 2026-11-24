//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticlepainter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlepainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickParticlePainter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickParticlePainter : QQuickParticlePainter {
  using QQuickParticlePainter::reset;
  using QQuickParticlePainter::componentComplete;
  using QQuickParticlePainter::initialize;
  using QQuickParticlePainter::commit;
};

//  A QQuickParticlePainter that Python can take functions over in. Every QQuickParticlePainter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickParticlePainterCall0)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickParticlePainterCall1)(const void *, int *);
typedef void (*CuteQQuickParticlePainterCall2)(const void *, int *);
typedef void (*CuteQQuickParticlePainterCall3)(const void *, int *);
typedef void (*CuteQQuickParticlePainterCall4)(const void *, int, int, int *);
typedef void (*CuteQQuickParticlePainterCall5)(const void *, int, int, int *);
typedef const QRectF * (*CuteQQuickParticlePainterCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickParticlePainterCall7)(const void *, int *);
typedef bool (*CuteQQuickParticlePainterCall8)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickParticlePainterCall9)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickParticlePainterCall10)(const void *, int *);
typedef void * (*CuteQQuickParticlePainterCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticlePainterCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticlePainterCall13)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickParticlePainterCall14)(const void *, int *);
typedef void (*CuteQQuickParticlePainterCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall16)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickParticlePainterCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickParticlePainterCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall24)(const void *, int *);
typedef void (*CuteQQuickParticlePainterCall25)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickParticlePainterCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickParticlePainterCall27)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickParticlePainterCall30)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticlePainterCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticlePainterCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticlePainterCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticlePainterCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickParticlePainterCall35)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickParticlePainterCall36)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickParticlePainterCall37)(const void *, int *);
typedef void (*CuteQQuickParticlePainterCall38)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticlePainterCall39)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticlePainterCall40)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticlePainterCall41)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticlePainterCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticlePainterCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticlePainterCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickParticlePainter : public QQuickParticlePainter {
public:
  using QQuickParticlePainter::QQuickParticlePainter;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter5resetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter10initializeEii")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticlePainter6commitEii")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
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

  //  void QQuickParticlePainter::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParticlePainterCall0 call = reinterpret_cast<CuteQQuickParticlePainterCall0>(taken[0]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::itemChange(a0, a1);
  }

  //  void QQuickParticlePainter::sceneGraphInvalidated()
  void sceneGraphInvalidated() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParticlePainterCall1 call = reinterpret_cast<CuteQQuickParticlePainterCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::sceneGraphInvalidated();
  }

  //  void QQuickParticlePainter::reset()
  void reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParticlePainterCall2 call = reinterpret_cast<CuteQQuickParticlePainterCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::reset();
  }

  //  void QQuickParticlePainter::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParticlePainterCall3 call = reinterpret_cast<CuteQQuickParticlePainterCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::componentComplete();
  }

  //  void QQuickParticlePainter::initialize(int gIdx, int pIdx)
  void initialize(int gIdx, int pIdx) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickParticlePainterCall4 call = reinterpret_cast<CuteQQuickParticlePainterCall4>(taken[4]);
      call(this, gIdx, pIdx, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::initialize(gIdx, pIdx);
  }

  //  void QQuickParticlePainter::commit(int gIdx, int pIdx)
  void commit(int gIdx, int pIdx) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickParticlePainterCall5 call = reinterpret_cast<CuteQQuickParticlePainterCall5>(taken[5]);
      call(this, gIdx, pIdx, &handled);
      if (handled) return;
    }
    QQuickParticlePainter::commit(gIdx, pIdx);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickParticlePainterCall6 call = reinterpret_cast<CuteQQuickParticlePainterCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickParticlePainterCall7 call = reinterpret_cast<CuteQQuickParticlePainterCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickParticlePainterCall8 call = reinterpret_cast<CuteQQuickParticlePainterCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickParticlePainterCall9 call = reinterpret_cast<CuteQQuickParticlePainterCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickParticlePainterCall10 call = reinterpret_cast<CuteQQuickParticlePainterCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickParticlePainterCall11 call = reinterpret_cast<CuteQQuickParticlePainterCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickParticlePainterCall12 call = reinterpret_cast<CuteQQuickParticlePainterCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQQuickParticlePainterCall13 call = reinterpret_cast<CuteQQuickParticlePainterCall13>(taken[13]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickParticlePainterCall14 call = reinterpret_cast<CuteQQuickParticlePainterCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickParticlePainterCall15 call = reinterpret_cast<CuteQQuickParticlePainterCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickParticlePainterCall16 call = reinterpret_cast<CuteQQuickParticlePainterCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickParticlePainterCall17 call = reinterpret_cast<CuteQQuickParticlePainterCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickParticlePainterCall18 call = reinterpret_cast<CuteQQuickParticlePainterCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickParticlePainterCall19 call = reinterpret_cast<CuteQQuickParticlePainterCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickParticlePainterCall20 call = reinterpret_cast<CuteQQuickParticlePainterCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickParticlePainterCall21 call = reinterpret_cast<CuteQQuickParticlePainterCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickParticlePainterCall22 call = reinterpret_cast<CuteQQuickParticlePainterCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickParticlePainterCall23 call = reinterpret_cast<CuteQQuickParticlePainterCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickParticlePainterCall24 call = reinterpret_cast<CuteQQuickParticlePainterCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickParticlePainterCall25 call = reinterpret_cast<CuteQQuickParticlePainterCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickParticlePainterCall26 call = reinterpret_cast<CuteQQuickParticlePainterCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickParticlePainterCall27 call = reinterpret_cast<CuteQQuickParticlePainterCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickParticlePainterCall28 call = reinterpret_cast<CuteQQuickParticlePainterCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickParticlePainterCall29 call = reinterpret_cast<CuteQQuickParticlePainterCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickParticlePainterCall30 call = reinterpret_cast<CuteQQuickParticlePainterCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickParticlePainterCall31 call = reinterpret_cast<CuteQQuickParticlePainterCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickParticlePainterCall32 call = reinterpret_cast<CuteQQuickParticlePainterCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickParticlePainterCall33 call = reinterpret_cast<CuteQQuickParticlePainterCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickParticlePainterCall34 call = reinterpret_cast<CuteQQuickParticlePainterCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickParticlePainterCall35 call = reinterpret_cast<CuteQQuickParticlePainterCall35>(taken[35]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickParticlePainterCall36 call = reinterpret_cast<CuteQQuickParticlePainterCall36>(taken[36]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickParticlePainterCall37 call = reinterpret_cast<CuteQQuickParticlePainterCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickParticlePainterCall38 call = reinterpret_cast<CuteQQuickParticlePainterCall38>(taken[38]);
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
      CuteQQuickParticlePainterCall39 call = reinterpret_cast<CuteQQuickParticlePainterCall39>(taken[39]);
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
      CuteQQuickParticlePainterCall40 call = reinterpret_cast<CuteQQuickParticlePainterCall40>(taken[40]);
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
      CuteQQuickParticlePainterCall41 call = reinterpret_cast<CuteQQuickParticlePainterCall41>(taken[41]);
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
      CuteQQuickParticlePainterCall42 call = reinterpret_cast<CuteQQuickParticlePainterCall42>(taken[42]);
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
      CuteQQuickParticlePainterCall43 call = reinterpret_cast<CuteQQuickParticlePainterCall43>(taken[43]);
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
      CuteQQuickParticlePainterCall44 call = reinterpret_cast<CuteQQuickParticlePainterCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickParticlePainter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickParticlePainter10metaObjectEv(
    const QQuickParticlePainter *self) {
  return self->metaObject();
}

//  QString QQuickParticlePainter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickParticlePainter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParticlePainter::tr(s, c, n));
}

//  void QQuickParticlePainter::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter24qt_qmlMarker_uncreatableEv(
    QQuickParticlePainter *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickParticlePainter::QQuickParticlePainter(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickParticlePainter *ritual_ZN21QQuickParticlePainterC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickParticlePainter(parent);
}

//  QQuickParticlePainter::~QQuickParticlePainter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainterD1Ev(QQuickParticlePainter *self) {
  delete self;
}

//  void QQuickParticlePainter::load(QQuickParticleData *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter4loadEP18QQuickParticleData(
    QQuickParticlePainter *self,
    QQuickParticleData *a0) {
  self->load(a0);
}

//  void QQuickParticlePainter::reload(QQuickParticleData *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter6reloadEP18QQuickParticleData(
    QQuickParticlePainter *self,
    QQuickParticleData *a0) {
  self->reload(a0);
}

//  void QQuickParticlePainter::setCount(int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter8setCountEi(
    QQuickParticlePainter *self,
    int c) {
  self->setCount(c);
}

//  int QQuickParticlePainter::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickParticlePainter5countEv(
    const QQuickParticlePainter *self) {
  return self->count();
}

//  void QQuickParticlePainter::performPendingCommits()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter21performPendingCommitsEv(
    QQuickParticlePainter *self) {
  self->performPendingCommits();
}

//  QQuickParticleSystem *QQuickParticlePainter::system() const
extern "C" Q_DECL_EXPORT
QQuickParticleSystem *ritual_ZNK21QQuickParticlePainter6systemEv(
    const QQuickParticlePainter *self) {
  return self->system();
}

//  QStringList QQuickParticlePainter::groups() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QQuickParticlePainter6groupsEv(
    const QQuickParticlePainter *self) {
  return new QList<QString>(self->groups());
}

//  void QQuickParticlePainter::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickParticlePainter *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuickParticlePainter::setSystem(QQuickParticleSystem *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter9setSystemEP20QQuickParticleSystem(
    QQuickParticlePainter *self,
    QQuickParticleSystem *arg) {
  self->setSystem(arg);
}

//  void QQuickParticlePainter::setGroups(const QStringList &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter9setGroupsERK5QListI7QStringE(
    QQuickParticlePainter *self,
    const QList<QString> *arg) {
  self->setGroups(*arg);
}

//  void QQuickParticlePainter::calcSystemOffset(bool resetPending)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter16calcSystemOffsetEb(
    QQuickParticlePainter *self,
    bool resetPending) {
  self->calcSystemOffset(resetPending);
}

//  void QQuickParticlePainter::sceneGraphInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv(
    QQuickParticlePainter *self) {
  self->sceneGraphInvalidated();
}

//  void QQuickParticlePainter::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter5resetEv(QQuickParticlePainter *self) {
  self->reset();
}

//  void QQuickParticlePainter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter17componentCompleteEv(
    QQuickParticlePainter *self) {
  self->componentComplete();
}

//  void QQuickParticlePainter::initialize(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter10initializeEii(
    QQuickParticlePainter *self,
    int gIdx,
    int pIdx) {
  self->initialize(gIdx, pIdx);
}

//  void QQuickParticlePainter::commit(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticlePainter6commitEii(
    QQuickParticlePainter *self,
    int gIdx,
    int pIdx) {
  self->commit(gIdx, pIdx);
}

//  void QQuickParticlePainter::recalculateGroupIds() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickParticlePainter19recalculateGroupIdsEv(
    const QQuickParticlePainter *self) {
  self->recalculateGroupIds();
}

//  a Python function taken by a CuteQQuickParticlePainter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParticlePainter(
    QQuickParticlePainter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParticlePainter *>(self)->take(key, call);
}

//  void QQuickParticlePainter::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticlePainter10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickParticlePainter *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->QQuickParticlePainter::itemChange(a0, *a1);
}

//  void QQuickParticlePainter::sceneGraphInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticlePainter21sceneGraphInvalidatedEv(
    QQuickParticlePainter *self) {
  self->QQuickParticlePainter::sceneGraphInvalidated();
}

//  void QQuickParticlePainter::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticlePainter5resetEv(
    QQuickParticlePainter *self) {
  static_cast<OwnQQuickParticlePainter *>(self)->OwnQQuickParticlePainter::reset();
}

//  void QQuickParticlePainter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticlePainter17componentCompleteEv(
    QQuickParticlePainter *self) {
  static_cast<OwnQQuickParticlePainter *>(self)->OwnQQuickParticlePainter::componentComplete();
}

//  void QQuickParticlePainter::initialize(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticlePainter10initializeEii(
    QQuickParticlePainter *self,
    int gIdx,
    int pIdx) {
  static_cast<OwnQQuickParticlePainter *>(self)->OwnQQuickParticlePainter::initialize(
      gIdx,
      pIdx);
}

//  void QQuickParticlePainter::commit(int gIdx, int pIdx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticlePainter6commitEii(
    QQuickParticlePainter *self,
    int gIdx,
    int pIdx) {
  static_cast<OwnQQuickParticlePainter *>(self)->OwnQQuickParticlePainter::commit(
      gIdx,
      pIdx);
}
