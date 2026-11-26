//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickwander_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickwander_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWanderAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWanderAffector : QQuickWanderAffector {
  using QQuickWanderAffector::affectParticle;
};

//  A QQuickWanderAffector that Python can take functions over in. Every QQuickWanderAffector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickWanderAffectorCall0)(const void *, QQuickParticleData *, qreal, int *);
typedef void (*CuteQQuickWanderAffectorCall1)(const void *, qreal, int *);
typedef void (*CuteQQuickWanderAffectorCall2)(const void *, QQuickParticleData *, int *);
typedef void (*CuteQQuickWanderAffectorCall3)(const void *, int *);
typedef const QRectF * (*CuteQQuickWanderAffectorCall4)(const void *, int *);
typedef const QRectF * (*CuteQQuickWanderAffectorCall5)(const void *, int *);
typedef bool (*CuteQQuickWanderAffectorCall6)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickWanderAffectorCall7)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickWanderAffectorCall8)(const void *, int *);
typedef void * (*CuteQQuickWanderAffectorCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWanderAffectorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWanderAffectorCall11)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickWanderAffectorCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickWanderAffectorCall13)(const void *, int *);
typedef void (*CuteQQuickWanderAffectorCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickWanderAffectorCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickWanderAffectorCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall23)(const void *, int *);
typedef void (*CuteQQuickWanderAffectorCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWanderAffectorCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickWanderAffectorCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickWanderAffectorCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWanderAffectorCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWanderAffectorCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWanderAffectorCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickWanderAffectorCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickWanderAffectorCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickWanderAffectorCall35)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickWanderAffectorCall36)(const void *, int *);
typedef void (*CuteQQuickWanderAffectorCall37)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWanderAffectorCall38)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWanderAffectorCall39)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWanderAffectorCall40)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWanderAffectorCall41)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWanderAffectorCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWanderAffectorCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWanderAffector : public QQuickWanderAffector {
public:
  using QQuickWanderAffector::QQuickWanderAffector;
  void *taken[44] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickParticleAffector14affectParticleEP18QQuickParticleDatad")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickParticleAffector12affectSystemEd")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickParticleAffector5resetEP18QQuickParticleData")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
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

  //  bool QQuickWanderAffector::affectParticle(QQuickParticleData *d,
  //      qreal dt)
  bool affectParticle(QQuickParticleData *d, qreal dt) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall0 call = reinterpret_cast<CuteQQuickWanderAffectorCall0>(taken[0]);
      bool given = call(this, d, dt, &handled);
      if (handled) return given;
    }
    return QQuickWanderAffector::affectParticle(d, dt);
  }

  //  void QQuickParticleAffector::affectSystem(qreal dt)
  void affectSystem(qreal dt) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall1 call = reinterpret_cast<CuteQQuickWanderAffectorCall1>(taken[1]);
      call(this, dt, &handled);
      if (handled) return;
    }
    QQuickParticleAffector::affectSystem(dt);
  }

  //  void QQuickParticleAffector::reset(QQuickParticleData *a0)
  void reset(QQuickParticleData *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall2 call = reinterpret_cast<CuteQQuickWanderAffectorCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickParticleAffector::reset(a0);
  }

  //  void QQuickParticleAffector::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall3 call = reinterpret_cast<CuteQQuickWanderAffectorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticleAffector::componentComplete();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall4 call = reinterpret_cast<CuteQQuickWanderAffectorCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall5 call = reinterpret_cast<CuteQQuickWanderAffectorCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall6 call = reinterpret_cast<CuteQQuickWanderAffectorCall6>(taken[6]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall7 call = reinterpret_cast<CuteQQuickWanderAffectorCall7>(taken[7]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall8 call = reinterpret_cast<CuteQQuickWanderAffectorCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall9 call = reinterpret_cast<CuteQQuickWanderAffectorCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall10 call = reinterpret_cast<CuteQQuickWanderAffectorCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall11 call = reinterpret_cast<CuteQQuickWanderAffectorCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall12 call = reinterpret_cast<CuteQQuickWanderAffectorCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall13 call = reinterpret_cast<CuteQQuickWanderAffectorCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall14 call = reinterpret_cast<CuteQQuickWanderAffectorCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall15 call = reinterpret_cast<CuteQQuickWanderAffectorCall15>(taken[15]);
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
      CuteQQuickWanderAffectorCall16 call = reinterpret_cast<CuteQQuickWanderAffectorCall16>(taken[16]);
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
      CuteQQuickWanderAffectorCall17 call = reinterpret_cast<CuteQQuickWanderAffectorCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall18 call = reinterpret_cast<CuteQQuickWanderAffectorCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall19 call = reinterpret_cast<CuteQQuickWanderAffectorCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall20 call = reinterpret_cast<CuteQQuickWanderAffectorCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall21 call = reinterpret_cast<CuteQQuickWanderAffectorCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall22 call = reinterpret_cast<CuteQQuickWanderAffectorCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall23 call = reinterpret_cast<CuteQQuickWanderAffectorCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall24 call = reinterpret_cast<CuteQQuickWanderAffectorCall24>(taken[24]);
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
      CuteQQuickWanderAffectorCall25 call = reinterpret_cast<CuteQQuickWanderAffectorCall25>(taken[25]);
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
      CuteQQuickWanderAffectorCall26 call = reinterpret_cast<CuteQQuickWanderAffectorCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall27 call = reinterpret_cast<CuteQQuickWanderAffectorCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall28 call = reinterpret_cast<CuteQQuickWanderAffectorCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall29 call = reinterpret_cast<CuteQQuickWanderAffectorCall29>(taken[29]);
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
      CuteQQuickWanderAffectorCall30 call = reinterpret_cast<CuteQQuickWanderAffectorCall30>(taken[30]);
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
      CuteQQuickWanderAffectorCall31 call = reinterpret_cast<CuteQQuickWanderAffectorCall31>(taken[31]);
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
      CuteQQuickWanderAffectorCall32 call = reinterpret_cast<CuteQQuickWanderAffectorCall32>(taken[32]);
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
      CuteQQuickWanderAffectorCall33 call = reinterpret_cast<CuteQQuickWanderAffectorCall33>(taken[33]);
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
      CuteQQuickWanderAffectorCall34 call = reinterpret_cast<CuteQQuickWanderAffectorCall34>(taken[34]);
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
      CuteQQuickWanderAffectorCall35 call = reinterpret_cast<CuteQQuickWanderAffectorCall35>(taken[35]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall36 call = reinterpret_cast<CuteQQuickWanderAffectorCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickWanderAffectorCall37 call = reinterpret_cast<CuteQQuickWanderAffectorCall37>(taken[37]);
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
      CuteQQuickWanderAffectorCall38 call = reinterpret_cast<CuteQQuickWanderAffectorCall38>(taken[38]);
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
      CuteQQuickWanderAffectorCall39 call = reinterpret_cast<CuteQQuickWanderAffectorCall39>(taken[39]);
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
      CuteQQuickWanderAffectorCall40 call = reinterpret_cast<CuteQQuickWanderAffectorCall40>(taken[40]);
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
      CuteQQuickWanderAffectorCall41 call = reinterpret_cast<CuteQQuickWanderAffectorCall41>(taken[41]);
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
      CuteQQuickWanderAffectorCall42 call = reinterpret_cast<CuteQQuickWanderAffectorCall42>(taken[42]);
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
      CuteQQuickWanderAffectorCall43 call = reinterpret_cast<CuteQQuickWanderAffectorCall43>(taken[43]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWanderAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickWanderAffector10metaObjectEv(
    const QQuickWanderAffector *self) {
  return self->metaObject();
}

//  void *QQuickWanderAffector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickWanderAffector11qt_metacastEPKc(
    QQuickWanderAffector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWanderAffector::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickWanderAffector11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWanderAffector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWanderAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickWanderAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWanderAffector::tr(s, c, n));
}

