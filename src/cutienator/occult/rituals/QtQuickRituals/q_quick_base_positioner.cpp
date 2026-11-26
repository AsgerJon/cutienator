//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickBasePositioner may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickBasePositioner : QQuickBasePositioner {
  using QQuickBasePositioner::componentComplete;
  using QQuickBasePositioner::itemChange;
  using QQuickBasePositioner::updatePolish;
};

//  A QQuickBasePositioner that Python can take functions over in. Every QQuickBasePositioner
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerCall1)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerCall3)(const void *, QSizeF *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_positioners)
typedef const QRectF * (*CuteQQuickBasePositionerCall5)(const void *, int *);
typedef const QRectF * (*CuteQQuickBasePositionerCall6)(const void *, int *);
typedef bool (*CuteQQuickBasePositionerCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickBasePositionerCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickBasePositionerCall9)(const void *, int *);
typedef void * (*CuteQQuickBasePositionerCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBasePositionerCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBasePositionerCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickBasePositionerCall13)(const void *, int *);
typedef void (*CuteQQuickBasePositionerCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickBasePositionerCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickBasePositionerCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall23)(const void *, int *);
typedef void (*CuteQQuickBasePositionerCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickBasePositionerCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickBasePositionerCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickBasePositionerCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBasePositionerCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBasePositionerCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBasePositionerCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickBasePositionerCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickBasePositionerCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickBasePositionerCall35)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickBasePositionerCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickBasePositionerCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBasePositionerCall38)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBasePositionerCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBasePositionerCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBasePositionerCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickBasePositionerCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickBasePositioner : public QQuickBasePositioner {
public:
  using QQuickBasePositioner::QQuickBasePositioner;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN20QQuickBasePositioner13doPositioningEP6QSizeF")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN20QQuickBasePositioner24reportConflictingAnchorsEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
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

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositioner::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBasePositionerCall0 call = reinterpret_cast<CuteQQuickBasePositionerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBasePositioner::componentComplete();
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositioner::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBasePositionerCall1 call = reinterpret_cast<CuteQQuickBasePositionerCall1>(taken[1]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickBasePositioner::itemChange(a0, a1);
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositioner::updatePolish()
  void updatePolish() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickBasePositionerCall2 call = reinterpret_cast<CuteQQuickBasePositionerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBasePositioner::updatePolish();
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositioner::doPositioning(QSizeF *contentSize)
  void doPositioning(QSizeF *contentSize) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickBasePositionerCall3 call = reinterpret_cast<CuteQQuickBasePositionerCall3>(taken[3]);
      call(this, contentSize, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositioner::reportConflictingAnchors()
  void reportConflictingAnchors() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickBasePositionerCall4 call = reinterpret_cast<CuteQQuickBasePositionerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_positioners)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickBasePositionerCall5 call = reinterpret_cast<CuteQQuickBasePositionerCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickBasePositionerCall6 call = reinterpret_cast<CuteQQuickBasePositionerCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickBasePositionerCall7 call = reinterpret_cast<CuteQQuickBasePositionerCall7>(taken[7]);
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
      CuteQQuickBasePositionerCall8 call = reinterpret_cast<CuteQQuickBasePositionerCall8>(taken[8]);
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
      CuteQQuickBasePositionerCall9 call = reinterpret_cast<CuteQQuickBasePositionerCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickBasePositionerCall10 call = reinterpret_cast<CuteQQuickBasePositionerCall10>(taken[10]);
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
      CuteQQuickBasePositionerCall11 call = reinterpret_cast<CuteQQuickBasePositionerCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQQuickBasePositionerCall12 call = reinterpret_cast<CuteQQuickBasePositionerCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickBasePositionerCall13 call = reinterpret_cast<CuteQQuickBasePositionerCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickBasePositionerCall14 call = reinterpret_cast<CuteQQuickBasePositionerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickBasePositionerCall15 call = reinterpret_cast<CuteQQuickBasePositionerCall15>(taken[15]);
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
      CuteQQuickBasePositionerCall16 call = reinterpret_cast<CuteQQuickBasePositionerCall16>(taken[16]);
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
      CuteQQuickBasePositionerCall17 call = reinterpret_cast<CuteQQuickBasePositionerCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickBasePositionerCall18 call = reinterpret_cast<CuteQQuickBasePositionerCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickBasePositionerCall19 call = reinterpret_cast<CuteQQuickBasePositionerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickBasePositionerCall20 call = reinterpret_cast<CuteQQuickBasePositionerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickBasePositionerCall21 call = reinterpret_cast<CuteQQuickBasePositionerCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickBasePositionerCall22 call = reinterpret_cast<CuteQQuickBasePositionerCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickBasePositionerCall23 call = reinterpret_cast<CuteQQuickBasePositionerCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickBasePositionerCall24 call = reinterpret_cast<CuteQQuickBasePositionerCall24>(taken[24]);
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
      CuteQQuickBasePositionerCall25 call = reinterpret_cast<CuteQQuickBasePositionerCall25>(taken[25]);
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
      CuteQQuickBasePositionerCall26 call = reinterpret_cast<CuteQQuickBasePositionerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickBasePositionerCall27 call = reinterpret_cast<CuteQQuickBasePositionerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickBasePositionerCall28 call = reinterpret_cast<CuteQQuickBasePositionerCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickBasePositionerCall29 call = reinterpret_cast<CuteQQuickBasePositionerCall29>(taken[29]);
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
      CuteQQuickBasePositionerCall30 call = reinterpret_cast<CuteQQuickBasePositionerCall30>(taken[30]);
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
      CuteQQuickBasePositionerCall31 call = reinterpret_cast<CuteQQuickBasePositionerCall31>(taken[31]);
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
      CuteQQuickBasePositionerCall32 call = reinterpret_cast<CuteQQuickBasePositionerCall32>(taken[32]);
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
      CuteQQuickBasePositionerCall33 call = reinterpret_cast<CuteQQuickBasePositionerCall33>(taken[33]);
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
      CuteQQuickBasePositionerCall34 call = reinterpret_cast<CuteQQuickBasePositionerCall34>(taken[34]);
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
      CuteQQuickBasePositionerCall35 call = reinterpret_cast<CuteQQuickBasePositionerCall35>(taken[35]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickBasePositionerCall36 call = reinterpret_cast<CuteQQuickBasePositionerCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickBasePositionerCall37 call = reinterpret_cast<CuteQQuickBasePositionerCall37>(taken[37]);
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
      CuteQQuickBasePositionerCall38 call = reinterpret_cast<CuteQQuickBasePositionerCall38>(taken[38]);
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
      CuteQQuickBasePositionerCall39 call = reinterpret_cast<CuteQQuickBasePositionerCall39>(taken[39]);
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
      CuteQQuickBasePositionerCall40 call = reinterpret_cast<CuteQQuickBasePositionerCall40>(taken[40]);
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
      CuteQQuickBasePositionerCall41 call = reinterpret_cast<CuteQQuickBasePositionerCall41>(taken[41]);
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
      CuteQQuickBasePositionerCall42 call = reinterpret_cast<CuteQQuickBasePositionerCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickBasePositioner::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickBasePositioner10metaObjectEv(
    const QQuickBasePositioner *self) {
  return self->metaObject();
}

//  void *QQuickBasePositioner::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickBasePositioner11qt_metacastEPKc(
    QQuickBasePositioner *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBasePositioner::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickBasePositioner11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBasePositioner *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickBasePositioner::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickBasePositioner2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickBasePositioner::tr(s, c, n));
}

//  void QQuickBasePositioner::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner24qt_qmlMarker_uncreatableEv(
    QQuickBasePositioner *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickBasePositioner::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner21qt_qmlMarker_attachedEv(
    QQuickBasePositioner *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickBasePositioner::QQuickBasePositioner(PositionerType a0, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickBasePositioner *ritual_ZN20QQuickBasePositionerC1ENS_14PositionerTypeEP10QQuickItem(
    QQuickBasePositioner::PositionerType a0,
    QQuickItem *parent) {
  return new CuteQQuickBasePositioner(a0, parent);
}

//  QQuickBasePositioner::~QQuickBasePositioner()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositionerD1Ev(QQuickBasePositioner *self) {
  delete self;
}

//  qreal QQuickBasePositioner::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickBasePositioner7spacingEv(
    const QQuickBasePositioner *self) {
  return self->spacing();
}

//  void QQuickBasePositioner::setSpacing(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner10setSpacingEd(
    QQuickBasePositioner *self,
    qreal a0) {
  self->setSpacing(a0);
}

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickBasePositioner::populate() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK20QQuickBasePositioner8populateEv(
    const QQuickBasePositioner *self) {
  return self->populate();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickBasePositioner::setPopulate(QQuickTransition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner11setPopulateEP16QQuickTransition(
    QQuickBasePositioner *self,
    QQuickTransition *a0) {
  self->setPopulate(a0);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickBasePositioner::move() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK20QQuickBasePositioner4moveEv(
    const QQuickBasePositioner *self) {
  return self->move();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickBasePositioner::setMove(QQuickTransition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner7setMoveEP16QQuickTransition(
    QQuickBasePositioner *self,
    QQuickTransition *a0) {
  self->setMove(a0);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  QQuickTransition *QQuickBasePositioner::add() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK20QQuickBasePositioner3addEv(
    const QQuickBasePositioner *self) {
  return self->add();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickBasePositioner::setAdd(QQuickTransition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner6setAddEP16QQuickTransition(
    QQuickBasePositioner *self,
    QQuickTransition *a0) {
  self->setAdd(a0);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  QQuickPositionerAttached
//      *QQuickBasePositioner::qmlAttachedProperties(QObject *obj)
extern "C" Q_DECL_EXPORT
QQuickPositionerAttached *ritual_ZN20QQuickBasePositioner21qmlAttachedPropertiesEP7QObject(
    QObject *obj) {
  return QQuickBasePositioner::qmlAttachedProperties(obj);
}

//  void
//      QQuickBasePositioner::updateAttachedProperties(QQuickPositionerAttach
//      ed *specificProperty, QQuickItem *specificPropertyOwner) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QQuickBasePositioner24updateAttachedPropertiesEP24QQuickPositionerAttachedP10QQuickItem(
    const QQuickBasePositioner *self,
    QQuickPositionerAttached *specificProperty,
    QQuickItem *specificPropertyOwner) {
  self->updateAttachedProperties(specificProperty, specificPropertyOwner);
}

//  qreal QQuickBasePositioner::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickBasePositioner7paddingEv(
    const QQuickBasePositioner *self) {
  return self->padding();
}

//  void QQuickBasePositioner::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner10setPaddingEd(
    QQuickBasePositioner *self,
    qreal padding) {
  self->setPadding(padding);
}

//  void QQuickBasePositioner::resetPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner12resetPaddingEv(
    QQuickBasePositioner *self) {
  self->resetPadding();
}

//  qreal QQuickBasePositioner::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickBasePositioner10topPaddingEv(
    const QQuickBasePositioner *self) {
  return self->topPadding();
}

//  void QQuickBasePositioner::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner13setTopPaddingEd(
    QQuickBasePositioner *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickBasePositioner::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner15resetTopPaddingEv(
    QQuickBasePositioner *self) {
  self->resetTopPadding();
}

//  qreal QQuickBasePositioner::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickBasePositioner11leftPaddingEv(
    const QQuickBasePositioner *self) {
  return self->leftPadding();
}

//  void QQuickBasePositioner::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner14setLeftPaddingEd(
    QQuickBasePositioner *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickBasePositioner::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner16resetLeftPaddingEv(
    QQuickBasePositioner *self) {
  self->resetLeftPadding();
}

//  qreal QQuickBasePositioner::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickBasePositioner12rightPaddingEv(
    const QQuickBasePositioner *self) {
  return self->rightPadding();
}

//  void QQuickBasePositioner::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner15setRightPaddingEd(
    QQuickBasePositioner *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickBasePositioner::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner17resetRightPaddingEv(
    QQuickBasePositioner *self) {
  self->resetRightPadding();
}

//  qreal QQuickBasePositioner::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickBasePositioner13bottomPaddingEv(
    const QQuickBasePositioner *self) {
  return self->bottomPadding();
}

//  void QQuickBasePositioner::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner16setBottomPaddingEd(
    QQuickBasePositioner *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickBasePositioner::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner18resetBottomPaddingEv(
    QQuickBasePositioner *self) {
  self->resetBottomPadding();
}

//  void QQuickBasePositioner::forceLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner11forceLayoutEv(
    QQuickBasePositioner *self) {
  self->forceLayout();
}

