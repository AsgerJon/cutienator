//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickParticleSystem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickParticleSystem : QQuickParticleSystem {
  using QQuickParticleSystem::componentComplete;
};

//  A QQuickParticleSystem that Python can take functions over in. Every QQuickParticleSystem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickParticleSystemCall0)(const void *, int *);
typedef void (*CuteQQuickParticleSystemCall1)(const void *, int *);
typedef const QRectF * (*CuteQQuickParticleSystemCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickParticleSystemCall3)(const void *, int *);
typedef bool (*CuteQQuickParticleSystemCall4)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickParticleSystemCall5)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickParticleSystemCall6)(const void *, int *);
typedef void * (*CuteQQuickParticleSystemCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticleSystemCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleSystemCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickParticleSystemCall10)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickParticleSystemCall11)(const void *, int *);
typedef void (*CuteQQuickParticleSystemCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickParticleSystemCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickParticleSystemCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall21)(const void *, int *);
typedef void (*CuteQQuickParticleSystemCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickParticleSystemCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickParticleSystemCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickParticleSystemCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleSystemCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleSystemCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleSystemCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleSystemCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickParticleSystemCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickParticleSystemCall33)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickParticleSystemCall34)(const void *, int *);
typedef void (*CuteQQuickParticleSystemCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticleSystemCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleSystemCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleSystemCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleSystemCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleSystemCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleSystemCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickParticleSystem : public QQuickParticleSystem {
public:
  using QQuickParticleSystem::QQuickParticleSystem;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QQuickParticleSystem8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[35] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QQuickParticleSystem::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParticleSystemCall0 call = reinterpret_cast<CuteQQuickParticleSystemCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickParticleSystem::duration();
  }

  //  void QQuickParticleSystem::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParticleSystemCall1 call = reinterpret_cast<CuteQQuickParticleSystemCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticleSystem::componentComplete();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParticleSystemCall2 call = reinterpret_cast<CuteQQuickParticleSystemCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParticleSystemCall3 call = reinterpret_cast<CuteQQuickParticleSystemCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickParticleSystemCall4 call = reinterpret_cast<CuteQQuickParticleSystemCall4>(taken[4]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickParticleSystemCall5 call = reinterpret_cast<CuteQQuickParticleSystemCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickParticleSystemCall6 call = reinterpret_cast<CuteQQuickParticleSystemCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickParticleSystemCall7 call = reinterpret_cast<CuteQQuickParticleSystemCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickParticleSystemCall8 call = reinterpret_cast<CuteQQuickParticleSystemCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickParticleSystemCall9 call = reinterpret_cast<CuteQQuickParticleSystemCall9>(taken[9]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickParticleSystemCall10 call = reinterpret_cast<CuteQQuickParticleSystemCall10>(taken[10]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickParticleSystemCall11 call = reinterpret_cast<CuteQQuickParticleSystemCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickParticleSystemCall12 call = reinterpret_cast<CuteQQuickParticleSystemCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickParticleSystemCall13 call = reinterpret_cast<CuteQQuickParticleSystemCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickParticleSystemCall14 call = reinterpret_cast<CuteQQuickParticleSystemCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickParticleSystemCall15 call = reinterpret_cast<CuteQQuickParticleSystemCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickParticleSystemCall16 call = reinterpret_cast<CuteQQuickParticleSystemCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickParticleSystemCall17 call = reinterpret_cast<CuteQQuickParticleSystemCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickParticleSystemCall18 call = reinterpret_cast<CuteQQuickParticleSystemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickParticleSystemCall19 call = reinterpret_cast<CuteQQuickParticleSystemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickParticleSystemCall20 call = reinterpret_cast<CuteQQuickParticleSystemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickParticleSystemCall21 call = reinterpret_cast<CuteQQuickParticleSystemCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickParticleSystemCall22 call = reinterpret_cast<CuteQQuickParticleSystemCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickParticleSystemCall23 call = reinterpret_cast<CuteQQuickParticleSystemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickParticleSystemCall24 call = reinterpret_cast<CuteQQuickParticleSystemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickParticleSystemCall25 call = reinterpret_cast<CuteQQuickParticleSystemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickParticleSystemCall26 call = reinterpret_cast<CuteQQuickParticleSystemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickParticleSystemCall27 call = reinterpret_cast<CuteQQuickParticleSystemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickParticleSystemCall28 call = reinterpret_cast<CuteQQuickParticleSystemCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickParticleSystemCall29 call = reinterpret_cast<CuteQQuickParticleSystemCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickParticleSystemCall30 call = reinterpret_cast<CuteQQuickParticleSystemCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickParticleSystemCall31 call = reinterpret_cast<CuteQQuickParticleSystemCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickParticleSystemCall32 call = reinterpret_cast<CuteQQuickParticleSystemCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQQuickParticleSystemCall33 call = reinterpret_cast<CuteQQuickParticleSystemCall33>(taken[33]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickParticleSystemCall34 call = reinterpret_cast<CuteQQuickParticleSystemCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickParticleSystemCall35 call = reinterpret_cast<CuteQQuickParticleSystemCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickParticleSystemCall36 call = reinterpret_cast<CuteQQuickParticleSystemCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickParticleSystemCall37 call = reinterpret_cast<CuteQQuickParticleSystemCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickParticleSystemCall38 call = reinterpret_cast<CuteQQuickParticleSystemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickParticleSystemCall39 call = reinterpret_cast<CuteQQuickParticleSystemCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickParticleSystemCall40 call = reinterpret_cast<CuteQQuickParticleSystemCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickParticleSystemCall41 call = reinterpret_cast<CuteQQuickParticleSystemCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickParticleSystem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickParticleSystem10metaObjectEv(
    const QQuickParticleSystem *self) {
  return self->metaObject();
}