//  QQuickWanderAffector::QQuickWanderAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickWanderAffector *ritual_ZN20QQuickWanderAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickWanderAffector(parent);
}

//  QQuickWanderAffector::~QQuickWanderAffector()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffectorD1Ev(QQuickWanderAffector *self) {
  delete self;
}

//  qreal QQuickWanderAffector::xVariance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickWanderAffector9xVarianceEv(
    const QQuickWanderAffector *self) {
  return self->xVariance();
}

//  qreal QQuickWanderAffector::yVariance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickWanderAffector9yVarianceEv(
    const QQuickWanderAffector *self) {
  return self->yVariance();
}

//  qreal QQuickWanderAffector::pace() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickWanderAffector4paceEv(
    const QQuickWanderAffector *self) {
  return self->pace();
}

//  AffectableParameters QQuickWanderAffector::affectedParameter() const
extern "C" Q_DECL_EXPORT
QQuickWanderAffector::AffectableParameters ritual_ZNK20QQuickWanderAffector17affectedParameterEv(
    const QQuickWanderAffector *self) {
  return self->affectedParameter();
}

//  bool QQuickWanderAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickWanderAffector14affectParticleEP18QQuickParticleDatad(
    QQuickWanderAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  void QQuickWanderAffector::xVarianceChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector16xVarianceChangedEd(
    QQuickWanderAffector *self,
    qreal arg) {
  self->xVarianceChanged(arg);
}

//  void QQuickWanderAffector::yVarianceChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector16yVarianceChangedEd(
    QQuickWanderAffector *self,
    qreal arg) {
  self->yVarianceChanged(arg);
}

//  void QQuickWanderAffector::paceChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector11paceChangedEd(
    QQuickWanderAffector *self,
    qreal arg) {
  self->paceChanged(arg);
}

//  void QQuickWanderAffector::affectedParameterChanged(AffectableParameters
//      arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector24affectedParameterChangedENS_20AffectableParametersE(
    QQuickWanderAffector *self,
    QQuickWanderAffector::AffectableParameters arg) {
  self->affectedParameterChanged(arg);
}

//  void QQuickWanderAffector::setXVariance(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector12setXVarianceEd(
    QQuickWanderAffector *self,
    qreal arg) {
  self->setXVariance(arg);
}

//  void QQuickWanderAffector::setYVariance(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector12setYVarianceEd(
    QQuickWanderAffector *self,
    qreal arg) {
  self->setYVariance(arg);
}

//  void QQuickWanderAffector::setPace(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector7setPaceEd(
    QQuickWanderAffector *self,
    qreal arg) {
  self->setPace(arg);
}

//  void QQuickWanderAffector::setAffectedParameter(AffectableParameters arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickWanderAffector20setAffectedParameterENS_20AffectableParametersE(
    QQuickWanderAffector *self,
    QQuickWanderAffector::AffectableParameters arg) {
  self->setAffectedParameter(arg);
}

//  WanderData *QQuickWanderAffector::getData(int idx)
extern "C" Q_DECL_EXPORT
WanderData *ritual_ZN20QQuickWanderAffector7getDataEi(
    QQuickWanderAffector *self,
    int idx) {
  return self->getData(idx);
}

//  a Python function taken by a CuteQQuickWanderAffector, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWanderAffector(
    QQuickWanderAffector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWanderAffector *>(self)->take(key, call);
}

//  bool QQuickWanderAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickWanderAffector14affectParticleEP18QQuickParticleDatad(
    QQuickWanderAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickWanderAffector *>(self)->OwnQQuickWanderAffector::affectParticle(
      d,
      dt);
}
