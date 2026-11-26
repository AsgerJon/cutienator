//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticleemitter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticleemitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickv4particledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickParticleEmitter that Python can take functions over in. Every QQuickParticleEmitter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickParticleEmitterCall0)(const void *, int, int *);
typedef void (*CuteQQuickParticleEmitterCall1)(const void *, int *);
typedef void (*CuteQQuickParticleEmitterCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickParticleEmitterCall3)(const void *, int *);
typedef const QRectF * (*CuteQQuickParticleEmitterCall4)(const void *, int *);
typedef bool (*CuteQQuickParticleEmitterCall5)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickParticleEmitterCall6)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickParticleEmitterCall7)(const void *, int *);
typedef void * (*CuteQQuickParticleEmitterCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticleEmitterCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleEmitterCall10)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickParticleEmitterCall11)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickParticleEmitterCall12)(const void *, int *);
typedef void (*CuteQQuickParticleEmitterCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickParticleEmitterCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickParticleEmitterCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall22)(const void *, int *);
typedef void (*CuteQQuickParticleEmitterCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickParticleEmitterCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickParticleEmitterCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickParticleEmitterCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleEmitterCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleEmitterCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleEmitterCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickParticleEmitterCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickParticleEmitterCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickParticleEmitterCall34)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickParticleEmitterCall35)(const void *, int *);
typedef void (*CuteQQuickParticleEmitterCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticleEmitterCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleEmitterCall38)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleEmitterCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleEmitterCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleEmitterCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleEmitterCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickParticleEmitter : public QQuickParticleEmitter {
public:
  using QQuickParticleEmitter::QQuickParticleEmitter;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuickParticleEmitter10emitWindowEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickParticleEmitter5resetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[36] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickParticleEmitter::emitWindow(int timeStamp)
  void emitWindow(int timeStamp) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall0 call = reinterpret_cast<CuteQQuickParticleEmitterCall0>(taken[0]);
      call(this, timeStamp, &handled);
      if (handled) return;
    }
    QQuickParticleEmitter::emitWindow(timeStamp);
  }

  //  void QQuickParticleEmitter::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall1 call = reinterpret_cast<CuteQQuickParticleEmitterCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticleEmitter::componentComplete();
  }

  //  void QQuickParticleEmitter::reset()
  void reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall2 call = reinterpret_cast<CuteQQuickParticleEmitterCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickParticleEmitter::reset();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall3 call = reinterpret_cast<CuteQQuickParticleEmitterCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall4 call = reinterpret_cast<CuteQQuickParticleEmitterCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall5 call = reinterpret_cast<CuteQQuickParticleEmitterCall5>(taken[5]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall6 call = reinterpret_cast<CuteQQuickParticleEmitterCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall7 call = reinterpret_cast<CuteQQuickParticleEmitterCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall8 call = reinterpret_cast<CuteQQuickParticleEmitterCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall9 call = reinterpret_cast<CuteQQuickParticleEmitterCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall10 call = reinterpret_cast<CuteQQuickParticleEmitterCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall11 call = reinterpret_cast<CuteQQuickParticleEmitterCall11>(taken[11]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall12 call = reinterpret_cast<CuteQQuickParticleEmitterCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall13 call = reinterpret_cast<CuteQQuickParticleEmitterCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall14 call = reinterpret_cast<CuteQQuickParticleEmitterCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall15 call = reinterpret_cast<CuteQQuickParticleEmitterCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall16 call = reinterpret_cast<CuteQQuickParticleEmitterCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall17 call = reinterpret_cast<CuteQQuickParticleEmitterCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall18 call = reinterpret_cast<CuteQQuickParticleEmitterCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall19 call = reinterpret_cast<CuteQQuickParticleEmitterCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall20 call = reinterpret_cast<CuteQQuickParticleEmitterCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall21 call = reinterpret_cast<CuteQQuickParticleEmitterCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall22 call = reinterpret_cast<CuteQQuickParticleEmitterCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall23 call = reinterpret_cast<CuteQQuickParticleEmitterCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall24 call = reinterpret_cast<CuteQQuickParticleEmitterCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall25 call = reinterpret_cast<CuteQQuickParticleEmitterCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall26 call = reinterpret_cast<CuteQQuickParticleEmitterCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall27 call = reinterpret_cast<CuteQQuickParticleEmitterCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall28 call = reinterpret_cast<CuteQQuickParticleEmitterCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall29 call = reinterpret_cast<CuteQQuickParticleEmitterCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall30 call = reinterpret_cast<CuteQQuickParticleEmitterCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall31 call = reinterpret_cast<CuteQQuickParticleEmitterCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall32 call = reinterpret_cast<CuteQQuickParticleEmitterCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall33 call = reinterpret_cast<CuteQQuickParticleEmitterCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall34 call = reinterpret_cast<CuteQQuickParticleEmitterCall34>(taken[34]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall35 call = reinterpret_cast<CuteQQuickParticleEmitterCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall36 call = reinterpret_cast<CuteQQuickParticleEmitterCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall37 call = reinterpret_cast<CuteQQuickParticleEmitterCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall38 call = reinterpret_cast<CuteQQuickParticleEmitterCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall39 call = reinterpret_cast<CuteQQuickParticleEmitterCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall40 call = reinterpret_cast<CuteQQuickParticleEmitterCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall41 call = reinterpret_cast<CuteQQuickParticleEmitterCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickParticleEmitterCall42 call = reinterpret_cast<CuteQQuickParticleEmitterCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickParticleEmitter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickParticleEmitter10metaObjectEv(
    const QQuickParticleEmitter *self) {
  return self->metaObject();
}

//  void *QQuickParticleEmitter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickParticleEmitter11qt_metacastEPKc(
    QQuickParticleEmitter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickParticleEmitter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickParticleEmitter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickParticleEmitter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickParticleEmitter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickParticleEmitter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParticleEmitter::tr(s, c, n));
}

//  QQuickParticleEmitter::QQuickParticleEmitter(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickParticleEmitter *ritual_ZN21QQuickParticleEmitterC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickParticleEmitter(parent);
}