//  QQuickBasePositioner::QQuickBasePositioner(QQuickBasePositionerPrivate
//      &dd, PositionerType at, QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickBasePositioner *ritual_ZN20QQuickBasePositionerC1ER27QQuickBasePositionerPrivateNS_14PositionerTypeEP10QQuickItem(
    QQuickBasePositionerPrivate *dd,
    QQuickBasePositioner::PositionerType at,
    QQuickItem *parent) {
  return new CuteQQuickBasePositioner(*dd, at, parent);
}

//  void QQuickBasePositioner::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner17componentCompleteEv(
    QQuickBasePositioner *self) {
  self->componentComplete();
}

//  void QQuickBasePositioner::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickBasePositioner *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuickBasePositioner::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner12updatePolishEv(
    QQuickBasePositioner *self) {
  self->updatePolish();
}

//  void QQuickBasePositioner::spacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner14spacingChangedEv(
    QQuickBasePositioner *self) {
  self->spacingChanged();
}

//  void QQuickBasePositioner::populateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner15populateChangedEv(
    QQuickBasePositioner *self) {
  self->populateChanged();
}

//  void QQuickBasePositioner::moveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner11moveChangedEv(
    QQuickBasePositioner *self) {
  self->moveChanged();
}

//  void QQuickBasePositioner::addChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner10addChangedEv(
    QQuickBasePositioner *self) {
  self->addChanged();
}