//  void *QQuickParticleSystem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickParticleSystem11qt_metacastEPKc(
    QQuickParticleSystem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickParticleSystem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickParticleSystem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickParticleSystem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickParticleSystem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickParticleSystem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParticleSystem::tr(s, c, n));
}

//  QQuickParticleSystem::QQuickParticleSystem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickParticleSystem *ritual_ZN20QQuickParticleSystemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickParticleSystem(parent);
}

//  QQuickParticleSystem::~QQuickParticleSystem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystemD1Ev(QQuickParticleSystem *self) {
  delete self;
}

//  bool QQuickParticleSystem::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickParticleSystem9isRunningEv(
    const QQuickParticleSystem *self) {
  return self->isRunning();
}

//  int QQuickParticleSystem::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickParticleSystem5countEv(
    const QQuickParticleSystem *self) {
  return self->count();
}

//  void QQuickParticleSystem::systemInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem17systemInitializedEv(
    QQuickParticleSystem *self) {
  self->systemInitialized();
}

//  void QQuickParticleSystem::runningChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem14runningChangedEb(
    QQuickParticleSystem *self,
    bool arg) {
  self->runningChanged(arg);
}

//  void QQuickParticleSystem::pausedChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem13pausedChangedEb(
    QQuickParticleSystem *self,
    bool arg) {
  self->pausedChanged(arg);
}

//  void QQuickParticleSystem::emptyChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem12emptyChangedEb(
    QQuickParticleSystem *self,
    bool arg) {
  self->emptyChanged(arg);
}

//  void QQuickParticleSystem::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem5startEv(QQuickParticleSystem *self) {
  self->start();
}

//  void QQuickParticleSystem::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem4stopEv(QQuickParticleSystem *self) {
  self->stop();
}

//  void QQuickParticleSystem::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem7restartEv(QQuickParticleSystem *self) {
  self->restart();
}

//  void QQuickParticleSystem::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem5pauseEv(QQuickParticleSystem *self) {
  self->pause();
}

//  void QQuickParticleSystem::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem6resumeEv(QQuickParticleSystem *self) {
  self->resume();
}

//  void QQuickParticleSystem::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem5resetEv(QQuickParticleSystem *self) {
  self->reset();
}

//  void QQuickParticleSystem::setRunning(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem10setRunningEb(
    QQuickParticleSystem *self,
    bool arg) {
  self->setRunning(arg);
}