//  QQuickParticleEmitter::~QQuickParticleEmitter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitterD1Ev(QQuickParticleEmitter *self) {
  delete self;
}

//  void QQuickParticleEmitter::emitWindow(int timeStamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter10emitWindowEi(
    QQuickParticleEmitter *self,
    int timeStamp) {
  self->emitWindow(timeStamp);
}

//  bool QQuickParticleEmitter::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickParticleEmitter7enabledEv(
    const QQuickParticleEmitter *self) {
  return self->enabled();
}

//  qreal QQuickParticleEmitter::particlesPerSecond() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickParticleEmitter18particlesPerSecondEv(
    const QQuickParticleEmitter *self) {
  return self->particlesPerSecond();
}

//  int QQuickParticleEmitter::particleDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickParticleEmitter16particleDurationEv(
    const QQuickParticleEmitter *self) {
  return self->particleDuration();
}

//  QQuickParticleSystem *QQuickParticleEmitter::system() const
extern "C" Q_DECL_EXPORT
QQuickParticleSystem *ritual_ZNK21QQuickParticleEmitter6systemEv(
    const QQuickParticleEmitter *self) {
  return self->system();
}

//  QString QQuickParticleEmitter::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickParticleEmitter5groupEv(
    const QQuickParticleEmitter *self) {
  return new QString(self->group());
}

//  QQuickParticleGroupData::ID QQuickParticleEmitter::groupId() const
extern "C" Q_DECL_EXPORT
QQuickParticleGroupData::ID ritual_ZNK21QQuickParticleEmitter7groupIdEv(
    const QQuickParticleEmitter *self) {
  return self->groupId();
}