//  void QQuickBasePositioner::paddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner14paddingChangedEv(
    QQuickBasePositioner *self) {
  self->paddingChanged();
}

//  void QQuickBasePositioner::topPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner17topPaddingChangedEv(
    QQuickBasePositioner *self) {
  self->topPaddingChanged();
}

//  void QQuickBasePositioner::leftPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner18leftPaddingChangedEv(
    QQuickBasePositioner *self) {
  self->leftPaddingChanged();
}

//  void QQuickBasePositioner::rightPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner19rightPaddingChangedEv(
    QQuickBasePositioner *self) {
  self->rightPaddingChanged();
}

//  void QQuickBasePositioner::bottomPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner20bottomPaddingChangedEv(
    QQuickBasePositioner *self) {
  self->bottomPaddingChanged();
}

//  void QQuickBasePositioner::positioningComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner19positioningCompleteEv(
    QQuickBasePositioner *self) {
  self->positioningComplete();
}

//  void QQuickBasePositioner::prePositioning()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner14prePositioningEv(
    QQuickBasePositioner *self) {
  self->prePositioning();
}

//  void QQuickBasePositioner::doPositioning(QSizeF *contentSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner13doPositioningEP6QSizeF(
    QQuickBasePositioner *self,
    QSizeF *contentSize) {
  self->doPositioning(contentSize);
}