//  void QQuickParticleSystem::setPaused(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem9setPausedEb(
    QQuickParticleSystem *self,
    bool arg) {
  self->setPaused(arg);
}

//  int QQuickParticleSystem::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickParticleSystem8durationEv(
    const QQuickParticleSystem *self) {
  return self->duration();
}

//  void QQuickParticleSystem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem17componentCompleteEv(
    QQuickParticleSystem *self) {
  self->componentComplete();
}

//  void QQuickParticleSystem::emittersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem15emittersChangedEv(
    QQuickParticleSystem *self) {
  self->emittersChanged();
}

//  void QQuickParticleSystem::loadPainter(QQuickParticlePainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem11loadPainterEP21QQuickParticlePainter(
    QQuickParticleSystem *self,
    QQuickParticlePainter *p) {
  self->loadPainter(p);
}

//  void QQuickParticleSystem::createEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem12createEngineEv(
    QQuickParticleSystem *self) {
  self->createEngine();
}

//  void QQuickParticleSystem::particleStateChange(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem19particleStateChangeEi(
    QQuickParticleSystem *self,
    int idx) {
  self->particleStateChange(idx);
}

//  void QQuickParticleSystem::emitParticle(QQuickParticleData *p,
//      QQuickParticleEmitter *particleEmitter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem12emitParticleEP18QQuickParticleDataP21QQuickParticleEmitter(
    QQuickParticleSystem *self,
    QQuickParticleData *p,
    QQuickParticleEmitter *particleEmitter) {
  self->emitParticle(p, particleEmitter);
}

//  QQuickParticleData *QQuickParticleSystem::newDatum(int groupId, bool
//      respectLimits, int sysIdx, const QQuickParticleData *cloneFrom)
extern "C" Q_DECL_EXPORT
QQuickParticleData *ritual_ZN20QQuickParticleSystem8newDatumEibiPK18QQuickParticleData(
    QQuickParticleSystem *self,
    int groupId,
    bool respectLimits,
    int sysIdx,
    const QQuickParticleData *cloneFrom) {
  return self->newDatum(groupId, respectLimits, sysIdx, cloneFrom);
}

//  void QQuickParticleSystem::finishNewDatum(QQuickParticleData *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem14finishNewDatumEP18QQuickParticleData(
    QQuickParticleSystem *self,
    QQuickParticleData *a0) {
  self->finishNewDatum(a0);
}

//  void QQuickParticleSystem::moveGroups(QQuickParticleData *d, int newGIdx)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem10moveGroupsEP18QQuickParticleDatai(
    QQuickParticleSystem *self,
    QQuickParticleData *d,
    int newGIdx) {
  self->moveGroups(d, newGIdx);
}

//  int QQuickParticleSystem::nextSystemIndex()
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickParticleSystem15nextSystemIndexEv(
    QQuickParticleSystem *self) {
  return self->nextSystemIndex();
}

//  int QQuickParticleSystem::systemSync(QQuickParticlePainter *p)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickParticleSystem10systemSyncEP21QQuickParticlePainter(
    QQuickParticleSystem *self,
    QQuickParticlePainter *p) {
  return self->systemSync(p);
}

//  int QQuickParticleSystem::registerParticleGroupData(const QString &name,
//      QQuickParticleGroupData *pgd)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickParticleSystem25registerParticleGroupDataERK7QStringP23QQuickParticleGroupData(
    QQuickParticleSystem *self,
    const QString *name,
    QQuickParticleGroupData *pgd) {
  return self->registerParticleGroupData(*name, pgd);
}

//  void QQuickParticleSystem::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem17updateCurrentTimeEi(
    QQuickParticleSystem *self,
    int currentTime) {
  self->updateCurrentTime(currentTime);
}

//  void QQuickParticleSystem::registerParticlePainter(QQuickParticlePainter
//      *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem23registerParticlePainterEP21QQuickParticlePainter(
    QQuickParticleSystem *self,
    QQuickParticlePainter *p) {
  self->registerParticlePainter(p);
}

//  void QQuickParticleSystem::registerParticleEmitter(QQuickParticleEmitter
//      *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem23registerParticleEmitterEP21QQuickParticleEmitter(
    QQuickParticleSystem *self,
    QQuickParticleEmitter *e) {
  self->registerParticleEmitter(e);
}