//  int QQuickParticleEmitter::particleDurationVariation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickParticleEmitter25particleDurationVariationEv(
    const QQuickParticleEmitter *self) {
  return self->particleDurationVariation();
}

//  qreal QQuickParticleEmitter::velocityFromMovement() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickParticleEmitter20velocityFromMovementEv(
    const QQuickParticleEmitter *self) {
  return self->velocityFromMovement();
}

//  void QQuickParticleEmitter::setVelocityFromMovement(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter23setVelocityFromMovementEd(
    QQuickParticleEmitter *self,
    qreal s) {
  self->setVelocityFromMovement(s);
}

//  void QQuickParticleEmitter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter17componentCompleteEv(
    QQuickParticleEmitter *self) {
  self->componentComplete();
}

//  void QQuickParticleEmitter::emitParticles(const
//      QList<QQuickV4ParticleData> &particles)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter13emitParticlesERK5QListI20QQuickV4ParticleDataE(
    QQuickParticleEmitter *self,
    const QList<QQuickV4ParticleData> *particles) {
  self->emitParticles(*particles);
}

//  void QQuickParticleEmitter::particlesPerSecondChanged(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter25particlesPerSecondChangedEd(
    QQuickParticleEmitter *self,
    qreal a0) {
  self->particlesPerSecondChanged(a0);
}

//  void QQuickParticleEmitter::particleDurationChanged(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter23particleDurationChangedEi(
    QQuickParticleEmitter *self,
    int a0) {
  self->particleDurationChanged(a0);
}

//  void QQuickParticleEmitter::enabledChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter14enabledChangedEb(
    QQuickParticleEmitter *self,
    bool a0) {
  self->enabledChanged(a0);
}

//  void QQuickParticleEmitter::systemChanged(QQuickParticleSystem *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter13systemChangedEP20QQuickParticleSystem(
    QQuickParticleEmitter *self,
    QQuickParticleSystem *arg) {
  self->systemChanged(arg);
}

//  void QQuickParticleEmitter::groupChanged(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter12groupChangedERK7QString(
    QQuickParticleEmitter *self,
    const QString *arg) {
  self->groupChanged(*arg);
}

//  void QQuickParticleEmitter::particleDurationVariationChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter32particleDurationVariationChangedEi(
    QQuickParticleEmitter *self,
    int arg) {
  self->particleDurationVariationChanged(arg);
}

//  void QQuickParticleEmitter::extruderChanged(QQuickParticleExtruder *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter15extruderChangedEP22QQuickParticleExtruder(
    QQuickParticleEmitter *self,
    QQuickParticleExtruder *arg) {
  self->extruderChanged(arg);
}

//  void QQuickParticleEmitter::particleSizeChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter19particleSizeChangedEd(
    QQuickParticleEmitter *self,
    qreal arg) {
  self->particleSizeChanged(arg);
}

//  void QQuickParticleEmitter::particleEndSizeChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter22particleEndSizeChangedEd(
    QQuickParticleEmitter *self,
    qreal arg) {
  self->particleEndSizeChanged(arg);
}

//  void QQuickParticleEmitter::particleSizeVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter28particleSizeVariationChangedEd(
    QQuickParticleEmitter *self,
    qreal arg) {
  self->particleSizeVariationChanged(arg);
}

//  void QQuickParticleEmitter::velocityChanged(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter15velocityChangedEP15QQuickDirection(
    QQuickParticleEmitter *self,
    QQuickDirection *arg) {
  self->velocityChanged(arg);
}

//  void QQuickParticleEmitter::accelerationChanged(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter19accelerationChangedEP15QQuickDirection(
    QQuickParticleEmitter *self,
    QQuickDirection *arg) {
  self->accelerationChanged(arg);
}

//  void QQuickParticleEmitter::maximumEmittedChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter21maximumEmittedChangedEi(
    QQuickParticleEmitter *self,
    int arg) {
  self->maximumEmittedChanged(arg);
}