//  void QQuickBasePositioner::reportConflictingAnchors()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner24reportConflictingAnchorsEv(
    QQuickBasePositioner *self) {
  self->reportConflictingAnchors();
}

//  void QQuickBasePositioner::positionItem(qreal x, qreal y, PositionedItem
//      *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner12positionItemEddPNS_14PositionedItemE(
    QQuickBasePositioner *self,
    qreal x,
    qreal y,
    QQuickBasePositioner::PositionedItem *target) {
  self->positionItem(x, y, target);
}

//  void QQuickBasePositioner::positionItemX(qreal a0, PositionedItem
//      *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner13positionItemXEdPNS_14PositionedItemE(
    QQuickBasePositioner *self,
    qreal a0,
    QQuickBasePositioner::PositionedItem *target) {
  self->positionItemX(a0, target);
}

//  void QQuickBasePositioner::positionItemY(qreal a0, PositionedItem
//      *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickBasePositioner13positionItemYEdPNS_14PositionedItemE(
    QQuickBasePositioner *self,
    qreal a0,
    QQuickBasePositioner::PositionedItem *target) {
  self->positionItemY(a0, target);
}

//  QQuickBasePositionerPrivate *QQuickBasePositioner::d_func()
extern "C" Q_DECL_EXPORT
QQuickBasePositionerPrivate *ritual_ZN20QQuickBasePositioner6d_funcEv(
    QQuickBasePositioner *self) {
  return self->d_func();
}

//  const QQuickBasePositionerPrivate *QQuickBasePositioner::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickBasePositionerPrivate *ritual_ZNK20QQuickBasePositioner6d_funcEv(
    const QQuickBasePositioner *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickBasePositioner, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBasePositioner(
    QQuickBasePositioner *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBasePositioner *>(self)->take(key, call);
}

//  void QQuickBasePositioner::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickBasePositioner17componentCompleteEv(
    QQuickBasePositioner *self) {
  static_cast<OwnQQuickBasePositioner *>(self)->OwnQQuickBasePositioner::componentComplete();
}

//  void QQuickBasePositioner::itemChange(ItemChange a0, const ItemChangeData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickBasePositioner10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickBasePositioner *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  static_cast<OwnQQuickBasePositioner *>(self)->OwnQQuickBasePositioner::itemChange(
      a0,
      *a1);
}

//  void QQuickBasePositioner::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickBasePositioner12updatePolishEv(
    QQuickBasePositioner *self) {
  static_cast<OwnQQuickBasePositioner *>(self)->OwnQQuickBasePositioner::updatePolish();
}

#endif  // QT_CONFIG(quick_positioners)
#endif  // QT_CONFIG(quick_positioners)
