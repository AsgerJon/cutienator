//  Written by dev_tooling.RitualGenerator from the records of QtLocation/6.1
//  2.0/QtLocation/private/qdeclarativegeomapcopyrightsnotice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapcopyrightsnotice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDeclarativeGeoMapCopyrightNotice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeGeoMapCopyrightNotice : QDeclarativeGeoMapCopyrightNotice {
  using QDeclarativeGeoMapCopyrightNotice::paint;
  using QDeclarativeGeoMapCopyrightNotice::mousePressEvent;
  using QDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent;
};

//  A QDeclarativeGeoMapCopyrightNotice that Python can take functions over in. Every QDeclarativeGeoMapCopyrightNotice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall0)(const void *, QPainter *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall1)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall2)(const void *, QMouseEvent *, int *);
typedef bool (*CuteQDeclarativeGeoMapCopyrightNoticeCall3)(const void *, int *);
typedef void * (*CuteQDeclarativeGeoMapCopyrightNoticeCall4)(const void *, int *);
typedef void * (*CuteQDeclarativeGeoMapCopyrightNoticeCall5)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall6)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall7)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapCopyrightNoticeCall8)(const void *, int *);
typedef const QRectF * (*CuteQDeclarativeGeoMapCopyrightNoticeCall9)(const void *, int *);
typedef bool (*CuteQDeclarativeGeoMapCopyrightNoticeCall10)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQDeclarativeGeoMapCopyrightNoticeCall11)(const void *, int, int *);
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapCopyrightNoticeCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall13)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall14)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall15)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall17)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall18)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall23)(const void *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQDeclarativeGeoMapCopyrightNoticeCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoMapCopyrightNoticeCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoMapCopyrightNoticeCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoMapCopyrightNotice : public QDeclarativeGeoMapCopyrightNotice {
public:
  using QDeclarativeGeoMapCopyrightNotice::QDeclarativeGeoMapCopyrightNotice;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickPaintedItem5paintEP8QPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
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
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
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

  //  void QDeclarativeGeoMapCopyrightNotice::paint(QPainter *painter)
  void paint(QPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall0 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapCopyrightNotice::paint(painter);
  }

  //  void QDeclarativeGeoMapCopyrightNotice::mousePressEvent(QMouseEvent
  //      *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall1 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapCopyrightNotice::mousePressEvent(event);
  }

  //  void QDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent(QMouseEvent
  //      *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall2 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent(event);
  }

  //  bool QQuickPaintedItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall3 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPaintedItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickPaintedItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall4 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickPaintedItem::textureProvider();
  }

  //  QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall5 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall5>(taken[5]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickPaintedItem::updatePaintNode(a0, a1);
  }

  //  void QQuickPaintedItem::releaseResources()
  void releaseResources() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall6 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::releaseResources();
  }

  //  void QQuickPaintedItem::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall7 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall7>(taken[7]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::itemChange(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall8 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall9 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall10 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall10>(taken[10]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall11 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall11>(taken[11]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall12 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall12>(taken[12]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall13 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall13>(taken[13]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[14]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall14 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall15 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall16 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall17 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall17>(taken[17]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall18 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall18>(taken[18]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall19 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall20 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall21 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall22 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall23 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall24 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall24>(taken[24]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall25 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall25>(taken[25]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall26 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall27 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall28 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall29 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall29>(taken[29]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall30 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall30>(taken[30]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall31 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall31>(taken[31]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall32 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall32>(taken[32]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall33 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall33>(taken[33]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall34 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativeGeoMapCopyrightNoticeCall35 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall35>(taken[35]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall36 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall36>(taken[36]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall37 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall37>(taken[37]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall38 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall38>(taken[38]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall39 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall39>(taken[39]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall40 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall40>(taken[40]);
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
      CuteQDeclarativeGeoMapCopyrightNoticeCall41 call = reinterpret_cast<CuteQDeclarativeGeoMapCopyrightNoticeCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoMapCopyrightNotice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QDeclarativeGeoMapCopyrightNotice10metaObjectEv(
    const QDeclarativeGeoMapCopyrightNotice *self) {
  return self->metaObject();
}

//  QString QDeclarativeGeoMapCopyrightNotice::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QDeclarativeGeoMapCopyrightNotice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoMapCopyrightNotice::tr(s, c, n));
}

//  QDeclarativeGeoMapCopyrightNotice::QDeclarativeGeoMapCopyrightNotice(QQui
//      ckItem *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapCopyrightNotice *ritual_ZN33QDeclarativeGeoMapCopyrightNoticeC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQDeclarativeGeoMapCopyrightNotice(parent);
}

//  QDeclarativeGeoMapCopyrightNotice::~QDeclarativeGeoMapCopyrightNotice()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNoticeD1Ev(
    QDeclarativeGeoMapCopyrightNotice *self) {
  delete self;
}

//  void QDeclarativeGeoMapCopyrightNotice::setCopyrightsZ(qreal copyrightsZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice14setCopyrightsZEd(
    QDeclarativeGeoMapCopyrightNotice *self,
    qreal copyrightsZ) {
  self->setCopyrightsZ(copyrightsZ);
}

//  void QDeclarativeGeoMapCopyrightNotice::setCopyrightsVisible(bool
//      visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice20setCopyrightsVisibleEb(
    QDeclarativeGeoMapCopyrightNotice *self,
    bool visible) {
  self->setCopyrightsVisible(visible);
}