//  void QQuickParticleEmitter::particleCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter20particleCountChangedEv(
    QQuickParticleEmitter *self) {
  self->particleCountChanged();
}

//  void QQuickParticleEmitter::velocityFromMovementChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter27velocityFromMovementChangedEv(
    QQuickParticleEmitter *self) {
  self->velocityFromMovementChanged();
}

//  void QQuickParticleEmitter::startTimeChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter16startTimeChangedEi(
    QQuickParticleEmitter *self,
    int arg) {
  self->startTimeChanged(arg);
}

//  void QQuickParticleEmitter::pulse(int milliseconds)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter5pulseEi(
    QQuickParticleEmitter *self,
    int milliseconds) {
  self->pulse(milliseconds);
}

//  void QQuickParticleEmitter::burst(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter5burstEi(
    QQuickParticleEmitter *self,
    int num) {
  self->burst(num);
}

//  void QQuickParticleEmitter::burst(int num, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter5burstEidd(
    QQuickParticleEmitter *self,
    int num,
    qreal x,
    qreal y) {
  self->burst(num, x, y);
}

//  void QQuickParticleEmitter::setEnabled(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter10setEnabledEb(
    QQuickParticleEmitter *self,
    bool arg) {
  self->setEnabled(arg);
}

//  void QQuickParticleEmitter::setParticlesPerSecond(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter21setParticlesPerSecondEd(
    QQuickParticleEmitter *self,
    qreal arg) {
  self->setParticlesPerSecond(arg);
}

//  void QQuickParticleEmitter::setParticleDuration(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter19setParticleDurationEi(
    QQuickParticleEmitter *self,
    int arg) {
  self->setParticleDuration(arg);
}

//  void QQuickParticleEmitter::setSystem(QQuickParticleSystem *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter9setSystemEP20QQuickParticleSystem(
    QQuickParticleEmitter *self,
    QQuickParticleSystem *arg) {
  self->setSystem(arg);
}

//  void QQuickParticleEmitter::setGroup(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter8setGroupERK7QString(
    QQuickParticleEmitter *self,
    const QString *arg) {
  self->setGroup(*arg);
}

//  void QQuickParticleEmitter::setParticleDurationVariation(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter28setParticleDurationVariationEi(
    QQuickParticleEmitter *self,
    int arg) {
  self->setParticleDurationVariation(arg);
}

//  void QQuickParticleEmitter::setExtruder(QQuickParticleExtruder *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter11setExtruderEP22QQuickParticleExtruder(
    QQuickParticleEmitter *self,
    QQuickParticleExtruder *arg) {
  self->setExtruder(arg);
}

//  void QQuickParticleEmitter::setParticleSize(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter15setParticleSizeEd(
    QQuickParticleEmitter *self,
    qreal arg) {
  self->setParticleSize(arg);
}

//  void QQuickParticleEmitter::setParticleEndSize(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter18setParticleEndSizeEd(
    QQuickParticleEmitter *self,
    qreal arg) {
  self->setParticleEndSize(arg);
}

//  void QQuickParticleEmitter::setParticleSizeVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter24setParticleSizeVariationEd(
    QQuickParticleEmitter *self,
    qreal arg) {
  self->setParticleSizeVariation(arg);
}

//  void QQuickParticleEmitter::setVelocity(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter11setVelocityEP15QQuickDirection(
    QQuickParticleEmitter *self,
    QQuickDirection *arg) {
  self->setVelocity(arg);
}

//  void QQuickParticleEmitter::setAcceleration(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter15setAccelerationEP15QQuickDirection(
    QQuickParticleEmitter *self,
    QQuickDirection *arg) {
  self->setAcceleration(arg);
}

//  void QQuickParticleEmitter::setMaxParticleCount(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter19setMaxParticleCountEi(
    QQuickParticleEmitter *self,
    int arg) {
  self->setMaxParticleCount(arg);
}