//  void QQuickParticleSystem::finishRegisteringParticleEmitter(QQuickParticl
//      eEmitter *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem32finishRegisteringParticleEmitterEP21QQuickParticleEmitter(
    QQuickParticleSystem *self,
    QQuickParticleEmitter *e) {
  self->finishRegisteringParticleEmitter(e);
}

//  void
//      QQuickParticleSystem::registerParticleAffector(QQuickParticleAffector
//      *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem24registerParticleAffectorEP22QQuickParticleAffector(
    QQuickParticleSystem *self,
    QQuickParticleAffector *a) {
  self->registerParticleAffector(a);
}

//  void QQuickParticleSystem::registerParticleGroup(QQuickParticleGroup *g)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem21registerParticleGroupEP19QQuickParticleGroup(
    QQuickParticleSystem *self,
    QQuickParticleGroup *g) {
  self->registerParticleGroup(g);
}

//  void
//      QQuickParticleSystem::unregisterParticlePainter(QQuickParticlePainter
//      *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem25unregisterParticlePainterEP21QQuickParticlePainter(
    QQuickParticleSystem *self,
    QQuickParticlePainter *p) {
  self->unregisterParticlePainter(p);
}

//  void
//      QQuickParticleSystem::unregisterParticleEmitter(QQuickParticleEmitter
//      *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem25unregisterParticleEmitterEP21QQuickParticleEmitter(
    QQuickParticleSystem *self,
    QQuickParticleEmitter *e) {
  self->unregisterParticleEmitter(e);
}

//  void
//      QQuickParticleSystem::unregisterParticleAffector(QQuickParticleAffect
//      or *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem26unregisterParticleAffectorEP22QQuickParticleAffector(
    QQuickParticleSystem *self,
    QQuickParticleAffector *a) {
  self->unregisterParticleAffector(a);
}

//  void
//      QQuickParticleSystem::statePropertyRedirect(QQmlListProperty<QObject>
//      *prop, QObject *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem21statePropertyRedirectEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *prop,
    QObject *value) {
  QQuickParticleSystem::statePropertyRedirect(prop, value);
}

//  void QQuickParticleSystem::stateRedirect(QQuickParticleGroup *group,
//      QQuickParticleSystem *sys, QObject *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem13stateRedirectEP19QQuickParticleGroupPS_P7QObject(
    QQuickParticleGroup *group,
    QQuickParticleSystem *sys,
    QObject *value) {
  QQuickParticleSystem::stateRedirect(group, sys, value);
}

//  bool QQuickParticleSystem::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickParticleSystem8isPausedEv(
    const QQuickParticleSystem *self) {
  return self->isPaused();
}

//  bool QQuickParticleSystem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickParticleSystem7isEmptyEv(
    const QQuickParticleSystem *self) {
  return self->isEmpty();
}

//  void QQuickParticleSystem::searchNextFreeGroupId()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem21searchNextFreeGroupIdEv(
    QQuickParticleSystem *self) {
  self->searchNextFreeGroupId();
}

//  void QQuickParticleSystem::emitterAdded(QQuickParticleEmitter *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem12emitterAddedEP21QQuickParticleEmitter(
    QQuickParticleSystem *self,
    QQuickParticleEmitter *e) {
  self->emitterAdded(e);
}

//  void QQuickParticleSystem::postProcessEmitters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem19postProcessEmittersEv(
    QQuickParticleSystem *self) {
  self->postProcessEmitters();
}

//  void QQuickParticleSystem::initGroups()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickParticleSystem10initGroupsEv(
    QQuickParticleSystem *self) {
  self->initGroups();
}

//  a Python function taken by a CuteQQuickParticleSystem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParticleSystem(
    QQuickParticleSystem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParticleSystem *>(self)->take(key, call);
}

//  int QQuickParticleSystem::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QQuickParticleSystem8durationEv(
    const QQuickParticleSystem *self) {
  return self->QQuickParticleSystem::duration();
}

//  void QQuickParticleSystem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickParticleSystem17componentCompleteEv(
    QQuickParticleSystem *self) {
  static_cast<OwnQQuickParticleSystem *>(self)->OwnQQuickParticleSystem::componentComplete();
}