//  bool QDeclarativeGeoMapCopyrightNotice::copyrightsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QDeclarativeGeoMapCopyrightNotice17copyrightsVisibleEv(
    const QDeclarativeGeoMapCopyrightNotice *self) {
  return self->copyrightsVisible();
}

//  void QDeclarativeGeoMapCopyrightNotice::anchorToBottomLeft()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice18anchorToBottomLeftEv(
    QDeclarativeGeoMapCopyrightNotice *self) {
  self->anchorToBottomLeft();
}

//  void QDeclarativeGeoMapCopyrightNotice::setMapSource(QDeclarativeGeoMap
//      *mapSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice12setMapSourceEP18QDeclarativeGeoMap(
    QDeclarativeGeoMapCopyrightNotice *self,
    QDeclarativeGeoMap *mapSource) {
  self->setMapSource(mapSource);
}

//  QDeclarativeGeoMap *QDeclarativeGeoMapCopyrightNotice::mapSource()
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMap *ritual_ZN33QDeclarativeGeoMapCopyrightNotice9mapSourceEv(
    QDeclarativeGeoMapCopyrightNotice *self) {
  return self->mapSource();
}

//  QString QDeclarativeGeoMapCopyrightNotice::styleSheet() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QDeclarativeGeoMapCopyrightNotice10styleSheetEv(
    const QDeclarativeGeoMapCopyrightNotice *self) {
  return new QString(self->styleSheet());
}

//  void QDeclarativeGeoMapCopyrightNotice::setStyleSheet(const QString
//      &styleSheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice13setStyleSheetERK7QString(
    QDeclarativeGeoMapCopyrightNotice *self,
    const QString *styleSheet) {
  self->setStyleSheet(*styleSheet);
}

//  void QDeclarativeGeoMapCopyrightNotice::copyrightsImageChanged(const
//      QImage &copyrightsImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice22copyrightsImageChangedERK6QImage(
    QDeclarativeGeoMapCopyrightNotice *self,
    const QImage *copyrightsImage) {
  self->copyrightsImageChanged(*copyrightsImage);
}

//  void QDeclarativeGeoMapCopyrightNotice::copyrightsChanged(const QString
//      &copyrightsHtml)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice17copyrightsChangedERK7QString(
    QDeclarativeGeoMapCopyrightNotice *self,
    const QString *copyrightsHtml) {
  self->copyrightsChanged(*copyrightsHtml);
}

//  void
//      QDeclarativeGeoMapCopyrightNotice::onCopyrightsStyleSheetChanged(cons
//      t QString &styleSheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice29onCopyrightsStyleSheetChangedERK7QString(
    QDeclarativeGeoMapCopyrightNotice *self,
    const QString *styleSheet) {
  self->onCopyrightsStyleSheetChanged(*styleSheet);
}

//  void QDeclarativeGeoMapCopyrightNotice::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice5paintEP8QPainter(
    QDeclarativeGeoMapCopyrightNotice *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QDeclarativeGeoMapCopyrightNotice::mousePressEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice15mousePressEventEP11QMouseEvent(
    QDeclarativeGeoMapCopyrightNotice *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice17mouseReleaseEventEP11QMouseEvent(
    QDeclarativeGeoMapCopyrightNotice *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QDeclarativeGeoMapCopyrightNotice::rasterizeHtmlAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice22rasterizeHtmlAndUpdateEv(
    QDeclarativeGeoMapCopyrightNotice *self) {
  self->rasterizeHtmlAndUpdate();
}

//  void QDeclarativeGeoMapCopyrightNotice::connectMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice10connectMapEv(
    QDeclarativeGeoMapCopyrightNotice *self) {
  self->connectMap();
}

//  void QDeclarativeGeoMapCopyrightNotice::createCopyright()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeGeoMapCopyrightNotice15createCopyrightEv(
    QDeclarativeGeoMapCopyrightNotice *self) {
  self->createCopyright();
}

//  a Python function taken by a CuteQDeclarativeGeoMapCopyrightNotice, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoMapCopyrightNotice(
    QDeclarativeGeoMapCopyrightNotice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoMapCopyrightNotice *>(self)->take(key, call);
}

//  void QDeclarativeGeoMapCopyrightNotice::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN33QDeclarativeGeoMapCopyrightNotice5paintEP8QPainter(
    QDeclarativeGeoMapCopyrightNotice *self,
    QPainter *painter) {
  static_cast<OwnQDeclarativeGeoMapCopyrightNotice *>(self)->OwnQDeclarativeGeoMapCopyrightNotice::paint(
      painter);
}

//  void QDeclarativeGeoMapCopyrightNotice::mousePressEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN33QDeclarativeGeoMapCopyrightNotice15mousePressEventEP11QMouseEvent(
    QDeclarativeGeoMapCopyrightNotice *self,
    QMouseEvent *event) {
  static_cast<OwnQDeclarativeGeoMapCopyrightNotice *>(self)->OwnQDeclarativeGeoMapCopyrightNotice::mousePressEvent(
      event);
}

//  void QDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN33QDeclarativeGeoMapCopyrightNotice17mouseReleaseEventEP11QMouseEvent(
    QDeclarativeGeoMapCopyrightNotice *self,
    QMouseEvent *event) {
  static_cast<OwnQDeclarativeGeoMapCopyrightNotice *>(self)->OwnQDeclarativeGeoMapCopyrightNotice::mouseReleaseEvent(
      event);
}