//  void QQuickParticleEmitter::setStartTime(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter12setStartTimeEi(
    QQuickParticleEmitter *self,
    int arg) {
  self->setStartTime(arg);
}

//  void QQuickParticleEmitter::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter5resetEv(QQuickParticleEmitter *self) {
  self->reset();
}

//  int QQuickParticleEmitter::particleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickParticleEmitter13particleCountEv(
    const QQuickParticleEmitter *self) {
  return self->particleCount();
}

//  QQuickParticleExtruder *QQuickParticleEmitter::extruder() const
extern "C" Q_DECL_EXPORT
QQuickParticleExtruder *ritual_ZNK21QQuickParticleEmitter8extruderEv(
    const QQuickParticleEmitter *self) {
  return self->extruder();
}

//  qreal QQuickParticleEmitter::particleSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickParticleEmitter12particleSizeEv(
    const QQuickParticleEmitter *self) {
  return self->particleSize();
}

//  qreal QQuickParticleEmitter::particleEndSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickParticleEmitter15particleEndSizeEv(
    const QQuickParticleEmitter *self) {
  return self->particleEndSize();
}

//  qreal QQuickParticleEmitter::particleSizeVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickParticleEmitter21particleSizeVariationEv(
    const QQuickParticleEmitter *self) {
  return self->particleSizeVariation();
}

//  QQuickDirection *QQuickParticleEmitter::velocity() const
extern "C" Q_DECL_EXPORT
QQuickDirection *ritual_ZNK21QQuickParticleEmitter8velocityEv(
    const QQuickParticleEmitter *self) {
  return self->velocity();
}

//  QQuickDirection *QQuickParticleEmitter::acceleration() const
extern "C" Q_DECL_EXPORT
QQuickDirection *ritual_ZNK21QQuickParticleEmitter12accelerationEv(
    const QQuickParticleEmitter *self) {
  return self->acceleration();
}

//  int QQuickParticleEmitter::maxParticleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickParticleEmitter16maxParticleCountEv(
    const QQuickParticleEmitter *self) {
  return self->maxParticleCount();
}

//  int QQuickParticleEmitter::startTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickParticleEmitter9startTimeEv(
    const QQuickParticleEmitter *self) {
  return self->startTime();
}

//  void QQuickParticleEmitter::reclaculateGroupId() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickParticleEmitter18reclaculateGroupIdEv(
    const QQuickParticleEmitter *self) {
  self->reclaculateGroupId();
}

//  QQuickParticleExtruder *QQuickParticleEmitter::effectiveExtruder()
extern "C" Q_DECL_EXPORT
QQuickParticleExtruder *ritual_ZN21QQuickParticleEmitter17effectiveExtruderEv(
    QQuickParticleEmitter *self) {
  return self->effectiveExtruder();
}

//  bool QQuickParticleEmitter::isEmitConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickParticleEmitter15isEmitConnectedEv(
    QQuickParticleEmitter *self) {
  return self->isEmitConnected();
}

//  void QQuickParticleEmitter::callSystemEmittersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickParticleEmitter25callSystemEmittersChangedEv(
    QQuickParticleEmitter *self) {
  self->callSystemEmittersChanged();
}

//  a Python function taken by a CuteQQuickParticleEmitter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParticleEmitter(
    QQuickParticleEmitter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParticleEmitter *>(self)->take(key, call);
}

//  void QQuickParticleEmitter::emitWindow(int timeStamp)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticleEmitter10emitWindowEi(
    QQuickParticleEmitter *self,
    int timeStamp) {
  self->QQuickParticleEmitter::emitWindow(timeStamp);
}

//  void QQuickParticleEmitter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticleEmitter17componentCompleteEv(
    QQuickParticleEmitter *self) {
  self->QQuickParticleEmitter::componentComplete();
}

//  void QQuickParticleEmitter::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickParticleEmitter5resetEv(
    QQuickParticleEmitter *self) {
  self->QQuickParticleEmitter::reset();
}
