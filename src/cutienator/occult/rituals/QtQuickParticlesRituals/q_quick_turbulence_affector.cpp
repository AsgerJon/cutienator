//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickturbulence_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickturbulence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTurbulenceAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTurbulenceAffector : QQuickTurbulenceAffector {
  using QQuickTurbulenceAffector::geometryChange;
};

//  A QQuickTurbulenceAffector that Python can take functions over in. Every QQuickTurbulenceAffector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTurbulenceAffectorCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall2)(const void *, QQuickParticleData *, int *);
typedef bool (*CuteQQuickTurbulenceAffectorCall3)(const void *, QQuickParticleData *, qreal, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall4)(const void *, int *);
typedef const QRectF * (*CuteQQuickTurbulenceAffectorCall5)(const void *, int *);
typedef const QRectF * (*CuteQQuickTurbulenceAffectorCall6)(const void *, int *);
typedef bool (*CuteQQuickTurbulenceAffectorCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTurbulenceAffectorCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickTurbulenceAffectorCall9)(const void *, int *);
typedef void * (*CuteQQuickTurbulenceAffectorCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTurbulenceAffectorCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTurbulenceAffectorCall12)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall13)(const void *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTurbulenceAffectorCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTurbulenceAffectorCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall23)(const void *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTurbulenceAffectorCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTurbulenceAffectorCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTurbulenceAffectorCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTurbulenceAffectorCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTurbulenceAffectorCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTurbulenceAffectorCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickTurbulenceAffectorCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickTurbulenceAffectorCall35)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall36)(const void *, int *);
typedef void (*CuteQQuickTurbulenceAffectorCall37)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTurbulenceAffectorCall38)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTurbulenceAffectorCall39)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTurbulenceAffectorCall40)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTurbulenceAffectorCall41)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTurbulenceAffectorCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTurbulenceAffectorCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTurbulenceAffector : public QQuickTurbulenceAffector {
public:
  using QQuickTurbulenceAffector::QQuickTurbulenceAffector;
  void *taken[44] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickParticleAffector12affectSystemEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickParticleAffector5resetEP18QQuickParticleData")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickParticleAffector14affectParticleEP18QQuickParticleDatad")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[37] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickTurbulenceAffector::affectSystem(qreal dt)
  void affectSystem(qreal dt) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall0 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall0>(taken[0]);
      call(this, dt, &handled);
      if (handled) return;
    }
    QQuickTurbulenceAffector::affectSystem(dt);
  }

  //  void QQuickTurbulenceAffector::geometryChange(const QRectF
  //      &newGeometry, const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall1 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTurbulenceAffector::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickParticleAffector::reset(QQuickParticleData *a0)
  void reset(QQuickParticleData *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall2 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickParticleAffector::reset(a0);
  }

  //  bool QQuickParticleAffector::affectParticle(QQuickParticleData *d,
  //      qreal dt)
  bool affectParticle(QQuickParticleData *d, qreal dt) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall3 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall3>(taken[3]);
      bool given = call(this, d, dt, &handled);
      if (handled) return given;
    }
    return QQuickParticleAffector::affectParticle(d, dt);
  }

  //  void QQuickParticleAffector::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall4 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticleAffector::componentComplete();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall5 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall6 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall7 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall8 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall9 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall10 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall11 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall12 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall12>(taken[12]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall13 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall14 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall15 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall16 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall17 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall18 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall19 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall20 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall21 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall22 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall23 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall24 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall25 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall26 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall27 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall28 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall29 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall30 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall31 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall32 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall33 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall34 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall35 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall35>(taken[35]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall36 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall37 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall38 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall38>(taken[38]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall39 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall40 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall41 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall42 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickTurbulenceAffectorCall43 call = reinterpret_cast<CuteQQuickTurbulenceAffectorCall43>(taken[43]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTurbulenceAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickTurbulenceAffector10metaObjectEv(
    const QQuickTurbulenceAffector *self) {
  return self->metaObject();
}

//  QString QQuickTurbulenceAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickTurbulenceAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTurbulenceAffector::tr(s, c, n));
}

//  QQuickTurbulenceAffector::QQuickTurbulenceAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTurbulenceAffector *ritual_ZN24QQuickTurbulenceAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickTurbulenceAffector(parent);
}

//  QQuickTurbulenceAffector::~QQuickTurbulenceAffector()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTurbulenceAffectorD1Ev(
    QQuickTurbulenceAffector *self) {
  delete self;
}

//  void QQuickTurbulenceAffector::affectSystem(qreal dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTurbulenceAffector12affectSystemEd(
    QQuickTurbulenceAffector *self,
    qreal dt) {
  self->affectSystem(dt);
}

//  qreal QQuickTurbulenceAffector::strength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickTurbulenceAffector8strengthEv(
    const QQuickTurbulenceAffector *self) {
  return self->strength();
}

//  QUrl QQuickTurbulenceAffector::noiseSource() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QQuickTurbulenceAffector11noiseSourceEv(
    const QQuickTurbulenceAffector *self) {
  return new QUrl(self->noiseSource());
}

//  void QQuickTurbulenceAffector::setStrength(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTurbulenceAffector11setStrengthEd(
    QQuickTurbulenceAffector *self,
    qreal arg) {
  self->setStrength(arg);
}

//  void QQuickTurbulenceAffector::setNoiseSource(const QUrl &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTurbulenceAffector14setNoiseSourceERK4QUrl(
    QQuickTurbulenceAffector *self,
    const QUrl *arg) {
  self->setNoiseSource(*arg);
}

//  void QQuickTurbulenceAffector::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTurbulenceAffector14geometryChangeERK6QRectFS2_(
    QQuickTurbulenceAffector *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTurbulenceAffector::ensureInit()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTurbulenceAffector10ensureInitEv(
    QQuickTurbulenceAffector *self) {
  self->ensureInit();
}

//  void QQuickTurbulenceAffector::initializeGrid()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTurbulenceAffector14initializeGridEv(
    QQuickTurbulenceAffector *self) {
  self->initializeGrid();
}

//  qreal QQuickTurbulenceAffector::boundsRespectingField(int x, int y)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN24QQuickTurbulenceAffector21boundsRespectingFieldEii(
    QQuickTurbulenceAffector *self,
    int x,
    int y) {
  return self->boundsRespectingField(x, y);
}

//  a Python function taken by a CuteQQuickTurbulenceAffector, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTurbulenceAffector(
    QQuickTurbulenceAffector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTurbulenceAffector *>(self)->take(key, call);
}

//  void QQuickTurbulenceAffector::affectSystem(qreal dt)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickTurbulenceAffector12affectSystemEd(
    QQuickTurbulenceAffector *self,
    qreal dt) {
  self->QQuickTurbulenceAffector::affectSystem(dt);
}

//  void QQuickTurbulenceAffector::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickTurbulenceAffector14geometryChangeERK6QRectFS2_(
    QQuickTurbulenceAffector *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTurbulenceAffector *>(self)->OwnQQuickTurbulenceAffector::geometryChange(
      *newGeometry,
      *oldGeometry);
}
